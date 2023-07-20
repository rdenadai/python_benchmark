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

> Last run: Thu Jul 20 04:33:34 UTC 2023
### **Comparison**

#### How much faster 3.12 is? (Mean / Median from 3.6 to 3.11)
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 7.43% / 7.04% | 1.62% / 1.26% | -4.27% / -4.18% | 2.08% / 1.76% | -9.18% / -9.58% | -23.01% / -23.19% |
| `algorithm/search/hashmap_lookup.py` | 9.08% / 8.95% | 3.70% / 4.15% | -2.66% / -2.43% | 2.16% / 2.38% | -8.82% / -8.79% | -21.24% / -21.41% |
| `algorithm/search/index.py` | 7.31% / 7.61% | 2.07% / 1.66% | -4.13% / -3.84% | 0.48% / -0.02% | -11.42% / -11.64% | -23.39% / -23.42% |
| `algorithm/search/linear.py` | 6.80% / 7.37% | 2.73% / 4.05% | -4.35% / -3.59% | 0.81% / 1.55% | -9.92% / -9.42% | -23.02% / -22.39% |
| `algorithm/twosum/twosum.py` | -8.62% / -8.81% | -26.67% / -26.80% | -16.59% / -16.98% | -0.26% / -0.42% | -7.04% / -6.42% | -13.66% / -14.19% |
| `algorithm/twosum/twosum_naive.py` | -9.88% / -9.86% | -26.56% / -26.97% | -17.62% / -17.77% | -1.74% / -2.03% | -11.82% / -12.24% | -12.74% / -13.04% |
| `complex/classes/classes.py` | 92.49% / 93.31% | 62.80% / 63.08% | 74.66% / 75.22% | 96.21% / 96.15% | 78.71% / 77.32% | -16.95% / -16.55% |
| `complex/classes/dataclasses_.py` | -- / -- | -29.15% / -28.91% | -22.36% / -22.57% | 1.12% / 0.91% | -9.65% / -9.87% | -15.22% / -15.48% |
| `complex/classes/namedtuple_classes.py` | -5.77% / -6.19% | -19.97% / -19.98% | -15.85% / -16.38% | 0.25% / -0.08% | -9.96% / -10.13% | -14.13% / -14.14% |
| `complex/classes/simplenamespace.py` | 115.09% / 115.63% | 38.40% / 40.53% | 45.95% / 47.18% | 71.56% / 73.17% | 53.52% / 54.63% | -15.83% / -15.44% |
| `complex/classes/sloted_classes.py` | 87.52% / 88.67% | 61.24% / 61.68% | 73.72% / 76.35% | 97.95% / 97.61% | 78.22% / 78.34% | -17.35% / -17.03% |
| `complex/generators/simple.py` | 62.23% / 62.10% | 48.74% / 48.33% | 48.36% / 48.95% | 57.16% / 57.60% | 48.91% / 48.49% | -13.65% / -13.27% |
| `dummy/dummy.py` | 120.36% / 121.87% | 83.85% / 83.51% | 98.18% / 99.77% | 130.89% / 131.25% | 112.51% / 115.00% | -15.47% / -16.60% |
| `long_run/database/postgresql.py` | -21.53% / -21.50% | -27.80% / -27.79% | -19.01% / -18.86% | -6.36% / -6.27% | -16.20% / -15.94% | -16.18% / -16.34% |
| `long_run/database/sqlite_.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/file/load_titanic_csv_pandas.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/file/load_titanic_csv_python.py` | -1.55% / -2.08% | -11.04% / -11.66% | -3.38% / -3.78% | 15.80% / 15.11% | 1.38% / 1.11% | -8.10% / -8.47% |
| `long_run/processes/collect_names_from_site.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/processes/generate_fake_data.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/processes/maze_generator.py` | 80.28% / 83.07% | 78.53% / 77.72% | 64.46% / 58.46% | 72.01% / 76.46% | 33.03% / 32.97% | -13.30% / -11.26% |
| `long_run/text/clean_text.py` | 0.59% / 0.72% | -8.44% / -8.23% | 1.55% / 1.74% | 9.79% / 9.56% | 2.18% / 1.23% | -8.42% / -9.11% |
| `long_run/text/count_words.py` | 3.67% / 3.75% | -5.10% / -4.85% | 3.41% / 2.89% | 18.88% / 18.82% | 5.21% / 4.84% | -9.78% / -10.03% |
| `math/haversine.py` | 3.54% / 0.65% | 10.64% / 7.97% | -3.68% / -5.09% | 9.81% / 7.09% | -6.91% / -8.98% | -20.98% / -22.46% |
| `math/mandelbrot.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `math/pow_simple.py` | 27.44% / 27.10% | 32.39% / 31.94% | 34.17% / 34.60% | 34.21% / 33.94% | 22.35% / 22.64% | -6.45% / -6.20% |
| `math/pow_using_math.py` | 27.65% / 27.82% | 40.66% / 40.89% | 8.56% / 8.37% | 12.05% / 12.16% | 4.16% / 4.41% | -11.14% / -10.97% |
| `modules/json/json_module.py` | 12.97% / 12.94% | 15.10% / 13.89% | 6.52% / 5.56% | 10.83% / 10.65% | 2.03% / 1.13% | -8.56% / -9.20% |
| `modules/json/orjson_module.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
---

#### How much more memory 3.12 uses? (Memory diff from 3.6 to 3.11)
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 24.25% | 20.86% | 19.84% | 10.81% | 8.6% | 0.93% |
| `algorithm/search/hashmap_lookup.py` | 28.04% | 19.8% | 18.66% | 18.1% | 7.57% | 1.59% |
| `algorithm/search/index.py` | 25.13% | 20.23% | 18.89% | 14.24% | 8.89% | -1.08% |
| `algorithm/search/linear.py` | 22.65% | 18.63% | 18.17% | 14.83% | 8.77% | -2.04% |
| `algorithm/twosum/twosum.py` | 24.27% | 29.98% | 28.36% | 17.9% | 15.4% | 2.4% |
| `algorithm/twosum/twosum_naive.py` | 24.2% | 31.24% | 27.28% | 22.16% | 17.08% | 4.43% |
| `complex/classes/classes.py` | 30.4% | 34.49% | 30.31% | 20.51% | 11.12% | 0.25% |
| `complex/classes/dataclasses_.py` | -- | 30.22% | 26.58% | 15.41% | 9.85% | -1.92% |
| `complex/classes/namedtuple_classes.py` | 24.58% | 31.3% | 29.08% | 19.15% | 15.62% | 1.79% |
| `complex/classes/simplenamespace.py` | 34.76% | 41.07% | 34.5% | 29.23% | 15.55% | 3.41% |
| `complex/classes/sloted_classes.py` | 29.25% | 35.34% | 30.19% | 24.45% | 10.73% | 2.29% |
| `complex/generators/simple.py` | 31.81% | 38.47% | 32.26% | 21.84% | 12.52% | -0.08% |
| `dummy/dummy.py` | 24.11% | 28.38% | 25.65% | 15.15% | 11.41% | -0.2% |
| `long_run/database/postgresql.py` | 18.92% | 20.44% | 20.18% | 10.71% | 14.64% | 2.69% |
| `long_run/database/sqlite_.py` | -- | -- | -- | -- | -- | -- |
| `long_run/file/load_titanic_csv_pandas.py` | -- | -- | -- | -- | -- | -- |
| `long_run/file/load_titanic_csv_python.py` | 25.34% | 31.82% | 27.0% | 18.42% | 20.05% | 3.53% |
| `long_run/processes/collect_names_from_site.py` | -- | -- | -- | -- | -- | -- |
| `long_run/processes/generate_fake_data.py` | -- | -- | -- | -- | -- | -- |
| `long_run/processes/maze_generator.py` | 29.08% | 28.41% | 28.16% | 19.4% | 17.66% | 4.66% |
| `long_run/text/clean_text.py` | 24.35% | 30.77% | 28.11% | 17.96% | 15.21% | 2.95% |
| `long_run/text/count_words.py` | 23.07% | 27.34% | 24.39% | 12.93% | 11.04% | -0.24% |
| `math/haversine.py` | 25.51% | 29.97% | 26.53% | 16.93% | 15.88% | 4.02% |
| `math/mandelbrot.py` | -- | -- | -- | -- | -- | -- |
| `math/pow_simple.py` | 25.99% | 29.55% | 25.04% | 16.19% | 15.98% | 3.05% |
| `math/pow_using_math.py` | 27.79% | 31.57% | 28.79% | 17.85% | 14.18% | 3.88% |
| `modules/json/json_module.py` | 30.61% | 27.51% | 30.14% | 20.85% | 18.5% | 6.17% |
| `modules/json/orjson_module.py` | -- | -- | -- | -- | -- | -- |
---

#### **Execution**

##### **Mean [s]**
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 1.27713 | 1.20807 | 1.13802 | 1.2135 | 1.07966 | 0.91525 | 1.18876 |
| `algorithm/search/hashmap_lookup.py` | 1.2848 | 1.22133 | 1.14648 | 1.20324 | 1.0739 | 0.92763 | 1.1778 |
| `algorithm/search/index.py` | 1.30595 | 1.24223 | 1.1668 | 1.22284 | 1.07798 | 0.93233 | 1.21702 |
| `algorithm/search/linear.py` | 1.3417 | 1.29059 | 1.20161 | 1.26642 | 1.1316 | 0.9671 | 1.25627 |
| `algorithm/twosum/twosum.py` | 0.09821 | 0.07881 | 0.08965 | 0.1072 | 0.09991 | 0.0928 | 0.10748 |
| `algorithm/twosum/twosum_naive.py` | 0.09801 | 0.07987 | 0.08959 | 0.10686 | 0.0959 | 0.0949 | 0.10875 |
| `complex/classes/classes.py` | 0.0518 | 0.04381 | 0.047 | 0.0528 | 0.04809 | 0.02235 | 0.02691 |
| `complex/classes/dataclasses_.py` | -- | 0.11715 | 0.12838 | 0.16721 | 0.1494 | 0.1402 | 0.16536 |
| `complex/classes/namedtuple_classes.py` | 0.11213 | 0.09523 | 0.10014 | 0.1193 | 0.10715 | 0.10219 | 0.119 |
| `complex/classes/simplenamespace.py` | 0.07214 | 0.04642 | 0.04895 | 0.05754 | 0.05149 | 0.02823 | 0.03354 |
| `complex/classes/sloted_classes.py` | 0.05123 | 0.04405 | 0.04746 | 0.05408 | 0.04869 | 0.02258 | 0.02732 |
| `complex/generators/simple.py` | 0.07782 | 0.07135 | 0.07117 | 0.07539 | 0.07143 | 0.04142 | 0.04797 |
| `dummy/dummy.py` | 0.03874 | 0.03232 | 0.03484 | 0.04059 | 0.03736 | 0.01486 | 0.01758 |
| `long_run/database/postgresql.py` | 0.17597 | 0.1619 | 0.18163 | 0.20998 | 0.18793 | 0.18797 | 0.22425 |
| `long_run/database/sqlite_.py` | 0.6733 | 0.58248 | 0.65528 | 0.75904 | 0.67795 | 0.69879 | -- |
| `long_run/file/load_titanic_csv_pandas.py` | 0.7612 | 0.65519 | 0.71629 | 0.78969 | 0.72022 | 0.74075 | -- |
| `long_run/file/load_titanic_csv_python.py` | 0.08279 | 0.07481 | 0.08125 | 0.09738 | 0.08525 | 0.07728 | 0.08409 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 1.34685 | 1.46051 | 1.36394 | 1.25255 | -- |
| `long_run/processes/generate_fake_data.py` | 0.99163 | 0.89707 | 0.95807 | 1.05338 | 0.98424 | 0.96041 | -- |
| `long_run/processes/maze_generator.py` | 0.24372 | 0.24135 | 0.22234 | 0.23254 | 0.17984 | 0.11721 | 0.13519 |
| `long_run/text/clean_text.py` | 0.24863 | 0.22631 | 0.25099 | 0.27136 | 0.25254 | 0.22636 | 0.24716 |
| `long_run/text/count_words.py` | 0.10457 | 0.09573 | 0.10431 | 0.11991 | 0.10613 | 0.091 | 0.10087 |
| `math/haversine.py` | 0.71672 | 0.76586 | 0.66672 | 0.76014 | 0.64441 | 0.54696 | 0.69221 |
| `math/mandelbrot.py` | 4.44783 | 4.29542 | 4.34127 | 3.9563 | 3.90774 | 3.90908 | -- |
| `math/pow_simple.py` | 0.45454 | 0.47218 | 0.47855 | 0.47868 | 0.4364 | 0.33365 | 0.35667 |
| `math/pow_using_math.py` | 1.40262 | 1.5456 | 1.19287 | 1.23121 | 1.14454 | 0.97641 | 1.09882 |
| `modules/json/json_module.py` | 0.48117 | 0.49022 | 0.45371 | 0.47205 | 0.43458 | 0.38948 | 0.42592 |
| `modules/json/orjson_module.py` | 0.32131 | 0.26375 | 0.31317 | 0.36978 | 0.35034 | 0.30252 | -- |

##### **Median [s]**
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 1.27407 | 1.20534 | 1.1406 | 1.21128 | 1.07622 | 0.91422 | 1.1903 |
| `algorithm/search/hashmap_lookup.py` | 1.27879 | 1.22236 | 1.14516 | 1.20166 | 1.07049 | 0.92235 | 1.17369 |
| `algorithm/search/index.py` | 1.30885 | 1.23643 | 1.16962 | 1.21606 | 1.07468 | 0.93147 | 1.21627 |
| `algorithm/search/linear.py` | 1.34022 | 1.29881 | 1.20344 | 1.2676 | 1.13058 | 0.96873 | 1.24821 |
| `algorithm/twosum/twosum.py` | 0.09808 | 0.07873 | 0.08929 | 0.1071 | 0.10064 | 0.09229 | 0.10755 |
| `algorithm/twosum/twosum_naive.py` | 0.09833 | 0.07967 | 0.0897 | 0.10688 | 0.09574 | 0.09487 | 0.10909 |
| `complex/classes/classes.py` | 0.05173 | 0.04364 | 0.04689 | 0.05249 | 0.04745 | 0.02233 | 0.02676 |
| `complex/classes/dataclasses_.py` | -- | 0.11758 | 0.12807 | 0.16691 | 0.14908 | 0.1398 | 0.1654 |
| `complex/classes/namedtuple_classes.py` | 0.11177 | 0.09534 | 0.09962 | 0.11904 | 0.10707 | 0.10229 | 0.11914 |
| `complex/classes/simplenamespace.py` | 0.07176 | 0.04677 | 0.04898 | 0.05763 | 0.05146 | 0.02814 | 0.03328 |
| `complex/classes/sloted_classes.py` | 0.0513 | 0.04396 | 0.04795 | 0.05373 | 0.04849 | 0.02256 | 0.02719 |
| `complex/generators/simple.py` | 0.07745 | 0.07087 | 0.07117 | 0.0753 | 0.07095 | 0.04144 | 0.04778 |
| `dummy/dummy.py` | 0.03876 | 0.03206 | 0.0349 | 0.0404 | 0.03756 | 0.01457 | 0.01747 |
| `long_run/database/postgresql.py` | 0.17599 | 0.16187 | 0.1819 | 0.21012 | 0.18844 | 0.18756 | 0.22418 |
| `long_run/database/sqlite_.py` | 0.67382 | 0.58148 | 0.65603 | 0.75422 | 0.67549 | 0.69964 | -- |
| `long_run/file/load_titanic_csv_pandas.py` | 0.75972 | 0.64772 | 0.71517 | 0.79098 | 0.71971 | 0.73884 | -- |
| `long_run/file/load_titanic_csv_python.py` | 0.08266 | 0.07458 | 0.08123 | 0.09718 | 0.08536 | 0.07727 | 0.08442 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 1.34902 | 1.46087 | 1.36372 | 1.25363 | -- |
| `long_run/processes/generate_fake_data.py` | 0.98897 | 0.89715 | 0.95256 | 1.05401 | 0.9615 | 0.95839 | -- |
| `long_run/processes/maze_generator.py` | 0.24383 | 0.23671 | 0.21105 | 0.23503 | 0.1771 | 0.11819 | 0.13319 |
| `long_run/text/clean_text.py` | 0.24851 | 0.22643 | 0.25104 | 0.27033 | 0.24978 | 0.22427 | 0.24674 |
| `long_run/text/count_words.py` | 0.10476 | 0.09607 | 0.10389 | 0.11997 | 0.10586 | 0.09084 | 0.10097 |
| `math/haversine.py` | 0.70997 | 0.76162 | 0.66948 | 0.7554 | 0.64203 | 0.54695 | 0.70538 |
| `math/mandelbrot.py` | 4.44472 | 4.3317 | 4.34022 | 3.93103 | 3.9056 | 3.89498 | -- |
| `math/pow_simple.py` | 0.45229 | 0.4695 | 0.47898 | 0.47661 | 0.4364 | 0.33377 | 0.35585 |
| `math/pow_using_math.py` | 1.40292 | 1.54636 | 1.18946 | 1.23105 | 1.14598 | 0.97711 | 1.09755 |
| `modules/json/json_module.py` | 0.48212 | 0.4862 | 0.45062 | 0.47238 | 0.43171 | 0.38764 | 0.4269 |
| `modules/json/orjson_module.py` | 0.32182 | 0.26325 | 0.31462 | 0.36873 | 0.35422 | 0.30243 | -- |

#### **Memory Usage**

##### **MEM [MB]**
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 28.67132 | 29.47489 | 29.72545 | 32.149 | 32.80301 | 35.29353 | 35.62333 |
| `algorithm/search/hashmap_lookup.py` | 28.15737 | 30.09375 | 30.38337 | 30.52623 | 33.51451 | 35.48828 | 36.0519 |
| `algorithm/search/index.py` | 28.35268 | 29.50893 | 29.84263 | 31.05692 | 32.58092 | 35.86607 | 35.47879 |
| `algorithm/search/linear.py` | 28.74777 | 29.72154 | 29.83761 | 30.7048 | 32.41518 | 35.99163 | 35.25893 |
| `algorithm/twosum/twosum.py` | 22.2394 | 21.26172 | 21.52958 | 23.44085 | 23.94866 | 26.98772 | 27.63616 |
| `algorithm/twosum/twosum_naive.py` | 22.28571 | 21.0904 | 21.74609 | 22.65681 | 23.64007 | 26.50502 | 27.67857 |
| `complex/classes/classes.py` | 21.85714 | 21.19252 | 21.87277 | 23.65067 | 25.64955 | 28.43025 | 28.50223 |
| `complex/classes/dataclasses_.py` | -- | 21.25837 | 21.86942 | 23.98605 | 25.20089 | 28.22377 | 27.68304 |
| `complex/classes/namedtuple_classes.py` | 22.3298 | 21.18694 | 21.55078 | 23.34821 | 24.06138 | 27.32812 | 27.81864 |
| `complex/classes/simplenamespace.py` | 21.88225 | 20.9029 | 21.92467 | 22.81808 | 25.51897 | 28.51618 | 29.48772 |
| `complex/classes/sloted_classes.py` | 22.01451 | 21.02344 | 21.85603 | 22.86328 | 25.69531 | 27.81696 | 28.45368 |
| `complex/generators/simple.py` | 22.03906 | 20.97879 | 21.96484 | 23.84152 | 25.81808 | 29.07422 | 29.04967 |
| `dummy/dummy.py` | 21.69587 | 20.97321 | 21.43025 | 23.38337 | 24.16797 | 26.97991 | 26.92634 |
| `long_run/database/postgresql.py` | 27.35826 | 27.01339 | 27.07143 | 29.3856 | 28.37946 | 31.68192 | 32.53404 |
| `long_run/database/sqlite_.py` | 63.72154 | 66.4827 | 66.87667 | 67.2952 | 66.23382 | 72.75614 | -- |
| `long_run/file/load_titanic_csv_pandas.py` | 62.23159 | 64.81473 | 65.21484 | 65.92969 | 65.05636 | 70.59208 | -- |
| `long_run/file/load_titanic_csv_python.py` | 22.15513 | 21.06641 | 21.86551 | 23.45033 | 23.13114 | 26.82366 | 27.76953 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 45.41295 | 45.34319 | 45.12556 | 47.41908 | -- |
| `long_run/processes/generate_fake_data.py` | 64.86886 | 69.54074 | 66.45703 | 69.65234 | 68.62277 | 72.27902 | -- |
| `long_run/processes/maze_generator.py` | 21.74833 | 21.86217 | 21.90346 | 23.51116 | 23.85826 | 26.82143 | 28.07254 |
| `long_run/text/clean_text.py` | 22.28516 | 21.19029 | 21.63114 | 23.49275 | 24.05301 | 26.91741 | 27.71094 |
| `long_run/text/count_words.py` | 21.75056 | 21.02065 | 21.51953 | 23.70368 | 24.10603 | 26.83147 | 26.76786 |
| `math/haversine.py` | 21.89955 | 21.14732 | 21.72321 | 23.5067 | 23.71931 | 26.42411 | 27.48549 |
| `math/mandelbrot.py` | 36.70033 | 35.65123 | 36.07533 | 38.54911 | 39.63895 | 40.90792 | -- |
| `math/pow_simple.py` | 21.66518 | 21.07031 | 21.8298 | 23.49275 | 23.5346 | 26.48884 | 27.29576 |
| `math/pow_using_math.py` | 21.66685 | 21.0452 | 21.49944 | 23.49386 | 24.24944 | 26.65346 | 27.68862 |
| `modules/json/json_module.py` | 21.84152 | 22.37221 | 21.91964 | 23.60435 | 24.07366 | 26.86942 | 28.52623 |
| `modules/json/orjson_module.py` | 22.5971 | 22.5865 | 22.4654 | 24.08371 | 24.60658 | 27.5173 | -- |

---


### **Python 3.6**

```bash
Python 3.6.15

Linux c41c48ec88b3 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          4
Thread(s) per core:              2
Core(s) per socket:              2
NUMA node(s):                    1
Model name:                      Intel(R) Xeon(R) CPU E5-2666 v3 @ 2.90GHz
NUMA node0 CPU(s):               0-3

MemTotal:        7621152 kB
MemFree:          607052 kB
MemAvailable:    6901504 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.27713 | 0.02156 | 1.27407 | 1.25251 | 1.30198 | 28.67132 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.2848 | 0.0108 | 1.27879 | 1.27616 | 1.30225 | 28.15737 |
| `algorithm/search/index.py` | yes | 1.30595 | 0.01406 | 1.30885 | 1.28371 | 1.32217 | 28.35268 |
| `algorithm/search/linear.py` | yes | 1.3417 | 0.02777 | 1.34022 | 1.30133 | 1.38769 | 28.74777 |
| `algorithm/twosum/twosum.py` | yes | 0.09821 | 0.00101 | 0.09808 | 0.09669 | 0.09968 | 22.2394 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.09801 | 0.00086 | 0.09833 | 0.0967 | 0.09928 | 22.28571 |
| `complex/classes/classes.py` | yes | 0.0518 | 0.0006 | 0.05173 | 0.0507 | 0.05257 | 21.85714 |
| `complex/classes/dataclasses_.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `complex/classes/namedtuple_classes.py` | yes | 0.11213 | 0.00168 | 0.11177 | 0.11004 | 0.11484 | 22.3298 |
| `complex/classes/simplenamespace.py` | yes | 0.07214 | 0.00087 | 0.07176 | 0.07133 | 0.07391 | 21.88225 |
| `complex/classes/sloted_classes.py` | yes | 0.05123 | 0.00047 | 0.0513 | 0.05035 | 0.05173 | 22.01451 |
| `complex/generators/simple.py` | yes | 0.07782 | 0.00089 | 0.07745 | 0.07672 | 0.0789 | 22.03906 |
| `dummy/dummy.py` | yes | 0.03874 | 0.00023 | 0.03876 | 0.03839 | 0.03907 | 21.69587 |
| `long_run/database/postgresql.py` | yes | 0.17597 | 0.00192 | 0.17599 | 0.17302 | 0.17855 | 27.35826 |
| `long_run/database/sqlite_.py` | yes | 0.6733 | 0.00516 | 0.67382 | 0.66621 | 0.67933 | 63.72154 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.7612 | 0.00421 | 0.75972 | 0.75776 | 0.76964 | 62.23159 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.08279 | 0.0005 | 0.08266 | 0.08237 | 0.08383 | 22.15513 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | yes | 0.99163 | 0.0097 | 0.98897 | 0.98337 | 1.00868 | 64.86886 |
| `long_run/processes/maze_generator.py` | yes | 0.24372 | 0.00909 | 0.24383 | 0.22887 | 0.25943 | 21.74833 |
| `long_run/text/clean_text.py` | yes | 0.24863 | 0.00151 | 0.24851 | 0.24574 | 0.25043 | 22.28516 |
| `long_run/text/count_words.py` | yes | 0.10457 | 0.00074 | 0.10476 | 0.10342 | 0.10534 | 21.75056 |
| `math/haversine.py` | yes | 0.71672 | 0.01928 | 0.70997 | 0.70618 | 0.76019 | 21.89955 |
| `math/mandelbrot.py` | yes | 4.44783 | 0.02077 | 4.44472 | 4.42295 | 4.47602 | 36.70033 |
| `math/pow_simple.py` | yes | 0.45454 | 0.00404 | 0.45229 | 0.45144 | 0.46249 | 21.66518 |
| `math/pow_using_math.py` | yes | 1.40262 | 0.0075 | 1.40292 | 1.39223 | 1.41349 | 21.66685 |
| `modules/json/json_module.py` | yes | 0.48117 | 0.00495 | 0.48212 | 0.47467 | 0.48908 | 21.84152 |
| `modules/json/orjson_module.py` | yes | 0.32131 | 0.00314 | 0.32182 | 0.3159 | 0.32527 | 22.5971 |


### **Python 3.7**

```bash
Python 3.7.17

Linux 63921dff2e60 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          4
Model name:                      Intel(R) Xeon(R) CPU E5-2666 v3 @ 2.90GHz
Thread(s) per core:              2
Core(s) per socket:              2
NUMA node(s):                    1
NUMA node0 CPU(s):               0-3

MemTotal:        7621152 kB
MemFree:          611068 kB
MemAvailable:    6908448 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.20807 | 0.02046 | 1.20534 | 1.17806 | 1.24398 | 29.47489 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.22133 | 0.01116 | 1.22236 | 1.20856 | 1.23663 | 30.09375 |
| `algorithm/search/index.py` | yes | 1.24223 | 0.01993 | 1.23643 | 1.22399 | 1.28352 | 29.50893 |
| `algorithm/search/linear.py` | yes | 1.29059 | 0.01755 | 1.29881 | 1.26507 | 1.31229 | 29.72154 |
| `algorithm/twosum/twosum.py` | yes | 0.07881 | 0.00036 | 0.07873 | 0.07835 | 0.07943 | 21.26172 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07987 | 0.00079 | 0.07967 | 0.0792 | 0.08137 | 21.0904 |
| `complex/classes/classes.py` | yes | 0.04381 | 0.00057 | 0.04364 | 0.04342 | 0.04503 | 21.19252 |
| `complex/classes/dataclasses_.py` | yes | 0.11715 | 0.00084 | 0.11758 | 0.11585 | 0.11797 | 21.25837 |
| `complex/classes/namedtuple_classes.py` | yes | 0.09523 | 0.00073 | 0.09534 | 0.09392 | 0.09601 | 21.18694 |
| `complex/classes/simplenamespace.py` | yes | 0.04642 | 0.00157 | 0.04677 | 0.04446 | 0.0493 | 20.9029 |
| `complex/classes/sloted_classes.py` | yes | 0.04405 | 0.00067 | 0.04396 | 0.04333 | 0.04522 | 21.02344 |
| `complex/generators/simple.py` | yes | 0.07135 | 0.0017 | 0.07087 | 0.06924 | 0.07376 | 20.97879 |
| `dummy/dummy.py` | yes | 0.03232 | 0.00073 | 0.03206 | 0.03173 | 0.03376 | 20.97321 |
| `long_run/database/postgresql.py` | yes | 0.1619 | 0.00132 | 0.16187 | 0.16009 | 0.16363 | 27.01339 |
| `long_run/database/sqlite_.py` | yes | 0.58248 | 0.00445 | 0.58148 | 0.57778 | 0.59116 | 66.4827 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.65519 | 0.01598 | 0.64772 | 0.6417 | 0.67944 | 64.81473 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.07481 | 0.00093 | 0.07458 | 0.07349 | 0.07645 | 21.06641 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | yes | 0.89707 | 0.00485 | 0.89715 | 0.89108 | 0.90384 | 69.54074 |
| `long_run/processes/maze_generator.py` | yes | 0.24135 | 0.01426 | 0.23671 | 0.22136 | 0.26085 | 21.86217 |
| `long_run/text/clean_text.py` | yes | 0.22631 | 0.00116 | 0.22643 | 0.22454 | 0.22762 | 21.19029 |
| `long_run/text/count_words.py` | yes | 0.09573 | 0.00049 | 0.09607 | 0.09501 | 0.09619 | 21.02065 |
| `math/haversine.py` | yes | 0.76586 | 0.01197 | 0.76162 | 0.75019 | 0.78546 | 21.14732 |
| `math/mandelbrot.py` | yes | 4.29542 | 0.10277 | 4.3317 | 4.06281 | 4.34342 | 35.65123 |
| `math/pow_simple.py` | yes | 0.47218 | 0.00532 | 0.4695 | 0.46836 | 0.48272 | 21.07031 |
| `math/pow_using_math.py` | yes | 1.5456 | 0.02017 | 1.54636 | 1.52396 | 1.57576 | 21.0452 |
| `modules/json/json_module.py` | yes | 0.49022 | 0.01301 | 0.4862 | 0.47696 | 0.5092 | 22.37221 |
| `modules/json/orjson_module.py` | yes | 0.26375 | 0.00275 | 0.26325 | 0.26076 | 0.26817 | 22.5865 |


### **Python 3.8**

```bash
Python 3.8.17

Linux f5a5bdf10e0a 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          4
Model name:                      Intel(R) Xeon(R) CPU E5-2666 v3 @ 2.90GHz
Thread(s) per core:              2
Core(s) per socket:              2
NUMA node(s):                    1
NUMA node0 CPU(s):               0-3

MemTotal:        7621152 kB
MemFree:          608580 kB
MemAvailable:    6900080 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.13802 | 0.01197 | 1.1406 | 1.11944 | 1.15803 | 29.72545 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.14648 | 0.0128 | 1.14516 | 1.12668 | 1.1645 | 30.38337 |
| `algorithm/search/index.py` | yes | 1.1668 | 0.01155 | 1.16962 | 1.15203 | 1.18158 | 29.84263 |
| `algorithm/search/linear.py` | yes | 1.20161 | 0.01172 | 1.20344 | 1.18131 | 1.21965 | 29.83761 |
| `algorithm/twosum/twosum.py` | yes | 0.08965 | 0.00233 | 0.08929 | 0.08785 | 0.09456 | 21.52958 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.08959 | 0.00124 | 0.0897 | 0.08797 | 0.09128 | 21.74609 |
| `complex/classes/classes.py` | yes | 0.047 | 0.00048 | 0.04689 | 0.04656 | 0.04801 | 21.87277 |
| `complex/classes/dataclasses_.py` | yes | 0.12838 | 0.00074 | 0.12807 | 0.12769 | 0.12949 | 21.86942 |
| `complex/classes/namedtuple_classes.py` | yes | 0.10014 | 0.00173 | 0.09962 | 0.09843 | 0.1029 | 21.55078 |
| `complex/classes/simplenamespace.py` | yes | 0.04895 | 0.00086 | 0.04898 | 0.04747 | 0.04987 | 21.92467 |
| `complex/classes/sloted_classes.py` | yes | 0.04746 | 0.00097 | 0.04795 | 0.04633 | 0.04853 | 21.85603 |
| `complex/generators/simple.py` | yes | 0.07117 | 0.00044 | 0.07117 | 0.0706 | 0.07187 | 21.96484 |
| `dummy/dummy.py` | yes | 0.03484 | 0.00029 | 0.0349 | 0.0345 | 0.03522 | 21.43025 |
| `long_run/database/postgresql.py` | yes | 0.18163 | 0.00239 | 0.1819 | 0.1785 | 0.18588 | 27.07143 |
| `long_run/database/sqlite_.py` | yes | 0.65528 | 0.00377 | 0.65603 | 0.64954 | 0.66097 | 66.87667 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.71629 | 0.00475 | 0.71517 | 0.7107 | 0.72579 | 65.21484 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.08125 | 0.00044 | 0.08123 | 0.08081 | 0.08213 | 21.86551 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.34685 | 0.00775 | 1.34902 | 1.33363 | 1.3552 | 45.41295 |
| `long_run/processes/generate_fake_data.py` | yes | 0.95807 | 0.01161 | 0.95256 | 0.94987 | 0.98032 | 66.45703 |
| `long_run/processes/maze_generator.py` | yes | 0.22234 | 0.02377 | 0.21105 | 0.19989 | 0.26247 | 21.90346 |
| `long_run/text/clean_text.py` | yes | 0.25099 | 0.00151 | 0.25104 | 0.24917 | 0.25347 | 21.63114 |
| `long_run/text/count_words.py` | yes | 0.10431 | 0.00124 | 0.10389 | 0.10308 | 0.10609 | 21.51953 |
| `math/haversine.py` | yes | 0.66672 | 0.00808 | 0.66948 | 0.65634 | 0.67979 | 21.72321 |
| `math/mandelbrot.py` | yes | 4.34127 | 0.02779 | 4.34022 | 4.31014 | 4.38704 | 36.07533 |
| `math/pow_simple.py` | yes | 0.47855 | 0.00256 | 0.47898 | 0.47527 | 0.48292 | 21.8298 |
| `math/pow_using_math.py` | yes | 1.19287 | 0.0093 | 1.18946 | 1.18634 | 1.21274 | 21.49944 |
| `modules/json/json_module.py` | yes | 0.45371 | 0.01927 | 0.45062 | 0.43696 | 0.49453 | 21.91964 |
| `modules/json/orjson_module.py` | yes | 0.31317 | 0.00341 | 0.31462 | 0.30678 | 0.31644 | 22.4654 |


### **Python 3.9**

```bash
Python 3.9.17

Linux 058e914cb63f 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          4
Model name:                      Intel(R) Xeon(R) CPU E5-2666 v3 @ 2.90GHz
Thread(s) per core:              2
Core(s) per socket:              2
NUMA node(s):                    1
NUMA node0 CPU(s):               0-3

MemTotal:        7621152 kB
MemFree:          614984 kB
MemAvailable:    6908456 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.2135 | 0.02145 | 1.21128 | 1.1903 | 1.25501 | 32.149 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.20324 | 0.00547 | 1.20166 | 1.19864 | 1.21152 | 30.52623 |
| `algorithm/search/index.py` | yes | 1.22284 | 0.02171 | 1.21606 | 1.19513 | 1.26263 | 31.05692 |
| `algorithm/search/linear.py` | yes | 1.26642 | 0.01316 | 1.2676 | 1.24842 | 1.28499 | 30.7048 |
| `algorithm/twosum/twosum.py` | yes | 0.1072 | 0.00038 | 0.1071 | 0.10688 | 0.10792 | 23.44085 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.10686 | 0.00035 | 0.10688 | 0.10632 | 0.10732 | 22.65681 |
| `complex/classes/classes.py` | yes | 0.0528 | 0.00071 | 0.05249 | 0.05239 | 0.05437 | 23.65067 |
| `complex/classes/dataclasses_.py` | yes | 0.16721 | 0.00125 | 0.16691 | 0.16585 | 0.1693 | 23.98605 |
| `complex/classes/namedtuple_classes.py` | yes | 0.1193 | 0.00159 | 0.11904 | 0.11735 | 0.12192 | 23.34821 |
| `complex/classes/simplenamespace.py` | yes | 0.05754 | 0.00057 | 0.05763 | 0.05683 | 0.0584 | 22.81808 |
| `complex/classes/sloted_classes.py` | yes | 0.05408 | 0.00127 | 0.05373 | 0.05269 | 0.05551 | 22.86328 |
| `complex/generators/simple.py` | yes | 0.07539 | 0.00075 | 0.0753 | 0.07419 | 0.0764 | 23.84152 |
| `dummy/dummy.py` | yes | 0.04059 | 0.00055 | 0.0404 | 0.04018 | 0.0418 | 23.38337 |
| `long_run/database/postgresql.py` | yes | 0.20998 | 0.00106 | 0.21012 | 0.20846 | 0.21171 | 29.3856 |
| `long_run/database/sqlite_.py` | yes | 0.75904 | 0.02529 | 0.75422 | 0.72986 | 0.79073 | 67.2952 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.78969 | 0.00248 | 0.79098 | 0.78609 | 0.79148 | 65.92969 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.09738 | 0.00059 | 0.09718 | 0.09644 | 0.09834 | 23.45033 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.46051 | 0.01309 | 1.46087 | 1.4417 | 1.4822 | 45.34319 |
| `long_run/processes/generate_fake_data.py` | yes | 1.05338 | 0.00754 | 1.05401 | 1.04177 | 1.06204 | 69.65234 |
| `long_run/processes/maze_generator.py` | yes | 0.23254 | 0.0138 | 0.23503 | 0.21507 | 0.25264 | 23.51116 |
| `long_run/text/clean_text.py` | yes | 0.27136 | 0.00211 | 0.27033 | 0.26949 | 0.27542 | 23.49275 |
| `long_run/text/count_words.py` | yes | 0.11991 | 0.00062 | 0.11997 | 0.11918 | 0.12079 | 23.70368 |
| `math/haversine.py` | yes | 0.76014 | 0.01354 | 0.7554 | 0.74912 | 0.78435 | 23.5067 |
| `math/mandelbrot.py` | yes | 3.9563 | 0.07458 | 3.93103 | 3.88585 | 4.09464 | 38.54911 |
| `math/pow_simple.py` | yes | 0.47868 | 0.00395 | 0.47661 | 0.47597 | 0.48672 | 23.49275 |
| `math/pow_using_math.py` | yes | 1.23121 | 0.00969 | 1.23105 | 1.2193 | 1.2447 | 23.49386 |
| `modules/json/json_module.py` | yes | 0.47205 | 0.00386 | 0.47238 | 0.46563 | 0.4772 | 23.60435 |
| `modules/json/orjson_module.py` | yes | 0.36978 | 0.00557 | 0.36873 | 0.36423 | 0.38172 | 24.08371 |


### **Python 3.10**

```bash
Python 3.10.12

Linux 134d12a6dd2d 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          4
Model name:                      Intel(R) Xeon(R) CPU E5-2666 v3 @ 2.90GHz
Thread(s) per core:              2
Core(s) per socket:              2
NUMA node(s):                    1
NUMA node0 CPU(s):               0-3

MemTotal:        7621152 kB
MemFree:          601912 kB
MemAvailable:    6895992 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.07966 | 0.01333 | 1.07622 | 1.06661 | 1.09939 | 32.80301 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.0739 | 0.01054 | 1.07049 | 1.0603 | 1.09396 | 33.51451 |
| `algorithm/search/index.py` | yes | 1.07798 | 0.00507 | 1.07468 | 1.07412 | 1.08555 | 32.58092 |
| `algorithm/search/linear.py` | yes | 1.1316 | 0.00962 | 1.13058 | 1.11572 | 1.14431 | 32.41518 |
| `algorithm/twosum/twosum.py` | yes | 0.09991 | 0.00109 | 0.10064 | 0.09788 | 0.10069 | 23.94866 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.0959 | 0.00053 | 0.09574 | 0.09538 | 0.09698 | 23.64007 |
| `complex/classes/classes.py` | yes | 0.04809 | 0.00096 | 0.04745 | 0.04721 | 0.04952 | 25.64955 |
| `complex/classes/dataclasses_.py` | yes | 0.1494 | 0.00193 | 0.14908 | 0.14704 | 0.15307 | 25.20089 |
| `complex/classes/namedtuple_classes.py` | yes | 0.10715 | 0.00052 | 0.10707 | 0.10649 | 0.10787 | 24.06138 |
| `complex/classes/simplenamespace.py` | yes | 0.05149 | 0.00109 | 0.05146 | 0.04982 | 0.05281 | 25.51897 |
| `complex/classes/sloted_classes.py` | yes | 0.04869 | 0.00106 | 0.04849 | 0.04747 | 0.05049 | 25.69531 |
| `complex/generators/simple.py` | yes | 0.07143 | 0.00111 | 0.07095 | 0.06996 | 0.07298 | 25.81808 |
| `dummy/dummy.py` | yes | 0.03736 | 0.00036 | 0.03756 | 0.03689 | 0.03771 | 24.16797 |
| `long_run/database/postgresql.py` | yes | 0.18793 | 0.0016 | 0.18844 | 0.18505 | 0.1898 | 28.37946 |
| `long_run/database/sqlite_.py` | yes | 0.67795 | 0.004 | 0.67549 | 0.67435 | 0.68321 | 66.23382 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.72022 | 0.00328 | 0.71971 | 0.71663 | 0.72575 | 65.05636 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.08525 | 0.00094 | 0.08536 | 0.08342 | 0.08639 | 23.13114 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.36394 | 0.0058 | 1.36372 | 1.35756 | 1.37173 | 45.12556 |
| `long_run/processes/generate_fake_data.py` | yes | 0.98424 | 0.03621 | 0.9615 | 0.95173 | 1.03624 | 68.62277 |
| `long_run/processes/maze_generator.py` | yes | 0.17984 | 0.01033 | 0.1771 | 0.16939 | 0.19422 | 23.85826 |
| `long_run/text/clean_text.py` | yes | 0.25254 | 0.0049 | 0.24978 | 0.24725 | 0.25809 | 24.05301 |
| `long_run/text/count_words.py` | yes | 0.10613 | 0.00118 | 0.10586 | 0.10467 | 0.10846 | 24.10603 |
| `math/haversine.py` | yes | 0.64441 | 0.00462 | 0.64203 | 0.6401 | 0.65121 | 23.71931 |
| `math/mandelbrot.py` | yes | 3.90774 | 0.04005 | 3.9056 | 3.84921 | 3.95446 | 39.63895 |
| `math/pow_simple.py` | yes | 0.4364 | 0.00441 | 0.4364 | 0.42838 | 0.44211 | 23.5346 |
| `math/pow_using_math.py` | yes | 1.14454 | 0.00651 | 1.14598 | 1.13331 | 1.15196 | 24.24944 |
| `modules/json/json_module.py` | yes | 0.43458 | 0.00606 | 0.43171 | 0.43021 | 0.44694 | 24.07366 |
| `modules/json/orjson_module.py` | yes | 0.35034 | 0.01059 | 0.35422 | 0.33433 | 0.36354 | 24.60658 |


### **Python 3.11**

```bash
Python 3.11.4

Linux 2061df3a5467 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          4
Model name:                      Intel(R) Xeon(R) CPU E5-2666 v3 @ 2.90GHz
Thread(s) per core:              2
Core(s) per socket:              2
NUMA node(s):                    1
NUMA node0 CPU(s):               0-3

MemTotal:        7621152 kB
MemFree:          617740 kB
MemAvailable:    6912544 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 0.91525 | 0.00423 | 0.91422 | 0.90983 | 0.92319 | 35.29353 |
| `algorithm/search/hashmap_lookup.py` | yes | 0.92763 | 0.01581 | 0.92235 | 0.91173 | 0.95203 | 35.48828 |
| `algorithm/search/index.py` | yes | 0.93233 | 0.00718 | 0.93147 | 0.92357 | 0.94515 | 35.86607 |
| `algorithm/search/linear.py` | yes | 0.9671 | 0.00558 | 0.96873 | 0.95987 | 0.97307 | 35.99163 |
| `algorithm/twosum/twosum.py` | yes | 0.0928 | 0.00189 | 0.09229 | 0.09094 | 0.09668 | 26.98772 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.0949 | 0.00158 | 0.09487 | 0.09248 | 0.09696 | 26.50502 |
| `complex/classes/classes.py` | yes | 0.02235 | 0.00013 | 0.02233 | 0.02218 | 0.02251 | 28.43025 |
| `complex/classes/dataclasses_.py` | yes | 0.1402 | 0.00115 | 0.1398 | 0.13895 | 0.14201 | 28.22377 |
| `complex/classes/namedtuple_classes.py` | yes | 0.10219 | 0.00138 | 0.10229 | 0.10074 | 0.10468 | 27.32812 |
| `complex/classes/simplenamespace.py` | yes | 0.02823 | 0.00061 | 0.02814 | 0.02779 | 0.02958 | 28.51618 |
| `complex/classes/sloted_classes.py` | yes | 0.02258 | 0.00021 | 0.02256 | 0.02231 | 0.02293 | 27.81696 |
| `complex/generators/simple.py` | yes | 0.04142 | 0.00035 | 0.04144 | 0.0408 | 0.04185 | 29.07422 |
| `dummy/dummy.py` | yes | 0.01486 | 0.00064 | 0.01457 | 0.01453 | 0.0163 | 26.97991 |
| `long_run/database/postgresql.py` | yes | 0.18797 | 0.00099 | 0.18756 | 0.18717 | 0.18985 | 31.68192 |
| `long_run/database/sqlite_.py` | yes | 0.69879 | 0.00291 | 0.69964 | 0.69313 | 0.7022 | 72.75614 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.74075 | 0.00571 | 0.73884 | 0.73479 | 0.74854 | 70.59208 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.07728 | 0.00088 | 0.07727 | 0.07603 | 0.07871 | 26.82366 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.25255 | 0.00551 | 1.25363 | 1.24525 | 1.25908 | 47.41908 |
| `long_run/processes/generate_fake_data.py` | yes | 0.96041 | 0.00674 | 0.95839 | 0.9533 | 0.96906 | 72.27902 |
| `long_run/processes/maze_generator.py` | yes | 0.11721 | 0.0067 | 0.11819 | 0.1071 | 0.12366 | 26.82143 |
| `long_run/text/clean_text.py` | yes | 0.22636 | 0.00486 | 0.22427 | 0.22199 | 0.23415 | 26.91741 |
| `long_run/text/count_words.py` | yes | 0.091 | 0.00082 | 0.09084 | 0.08967 | 0.09202 | 26.83147 |
| `math/haversine.py` | yes | 0.54696 | 0.00293 | 0.54695 | 0.54348 | 0.55038 | 26.42411 |
| `math/mandelbrot.py` | yes | 3.90908 | 0.06111 | 3.89498 | 3.83415 | 3.99161 | 40.90792 |
| `math/pow_simple.py` | yes | 0.33365 | 0.00509 | 0.33377 | 0.32695 | 0.34363 | 26.48884 |
| `math/pow_using_math.py` | yes | 0.97641 | 0.0066 | 0.97711 | 0.96405 | 0.98501 | 26.65346 |
| `modules/json/json_module.py` | yes | 0.38948 | 0.01231 | 0.38764 | 0.37558 | 0.41071 | 26.86942 |
| `modules/json/orjson_module.py` | yes | 0.30252 | 0.00179 | 0.30243 | 0.3003 | 0.30474 | 27.5173 |


### **Python 3.12**

```bash
Python 3.12.0b4

Linux e21070b4cad5 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          4
Model name:                      Intel(R) Xeon(R) CPU E5-2666 v3 @ 2.90GHz
Thread(s) per core:              2
Core(s) per socket:              2
NUMA node(s):                    1
NUMA node0 CPU(s):               0-3

MemTotal:        7621152 kB
MemFree:          602788 kB
MemAvailable:    6897028 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.18876 | 0.01352 | 1.1903 | 1.17282 | 1.21409 | 35.62333 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.1778 | 0.01378 | 1.17369 | 1.16593 | 1.20442 | 36.0519 |
| `algorithm/search/index.py` | yes | 1.21702 | 0.01214 | 1.21627 | 1.19822 | 1.23386 | 35.47879 |
| `algorithm/search/linear.py` | yes | 1.25627 | 0.01766 | 1.24821 | 1.23562 | 1.27754 | 35.25893 |
| `algorithm/twosum/twosum.py` | yes | 0.10748 | 0.00039 | 0.10755 | 0.10702 | 0.10799 | 27.63616 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.10875 | 0.00136 | 0.10909 | 0.10686 | 0.11051 | 27.67857 |
| `complex/classes/classes.py` | yes | 0.02691 | 0.00073 | 0.02676 | 0.02626 | 0.02846 | 28.50223 |
| `complex/classes/dataclasses_.py` | yes | 0.16536 | 0.00047 | 0.1654 | 0.16455 | 0.16591 | 27.68304 |
| `complex/classes/namedtuple_classes.py` | yes | 0.119 | 0.00121 | 0.11914 | 0.11708 | 0.12056 | 27.81864 |
| `complex/classes/simplenamespace.py` | yes | 0.03354 | 0.00076 | 0.03328 | 0.03286 | 0.03474 | 29.48772 |
| `complex/classes/sloted_classes.py` | yes | 0.02732 | 0.00137 | 0.02719 | 0.02596 | 0.0302 | 28.45368 |
| `complex/generators/simple.py` | yes | 0.04797 | 0.00042 | 0.04778 | 0.04755 | 0.04863 | 29.04967 |
| `dummy/dummy.py` | yes | 0.01758 | 0.00031 | 0.01747 | 0.0173 | 0.01801 | 26.92634 |
| `long_run/database/postgresql.py` | yes | 0.22425 | 0.00129 | 0.22418 | 0.22267 | 0.22598 | 32.53404 |
| `long_run/database/sqlite_.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/file/load_titanic_csv_pandas.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.08409 | 0.0011 | 0.08442 | 0.08263 | 0.08557 | 27.76953 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/maze_generator.py` | yes | 0.13519 | 0.01135 | 0.13319 | 0.12047 | 0.15588 | 28.07254 |
| `long_run/text/clean_text.py` | yes | 0.24716 | 0.00206 | 0.24674 | 0.24459 | 0.25036 | 27.71094 |
| `long_run/text/count_words.py` | yes | 0.10087 | 0.00115 | 0.10097 | 0.099 | 0.10202 | 26.76786 |
| `math/haversine.py` | yes | 0.69221 | 0.04756 | 0.70538 | 0.64129 | 0.74801 | 27.48549 |
| `math/mandelbrot.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `math/pow_simple.py` | yes | 0.35667 | 0.00349 | 0.35585 | 0.35252 | 0.36197 | 27.29576 |
| `math/pow_using_math.py` | yes | 1.09882 | 0.02748 | 1.09755 | 1.0716 | 1.14297 | 27.68862 |
| `modules/json/json_module.py` | yes | 0.42592 | 0.00563 | 0.4269 | 0.41715 | 0.43309 | 28.52623 |
| `modules/json/orjson_module.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |

