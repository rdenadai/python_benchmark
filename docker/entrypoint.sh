#!/bin/bash

i=0
for FILE in $(find src/ -name "*.py")
do
    echo "--------------------"
    echo "Running $FILE"

    DONT_RUN=$(grep -rnw "${FILE}" -e "@DONT_RUN")
    ALLOWED_PYTHON=$(grep -rnw "${FILE}" -e "@ALLOWED_VERSIONS")
    ALLOWED_PYTHON_VERSION=$(echo $ALLOWED_PYTHON | grep "${PY_VERSION}")
    MPROF_INTERVAL=$(cat ${FILE} | grep -e "@MPROF_INTERVAL" | sed 's/# @MPROF_INTERVAL: //')
    MPROF_INTERVAL=${MPROF_INTERVAL:="0.01"}
    MPROF_MULTIPROCESS=$(cat ${FILE} | grep -e "@MPROF_MULTIPROCESS" | sed 's/# @MPROF_MULTIPROCESS: //')
    MPROF_MULTIPROCESS=${MPROF_MULTIPROCESS:="-C"}

    if [ -z "$DONT_RUN" ]
    then
        if [ -z "$ALLOWED_PYTHON" ] || [ -z "$ALLOWED_PYTHON_VERSION" ]
        then
            echo "Python ${PY_VERSION} version not allowed in $FILE"
            echo "{\"results\": [{\"command\": \"${FILE}\"}]}" > report/tmp/${i}part_${PY_VERSION}.json
        else
            # Performance
            hyperfine --show-output --export-json report/tmp/${i}part_${PY_VERSION}.json --runs 10 --warmup 3 "python ${FILE}"
            # Memory
            for k in {1..10}; do
                mprof run ${MPROF_MULTIPROCESS} -T ${MPROF_INTERVAL} -o report/tmp/${i}_${k}part_${PY_VERSION}.dat ${FILE} &>/dev/null &
            done
            wait
            for k in {1..10}; do
                cat report/tmp/${i}_${k}part_${PY_VERSION}.dat | sed '/^CHLD/ d' > report/tmp/${i}_${k}part_${PY_VERSION}_parcial.dat
                mv report/tmp/${i}_${k}part_${PY_VERSION}_parcial.dat report/tmp/${i}_${k}part_${PY_VERSION}.dat
            done
        fi
        ((i=i+1))
    else
        echo "Skipping $FILE"
    fi
done

python -m report ${PY_VERSION}
sleep 1

rm report/tmp/*.json &
rm report/tmp/*.dat &
sleep 2