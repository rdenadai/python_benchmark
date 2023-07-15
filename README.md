# Python Benchmark

This is a simple repo to validate and test any (almost any) python program againts all python 3 versions.

- Python 3.6.15
- Python 3.7.16
- Python 3.8.16
- Python 3.9.16
- Python 3.10.11
- Python 3.11.3
- Python 3.12b1

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

> Last run: Sat Jul 15 19:49:12 UTC 2023
### **Comparison**

#### How much faster 3.12 is? (Mean / Median from 3.6 to 3.11)
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 |
|:---|---:|---:|---:|---:|---:|---:|
---

#### How much more memory 3.12 uses? (Memory diff from 3.6 to 3.11)
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 |
|:---|---:|---:|---:|---:|---:|---:|
---

#### **Execution**

##### **Mean [s]**
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
|:---|---:|---:|---:|---:|---:|---:|---:|

##### **Median [s]**
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
|:---|---:|---:|---:|---:|---:|---:|---:|

#### **Memory Usage**

##### **MEM [MB]**
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
|:---|---:|---:|---:|---:|---:|---:|---:|

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

Linux bc1368c05eea 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          2
Model name:                      Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
Thread(s) per core:              1
Core(s) per socket:              2
NUMA node(s):                    1
NUMA node0 CPU(s):               0,1

MemTotal:        4014620 kB
MemFree:          323824 kB
MemAvailable:    2798848 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|


### **Python 3.11**

```bash
Python 3.11.4

Linux df7fca977258 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          2
Model name:                      Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
Thread(s) per core:              1
Core(s) per socket:              2
NUMA node(s):                    1
NUMA node0 CPU(s):               0,1

MemTotal:        4014620 kB
MemFree:          346424 kB
MemAvailable:    2736188 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|


### **Python 3.12**

```bash
Python 3.12.0b4

Linux c2679a3504bc 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          2
Model name:                      Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
Thread(s) per core:              1
Core(s) per socket:              2
NUMA node(s):                    1
NUMA node0 CPU(s):               0,1

MemTotal:        4014620 kB
MemFree:          801596 kB
MemAvailable:    3193772 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|

