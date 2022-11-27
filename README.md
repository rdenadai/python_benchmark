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
> Last run: Sat Nov 26 11:23:04 AM -03 2022
### **Comparison**

#### How much faster 3.11 is? (Mean / Median from 3.6 to 3.10)
| Command | 3.6 (Mean / Median) | 3.7 (...) | 3.8 (...) | 3.9 (...) | 3.10 (...) |
|:---|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 15.23% / 13.60% | -6.46% / -6.44% | 2.65% / 2.24% | 13.69% / 13.01% | 8.14% / 8.20% |
| `algorithm/twosum/twosum_naive.py` | 13.86% / 13.67% | -4.45% / -6.08% | 3.21% / 3.07% | 13.86% / 13.81% | 8.38% / 8.19% |
| `complex/classes/classes.py` | 127.60% / 132.30% | 90.51% / 95.01% | 105.08% / 104.46% | 111.44% / 116.23% | 102.36% / 107.77% |
| `complex/classes/dataclasses_.py` | -- / -- | -10.83% / -10.80% | -3.15% / -3.16% | 14.11% / 14.17% | 7.29% / 7.06% |
| `complex/classes/namedtuple_classes.py` | 18.70% / 19.21% | -3.33% / -3.11% | 4.83% / 3.43% | 12.41% / 12.66% | 7.32% / 7.45% |
| `complex/classes/simplenamespace.py` | 138.21% / 141.07% | 53.41% / 54.19% | 62.27% / 63.59% | 77.43% / 79.44% | 64.77% / 67.02% |
| `complex/classes/sloted_classes.py` | 100.09% / 104.00% | 66.49% / 71.21% | 73.69% / 78.06% | 85.23% / 90.43% | 76.82% / 79.71% |
| `dummy/dummy.py` | 101.09% / 91.57% | 63.57% / 58.46% | 74.86% / 69.00% | 96.84% / 83.32% | 80.69% / 75.55% |
| `long_run/database/postgresql.py` | 2.41% / 2.64% | -5.65% / -6.34% | 1.55% / 1.34% | 9.05% / 9.22% | 2.08% / 1.81% |
| `long_run/file/load_titanic_csv_pandas.py` | 14.45% / 14.13% | -6.71% / -7.10% | 2.44% / 2.38% | 7.86% / 7.90% | 1.92% / 2.08% |
| `long_run/file/load_titanic_csv_python.py` | 24.49% / 22.86% | 10.36% / 10.05% | 18.27% / 18.11% | 28.30% / 28.13% | 18.71% / 18.34% |
| `long_run/processes/collect_names_from_site.py` | -- / -- | -- / -- | 20.83% / 20.85% | 24.66% / 23.70% | 19.41% / 19.19% |
| `long_run/processes/generate_fake_data.py` | 8.31% / 8.17% | -3.87% / -3.83% | 0.36% / 0.33% | 6.56% / 6.23% | 1.59% / 1.41% |
| `math/haversine.py` | 31.14% / 30.55% | 23.54% / 23.82% | 10.66% / 11.06% | 22.47% / 23.85% | 14.06% / 14.74% |
| `math/pow_simple.py` | 41.31% / 40.98% | 33.94% / 33.58% | 33.75% / 33.35% | 32.78% / 31.50% | 25.54% / 25.14% |
| `math/pow_using_math.py` | 37.77% / 37.45% | 22.23% / 21.56% | 16.76% / 15.54% | 18.75% / 19.51% | 17.82% / 17.40% |
| `modules/json/json_module.py` | 47.67% / 48.99% | 37.69% / 36.83% | 26.39% / 27.56% | 34.19% / 34.74% | 19.06% / 19.79% |
| `modules/json/orjson_module.py` | 53.38% / 53.14% | 19.82% / 19.95% | 28.06% / 24.80% | 37.60% / 37.09% | 26.73% / 26.66% |
---

#### How much more memory 3.11 uses? (Memory from 3.6 to 3.10)
| Command |  3.6 | 3.7 | 3.8 | 3.9 | 3.10 |
|:---|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 16.75% | 29.09% | 26.01% | 20.49% | 16.97% |
| `algorithm/twosum/twosum_naive.py` | 16.13% | 28.67% | 25.08% | 14.54% | 11.66% |
| `complex/classes/classes.py` | 23.84% | 36.6% | 33.75% | 26.47% | 17.91% |
| `complex/classes/dataclasses_.py` | -- | 36.73% | 31.97% | 19.66% | 17.71% |
| `complex/classes/namedtuple_classes.py` | 18.78% | 31.29% | 27.99% | 15.93% | 10.89% |
| `complex/classes/simplenamespace.py` | 24.18% | 33.48% | 32.33% | 21.32% | 11.05% |
| `complex/classes/sloted_classes.py` | 24.65% | 36.35% | 32.16% | 21.0% | 11.89% |
| `dummy/dummy.py` | 19.87% | 28.8% | 26.04% | 13.48% | 13.41% |
| `long_run/database/postgresql.py` | 18.24% | 30.93% | 29.69% | 20.53% | 22.64% |
| `long_run/file/load_titanic_csv_pandas.py` | 11.66% | 9.23% | 8.68% | 6.3% | 9.62% |
| `long_run/file/load_titanic_csv_python.py` | 17.41% | 29.65% | 25.01% | 17.16% | 12.66% |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 5.87% | 5.7% | 5.45% |
| `long_run/processes/generate_fake_data.py` | 11.13% | 5.87% | 10.56% | 5.64% | 7.1% |
| `math/haversine.py` | 17.74% | 27.72% | 24.75% | 14.16% | 13.5% |
| `math/pow_simple.py` | 17.75% | 28.44% | 24.76% | 13.93% | 15.07% |
| `math/pow_using_math.py` | 20.74% | 30.89% | 27.06% | 17.47% | 13.23% |
| `modules/json/json_module.py` | 19.97% | 22.98% | 23.36% | 20.12% | 17.68% |
| `modules/json/orjson_module.py` | 18.44% | 24.76% | 24.24% | 14.73% | 17.8% |
---

#### **Execution**

| Command |  Mean 3.6 [s] | Mean 3.7 [s] | Mean 3.8 [s] | Mean 3.9 [s] | Mean 3.10 [s] | Mean 3.11 [s] |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 0.08012 | 0.06504 | 0.07137 | 0.07905 | 0.07519 | 0.06953 |
| `algorithm/twosum/twosum_naive.py` | 0.07863 | 0.06599 | 0.07128 | 0.07863 | 0.07485 | 0.06906 |
| `complex/classes/classes.py` | 0.04436 | 0.03713 | 0.03997 | 0.04121 | 0.03944 | 0.01949 |
| `complex/classes/dataclasses_.py` | -- | 0.09571 | 0.10396 | 0.12249 | 0.11517 | 0.10734 |
| `complex/classes/namedtuple_classes.py` | 0.09313 | 0.07585 | 0.08225 | 0.0882 | 0.0842 | 0.07846 |
| `complex/classes/simplenamespace.py` | 0.0591 | 0.03806 | 0.04026 | 0.04402 | 0.04088 | 0.02481 |
| `complex/classes/sloted_classes.py` | 0.04472 | 0.03721 | 0.03882 | 0.0414 | 0.03952 | 0.02235 |
| `dummy/dummy.py` | 0.03312 | 0.02694 | 0.0288 | 0.03242 | 0.02976 | 0.01647 |
| `long_run/database/postgresql.py` | 0.14422 | 0.13287 | 0.143 | 0.15356 | 0.14375 | 0.14082 |
| `long_run/file/load_titanic_csv_pandas.py` | 0.66368 | 0.541 | 0.59405 | 0.62548 | 0.59106 | 0.5799 |
| `long_run/file/load_titanic_csv_python.py` | 0.06894 | 0.06112 | 0.0655 | 0.07105 | 0.06574 | 0.05538 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 1.73577 | 1.79078 | 1.7154 | 1.43654 |
| `long_run/processes/generate_fake_data.py` | 0.80236 | 0.71216 | 0.74352 | 0.78939 | 0.75261 | 0.74082 |
| `math/haversine.py` | 0.61803 | 0.58219 | 0.52151 | 0.57715 | 0.53754 | 0.47127 |
| `math/pow_simple.py` | 0.44517 | 0.42196 | 0.42136 | 0.41831 | 0.39549 | 0.31503 |
| `math/pow_using_math.py` | 1.59405 | 1.41425 | 1.35104 | 1.374 | 1.36321 | 1.15706 |
| `modules/json/json_module.py` | 0.4105 | 0.38276 | 0.35134 | 0.37303 | 0.33097 | 0.27798 |
| `modules/json/orjson_module.py` | 0.26228 | 0.2049 | 0.21898 | 0.2353 | 0.21671 | 0.171 |

| Command |  Median 3.6 [s] | Median 3.7 [s] | Median 3.8 [s] | Median 3.9 [s] | Median 3.10 [s] | Median 3.11 [s] |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 0.079 | 0.06506 | 0.0711 | 0.07859 | 0.07524 | 0.06954 |
| `algorithm/twosum/twosum_naive.py` | 0.07858 | 0.06493 | 0.07125 | 0.07868 | 0.07479 | 0.06913 |
| `complex/classes/classes.py` | 0.04423 | 0.03713 | 0.03893 | 0.04117 | 0.03956 | 0.01904 |
| `complex/classes/dataclasses_.py` | -- | 0.09566 | 0.10385 | 0.12244 | 0.11481 | 0.10724 |
| `complex/classes/namedtuple_classes.py` | 0.0934 | 0.07591 | 0.08104 | 0.08827 | 0.08419 | 0.07835 |
| `complex/classes/simplenamespace.py` | 0.05899 | 0.03773 | 0.04003 | 0.04391 | 0.04087 | 0.02447 |
| `complex/classes/sloted_classes.py` | 0.04435 | 0.03722 | 0.03871 | 0.0414 | 0.03907 | 0.02174 |
| `dummy/dummy.py` | 0.03251 | 0.02689 | 0.02868 | 0.03111 | 0.02979 | 0.01697 |
| `long_run/database/postgresql.py` | 0.14431 | 0.13169 | 0.14248 | 0.15356 | 0.14314 | 0.1406 |
| `long_run/file/load_titanic_csv_pandas.py` | 0.66173 | 0.53867 | 0.59361 | 0.6256 | 0.5919 | 0.57982 |
| `long_run/file/load_titanic_csv_python.py` | 0.06819 | 0.06108 | 0.06555 | 0.07111 | 0.06568 | 0.0555 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 1.73762 | 1.77857 | 1.71371 | 1.43784 |
| `long_run/processes/generate_fake_data.py` | 0.80146 | 0.71256 | 0.74333 | 0.78708 | 0.75134 | 0.7409 |
| `math/haversine.py` | 0.60929 | 0.57786 | 0.51834 | 0.578 | 0.5355 | 0.46671 |
| `math/pow_simple.py` | 0.44405 | 0.42074 | 0.42001 | 0.41419 | 0.39416 | 0.31497 |
| `math/pow_using_math.py` | 1.58502 | 1.40175 | 1.33229 | 1.37807 | 1.35376 | 1.15314 |
| `modules/json/json_module.py` | 0.41043 | 0.37693 | 0.3514 | 0.37118 | 0.33 | 0.27548 |
| `modules/json/orjson_module.py` | 0.26191 | 0.20515 | 0.21345 | 0.23446 | 0.21663 | 0.17103 |

#### **Memory Usage**

| Command |  MEM 3.6 [MB] | MEM 3.7 [MB] | MEM 3.8 [MB] | MEM 3.9 [MB] | MEM 3.10 [MB] | MEM 3.11 [MB] |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/twosum/twosum.py` | 22.21758 | 20.09336 | 20.58398 | 21.52813 | 22.17617 | 25.93867 |
| `algorithm/twosum/twosum_naive.py` | 22.24219 | 20.07383 | 20.65 | 22.54922 | 23.13125 | 25.82891 |
| `complex/classes/classes.py` | 22.12031 | 20.05391 | 20.48125 | 21.66094 | 23.2332 | 27.39414 |
| `complex/classes/dataclasses_.py` | -- | 20.0043 | 20.72539 | 22.85859 | 23.23633 | 27.35195 |
| `complex/classes/namedtuple_classes.py` | 22.19727 | 20.08242 | 20.60039 | 22.74336 | 23.77812 | 26.3668 |
| `complex/classes/simplenamespace.py` | 21.98984 | 20.45703 | 20.63633 | 22.50781 | 24.58984 | 27.30703 |
| `complex/classes/sloted_classes.py` | 21.92344 | 20.04219 | 20.67695 | 22.58398 | 24.42383 | 27.32695 |
| `dummy/dummy.py` | 21.50273 | 20.01172 | 20.44922 | 22.71328 | 22.72812 | 25.775 |
| `long_run/database/postgresql.py` | 26.70508 | 24.11641 | 24.34688 | 26.19727 | 25.74727 | 31.57617 |
| `long_run/file/load_titanic_csv_pandas.py` | 61.73633 | 63.10938 | 63.42695 | 64.85039 | 62.88359 | 68.93438 |
| `long_run/file/load_titanic_csv_python.py` | 22.07578 | 19.99141 | 20.7332 | 22.12344 | 23.00703 | 25.91914 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 44.57227 | 44.64375 | 44.75 | 47.18906 |
| `long_run/processes/generate_fake_data.py` | 64.65352 | 67.86602 | 64.98633 | 68.01055 | 67.08281 | 71.84766 |
| `math/haversine.py` | 21.79766 | 20.09375 | 20.57305 | 22.48203 | 22.61211 | 25.66445 |
| `math/pow_simple.py` | 21.73633 | 19.92695 | 20.51523 | 22.46523 | 22.24219 | 25.59414 |
| `math/pow_using_math.py` | 21.68242 | 20.00117 | 20.60312 | 22.28477 | 23.11914 | 26.17891 |
| `modules/json/json_module.py` | 21.76914 | 21.2375 | 21.17148 | 21.74219 | 22.19336 | 26.11719 |
| `modules/json/orjson_module.py` | 22.59766 | 21.45195 | 21.54141 | 23.32773 | 22.71914 | 26.76406 |

---


### **Python 3.6**

```bash
Python 3.6.15

Linux b39e2b5c7919 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         4969044 kB
MemAvailable:   14456964 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.03312 | 0.00171 | 0.03251 | 0.03236 | 0.03795 | 21.50273 |
| `long_run/processes/generate_fake_data.py` | yes | 0.80236 | 0.00447 | 0.80146 | 0.79616 | 0.81018 | 64.65352 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/database/postgresql.py` | yes | 0.14422 | 0.00198 | 0.14431 | 0.14186 | 0.14899 | 26.70508 |
| `math/haversine.py` | yes | 0.61803 | 0.02527 | 0.60929 | 0.59697 | 0.68087 | 21.79766 |
| `math/pow_using_math.py` | yes | 1.59405 | 0.07067 | 1.58502 | 1.49987 | 1.69209 | 21.68242 |
| `math/pow_simple.py` | yes | 0.44517 | 0.00759 | 0.44405 | 0.43669 | 0.4588 | 21.73633 |
| `modules/json/json_module.py` | yes | 0.4105 | 0.00639 | 0.41043 | 0.39936 | 0.42147 | 21.76914 |
| `modules/json/orjson_module.py` | yes | 0.26228 | 0.00313 | 0.26191 | 0.25723 | 0.2671 | 22.59766 |
| `complex/classes/namedtuple_classes.py` | yes | 0.09313 | 0.00161 | 0.0934 | 0.0908 | 0.09587 | 22.19727 |
| `complex/classes/classes.py` | yes | 0.04436 | 0.00047 | 0.04423 | 0.04373 | 0.04549 | 22.12031 |
| `complex/classes/dataclasses_.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `complex/classes/sloted_classes.py` | yes | 0.04472 | 0.0015 | 0.04435 | 0.04321 | 0.04878 | 21.92344 |
| `complex/classes/simplenamespace.py` | yes | 0.0591 | 0.00076 | 0.05899 | 0.05835 | 0.06097 | 21.98984 |
| `algorithm/twosum/twosum.py` | yes | 0.08012 | 0.00322 | 0.079 | 0.07771 | 0.0884 | 22.21758 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07863 | 0.00036 | 0.07858 | 0.07801 | 0.07922 | 22.24219 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06894 | 0.0023 | 0.06819 | 0.06727 | 0.07516 | 22.07578 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.66368 | 0.00568 | 0.66173 | 0.65768 | 0.67677 | 61.73633 |


### **Python 3.7**

```bash
Python 3.7.15

Linux b80b1d1d90db 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         4950156 kB
MemAvailable:   14438856 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.02694 | 0.00015 | 0.02689 | 0.02678 | 0.0272 | 20.01172 |
| `long_run/processes/generate_fake_data.py` | yes | 0.71216 | 0.00277 | 0.71256 | 0.70575 | 0.71463 | 67.86602 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/database/postgresql.py` | yes | 0.13287 | 0.00488 | 0.13169 | 0.12857 | 0.14553 | 24.11641 |
| `math/haversine.py` | yes | 0.58219 | 0.01498 | 0.57786 | 0.56552 | 0.6071 | 20.09375 |
| `math/pow_using_math.py` | yes | 1.41425 | 0.03359 | 1.40175 | 1.36173 | 1.45877 | 20.00117 |
| `math/pow_simple.py` | yes | 0.42196 | 0.01254 | 0.42074 | 0.40874 | 0.44618 | 19.92695 |
| `modules/json/json_module.py` | yes | 0.38276 | 0.01273 | 0.37693 | 0.37011 | 0.41386 | 21.2375 |
| `modules/json/orjson_module.py` | yes | 0.2049 | 0.00178 | 0.20515 | 0.2012 | 0.20681 | 21.45195 |
| `complex/classes/namedtuple_classes.py` | yes | 0.07585 | 0.0012 | 0.07591 | 0.07428 | 0.07769 | 20.08242 |
| `complex/classes/classes.py` | yes | 0.03713 | 0.00043 | 0.03713 | 0.03654 | 0.038 | 20.05391 |
| `complex/classes/dataclasses_.py` | yes | 0.09571 | 0.00082 | 0.09566 | 0.09445 | 0.09702 | 20.0043 |
| `complex/classes/sloted_classes.py` | yes | 0.03721 | 0.00046 | 0.03722 | 0.03666 | 0.03792 | 20.04219 |
| `complex/classes/simplenamespace.py` | yes | 0.03806 | 0.00108 | 0.03773 | 0.0374 | 0.04104 | 20.45703 |
| `algorithm/twosum/twosum.py` | yes | 0.06504 | 0.00051 | 0.06506 | 0.06423 | 0.06566 | 20.09336 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.06599 | 0.00351 | 0.06493 | 0.0644 | 0.07592 | 20.07383 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06112 | 0.00031 | 0.06108 | 0.06073 | 0.06168 | 19.99141 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.541 | 0.005 | 0.53867 | 0.53721 | 0.55284 | 63.10938 |


### **Python 3.8**

```bash
Python 3.8.15

Linux c0c066bfb1bf 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         4971180 kB
MemAvailable:   14460940 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.0288 | 0.00042 | 0.02868 | 0.02831 | 0.02974 | 20.44922 |
| `long_run/processes/generate_fake_data.py` | yes | 0.74352 | 0.00331 | 0.74333 | 0.73963 | 0.74935 | 64.98633 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.73577 | 0.01893 | 1.73762 | 1.69396 | 1.76253 | 44.57227 |
| `long_run/database/postgresql.py` | yes | 0.143 | 0.00238 | 0.14248 | 0.14102 | 0.14957 | 24.34688 |
| `math/haversine.py` | yes | 0.52151 | 0.01388 | 0.51834 | 0.50623 | 0.54696 | 20.57305 |
| `math/pow_using_math.py` | yes | 1.35104 | 0.05197 | 1.33229 | 1.30793 | 1.48585 | 20.60312 |
| `math/pow_simple.py` | yes | 0.42136 | 0.00891 | 0.42001 | 0.40871 | 0.44109 | 20.51523 |
| `modules/json/json_module.py` | yes | 0.35134 | 0.00335 | 0.3514 | 0.34665 | 0.35698 | 21.17148 |
| `modules/json/orjson_module.py` | yes | 0.21898 | 0.01206 | 0.21345 | 0.21092 | 0.2467 | 21.54141 |
| `complex/classes/namedtuple_classes.py` | yes | 0.08225 | 0.00406 | 0.08104 | 0.08012 | 0.09374 | 20.60039 |
| `complex/classes/classes.py` | yes | 0.03997 | 0.00229 | 0.03893 | 0.03839 | 0.04449 | 20.48125 |
| `complex/classes/dataclasses_.py` | yes | 0.10396 | 0.00078 | 0.10385 | 0.10316 | 0.10584 | 20.72539 |
| `complex/classes/sloted_classes.py` | yes | 0.03882 | 0.00051 | 0.03871 | 0.0379 | 0.03965 | 20.67695 |
| `complex/classes/simplenamespace.py` | yes | 0.04026 | 0.00078 | 0.04003 | 0.03962 | 0.04231 | 20.63633 |
| `algorithm/twosum/twosum.py` | yes | 0.07137 | 0.00063 | 0.0711 | 0.07067 | 0.07231 | 20.58398 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07128 | 0.00072 | 0.07125 | 0.0701 | 0.07264 | 20.65 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.0655 | 0.00035 | 0.06555 | 0.06489 | 0.06605 | 20.7332 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.59405 | 0.00503 | 0.59361 | 0.58847 | 0.60115 | 63.42695 |


### **Python 3.9**

```bash
Python 3.9.15

Linux f43fc35d1971 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         4955784 kB
MemAvailable:   14446400 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.03242 | 0.00472 | 0.03111 | 0.03027 | 0.04579 | 22.71328 |
| `long_run/processes/generate_fake_data.py` | yes | 0.78939 | 0.00952 | 0.78708 | 0.7804 | 0.8117 | 68.01055 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.79078 | 0.02788 | 1.77857 | 1.75381 | 1.82857 | 44.64375 |
| `long_run/database/postgresql.py` | yes | 0.15356 | 0.00069 | 0.15356 | 0.15217 | 0.15426 | 26.19727 |
| `math/haversine.py` | yes | 0.57715 | 0.00776 | 0.578 | 0.56678 | 0.58948 | 22.48203 |
| `math/pow_using_math.py` | yes | 1.374 | 0.01259 | 1.37807 | 1.35593 | 1.39368 | 22.28477 |
| `math/pow_simple.py` | yes | 0.41831 | 0.00728 | 0.41419 | 0.41292 | 0.43293 | 22.46523 |
| `modules/json/json_module.py` | yes | 0.37303 | 0.00886 | 0.37118 | 0.36243 | 0.39136 | 21.74219 |
| `modules/json/orjson_module.py` | yes | 0.2353 | 0.00207 | 0.23446 | 0.23268 | 0.23854 | 23.32773 |
| `complex/classes/namedtuple_classes.py` | yes | 0.0882 | 0.00047 | 0.08827 | 0.08735 | 0.08881 | 22.74336 |
| `complex/classes/classes.py` | yes | 0.04121 | 0.00044 | 0.04117 | 0.04075 | 0.04227 | 21.66094 |
| `complex/classes/dataclasses_.py` | yes | 0.12249 | 0.0004 | 0.12244 | 0.12178 | 0.12319 | 22.85859 |
| `complex/classes/sloted_classes.py` | yes | 0.0414 | 0.0005 | 0.0414 | 0.0405 | 0.04238 | 22.58398 |
| `complex/classes/simplenamespace.py` | yes | 0.04402 | 0.00031 | 0.04391 | 0.04372 | 0.04459 | 22.50781 |
| `algorithm/twosum/twosum.py` | yes | 0.07905 | 0.00136 | 0.07859 | 0.07788 | 0.08251 | 21.52813 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07863 | 0.0003 | 0.07868 | 0.0781 | 0.07902 | 22.54922 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.07105 | 0.00043 | 0.07111 | 0.07022 | 0.07155 | 22.12344 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.62548 | 0.00251 | 0.6256 | 0.62113 | 0.62899 | 64.85039 |


### **Python 3.10**

```bash
Python 3.10.8

Linux 2a18f956fd22 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         4929932 kB
MemAvailable:   14445392 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.02976 | 0.00028 | 0.02979 | 0.02928 | 0.03028 | 22.72812 |
| `long_run/processes/generate_fake_data.py` | yes | 0.75261 | 0.00798 | 0.75134 | 0.74312 | 0.7697 | 67.08281 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.7154 | 0.02346 | 1.71371 | 1.68068 | 1.74953 | 44.75 |
| `long_run/database/postgresql.py` | yes | 0.14375 | 0.00164 | 0.14314 | 0.14244 | 0.14731 | 25.74727 |
| `math/haversine.py` | yes | 0.53754 | 0.00992 | 0.5355 | 0.5272 | 0.56169 | 22.61211 |
| `math/pow_using_math.py` | yes | 1.36321 | 0.02929 | 1.35376 | 1.33291 | 1.41644 | 23.11914 |
| `math/pow_simple.py` | yes | 0.39549 | 0.0045 | 0.39416 | 0.39128 | 0.40565 | 22.24219 |
| `modules/json/json_module.py` | yes | 0.33097 | 0.00701 | 0.33 | 0.32035 | 0.34606 | 22.19336 |
| `modules/json/orjson_module.py` | yes | 0.21671 | 0.00434 | 0.21663 | 0.21136 | 0.22579 | 22.71914 |
| `complex/classes/namedtuple_classes.py` | yes | 0.0842 | 0.00055 | 0.08419 | 0.08361 | 0.08558 | 23.77812 |
| `complex/classes/classes.py` | yes | 0.03944 | 0.00054 | 0.03956 | 0.03854 | 0.04021 | 23.2332 |
| `complex/classes/dataclasses_.py` | yes | 0.11517 | 0.00138 | 0.11481 | 0.11398 | 0.11872 | 23.23633 |
| `complex/classes/sloted_classes.py` | yes | 0.03952 | 0.00147 | 0.03907 | 0.03863 | 0.04361 | 24.42383 |
| `complex/classes/simplenamespace.py` | yes | 0.04088 | 0.00045 | 0.04087 | 0.0402 | 0.04148 | 24.58984 |
| `algorithm/twosum/twosum.py` | yes | 0.07519 | 0.00047 | 0.07524 | 0.07441 | 0.07585 | 22.17617 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07485 | 0.00056 | 0.07479 | 0.07432 | 0.07617 | 23.13125 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06574 | 0.00023 | 0.06568 | 0.06547 | 0.06618 | 23.00703 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.59106 | 0.00248 | 0.5919 | 0.58656 | 0.59457 | 62.88359 |


### **Python 3.11**

```bash
Python 3.11.0

Linux 2293264c899c 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078824 kB
MemFree:         4927236 kB
MemAvailable:   14443732 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.01647 | 0.00441 | 0.01697 | 0.01196 | 0.02364 | 25.775 |
| `long_run/processes/generate_fake_data.py` | yes | 0.74082 | 0.00466 | 0.7409 | 0.73409 | 0.74763 | 71.84766 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.43654 | 0.01101 | 1.43784 | 1.41957 | 1.45354 | 47.18906 |
| `long_run/database/postgresql.py` | yes | 0.14082 | 0.00081 | 0.1406 | 0.13961 | 0.14223 | 31.57617 |
| `math/haversine.py` | yes | 0.47127 | 0.01905 | 0.46671 | 0.4501 | 0.50531 | 25.66445 |
| `math/pow_using_math.py` | yes | 1.15706 | 0.01117 | 1.15314 | 1.14462 | 1.17615 | 26.17891 |
| `math/pow_simple.py` | yes | 0.31503 | 0.00111 | 0.31497 | 0.31382 | 0.31731 | 25.59414 |
| `modules/json/json_module.py` | yes | 0.27798 | 0.00744 | 0.27548 | 0.27332 | 0.2987 | 26.11719 |
| `modules/json/orjson_module.py` | yes | 0.171 | 0.00084 | 0.17103 | 0.1697 | 0.17242 | 26.76406 |
| `complex/classes/namedtuple_classes.py` | yes | 0.07846 | 0.00041 | 0.07835 | 0.07779 | 0.07925 | 26.3668 |
| `complex/classes/classes.py` | yes | 0.01949 | 0.00154 | 0.01904 | 0.01875 | 0.02384 | 27.39414 |
| `complex/classes/dataclasses_.py` | yes | 0.10734 | 0.00044 | 0.10724 | 0.10661 | 0.10808 | 27.35195 |
| `complex/classes/sloted_classes.py` | yes | 0.02235 | 0.00293 | 0.02174 | 0.01922 | 0.02645 | 27.32695 |
| `complex/classes/simplenamespace.py` | yes | 0.02481 | 0.0009 | 0.02447 | 0.0241 | 0.02661 | 27.30703 |
| `algorithm/twosum/twosum.py` | yes | 0.06953 | 0.00051 | 0.06954 | 0.06887 | 0.07043 | 25.93867 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.06906 | 0.00037 | 0.06913 | 0.06856 | 0.0696 | 25.82891 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.05538 | 0.00049 | 0.0555 | 0.05472 | 0.05599 | 25.91914 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.5799 | 0.00369 | 0.57982 | 0.57601 | 0.58843 | 68.93438 |

