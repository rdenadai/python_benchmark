#!/bin/bash

echo "Starting benchmark"
start=`date +%s`

FULL_REPORT=README.md
rm ${FULL_REPORT} &>/dev/null &

docker-compose down &>/dev/null
docker-compose up --build -d &>/dev/null

sleep 2

python support/report_aggregate.py

cat support/template.md >> ${FULL_REPORT}
echo "" >> ${FULL_REPORT}
echo "> Last run: $(date)" >> ${FULL_REPORT}
cat support/compare.md >> ${FULL_REPORT}
for FILE in $(find report/markdown -name "*.md" | sort -V)
do
    NAME=$(basename -- ${FILE} .md)
    echo "" >> ${FULL_REPORT}
    cat ${FILE} >> ${FULL_REPORT}
    echo "" >> ${FULL_REPORT}
done

rm support/compare.md

sleep 2

# Clean Up
docker-compose down &>/dev/null
docker system prune -f &>/dev/null

end=`date +%s`
runtime=$((end-start))
echo "Total time: ${runtime} seconds"