#!/bin/bash

FULL_REPORT=README.md
rm ${FULL_REPORT}

docker-compose down
docker-compose up --build -d

sleep 2

cat template.md >> ${FULL_REPORT}
echo "" >> ${FULL_REPORT}
echo "> Last run: $(date)" >> ${FULL_REPORT}
for FILE in $(find report/markdown -name "*.md" | sort -V)
do
    NAME=$(basename -- ${FILE} .md)
    echo "" >> ${FULL_REPORT}
    cat ${FILE} >> ${FULL_REPORT}
    echo "" >> ${FULL_REPORT}
done

sleep 2

# Clean Up
docker-compose down
docker system prune -f