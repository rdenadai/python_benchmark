#!/bin/bash

echo "Starting benchmark"
start=`date +%s`

FULL_REPORT=README.md
rm ${FULL_REPORT} &>/dev/null &

echo "Cleaning up previous docker containers and images"
docker compose down &>/dev/null
echo "Building Docker images"
docker compose up --build -d &>/dev/null
sleep 2

echo "Running aggregate report script"
if [[ "$(python3 -V)" =~ "Python 3" ]]; then
    python3 src/support/report_aggregate.py
else
	python src/support/report_aggregate.py
fi

echo "Generating markdown report"
cat src/support/template.md >> ${FULL_REPORT}
echo "" >> ${FULL_REPORT}
echo "> Last run: $(date)" >> ${FULL_REPORT}
cat src/support/compare.md >> ${FULL_REPORT}
echo "" >> ${FULL_REPORT}
echo "---" >> ${FULL_REPORT}
echo "" >> ${FULL_REPORT}
for FILE in $(find report/markdown -name "*.md" | sort -V)
do
    NAME=$(basename -- ${FILE} .md)
    echo "" >> ${FULL_REPORT}
    cat ${FILE} >> ${FULL_REPORT}
    echo "" >> ${FULL_REPORT}
done

rm src/support/compare.md

# Clean Up
echo "Cleaning up temporary files"
sleep 2
for k in {6..13}; do
    docker logs python_performance_python3${k}_1  >& report/logs/python_performance_python3${k}.log
done
docker compose down &>/dev/null
docker system prune -f &>/dev/null

end=`date +%s`
runtime=$((end-start))
echo "Total time: ${runtime} seconds"
