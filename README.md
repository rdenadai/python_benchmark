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
> Last run: Sat Nov 26 10:30:19 AM -03 2022
### **Comparison**

#### How much faster 3.11 is? (Mean / Median from 3.6 to 3.10)
| Command | 3.6 (Mean / Median) | 3.7 (...) | 3.8 (...) | 3.9 (...) | 3.10 (...) |
|:---|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 13.73% / 14.11% | -5.23% / -6.90% | 1.44% / 1.70% | 12.76% / 12.65% | 7.87% / 7.88% |
| `algorithm/twosum/twosum_naive.py` | 12.68% / 12.14% | -8.97% / -7.78% | -0.29% / 0.76% | 9.47% / 10.60% | 5.59% / 6.37% |
| `complex/classes/classes.py` | 113.77% / 106.96% | 78.54% / 72.48% | 91.69% / 83.08% | 101.93% / 95.14% | 90.09% / 82.76% |
| `complex/classes/dataclasses_.py` | -- / -- | -10.70% / -10.75% | -3.35% / -3.55% | 16.46% / 16.18% | 7.39% / 7.02% |
| `complex/classes/namedtuple_classes.py` | 14.02% / 13.24% | -5.61% / -6.11% | 1.26% / 0.68% | 11.41% / 10.97% | 5.86% / 4.88% |
| `complex/classes/simplenamespace.py` | 136.18% / 140.06% | 51.44% / 53.37% | 59.03% / 61.28% | 77.92% / 79.55% | 64.22% / 67.37% |
| `complex/classes/sloted_classes.py` | 132.76% / 130.99% | 96.12% / 95.18% | 102.46% / 102.20% | 117.71% / 117.80% | 106.29% / 104.82% |
| `dummy/dummy.py` | 98.79% / 75.36% | 59.70% / 39.68% | 75.17% / 54.45% | 86.16% / 62.88% | 71.00% / 49.12% |
| `long_run/database/postgresql.py` | 1.67% / 1.98% | -8.59% / -8.12% | -0.35% / 0.22% | 8.04% / 8.74% | 1.07% / 1.74% |
| `long_run/file/load_titanic_csv_pandas.py` | 15.18% / 15.22% | -5.22% / -5.70% | 2.55% / 1.92% | 10.54% / 10.18% | 2.25% / 2.02% |
| `long_run/file/load_titanic_csv_python.py` | 21.99% / 22.76% | 9.07% / 9.63% | 16.62% / 16.64% | 27.66% / 28.26% | 16.56% / 17.42% |
| `long_run/processes/collect_names_from_site.py` | -- / -- | -- / -- | 22.62% / 23.21% | 26.79% / 26.03% | 22.14% / 20.36% |
| `long_run/processes/generate_fake_data.py` | 8.80% / 8.85% | -3.93% / -3.70% | 1.38% / 1.09% | 5.59% / 5.50% | 2.15% / 2.07% |
| `math/pow_simple.py` | 43.27% / 44.10% | 38.43% / 37.80% | 37.55% / 39.11% | 31.84% / 32.02% | 24.30% / 24.70% |
| `math/pow_using_math.py` | 38.20% / 37.69% | 22.46% / 22.50% | 14.14% / 14.40% | 20.07% / 20.88% | 13.60% / 14.28% |
| `modules/json/json_module.py` | 45.34% / 44.98% | 34.72% / 34.71% | 26.42% / 25.03% | 29.28% / 29.20% | 16.91% / 16.38% |
| `modules/json/orjson_module.py` | 53.86% / 53.86% | 18.76% / 18.49% | 23.83% / 23.80% | 37.69% / 37.92% | 24.33% / 24.26% |
---

#### How much more memory 3.11 uses? (Memory from 3.6 to 3.10)
| Command |  3.6 | 3.7 | 3.8 | 3.9 | 3.10 |
|:---|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 17.07% | 29.33% | 26.28% | 20.3% | 17.58% |
| `algorithm/twosum/twosum_naive.py` | 16.15% | 28.51% | 25.96% | 14.55% | 11.85% |
| `complex/classes/classes.py` | 24.96% | 36.14% | 33.05% | 26.06% | 16.72% |
| `complex/classes/dataclasses_.py` | -- | 36.41% | 32.15% | 19.85% | 17.99% |
| `complex/classes/namedtuple_classes.py` | 19.24% | 30.67% | 29.3% | 15.51% | 10.65% |
| `complex/classes/simplenamespace.py` | 25.87% | 38.62% | 34.88% | 23.4% | 12.46% |
| `complex/classes/sloted_classes.py` | 24.86% | 36.33% | 32.14% | 20.54% | 12.12% |
| `dummy/dummy.py` | 19.34% | 29.93% | 28.05% | 14.09% | 12.99% |
| `long_run/database/postgresql.py` | 20.46% | 31.5% | 27.69% | 20.7% | 24.09% |
| `long_run/file/load_titanic_csv_pandas.py` | 11.98% | 9.35% | 8.9% | 6.68% | 9.3% |
| `long_run/file/load_titanic_csv_python.py` | 17.93% | 29.65% | 24.87% | 17.96% | 12.06% |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 5.64% | 4.99% | 5.43% |
| `long_run/processes/generate_fake_data.py` | 11.58% | 6.15% | 11.04% | 5.88% | 7.49% |
| `math/pow_simple.py` | 17.98% | 29.13% | 24.52% | 13.96% | 15.06% |
| `math/pow_using_math.py` | 20.72% | 30.23% | 26.33% | 16.81% | 12.95% |
| `modules/json/json_module.py` | 19.48% | 22.5% | 22.78% | 20.16% | 17.35% |
| `modules/json/orjson_module.py` | 18.22% | 24.8% | 23.8% | 14.46% | 18.56% |
---

#### **Execution**

| Command |  Mean 3.6 [s] | Mean 3.7 [s] | Mean 3.8 [s] | Mean 3.9 [s] | Mean 3.10 [s] | Mean 3.11 [s] |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 0.07959 | 0.06632 | 0.07099 | 0.07891 | 0.07549 | 0.06998 |
| `algorithm/twosum/twosum_naive.py` | 0.08077 | 0.06525 | 0.07147 | 0.07847 | 0.07569 | 0.07168 |
| `complex/classes/classes.py` | 0.04423 | 0.03694 | 0.03966 | 0.04178 | 0.03933 | 0.02069 |
| `complex/classes/dataclasses_.py` | -- | 0.09589 | 0.10378 | 0.12506 | 0.11532 | 0.10738 |
| `complex/classes/namedtuple_classes.py` | 0.09123 | 0.07552 | 0.08102 | 0.08914 | 0.0847 | 0.08001 |
| `complex/classes/simplenamespace.py` | 0.05914 | 0.03792 | 0.03982 | 0.04455 | 0.04112 | 0.02504 |
| `complex/classes/sloted_classes.py` | 0.04441 | 0.03742 | 0.03863 | 0.04154 | 0.03936 | 0.01908 |
| `dummy/dummy.py` | 0.0329 | 0.02643 | 0.02899 | 0.03081 | 0.0283 | 0.01655 |
| `long_run/database/postgresql.py` | 0.1445 | 0.12991 | 0.14162 | 0.15354 | 0.14364 | 0.14212 |
| `long_run/file/load_titanic_csv_pandas.py` | 0.6775 | 0.5575 | 0.60323 | 0.65021 | 0.60146 | 0.58823 |
| `long_run/file/load_titanic_csv_python.py` | 0.06901 | 0.0617 | 0.06597 | 0.07222 | 0.06594 | 0.05657 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 1.97257 | 2.03968 | 1.96483 | 1.60867 |
| `long_run/processes/generate_fake_data.py` | 0.82029 | 0.72429 | 0.76432 | 0.79605 | 0.77011 | 0.75392 |
| `math/pow_simple.py` | 0.45588 | 0.4405 | 0.43767 | 0.41953 | 0.39551 | 0.3182 |
| `math/pow_using_math.py` | 1.63295 | 1.44698 | 1.34858 | 1.41871 | 1.34228 | 1.18155 |
| `modules/json/json_module.py` | 0.41281 | 0.38265 | 0.35906 | 0.36718 | 0.33206 | 0.28403 |
| `modules/json/orjson_module.py` | 0.26657 | 0.20575 | 0.21453 | 0.23855 | 0.2154 | 0.17325 |

| Command |  Median 3.6 [s] | Median 3.7 [s] | Median 3.8 [s] | Median 3.9 [s] | Median 3.10 [s] | Median 3.11 [s] |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 0.07983 | 0.06513 | 0.07115 | 0.07881 | 0.07547 | 0.06996 |
| `algorithm/twosum/twosum_naive.py` | 0.07953 | 0.0654 | 0.07146 | 0.07844 | 0.07544 | 0.07092 |
| `complex/classes/classes.py` | 0.04429 | 0.03691 | 0.03918 | 0.04176 | 0.03911 | 0.0214 |
| `complex/classes/dataclasses_.py` | -- | 0.09588 | 0.10362 | 0.12481 | 0.11497 | 0.10743 |
| `complex/classes/namedtuple_classes.py` | 0.09106 | 0.0755 | 0.08096 | 0.08923 | 0.08433 | 0.08041 |
| `complex/classes/simplenamespace.py` | 0.05915 | 0.03779 | 0.03974 | 0.04424 | 0.04124 | 0.02464 |
| `complex/classes/sloted_classes.py` | 0.04412 | 0.03728 | 0.03862 | 0.0416 | 0.03912 | 0.0191 |
| `dummy/dummy.py` | 0.03288 | 0.02619 | 0.02896 | 0.03054 | 0.02796 | 0.01875 |
| `long_run/database/postgresql.py` | 0.14414 | 0.12986 | 0.14165 | 0.1537 | 0.1438 | 0.14134 |
| `long_run/file/load_titanic_csv_pandas.py` | 0.67688 | 0.55397 | 0.59875 | 0.64725 | 0.59931 | 0.58746 |
| `long_run/file/load_titanic_csv_python.py` | 0.06898 | 0.0616 | 0.06554 | 0.07207 | 0.06598 | 0.05619 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 1.98818 | 2.0337 | 1.94217 | 1.61366 |
| `long_run/processes/generate_fake_data.py` | 0.81868 | 0.72424 | 0.7603 | 0.79348 | 0.76764 | 0.7521 |
| `math/pow_simple.py` | 0.45515 | 0.43524 | 0.43937 | 0.417 | 0.39388 | 0.31585 |
| `math/pow_using_math.py` | 1.61114 | 1.43347 | 1.33867 | 1.41442 | 1.33727 | 1.17014 |
| `modules/json/json_module.py` | 0.41272 | 0.38347 | 0.35593 | 0.36778 | 0.3313 | 0.28467 |
| `modules/json/orjson_module.py` | 0.26619 | 0.205 | 0.21418 | 0.23862 | 0.21499 | 0.17301 |

#### **Memory Usage**

| Command |  MEM 3.6 [MB] | MEM 3.7 [MB] | MEM 3.8 [MB] | MEM 3.9 [MB] | MEM 3.10 [MB] | MEM 3.11 [MB] |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 22.14258 | 20.04336 | 20.52813 | 21.54883 | 22.04687 | 25.92305 |
| `algorithm/twosum/twosum_naive.py` | 22.1793 | 20.04609 | 20.45156 | 22.48867 | 23.03125 | 25.76133 |
| `complex/classes/classes.py` | 21.83047 | 20.0375 | 20.50273 | 21.63984 | 23.37266 | 27.27969 |
| `complex/classes/dataclasses_.py` | -- | 20.04375 | 20.68984 | 22.81367 | 23.17422 | 27.34258 |
| `complex/classes/namedtuple_classes.py` | 22.09375 | 20.16094 | 20.37461 | 22.80586 | 23.8082 | 26.34414 |
| `complex/classes/simplenamespace.py` | 22.02539 | 19.99922 | 20.55469 | 22.4668 | 24.65117 | 27.72383 |
| `complex/classes/sloted_classes.py` | 21.80703 | 19.97266 | 20.60625 | 22.58828 | 24.28437 | 27.22852 |
| `dummy/dummy.py` | 21.60273 | 19.84219 | 20.13281 | 22.59609 | 22.81563 | 25.78008 |
| `long_run/database/postgresql.py` | 26.30781 | 24.09922 | 24.81758 | 26.25586 | 25.53828 | 31.69023 |
| `long_run/file/load_titanic_csv_pandas.py` | 61.68125 | 63.16602 | 63.42695 | 64.74336 | 63.19297 | 69.0707 |
| `long_run/file/load_titanic_csv_python.py` | 21.91445 | 19.93477 | 20.69727 | 21.91016 | 23.06211 | 25.84453 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 44.62891 | 44.90352 | 44.71875 | 47.1457 |
| `long_run/processes/generate_fake_data.py` | 64.56602 | 67.86758 | 64.87969 | 68.04492 | 67.02539 | 72.04297 |
| `math/pow_simple.py` | 21.69063 | 19.81875 | 20.55156 | 22.45664 | 22.24062 | 25.59102 |
| `math/pow_using_math.py` | 21.63672 | 20.05703 | 20.67578 | 22.35977 | 23.12461 | 26.11953 |
| `modules/json/json_module.py` | 21.81328 | 21.27617 | 21.22656 | 21.69023 | 22.20937 | 26.06289 |
| `modules/json/orjson_module.py` | 22.62734 | 21.43477 | 21.60742 | 23.37187 | 22.56328 | 26.75039 |

---


### **Python 3.6**

```bash
Python 3.6.15

Linux 496446bd07c7 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         5427996 kB
MemAvailable:   14455908 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.0329 | 0.0003 | 0.03288 | 0.03251 | 0.03353 | 21.60273 |
| `long_run/processes/generate_fake_data.py` | yes | 0.82029 | 0.01045 | 0.81868 | 0.80915 | 0.83734 | 64.56602 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/database/postgresql.py` | yes | 0.1445 | 0.0021 | 0.14414 | 0.14196 | 0.14757 | 26.30781 |
| `math/pow_using_math.py` | yes | 1.63295 | 0.08419 | 1.61114 | 1.54502 | 1.84507 | 21.63672 |
| `math/pow_simple.py` | yes | 0.45588 | 0.00591 | 0.45515 | 0.44806 | 0.46534 | 21.69063 |
| `modules/json/json_module.py` | yes | 0.41281 | 0.00595 | 0.41272 | 0.40316 | 0.42057 | 21.81328 |
| `modules/json/orjson_module.py` | yes | 0.26657 | 0.00235 | 0.26619 | 0.264 | 0.27206 | 22.62734 |
| `complex/classes/namedtuple_classes.py` | yes | 0.09123 | 0.00079 | 0.09106 | 0.09021 | 0.09313 | 22.09375 |
| `complex/classes/classes.py` | yes | 0.04423 | 0.00032 | 0.04429 | 0.04364 | 0.04462 | 21.83047 |
| `complex/classes/dataclasses_.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `complex/classes/sloted_classes.py` | yes | 0.04441 | 0.00083 | 0.04412 | 0.04376 | 0.0465 | 21.80703 |
| `complex/classes/simplenamespace.py` | yes | 0.05914 | 0.00038 | 0.05915 | 0.05821 | 0.05965 | 22.02539 |
| `algorithm/twosum/twosum.py` | yes | 0.07959 | 0.00068 | 0.07983 | 0.07856 | 0.08043 | 22.14258 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.08077 | 0.00304 | 0.07953 | 0.0783 | 0.0883 | 22.1793 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06901 | 0.00052 | 0.06898 | 0.06785 | 0.0696 | 21.91445 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.6775 | 0.0072 | 0.67688 | 0.66734 | 0.6902 | 61.68125 |


### **Python 3.7**

```bash
Python 3.7.15

Linux cd45161cb82d 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         5397824 kB
MemAvailable:   14440348 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.02643 | 0.0004 | 0.02619 | 0.026 | 0.02708 | 19.84219 |
| `long_run/processes/generate_fake_data.py` | yes | 0.72429 | 0.00385 | 0.72424 | 0.71998 | 0.73147 | 67.86758 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/database/postgresql.py` | yes | 0.12991 | 0.00067 | 0.12986 | 0.12889 | 0.13083 | 24.09922 |
| `math/pow_using_math.py` | yes | 1.44698 | 0.04565 | 1.43347 | 1.39724 | 1.53168 | 20.05703 |
| `math/pow_simple.py` | yes | 0.4405 | 0.02031 | 0.43524 | 0.42015 | 0.47536 | 19.81875 |
| `modules/json/json_module.py` | yes | 0.38265 | 0.00796 | 0.38347 | 0.37281 | 0.3942 | 21.27617 |
| `modules/json/orjson_module.py` | yes | 0.20575 | 0.00205 | 0.205 | 0.20364 | 0.20919 | 21.43477 |
| `complex/classes/namedtuple_classes.py` | yes | 0.07552 | 0.00063 | 0.0755 | 0.07421 | 0.07651 | 20.16094 |
| `complex/classes/classes.py` | yes | 0.03694 | 0.00019 | 0.03691 | 0.03671 | 0.03735 | 20.0375 |
| `complex/classes/dataclasses_.py` | yes | 0.09589 | 0.00041 | 0.09588 | 0.09532 | 0.09657 | 20.04375 |
| `complex/classes/sloted_classes.py` | yes | 0.03742 | 0.00069 | 0.03728 | 0.03653 | 0.03901 | 19.97266 |
| `complex/classes/simplenamespace.py` | yes | 0.03792 | 0.00038 | 0.03779 | 0.03752 | 0.03859 | 19.99922 |
| `algorithm/twosum/twosum.py` | yes | 0.06632 | 0.00263 | 0.06513 | 0.06441 | 0.07272 | 20.04336 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.06525 | 0.00051 | 0.0654 | 0.06422 | 0.06576 | 20.04609 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.0617 | 0.00047 | 0.0616 | 0.06085 | 0.06241 | 19.93477 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.5575 | 0.01275 | 0.55397 | 0.54444 | 0.58042 | 63.16602 |


### **Python 3.8**

```bash
Python 3.8.15

Linux bc743e2b8e2c 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         5385388 kB
MemAvailable:   14458772 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.02899 | 0.00077 | 0.02896 | 0.02813 | 0.03064 | 20.13281 |
| `long_run/processes/generate_fake_data.py` | yes | 0.76432 | 0.01305 | 0.7603 | 0.74633 | 0.78824 | 64.87969 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.97257 | 0.08362 | 1.98818 | 1.84786 | 2.10274 | 44.62891 |
| `long_run/database/postgresql.py` | yes | 0.14162 | 0.00051 | 0.14165 | 0.14081 | 0.14229 | 24.81758 |
| `math/pow_using_math.py` | yes | 1.34858 | 0.03228 | 1.33867 | 1.32002 | 1.4168 | 20.67578 |
| `math/pow_simple.py` | yes | 0.43767 | 0.01284 | 0.43937 | 0.41866 | 0.46077 | 20.55156 |
| `modules/json/json_module.py` | yes | 0.35906 | 0.00718 | 0.35593 | 0.35121 | 0.3742 | 21.22656 |
| `modules/json/orjson_module.py` | yes | 0.21453 | 0.00122 | 0.21418 | 0.21336 | 0.21678 | 21.60742 |
| `complex/classes/namedtuple_classes.py` | yes | 0.08102 | 0.00103 | 0.08096 | 0.07964 | 0.08351 | 20.37461 |
| `complex/classes/classes.py` | yes | 0.03966 | 0.00128 | 0.03918 | 0.03829 | 0.04203 | 20.50273 |
| `complex/classes/dataclasses_.py` | yes | 0.10378 | 0.00102 | 0.10362 | 0.10259 | 0.10582 | 20.68984 |
| `complex/classes/sloted_classes.py` | yes | 0.03863 | 0.0004 | 0.03862 | 0.03813 | 0.03928 | 20.60625 |
| `complex/classes/simplenamespace.py` | yes | 0.03982 | 0.00048 | 0.03974 | 0.03908 | 0.04069 | 20.55469 |
| `algorithm/twosum/twosum.py` | yes | 0.07099 | 0.00034 | 0.07115 | 0.07036 | 0.0713 | 20.52813 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07147 | 0.00046 | 0.07146 | 0.07049 | 0.07221 | 20.45156 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06597 | 0.00127 | 0.06554 | 0.06502 | 0.06939 | 20.69727 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.60323 | 0.01176 | 0.59875 | 0.59507 | 0.63299 | 63.42695 |


### **Python 3.9**

```bash
Python 3.9.15

Linux 0f6a8cf1c621 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         5343728 kB
MemAvailable:   14443452 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.03081 | 0.00078 | 0.03054 | 0.03008 | 0.03265 | 22.59609 |
| `long_run/processes/generate_fake_data.py` | yes | 0.79605 | 0.00676 | 0.79348 | 0.78889 | 0.80705 | 68.04492 |
| `long_run/processes/collect_names_from_site.py` | yes | 2.03968 | 0.13635 | 2.0337 | 1.90361 | 2.38813 | 44.90352 |
| `long_run/database/postgresql.py` | yes | 0.15354 | 0.00056 | 0.1537 | 0.15248 | 0.15425 | 26.25586 |
| `math/pow_using_math.py` | yes | 1.41871 | 0.04008 | 1.41442 | 1.36339 | 1.48948 | 22.35977 |
| `math/pow_simple.py` | yes | 0.41953 | 0.01011 | 0.417 | 0.41119 | 0.44592 | 22.45664 |
| `modules/json/json_module.py` | yes | 0.36718 | 0.00588 | 0.36778 | 0.35574 | 0.3752 | 21.69023 |
| `modules/json/orjson_module.py` | yes | 0.23855 | 0.00369 | 0.23862 | 0.23358 | 0.24428 | 23.37187 |
| `complex/classes/namedtuple_classes.py` | yes | 0.08914 | 0.00066 | 0.08923 | 0.08812 | 0.09043 | 22.80586 |
| `complex/classes/classes.py` | yes | 0.04178 | 0.00045 | 0.04176 | 0.04111 | 0.04261 | 21.63984 |
| `complex/classes/dataclasses_.py` | yes | 0.12506 | 0.00147 | 0.12481 | 0.12281 | 0.1274 | 22.81367 |
| `complex/classes/sloted_classes.py` | yes | 0.04154 | 0.00031 | 0.0416 | 0.04097 | 0.04209 | 22.58828 |
| `complex/classes/simplenamespace.py` | yes | 0.04455 | 0.00102 | 0.04424 | 0.04368 | 0.04721 | 22.4668 |
| `algorithm/twosum/twosum.py` | yes | 0.07891 | 0.00047 | 0.07881 | 0.0784 | 0.07989 | 21.54883 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07847 | 0.00058 | 0.07844 | 0.07736 | 0.07943 | 22.48867 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.07222 | 0.001 | 0.07207 | 0.07088 | 0.07466 | 21.91016 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.65021 | 0.0152 | 0.64725 | 0.63525 | 0.68968 | 64.74336 |


### **Python 3.10**

```bash
Python 3.10.8

Linux 55a8612c208e 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         5320796 kB
MemAvailable:   14441832 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.0283 | 0.00094 | 0.02796 | 0.02757 | 0.03082 | 22.81563 |
| `long_run/processes/generate_fake_data.py` | yes | 0.77011 | 0.01506 | 0.76764 | 0.75308 | 0.79133 | 67.02539 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.96483 | 0.09092 | 1.94217 | 1.84924 | 2.15977 | 44.71875 |
| `long_run/database/postgresql.py` | yes | 0.14364 | 0.00066 | 0.1438 | 0.14255 | 0.14457 | 25.53828 |
| `math/pow_using_math.py` | yes | 1.34228 | 0.02257 | 1.33727 | 1.30456 | 1.3831 | 23.12461 |
| `math/pow_simple.py` | yes | 0.39551 | 0.00635 | 0.39388 | 0.39089 | 0.41265 | 22.24062 |
| `modules/json/json_module.py` | yes | 0.33206 | 0.00596 | 0.3313 | 0.32615 | 0.34528 | 22.20937 |
| `modules/json/orjson_module.py` | yes | 0.2154 | 0.00249 | 0.21499 | 0.21231 | 0.22035 | 22.56328 |
| `complex/classes/namedtuple_classes.py` | yes | 0.0847 | 0.00158 | 0.08433 | 0.08354 | 0.08902 | 23.8082 |
| `complex/classes/classes.py` | yes | 0.03933 | 0.00079 | 0.03911 | 0.03864 | 0.04137 | 23.37266 |
| `complex/classes/dataclasses_.py` | yes | 0.11532 | 0.00074 | 0.11497 | 0.11442 | 0.11654 | 23.17422 |
| `complex/classes/sloted_classes.py` | yes | 0.03936 | 0.00112 | 0.03912 | 0.03806 | 0.04189 | 24.28437 |
| `complex/classes/simplenamespace.py` | yes | 0.04112 | 0.00048 | 0.04124 | 0.04036 | 0.04186 | 24.65117 |
| `algorithm/twosum/twosum.py` | yes | 0.07549 | 0.00106 | 0.07547 | 0.07425 | 0.07785 | 22.04687 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07569 | 0.00112 | 0.07544 | 0.07431 | 0.07713 | 23.03125 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06594 | 0.00046 | 0.06598 | 0.06481 | 0.06643 | 23.06211 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.60146 | 0.00607 | 0.59931 | 0.59528 | 0.61488 | 63.19297 |


### **Python 3.11**

```bash
Python 3.11.0

Linux 0a89f663d868 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         5297844 kB
MemAvailable:   14438168 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.01655 | 0.00307 | 0.01875 | 0.01195 | 0.01897 | 25.78008 |
| `long_run/processes/generate_fake_data.py` | yes | 0.75392 | 0.00904 | 0.7521 | 0.74352 | 0.77132 | 72.04297 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.60867 | 0.05743 | 1.61366 | 1.53783 | 1.7105 | 47.1457 |
| `long_run/database/postgresql.py` | yes | 0.14212 | 0.00235 | 0.14134 | 0.14037 | 0.14812 | 31.69023 |
| `math/pow_using_math.py` | yes | 1.18155 | 0.02901 | 1.17014 | 1.15232 | 1.22826 | 26.11953 |
| `math/pow_simple.py` | yes | 0.3182 | 0.00694 | 0.31585 | 0.3148 | 0.33763 | 25.59102 |
| `modules/json/json_module.py` | yes | 0.28403 | 0.00228 | 0.28467 | 0.27906 | 0.28681 | 26.06289 |
| `modules/json/orjson_module.py` | yes | 0.17325 | 0.00189 | 0.17301 | 0.17148 | 0.17822 | 26.75039 |
| `complex/classes/namedtuple_classes.py` | yes | 0.08001 | 0.00159 | 0.08041 | 0.07774 | 0.08252 | 26.34414 |
| `complex/classes/classes.py` | yes | 0.02069 | 0.00099 | 0.0214 | 0.01936 | 0.02149 | 27.27969 |
| `complex/classes/dataclasses_.py` | yes | 0.10738 | 0.00031 | 0.10743 | 0.10681 | 0.10785 | 27.34258 |
| `complex/classes/sloted_classes.py` | yes | 0.01908 | 0.0003 | 0.0191 | 0.01873 | 0.01962 | 27.22852 |
| `complex/classes/simplenamespace.py` | yes | 0.02504 | 0.00116 | 0.02464 | 0.02415 | 0.02772 | 27.72383 |
| `algorithm/twosum/twosum.py` | yes | 0.06998 | 0.00075 | 0.06996 | 0.06926 | 0.07188 | 25.92305 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07168 | 0.00317 | 0.07092 | 0.06964 | 0.08047 | 25.76133 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.05657 | 0.00122 | 0.05619 | 0.05563 | 0.05971 | 25.84453 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.58823 | 0.00392 | 0.58746 | 0.58551 | 0.59905 | 69.0707 |

