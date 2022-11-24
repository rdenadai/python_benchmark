import psycopg2


def main():
    # Connect to your postgres DB
    with psycopg2.connect(host="postgres", dbname="benchmark", user="postgres", password="password") as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            # Execute a query
            cur.execute("SELECT * FROM my_data")
            # Retrieve query results
            records = cur.fetchall()


if __name__ == "__main__":
    raise SystemError(main())
