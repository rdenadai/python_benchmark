# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13, 3.14

# The Computer Language Benchmarks Game
# https://salsa.debian.org/benchmarksgame-team/benchmarksgame/
#
# Contributed by Sebastien Loisel
# Fixed by Isaac Gouy
# Sped up by Josh Goldfoot
# Dirtily sped up by Simon Descarpentries
# Used list comprehension by Vadim Zelenin
# Concurrency by Jason Stitt
# Concurrency simplified by Matt Vollrath
# Optimized math by Adam Beckmeyer


from itertools import repeat
from math import sqrt
from multiprocessing import Pool, cpu_count


def eval_A(i, j):
    ij = i + j
    return ij * (ij + 1) // 2 + i + 1


def A_sum(u, i):
    return sum(u_j / eval_A(i, j) for j, u_j in enumerate(u))


def At_sum(u, i):
    return sum(u_j / eval_A(j, i) for j, u_j in enumerate(u))


def multiply_AtAv(u, pool):
    r = range(len(u))
    tmp = pool.starmap(A_sum, zip(repeat(u), r))
    return pool.starmap(At_sum, zip(repeat(tmp), r))


def main(n):
    u = [1] * n

    with Pool(processes=cpu_count()) as pool:
        for _ in range(10):
            v = multiply_AtAv(u, pool)
            u = multiply_AtAv(v, pool)

    vBv = vv = 0

    for ue, ve in zip(u, v):
        vBv += ue * ve
        vv += ve * ve

    result = sqrt(vBv / vv)
    assert float(f"{result:.9f}") == 1.274223986


if __name__ == "__main__":
    raise SystemExit(main(300))
