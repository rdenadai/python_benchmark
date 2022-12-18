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
> Last run: Sun Dec 18 08:33:49 AM -03 2022
### **Comparison**

#### How much faster 3.11 is? (Mean / Median from 3.6 to 3.10)
| Command | 3.6 (Mean / Median) | 3.7 (...) | 3.8 (...) | 3.9 (...) | 3.10 (...) |
|:---|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 13.13% / 12.92% | -7.00% / -7.07% | 2.13% / 2.10% | 13.72% / 14.02% | 6.32% / 6.45% |
| `algorithm/twosum/twosum_naive.py` | 12.33% / 12.28% | -7.96% / -7.86% | 1.76% / 1.39% | 11.34% / 11.42% | 5.87% / 5.96% |
| `complex/classes/classes.py` | 121.13% / 122.32% | 84.78% / 85.37% | 93.59% / 93.51% | 107.51% / 108.14% | 93.44% / 93.36% |
| `complex/classes/dataclasses_.py` | -- / -- | -11.41% / -10.97% | -5.35% / -4.49% | 13.51% / 14.04% | 6.61% / 7.48% |
| `complex/classes/namedtuple_classes.py` | 15.24% / 15.51% | -5.63% / -5.34% | 1.67% / 2.09% | 12.09% / 12.27% | 5.87% / 6.32% |
| `complex/classes/simplenamespace.py` | 139.62% / 137.45% | 56.59% / 54.88% | 67.36% / 61.09% | 80.86% / 79.08% | 70.54% / 66.40% |
| `complex/classes/sloted_classes.py` | 120.87% / 122.49% | 85.90% / 87.42% | 94.58% / 95.86% | 107.23% / 108.84% | 95.99% / 96.97% |
| `dummy/dummy.py` | 54.21% / 52.23% | 24.97% / 25.05% | 25.76% / 25.74% | 44.49% / 43.67% | 39.05% / 39.01% |
| `long_run/database/postgresql.py` | 1.43% / 1.44% | -7.94% / -8.90% | -0.18% / -0.08% | 8.08% / 8.02% | 1.65% / 1.10% |
| `long_run/database/sqlite_.py` | 4.82% / 4.38% | -9.89% / -10.05% | -0.26% / -0.51% | 5.07% / 4.62% | 0.85% / 0.39% |
| `long_run/file/load_titanic_csv_pandas.py` | 11.37% / 11.63% | -6.60% / -6.90% | 2.40% / 2.13% | 8.31% / 8.14% | 2.01% / 1.87% |
| `long_run/file/load_titanic_csv_python.py` | 20.73% / 20.90% | 8.74% / 9.22% | 15.88% / 16.25% | 26.60% / 26.85% | 19.17% / 17.15% |
| `long_run/processes/collect_names_from_site.py` | -- / -- | -- / -- | 154.49% / 147.40% | 26.63% / 23.05% | 19.10% / 18.63% |
| `long_run/processes/generate_fake_data.py` | 6.69% / 6.77% | -3.79% / -3.89% | 0.10% / 0.28% | 6.17% / 6.05% | 0.66% / 0.70% |
| `math/haversine.py` | 32.26% / 31.60% | 26.29% / 25.57% | 15.81% / 14.83% | 28.96% / 28.59% | 18.96% / 17.83% |
| `math/mandelbrot.py` | -1.32% / -0.98% | -0.96% / -0.70% | -0.55% / -0.55% | -1.05% / -0.95% | -1.35% / -1.14% |
| `math/pow_simple.py` | 36.16% / 37.91% | 29.49% / 29.46% | 28.18% / 29.97% | 29.12% / 30.32% | 22.97% / 23.18% |
| `math/pow_using_math.py` | 31.63% / 30.10% | 23.59% / 20.24% | 14.34% / 13.73% | 18.44% / 17.71% | 14.11% / 14.25% |
| `modules/json/json_module.py` | 47.30% / 47.24% | 36.58% / 35.73% | 25.62% / 25.70% | 29.78% / 30.04% | 17.63% / 17.71% |
| `modules/json/orjson_module.py` | 55.19% / 54.78% | 15.97% / 16.33% | 21.28% / 21.46% | 33.46% / 33.62% | 21.43% / 21.95% |
---

#### How much more memory 3.11 uses? (Memory from 3.6 to 3.10)
| Command |  3.6 | 3.7 | 3.8 | 3.9 | 3.10 |
|:---|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 15.34% | 27.61% | 25.12% | 18.49% | 10.9% |
| `algorithm/twosum/twosum_naive.py` | 15.29% | 27.35% | 24.66% | 13.52% | 13.65% |
| `complex/classes/classes.py` | 22.12% | 33.88% | 30.31% | 22.24% | 10.1% |
| `complex/classes/dataclasses_.py` | -- | 35.06% | 31.31% | 18.44% | 14.75% |
| `complex/classes/namedtuple_classes.py` | 19.46% | 30.97% | 30.26% | 16.28% | 12.06% |
| `complex/classes/simplenamespace.py` | 23.04% | 33.88% | 29.98% | 19.21% | 12.33% |
| `complex/classes/sloted_classes.py` | 22.73% | 34.37% | 30.01% | 19.06% | 12.35% |
| `dummy/dummy.py` | 19.45% | 29.39% | 26.39% | 13.17% | 15.08% |
| `long_run/database/postgresql.py` | 11.21% | 21.97% | 21.91% | 12.84% | 6.35% |
| `long_run/database/sqlite_.py` | 13.33% | 9.35% | 9.23% | 7.13% | 8.46% |
| `long_run/file/load_titanic_csv_pandas.py` | 12.48% | 8.76% | 8.5% | 7.76% | 7.99% |
| `long_run/file/load_titanic_csv_python.py` | 17.45% | 29.52% | 25.54% | 16.3% | 12.03% |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 5.42% | 5.31% | 4.8% |
| `long_run/processes/generate_fake_data.py` | 12.06% | 5.47% | 10.35% | 5.33% | 6.85% |
| `math/haversine.py` | 17.89% | 26.89% | 24.85% | 14.02% | 13.15% |
| `math/mandelbrot.py` | 7.08% | 12.73% | 11.81% | 9.25% | 8.61% |
| `math/pow_simple.py` | 18.31% | 28.36% | 24.92% | 14.05% | 13.12% |
| `math/pow_using_math.py` | 18.35% | 27.51% | 24.67% | 14.51% | 14.31% |
| `modules/json/json_module.py` | 18.08% | 21.52% | 22.09% | 18.51% | 11.03% |
| `modules/json/orjson_module.py` | 17.01% | 22.64% | 22.75% | 12.82% | 14.69% |
---

#### **Execution**

| Command |  Mean 3.6 [s] | Mean 3.7 [s] | Mean 3.8 [s] | Mean 3.9 [s] | Mean 3.10 [s] | Mean 3.11 [s] |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 0.07874 | 0.06473 | 0.07108 | 0.07915 | 0.074 | 0.0696 |
| `algorithm/twosum/twosum_naive.py` | 0.07906 | 0.06478 | 0.07162 | 0.07836 | 0.07451 | 0.07038 |
| `complex/classes/classes.py` | 0.04447 | 0.03716 | 0.03893 | 0.04173 | 0.0389 | 0.02011 |
| `complex/classes/dataclasses_.py` | -- | 0.09606 | 0.10263 | 0.12308 | 0.1156 | 0.10843 |
| `complex/classes/namedtuple_classes.py` | 0.09125 | 0.07472 | 0.0805 | 0.08875 | 0.08383 | 0.07918 |
| `complex/classes/simplenamespace.py` | 0.05873 | 0.03838 | 0.04102 | 0.04433 | 0.0418 | 0.02451 |
| `complex/classes/sloted_classes.py` | 0.04402 | 0.03705 | 0.03878 | 0.0413 | 0.03906 | 0.01993 |
| `dummy/dummy.py` | 0.03317 | 0.02688 | 0.02705 | 0.03108 | 0.02991 | 0.02151 |
| `long_run/database/postgresql.py` | 0.14391 | 0.13061 | 0.14162 | 0.15335 | 0.14422 | 0.14188 |
| `long_run/database/sqlite_.py` | 0.58246 | 0.5007 | 0.55421 | 0.58384 | 0.56043 | 0.55568 |
| `long_run/file/load_titanic_csv_pandas.py` | 0.64872 | 0.54405 | 0.59646 | 0.63091 | 0.5942 | 0.58249 |
| `long_run/file/load_titanic_csv_python.py` | 0.06826 | 0.06148 | 0.06552 | 0.07158 | 0.06738 | 0.05654 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 3.68563 | 1.83386 | 1.72493 | 1.44826 |
| `long_run/processes/generate_fake_data.py` | 0.79643 | 0.71822 | 0.74727 | 0.7926 | 0.75146 | 0.74651 |
| `math/haversine.py` | 0.60174 | 0.57456 | 0.52688 | 0.58674 | 0.54121 | 0.45497 |
| `math/mandelbrot.py` | 14.87851 | 14.93252 | 14.9947 | 14.91929 | 14.87439 | 15.0777 |
| `math/pow_simple.py` | 0.44462 | 0.42284 | 0.41856 | 0.42164 | 0.40156 | 0.32654 |
| `math/pow_using_math.py` | 1.53539 | 1.44165 | 1.33371 | 1.38163 | 1.3311 | 1.16648 |
| `modules/json/json_module.py` | 0.41398 | 0.38385 | 0.35303 | 0.36472 | 0.33059 | 0.28104 |
| `modules/json/orjson_module.py` | 0.27308 | 0.20406 | 0.2134 | 0.23484 | 0.21367 | 0.17596 |

| Command |  Median 3.6 [s] | Median 3.7 [s] | Median 3.8 [s] | Median 3.9 [s] | Median 3.10 [s] | Median 3.11 [s] |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 0.07859 | 0.06468 | 0.07106 | 0.07936 | 0.07409 | 0.0696 |
| `algorithm/twosum/twosum_naive.py` | 0.07898 | 0.06481 | 0.07132 | 0.07837 | 0.07453 | 0.07034 |
| `complex/classes/classes.py` | 0.04453 | 0.03713 | 0.03876 | 0.04169 | 0.03873 | 0.02003 |
| `complex/classes/dataclasses_.py` | -- | 0.09574 | 0.10271 | 0.12264 | 0.11558 | 0.10754 |
| `complex/classes/namedtuple_classes.py` | 0.09106 | 0.07462 | 0.08048 | 0.0885 | 0.08381 | 0.07883 |
| `complex/classes/simplenamespace.py` | 0.05858 | 0.03821 | 0.03974 | 0.04418 | 0.04105 | 0.02467 |
| `complex/classes/sloted_classes.py` | 0.04403 | 0.03709 | 0.03876 | 0.04133 | 0.03898 | 0.01979 |
| `dummy/dummy.py` | 0.0327 | 0.02686 | 0.02701 | 0.03086 | 0.02986 | 0.02148 |
| `long_run/database/postgresql.py` | 0.14392 | 0.12925 | 0.14176 | 0.15326 | 0.14344 | 0.14188 |
| `long_run/database/sqlite_.py` | 0.58051 | 0.5003 | 0.55334 | 0.58184 | 0.55835 | 0.55617 |
| `long_run/file/load_titanic_csv_pandas.py` | 0.6497 | 0.54187 | 0.59438 | 0.62935 | 0.59286 | 0.582 |
| `long_run/file/load_titanic_csv_python.py` | 0.06809 | 0.06151 | 0.06547 | 0.07144 | 0.06598 | 0.05632 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 3.58295 | 1.78199 | 1.71808 | 1.44823 |
| `long_run/processes/generate_fake_data.py` | 0.79618 | 0.71663 | 0.74774 | 0.79082 | 0.7509 | 0.74567 |
| `math/haversine.py` | 0.60057 | 0.57303 | 0.52402 | 0.58683 | 0.53771 | 0.45635 |
| `math/mandelbrot.py` | 14.89257 | 14.93387 | 14.95654 | 14.89641 | 14.86863 | 15.03949 |
| `math/pow_simple.py` | 0.44223 | 0.41512 | 0.41676 | 0.4179 | 0.39499 | 0.32066 |
| `math/pow_using_math.py` | 1.51745 | 1.40242 | 1.32649 | 1.3729 | 1.33259 | 1.16637 |
| `modules/json/json_module.py` | 0.41416 | 0.38179 | 0.35358 | 0.36578 | 0.33112 | 0.28129 |
| `modules/json/orjson_module.py` | 0.27103 | 0.20371 | 0.21268 | 0.23399 | 0.21355 | 0.17511 |

#### **Memory Usage**

| Command |  MEM 3.6 [MB] | MEM 3.7 [MB] | MEM 3.8 [MB] | MEM 3.9 [MB] | MEM 3.10 [MB] | MEM 3.11 [MB] |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 22.30352 | 20.15977 | 20.56016 | 21.71016 | 23.19609 | 25.725 |
| `algorithm/twosum/twosum_naive.py` | 22.31094 | 20.19883 | 20.63398 | 22.65859 | 22.6332 | 25.72305 |
| `complex/classes/classes.py` | 22.01914 | 20.08516 | 20.63594 | 21.99805 | 24.42383 | 26.88984 |
| `complex/classes/dataclasses_.py` | -- | 20.09258 | 20.66641 | 22.91289 | 23.64883 | 27.1375 |
| `complex/classes/namedtuple_classes.py` | 22.21367 | 20.26172 | 20.37227 | 22.8207 | 23.68086 | 26.53594 |
| `complex/classes/simplenamespace.py` | 21.91641 | 20.14219 | 20.74687 | 22.62031 | 24.00742 | 26.9668 |
| `complex/classes/sloted_classes.py` | 21.99727 | 20.09219 | 20.76523 | 22.67617 | 24.0293 | 26.99727 |
| `dummy/dummy.py` | 21.66172 | 19.99727 | 20.47305 | 22.86289 | 22.48398 | 25.875 |
| `long_run/database/postgresql.py` | 26.83789 | 24.46992 | 24.48242 | 26.44844 | 28.06367 | 29.84531 |
| `long_run/database/sqlite_.py` | 62.96563 | 65.25664 | 65.32969 | 66.6082 | 65.78984 | 71.35781 |
| `long_run/file/load_titanic_csv_pandas.py` | 61.78672 | 63.89883 | 64.05547 | 64.49258 | 64.35508 | 69.49727 |
| `long_run/file/load_titanic_csv_python.py` | 22.15313 | 20.08906 | 20.72539 | 22.37148 | 23.22383 | 26.01836 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 44.71523 | 44.76133 | 44.98203 | 47.14023 |
| `long_run/processes/generate_fake_data.py` | 64.55469 | 68.58633 | 65.55117 | 68.67773 | 67.69922 | 72.33789 |
| `math/haversine.py` | 21.80703 | 20.26016 | 20.59102 | 22.54609 | 22.71992 | 25.70742 |
| `math/mandelbrot.py` | 36.47578 | 34.64805 | 34.9332 | 35.75039 | 35.96211 | 39.05898 |
| `math/pow_simple.py` | 21.76406 | 20.06055 | 20.61289 | 22.57773 | 22.76367 | 25.74961 |
| `math/pow_using_math.py` | 21.71602 | 20.15664 | 20.61445 | 22.44375 | 22.48281 | 25.70078 |
| `modules/json/json_module.py` | 21.90547 | 21.28594 | 21.18711 | 21.82578 | 23.29687 | 25.8668 |
| `modules/json/orjson_module.py` | 22.63203 | 21.59375 | 21.575 | 23.47383 | 23.09141 | 26.48242 |

---


### **Python 3.6**

```bash
Python 3.6.15

Linux 7d7e8bc36590 5.15.0-56-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         3902772 kB
MemAvailable:   14255220 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.03317 | 0.00129 | 0.0327 | 0.03206 | 0.03633 | 21.66172 |
| `long_run/processes/generate_fake_data.py` | yes | 0.79643 | 0.00514 | 0.79618 | 0.78726 | 0.8029 | 64.55469 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/database/sqlite_.py` | yes | 0.58246 | 0.00528 | 0.58051 | 0.57692 | 0.59407 | 62.96563 |
| `long_run/database/postgresql.py` | yes | 0.14391 | 0.00068 | 0.14392 | 0.14274 | 0.14478 | 26.83789 |
| `math/haversine.py` | yes | 0.60174 | 0.01125 | 0.60057 | 0.58856 | 0.62069 | 21.80703 |
| `math/pow_using_math.py` | yes | 1.53539 | 0.06122 | 1.51745 | 1.4926 | 1.70583 | 21.71602 |
| `math/mandelbrot.py` | yes | 14.87851 | 0.25374 | 14.89257 | 14.55218 | 15.427 | 36.47578 |
| `math/pow_simple.py` | yes | 0.44462 | 0.00747 | 0.44223 | 0.43868 | 0.46181 | 21.76406 |
| `modules/json/json_module.py` | yes | 0.41398 | 0.00264 | 0.41416 | 0.4092 | 0.41794 | 21.90547 |
| `modules/json/orjson_module.py` | yes | 0.27308 | 0.00968 | 0.27103 | 0.26155 | 0.29038 | 22.63203 |
| `complex/classes/namedtuple_classes.py` | yes | 0.09125 | 0.00139 | 0.09106 | 0.08979 | 0.09478 | 22.21367 |
| `complex/classes/classes.py` | yes | 0.04447 | 0.00045 | 0.04453 | 0.04372 | 0.04509 | 22.01914 |
| `complex/classes/dataclasses_.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `complex/classes/sloted_classes.py` | yes | 0.04402 | 0.00038 | 0.04403 | 0.04357 | 0.04473 | 21.99727 |
| `complex/classes/simplenamespace.py` | yes | 0.05873 | 0.00045 | 0.05858 | 0.05829 | 0.05938 | 21.91641 |
| `algorithm/twosum/twosum.py` | yes | 0.07874 | 0.00091 | 0.07859 | 0.07753 | 0.08032 | 22.30352 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07906 | 0.00097 | 0.07898 | 0.07769 | 0.08077 | 22.31094 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06826 | 0.00074 | 0.06809 | 0.06731 | 0.06981 | 22.15313 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.64872 | 0.00427 | 0.6497 | 0.64312 | 0.6547 | 61.78672 |


### **Python 3.7**

```bash
Python 3.7.16

Linux 01dd7e01f17b 5.15.0-56-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         3884584 kB
MemAvailable:   14240500 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.02688 | 0.00033 | 0.02686 | 0.02625 | 0.02729 | 19.99727 |
| `long_run/processes/generate_fake_data.py` | yes | 0.71822 | 0.00757 | 0.71663 | 0.70895 | 0.73246 | 68.58633 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/database/sqlite_.py` | yes | 0.5007 | 0.00361 | 0.5003 | 0.49647 | 0.50925 | 65.25664 |
| `long_run/database/postgresql.py` | yes | 0.13061 | 0.00455 | 0.12925 | 0.12845 | 0.14346 | 24.46992 |
| `math/haversine.py` | yes | 0.57456 | 0.01134 | 0.57303 | 0.56122 | 0.59455 | 20.26016 |
| `math/pow_using_math.py` | yes | 1.44165 | 0.08011 | 1.40242 | 1.38993 | 1.64601 | 20.15664 |
| `math/mandelbrot.py` | yes | 14.93252 | 0.07694 | 14.93387 | 14.79167 | 15.08568 | 34.64805 |
| `math/pow_simple.py` | yes | 0.42284 | 0.01717 | 0.41512 | 0.41105 | 0.46533 | 20.06055 |
| `modules/json/json_module.py` | yes | 0.38385 | 0.00775 | 0.38179 | 0.37576 | 0.40267 | 21.28594 |
| `modules/json/orjson_module.py` | yes | 0.20406 | 0.0028 | 0.20371 | 0.20172 | 0.21123 | 21.59375 |
| `complex/classes/namedtuple_classes.py` | yes | 0.07472 | 0.00056 | 0.07462 | 0.07388 | 0.07594 | 20.26172 |
| `complex/classes/classes.py` | yes | 0.03716 | 0.00066 | 0.03713 | 0.03609 | 0.03861 | 20.08516 |
| `complex/classes/dataclasses_.py` | yes | 0.09606 | 0.00099 | 0.09574 | 0.09514 | 0.09817 | 20.09258 |
| `complex/classes/sloted_classes.py` | yes | 0.03705 | 0.0003 | 0.03709 | 0.03652 | 0.03743 | 20.09219 |
| `complex/classes/simplenamespace.py` | yes | 0.03838 | 0.00063 | 0.03821 | 0.03778 | 0.03977 | 20.14219 |
| `algorithm/twosum/twosum.py` | yes | 0.06473 | 0.00045 | 0.06468 | 0.0641 | 0.06549 | 20.15977 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.06478 | 0.0007 | 0.06481 | 0.06389 | 0.06594 | 20.19883 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06148 | 0.00053 | 0.06151 | 0.06039 | 0.06216 | 20.08906 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.54405 | 0.00686 | 0.54187 | 0.53951 | 0.5625 | 63.89883 |


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
Python 3.9.16

Linux 7e1990e6afc1 5.15.0-56-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         3882300 kB
MemAvailable:   14242380 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.03108 | 0.00082 | 0.03086 | 0.03059 | 0.03336 | 22.86289 |
| `long_run/processes/generate_fake_data.py` | yes | 0.7926 | 0.0143 | 0.79082 | 0.77834 | 0.82801 | 68.67773 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.83386 | 0.19702 | 1.78199 | 1.71966 | 2.39015 | 44.76133 |
| `long_run/database/sqlite_.py` | yes | 0.58384 | 0.00679 | 0.58184 | 0.57677 | 0.60161 | 66.6082 |
| `long_run/database/postgresql.py` | yes | 0.15335 | 0.00095 | 0.15326 | 0.15219 | 0.15532 | 26.44844 |
| `math/haversine.py` | yes | 0.58674 | 0.01007 | 0.58683 | 0.56299 | 0.60048 | 22.54609 |
| `math/pow_using_math.py` | yes | 1.38163 | 0.02626 | 1.3729 | 1.35666 | 1.44589 | 22.44375 |
| `math/mandelbrot.py` | yes | 14.91929 | 0.14673 | 14.89641 | 14.66988 | 15.25113 | 35.75039 |
| `math/pow_simple.py` | yes | 0.42164 | 0.00956 | 0.4179 | 0.41438 | 0.44014 | 22.57773 |
| `modules/json/json_module.py` | yes | 0.36472 | 0.0052 | 0.36578 | 0.35446 | 0.37304 | 21.82578 |
| `modules/json/orjson_module.py` | yes | 0.23484 | 0.00315 | 0.23399 | 0.23042 | 0.24171 | 23.47383 |
| `complex/classes/namedtuple_classes.py` | yes | 0.08875 | 0.00129 | 0.0885 | 0.08759 | 0.09198 | 22.8207 |
| `complex/classes/classes.py` | yes | 0.04173 | 0.00072 | 0.04169 | 0.04096 | 0.04322 | 21.99805 |
| `complex/classes/dataclasses_.py` | yes | 0.12308 | 0.00137 | 0.12264 | 0.12242 | 0.12693 | 22.91289 |
| `complex/classes/sloted_classes.py` | yes | 0.0413 | 0.00033 | 0.04133 | 0.04078 | 0.04186 | 22.67617 |
| `complex/classes/simplenamespace.py` | yes | 0.04433 | 0.0004 | 0.04418 | 0.0439 | 0.04507 | 22.62031 |
| `algorithm/twosum/twosum.py` | yes | 0.07915 | 0.0006 | 0.07936 | 0.07832 | 0.08 | 21.71016 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07836 | 0.00062 | 0.07837 | 0.07728 | 0.07937 | 22.65859 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.07158 | 0.00083 | 0.07144 | 0.07039 | 0.07283 | 22.37148 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.63091 | 0.01104 | 0.62935 | 0.62128 | 0.66032 | 64.49258 |


### **Python 3.10**

```bash
Python 3.10.9

Linux 1efd6fdbce2b 5.15.0-56-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         3882104 kB
MemAvailable:   14243368 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.02991 | 0.00043 | 0.02986 | 0.0292 | 0.0308 | 22.48398 |
| `long_run/processes/generate_fake_data.py` | yes | 0.75146 | 0.00481 | 0.7509 | 0.74552 | 0.75949 | 67.69922 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.72493 | 0.04499 | 1.71808 | 1.67308 | 1.83852 | 44.98203 |
| `long_run/database/sqlite_.py` | yes | 0.56043 | 0.00831 | 0.55835 | 0.55363 | 0.5816 | 65.78984 |
| `long_run/database/postgresql.py` | yes | 0.14422 | 0.00246 | 0.14344 | 0.14169 | 0.15006 | 28.06367 |
| `math/haversine.py` | yes | 0.54121 | 0.01171 | 0.53771 | 0.52176 | 0.5573 | 22.71992 |
| `math/pow_using_math.py` | yes | 1.3311 | 0.02303 | 1.33259 | 1.29877 | 1.36722 | 22.48281 |
| `math/mandelbrot.py` | yes | 14.87439 | 0.21113 | 14.86863 | 14.6014 | 15.2672 | 35.96211 |
| `math/pow_simple.py` | yes | 0.40156 | 0.01362 | 0.39499 | 0.39112 | 0.43502 | 22.76367 |
| `modules/json/json_module.py` | yes | 0.33059 | 0.00504 | 0.33112 | 0.32167 | 0.33648 | 23.29687 |
| `modules/json/orjson_module.py` | yes | 0.21367 | 0.00154 | 0.21355 | 0.21178 | 0.21654 | 23.09141 |
| `complex/classes/namedtuple_classes.py` | yes | 0.08383 | 0.0003 | 0.08381 | 0.08342 | 0.08426 | 23.68086 |
| `complex/classes/classes.py` | yes | 0.0389 | 0.00048 | 0.03873 | 0.03825 | 0.03963 | 24.42383 |
| `complex/classes/dataclasses_.py` | yes | 0.1156 | 0.00054 | 0.11558 | 0.11461 | 0.1167 | 23.64883 |
| `complex/classes/sloted_classes.py` | yes | 0.03906 | 0.00044 | 0.03898 | 0.03859 | 0.03986 | 24.0293 |
| `complex/classes/simplenamespace.py` | yes | 0.0418 | 0.00286 | 0.04105 | 0.04026 | 0.04988 | 24.00742 |
| `algorithm/twosum/twosum.py` | yes | 0.074 | 0.00043 | 0.07409 | 0.07333 | 0.07463 | 23.19609 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07451 | 0.00042 | 0.07453 | 0.07391 | 0.07511 | 22.6332 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06738 | 0.00456 | 0.06598 | 0.06546 | 0.08032 | 23.22383 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.5942 | 0.00747 | 0.59286 | 0.58522 | 0.60878 | 64.35508 |


### **Python 3.11**

```bash
Python 3.11.1

Linux 468005a4cacf 5.15.0-56-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         3870328 kB
MemAvailable:   14233156 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.02151 | 0.0024 | 0.02148 | 0.01816 | 0.02483 | 25.875 |
| `long_run/processes/generate_fake_data.py` | yes | 0.74651 | 0.00358 | 0.74567 | 0.74171 | 0.75156 | 72.33789 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.44826 | 0.01178 | 1.44823 | 1.43574 | 1.46984 | 47.14023 |
| `long_run/database/sqlite_.py` | yes | 0.55568 | 0.00204 | 0.55617 | 0.55282 | 0.55912 | 71.35781 |
| `long_run/database/postgresql.py` | yes | 0.14188 | 0.00109 | 0.14188 | 0.14027 | 0.14347 | 29.84531 |
| `math/haversine.py` | yes | 0.45497 | 0.00543 | 0.45635 | 0.44542 | 0.46381 | 25.70742 |
| `math/pow_using_math.py` | yes | 1.16648 | 0.00464 | 1.16637 | 1.15586 | 1.17204 | 25.70078 |
| `math/mandelbrot.py` | yes | 15.0777 | 0.13212 | 15.03949 | 14.92236 | 15.296 | 39.05898 |
| `math/pow_simple.py` | yes | 0.32654 | 0.00953 | 0.32066 | 0.31802 | 0.34081 | 25.74961 |
| `modules/json/json_module.py` | yes | 0.28104 | 0.00167 | 0.28129 | 0.27763 | 0.2833 | 25.8668 |
| `modules/json/orjson_module.py` | yes | 0.17596 | 0.00335 | 0.17511 | 0.17247 | 0.18246 | 26.48242 |
| `complex/classes/namedtuple_classes.py` | yes | 0.07918 | 0.00089 | 0.07883 | 0.07815 | 0.08074 | 26.53594 |
| `complex/classes/classes.py` | yes | 0.02011 | 0.00058 | 0.02003 | 0.01932 | 0.02096 | 26.88984 |
| `complex/classes/dataclasses_.py` | yes | 0.10843 | 0.00263 | 0.10754 | 0.10674 | 0.11552 | 27.1375 |
| `complex/classes/sloted_classes.py` | yes | 0.01993 | 0.00051 | 0.01979 | 0.01952 | 0.0213 | 26.99727 |
| `complex/classes/simplenamespace.py` | yes | 0.02451 | 0.00036 | 0.02467 | 0.02384 | 0.02487 | 26.9668 |
| `algorithm/twosum/twosum.py` | yes | 0.0696 | 0.00048 | 0.0696 | 0.06867 | 0.07036 | 25.725 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07038 | 0.00052 | 0.07034 | 0.06969 | 0.07136 | 25.72305 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.05654 | 0.00097 | 0.05632 | 0.05575 | 0.0591 | 26.01836 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.58249 | 0.00342 | 0.582 | 0.5788 | 0.59119 | 69.49727 |

