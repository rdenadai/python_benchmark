# Python Benchmark

This is a simple repo to validate and test any (almost any) python program againts all python 3 versions.

- Python 3.6.15
- Python 3.7.17
- Python 3.8.17
- Python 3.9.17
- Python 3.10.12
- Python 3.11.4
- Python 3.12b4

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
# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12
```

- @DONT_RUN: This file should not be executed (in case of utils routines);
- @MPROF_INTERVAL: To benchmark memory usage mprof is used, this param you maybe able to improve interval collect of memory;
- @MPROF_MULTIPROCESS: In case your program uses python multiprocess (possible params -M or -C, default: -C);
- @ALLOWED_VERSIONS: What python versions your program can be run: from 3.6 to 3.11;

## Results

> Last run: Sat Jul 15 23:08:27 UTC 2023
### **Comparison**

#### How much faster 3.12 is? (Mean / Median from 3.6 to 3.11)
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | -11.41% / -11.66% | -24.46% / -24.64% |
| `algorithm/search/hashmap_lookup.py` | -12.28% / -11.11% | -24.66% / -23.61% |
| `algorithm/search/index.py` | -10.99% / -10.82% | -23.24% / -23.25% |
| `algorithm/search/linear.py` | -10.69% / -10.18% | -23.44% / -22.98% |
| `algorithm/twosum/twosum.py` | -11.14% / -11.08% | -14.35% / -14.56% |
| `algorithm/twosum/twosum_naive.py` | -13.31% / -13.09% | -15.43% / -14.86% |
| `complex/classes/classes.py` | 98.38% / 84.08% | -9.54% / -8.26% |
| `complex/classes/dataclasses_.py` | -10.69% / -10.98% | -14.08% / -14.33% |
| `complex/classes/namedtuple_classes.py` | -9.35% / -8.92% | -15.75% / -15.42% |
| `complex/classes/simplenamespace.py` | 48.56% / 49.12% | -14.99% / -14.58% |
| `complex/classes/sloted_classes.py` | 81.62% / 80.11% | -12.63% / -13.73% |
| `complex/generators/simple.py` | 36.35% / 38.94% | -17.67% / -16.46% |
| `dummy/dummy.py` | 114.70% / 120.63% | -8.76% / -7.56% |
| `long_run/database/postgresql.py` | -16.37% / -16.17% | -17.73% / -18.30% |
| `long_run/database/sqlite_.py` | -- / -- | -- / -- |
| `long_run/file/load_titanic_csv_pandas.py` | -- / -- | -- / -- |
| `long_run/file/load_titanic_csv_python.py` | -1.17% / -0.78% | -9.32% / -9.50% |
| `long_run/processes/collect_names_from_site.py` | -- / -- | -- / -- |
| `long_run/processes/generate_fake_data.py` | -- / -- | -- / -- |
| `long_run/processes/maze_generator.py` | 30.07% / 27.78% | -12.33% / -13.27% |
| `long_run/text/clean_text.py` | 8.67% / 8.70% | -5.17% / -5.16% |
| `long_run/text/count_words.py` | 4.52% / 4.75% | -11.08% / -10.49% |
| `math/haversine.py` | -7.41% / -8.20% | -22.02% / -22.39% |
| `math/mandelbrot.py` | -- / -- | -- / -- |
| `math/pow_simple.py` | 24.36% / 23.98% | -9.52% / -10.03% |
| `math/pow_using_math.py` | 3.66% / 3.66% | -10.65% / -10.51% |
| `modules/json/json_module.py` | -3.71% / -4.10% | -10.40% / -11.06% |
| `modules/json/orjson_module.py` | -- / -- | -- / -- |
---

#### How much more memory 3.12 uses? (Memory diff from 3.6 to 3.11)
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 7.29% | -1.01% |
| `algorithm/search/hashmap_lookup.py` | 13.89% | -1.19% |
| `algorithm/search/index.py` | 9.61% | -0.89% |
| `algorithm/search/linear.py` | 11.45% | -0.54% |
| `algorithm/twosum/twosum.py` | 15.29% | 2.76% |
| `algorithm/twosum/twosum_naive.py` | 14.22% | 4.12% |
| `complex/classes/classes.py` | 12.27% | -0.03% |
| `complex/classes/dataclasses_.py` | 12.81% | -2.45% |
| `complex/classes/namedtuple_classes.py` | 15.38% | 0.03% |
| `complex/classes/simplenamespace.py` | 14.81% | 3.25% |
| `complex/classes/sloted_classes.py` | 11.18% | 1.36% |
| `complex/generators/simple.py` | 14.38% | 0.34% |
| `dummy/dummy.py` | 13.1% | 3.06% |
| `long_run/database/postgresql.py` | 7.04% | -1.24% |
| `long_run/database/sqlite_.py` | -- | -- |
| `long_run/file/load_titanic_csv_pandas.py` | -- | -- |
| `long_run/file/load_titanic_csv_python.py` | 18.23% | 4.01% |
| `long_run/processes/collect_names_from_site.py` | -- | -- |
| `long_run/processes/generate_fake_data.py` | -- | -- |
| `long_run/processes/maze_generator.py` | 15.21% | 2.96% |
| `long_run/text/clean_text.py` | 15.03% | 2.9% |
| `long_run/text/count_words.py` | 14.89% | 0.94% |
| `math/haversine.py` | 18.83% | 2.35% |
| `math/mandelbrot.py` | -- | -- |
| `math/pow_simple.py` | 19.58% | 2.44% |
| `math/pow_using_math.py` | 12.38% | 2.77% |
| `modules/json/json_module.py` | 17.06% | 4.74% |
| `modules/json/orjson_module.py` | -- | -- |
---

#### **Execution**

##### **Mean [s]**
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 1.2999 | 1.10848 | 1.46736 |
| `algorithm/search/hashmap_lookup.py` | 1.29852 | 1.11532 | 1.4803 |
| `algorithm/search/index.py` | 1.31801 | 1.13663 | 1.48073 |
| `algorithm/search/linear.py` | 1.37743 | 1.18072 | 1.54222 |
| `algorithm/twosum/twosum.py` | 0.12099 | 0.11662 | 0.13616 |
| `algorithm/twosum/twosum_naive.py` | 0.12003 | 0.1171 | 0.13846 |
| `complex/classes/classes.py` | 0.06507 | 0.02967 | 0.0328 |
| `complex/classes/dataclasses_.py` | 0.18426 | 0.17727 | 0.20631 |
| `complex/classes/namedtuple_classes.py` | 0.13476 | 0.12525 | 0.14866 |
| `complex/classes/simplenamespace.py` | 0.06342 | 0.03629 | 0.04269 |
| `complex/classes/sloted_classes.py` | 0.05968 | 0.02871 | 0.03286 |
| `complex/generators/simple.py` | 0.0859 | 0.05187 | 0.063 |
| `dummy/dummy.py` | 0.04704 | 0.01999 | 0.02191 |
| `long_run/database/postgresql.py` | 0.23542 | 0.2316 | 0.28151 |
| `long_run/database/sqlite_.py` | 0.80464 | 0.83387 | -- |
| `long_run/file/load_titanic_csv_pandas.py` | 0.86849 | 0.90332 | -- |
| `long_run/file/load_titanic_csv_python.py` | 0.1032 | 0.09469 | 0.10442 |
| `long_run/processes/collect_names_from_site.py` | 1.64788 | 1.58295 | -- |
| `long_run/processes/generate_fake_data.py` | 1.15325 | 1.12875 | -- |
| `long_run/processes/maze_generator.py` | 0.21774 | 0.14676 | 0.1674 |
| `long_run/text/clean_text.py` | 0.28541 | 0.24907 | 0.26265 |
| `long_run/text/count_words.py` | 0.13089 | 0.11135 | 0.12523 |
| `math/haversine.py` | 0.76051 | 0.64051 | 0.82138 |
| `math/mandelbrot.py` | 3.86269 | 3.86186 | -- |
| `math/pow_simple.py` | 0.52031 | 0.37856 | 0.41839 |
| `math/pow_using_math.py` | 1.32867 | 1.14534 | 1.28179 |
| `modules/json/json_module.py` | 0.4961 | 0.46161 | 0.51519 |
| `modules/json/orjson_module.py` | 0.35738 | 0.28517 | -- |

##### **Median [s]**
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 1.29984 | 1.10892 | 1.47143 |
| `algorithm/search/hashmap_lookup.py` | 1.29573 | 1.11352 | 1.45765 |
| `algorithm/search/index.py` | 1.31779 | 1.13414 | 1.47769 |
| `algorithm/search/linear.py` | 1.37636 | 1.18023 | 1.53228 |
| `algorithm/twosum/twosum.py` | 0.12132 | 0.11657 | 0.13644 |
| `algorithm/twosum/twosum_naive.py` | 0.12022 | 0.11777 | 0.13833 |
| `complex/classes/classes.py` | 0.05953 | 0.02967 | 0.03234 |
| `complex/classes/dataclasses_.py` | 0.18365 | 0.17675 | 0.20631 |
| `complex/classes/namedtuple_classes.py` | 0.13494 | 0.12531 | 0.14815 |
| `complex/classes/simplenamespace.py` | 0.06342 | 0.03633 | 0.04253 |
| `complex/classes/sloted_classes.py` | 0.05969 | 0.02859 | 0.03314 |
| `complex/generators/simple.py` | 0.0856 | 0.05147 | 0.06161 |
| `dummy/dummy.py` | 0.04728 | 0.01981 | 0.02143 |
| `long_run/database/postgresql.py` | 0.23632 | 0.23031 | 0.28189 |
| `long_run/database/sqlite_.py` | 0.80311 | 0.83194 | -- |
| `long_run/file/load_titanic_csv_pandas.py` | 0.86657 | 0.90562 | -- |
| `long_run/file/load_titanic_csv_python.py` | 0.10321 | 0.09414 | 0.10402 |
| `long_run/processes/collect_names_from_site.py` | 1.65439 | 1.53328 | -- |
| `long_run/processes/generate_fake_data.py` | 1.15232 | 1.12299 | -- |
| `long_run/processes/maze_generator.py` | 0.21302 | 0.14459 | 0.16671 |
| `long_run/text/clean_text.py` | 0.2854 | 0.24899 | 0.26255 |
| `long_run/text/count_words.py` | 0.13038 | 0.11141 | 0.12447 |
| `math/haversine.py` | 0.75774 | 0.64067 | 0.82546 |
| `math/mandelbrot.py` | 3.83777 | 3.85169 | -- |
| `math/pow_simple.py` | 0.51872 | 0.37643 | 0.41838 |
| `math/pow_using_math.py` | 1.32709 | 1.14566 | 1.28024 |
| `modules/json/json_module.py` | 0.49349 | 0.45766 | 0.51459 |
| `modules/json/orjson_module.py` | 0.35882 | 0.28559 | -- |

#### **Memory Usage**

##### **MEM [MB]**
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 32.59805 | 35.33008 | 34.97305 |
| `algorithm/search/hashmap_lookup.py` | 31.38398 | 36.17305 | 35.74336 |
| `algorithm/search/index.py` | 31.90273 | 35.28164 | 34.96836 |
| `algorithm/search/linear.py` | 31.28398 | 35.05547 | 34.86719 |
| `algorithm/twosum/twosum.py` | 23.60664 | 26.48672 | 27.2168 |
| `algorithm/twosum/twosum_naive.py` | 24.11133 | 26.45156 | 27.54062 |
| `complex/classes/classes.py` | 24.71719 | 27.7582 | 27.75 |
| `complex/classes/dataclasses_.py` | 24.66797 | 28.5293 | 27.82891 |
| `complex/classes/namedtuple_classes.py` | 23.82656 | 27.48398 | 27.49141 |
| `complex/classes/simplenamespace.py` | 25.44141 | 28.29141 | 29.21055 |
| `complex/classes/sloted_classes.py` | 25.22148 | 27.66445 | 28.0418 |
| `complex/generators/simple.py` | 25.22813 | 28.75742 | 28.85586 |
| `dummy/dummy.py` | 24.16914 | 26.52305 | 27.33477 |
| `long_run/database/postgresql.py` | 29.32031 | 31.77891 | 31.38555 |
| `long_run/database/sqlite_.py` | 66.01055 | 71.79961 | -- |
| `long_run/file/load_titanic_csv_pandas.py` | 65.07227 | 70.16211 | -- |
| `long_run/file/load_titanic_csv_python.py` | 23.54687 | 26.76602 | 27.83906 |
| `long_run/processes/collect_names_from_site.py` | 45.06953 | 47.28477 | -- |
| `long_run/processes/generate_fake_data.py` | 68.19844 | 71.56992 | -- |
| `long_run/processes/maze_generator.py` | 24.15977 | 27.03438 | 27.83516 |
| `long_run/text/clean_text.py` | 23.65078 | 26.43867 | 27.20547 |
| `long_run/text/count_words.py` | 23.65391 | 26.92344 | 27.17695 |
| `math/haversine.py` | 23.24883 | 26.99375 | 27.62773 |
| `math/mandelbrot.py` | 39.29336 | 40.43672 | -- |
| `math/pow_simple.py` | 23.0918 | 26.95547 | 27.61406 |
| `math/pow_using_math.py` | 24.17734 | 26.4375 | 27.16953 |
| `modules/json/json_module.py` | 23.81289 | 26.61445 | 27.87617 |
| `modules/json/orjson_module.py` | 24.24766 | 27.54844 | -- |

---


### **Python 3.6**

```bash
Python 3.6.15

Linux 1fb3683a55f0 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          2
Thread(s) per core:              1
Core(s) per socket:              2
NUMA node(s):                    1
Model name:                      Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
NUMA node0 CPU(s):               0,1

MemTotal:        4014620 kB
MemFree:          419952 kB
MemAvailable:    2826516 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|


### **Python 3.7**

```bash
Python 3.7.17

Linux c8790bc35f10 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          2
Model name:                      Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
Thread(s) per core:              1
Core(s) per socket:              2
NUMA node(s):                    1
NUMA node0 CPU(s):               0,1

MemTotal:        4014620 kB
MemFree:          441540 kB
MemAvailable:    2814168 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|


### **Python 3.8**

```bash
Python 3.8.17

Linux 84ecc104923a 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          2
Model name:                      Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
Thread(s) per core:              1
Core(s) per socket:              2
NUMA node(s):                    1
NUMA node0 CPU(s):               0,1

MemTotal:        4014620 kB
MemFree:          435168 kB
MemAvailable:    2811364 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|


### **Python 3.9**

```bash
Python 3.9.17

Linux ae1d4b39d6bd 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          2
Model name:                      Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
Thread(s) per core:              1
Core(s) per socket:              2
NUMA node(s):                    1
NUMA node0 CPU(s):               0,1

MemTotal:        4014620 kB
MemFree:          374716 kB
MemAvailable:    2802560 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|


### **Python 3.10**

```bash
Python 3.10.12

Linux 0212e2a176fd 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          2
Model name:                      Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
Thread(s) per core:              1
Core(s) per socket:              2
NUMA node(s):                    1
NUMA node0 CPU(s):               0,1

MemTotal:        4014620 kB
MemFree:          914480 kB
MemAvailable:    3300928 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.2999 | 0.01334 | 1.29984 | 1.28447 | 1.3238 | 32.59805 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.29852 | 0.01444 | 1.29573 | 1.2764 | 1.31905 | 31.38398 |
| `algorithm/search/index.py` | yes | 1.31801 | 0.01041 | 1.31779 | 1.29992 | 1.33573 | 31.90273 |
| `algorithm/search/linear.py` | yes | 1.37743 | 0.01009 | 1.37636 | 1.36397 | 1.39896 | 31.28398 |
| `algorithm/twosum/twosum.py` | yes | 0.12099 | 0.00224 | 0.12132 | 0.11792 | 0.12566 | 23.60664 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.12003 | 0.0011 | 0.12022 | 0.11829 | 0.12201 | 24.11133 |
| `complex/classes/classes.py` | yes | 0.06507 | 0.01351 | 0.05953 | 0.05876 | 0.10221 | 24.71719 |
| `complex/classes/dataclasses_.py` | yes | 0.18426 | 0.00193 | 0.18365 | 0.18203 | 0.18663 | 24.66797 |
| `complex/classes/namedtuple_classes.py` | yes | 0.13476 | 0.00167 | 0.13494 | 0.13248 | 0.13815 | 23.82656 |
| `complex/classes/simplenamespace.py` | yes | 0.06342 | 0.00056 | 0.06342 | 0.06256 | 0.06454 | 25.44141 |
| `complex/classes/sloted_classes.py` | yes | 0.05968 | 0.00039 | 0.05969 | 0.05898 | 0.06025 | 25.22148 |
| `complex/generators/simple.py` | yes | 0.0859 | 0.00116 | 0.0856 | 0.08476 | 0.08875 | 25.22813 |
| `dummy/dummy.py` | yes | 0.04704 | 0.00083 | 0.04728 | 0.04591 | 0.04853 | 24.16914 |
| `long_run/database/postgresql.py` | yes | 0.23542 | 0.00434 | 0.23632 | 0.22829 | 0.24011 | 29.32031 |
| `long_run/database/sqlite_.py` | yes | 0.80464 | 0.00812 | 0.80311 | 0.79378 | 0.82035 | 66.01055 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.86849 | 0.01262 | 0.86657 | 0.85068 | 0.88691 | 65.07227 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.1032 | 0.00064 | 0.10321 | 0.10226 | 0.1041 | 23.54687 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.64788 | 0.01694 | 1.65439 | 1.61848 | 1.67038 | 45.06953 |
| `long_run/processes/generate_fake_data.py` | yes | 1.15325 | 0.01467 | 1.15232 | 1.13735 | 1.18469 | 68.19844 |
| `long_run/processes/maze_generator.py` | yes | 0.21774 | 0.01877 | 0.21302 | 0.19217 | 0.25447 | 24.15977 |
| `long_run/text/clean_text.py` | yes | 0.28541 | 0.00216 | 0.2854 | 0.28176 | 0.28802 | 23.65078 |
| `long_run/text/count_words.py` | yes | 0.13089 | 0.00144 | 0.13038 | 0.12898 | 0.13318 | 23.65391 |
| `math/haversine.py` | yes | 0.76051 | 0.01122 | 0.75774 | 0.74891 | 0.78062 | 23.24883 |
| `math/mandelbrot.py` | yes | 3.86269 | 0.05177 | 3.83777 | 3.82441 | 3.97829 | 39.29336 |
| `math/pow_simple.py` | yes | 0.52031 | 0.00346 | 0.51872 | 0.51704 | 0.52485 | 23.0918 |
| `math/pow_using_math.py` | yes | 1.32867 | 0.01507 | 1.32709 | 1.31351 | 1.35934 | 24.17734 |
| `modules/json/json_module.py` | yes | 0.4961 | 0.01021 | 0.49349 | 0.48471 | 0.52121 | 23.81289 |
| `modules/json/orjson_module.py` | yes | 0.35738 | 0.00726 | 0.35882 | 0.3457 | 0.36733 | 24.24766 |


### **Python 3.11**

```bash
Python 3.11.4

Linux b3690b293c4a 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          2
Model name:                      Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
Thread(s) per core:              1
Core(s) per socket:              2
NUMA node(s):                    1
NUMA node0 CPU(s):               0,1

MemTotal:        4014620 kB
MemFree:          991724 kB
MemAvailable:    3289524 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.10848 | 0.00955 | 1.10892 | 1.09361 | 1.12473 | 35.33008 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.11532 | 0.00804 | 1.11352 | 1.10644 | 1.12932 | 36.17305 |
| `algorithm/search/index.py` | yes | 1.13663 | 0.0077 | 1.13414 | 1.12703 | 1.14766 | 35.28164 |
| `algorithm/search/linear.py` | yes | 1.18072 | 0.00987 | 1.18023 | 1.16445 | 1.19684 | 35.05547 |
| `algorithm/twosum/twosum.py` | yes | 0.11662 | 0.00118 | 0.11657 | 0.11466 | 0.11896 | 26.48672 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.1171 | 0.00383 | 0.11777 | 0.11172 | 0.12156 | 26.45156 |
| `complex/classes/classes.py` | yes | 0.02967 | 0.00063 | 0.02967 | 0.02845 | 0.03076 | 27.7582 |
| `complex/classes/dataclasses_.py` | yes | 0.17727 | 0.00387 | 0.17675 | 0.17216 | 0.18316 | 28.5293 |
| `complex/classes/namedtuple_classes.py` | yes | 0.12525 | 0.0012 | 0.12531 | 0.12312 | 0.12707 | 27.48398 |
| `complex/classes/simplenamespace.py` | yes | 0.03629 | 0.00034 | 0.03633 | 0.03573 | 0.03689 | 28.29141 |
| `complex/classes/sloted_classes.py` | yes | 0.02871 | 0.00071 | 0.02859 | 0.02805 | 0.03051 | 27.66445 |
| `complex/generators/simple.py` | yes | 0.05187 | 0.00068 | 0.05147 | 0.0513 | 0.05307 | 28.75742 |
| `dummy/dummy.py` | yes | 0.01999 | 0.00052 | 0.01981 | 0.01936 | 0.02093 | 26.52305 |
| `long_run/database/postgresql.py` | yes | 0.2316 | 0.0028 | 0.23031 | 0.22838 | 0.23756 | 31.77891 |
| `long_run/database/sqlite_.py` | yes | 0.83387 | 0.00883 | 0.83194 | 0.8252 | 0.85172 | 71.79961 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.90332 | 0.00929 | 0.90562 | 0.88792 | 0.91613 | 70.16211 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.09469 | 0.00217 | 0.09414 | 0.09279 | 0.10044 | 26.76602 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.58295 | 0.12293 | 1.53328 | 1.5194 | 1.91664 | 47.28477 |
| `long_run/processes/generate_fake_data.py` | yes | 1.12875 | 0.01612 | 1.12299 | 1.10959 | 1.1646 | 71.56992 |
| `long_run/processes/maze_generator.py` | yes | 0.14676 | 0.00661 | 0.14459 | 0.13967 | 0.15826 | 27.03438 |
| `long_run/text/clean_text.py` | yes | 0.24907 | 0.00172 | 0.24899 | 0.24647 | 0.25175 | 26.43867 |
| `long_run/text/count_words.py` | yes | 0.11135 | 0.00096 | 0.11141 | 0.11019 | 0.11279 | 26.92344 |
| `math/haversine.py` | yes | 0.64051 | 0.00278 | 0.64067 | 0.63633 | 0.64531 | 26.99375 |
| `math/mandelbrot.py` | yes | 3.86186 | 0.04395 | 3.85169 | 3.82482 | 3.97532 | 40.43672 |
| `math/pow_simple.py` | yes | 0.37856 | 0.00457 | 0.37643 | 0.37482 | 0.38694 | 26.95547 |
| `math/pow_using_math.py` | yes | 1.14534 | 0.01331 | 1.14566 | 1.12926 | 1.17339 | 26.4375 |
| `modules/json/json_module.py` | yes | 0.46161 | 0.01084 | 0.45766 | 0.44648 | 0.47841 | 26.61445 |
| `modules/json/orjson_module.py` | yes | 0.28517 | 0.00207 | 0.28559 | 0.28202 | 0.28784 | 27.54844 |


### **Python 3.12**

```bash
Python 3.12.0b4

Linux 41a3783ad3e6 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          2
Model name:                      Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
Thread(s) per core:              1
Core(s) per socket:              2
NUMA node(s):                    1
NUMA node0 CPU(s):               0,1

MemTotal:        4014620 kB
MemFree:          978212 kB
MemAvailable:    3278652 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.46736 | 0.01232 | 1.47143 | 1.44262 | 1.48359 | 34.97305 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.4803 | 0.0754 | 1.45765 | 1.42686 | 1.68305 | 35.74336 |
| `algorithm/search/index.py` | yes | 1.48073 | 0.0178 | 1.47769 | 1.4561 | 1.51402 | 34.96836 |
| `algorithm/search/linear.py` | yes | 1.54222 | 0.02233 | 1.53228 | 1.51129 | 1.57907 | 34.86719 |
| `algorithm/twosum/twosum.py` | yes | 0.13616 | 0.00227 | 0.13644 | 0.13314 | 0.1414 | 27.2168 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.13846 | 0.00188 | 0.13833 | 0.13544 | 0.14271 | 27.54062 |
| `complex/classes/classes.py` | yes | 0.0328 | 0.00131 | 0.03234 | 0.0317 | 0.03522 | 27.75 |
| `complex/classes/dataclasses_.py` | yes | 0.20631 | 0.00092 | 0.20631 | 0.20489 | 0.2077 | 27.82891 |
| `complex/classes/namedtuple_classes.py` | yes | 0.14866 | 0.00124 | 0.14815 | 0.14759 | 0.15101 | 27.49141 |
| `complex/classes/simplenamespace.py` | yes | 0.04269 | 0.00094 | 0.04253 | 0.04123 | 0.04441 | 29.21055 |
| `complex/classes/sloted_classes.py` | yes | 0.03286 | 0.00064 | 0.03314 | 0.03186 | 0.03354 | 28.0418 |
| `complex/generators/simple.py` | yes | 0.063 | 0.00288 | 0.06161 | 0.06014 | 0.06774 | 28.85586 |
| `dummy/dummy.py` | yes | 0.02191 | 0.00109 | 0.02143 | 0.02109 | 0.02448 | 27.33477 |
| `long_run/database/postgresql.py` | yes | 0.28151 | 0.0019 | 0.28189 | 0.27675 | 0.28308 | 31.38555 |
| `long_run/database/sqlite_.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/file/load_titanic_csv_pandas.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.10442 | 0.00163 | 0.10402 | 0.10226 | 0.1081 | 27.83906 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/maze_generator.py` | yes | 0.1674 | 0.01013 | 0.16671 | 0.14867 | 0.18351 | 27.83516 |
| `long_run/text/clean_text.py` | yes | 0.26265 | 0.00328 | 0.26255 | 0.25759 | 0.26903 | 27.20547 |
| `long_run/text/count_words.py` | yes | 0.12523 | 0.002 | 0.12447 | 0.12312 | 0.12971 | 27.17695 |
| `math/haversine.py` | yes | 0.82138 | 0.03337 | 0.82546 | 0.76933 | 0.88312 | 27.62773 |
| `math/mandelbrot.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `math/pow_simple.py` | yes | 0.41839 | 0.00339 | 0.41838 | 0.41388 | 0.42474 | 27.61406 |
| `math/pow_using_math.py` | yes | 1.28179 | 0.01016 | 1.28024 | 1.26891 | 1.30136 | 27.16953 |
| `modules/json/json_module.py` | yes | 0.51519 | 0.01891 | 0.51459 | 0.48768 | 0.53983 | 27.87617 |
| `modules/json/orjson_module.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |

