# Python Benchmark

This is a simple repo to validate and test any (almost any) python program againts all python 3 versions.
 - Python 3.6.15
 - Python 3.7.15
 - Python 3.8.15
 - Python 3.9.15
 - Python 3.10.8
 - Python 3.11.0

## Should i care about it

Yes!! ... No ... it depends ... 

> “The real problem is that programmers have spent far too much time worrying about efficiency in the wrong places and at the wrong times; premature optimization is the root of all evil (or at least most of it) in programming.”. Donald Knuth

I love to test and check to see if my programs run faster and / or have a small memory footprint, and that's why i realize: "Why not to write a simple benchmark suite".

Here you find small bits of python code test against major python 3 versions ...

## Dependencies

To run the full tests, please keep in mind the you need **docker** (and docker-compose) installed in the environment.

All the tests run inside a docker container image based on each python version described above.

Since python libs have different behaviors and support versions, inside the **docker/** folder there's a requirements99.txt versioning number.

You also need python installed because of the **src/support/report_aggragete.py** program (it will run at the end of the benchmark.sh bash script).

## How to run

To run the full suite, just type in:

```bash
$> ./benchmarh.sh
```

Results will be write down on the main README.md file (it's partiallys regenerated at each run).

To benchmark a new program, simple put it inside de **src/tests/** folder.

Please also check this metadata tags to put inside the program to be able to change some aspects of execution.

```python
# @DONT_RUN
# @MPROF_INTERVAL: 0.1
# @MPROF_MULTIPROCESS: -M
# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11
```

 - @DONT_RUN: This file should not be executed (in case of utils routines);
 - @MPROF_INTERVAL: To benchmark memory usage mprof is used, this param you maybe able to improve interval collect of memory;
 - @MPROF_MULTIPROCESS: In case your program uses python multiprocess (possible params -M or -C, default: -C);
 - @ALLOWED_VERSIONS: What python versions your program can be run: from 3.6 to 3.11;

## Results
> Last run: Tue Nov 29 12:39:06 PM -03 2022
### **Comparison**

#### How much faster 3.11 is? (Mean / Median from 3.6 to 3.10)
| Command | 3.6 (Mean / Median) | 3.7 (...) | 3.8 (...) | 3.9 (...) | 3.10 (...) |
|:---|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 12.03% / 13.46% | -8.81% / -7.30% | 0.17% / 1.85% | 11.85% / 12.90% | 6.72% / 7.42% |
| `algorithm/twosum/twosum_naive.py` | 13.29% / 12.46% | -7.93% / -8.99% | 1.39% / 0.52% | 11.82% / 11.02% | 8.22% / 5.07% |
| `complex/classes/classes.py` | 91.01% / 97.24% | 59.81% / 64.37% | 68.24% / 72.65% | 78.00% / 83.52% | 68.93% / 73.90% |
| `complex/classes/dataclasses_.py` | -- / -- | -10.84% / -10.70% | -4.34% / -4.22% | 14.11% / 14.11% | 7.75% / 7.80% |
| `complex/classes/namedtuple_classes.py` | 18.38% / 17.58% | -1.67% / -2.55% | 3.42% / 3.30% | 15.12% / 14.68% | 7.43% / 6.82% |
| `complex/classes/simplenamespace.py` | 147.13% / 147.67% | 59.45% / 60.13% | 71.85% / 66.76% | 91.50% / 85.61% | 72.18% / 72.26% |
| `complex/classes/sloted_classes.py` | 125.09% / 124.69% | 89.09% / 88.45% | 98.57% / 98.16% | 112.19% / 111.76% | 99.39% / 99.54% |
| `dummy/dummy.py` | 82.97% / 71.32% | 57.17% / 32.10% | 52.05% / 42.38% | 66.44% / 56.30% | 68.35% / 55.51% |
| `long_run/database/postgresql.py` | 3.64% / 3.28% | -7.81% / -7.64% | 0.78% / 1.03% | 9.63% / 9.68% | 1.91% / 2.11% |
| `long_run/database/sqlite_.py` | 4.89% / 4.95% | -10.13% / -9.95% | -0.39% / -0.37% | 4.59% / 4.78% | 0.38% / 0.57% |
| `long_run/file/load_titanic_csv_pandas.py` | 14.78% / 15.00% | -6.53% / -6.41% | 2.42% / 2.38% | 8.45% / 8.23% | 2.50% / 2.49% |
| `long_run/file/load_titanic_csv_python.py` | 24.66% / 25.04% | 11.22% / 11.04% | 18.91% / 18.89% | 29.38% / 29.54% | 23.07% / 19.43% |
| `long_run/processes/collect_names_from_site.py` | -- / -- | -- / -- | 16.92% / 17.11% | 11.16% / 16.12% | 4.83% / 7.06% |
| `long_run/processes/generate_fake_data.py` | 9.22% / 8.57% | -3.76% / -4.32% | 0.03% / -0.02% | 6.80% / 6.13% | 1.29% / 0.44% |
| `math/haversine.py` | 30.56% / 29.55% | 26.43% / 25.31% | 11.97% / 10.95% | 26.25% / 25.32% | 15.75% / 15.13% |
| `math/mandelbrot.py` | -0.41% / -0.31% | -1.12% / -0.92% | 0.29% / 0.16% | 1.74% / 0.64% | 1.19% / 0.23% |
| `math/pow_simple.py` | 40.95% / 41.27% | 33.12% / 32.60% | 32.08% / 32.34% | 30.83% / 31.31% | 25.28% / 25.12% |
| `math/pow_using_math.py` | 35.23% / 36.55% | 21.85% / 22.58% | 13.84% / 13.18% | 20.31% / 19.19% | 15.69% / 15.01% |
| `modules/json/json_module.py` | 46.82% / 46.57% | 35.66% / 35.23% | 25.97% / 26.05% | 30.25% / 29.86% | 17.53% / 17.30% |
| `modules/json/orjson_module.py` | 52.80% / 53.28% | 17.69% / 17.53% | 23.63% / 23.32% | 37.83% / 37.23% | 24.17% / 24.28% |
---

#### How much more memory 3.11 uses? (Memory from 3.6 to 3.10)
| Command |  3.6 | 3.7 | 3.8 | 3.9 | 3.10 |
|:---|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 15.73% | 29.66% | 26.36% | 20.22% | 17.78% |
| `algorithm/twosum/twosum_naive.py` | 15.18% | 29.25% | 25.06% | 14.86% | 11.05% |
| `complex/classes/classes.py` | 24.01% | 36.3% | 32.03% | 25.98% | 16.78% |
| `complex/classes/dataclasses_.py` | -- | 36.31% | 32.17% | 19.51% | 16.65% |
| `complex/classes/namedtuple_classes.py` | 18.27% | 30.58% | 29.43% | 15.77% | 10.44% |
| `complex/classes/simplenamespace.py` | 25.82% | 39.92% | 34.02% | 23.2% | 12.91% |
| `complex/classes/sloted_classes.py` | 23.01% | 35.44% | 30.73% | 20.53% | 11.43% |
| `dummy/dummy.py` | 18.39% | 29.64% | 26.01% | 13.7% | 13.82% |
| `long_run/database/postgresql.py` | 18.7% | 32.15% | 30.38% | 21.32% | 23.02% |
| `long_run/database/sqlite_.py` | 12.77% | 9.21% | 8.74% | 7.89% | 8.07% |
| `long_run/file/load_titanic_csv_pandas.py` | 12.32% | 9.14% | 8.51% | 6.75% | 8.75% |
| `long_run/file/load_titanic_csv_python.py` | 17.0% | 29.63% | 24.78% | 17.13% | 12.29% |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 5.73% | 4.84% | 4.61% |
| `long_run/processes/generate_fake_data.py` | 11.48% | 5.51% | 10.34% | 6.01% | 7.56% |
| `math/haversine.py` | 17.26% | 27.81% | 24.39% | 14.18% | 12.96% |
| `math/mandelbrot.py` | 6.23% | 12.19% | 10.84% | 9.21% | 7.66% |
| `math/pow_simple.py` | 17.59% | 28.63% | 24.06% | 13.85% | 14.46% |
| `math/pow_using_math.py` | 20.33% | 30.31% | 26.91% | 17.75% | 12.81% |
| `modules/json/json_module.py` | 19.32% | 23.8% | 23.19% | 20.19% | 17.25% |
| `modules/json/orjson_module.py` | 18.53% | 24.61% | 24.19% | 14.52% | 18.15% |
---

#### **Execution**

| Command |  Mean 3.6 [s] | Mean 3.7 [s] | Mean 3.8 [s] | Mean 3.9 [s] | Mean 3.10 [s] | Mean 3.11 [s] |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 0.0795 | 0.06471 | 0.07108 | 0.07937 | 0.07573 | 0.07096 |
| `algorithm/twosum/twosum_naive.py` | 0.08003 | 0.06504 | 0.07162 | 0.07899 | 0.07645 | 0.07064 |
| `complex/classes/classes.py` | 0.0442 | 0.03698 | 0.03893 | 0.04119 | 0.03909 | 0.02314 |
| `complex/classes/dataclasses_.py` | -- | 0.09566 | 0.10263 | 0.12243 | 0.1156 | 0.10729 |
| `complex/classes/namedtuple_classes.py` | 0.09215 | 0.07654 | 0.0805 | 0.08961 | 0.08362 | 0.07784 |
| `complex/classes/simplenamespace.py` | 0.05899 | 0.03806 | 0.04102 | 0.04571 | 0.0411 | 0.02387 |
| `complex/classes/sloted_classes.py` | 0.04396 | 0.03693 | 0.03878 | 0.04144 | 0.03894 | 0.01953 |
| `dummy/dummy.py` | 0.03255 | 0.02796 | 0.02705 | 0.02961 | 0.02995 | 0.01779 |
| `long_run/database/postgresql.py` | 0.14564 | 0.12954 | 0.14162 | 0.15405 | 0.1432 | 0.14052 |
| `long_run/database/sqlite_.py` | 0.58362 | 0.50001 | 0.55421 | 0.58194 | 0.55854 | 0.5564 |
| `long_run/file/load_titanic_csv_pandas.py` | 0.66847 | 0.54437 | 0.59646 | 0.63157 | 0.59693 | 0.58237 |
| `long_run/file/load_titanic_csv_python.py` | 0.06869 | 0.06128 | 0.06552 | 0.07129 | 0.06781 | 0.0551 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 3.68563 | 3.50393 | 3.30459 | 3.15225 |
| `long_run/processes/generate_fake_data.py` | 0.81595 | 0.71897 | 0.74727 | 0.79788 | 0.75671 | 0.74707 |
| `math/haversine.py` | 0.61437 | 0.59492 | 0.52688 | 0.59411 | 0.54467 | 0.47057 |
| `math/mandelbrot.py` | 14.89008 | 14.78379 | 14.9947 | 15.21169 | 15.13002 | 14.95167 |
| `math/pow_simple.py` | 0.44665 | 0.42185 | 0.41856 | 0.4146 | 0.397 | 0.31689 |
| `math/pow_using_math.py` | 1.58435 | 1.42762 | 1.33371 | 1.40951 | 1.35538 | 1.1716 |
| `modules/json/json_module.py` | 0.41144 | 0.38018 | 0.35303 | 0.36501 | 0.32937 | 0.28024 |
| `modules/json/orjson_module.py` | 0.26375 | 0.20314 | 0.2134 | 0.2379 | 0.21433 | 0.17261 |

| Command |  Median 3.6 [s] | Median 3.7 [s] | Median 3.8 [s] | Median 3.9 [s] | Median 3.10 [s] | Median 3.11 [s] |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 0.07916 | 0.06468 | 0.07106 | 0.07877 | 0.07495 | 0.06977 |
| `algorithm/twosum/twosum_naive.py` | 0.07979 | 0.06457 | 0.07132 | 0.07877 | 0.07455 | 0.07095 |
| `complex/classes/classes.py` | 0.04428 | 0.0369 | 0.03876 | 0.0412 | 0.03904 | 0.02245 |
| `complex/classes/dataclasses_.py` | -- | 0.09576 | 0.10271 | 0.12237 | 0.1156 | 0.10724 |
| `complex/classes/namedtuple_classes.py` | 0.09161 | 0.07592 | 0.08048 | 0.08935 | 0.08322 | 0.07791 |
| `complex/classes/simplenamespace.py` | 0.05902 | 0.03816 | 0.03974 | 0.04423 | 0.04105 | 0.02383 |
| `complex/classes/sloted_classes.py` | 0.04395 | 0.03686 | 0.03876 | 0.04142 | 0.03903 | 0.01956 |
| `dummy/dummy.py` | 0.0325 | 0.02506 | 0.02701 | 0.02965 | 0.0295 | 0.01897 |
| `long_run/database/postgresql.py` | 0.14491 | 0.12959 | 0.14176 | 0.15389 | 0.14327 | 0.14031 |
| `long_run/database/sqlite_.py` | 0.58286 | 0.50014 | 0.55334 | 0.58193 | 0.55854 | 0.55539 |
| `long_run/file/load_titanic_csv_pandas.py` | 0.66764 | 0.54338 | 0.59438 | 0.62839 | 0.59504 | 0.58058 |
| `long_run/file/load_titanic_csv_python.py` | 0.06886 | 0.06115 | 0.06547 | 0.07134 | 0.06577 | 0.05507 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 3.58295 | 3.55265 | 3.27545 | 3.05938 |
| `long_run/processes/generate_fake_data.py` | 0.81201 | 0.71562 | 0.74774 | 0.79378 | 0.7512 | 0.7479 |
| `math/haversine.py` | 0.61189 | 0.59185 | 0.52402 | 0.59188 | 0.54379 | 0.47231 |
| `math/mandelbrot.py` | 14.88607 | 14.79481 | 14.95654 | 15.02875 | 14.96732 | 14.93276 |
| `math/pow_simple.py` | 0.44488 | 0.41756 | 0.41676 | 0.4135 | 0.394 | 0.31491 |
| `math/pow_using_math.py` | 1.60033 | 1.43656 | 1.32649 | 1.39687 | 1.34783 | 1.17197 |
| `modules/json/json_module.py` | 0.41115 | 0.37934 | 0.35358 | 0.36427 | 0.32903 | 0.28051 |
| `modules/json/orjson_module.py` | 0.26435 | 0.20269 | 0.21268 | 0.23666 | 0.21434 | 0.17246 |

#### **Memory Usage**

| Command |  MEM 3.6 [MB] | MEM 3.7 [MB] | MEM 3.8 [MB] | MEM 3.9 [MB] | MEM 3.10 [MB] | MEM 3.11 [MB] |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 22.44922 | 20.0375 | 20.56016 | 21.61094 | 22.05703 | 25.97969 |
| `algorithm/twosum/twosum_naive.py` | 22.40273 | 19.96445 | 20.63398 | 22.4668 | 23.23633 | 25.8043 |
| `complex/classes/classes.py` | 21.96992 | 19.98867 | 20.63594 | 21.62656 | 23.3293 | 27.24492 |
| `complex/classes/dataclasses_.py` | -- | 20.03828 | 20.66641 | 22.85508 | 23.41602 | 27.31406 |
| `complex/classes/namedtuple_classes.py` | 22.29453 | 20.19258 | 20.37227 | 22.77695 | 23.87539 | 26.36797 |
| `complex/classes/simplenamespace.py` | 22.09961 | 19.87227 | 20.74687 | 22.56836 | 24.62539 | 27.80508 |
| `complex/classes/sloted_classes.py` | 22.06836 | 20.04414 | 20.76523 | 22.52266 | 24.36328 | 27.14688 |
| `dummy/dummy.py` | 21.79023 | 19.90039 | 20.47305 | 22.68867 | 22.66562 | 25.79805 |
| `long_run/database/postgresql.py` | 26.89297 | 24.15508 | 24.48242 | 26.31055 | 25.94805 | 31.92109 |
| `long_run/database/sqlite_.py` | 62.99492 | 65.04922 | 65.32969 | 65.84609 | 65.73672 | 71.04023 |
| `long_run/file/load_titanic_csv_pandas.py` | 61.88477 | 63.68477 | 64.05547 | 65.11328 | 63.91445 | 69.50859 |
| `long_run/file/load_titanic_csv_python.py` | 22.10391 | 19.95 | 20.72539 | 22.0793 | 23.03125 | 25.86172 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 44.71523 | 45.09766 | 45.19453 | 47.2793 |
| `long_run/processes/generate_fake_data.py` | 64.88125 | 68.55273 | 65.55117 | 68.22773 | 67.24727 | 72.32969 |
| `math/haversine.py` | 21.84336 | 20.03984 | 20.59102 | 22.43242 | 22.67461 | 25.6125 |
| `math/mandelbrot.py` | 36.45 | 34.51367 | 34.9332 | 35.45469 | 35.9668 | 38.72031 |
| `math/pow_simple.py` | 21.74727 | 19.88125 | 20.61289 | 22.46172 | 22.34258 | 25.57227 |
| `math/pow_using_math.py` | 21.74258 | 20.07734 | 20.61445 | 22.21797 | 23.19141 | 26.16211 |
| `modules/json/json_module.py` | 21.87383 | 21.0832 | 21.18711 | 21.71484 | 22.25977 | 26.1 |
| `modules/json/orjson_module.py` | 22.60508 | 21.50195 | 21.575 | 23.39648 | 22.67734 | 26.79336 |

---


### **Python 3.6**

```bash
Python 3.6.15

Linux 67d881f0c9bc 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         6644568 kB
MemAvailable:   14559640 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.03255 | 0.00036 | 0.0325 | 0.0321 | 0.03322 | 21.79023 |
| `long_run/processes/generate_fake_data.py` | yes | 0.81595 | 0.01212 | 0.81201 | 0.80206 | 0.84184 | 64.88125 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/database/sqlite_.py` | yes | 0.58362 | 0.00452 | 0.58286 | 0.57694 | 0.59191 | 62.99492 |
| `long_run/database/postgresql.py` | yes | 0.14564 | 0.00298 | 0.14491 | 0.14243 | 0.15284 | 26.89297 |
| `math/haversine.py` | yes | 0.61437 | 0.01343 | 0.61189 | 0.59802 | 0.64442 | 21.84336 |
| `math/pow_using_math.py` | yes | 1.58435 | 0.06375 | 1.60033 | 1.50231 | 1.67929 | 21.74258 |
| `math/mandelbrot.py` | yes | 14.89008 | 0.05825 | 14.88607 | 14.83198 | 15.02585 | 36.45 |
| `math/pow_simple.py` | yes | 0.44665 | 0.00569 | 0.44488 | 0.44141 | 0.46046 | 21.74727 |
| `modules/json/json_module.py` | yes | 0.41144 | 0.0049 | 0.41115 | 0.40305 | 0.419 | 21.87383 |
| `modules/json/orjson_module.py` | yes | 0.26375 | 0.00216 | 0.26435 | 0.26043 | 0.26599 | 22.60508 |
| `complex/classes/namedtuple_classes.py` | yes | 0.09215 | 0.00169 | 0.09161 | 0.09081 | 0.09676 | 22.29453 |
| `complex/classes/classes.py` | yes | 0.0442 | 0.0004 | 0.04428 | 0.04356 | 0.0448 | 21.96992 |
| `complex/classes/dataclasses_.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `complex/classes/sloted_classes.py` | yes | 0.04396 | 0.00028 | 0.04395 | 0.0434 | 0.04439 | 22.06836 |
| `complex/classes/simplenamespace.py` | yes | 0.05899 | 0.00038 | 0.05902 | 0.0583 | 0.05953 | 22.09961 |
| `algorithm/twosum/twosum.py` | yes | 0.0795 | 0.00106 | 0.07916 | 0.07823 | 0.08122 | 22.44922 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.08003 | 0.00094 | 0.07979 | 0.07899 | 0.08224 | 22.40273 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06869 | 0.00067 | 0.06886 | 0.06776 | 0.06968 | 22.10391 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.66847 | 0.01139 | 0.66764 | 0.65357 | 0.69174 | 61.88477 |


### **Python 3.7**

```bash
Python 3.7.15

Linux cc99ec4fd242 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         6626580 kB
MemAvailable:   14556280 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.02796 | 0.00473 | 0.02506 | 0.02462 | 0.03807 | 19.90039 |
| `long_run/processes/generate_fake_data.py` | yes | 0.71897 | 0.01193 | 0.71562 | 0.70904 | 0.74473 | 68.55273 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/database/sqlite_.py` | yes | 0.50001 | 0.00236 | 0.50014 | 0.49623 | 0.50332 | 65.04922 |
| `long_run/database/postgresql.py` | yes | 0.12954 | 0.00081 | 0.12959 | 0.12835 | 0.13103 | 24.15508 |
| `math/haversine.py` | yes | 0.59492 | 0.02258 | 0.59185 | 0.56599 | 0.6474 | 20.03984 |
| `math/pow_using_math.py` | yes | 1.42762 | 0.02832 | 1.43656 | 1.38414 | 1.46183 | 20.07734 |
| `math/mandelbrot.py` | yes | 14.78379 | 0.15258 | 14.79481 | 14.53766 | 14.97929 | 34.51367 |
| `math/pow_simple.py` | yes | 0.42185 | 0.01019 | 0.41756 | 0.41166 | 0.43971 | 19.88125 |
| `modules/json/json_module.py` | yes | 0.38018 | 0.00593 | 0.37934 | 0.37207 | 0.39226 | 21.0832 |
| `modules/json/orjson_module.py` | yes | 0.20314 | 0.00156 | 0.20269 | 0.20177 | 0.20719 | 21.50195 |
| `complex/classes/namedtuple_classes.py` | yes | 0.07654 | 0.00263 | 0.07592 | 0.07361 | 0.08109 | 20.19258 |
| `complex/classes/classes.py` | yes | 0.03698 | 0.0004 | 0.0369 | 0.03657 | 0.03774 | 19.98867 |
| `complex/classes/dataclasses_.py` | yes | 0.09566 | 0.0007 | 0.09576 | 0.09445 | 0.09677 | 20.03828 |
| `complex/classes/sloted_classes.py` | yes | 0.03693 | 0.00034 | 0.03686 | 0.03653 | 0.03752 | 20.04414 |
| `complex/classes/simplenamespace.py` | yes | 0.03806 | 0.00037 | 0.03816 | 0.03749 | 0.03847 | 19.87227 |
| `algorithm/twosum/twosum.py` | yes | 0.06471 | 0.00036 | 0.06468 | 0.06415 | 0.06542 | 20.0375 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.06504 | 0.0014 | 0.06457 | 0.06385 | 0.06853 | 19.96445 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06128 | 0.00062 | 0.06115 | 0.06042 | 0.06249 | 19.95 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.54437 | 0.00461 | 0.54338 | 0.53992 | 0.5558 | 63.68477 |


### **Python 3.8**

```bash
Python 3.8.15

Linux 2e2347a3652b 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         6632188 kB
MemAvailable:   14573168 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.02705 | 0.0006 | 0.02701 | 0.02621 | 0.02818 | 20.47305 |
| `long_run/processes/generate_fake_data.py` | yes | 0.74727 | 0.0061 | 0.74774 | 0.73986 | 0.75686 | 65.55117 |
| `long_run/processes/collect_names_from_site.py` | yes | 3.68563 | 0.55163 | 3.58295 | 2.96887 | 4.62939 | 44.71523 |
| `long_run/database/sqlite_.py` | yes | 0.55421 | 0.00461 | 0.55334 | 0.54788 | 0.56437 | 65.32969 |
| `long_run/database/postgresql.py` | yes | 0.14162 | 0.0008 | 0.14176 | 0.1404 | 0.14283 | 24.48242 |
| `math/haversine.py` | yes | 0.52688 | 0.01156 | 0.52402 | 0.5149 | 0.55269 | 20.59102 |
| `math/pow_using_math.py` | yes | 1.33371 | 0.01685 | 1.32649 | 1.32084 | 1.37411 | 20.61445 |
| `math/mandelbrot.py` | yes | 14.9947 | 0.14109 | 14.95654 | 14.8497 | 15.37504 | 34.9332 |
| `math/pow_simple.py` | yes | 0.41856 | 0.0048 | 0.41676 | 0.41521 | 0.43117 | 20.61289 |
| `modules/json/json_module.py` | yes | 0.35303 | 0.00532 | 0.35358 | 0.34598 | 0.36136 | 21.18711 |
| `modules/json/orjson_module.py` | yes | 0.2134 | 0.00199 | 0.21268 | 0.21122 | 0.21777 | 21.575 |
| `complex/classes/namedtuple_classes.py` | yes | 0.0805 | 0.00045 | 0.08048 | 0.07995 | 0.0813 | 20.37227 |
| `complex/classes/classes.py` | yes | 0.03893 | 0.00057 | 0.03876 | 0.03829 | 0.04028 | 20.63594 |
| `complex/classes/dataclasses_.py` | yes | 0.10263 | 0.00055 | 0.10271 | 0.1015 | 0.10325 | 20.66641 |
| `complex/classes/sloted_classes.py` | yes | 0.03878 | 0.00038 | 0.03876 | 0.03823 | 0.03939 | 20.76523 |
| `complex/classes/simplenamespace.py` | yes | 0.04102 | 0.00186 | 0.03974 | 0.03926 | 0.04377 | 20.74687 |
| `algorithm/twosum/twosum.py` | yes | 0.07108 | 0.00048 | 0.07106 | 0.07035 | 0.07169 | 20.56016 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07162 | 0.00127 | 0.07132 | 0.06999 | 0.07435 | 20.63398 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06552 | 0.0003 | 0.06547 | 0.06509 | 0.06595 | 20.72539 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.59646 | 0.0061 | 0.59438 | 0.5923 | 0.6129 | 64.05547 |


### **Python 3.9**

```bash
Python 3.9.15

Linux b25ab42144a8 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         6598156 kB
MemAvailable:   14549660 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.02961 | 0.00053 | 0.02965 | 0.0288 | 0.03067 | 22.68867 |
| `long_run/processes/generate_fake_data.py` | yes | 0.79788 | 0.01552 | 0.79378 | 0.78566 | 0.83823 | 68.22773 |
| `long_run/processes/collect_names_from_site.py` | yes | 3.50393 | 0.94225 | 3.55265 | 2.11588 | 5.01346 | 45.09766 |
| `long_run/database/sqlite_.py` | yes | 0.58194 | 0.00196 | 0.58193 | 0.57927 | 0.58628 | 65.84609 |
| `long_run/database/postgresql.py` | yes | 0.15405 | 0.00081 | 0.15389 | 0.15278 | 0.15549 | 26.31055 |
| `math/haversine.py` | yes | 0.59411 | 0.01572 | 0.59188 | 0.57179 | 0.62062 | 22.43242 |
| `math/pow_using_math.py` | yes | 1.40951 | 0.04596 | 1.39687 | 1.36404 | 1.50642 | 22.21797 |
| `math/mandelbrot.py` | yes | 15.21169 | 0.3639 | 15.02875 | 14.86413 | 15.8278 | 35.45469 |
| `math/pow_simple.py` | yes | 0.4146 | 0.0025 | 0.4135 | 0.41222 | 0.41977 | 22.46172 |
| `modules/json/json_module.py` | yes | 0.36501 | 0.00594 | 0.36427 | 0.35633 | 0.37334 | 21.71484 |
| `modules/json/orjson_module.py` | yes | 0.2379 | 0.00467 | 0.23666 | 0.23395 | 0.25035 | 23.39648 |
| `complex/classes/namedtuple_classes.py` | yes | 0.08961 | 0.00152 | 0.08935 | 0.08832 | 0.09367 | 22.77695 |
| `complex/classes/classes.py` | yes | 0.04119 | 0.0005 | 0.0412 | 0.0404 | 0.04215 | 21.62656 |
| `complex/classes/dataclasses_.py` | yes | 0.12243 | 0.00023 | 0.12237 | 0.12221 | 0.12291 | 22.85508 |
| `complex/classes/sloted_classes.py` | yes | 0.04144 | 0.00013 | 0.04142 | 0.04129 | 0.04175 | 22.52266 |
| `complex/classes/simplenamespace.py` | yes | 0.04571 | 0.00481 | 0.04423 | 0.04386 | 0.05939 | 22.56836 |
| `algorithm/twosum/twosum.py` | yes | 0.07937 | 0.00141 | 0.07877 | 0.07807 | 0.08137 | 21.61094 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07899 | 0.0007 | 0.07877 | 0.07803 | 0.08039 | 22.4668 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.07129 | 0.00091 | 0.07134 | 0.06984 | 0.07266 | 22.0793 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.63157 | 0.00883 | 0.62839 | 0.62509 | 0.65465 | 65.11328 |


### **Python 3.10**

```bash
Python 3.10.8

Linux a9d8041ccd93 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         6589664 kB
MemAvailable:   14551976 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.02995 | 0.00133 | 0.0295 | 0.02918 | 0.03361 | 22.66562 |
| `long_run/processes/generate_fake_data.py` | yes | 0.75671 | 0.01677 | 0.7512 | 0.74718 | 0.80319 | 67.24727 |
| `long_run/processes/collect_names_from_site.py` | yes | 3.30459 | 0.90055 | 3.27545 | 2.05002 | 5.01627 | 45.19453 |
| `long_run/database/sqlite_.py` | yes | 0.55854 | 0.00386 | 0.55854 | 0.55314 | 0.56413 | 65.73672 |
| `long_run/database/postgresql.py` | yes | 0.1432 | 0.00067 | 0.14327 | 0.14226 | 0.14434 | 25.94805 |
| `math/haversine.py` | yes | 0.54467 | 0.01009 | 0.54379 | 0.53137 | 0.5613 | 22.67461 |
| `math/pow_using_math.py` | yes | 1.35538 | 0.03018 | 1.34783 | 1.32347 | 1.43265 | 23.19141 |
| `math/mandelbrot.py` | yes | 15.13002 | 0.35699 | 14.96732 | 14.71101 | 15.79404 | 35.9668 |
| `math/pow_simple.py` | yes | 0.397 | 0.00716 | 0.394 | 0.38986 | 0.41251 | 22.34258 |
| `modules/json/json_module.py` | yes | 0.32937 | 0.00327 | 0.32903 | 0.32525 | 0.33655 | 22.25977 |
| `modules/json/orjson_module.py` | yes | 0.21433 | 0.00166 | 0.21434 | 0.21205 | 0.21657 | 22.67734 |
| `complex/classes/namedtuple_classes.py` | yes | 0.08362 | 0.00132 | 0.08322 | 0.08255 | 0.08726 | 23.87539 |
| `complex/classes/classes.py` | yes | 0.03909 | 0.00035 | 0.03904 | 0.03861 | 0.03968 | 23.3293 |
| `complex/classes/dataclasses_.py` | yes | 0.1156 | 0.00069 | 0.1156 | 0.11447 | 0.11678 | 23.41602 |
| `complex/classes/sloted_classes.py` | yes | 0.03894 | 0.00036 | 0.03903 | 0.03835 | 0.03939 | 24.36328 |
| `complex/classes/simplenamespace.py` | yes | 0.0411 | 0.00043 | 0.04105 | 0.04033 | 0.04169 | 24.62539 |
| `algorithm/twosum/twosum.py` | yes | 0.07573 | 0.00297 | 0.07495 | 0.07396 | 0.08402 | 22.05703 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07645 | 0.00384 | 0.07455 | 0.07359 | 0.08355 | 23.23633 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06781 | 0.00658 | 0.06577 | 0.06537 | 0.08653 | 23.03125 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.59693 | 0.00599 | 0.59504 | 0.59166 | 0.61132 | 63.91445 |


### **Python 3.11**

```bash
Python 3.11.0

Linux af90d2d0ca2a 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         6583416 kB
MemAvailable:   14553444 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.01779 | 0.00269 | 0.01897 | 0.0115 | 0.01932 | 25.79805 |
| `long_run/processes/generate_fake_data.py` | yes | 0.74707 | 0.00541 | 0.7479 | 0.73639 | 0.75411 | 72.32969 |
| `long_run/processes/collect_names_from_site.py` | yes | 3.15225 | 0.64584 | 3.05938 | 2.08028 | 4.1565 | 47.2793 |
| `long_run/database/sqlite_.py` | yes | 0.5564 | 0.00524 | 0.55539 | 0.55115 | 0.56834 | 71.04023 |
| `long_run/database/postgresql.py` | yes | 0.14052 | 0.00065 | 0.14031 | 0.1398 | 0.14196 | 31.92109 |
| `math/haversine.py` | yes | 0.47057 | 0.01869 | 0.47231 | 0.44554 | 0.50328 | 25.6125 |
| `math/pow_using_math.py` | yes | 1.1716 | 0.01497 | 1.17197 | 1.15175 | 1.19802 | 26.16211 |
| `math/mandelbrot.py` | yes | 14.95167 | 0.13603 | 14.93276 | 14.81818 | 15.2932 | 38.72031 |
| `math/pow_simple.py` | yes | 0.31689 | 0.00518 | 0.31491 | 0.31385 | 0.32983 | 25.57227 |
| `modules/json/json_module.py` | yes | 0.28024 | 0.00263 | 0.28051 | 0.27575 | 0.28373 | 26.1 |
| `modules/json/orjson_module.py` | yes | 0.17261 | 0.0014 | 0.17246 | 0.17039 | 0.17453 | 26.79336 |
| `complex/classes/namedtuple_classes.py` | yes | 0.07784 | 0.0004 | 0.07791 | 0.07694 | 0.07832 | 26.36797 |
| `complex/classes/classes.py` | yes | 0.02314 | 0.00135 | 0.02245 | 0.02209 | 0.02515 | 27.24492 |
| `complex/classes/dataclasses_.py` | yes | 0.10729 | 0.00051 | 0.10724 | 0.10671 | 0.10821 | 27.31406 |
| `complex/classes/sloted_classes.py` | yes | 0.01953 | 0.0003 | 0.01956 | 0.01908 | 0.01993 | 27.14688 |
| `complex/classes/simplenamespace.py` | yes | 0.02387 | 0.00035 | 0.02383 | 0.0234 | 0.02457 | 27.80508 |
| `algorithm/twosum/twosum.py` | yes | 0.07096 | 0.0031 | 0.06977 | 0.06902 | 0.07935 | 25.97969 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07064 | 0.00119 | 0.07095 | 0.06922 | 0.07277 | 25.8043 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.0551 | 0.00051 | 0.05507 | 0.05429 | 0.05583 | 25.86172 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.58237 | 0.00449 | 0.58058 | 0.57856 | 0.5923 | 69.50859 |

