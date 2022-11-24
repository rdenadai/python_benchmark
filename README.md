# Python Benchmark

This is a simple repo to validate and test any (almost any) python program againts all python 3 versions.
 - Python 3.6.15
 - Python 3.7.15
 - Python 3.8.15
 - Python 3.9.15
 - Python 3.10.8
 - Python 3.11.0

## Dependencies

To run the full tests, please keep in mind the you need **docker** (and docker-compose) installed in the environment.

All the tests run inside a docker container image based on each python version described above.

Since python libs have different behaviors and support versions, inside the **docker/** folder there's a requirements99.txt versioning number.

## How to run

To run the full suite, just type in:

```bash
$> ./benchmarh.sh
```

Results will be write down on the main README.md file (it's partiallys regenerated at each run).

To benchmark a new program, simple put it inside de **src** folder.

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
> Last run: Thu Nov 24 12:23:41 AM -03 2022
### **Comparison**

#### **Execution**

| Command |  Mean 3.6 [s] | Mean 3.7 [s] | Mean 3.8 [s] | Mean 3.9 [s] | Mean 3.10 [s] | Mean 3.11 [s] |
|:---|---:|---:|---:|---:|---:|---:|
| algorithm/twosum/twosum.py | 0.07826 | 0.06476 | 0.07154 | 0.07881 | 0.07463 | 0.06953 |
| algorithm/twosum/twosum_naive.py | 0.07916 | 0.06513 | 0.07123 | 0.07947 | 0.07504 | 0.07005 |
| complex/classes/classes.py | 0.04434 | 0.03681 | 0.03889 | 0.04409 | 0.03927 | 0.02232 |
| complex/classes/dataclasses_.py | -1 | 0.09645 | 0.10337 | 0.12539 | 0.11522 | 0.10843 |
| complex/classes/namedtuple_classes.py | 0.09102 | 0.07353 | 0.08107 | 0.09004 | 0.08415 | 0.07917 |
| complex/classes/simplenamespace.py | 0.05959 | 0.03823 | 0.0403 | 0.04568 | 0.04058 | 0.0246 |
| complex/classes/sloted_classes.py | 0.04414 | 0.03696 | 0.03899 | 0.04326 | 0.03861 | 0.02138 |
| dummy/dummy.py | 0.03391 | 0.02483 | 0.02877 | 0.03108 | 0.02988 | 0.01323 |
| long_run/database/postgresql.py | -1 | -1 | -1 | -1 | -1 | -1 |
| long_run/file/load_titanic_csv_pandas.py | 0.66586 | 0.56564 | 0.59818 | 0.64618 | 0.6006 | 0.60004 |
| long_run/file/load_titanic_csv_python.py | 0.06938 | 0.06129 | 0.06565 | 0.07334 | 0.06517 | 0.05598 |
| long_run/processes/collect_names_from_site.py | -1 | -1 | 1.73235 | 1.78345 | 1.71222 | 1.44167 |
| long_run/processes/generate_fake_data.py | 0.81286 | 0.73122 | 0.75149 | 0.79816 | 0.76088 | 0.75547 |
| math/pow_simple.py | 0.45013 | 0.43542 | 0.42768 | 0.41809 | 0.41108 | 0.31799 |
| math/pow_using_math.py | 1.62891 | 1.44104 | 1.36814 | 1.38121 | 1.37048 | 1.17107 |
| modules/json/json_module.py | 0.41668 | 0.37991 | 0.35462 | 0.37887 | 0.33378 | 0.28385 |
| modules/json/orjson_module.py | 0.2678 | 0.20552 | 0.21364 | 0.24023 | 0.21609 | 0.17357 |

| Command |  Median 3.6 [s] | Median 3.7 [s] | Median 3.8 [s] | Median 3.9 [s] | Median 3.10 [s] | Median 3.11 [s] |
|:---|---:|---:|---:|---:|---:|---:|
| algorithm/twosum/twosum.py | 0.07818 | 0.06481 | 0.07149 | 0.07826 | 0.07468 | 0.06928 |
| algorithm/twosum/twosum_naive.py | 0.07919 | 0.06495 | 0.07122 | 0.07913 | 0.07485 | 0.06981 |
| complex/classes/classes.py | 0.04408 | 0.03679 | 0.0385 | 0.04233 | 0.03928 | 0.02179 |
| complex/classes/dataclasses_.py | -1 | 0.09641 | 0.10352 | 0.12528 | 0.11535 | 0.10829 |
| complex/classes/namedtuple_classes.py | 0.09103 | 0.07348 | 0.08108 | 0.08971 | 0.08402 | 0.07898 |
| complex/classes/simplenamespace.py | 0.05956 | 0.03819 | 0.03964 | 0.04428 | 0.04045 | 0.02434 |
| complex/classes/sloted_classes.py | 0.04401 | 0.03694 | 0.03894 | 0.04259 | 0.03854 | 0.02182 |
| dummy/dummy.py | 0.03373 | 0.0247 | 0.02813 | 0.03003 | 0.02981 | 0.0127 |
| long_run/database/postgresql.py | -1 | -1 | -1 | -1 | -1 | -1 |
| long_run/file/load_titanic_csv_pandas.py | 0.66562 | 0.55835 | 0.59691 | 0.64476 | 0.59955 | 0.60021 |
| long_run/file/load_titanic_csv_python.py | 0.06858 | 0.06133 | 0.06509 | 0.07281 | 0.06463 | 0.05571 |
| long_run/processes/collect_names_from_site.py | -1 | -1 | 1.73142 | 1.78831 | 1.71145 | 1.44608 |
| long_run/processes/generate_fake_data.py | 0.81225 | 0.72732 | 0.75166 | 0.79948 | 0.76066 | 0.75754 |
| math/pow_simple.py | 0.4522 | 0.43098 | 0.42535 | 0.41346 | 0.4072 | 0.31563 |
| math/pow_using_math.py | 1.62099 | 1.43325 | 1.35888 | 1.36694 | 1.34948 | 1.15966 |
| modules/json/json_module.py | 0.41601 | 0.38091 | 0.35353 | 0.37798 | 0.33268 | 0.27986 |
| modules/json/orjson_module.py | 0.26399 | 0.20454 | 0.21293 | 0.23909 | 0.21539 | 0.17321 |

#### **Memory Usage**

| Command |  MEM 3.6 [MB] | MEM 3.7 [MB] | MEM 3.8 [MB] | MEM 3.9 [MB] | MEM 3.10 [MB] | MEM 3.11 [MB] |
|:---|---:|---:|---:|---:|---:|---:|
| algorithm/twosum/twosum.py | 22.32227 | 19.83711 | 20.37734 | 22.09023 | 23.07422 | 25.91523 |
| algorithm/twosum/twosum_naive.py | 22.22227 | 20.00391 | 20.49375 | 21.54375 | 22.03594 | 25.85195 |
| complex/classes/classes.py | 21.97227 | 20.1793 | 20.35117 | 22.36562 | 24.35156 | 27.36875 |
| complex/classes/dataclasses_.py | -1 | 19.91719 | 20.74531 | 21.70586 | 23.31289 | 27.0418 |
| complex/classes/namedtuple_classes.py | 22.28437 | 20.01328 | 20.47188 | 22.67383 | 22.53672 | 26.67109 |
| complex/classes/simplenamespace.py | 21.98633 | 20.03164 | 20.85625 | 22.69687 | 23.26289 | 27.79961 |
| complex/classes/sloted_classes.py | 22.02969 | 19.89297 | 20.65977 | 21.61172 | 23.45469 | 27.31914 |
| dummy/dummy.py | 21.81836 | 19.81758 | 20.36719 | 22.07734 | 22.36563 | 25.88047 |
| long_run/database/postgresql.py | -1 | -1 | -1 | -1 | -1 | -1 |
| long_run/file/load_titanic_csv_pandas.py | 61.85391 | 63.15781 | 63.51562 | 63.89688 | 63.60039 | 68.98984 |
| long_run/file/load_titanic_csv_python.py | 22.10586 | 19.97031 | 20.70742 | 22.49336 | 23.06289 | 26.00703 |
| long_run/processes/collect_names_from_site.py | -1 | -1 | 44.4457 | 44.625 | 44.8375 | 47.07031 |
| long_run/processes/generate_fake_data.py | 64.74844 | 67.64258 | 64.88359 | 67.86992 | 67.16523 | 71.46484 |
| math/pow_simple.py | 21.79609 | 19.88438 | 20.46836 | 22.62852 | 22.80078 | 25.68008 |
| math/pow_using_math.py | 21.75039 | 19.97461 | 20.50234 | 22.37578 | 22.56953 | 25.53281 |
| modules/json/json_module.py | 21.82187 | 21.08516 | 21.12773 | 22.32148 | 23.14883 | 26.29531 |
| modules/json/orjson_module.py | 22.56406 | 21.46719 | 21.39453 | 22.82187 | 23.85469 | 26.76211 |

### **Python 3.6**

```bash
Python 3.6.15

Linux 2d6a1331447c 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078816 kB
MemFree:         7357832 kB
MemAvailable:   14451608 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.03391 | 0.00107 | 0.03373 | 0.03279 | 0.03659 | 21.81836 |
| `long_run/processes/generate_fake_data.py` | yes | 0.81286 | 0.01208 | 0.81225 | 0.79377 | 0.82946 | 64.74844 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/database/postgresql.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `math/pow_using_math.py` | yes | 1.62891 | 0.10564 | 1.62099 | 1.51844 | 1.85298 | 21.75039 |
| `math/pow_simple.py` | yes | 0.45013 | 0.00732 | 0.4522 | 0.44049 | 0.46061 | 21.79609 |
| `modules/json/json_module.py` | yes | 0.41668 | 0.00331 | 0.41601 | 0.41056 | 0.42142 | 21.82187 |
| `modules/json/orjson_module.py` | yes | 0.2678 | 0.00824 | 0.26399 | 0.25862 | 0.28607 | 22.56406 |
| `complex/classes/namedtuple_classes.py` | yes | 0.09102 | 0.00038 | 0.09103 | 0.0905 | 0.09183 | 22.28437 |
| `complex/classes/classes.py` | yes | 0.04434 | 0.00084 | 0.04408 | 0.04374 | 0.0466 | 21.97227 |
| `complex/classes/dataclasses_.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `complex/classes/sloted_classes.py` | yes | 0.04414 | 0.00041 | 0.04401 | 0.04363 | 0.04495 | 22.02969 |
| `complex/classes/simplenamespace.py` | yes | 0.05959 | 0.00052 | 0.05956 | 0.05884 | 0.06048 | 21.98633 |
| `algorithm/twosum/twosum.py` | yes | 0.07826 | 0.00051 | 0.07818 | 0.0775 | 0.07891 | 22.32227 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07916 | 0.00064 | 0.07919 | 0.0783 | 0.08056 | 22.22227 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06938 | 0.00314 | 0.06858 | 0.0677 | 0.07822 | 22.10586 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.66586 | 0.00573 | 0.66562 | 0.6575 | 0.67601 | 61.85391 |


### **Python 3.7**

```bash
Python 3.7.15

Linux 3dc785938d25 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078816 kB
MemFree:         7351288 kB
MemAvailable:   14455012 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.02483 | 0.00041 | 0.0247 | 0.02437 | 0.02546 | 19.81758 |
| `long_run/processes/generate_fake_data.py` | yes | 0.73122 | 0.0139 | 0.72732 | 0.71637 | 0.753 | 67.64258 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/database/postgresql.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `math/pow_using_math.py` | yes | 1.44104 | 0.02942 | 1.43325 | 1.40296 | 1.49422 | 19.97461 |
| `math/pow_simple.py` | yes | 0.43542 | 0.01575 | 0.43098 | 0.41776 | 0.45816 | 19.88438 |
| `modules/json/json_module.py` | yes | 0.37991 | 0.00444 | 0.38091 | 0.37261 | 0.38465 | 21.08516 |
| `modules/json/orjson_module.py` | yes | 0.20552 | 0.00273 | 0.20454 | 0.20199 | 0.21005 | 21.46719 |
| `complex/classes/namedtuple_classes.py` | yes | 0.07353 | 0.00082 | 0.07348 | 0.07236 | 0.07537 | 20.01328 |
| `complex/classes/classes.py` | yes | 0.03681 | 0.00019 | 0.03679 | 0.0366 | 0.03712 | 20.1793 |
| `complex/classes/dataclasses_.py` | yes | 0.09645 | 0.00136 | 0.09641 | 0.09489 | 0.09879 | 19.91719 |
| `complex/classes/sloted_classes.py` | yes | 0.03696 | 0.00037 | 0.03694 | 0.03645 | 0.03766 | 19.89297 |
| `complex/classes/simplenamespace.py` | yes | 0.03823 | 0.00048 | 0.03819 | 0.03748 | 0.03893 | 20.03164 |
| `algorithm/twosum/twosum.py` | yes | 0.06476 | 0.0005 | 0.06481 | 0.06397 | 0.06549 | 19.83711 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.06513 | 0.0012 | 0.06495 | 0.06368 | 0.06817 | 20.00391 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06129 | 0.00072 | 0.06133 | 0.06015 | 0.06228 | 19.97031 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.56564 | 0.02169 | 0.55835 | 0.54331 | 0.60131 | 63.15781 |


### **Python 3.8**

```bash
Python 3.8.15

Linux c37080b23897 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078816 kB
MemFree:         7355004 kB
MemAvailable:   14469940 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.02877 | 0.00188 | 0.02813 | 0.02773 | 0.03396 | 20.36719 |
| `long_run/processes/generate_fake_data.py` | yes | 0.75149 | 0.00644 | 0.75166 | 0.74208 | 0.76074 | 64.88359 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.73235 | 0.02878 | 1.73142 | 1.69985 | 1.7827 | 44.4457 |
| `long_run/database/postgresql.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `math/pow_using_math.py` | yes | 1.36814 | 0.05036 | 1.35888 | 1.31722 | 1.47103 | 20.50234 |
| `math/pow_simple.py` | yes | 0.42768 | 0.00955 | 0.42535 | 0.4186 | 0.44946 | 20.46836 |
| `modules/json/json_module.py` | yes | 0.35462 | 0.00459 | 0.35353 | 0.34672 | 0.36039 | 21.12773 |
| `modules/json/orjson_module.py` | yes | 0.21364 | 0.00284 | 0.21293 | 0.21092 | 0.21887 | 21.39453 |
| `complex/classes/namedtuple_classes.py` | yes | 0.08107 | 0.00041 | 0.08108 | 0.08058 | 0.08199 | 20.47188 |
| `complex/classes/classes.py` | yes | 0.03889 | 0.00123 | 0.0385 | 0.03805 | 0.04232 | 20.35117 |
| `complex/classes/dataclasses_.py` | yes | 0.10337 | 0.00094 | 0.10352 | 0.10206 | 0.10488 | 20.74531 |
| `complex/classes/sloted_classes.py` | yes | 0.03899 | 0.00051 | 0.03894 | 0.03823 | 0.03976 | 20.65977 |
| `complex/classes/simplenamespace.py` | yes | 0.0403 | 0.00155 | 0.03964 | 0.03909 | 0.04327 | 20.85625 |
| `algorithm/twosum/twosum.py` | yes | 0.07154 | 0.00086 | 0.07149 | 0.07028 | 0.07335 | 20.37734 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07123 | 0.00044 | 0.07122 | 0.07025 | 0.07177 | 20.49375 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06565 | 0.00265 | 0.06509 | 0.06376 | 0.07305 | 20.70742 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.59818 | 0.0066 | 0.59691 | 0.59072 | 0.61188 | 63.51562 |


### **Python 3.9**

```bash
Python 3.9.15

Linux ead93a992d43 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078816 kB
MemFree:         7337784 kB
MemAvailable:   14462904 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.03108 | 0.00256 | 0.03003 | 0.02918 | 0.0362 | 22.07734 |
| `long_run/processes/generate_fake_data.py` | yes | 0.79816 | 0.00751 | 0.79948 | 0.78659 | 0.80825 | 67.86992 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.78345 | 0.02196 | 1.78831 | 1.7515 | 1.81164 | 44.625 |
| `long_run/database/postgresql.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `math/pow_using_math.py` | yes | 1.38121 | 0.03238 | 1.36694 | 1.35156 | 1.44852 | 22.37578 |
| `math/pow_simple.py` | yes | 0.41809 | 0.00767 | 0.41346 | 0.41185 | 0.43124 | 22.62852 |
| `modules/json/json_module.py` | yes | 0.37887 | 0.01172 | 0.37798 | 0.36385 | 0.39969 | 22.32148 |
| `modules/json/orjson_module.py` | yes | 0.24023 | 0.00407 | 0.23909 | 0.23522 | 0.24727 | 22.82187 |
| `complex/classes/namedtuple_classes.py` | yes | 0.09004 | 0.00089 | 0.08971 | 0.08913 | 0.09196 | 22.67383 |
| `complex/classes/classes.py` | yes | 0.04409 | 0.00523 | 0.04233 | 0.04135 | 0.05874 | 22.36562 |
| `complex/classes/dataclasses_.py` | yes | 0.12539 | 0.00341 | 0.12528 | 0.12183 | 0.1339 | 21.70586 |
| `complex/classes/sloted_classes.py` | yes | 0.04326 | 0.00171 | 0.04259 | 0.04132 | 0.04596 | 21.61172 |
| `complex/classes/simplenamespace.py` | yes | 0.04568 | 0.0047 | 0.04428 | 0.04331 | 0.05895 | 22.69687 |
| `algorithm/twosum/twosum.py` | yes | 0.07881 | 0.00164 | 0.07826 | 0.07724 | 0.08182 | 22.09023 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07947 | 0.0014 | 0.07913 | 0.0781 | 0.08281 | 21.54375 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.07334 | 0.00123 | 0.07281 | 0.07236 | 0.07587 | 22.49336 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.64618 | 0.01028 | 0.64476 | 0.63331 | 0.66519 | 63.89688 |


### **Python 3.10**

```bash
Python 3.10.8

Linux d3d9db88473b 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078816 kB
MemFree:         7324464 kB
MemAvailable:   14459304 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.02988 | 0.00039 | 0.02981 | 0.02937 | 0.0305 | 22.36563 |
| `long_run/processes/generate_fake_data.py` | yes | 0.76088 | 0.00861 | 0.76066 | 0.74431 | 0.77887 | 67.16523 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.71222 | 0.02543 | 1.71145 | 1.66807 | 1.74785 | 44.8375 |
| `long_run/database/postgresql.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `math/pow_using_math.py` | yes | 1.37048 | 0.05611 | 1.34948 | 1.32827 | 1.5136 | 22.56953 |
| `math/pow_simple.py` | yes | 0.41108 | 0.01774 | 0.4072 | 0.39484 | 0.4476 | 22.80078 |
| `modules/json/json_module.py` | yes | 0.33378 | 0.00508 | 0.33268 | 0.32681 | 0.3442 | 23.14883 |
| `modules/json/orjson_module.py` | yes | 0.21609 | 0.00344 | 0.21539 | 0.21134 | 0.2225 | 23.85469 |
| `complex/classes/namedtuple_classes.py` | yes | 0.08415 | 0.00067 | 0.08402 | 0.08299 | 0.08533 | 22.53672 |
| `complex/classes/classes.py` | yes | 0.03927 | 0.0003 | 0.03928 | 0.03876 | 0.03964 | 24.35156 |
| `complex/classes/dataclasses_.py` | yes | 0.11522 | 0.00086 | 0.11535 | 0.11339 | 0.11696 | 23.31289 |
| `complex/classes/sloted_classes.py` | yes | 0.03861 | 0.00037 | 0.03854 | 0.03815 | 0.03935 | 23.45469 |
| `complex/classes/simplenamespace.py` | yes | 0.04058 | 0.00077 | 0.04045 | 0.03996 | 0.04265 | 23.26289 |
| `algorithm/twosum/twosum.py` | yes | 0.07463 | 0.00062 | 0.07468 | 0.07327 | 0.07538 | 23.07422 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07504 | 0.00157 | 0.07485 | 0.07377 | 0.07931 | 22.03594 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06517 | 0.00113 | 0.06463 | 0.06411 | 0.06753 | 23.06289 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.6006 | 0.00652 | 0.59955 | 0.59196 | 0.6118 | 63.60039 |


### **Python 3.11**

```bash
Python 3.11.0

Linux e8fb43dfc07e 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078816 kB
MemFree:         7309676 kB
MemAvailable:   14448116 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `dummy/dummy.py` | yes | 0.01323 | 0.00144 | 0.0127 | 0.01242 | 0.01721 | 25.88047 |
| `long_run/processes/generate_fake_data.py` | yes | 0.75547 | 0.00801 | 0.75754 | 0.74025 | 0.76654 | 71.46484 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.44167 | 0.01769 | 1.44608 | 1.41239 | 1.45933 | 47.07031 |
| `long_run/database/postgresql.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `math/pow_using_math.py` | yes | 1.17107 | 0.02464 | 1.15966 | 1.14829 | 1.21969 | 25.53281 |
| `math/pow_simple.py` | yes | 0.31799 | 0.00503 | 0.31563 | 0.31403 | 0.33007 | 25.68008 |
| `modules/json/json_module.py` | yes | 0.28385 | 0.00999 | 0.27986 | 0.27819 | 0.31016 | 26.29531 |
| `modules/json/orjson_module.py` | yes | 0.17357 | 0.00155 | 0.17321 | 0.17095 | 0.17646 | 26.76211 |
| `complex/classes/namedtuple_classes.py` | yes | 0.07917 | 0.00084 | 0.07898 | 0.07825 | 0.08119 | 26.67109 |
| `complex/classes/classes.py` | yes | 0.02232 | 0.00195 | 0.02179 | 0.01934 | 0.02457 | 27.36875 |
| `complex/classes/dataclasses_.py` | yes | 0.10843 | 0.00089 | 0.10829 | 0.10724 | 0.11023 | 27.0418 |
| `complex/classes/sloted_classes.py` | yes | 0.02138 | 0.00089 | 0.02182 | 0.0194 | 0.02189 | 27.31914 |
| `complex/classes/simplenamespace.py` | yes | 0.0246 | 0.00081 | 0.02434 | 0.02387 | 0.02679 | 27.79961 |
| `algorithm/twosum/twosum.py` | yes | 0.06953 | 0.0008 | 0.06928 | 0.0687 | 0.07134 | 25.91523 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07005 | 0.00105 | 0.06981 | 0.06889 | 0.07237 | 25.85195 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.05598 | 0.00066 | 0.05571 | 0.05508 | 0.05715 | 26.00703 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.60004 | 0.0113 | 0.60021 | 0.58471 | 0.61992 | 68.98984 |

