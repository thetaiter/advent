#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NO_COLOR='\033[0m'
NEWLINE=true

num_failed=0
num_skipped=0
num_passed=0

template="helpers/template.py"
parts=( $(find . -type f -name 'part*.py' | sort) )

function print() {
    local level="${1}"
    local text="${2}"
    local fd=1
    local newline_char="\n"

    if [ "${NEWLINE}" = false ]
    then
        newline_char=''
    fi

    if [[ "${level}" != 'INFO' ]]
    then
        fd=2
    fi

    printf -- "[%s] %-7s %s${newline_char}" "$(date +"%Y-%m-%d %H:%M:%S")" "(${level})" "${text}" >&${fd}
}

function log() {
    local level="${1}"
    local text="${2}"

    while IFS= read -r line
    do
        print "${level}" "${line}"
    done <<<"$(printf -- "${text}")"

    while [[ "${text}" == *'\n' ]]
    do
        print "${level}"
        text="${text%'\n'}"
    done
}

function info() {
    log 'INFO' "${1}"
}

function warn() {
    log 'WARN' "${1}" 3
}

function error() {
    log 'ERROR' "${1}"
}

function run_test() {
    local part="${1}"
    local test_failed=false
    local test_skipped=false
    local failure_message=''
    local skipped_message=''

    NEWLINE=false info "Running ${part}..."

    if diff -q "${part}" "${template}" > /dev/null
    then
        skipped_message="File matches template"
        test_skipped=true
    else
        local answer
        local answers=( $(grep 'Your puzzle answer was' "$(dirname "${part}")/README.md" | cut -d' ' -f5 | cut -d\` -f2) )

        if [[ "${part}" == *'part1'* ]]
        then
            answer="${answers[0]}"
        else
            answer="${answers[1]}"
        fi

        if [[ "${answer}" == *'_'* ]]
        then
            skipped_message="File \`${part}\` does not match template, but answer has not yet been set"
            test_skipped=true
        else
            local result
            set +e
            result="$(python3 "${part}" 2>&1)"
            local err_code="${?}"
            set -e

            if [ "${err_code}" -ne 0 ]
            then
                failure_message="${result}"
                test_failed=true
            else
                result="$(echo "${result}" | head -n 1)"
                if ! [ "${result}" -eq "${answer}" ]
                then
                    failure_message="Your answer was \`${result}\` but the answer should be \`${answer}\`"
                    test_failed=true
                fi
            fi
        fi
    fi

    if [ "${test_failed}" = true ]
    then
        printf -- "${RED}Failed :(${NO_COLOR}\n"
        error "${failure_message}"
        num_failed=$((num_failed+1))
    elif [ "${test_skipped}" = true ]
    then
        printf -- "${YELLOW}Skipped :|${NO_COLOR}\n"
        warn "${skipped_message}"
        num_skipped=$((num_skipped+1))
    else
        printf -- "${GREEN}Passed :)${NO_COLOR}\n"
        num_passed=$((num_passed+1))
    fi
}

function run_tests() {
    info "Running tests"

    for part in "${parts[@]}"
    do
        run_test "${part}"
    done

    info "\nTests completed successfully\n"
}

function print_results() {
    local total_tests="$((num_failed + num_skipped + num_passed))"
    local percent_failed="$(echo "${num_failed}/${total_tests}*100" | bc -l)"
    local percent_skipped="$(echo "${num_skipped}/${total_tests}*100" | bc -l)"
    local percent_passed="$(echo "${num_passed}/${total_tests}*100" | bc -l)"

    info "Out of ${total_tests} total tests:\n"
    info "$(printf -- "${RED}%3s (%.4g%%%%)${NO_COLOR} failed\n" "${num_failed}" "${percent_failed}")"
    info "$(printf -- "${YELLOW}%3s (%.4g%%%%)${NO_COLOR} skipped\n" "${num_skipped}" "${percent_skipped}")"
    info "$(printf -- "${GREEN}%3s (%.4g%%%%)${NO_COLOR} passed\n" "${num_passed}" "${percent_passed}")\n"
}

run_tests
print_results
