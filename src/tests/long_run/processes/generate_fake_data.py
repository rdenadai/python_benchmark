"""Runs in multiple processes the generation of 10.000 fake data (using Faker) and save into a csv (using pandas)."""

# @MPROF_INTERVAL: 0.1
# @MPROF_MULTIPROCESS: -M
# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12

from concurrent.futures import ProcessPoolExecutor
from functools import partial
from gc import set_threshold
from multiprocessing import cpu_count
from random import randint
from uuid import uuid4

import pandas as pd
from faker import Faker


def generate_item(fake, num):
    return (
        str(uuid4()),
        randint(0, 1_000_000) + num,
        fake.name(),
        fake.job(),
        fake.address().replace("\n", ""),
        fake.company(),
        fake.credit_card_provider(),
        fake.credit_card_number(),
        *fake.latlng(),
    )


def main():
    fake = Faker("pt_BR")

    with ProcessPoolExecutor(max_workers=cpu_count() * 2) as exc:
        items = exc.map(partial(generate_item, fake), range(1_000), chunksize=100)

        dataframe = pd.DataFrame(
            items,
            columns=(
                "uid",
                "registration",
                "name",
                "job",
                "address",
                "company",
                "credit_card_provider",
                "credit_card_number",
                "lat",
                "lng",
            ),
        )
        dataframe.to_csv("generated_data.csv", index=False)


if __name__ == "__main__":
    set_threshold(100_000, 1000, 1000)
    raise SystemExit(main())
