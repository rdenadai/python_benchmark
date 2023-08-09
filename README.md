# Python Benchmark

This is a simple repo to validate and test any (almost any) python program againts all python 3 versions.

- Python 3.6.15
- Python 3.7.17
- Python 3.8.17
- Python 3.9.17
- Python 3.10.12
- Python 3.11.4
- Python 3.12.0rc1

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

> Last run: Wed Aug  9 03:43:05 PM -03 2023
### **Comparison**

#### How much faster 3.12 is? (Mean / Median from 3.6 to 3.11)
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 21.99% / 21.77% | 21.36% / 22.44% | 6.94% / 6.15% | 10.10% / 8.89% | 2.20% / 2.67% | -14.06% / -14.78% |
| `algorithm/search/hashmap_lookup.py` | 25.30% / 25.72% | 20.58% / 21.75% | 4.52% / 4.82% | 11.29% / 11.67% | 3.18% / 2.93% | -12.44% / -11.79% |
| `algorithm/search/index.py` | 28.21% / 28.64% | 22.02% / 23.10% | 4.51% / 4.50% | 9.55% / 8.23% | 2.24% / 3.04% | -12.36% / -12.04% |
| `algorithm/search/linear.py` | 23.24% / 23.83% | 19.72% / 19.52% | 9.70% / 8.47% | 10.30% / 8.45% | 4.53% / 2.82% | -11.89% / -12.08% |
| `algorithm/twosum/twosum.py` | -4.56% / -10.24% | -22.70% / -22.22% | -25.03% / -24.24% | -14.65% / -13.83% | -11.70% / -11.99% | -14.49% / -15.32% |
| `algorithm/twosum/twosum_naive.py` | -10.61% / -11.53% | -18.73% / -19.68% | -21.28% / -23.24% | -11.02% / -15.22% | -9.97% / -12.16% | -14.93% / -17.45% |
| `complex/classes/classes.py` | 106.38% / 114.83% | 82.58% / 79.31% | 91.10% / 100.39% | 83.33% / 89.58% | 80.78% / 85.99% | -3.34% / -0.39% |
| `complex/classes/dataclasses_.py` | -- / -- | -18.93% / -19.48% | -16.47% / -19.41% | -7.86% / -9.01% | -3.66% / -5.06% | -12.63% / -13.18% |
| `complex/classes/namedtuple_classes.py` | 3.29% / 5.12% | -15.36% / -15.41% | -0.63% / -4.33% | -4.90% / -4.44% | -3.77% / -4.03% | -12.64% / -12.46% |
| `complex/classes/simplenamespace.py` | 118.18% / 115.14% | 39.46% / 43.15% | 33.33% / 31.97% | 53.51% / 53.80% | 49.91% / 46.58% | -13.15% / -13.75% |
| `complex/classes/sloted_classes.py` | 117.80% / 117.44% | 88.13% / 86.53% | 113.14% / 96.15% | 101.00% / 102.00% | 89.79% / 92.46% | 4.47% / -3.02% |
| `complex/generators/simple.py` | 51.94% / 50.83% | 39.45% / 39.27% | 24.65% / 26.21% | 38.78% / 43.65% | 36.53% / 40.84% | -5.19% / -9.83% |
| `dummy/dummy.py` | 130.21% / 125.62% | 77.93% / 80.08% | 79.39% / 78.83% | 96.60% / 94.95% | 103.86% / 104.76% | -22.83% / -21.70% |
| `long_run/database/postgresql.py` | -19.95% / -21.34% | -21.94% / -20.89% | -20.92% / -21.17% | -7.45% / -6.58% | -15.89% / -15.41% | -15.08% / -14.27% |
| `long_run/database/sqlite_.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/file/load_titanic_csv_pandas.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/file/load_titanic_csv_python.py` | 42.31% / 47.07% | 6.00% / 0.22% | -4.57% / -5.18% | 5.82% / 2.59% | 11.93% / 10.62% | -10.37% / -12.19% |
| `long_run/processes/collect_names_from_site.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/processes/generate_fake_data.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/processes/maze_generator.py` | 64.88% / 64.37% | 67.55% / 70.86% | 62.89% / 61.23% | 74.74% / 79.07% | 32.61% / 29.90% | -4.43% / -2.68% |
| `long_run/text/clean_text.py` | 12.27% / 9.13% | 0.94% / 1.58% | 0.18% / 0.04% | 6.11% / 5.83% | 7.10% / 5.63% | -4.43% / -5.24% |
| `long_run/text/count_words.py` | 12.68% / 5.28% | 2.87% / 1.39% | -0.60% / -1.33% | 9.80% / 9.77% | 10.75% / 5.58% | -7.37% / -10.18% |
| `math/haversine.py` | -13.40% / -14.77% | 8.90% / 6.55% | -6.16% / -6.93% | 12.59% / 9.53% | 4.75% / 1.56% | -10.31% / -11.72% |
| `math/mandelbrot.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `math/pow_simple.py` | 102.73% / 103.15% | 157.64% / 151.89% | 115.11% / 115.83% | 146.90% / 147.25% | 118.82% / 118.99% | 14.66% / 13.36% |
| `math/pow_using_math.py` | 13.60% / 11.48% | 43.11% / 43.22% | 9.54% / 8.10% | 20.12% / 18.15% | 18.97% / 18.35% | -3.75% / -3.55% |
| `modules/json/json_module.py` | 23.65% / 25.52% | 21.09% / 23.02% | 19.76% / 24.30% | 23.68% / 25.93% | 9.69% / 12.04% | -3.07% / -1.53% |
| `modules/json/orjson_module.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
---

#### How much more memory 3.12 uses? (Memory diff from 3.6 to 3.11)
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 20.61% | 18.58% | 17.51% | 9.47% | 3.85% | -1.96% |
| `algorithm/search/hashmap_lookup.py` | 28.25% | 17.08% | 19.04% | 16.89% | 6.21% | -1.51% |
| `algorithm/search/index.py` | 21.55% | 17.58% | 16.65% | 12.28% | 9.2% | -0.79% |
| `algorithm/search/linear.py` | 20.63% | 14.5% | 17.16% | 13.83% | 8.45% | -3.23% |
| `algorithm/twosum/twosum.py` | 23.68% | 29.02% | 24.64% | 16.02% | 15.48% | 0.94% |
| `algorithm/twosum/twosum_naive.py` | 24.08% | 29.65% | 25.05% | 20.27% | 15.11% | 3.17% |
| `complex/classes/classes.py` | 28.49% | 31.01% | 28.84% | 17.3% | 9.26% | -2.09% |
| `complex/classes/dataclasses_.py` | -- | 33.41% | 27.38% | 16.79% | 7.14% | 1.05% |
| `complex/classes/namedtuple_classes.py` | 26.24% | 32.09% | 28.53% | 19.4% | 16.16% | 3.17% |
| `complex/classes/simplenamespace.py` | 34.51% | 38.28% | 31.37% | 26.43% | 13.47% | 2.16% |
| `complex/classes/sloted_classes.py` | 28.27% | 32.8% | 27.5% | 22.29% | 10.6% | 0.83% |
| `complex/generators/simple.py` | 34.06% | 39.22% | 36.15% | 22.9% | 12.84% | 3.71% |
| `dummy/dummy.py` | 27.33% | 29.1% | 25.35% | 16.42% | 16.64% | 1.2% |
| `long_run/database/postgresql.py` | 22.95% | 19.94% | 18.68% | 10.5% | 14.17% | 4.86% |
| `long_run/database/sqlite_.py` | -- | -- | -- | -- | -- | -- |
| `long_run/file/load_titanic_csv_pandas.py` | -- | -- | -- | -- | -- | -- |
| `long_run/file/load_titanic_csv_python.py` | 27.02% | 31.04% | 27.35% | 18.27% | 19.45% | 3.65% |
| `long_run/processes/collect_names_from_site.py` | -- | -- | -- | -- | -- | -- |
| `long_run/processes/generate_fake_data.py` | -- | -- | -- | -- | -- | -- |
| `long_run/processes/maze_generator.py` | 32.16% | 29.43% | 28.79% | 19.96% | 18.97% | 5.22% |
| `long_run/text/clean_text.py` | 24.29% | 29.04% | 25.13% | 16.53% | 15.39% | 1.61% |
| `long_run/text/count_words.py` | 26.98% | 29.46% | 25.74% | 15.31% | 13.25% | 2.89% |
| `math/haversine.py` | 26.77% | 30.45% | 25.63% | 16.61% | 16.89% | 3.53% |
| `math/mandelbrot.py` | -- | -- | -- | -- | -- | -- |
| `math/pow_simple.py` | 27.81% | 30.01% | 26.27% | 16.52% | 15.16% | 3.68% |
| `math/pow_using_math.py` | 26.77% | 30.13% | 26.37% | 16.68% | 13.1% | 2.61% |
| `modules/json/json_module.py` | 29.92% | 26.9% | 27.5% | 18.47% | 17.12% | 4.0% |
| `modules/json/orjson_module.py` | -- | -- | -- | -- | -- | -- |
---

#### **Execution**

##### **Mean [s]**
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 1.69531 | 1.68654 | 1.48611 | 1.52999 | 1.42023 | 1.19427 | 1.38969 |
| `algorithm/search/hashmap_lookup.py` | 1.73487 | 1.66957 | 1.44718 | 1.5409 | 1.42864 | 1.21232 | 1.38459 |
| `algorithm/search/index.py` | 1.78044 | 1.69446 | 1.45126 | 1.52132 | 1.41971 | 1.21697 | 1.38865 |
| `algorithm/search/linear.py` | 1.76945 | 1.71896 | 1.57514 | 1.58368 | 1.50093 | 1.26511 | 1.43582 |
| `algorithm/twosum/twosum.py` | 0.09926 | 0.08039 | 0.07797 | 0.08876 | 0.09183 | 0.08893 | 0.104 |
| `algorithm/twosum/twosum_naive.py` | 0.09111 | 0.08283 | 0.08023 | 0.09069 | 0.09176 | 0.0867 | 0.10192 |
| `complex/classes/classes.py` | 0.05498 | 0.04864 | 0.05091 | 0.04884 | 0.04816 | 0.02575 | 0.02664 |
| `complex/classes/dataclasses_.py` | -- | 0.12416 | 0.12794 | 0.14112 | 0.14756 | 0.13382 | 0.15316 |
| `complex/classes/namedtuple_classes.py` | 0.11656 | 0.09552 | 0.11214 | 0.10732 | 0.1086 | 0.09859 | 0.11285 |
| `complex/classes/simplenamespace.py` | 0.07514 | 0.04803 | 0.04592 | 0.05287 | 0.05163 | 0.02991 | 0.03444 |
| `complex/classes/sloted_classes.py` | 0.05652 | 0.04882 | 0.05531 | 0.05216 | 0.04925 | 0.02711 | 0.02595 |
| `complex/generators/simple.py` | 0.07957 | 0.07303 | 0.06528 | 0.07268 | 0.0715 | 0.04965 | 0.05237 |
| `dummy/dummy.py` | 0.03932 | 0.03039 | 0.03064 | 0.03358 | 0.03482 | 0.01318 | 0.01708 |
| `long_run/database/postgresql.py` | 0.16714 | 0.16298 | 0.16512 | 0.19325 | 0.17562 | 0.17732 | 0.2088 |
| `long_run/database/sqlite_.py` | 0.64942 | 0.6225 | 0.63197 | 0.74685 | 0.7041 | 0.70201 | -- |
| `long_run/file/load_titanic_csv_pandas.py` | 0.76741 | 0.66621 | 0.68714 | 0.755 | 0.76406 | 0.74635 | -- |
| `long_run/file/load_titanic_csv_python.py` | 0.1117 | 0.0832 | 0.0749 | 0.08306 | 0.08785 | 0.07035 | 0.07849 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 2.08503 | 2.247 | 2.13051 | 1.84199 | -- |
| `long_run/processes/generate_fake_data.py` | 0.95498 | 0.92023 | 0.92717 | 1.02818 | 0.95808 | 0.93505 | -- |
| `long_run/processes/maze_generator.py` | 0.36909 | 0.37506 | 0.36464 | 0.39116 | 0.29685 | 0.21394 | 0.22385 |
| `long_run/text/clean_text.py` | 0.32017 | 0.28788 | 0.28569 | 0.30261 | 0.30544 | 0.27257 | 0.28519 |
| `long_run/text/count_words.py` | 0.1069 | 0.09759 | 0.0943 | 0.10417 | 0.10507 | 0.08788 | 0.09487 |
| `math/haversine.py` | 0.86711 | 1.09047 | 0.9396 | 1.12738 | 1.0489 | 0.8981 | 1.00133 |
| `math/mandelbrot.py` | 3.67742 | 3.51183 | 3.52718 | 3.01772 | 3.00763 | 3.02417 | -- |
| `math/pow_simple.py` | 0.72302 | 0.91884 | 0.76718 | 0.88054 | 0.7804 | 0.40891 | 0.35664 |
| `math/pow_using_math.py` | 1.51287 | 1.90588 | 1.45879 | 1.59969 | 1.5844 | 1.28182 | 1.33177 |
| `modules/json/json_module.py` | 0.56449 | 0.5528 | 0.54672 | 0.56462 | 0.50076 | 0.44251 | 0.45653 |
| `modules/json/orjson_module.py` | 0.35224 | 0.28909 | 0.30919 | 0.3782 | 0.34723 | 0.29741 | -- |

##### **Median [s]**
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 1.69248 | 1.70177 | 1.47536 | 1.51353 | 1.42701 | 1.18451 | 1.38991 |
| `algorithm/search/hashmap_lookup.py` | 1.7283 | 1.67377 | 1.44102 | 1.53524 | 1.415 | 1.21269 | 1.37474 |
| `algorithm/search/index.py` | 1.7772 | 1.7006 | 1.44367 | 1.49521 | 1.42345 | 1.21515 | 1.38148 |
| `algorithm/search/linear.py` | 1.7786 | 1.71668 | 1.55799 | 1.55767 | 1.47679 | 1.26278 | 1.43635 |
| `algorithm/twosum/twosum.py` | 0.09234 | 0.08001 | 0.07793 | 0.08864 | 0.09054 | 0.08711 | 0.10287 |
| `algorithm/twosum/twosum_naive.py` | 0.09204 | 0.08357 | 0.07986 | 0.08821 | 0.09139 | 0.08588 | 0.10404 |
| `complex/classes/classes.py` | 0.05504 | 0.04594 | 0.05134 | 0.04857 | 0.04765 | 0.02552 | 0.02562 |
| `complex/classes/dataclasses_.py` | -- | 0.12419 | 0.1243 | 0.14033 | 0.14643 | 0.13391 | 0.15423 |
| `complex/classes/namedtuple_classes.py` | 0.11672 | 0.09393 | 0.10623 | 0.10611 | 0.10657 | 0.0972 | 0.11104 |
| `complex/classes/simplenamespace.py` | 0.07274 | 0.0484 | 0.04462 | 0.052 | 0.04956 | 0.02916 | 0.03381 |
| `complex/classes/sloted_classes.py` | 0.05536 | 0.04749 | 0.04994 | 0.05143 | 0.049 | 0.02469 | 0.02546 |
| `complex/generators/simple.py` | 0.07751 | 0.07157 | 0.06486 | 0.07382 | 0.07238 | 0.04634 | 0.05139 |
| `dummy/dummy.py` | 0.03795 | 0.03029 | 0.03008 | 0.03279 | 0.03444 | 0.01317 | 0.01682 |
| `long_run/database/postgresql.py` | 0.16226 | 0.16319 | 0.16262 | 0.19271 | 0.1745 | 0.17684 | 0.20628 |
| `long_run/database/sqlite_.py` | 0.64961 | 0.61686 | 0.63006 | 0.74705 | 0.70219 | 0.70141 | -- |
| `long_run/file/load_titanic_csv_pandas.py` | 0.76594 | 0.66415 | 0.68559 | 0.74713 | 0.75719 | 0.7406 | -- |
| `long_run/file/load_titanic_csv_python.py` | 0.11582 | 0.07892 | 0.07467 | 0.08079 | 0.08711 | 0.06915 | 0.07875 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 2.08258 | 2.24778 | 2.13237 | 1.83253 | -- |
| `long_run/processes/generate_fake_data.py` | 0.95223 | 0.91061 | 0.9216 | 0.99667 | 0.95443 | 0.93369 | -- |
| `long_run/processes/maze_generator.py` | 0.36973 | 0.38434 | 0.36268 | 0.4028 | 0.2922 | 0.21891 | 0.22494 |
| `long_run/text/clean_text.py` | 0.31083 | 0.28933 | 0.28495 | 0.30143 | 0.30086 | 0.2699 | 0.28483 |
| `long_run/text/count_words.py` | 0.10033 | 0.09662 | 0.09403 | 0.10461 | 0.10062 | 0.0856 | 0.0953 |
| `math/haversine.py` | 0.86199 | 1.07761 | 0.94126 | 1.10783 | 1.02721 | 0.89291 | 1.0114 |
| `math/mandelbrot.py` | 3.67466 | 3.51841 | 3.53433 | 3.02291 | 3.00062 | 3.00532 | -- |
| `math/pow_simple.py` | 0.724 | 0.8977 | 0.76919 | 0.88116 | 0.78045 | 0.40398 | 0.35638 |
| `math/pow_using_math.py` | 1.4831 | 1.90539 | 1.43816 | 1.57183 | 1.57453 | 1.28307 | 1.33035 |
| `modules/json/json_module.py` | 0.56295 | 0.55176 | 0.5575 | 0.56481 | 0.50252 | 0.44165 | 0.44851 |
| `modules/json/orjson_module.py` | 0.34727 | 0.29147 | 0.31035 | 0.37767 | 0.34459 | 0.29638 | -- |

#### **Memory Usage**

##### **MEM [MB]**
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 28.94643 | 29.44141 | 29.70982 | 31.89174 | 33.61607 | 35.61049 | 34.91127 |
| `algorithm/search/hashmap_lookup.py` | 28.02455 | 30.69922 | 30.19252 | 30.74777 | 33.8404 | 36.49219 | 35.94252 |
| `algorithm/search/index.py` | 28.60045 | 29.56641 | 29.80357 | 30.96261 | 31.83705 | 35.04185 | 34.76507 |
| `algorithm/search/linear.py` | 28.88616 | 30.43136 | 29.74275 | 30.61049 | 32.1317 | 36.00781 | 34.84542 |
| `algorithm/twosum/twosum.py` | 22.02567 | 21.11384 | 21.85491 | 23.47824 | 23.58929 | 26.98661 | 27.24051 |
| `algorithm/twosum/twosum_naive.py` | 22.01395 | 21.06752 | 21.84263 | 22.71094 | 23.72879 | 26.476 | 27.31473 |
| `complex/classes/classes.py` | 21.71596 | 21.29799 | 21.65737 | 23.78683 | 25.53795 | 28.49833 | 27.9029 |
| `complex/classes/dataclasses_.py` | -- | 21.0519 | 22.04799 | 24.04855 | 26.21373 | 27.79241 | 28.08538 |
| `complex/classes/namedtuple_classes.py` | 22.17355 | 21.19196 | 21.77902 | 23.44308 | 24.09821 | 27.13281 | 27.99219 |
| `complex/classes/simplenamespace.py` | 21.60603 | 21.01674 | 22.12221 | 22.98605 | 25.61161 | 28.44643 | 29.06194 |
| `complex/classes/sloted_classes.py` | 21.83371 | 21.08929 | 21.96596 | 22.90179 | 25.32143 | 27.77679 | 28.00614 |
| `complex/generators/simple.py` | 21.98661 | 21.17188 | 21.64844 | 23.98326 | 26.12165 | 28.42076 | 29.47489 |
| `dummy/dummy.py` | 21.37054 | 21.07701 | 21.70759 | 23.37165 | 23.32757 | 26.88728 | 27.21038 |
| `long_run/database/postgresql.py` | 26.32031 | 26.98103 | 27.26786 | 29.28683 | 28.34431 | 30.85937 | 32.36049 |
| `long_run/database/sqlite_.py` | 62.976 | 66.14342 | 66.40402 | 66.93136 | 67.13225 | 72.41685 | -- |
| `long_run/file/load_titanic_csv_pandas.py` | 61.7394 | 64.36217 | 64.89007 | 65.59487 | 64.68304 | 70.65123 | -- |
| `long_run/file/load_titanic_csv_python.py` | 21.86049 | 21.19029 | 21.80413 | 23.47935 | 23.24609 | 26.78906 | 27.76786 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 45.29074 | 45.43471 | 45.42913 | 47.59319 | -- |
| `long_run/processes/generate_fake_data.py` | 64.4548 | 69.2779 | 66.60268 | 69.61217 | 68.57143 | 72.39621 | -- |
| `long_run/processes/maze_generator.py` | 21.43527 | 21.88728 | 21.99609 | 23.61607 | 23.8125 | 26.92355 | 28.32868 |
| `long_run/text/clean_text.py` | 22.05246 | 21.24107 | 21.90458 | 23.52176 | 23.75335 | 26.97545 | 27.40904 |
| `long_run/text/count_words.py` | 21.49944 | 21.08705 | 21.7115 | 23.67522 | 24.10435 | 26.53348 | 27.29911 |
| `math/haversine.py` | 21.58538 | 20.97656 | 21.78125 | 23.46652 | 23.40848 | 26.42969 | 27.36328 |
| `math/mandelbrot.py` | 36.28571 | 35.39174 | 35.88616 | 43.63393 | 39.4135 | 40.95201 | -- |
| `math/pow_simple.py` | 21.43025 | 21.06752 | 21.69196 | 23.50725 | 23.78404 | 26.41908 | 27.39062 |
| `math/pow_using_math.py` | 21.58259 | 21.02511 | 21.65067 | 23.44978 | 24.19085 | 26.66574 | 27.36049 |
| `modules/json/json_module.py` | 21.59877 | 22.11328 | 22.00781 | 23.68694 | 23.95926 | 26.98047 | 28.06083 |
| `modules/json/orjson_module.py` | 22.26563 | 22.46373 | 22.38728 | 24.07366 | 24.56585 | 26.90458 | -- |

---


### **Python 3.6**

```bash
Python 3.6.15

Linux 152c60f30b6b 5.15.0-78-generic unknown GNU/Linux

CPU(s):                          12
Thread(s) per core:              2
Core(s) per socket:              6
NUMA node(s):                    1
Model name:                      Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:                     4100.0000
NUMA node0 CPU(s):               0-11

MemTotal:       16066528 kB
MemFree:          906176 kB
MemAvailable:    7365140 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.69531 | 0.0286 | 1.69248 | 1.66043 | 1.73026 | 28.94643 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.73487 | 0.04248 | 1.7283 | 1.69035 | 1.79462 | 28.02455 |
| `algorithm/search/index.py` | yes | 1.78044 | 0.06586 | 1.7772 | 1.71313 | 1.8984 | 28.60045 |
| `algorithm/search/linear.py` | yes | 1.76945 | 0.02091 | 1.7786 | 1.74255 | 1.78962 | 28.88616 |
| `algorithm/twosum/twosum.py` | yes | 0.09926 | 0.01232 | 0.09234 | 0.08897 | 0.12252 | 22.02567 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.09111 | 0.00456 | 0.09204 | 0.08646 | 0.09753 | 22.01395 |
| `complex/classes/classes.py` | yes | 0.05498 | 0.00202 | 0.05504 | 0.05256 | 0.05881 | 21.71596 |
| `complex/classes/dataclasses_.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `complex/classes/namedtuple_classes.py` | yes | 0.11656 | 0.00331 | 0.11672 | 0.1117 | 0.12136 | 22.17355 |
| `complex/classes/simplenamespace.py` | yes | 0.07514 | 0.00446 | 0.07274 | 0.0711 | 0.08137 | 21.60603 |
| `complex/classes/sloted_classes.py` | yes | 0.05652 | 0.00203 | 0.05536 | 0.05471 | 0.06001 | 21.83371 |
| `complex/generators/simple.py` | yes | 0.07957 | 0.00468 | 0.07751 | 0.07581 | 0.08766 | 21.98661 |
| `dummy/dummy.py` | yes | 0.03932 | 0.00464 | 0.03795 | 0.03566 | 0.0496 | 21.37054 |
| `long_run/database/postgresql.py` | yes | 0.16714 | 0.01119 | 0.16226 | 0.15803 | 0.18534 | 26.32031 |
| `long_run/database/sqlite_.py` | yes | 0.64942 | 0.00918 | 0.64961 | 0.63972 | 0.66284 | 62.976 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.76741 | 0.02737 | 0.76594 | 0.73531 | 0.82307 | 61.7394 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.1117 | 0.02303 | 0.11582 | 0.07812 | 0.13697 | 21.86049 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | yes | 0.95498 | 0.038 | 0.95223 | 0.89409 | 1.00144 | 64.4548 |
| `long_run/processes/maze_generator.py` | yes | 0.36909 | 0.01771 | 0.36973 | 0.33707 | 0.39495 | 21.43527 |
| `long_run/text/clean_text.py` | yes | 0.32017 | 0.02399 | 0.31083 | 0.29766 | 0.35427 | 22.05246 |
| `long_run/text/count_words.py` | yes | 0.1069 | 0.0134 | 0.10033 | 0.09558 | 0.13464 | 21.49944 |
| `math/haversine.py` | yes | 0.86711 | 0.01601 | 0.86199 | 0.85481 | 0.90179 | 21.58538 |
| `math/mandelbrot.py` | yes | 3.67742 | 0.08522 | 3.67466 | 3.60726 | 3.85764 | 36.28571 |
| `math/pow_simple.py` | yes | 0.72302 | 0.013 | 0.724 | 0.70116 | 0.73813 | 21.43025 |
| `math/pow_using_math.py` | yes | 1.51287 | 0.0536 | 1.4831 | 1.46343 | 1.61973 | 21.58259 |
| `modules/json/json_module.py` | yes | 0.56449 | 0.00869 | 0.56295 | 0.55054 | 0.57608 | 21.59877 |
| `modules/json/orjson_module.py` | yes | 0.35224 | 0.02189 | 0.34727 | 0.33621 | 0.39988 | 22.26563 |


### **Python 3.7**

```bash
Python 3.7.17

Linux 431021ab462b 5.15.0-78-generic unknown GNU/Linux

CPU(s):                          12
Model name:                      Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:              2
Core(s) per socket:              6
CPU max MHz:                     4100.0000
NUMA node(s):                    1
NUMA node0 CPU(s):               0-11

MemTotal:       16066528 kB
MemFree:          502960 kB
MemAvailable:    7024844 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.68654 | 0.04204 | 1.70177 | 1.62229 | 1.74018 | 29.44141 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.66957 | 0.0166 | 1.67377 | 1.64803 | 1.69448 | 30.69922 |
| `algorithm/search/index.py` | yes | 1.69446 | 0.01957 | 1.7006 | 1.65483 | 1.71691 | 29.56641 |
| `algorithm/search/linear.py` | yes | 1.71896 | 0.03596 | 1.71668 | 1.67119 | 1.77302 | 30.43136 |
| `algorithm/twosum/twosum.py` | yes | 0.08039 | 0.0024 | 0.08001 | 0.07694 | 0.08299 | 21.11384 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.08283 | 0.00222 | 0.08357 | 0.0792 | 0.08525 | 21.06752 |
| `complex/classes/classes.py` | yes | 0.04864 | 0.00431 | 0.04594 | 0.04491 | 0.05538 | 21.29799 |
| `complex/classes/dataclasses_.py` | yes | 0.12416 | 0.00351 | 0.12419 | 0.12004 | 0.12886 | 21.0519 |
| `complex/classes/namedtuple_classes.py` | yes | 0.09552 | 0.00313 | 0.09393 | 0.09283 | 0.10104 | 21.19196 |
| `complex/classes/simplenamespace.py` | yes | 0.04803 | 0.00173 | 0.0484 | 0.04557 | 0.04996 | 21.01674 |
| `complex/classes/sloted_classes.py` | yes | 0.04882 | 0.0042 | 0.04749 | 0.04488 | 0.05708 | 21.08929 |
| `complex/generators/simple.py` | yes | 0.07303 | 0.00432 | 0.07157 | 0.06945 | 0.08209 | 21.17188 |
| `dummy/dummy.py` | yes | 0.03039 | 0.00143 | 0.03029 | 0.02866 | 0.03234 | 21.07701 |
| `long_run/database/postgresql.py` | yes | 0.16298 | 0.00531 | 0.16319 | 0.15732 | 0.17191 | 26.98103 |
| `long_run/database/sqlite_.py` | yes | 0.6225 | 0.01723 | 0.61686 | 0.60365 | 0.65491 | 66.14342 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.66621 | 0.0141 | 0.66415 | 0.65273 | 0.68741 | 64.36217 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.0832 | 0.00824 | 0.07892 | 0.07399 | 0.09554 | 21.19029 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | yes | 0.92023 | 0.02964 | 0.91061 | 0.89688 | 0.98086 | 69.2779 |
| `long_run/processes/maze_generator.py` | yes | 0.37506 | 0.02785 | 0.38434 | 0.3388 | 0.4126 | 21.88728 |
| `long_run/text/clean_text.py` | yes | 0.28788 | 0.00651 | 0.28933 | 0.28006 | 0.2979 | 21.24107 |
| `long_run/text/count_words.py` | yes | 0.09759 | 0.00428 | 0.09662 | 0.09213 | 0.10607 | 21.08705 |
| `math/haversine.py` | yes | 1.09047 | 0.04401 | 1.07761 | 1.05379 | 1.17172 | 20.97656 |
| `math/mandelbrot.py` | yes | 3.51183 | 0.0568 | 3.51841 | 3.43401 | 3.59024 | 35.39174 |
| `math/pow_simple.py` | yes | 0.91884 | 0.07288 | 0.8977 | 0.86559 | 1.07916 | 21.06752 |
| `math/pow_using_math.py` | yes | 1.90588 | 0.04481 | 1.90539 | 1.82763 | 1.95792 | 21.02511 |
| `modules/json/json_module.py` | yes | 0.5528 | 0.01505 | 0.55176 | 0.52993 | 0.57525 | 22.11328 |
| `modules/json/orjson_module.py` | yes | 0.28909 | 0.00891 | 0.29147 | 0.27422 | 0.2996 | 22.46373 |


### **Python 3.8**

```bash
Python 3.8.17

Linux d578ded9e5f1 5.15.0-78-generic unknown GNU/Linux

CPU(s):                          12
Model name:                      Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:              2
Core(s) per socket:              6
CPU max MHz:                     4100.0000
NUMA node(s):                    1
NUMA node0 CPU(s):               0-11

MemTotal:       16066528 kB
MemFree:         1163104 kB
MemAvailable:    7239908 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.48611 | 0.03808 | 1.47536 | 1.44586 | 1.54807 | 29.70982 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.44718 | 0.038 | 1.44102 | 1.41415 | 1.52858 | 30.19252 |
| `algorithm/search/index.py` | yes | 1.45126 | 0.01856 | 1.44367 | 1.43135 | 1.47583 | 29.80357 |
| `algorithm/search/linear.py` | yes | 1.57514 | 0.04515 | 1.55799 | 1.52072 | 1.65575 | 29.74275 |
| `algorithm/twosum/twosum.py` | yes | 0.07797 | 0.00174 | 0.07793 | 0.0757 | 0.08085 | 21.85491 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.08023 | 0.00232 | 0.07986 | 0.07763 | 0.08334 | 21.84263 |
| `complex/classes/classes.py` | yes | 0.05091 | 0.00173 | 0.05134 | 0.04828 | 0.05344 | 21.65737 |
| `complex/classes/dataclasses_.py` | yes | 0.12794 | 0.01321 | 0.1243 | 0.11604 | 0.1488 | 22.04799 |
| `complex/classes/namedtuple_classes.py` | yes | 0.11214 | 0.01378 | 0.10623 | 0.10127 | 0.14061 | 21.77902 |
| `complex/classes/simplenamespace.py` | yes | 0.04592 | 0.00247 | 0.04462 | 0.04414 | 0.05094 | 22.12221 |
| `complex/classes/sloted_classes.py` | yes | 0.05531 | 0.01521 | 0.04994 | 0.04707 | 0.08952 | 21.96596 |
| `complex/generators/simple.py` | yes | 0.06528 | 0.00121 | 0.06486 | 0.06431 | 0.06791 | 21.64844 |
| `dummy/dummy.py` | yes | 0.03064 | 0.00116 | 0.03008 | 0.02943 | 0.03226 | 21.70759 |
| `long_run/database/postgresql.py` | yes | 0.16512 | 0.00882 | 0.16262 | 0.15604 | 0.18043 | 27.26786 |
| `long_run/database/sqlite_.py` | yes | 0.63197 | 0.00695 | 0.63006 | 0.62241 | 0.64178 | 66.40402 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.68714 | 0.00812 | 0.68559 | 0.67663 | 0.70132 | 64.89007 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.0749 | 0.00201 | 0.07467 | 0.07253 | 0.0778 | 21.80413 |
| `long_run/processes/collect_names_from_site.py` | yes | 2.08503 | 0.04712 | 2.08258 | 2.03015 | 2.17065 | 45.29074 |
| `long_run/processes/generate_fake_data.py` | yes | 0.92717 | 0.05745 | 0.9216 | 0.84944 | 1.01262 | 66.60268 |
| `long_run/processes/maze_generator.py` | yes | 0.36464 | 0.03289 | 0.36268 | 0.32862 | 0.41551 | 21.99609 |
| `long_run/text/clean_text.py` | yes | 0.28569 | 0.00204 | 0.28495 | 0.28306 | 0.28852 | 21.90458 |
| `long_run/text/count_words.py` | yes | 0.0943 | 0.0008 | 0.09403 | 0.09339 | 0.09541 | 21.7115 |
| `math/haversine.py` | yes | 0.9396 | 0.02614 | 0.94126 | 0.90543 | 0.9884 | 21.78125 |
| `math/mandelbrot.py` | yes | 3.52718 | 0.09432 | 3.53433 | 3.4126 | 3.68553 | 35.88616 |
| `math/pow_simple.py` | yes | 0.76718 | 0.01162 | 0.76919 | 0.75245 | 0.78224 | 21.69196 |
| `math/pow_using_math.py` | yes | 1.45879 | 0.05511 | 1.43816 | 1.40365 | 1.55084 | 21.65067 |
| `modules/json/json_module.py` | yes | 0.54672 | 0.02363 | 0.5575 | 0.51442 | 0.57367 | 22.00781 |
| `modules/json/orjson_module.py` | yes | 0.30919 | 0.00791 | 0.31035 | 0.30048 | 0.32093 | 22.38728 |


### **Python 3.9**

```bash
Python 3.9.17

Linux 4b0297861900 5.15.0-78-generic unknown GNU/Linux

CPU(s):                          12
Model name:                      Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:              2
Core(s) per socket:              6
CPU max MHz:                     4100.0000
NUMA node(s):                    1
NUMA node0 CPU(s):               0-11

MemTotal:       16066528 kB
MemFree:         1292016 kB
MemAvailable:    7426312 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.52999 | 0.03554 | 1.51353 | 1.50066 | 1.60229 | 31.89174 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.5409 | 0.04514 | 1.53524 | 1.49782 | 1.63361 | 30.74777 |
| `algorithm/search/index.py` | yes | 1.52132 | 0.04486 | 1.49521 | 1.48254 | 1.59392 | 30.96261 |
| `algorithm/search/linear.py` | yes | 1.58368 | 0.06525 | 1.55767 | 1.53902 | 1.72605 | 30.61049 |
| `algorithm/twosum/twosum.py` | yes | 0.08876 | 0.00081 | 0.08864 | 0.08776 | 0.0899 | 23.47824 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.09069 | 0.00507 | 0.08821 | 0.08779 | 0.10163 | 22.71094 |
| `complex/classes/classes.py` | yes | 0.04884 | 0.00099 | 0.04857 | 0.04801 | 0.05069 | 23.78683 |
| `complex/classes/dataclasses_.py` | yes | 0.14112 | 0.00218 | 0.14033 | 0.13908 | 0.14545 | 24.04855 |
| `complex/classes/namedtuple_classes.py` | yes | 0.10732 | 0.00349 | 0.10611 | 0.10454 | 0.11469 | 23.44308 |
| `complex/classes/simplenamespace.py` | yes | 0.05287 | 0.00196 | 0.052 | 0.05121 | 0.05641 | 22.98605 |
| `complex/classes/sloted_classes.py` | yes | 0.05216 | 0.00317 | 0.05143 | 0.04892 | 0.05695 | 22.90179 |
| `complex/generators/simple.py` | yes | 0.07268 | 0.003 | 0.07382 | 0.0677 | 0.07611 | 23.98326 |
| `dummy/dummy.py` | yes | 0.03358 | 0.00144 | 0.03279 | 0.03243 | 0.03625 | 23.37165 |
| `long_run/database/postgresql.py` | yes | 0.19325 | 0.00415 | 0.19271 | 0.18788 | 0.20055 | 29.28683 |
| `long_run/database/sqlite_.py` | yes | 0.74685 | 0.00596 | 0.74705 | 0.73905 | 0.75732 | 66.93136 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.755 | 0.02583 | 0.74713 | 0.72695 | 0.80512 | 65.59487 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.08306 | 0.00519 | 0.08079 | 0.07981 | 0.09449 | 23.47935 |
| `long_run/processes/collect_names_from_site.py` | yes | 2.247 | 0.02937 | 2.24778 | 2.20957 | 2.28906 | 45.43471 |
| `long_run/processes/generate_fake_data.py` | yes | 1.02818 | 0.11211 | 0.99667 | 0.92754 | 1.26572 | 69.61217 |
| `long_run/processes/maze_generator.py` | yes | 0.39116 | 0.02851 | 0.4028 | 0.35381 | 0.42467 | 23.61607 |
| `long_run/text/clean_text.py` | yes | 0.30261 | 0.00655 | 0.30143 | 0.29524 | 0.3109 | 23.52176 |
| `long_run/text/count_words.py` | yes | 0.10417 | 0.00166 | 0.10461 | 0.10134 | 0.10622 | 23.67522 |
| `math/haversine.py` | yes | 1.12738 | 0.06222 | 1.10783 | 1.08634 | 1.26022 | 23.46652 |
| `math/mandelbrot.py` | yes | 3.01772 | 0.03416 | 3.02291 | 2.97208 | 3.06044 | 43.63393 |
| `math/pow_simple.py` | yes | 0.88054 | 0.01867 | 0.88116 | 0.86103 | 0.91757 | 23.50725 |
| `math/pow_using_math.py` | yes | 1.59969 | 0.06046 | 1.57183 | 1.5478 | 1.72002 | 23.44978 |
| `modules/json/json_module.py` | yes | 0.56462 | 0.01527 | 0.56481 | 0.5479 | 0.59287 | 23.68694 |
| `modules/json/orjson_module.py` | yes | 0.3782 | 0.01037 | 0.37767 | 0.36461 | 0.39881 | 24.07366 |


### **Python 3.10**

```bash
Python 3.10.12

Linux 135bb4be7dee 5.15.0-78-generic unknown GNU/Linux

CPU(s):                          12
Model name:                      Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:              2
Core(s) per socket:              6
CPU max MHz:                     4100.0000
NUMA node(s):                    1
NUMA node0 CPU(s):               0-11

MemTotal:       16066528 kB
MemFree:         1372992 kB
MemAvailable:    7551252 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.42023 | 0.03124 | 1.42701 | 1.36869 | 1.45266 | 33.61607 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.42864 | 0.0374 | 1.415 | 1.38669 | 1.49025 | 33.8404 |
| `algorithm/search/index.py` | yes | 1.41971 | 0.01657 | 1.42345 | 1.39805 | 1.44727 | 31.83705 |
| `algorithm/search/linear.py` | yes | 1.50093 | 0.07284 | 1.47679 | 1.44744 | 1.65269 | 32.1317 |
| `algorithm/twosum/twosum.py` | yes | 0.09183 | 0.00305 | 0.09054 | 0.08918 | 0.09818 | 23.58929 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.09176 | 0.00234 | 0.09139 | 0.08803 | 0.09556 | 23.72879 |
| `complex/classes/classes.py` | yes | 0.04816 | 0.00152 | 0.04765 | 0.04644 | 0.05097 | 25.53795 |
| `complex/classes/dataclasses_.py` | yes | 0.14756 | 0.00816 | 0.14643 | 0.13896 | 0.16409 | 26.21373 |
| `complex/classes/namedtuple_classes.py` | yes | 0.1086 | 0.00771 | 0.10657 | 0.10236 | 0.12443 | 24.09821 |
| `complex/classes/simplenamespace.py` | yes | 0.05163 | 0.00362 | 0.04956 | 0.04897 | 0.05902 | 25.61161 |
| `complex/classes/sloted_classes.py` | yes | 0.04925 | 0.00343 | 0.049 | 0.04588 | 0.05607 | 25.32143 |
| `complex/generators/simple.py` | yes | 0.0715 | 0.00297 | 0.07238 | 0.06694 | 0.07487 | 26.12165 |
| `dummy/dummy.py` | yes | 0.03482 | 0.00224 | 0.03444 | 0.0325 | 0.03864 | 23.32757 |
| `long_run/database/postgresql.py` | yes | 0.17562 | 0.00357 | 0.1745 | 0.1714 | 0.18295 | 28.34431 |
| `long_run/database/sqlite_.py` | yes | 0.7041 | 0.01069 | 0.70219 | 0.69058 | 0.72303 | 67.13225 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.76406 | 0.02301 | 0.75719 | 0.72907 | 0.80157 | 64.68304 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.08785 | 0.01193 | 0.08711 | 0.07725 | 0.11118 | 23.24609 |
| `long_run/processes/collect_names_from_site.py` | yes | 2.13051 | 0.03427 | 2.13237 | 2.0958 | 2.19766 | 45.42913 |
| `long_run/processes/generate_fake_data.py` | yes | 0.95808 | 0.0161 | 0.95443 | 0.94568 | 0.99148 | 68.57143 |
| `long_run/processes/maze_generator.py` | yes | 0.29685 | 0.02849 | 0.2922 | 0.26384 | 0.34283 | 23.8125 |
| `long_run/text/clean_text.py` | yes | 0.30544 | 0.0096 | 0.30086 | 0.29538 | 0.32249 | 23.75335 |
| `long_run/text/count_words.py` | yes | 0.10507 | 0.01116 | 0.10062 | 0.09853 | 0.12995 | 24.10435 |
| `math/haversine.py` | yes | 1.0489 | 0.05102 | 1.02721 | 1.00428 | 1.13781 | 23.40848 |
| `math/mandelbrot.py` | yes | 3.00763 | 0.05877 | 3.00062 | 2.90885 | 3.10253 | 39.4135 |
| `math/pow_simple.py` | yes | 0.7804 | 0.01098 | 0.78045 | 0.76935 | 0.79894 | 23.78404 |
| `math/pow_using_math.py` | yes | 1.5844 | 0.07123 | 1.57453 | 1.50591 | 1.71379 | 24.19085 |
| `modules/json/json_module.py` | yes | 0.50076 | 0.00874 | 0.50252 | 0.48682 | 0.5104 | 23.95926 |
| `modules/json/orjson_module.py` | yes | 0.34723 | 0.01042 | 0.34459 | 0.33544 | 0.36574 | 24.56585 |


### **Python 3.11**

```bash
Python 3.11.4

Linux bc865f15ca28 5.15.0-78-generic unknown GNU/Linux

CPU(s):                          12
Model name:                      Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:              2
Core(s) per socket:              6
CPU max MHz:                     4100.0000
NUMA node(s):                    1
NUMA node0 CPU(s):               0-11

MemTotal:       16066528 kB
MemFree:         1338560 kB
MemAvailable:    7552692 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.19427 | 0.01876 | 1.18451 | 1.17773 | 1.2214 | 35.61049 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.21232 | 0.0185 | 1.21269 | 1.18281 | 1.23777 | 36.49219 |
| `algorithm/search/index.py` | yes | 1.21697 | 0.01139 | 1.21515 | 1.20313 | 1.23487 | 35.04185 |
| `algorithm/search/linear.py` | yes | 1.26511 | 0.02226 | 1.26278 | 1.2351 | 1.29525 | 36.00781 |
| `algorithm/twosum/twosum.py` | yes | 0.08893 | 0.00685 | 0.08711 | 0.08202 | 0.10188 | 26.98661 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.0867 | 0.00438 | 0.08588 | 0.08324 | 0.09629 | 26.476 |
| `complex/classes/classes.py` | yes | 0.02575 | 0.00096 | 0.02552 | 0.02441 | 0.0272 | 28.49833 |
| `complex/classes/dataclasses_.py` | yes | 0.13382 | 0.0035 | 0.13391 | 0.12904 | 0.13988 | 27.79241 |
| `complex/classes/namedtuple_classes.py` | yes | 0.09859 | 0.00393 | 0.0972 | 0.09521 | 0.10617 | 27.13281 |
| `complex/classes/simplenamespace.py` | yes | 0.02991 | 0.0016 | 0.02916 | 0.02842 | 0.03293 | 28.44643 |
| `complex/classes/sloted_classes.py` | yes | 0.02711 | 0.00437 | 0.02469 | 0.02371 | 0.0351 | 27.77679 |
| `complex/generators/simple.py` | yes | 0.04965 | 0.00895 | 0.04634 | 0.04426 | 0.06954 | 28.42076 |
| `dummy/dummy.py` | yes | 0.01318 | 0.00069 | 0.01317 | 0.01226 | 0.01437 | 26.88728 |
| `long_run/database/postgresql.py` | yes | 0.17732 | 0.00496 | 0.17684 | 0.17044 | 0.18365 | 30.85937 |
| `long_run/database/sqlite_.py` | yes | 0.70201 | 0.00656 | 0.70141 | 0.69259 | 0.71198 | 72.41685 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.74635 | 0.01467 | 0.7406 | 0.73553 | 0.77747 | 70.65123 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.07035 | 0.00468 | 0.06915 | 0.06575 | 0.07733 | 26.78906 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.84199 | 0.02654 | 1.83253 | 1.81599 | 1.89465 | 47.59319 |
| `long_run/processes/generate_fake_data.py` | yes | 0.93505 | 0.0098 | 0.93369 | 0.92008 | 0.94921 | 72.39621 |
| `long_run/processes/maze_generator.py` | yes | 0.21394 | 0.01898 | 0.21891 | 0.17747 | 0.23484 | 26.92355 |
| `long_run/text/clean_text.py` | yes | 0.27257 | 0.00788 | 0.2699 | 0.2634 | 0.28459 | 26.97545 |
| `long_run/text/count_words.py` | yes | 0.08788 | 0.00662 | 0.0856 | 0.08233 | 0.10231 | 26.53348 |
| `math/haversine.py` | yes | 0.8981 | 0.02549 | 0.89291 | 0.87284 | 0.9476 | 26.42969 |
| `math/mandelbrot.py` | yes | 3.02417 | 0.06202 | 3.00532 | 2.94607 | 3.12749 | 40.95201 |
| `math/pow_simple.py` | yes | 0.40891 | 0.0277 | 0.40398 | 0.37459 | 0.44364 | 26.41908 |
| `math/pow_using_math.py` | yes | 1.28182 | 0.03635 | 1.28307 | 1.24687 | 1.35324 | 26.66574 |
| `modules/json/json_module.py` | yes | 0.44251 | 0.00804 | 0.44165 | 0.42789 | 0.45346 | 26.98047 |
| `modules/json/orjson_module.py` | yes | 0.29741 | 0.0092 | 0.29638 | 0.28525 | 0.3138 | 26.90458 |


### **Python 3.12**

```bash
Python 3.12.0rc1

Linux 405e066f186e 5.15.0-78-generic unknown GNU/Linux

CPU(s):                          12
Model name:                      Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:              2
Core(s) per socket:              6
CPU max MHz:                     4100.0000
NUMA node(s):                    1
NUMA node0 CPU(s):               0-11

MemTotal:       16066528 kB
MemFree:         1160948 kB
MemAvailable:    7630888 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.38969 | 0.05629 | 1.38991 | 1.33104 | 1.50273 | 34.91127 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.38459 | 0.06158 | 1.37474 | 1.33882 | 1.51555 | 35.94252 |
| `algorithm/search/index.py` | yes | 1.38865 | 0.01793 | 1.38148 | 1.37071 | 1.41308 | 34.76507 |
| `algorithm/search/linear.py` | yes | 1.43582 | 0.0209 | 1.43635 | 1.40338 | 1.46493 | 34.84542 |
| `algorithm/twosum/twosum.py` | yes | 0.104 | 0.00369 | 0.10287 | 0.09955 | 0.1095 | 27.24051 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.10192 | 0.00466 | 0.10404 | 0.09576 | 0.10832 | 27.31473 |
| `complex/classes/classes.py` | yes | 0.02664 | 0.00281 | 0.02562 | 0.02451 | 0.03279 | 27.9029 |
| `complex/classes/dataclasses_.py` | yes | 0.15316 | 0.00244 | 0.15423 | 0.15008 | 0.15604 | 28.08538 |
| `complex/classes/namedtuple_classes.py` | yes | 0.11285 | 0.00424 | 0.11104 | 0.10894 | 0.12068 | 27.99219 |
| `complex/classes/simplenamespace.py` | yes | 0.03444 | 0.00255 | 0.03381 | 0.03176 | 0.03787 | 29.06194 |
| `complex/classes/sloted_classes.py` | yes | 0.02595 | 0.00133 | 0.02546 | 0.0242 | 0.02755 | 28.00614 |
| `complex/generators/simple.py` | yes | 0.05237 | 0.00159 | 0.05139 | 0.05092 | 0.05448 | 29.47489 |
| `dummy/dummy.py` | yes | 0.01708 | 0.00165 | 0.01682 | 0.01515 | 0.01968 | 27.21038 |
| `long_run/database/postgresql.py` | yes | 0.2088 | 0.00768 | 0.20628 | 0.20044 | 0.22089 | 32.36049 |
| `long_run/database/sqlite_.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/file/load_titanic_csv_pandas.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.07849 | 0.00276 | 0.07875 | 0.07411 | 0.08203 | 27.76786 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/maze_generator.py` | yes | 0.22385 | 0.01027 | 0.22494 | 0.21058 | 0.23978 | 28.32868 |
| `long_run/text/clean_text.py` | yes | 0.28519 | 0.00679 | 0.28483 | 0.27698 | 0.29733 | 27.40904 |
| `long_run/text/count_words.py` | yes | 0.09487 | 0.00216 | 0.0953 | 0.09083 | 0.09769 | 27.29911 |
| `math/haversine.py` | yes | 1.00133 | 0.03056 | 1.0114 | 0.95616 | 1.03692 | 27.36328 |
| `math/mandelbrot.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `math/pow_simple.py` | yes | 0.35664 | 0.01205 | 0.35638 | 0.34399 | 0.37821 | 27.39062 |
| `math/pow_using_math.py` | yes | 1.33177 | 0.03574 | 1.33035 | 1.29083 | 1.38591 | 27.36049 |
| `modules/json/json_module.py` | yes | 0.45653 | 0.01867 | 0.44851 | 0.434 | 0.48586 | 28.06083 |
| `modules/json/orjson_module.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |

