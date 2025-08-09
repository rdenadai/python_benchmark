# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13, 3.14

from psycopg2 import connect
from psycopg2.extras import RealDictCursor


def main():
    # Connect to your postgres DB
    with connect(host="postgres", dbname="benchmark", user="postgres", password="password") as conn:
        # Open a cursor to perform database operations
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            # Execute a query
            cur.execute(
                """
                SELECT 
                    CONCAT(e.first_name, ' ',  e.last_name) as name,
                    e.email,
                    e.phone_number,
                    e.hire_date,
                    j.job_title,
                    j.min_salary,
                    j.max_salary
                FROM employees AS e
                INNER JOIN jobs AS j ON e.job_id = j.job_id
                """
            )
            # Retrieve query results
            records = cur.fetchall()
    for record in records:
        name, email = record.get("name"), record.get("email")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
