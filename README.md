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
> Last run: Wed Nov 23 01:10:05 AM -03 2022

### **Python 3.6**

```bash
Python 3.6.15

Linux 85d41708a857 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078816 kB
MemFree:         4921572 kB
MemAvailable:   11985580 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `complex/dataclasses_.py` | no | 0 | 0 | 0 | 0 | 0 | 0.0 |
| `complex/simplenamespace.py` | yes | 0.05209 | 0.0006 | 0.05225 | 0.05106 | 0.05266 | 17.53594 |
| `algorithm/twosum/twosum.py` | yes | 0.08267 | 0.00263 | 0.08128 | 0.0801 | 0.08634 | 13.49219 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.08389 | 0.00427 | 0.08406 | 0.07915 | 0.08894 | 17.95234 |
| `long_run/processes/generate_fake_data.py` | yes | 0.89876 | 0.07297 | 0.8797 | 0.82998 | 1.00086 | 65.18125 |
| `long_run/processes/collect_names_from_site.py` | no | 0 | 0 | 0 | 0 | 0 | 0.0 |
| `math/pow_using_math.py` | yes | 0.0339 | 0.0015 | 0.03328 | 0.03301 | 0.03657 | 21.98828 |
| `math/pow_simple.py` | yes | 0.0337 | 0.00034 | 0.03358 | 0.03341 | 0.03425 | 21.87266 |
| `modules/json/json_module.py` | yes | 0.20243 | 0.00195 | 0.20242 | 0.19948 | 0.20446 | 17.61094 |
| `modules/json/orjson_module.py` | yes | 0.18367 | 0.00224 | 0.18419 | 0.18094 | 0.18592 | 22.77188 |


### **Python 3.7**

```bash
Python 3.7.15

Linux 86d33f01a16e 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078816 kB
MemFree:         4939864 kB
MemAvailable:   12005024 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `complex/dataclasses_.py` | yes | 0.09213 | 0.00179 | 0.09295 | 0.08943 | 0.09365 | 15.98906 |
| `complex/simplenamespace.py` | yes | 0.04044 | 0.00931 | 0.03696 | 0.03379 | 0.05687 | 11.87813 |
| `algorithm/twosum/twosum.py` | yes | 0.06996 | 0.00234 | 0.07047 | 0.06736 | 0.07249 | 12.10391 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07017 | 0.00315 | 0.06974 | 0.06576 | 0.07347 | 19.95469 |
| `long_run/processes/generate_fake_data.py` | yes | 0.86367 | 0.09442 | 0.84429 | 0.75406 | 1.01012 | 68.64766 |
| `long_run/processes/collect_names_from_site.py` | no | 0 | 0 | 0 | 0 | 0 | 0.0 |
| `math/pow_using_math.py` | yes | 0.03145 | 0.0004 | 0.03157 | 0.03103 | 0.032 | 16.01875 |
| `math/pow_simple.py` | yes | 0.02853 | 0.00106 | 0.02826 | 0.02773 | 0.03036 | 15.86719 |
| `modules/json/json_module.py` | yes | 0.18486 | 0.00265 | 0.18419 | 0.18189 | 0.18898 | 21.01875 |
| `modules/json/orjson_module.py` | yes | 0.13423 | 0.01159 | 0.12838 | 0.12724 | 0.15441 | 17.17891 |


### **Python 3.8**

```bash
Python 3.8.15

Linux d2d4cd1d7cf1 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078816 kB
MemFree:         4831592 kB
MemAvailable:   11897812 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `complex/dataclasses_.py` | yes | 0.09645 | 0.00175 | 0.09573 | 0.09542 | 0.09957 | 20.61797 |
| `complex/simplenamespace.py` | yes | 0.03037 | 0.00025 | 0.03034 | 0.03001 | 0.03067 | 16.41875 |
| `algorithm/twosum/twosum.py` | yes | 0.0739 | 0.00086 | 0.07397 | 0.07252 | 0.07463 | 20.38203 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07319 | 0.00047 | 0.07332 | 0.07248 | 0.0737 | 20.49609 |
| `long_run/processes/generate_fake_data.py` | yes | 0.76172 | 0.00656 | 0.76363 | 0.75034 | 0.76708 | 65.61563 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.77313 | 0.02425 | 1.77373 | 1.74319 | 1.80776 | 44.69609 |
| `math/pow_using_math.py` | yes | 0.02924 | 0.00045 | 0.0291 | 0.02864 | 0.02979 | 20.34844 |
| `math/pow_simple.py` | yes | 0.04454 | 0.00809 | 0.04335 | 0.03566 | 0.05772 | 16.38594 |
| `modules/json/json_module.py` | yes | 0.19417 | 0.01449 | 0.18806 | 0.18611 | 0.21995 | 21.26094 |
| `modules/json/orjson_module.py` | yes | 0.1551 | 0.00239 | 0.15522 | 0.15143 | 0.15724 | 12.77266 |


### **Python 3.9**

```bash
Python 3.9.15

Linux 52aefb8f55e6 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078816 kB
MemFree:         4901388 kB
MemAvailable:   11968312 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `complex/dataclasses_.py` | yes | 0.12316 | 0.00453 | 0.12278 | 0.11881 | 0.13028 | 8.96016 |
| `complex/simplenamespace.py` | yes | 0.03462 | 0.00298 | 0.03358 | 0.03275 | 0.03991 | 13.23516 |
| `algorithm/twosum/twosum.py` | yes | 0.08243 | 0.00114 | 0.08292 | 0.08048 | 0.08334 | 21.93359 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.08638 | 0.00612 | 0.08286 | 0.08131 | 0.09587 | 17.29688 |
| `long_run/processes/generate_fake_data.py` | yes | 0.83602 | 0.01421 | 0.83631 | 0.81664 | 0.85123 | 68.43516 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.83408 | 0.03043 | 1.82609 | 1.8075 | 1.88669 | 45.2 |
| `math/pow_using_math.py` | yes | 0.03211 | 0.00112 | 0.0315 | 0.03114 | 0.03339 | 13.47031 |
| `math/pow_simple.py` | yes | 0.03414 | 0.00217 | 0.03456 | 0.03135 | 0.0369 | 22.7625 |
| `modules/json/json_module.py` | yes | 0.19619 | 0.00355 | 0.19682 | 0.19253 | 0.20115 | 17.90391 |
| `modules/json/orjson_module.py` | yes | 0.17309 | 0.00537 | 0.17132 | 0.16879 | 0.18248 | 23.08672 |


### **Python 3.10**

```bash
Python 3.10.8

Linux 6be269c52ca4 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078816 kB
MemFree:         4808816 kB
MemAvailable:   11876828 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `complex/dataclasses_.py` | yes | 0.11419 | 0.00424 | 0.11319 | 0.10952 | 0.11995 | 17.89688 |
| `complex/simplenamespace.py` | yes | 0.03641 | 0.00252 | 0.03566 | 0.03448 | 0.04072 | 23.22969 |
| `algorithm/twosum/twosum.py` | yes | 0.07971 | 0.00258 | 0.0785 | 0.07715 | 0.08348 | 23.22031 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.08249 | 0.00584 | 0.08046 | 0.07694 | 0.09214 | 22.18906 |
| `long_run/processes/generate_fake_data.py` | yes | 0.81879 | 0.0121 | 0.82538 | 0.80148 | 0.83024 | 67.52187 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.77777 | 0.0223 | 1.7832 | 1.74195 | 1.80003 | 44.89219 |
| `math/pow_using_math.py` | yes | 0.03171 | 0.0005 | 0.03146 | 0.03135 | 0.03258 | 22.7375 |
| `math/pow_simple.py` | yes | 0.03284 | 0.00311 | 0.03088 | 0.03027 | 0.03693 | 18.34844 |
| `modules/json/json_module.py` | yes | 0.17761 | 0.00394 | 0.17967 | 0.17292 | 0.18094 | 23.38047 |
| `modules/json/orjson_module.py` | yes | 0.16953 | 0.01042 | 0.16965 | 0.15736 | 0.18451 | 19.23672 |


### **Python 3.11**

```bash
Python 3.11.0

Linux da0e9f420241 5.15.0-53-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078816 kB
MemFree:         4812976 kB
MemAvailable:   11881692 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `complex/dataclasses_.py` | yes | 0.11373 | 0.00666 | 0.11235 | 0.10754 | 0.12473 | 20.52734 |
| `complex/simplenamespace.py` | yes | 0.01666 | 0.00116 | 0.01616 | 0.01563 | 0.01797 | 25.98672 |
| `algorithm/twosum/twosum.py` | yes | 0.07852 | 0.00068 | 0.07848 | 0.07769 | 0.07954 | 26.04219 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07906 | 0.00359 | 0.0799 | 0.07525 | 0.08318 | 15.57656 |
| `long_run/processes/generate_fake_data.py` | yes | 0.79946 | 0.01685 | 0.804 | 0.77227 | 0.81395 | 72.07266 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.47817 | 0.03539 | 1.46613 | 1.44877 | 1.53965 | 47.25078 |
| `math/pow_using_math.py` | yes | 0.01315 | 0.00045 | 0.01297 | 0.01266 | 0.01372 | 15.40078 |
| `math/pow_simple.py` | yes | 0.01277 | 0.00012 | 0.01277 | 0.01263 | 0.01295 | 15.45625 |
| `modules/json/json_module.py` | yes | 0.14917 | 0.00298 | 0.14888 | 0.14615 | 0.15307 | 26.41016 |
| `modules/json/orjson_module.py` | yes | 0.13045 | 0.00281 | 0.12878 | 0.12854 | 0.13512 | 21.48594 |

