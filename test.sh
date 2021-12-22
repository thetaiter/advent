#!/bin/bash -e

declare -a parts
failed_tests=false
template="helpers/template.py"
parts=( $(find . -type f -name 'part*.py' | sort) )

function run_test() {
    local part="${1}"

    echo "Running ${part}"

    if diff -q "${part}" "${template}" > /dev/null
    then
        echo "File matches template, skipping"
        return
    fi

    local result
    result="$(python3 "${part}")"
    if [ "${?}" -ne 0 ]
    then
        echo "There as an error with script \`${part}\`" >&2
        failed_tests=true
    else
        local answer
        local answers=( $(grep 'Your puzzle answer was' "$(dirname "${part}")/README.md" | cut -d' ' -f5 | cut -d\` -f2) )
        result="$(echo "${result}" | head -n 1)"

        if [[ "${part}" == *'part1'* ]]
        then
            answer="${answers[0]}"
        else
            answer="${answers[1]}"
        fi

        if [[ "${answer}" == *'_'* ]]
        then
            echo "Answer has not yet been set for \`${part}\`, marking as failed" >&2
            echo "Failed :(" >&2
            failed_tests=true
            return
        fi

        if [ "${result}" -eq "${answer}" ]
        then
            echo 'Passed :)'
        else
            echo 'Failed :(' >&2
            echo "Your answer was \`${result}\` but the answer should be \`${answer}\`" >&2
            failed_tests=true
        fi
    fi
}

for part in "${parts[@]}"
do
    run_test "${part}"
done

if [ "${failed_tests}" = true ]
then
    echo 'There were test failures...' >&2
    exit 2
else
    echo 'All tests passed!'
fi