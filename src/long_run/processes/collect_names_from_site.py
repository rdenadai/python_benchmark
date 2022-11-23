# @MPROF_INTERVAL: 0.1
# @MPROF_MULTIPROCESS: -M
# @ALLOWED_VERSIONS: 3.8, 3.9, 3.10, 3.11

import asyncio
import gc
import sys
from concurrent.futures import ProcessPoolExecutor
from enum import Enum
from functools import partial, wraps
from itertools import chain
from multiprocessing import cpu_count
from typing import List

import uvloop
from bs4 import BeautifulSoup as bsoup
from httpx import AsyncClient, Response


class Sex(str, Enum):
    M = "nomes-masculinos"
    F = "nomes-femininos"


def run_in_executor(_func):
    @wraps(_func)
    def wrapped(*args, **kwargs):
        loop = asyncio.get_event_loop()
        func = partial(_func, *args, **kwargs)
        return loop.run_in_executor(executor=None, func=func)

    return wrapped


async def fetch(url: str) -> Response:
    async with AsyncClient() as client:
        return await client.get(url, follow_redirects=True)


@run_in_executor
def save_names(filename: str, names: List[str]):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(names))


def parse_names(response: Response, name_size: int = 7) -> List[str]:
    parser = bsoup(response.text, "lxml")
    links = parser.find_all("span", class_="list-wide--name full-w")
    return [name for link in links if len(name := link.string.strip()) == name_size]


async def get_names(sex: str = Sex.M, name_size: int = 7, pages: int = 150) -> List[str]:
    names: List[str] = []

    urls = (f"https://www.dicionariodenomesproprios.com.br/{sex}/{i}" for i in range(1, pages + 1))
    responses = await asyncio.gather(*[fetch(url) for url in urls])
    with ProcessPoolExecutor(max_workers=cpu_count() * 2) as exc:
        names = sorted(chain(*exc.map(partial(parse_names, name_size=name_size), responses, chunksize=5)))

    return names


async def main():
    task_m = get_names(sex=Sex.M, pages=5)
    task_f = get_names(sex=Sex.F, pages=5)
    response = await asyncio.gather(*[task_m, task_f])

    names_m, names_f = response

    save_m = save_names("nomes_masculinos.txt", names_m)
    save_f = save_names("nomes_femininos.txt", names_f)
    await asyncio.gather(*[save_m, save_f])


if __name__ == "__main__":
    try:
        print("Iniciando rotina...")
        gc.set_threshold(7_000, 100, 100)
        gc.freeze()

        if sys.version_info >= (3, 11):
            with asyncio.Runner(loop_factory=uvloop.new_event_loop) as runner:
                runner.run(main())
        else:
            uvloop.install()
            asyncio.run(main())
    except KeyboardInterrupt:
        ...
    raise SystemExit(0)
