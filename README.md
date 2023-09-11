# Python Benchmark

This is a simple repo to validate and test any (almost any) python program againts all python 3 versions.

- Python 3.6.15
- Python 3.7.17
- Python 3.8.17
- Python 3.9.17
- Python 3.10.12
- Python 3.11.4
- Python 3.12.0rc2

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

> Last run: Mon Sep 11 08:16:19 PM -03 2023

### **Comparison**

#### How much faster 3.12 is? (Mean / Median from 3.6 to 3.11)

| Command                                         |               3.6 |               3.7 |               3.8 |               3.9 |              3.10 |              3.11 |
| :---------------------------------------------- | ----------------: | ----------------: | ----------------: | ----------------: | ----------------: | ----------------: |
| `algorithm/search/bin.py`                       |   23.67% / 24.33% |   21.08% / 21.49% |   18.25% / 18.86% |   20.21% / 19.63% |     3.44% / 4.09% | -12.14% / -11.73% |
| `algorithm/search/hashmap_lookup.py`            |   28.51% / 27.88% |   24.28% / 24.61% |   18.87% / 19.06% |   21.21% / 22.15% |     7.17% / 7.86% |   -9.82% / -9.98% |
| `algorithm/search/index.py`                     |   25.80% / 24.26% |   22.31% / 21.85% |   19.04% / 18.71% |   19.57% / 19.44% |     6.38% / 6.04% |  -9.96% / -10.53% |
| `algorithm/search/linear.py`                    |   24.41% / 24.87% |   21.35% / 20.84% |   17.05% / 16.80% |   20.36% / 18.74% |     3.24% / 2.97% | -11.62% / -11.62% |
| `algorithm/twosum/twosum.py`                    |    0.19% / -1.00% | -18.48% / -18.51% | -14.19% / -14.30% |   -0.70% / -1.00% |   -8.89% / -9.18% | -13.79% / -13.89% |
| `algorithm/twosum/twosum_naive.py`              |    0.48% / -0.65% | -18.88% / -18.89% | -14.14% / -14.33% |    -0.14% / 0.08% |   -8.30% / -8.27% | -13.13% / -13.15% |
| `complex/classes/classes.py`                    | 108.48% / 115.55% |   79.57% / 86.69% |   88.34% / 92.23% | 102.80% / 109.44% |   84.48% / 91.04% |   -6.91% / -4.04% |
| `complex/classes/dataclasses_.py`               |           -- / -- | -19.74% / -19.71% | -17.56% / -17.47% |     2.74% / 2.60% |   -6.43% / -6.17% | -13.52% / -13.40% |
| `complex/classes/namedtuple_classes.py`         |     1.70% / 2.17% | -14.88% / -14.38% | -12.32% / -11.82% |     0.06% / 0.71% |   -7.36% / -6.83% | -13.74% / -13.72% |
| `complex/classes/simplenamespace.py`            | 121.38% / 121.09% |   47.42% / 43.53% |   49.17% / 49.46% |   69.64% / 69.51% |   54.47% / 53.61% |   -8.98% / -9.27% |
| `complex/classes/sloted_classes.py`             | 108.10% / 111.88% |   78.78% / 82.66% |   86.54% / 90.02% | 102.45% / 107.06% |   83.80% / 87.61% |   -7.43% / -5.90% |
| `complex/generators/simple.py`                  |   49.79% / 49.22% |   40.01% / 39.44% |   38.40% / 38.34% |   44.50% / 44.01% |   35.22% / 35.31% | -10.18% / -10.57% |
| `dummy/dummy.py`                                |   73.94% / 78.64% |   39.34% / 44.30% |   47.32% / 51.88% |   63.85% / 68.57% |   62.36% / 67.57% | -17.61% / -15.42% |
| `long_run/database/postgresql.py`               | -12.43% / -12.50% | -19.58% / -19.61% | -14.59% / -15.38% |   -5.34% / -5.45% | -11.69% / -11.86% | -13.77% / -14.35% |
| `long_run/database/sqlite_.py`                  |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `long_run/file/load_titanic_csv_pandas.py`      |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `long_run/file/load_titanic_csv_python.py`      |   10.24% / 10.29% |     0.17% / 0.44% |     1.48% / 1.75% |   16.05% / 16.04% |     3.52% / 3.41% | -10.72% / -11.43% |
| `long_run/processes/collect_names_from_site.py` |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `long_run/processes/generate_fake_data.py`      |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `long_run/processes/maze_generator.py`          |   62.84% / 63.05% |   72.62% / 70.02% |   60.86% / 63.56% |   66.34% / 73.83% |   56.29% / 55.49% |     0.49% / 3.54% |
| `long_run/text/clean_text.py`                   |     3.96% / 4.16% |     4.72% / 3.55% |     8.21% / 8.49% |   13.18% / 13.54% |     7.41% / 6.83% |   -6.52% / -6.62% |
| `long_run/text/count_words.py`                  |   11.43% / 11.76% |     5.04% / 3.65% |     6.17% / 6.64% |   18.53% / 19.04% |     8.30% / 8.83% |   -7.17% / -8.81% |
| `math/haversine.py`                             |   -2.26% / -2.00% |     8.27% / 8.12% |     2.59% / 2.54% |   13.83% / 13.53% |     7.42% / 4.61% |   -8.49% / -8.50% |
| `math/mandelbrot.py`                            |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `math/pow_simple.py`                            | 103.75% / 107.58% | 140.81% / 143.48% | 138.14% / 142.57% | 142.71% / 147.06% | 128.82% / 132.89% |    9.48% / 11.53% |
| `math/pow_using_math.py`                        |   24.06% / 24.41% |   43.19% / 42.82% |   15.89% / 15.32% |   18.00% / 17.88% |   19.30% / 18.07% |   -1.96% / -1.87% |
| `modules/json/json_module.py`                   |   24.50% / 25.27% |   24.77% / 25.85% |   19.63% / 20.64% |   24.33% / 23.95% |     8.19% / 9.03% |   -1.72% / -0.42% |
| `modules/json/orjson_module.py`                 |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `programming_game_benchmark/nbody.py`           |   21.87% / 21.23% |   46.27% / 45.56% |   49.88% / 49.95% |   54.67% / 53.45% |   46.70% / 45.21% |   -2.58% / -3.99% |
| `programming_game_benchmark/spectral_norm.py`   |   -7.12% / -7.87% |   16.33% / 15.69% |     7.07% / 7.15% |   12.15% / 11.96% |   -0.87% / -0.87% | -15.14% / -15.03% |

---

#### How much more memory 3.12 uses? (Memory diff from 3.6 to 3.11)

| Command                                         |    3.6 |    3.7 |    3.8 |    3.9 |   3.10 |   3.11 |
| :---------------------------------------------- | -----: | -----: | -----: | -----: | -----: | -----: |
| `algorithm/search/bin.py`                       |  21.3% | 13.86% | 18.44% |  9.82% |  8.31% | -0.33% |
| `algorithm/search/hashmap_lookup.py`            | 27.42% |  18.4% | 19.92% | 19.23% |   6.5% |  0.81% |
| `algorithm/search/index.py`                     | 23.09% | 17.17% | 19.22% |  15.3% |  9.62% | -0.72% |
| `algorithm/search/linear.py`                    | 22.84% | 19.09% | 19.24% | 15.47% |   9.5% |  -0.8% |
| `algorithm/twosum/twosum.py`                    | 23.31% | 29.72% | 26.15% | 16.86% | 15.98% |  1.97% |
| `algorithm/twosum/twosum_naive.py`              |  20.2% |  27.8% | 22.63% | 18.55% | 13.13% |   1.5% |
| `complex/classes/classes.py`                    | 27.95% | 30.46% | 29.03% | 19.09% | 10.92% |  -1.2% |
| `complex/classes/dataclasses_.py`               |     -- | 32.64% | 28.44% | 17.14% |  7.55% |  0.74% |
| `complex/classes/namedtuple_classes.py`         | 24.89% | 30.73% | 27.45% | 18.98% | 15.76% |   2.2% |
| `complex/classes/simplenamespace.py`            | 33.57% | 39.02% | 31.34% | 27.01% |  9.68% |  2.89% |
| `complex/classes/sloted_classes.py`             |  25.5% | 29.96% | 25.43% | 20.09% |  6.58% |  -0.1% |
| `complex/generators/simple.py`                  |  31.1% |  37.1% | 34.39% | 23.35% | 14.44% |  4.46% |
| `dummy/dummy.py`                                | 27.53% | 31.37% | 26.85% |  18.4% |  17.4% |   2.7% |
| `long_run/database/postgresql.py`               | 21.28% | 20.29% | 18.07% | 10.85% | 14.72% |  4.93% |
| `long_run/database/sqlite_.py`                  |     -- |     -- |     -- |     -- |     -- |     -- |
| `long_run/file/load_titanic_csv_pandas.py`      |     -- |     -- |     -- |     -- |     -- |     -- |
| `long_run/file/load_titanic_csv_python.py`      | 24.81% | 29.86% | 25.64% | 16.92% | 17.52% |   2.5% |
| `long_run/processes/collect_names_from_site.py` |     -- |     -- |     -- |     -- |     -- |     -- |
| `long_run/processes/generate_fake_data.py`      |     -- |     -- |     -- |     -- |     -- |     -- |
| `long_run/processes/maze_generator.py`          | 29.92% | 28.68% | 27.98% | 19.47% | 18.54% |  4.81% |
| `long_run/text/clean_text.py`                   | 22.95% | 28.87% | 26.81% | 16.96% | 15.42% |  1.97% |
| `long_run/text/count_words.py`                  | 26.46% | 30.13% | 25.88% | 15.49% | 13.39% |  3.28% |
| `math/haversine.py`                             | 26.47% |  30.7% | 25.62% |  17.4% |  16.9% |  4.55% |
| `math/mandelbrot.py`                            |     -- |     -- |     -- |     -- |     -- |     -- |
| `math/pow_simple.py`                            | 25.91% |  30.9% | 25.12% | 16.89% | 15.71% |  3.92% |
| `math/pow_using_math.py`                        | 27.79% |  31.3% | 27.78% | 17.71% | 14.32% |  3.83% |
| `modules/json/json_module.py`                   | 28.79% |  26.7% | 27.55% | 19.32% | 17.51% |  4.86% |
| `modules/json/orjson_module.py`                 |     -- |     -- |     -- |     -- |     -- |     -- |
| `programming_game_benchmark/nbody.py`           | 26.17% | 30.77% | 26.89% |  21.3% | 14.76% |  3.67% |
| `programming_game_benchmark/spectral_norm.py`   | 27.33% | 24.35% | 25.18% | 18.57% | 20.33% |  5.12% |

---

#### **Execution**

##### **Mean [s]**

| Command                                         |     3.6 |     3.7 |     3.8 |     3.9 |    3.10 |    3.11 |    3.12 |
| :---------------------------------------------- | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| `algorithm/search/bin.py`                       | 1.48272 |  1.4517 | 1.41776 | 1.44129 | 1.24025 | 1.05342 | 1.19897 |
| `algorithm/search/hashmap_lookup.py`            |   1.529 | 1.47857 | 1.41426 | 1.44211 | 1.27511 | 1.07296 | 1.18975 |
| `algorithm/search/index.py`                     | 1.50153 | 1.45982 | 1.42079 | 1.42715 | 1.26973 | 1.07475 | 1.19357 |
| `algorithm/search/linear.py`                    | 1.56511 | 1.52673 |  1.4726 | 1.51419 | 1.29885 | 1.11193 | 1.25807 |
| `algorithm/twosum/twosum.py`                    | 0.08776 |  0.0714 | 0.07516 | 0.08698 |  0.0798 | 0.07551 | 0.08759 |
| `algorithm/twosum/twosum_naive.py`              | 0.08776 | 0.07085 | 0.07499 | 0.08722 | 0.08009 | 0.07587 | 0.08734 |
| `complex/classes/classes.py`                    | 0.04918 | 0.04236 | 0.04443 | 0.04784 | 0.04352 | 0.02196 | 0.02359 |
| `complex/classes/dataclasses_.py`               |      -- |  0.1085 | 0.11144 | 0.13889 | 0.12649 |  0.1169 | 0.13518 |
| `complex/classes/namedtuple_classes.py`         | 0.10169 | 0.08511 | 0.08767 | 0.10005 | 0.09263 | 0.08625 | 0.09999 |
| `complex/classes/simplenamespace.py`            | 0.06555 | 0.04365 | 0.04417 | 0.05023 | 0.04574 | 0.02695 | 0.02961 |
| `complex/classes/sloted_classes.py`             | 0.04932 | 0.04237 | 0.04421 | 0.04798 | 0.04356 | 0.02194 |  0.0237 |
| `complex/generators/simple.py`                  | 0.06971 | 0.06516 | 0.06441 | 0.06725 | 0.06293 |  0.0418 | 0.04654 |
| `dummy/dummy.py`                                | 0.03378 | 0.02706 | 0.02861 | 0.03182 | 0.03153 |   0.016 | 0.01942 |
| `long_run/database/postgresql.py`               | 0.15722 | 0.14438 | 0.15334 | 0.16995 | 0.15855 | 0.15482 | 0.17954 |
| `long_run/database/sqlite_.py`                  | 0.62778 | 0.55136 | 0.61451 | 0.66534 | 0.61578 | 0.61768 |      -- |
| `long_run/file/load_titanic_csv_pandas.py`      | 0.70436 | 0.60201 | 0.65586 | 0.70857 | 0.66839 | 0.65968 |      -- |
| `long_run/file/load_titanic_csv_python.py`      | 0.07578 | 0.06886 | 0.06976 | 0.07977 | 0.07116 | 0.06137 | 0.06874 |
| `long_run/processes/collect_names_from_site.py` |      -- |      -- | 2.41284 |  2.5156 | 2.48665 | 1.99313 |      -- |
| `long_run/processes/generate_fake_data.py`      | 0.87106 | 0.79887 | 0.83007 | 0.90604 | 0.84173 | 0.82162 |      -- |
| `long_run/processes/maze_generator.py`          | 0.31667 |  0.3357 | 0.31282 | 0.32348 | 0.30394 | 0.19542 | 0.19447 |
| `long_run/text/clean_text.py`                   | 0.26755 | 0.26952 |  0.2785 | 0.29128 | 0.27642 | 0.24058 | 0.25736 |
| `long_run/text/count_words.py`                  | 0.09439 | 0.08898 | 0.08994 | 0.10041 | 0.09174 | 0.07864 | 0.08471 |
| `math/haversine.py`                             | 0.86261 | 0.95559 | 0.90544 | 1.00468 | 0.94812 |  0.8077 | 0.88259 |
| `math/mandelbrot.py`                            | 3.15227 | 3.04288 | 3.03787 |  2.6179 | 2.61357 | 2.59169 |      -- |
| `math/pow_simple.py`                            | 0.64606 | 0.76355 | 0.75509 | 0.76957 | 0.72555 | 0.34713 | 0.31708 |
| `math/pow_using_math.py`                        | 1.48338 | 1.71215 | 1.38568 | 1.41092 | 1.42649 | 1.17229 | 1.19568 |
| `modules/json/json_module.py`                   | 0.50897 | 0.51007 | 0.48908 | 0.50828 | 0.44232 | 0.40178 | 0.40882 |
| `modules/json/orjson_module.py`                 | 0.30687 | 0.26262 | 0.29605 | 0.33215 | 0.30102 | 0.26451 |      -- |
| `programming_game_benchmark/nbody.py`           | 0.43473 | 0.52176 | 0.53462 | 0.55171 | 0.52331 | 0.34749 | 0.35671 |
| `programming_game_benchmark/spectral_norm.py`   | 0.58673 | 0.73483 | 0.67632 | 0.70842 | 0.62619 | 0.53606 | 0.63169 |

##### **Median [s]**

| Command                                         |     3.6 |     3.7 |     3.8 |     3.9 |    3.10 |    3.11 |    3.12 |
| :---------------------------------------------- | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| `algorithm/search/bin.py`                       | 1.48355 | 1.44968 | 1.41827 | 1.42749 | 1.24201 | 1.05323 | 1.19322 |
| `algorithm/search/hashmap_lookup.py`            | 1.51079 | 1.47215 | 1.40659 | 1.44311 | 1.27433 | 1.06349 | 1.18144 |
| `algorithm/search/index.py`                     | 1.48424 | 1.45544 | 1.41792 | 1.42666 | 1.26659 | 1.06873 | 1.19448 |
| `algorithm/search/linear.py`                    | 1.57024 | 1.51951 | 1.46875 | 1.49316 | 1.29476 | 1.11135 | 1.25746 |
| `algorithm/twosum/twosum.py`                    |  0.0868 | 0.07145 | 0.07514 |  0.0868 | 0.07963 |  0.0755 | 0.08768 |
| `algorithm/twosum/twosum_naive.py`              | 0.08673 | 0.07081 | 0.07479 | 0.08737 | 0.08008 | 0.07582 |  0.0873 |
| `complex/classes/classes.py`                    | 0.04908 | 0.04251 | 0.04377 | 0.04769 |  0.0435 | 0.02185 | 0.02277 |
| `complex/classes/dataclasses_.py`               |      -- |  0.1084 | 0.11143 | 0.13852 | 0.12668 | 0.11692 | 0.13501 |
| `complex/classes/namedtuple_classes.py`         | 0.10155 |  0.0851 | 0.08764 |  0.1001 |  0.0926 | 0.08575 | 0.09939 |
| `complex/classes/simplenamespace.py`            | 0.06562 |  0.0426 | 0.04436 | 0.05031 | 0.04559 | 0.02693 | 0.02968 |
| `complex/classes/sloted_classes.py`             | 0.04924 | 0.04245 | 0.04416 | 0.04812 |  0.0436 | 0.02187 | 0.02324 |
| `complex/generators/simple.py`                  | 0.06943 | 0.06488 | 0.06437 | 0.06701 | 0.06296 | 0.04161 | 0.04653 |
| `dummy/dummy.py`                                | 0.03371 | 0.02723 | 0.02866 | 0.03181 | 0.03162 | 0.01596 | 0.01887 |
| `long_run/database/postgresql.py`               | 0.15718 | 0.14441 |   0.152 | 0.16984 | 0.15832 | 0.15386 | 0.17963 |
| `long_run/database/sqlite_.py`                  | 0.62628 | 0.54995 | 0.61511 |   0.658 | 0.61474 | 0.61573 |      -- |
| `long_run/file/load_titanic_csv_pandas.py`      | 0.69888 | 0.59919 | 0.65707 | 0.70634 | 0.66906 | 0.65932 |      -- |
| `long_run/file/load_titanic_csv_python.py`      | 0.07576 | 0.06899 | 0.06989 | 0.07971 | 0.07103 | 0.06084 | 0.06869 |
| `long_run/processes/collect_names_from_site.py` |      -- |      -- | 2.36489 | 2.53206 | 2.47036 | 1.98294 |      -- |
| `long_run/processes/generate_fake_data.py`      | 0.86689 | 0.79984 | 0.82504 | 0.89676 | 0.84381 | 0.82105 |      -- |
| `long_run/processes/maze_generator.py`          | 0.31194 | 0.32526 | 0.31291 | 0.33255 | 0.29747 | 0.19808 | 0.19131 |
| `long_run/text/clean_text.py`                   | 0.26741 | 0.26585 | 0.27853 | 0.29149 | 0.27427 | 0.23973 | 0.25673 |
| `long_run/text/count_words.py`                  |  0.0943 | 0.08746 | 0.08998 | 0.10045 | 0.09183 | 0.07695 | 0.08438 |
| `math/haversine.py`                             | 0.85989 | 0.94871 | 0.89971 | 0.99614 | 0.91792 | 0.80286 | 0.87746 |
| `math/mandelbrot.py`                            | 3.16877 | 3.05285 | 3.03129 | 2.61669 | 2.58904 | 2.57193 |      -- |
| `math/pow_simple.py`                            | 0.64612 | 0.75785 | 0.75502 | 0.76899 |  0.7249 | 0.34714 | 0.31126 |
| `math/pow_using_math.py`                        | 1.48449 |  1.7042 |   1.376 | 1.40655 |  1.4088 | 1.17095 | 1.19324 |
| `modules/json/json_module.py`                   | 0.50691 | 0.50928 | 0.48818 | 0.50158 |  0.4412 | 0.40296 | 0.40467 |
| `modules/json/orjson_module.py`                 | 0.30674 | 0.26168 |  0.2964 | 0.33211 | 0.30156 | 0.26573 |      -- |
| `programming_game_benchmark/nbody.py`           | 0.43396 | 0.52107 | 0.53678 | 0.54932 |  0.5198 | 0.34369 | 0.35797 |
| `programming_game_benchmark/spectral_norm.py`   | 0.58208 | 0.73092 | 0.67693 | 0.70732 | 0.62628 | 0.53683 | 0.63177 |

#### **Memory Usage**

##### **MEM [MB]**

| Command                                         |      3.6 |      3.7 |      3.8 |      3.9 |     3.10 |     3.11 |     3.12 |
| :---------------------------------------------- | -------: | -------: | -------: | -------: | -------: | -------: | -------: |
| `algorithm/search/bin.py`                       | 29.10435 |  31.0067 | 29.80804 | 32.14676 | 32.59654 |  35.4202 | 35.30413 |
| `algorithm/search/hashmap_lookup.py`            | 28.53013 | 30.70257 | 30.31473 | 30.48884 | 34.13504 | 36.06194 | 36.35268 |
| `algorithm/search/index.py`                     | 28.93304 | 30.39397 | 29.87221 | 30.88672 | 32.48716 | 35.87333 | 35.61328 |
| `algorithm/search/linear.py`                    | 29.07924 | 29.99442 | 29.95703 | 30.93583 | 32.62221 | 36.00725 | 35.72042 |
| `algorithm/twosum/twosum.py`                    | 22.27455 | 21.17355 | 21.77344 | 23.50446 | 23.68248 | 26.93638 | 27.46652 |
| `algorithm/twosum/twosum_naive.py`              | 22.38337 | 21.05246 | 21.93862 | 22.69475 | 23.78125 | 26.50558 | 26.90402 |
| `complex/classes/classes.py`                    | 22.02009 | 21.59654 | 21.83594 | 23.65848 | 25.40179 |  28.5173 | 28.17467 |
| `complex/classes/dataclasses_.py`               |       -- | 21.14955 | 21.84096 | 23.94754 | 26.08259 | 27.84766 | 28.05301 |
| `complex/classes/namedtuple_classes.py`         | 22.37221 | 21.37333 | 21.92243 |  23.4827 | 24.13672 | 27.33817 | 27.94029 |
| `complex/classes/simplenamespace.py`            | 21.80246 | 20.94754 | 22.17188 | 22.92746 | 26.55078 | 28.30413 | 29.12109 |
| `complex/classes/sloted_classes.py`             | 22.02567 | 21.26897 | 22.03627 | 23.01786 | 25.93415 | 27.66853 | 27.64118 |
| `complex/generators/simple.py`                  | 22.52288 | 21.53683 |  21.9721 | 23.93806 | 25.80301 | 28.26618 |  29.5279 |
| `dummy/dummy.py`                                | 21.71484 | 21.07924 | 21.83147 | 23.38839 | 23.58817 | 26.96317 | 27.69252 |
| `long_run/database/postgresql.py`               | 26.75949 | 26.97935 | 27.48772 |  29.2779 | 28.29074 | 30.93025 | 32.45424 |
| `long_run/database/sqlite_.py`                  | 63.60826 | 66.50502 | 66.81696 |  67.6981 | 67.48382 |  72.4654 |       -- |
| `long_run/file/load_titanic_csv_pandas.py`      | 62.37109 | 64.85658 | 65.02232 | 65.94531 | 65.15011 | 70.72042 |       -- |
| `long_run/file/load_titanic_csv_python.py`      | 22.00223 | 21.14621 | 21.85658 | 23.48549 | 23.36719 | 26.79129 | 27.46038 |
| `long_run/processes/collect_names_from_site.py` |       -- |       -- | 45.61775 | 45.85826 | 45.77455 | 47.67466 |       -- |
| `long_run/processes/generate_fake_data.py`      | 64.77567 | 69.93583 | 66.73717 | 69.76897 | 68.92634 | 72.37556 |       -- |
| `long_run/processes/maze_generator.py`          | 21.73717 | 21.94643 | 22.06696 | 23.64007 | 23.82478 | 26.94531 | 28.24163 |
| `long_run/text/clean_text.py`                   |  22.3471 | 21.32087 | 21.66685 | 23.49107 |  23.8058 | 26.94531 |   27.476 |
| `long_run/text/count_words.py`                  | 21.65681 | 21.04632 |  21.7567 | 23.71261 |  24.1529 | 26.51618 | 27.38672 |
| `math/haversine.py`                             | 21.80859 | 21.10379 | 21.95592 |  23.4933 | 23.59375 |  26.3817 | 27.58203 |
| `math/mandelbrot.py`                            | 36.35603 | 35.81752 | 36.21987 | 43.91741 | 40.75391 | 40.91071 |       -- |
| `math/pow_simple.py`                            | 21.82645 | 20.99498 | 21.96484 | 23.51116 |    23.75 | 26.44643 | 27.48214 |
| `math/pow_using_math.py`                        | 21.65848 | 21.07924 | 21.66071 | 23.51395 |  24.2115 | 26.65737 | 27.67746 |
| `modules/json/json_module.py`                   |  21.9029 | 22.26395 | 22.11551 | 23.64118 | 24.00502 | 26.89955 | 28.20815 |
| `modules/json/orjson_module.py`                 | 22.73103 | 22.48382 | 22.41853 | 24.15402 | 24.62667 | 27.02065 |       -- |
| `programming_game_benchmark/nbody.py`           | 21.79911 | 21.03292 | 21.67578 | 22.67467 | 23.96652 | 26.53069 | 27.50502 |
| `programming_game_benchmark/spectral_norm.py`   |  22.3125 | 22.84821 | 22.69587 | 23.96205 | 23.61161 | 27.02623 | 28.41071 |

---

### **Python 3.6**

```bash
Python 3.6.15

Linux 870aa0e9144d 5.15.0-83-generic unknown GNU/Linux

CPU(s):                             12
Thread(s) per core:                 2
Core(s) per socket:                 6
NUMA node(s):                       1
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:                        4100.0000
NUMA node0 CPU(s):                  0-11

MemTotal:       16066472 kB
MemFree:         4865104 kB
MemAvailable:   14386660 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  1.48272 |    0.01014 |    1.48355 | 1.46859 | 1.49673 |    29.10435 |
| `algorithm/search/hashmap_lookup.py`            |      yes |    1.529 |    0.04344 |    1.51079 | 1.49749 | 1.62382 |    28.53013 |
| `algorithm/search/index.py`                     |      yes |  1.50153 |    0.02642 |    1.48424 | 1.47721 | 1.54185 |    28.93304 |
| `algorithm/search/linear.py`                    |      yes |  1.56511 |    0.03708 |    1.57024 | 1.51248 | 1.63032 |    29.07924 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.08776 |    0.00286 |     0.0868 | 0.08581 | 0.09415 |    22.27455 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.08776 |    0.00149 |    0.08673 | 0.08642 | 0.08972 |    22.38337 |
| `complex/classes/classes.py`                    |      yes |  0.04918 |    0.00038 |    0.04908 | 0.04864 | 0.04981 |    22.02009 |
| `complex/classes/dataclasses_.py`               |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.10169 |     0.0009 |    0.10155 | 0.10081 | 0.10356 |    22.37221 |
| `complex/classes/simplenamespace.py`            |      yes |  0.06555 |    0.00081 |    0.06562 | 0.06439 | 0.06682 |    21.80246 |
| `complex/classes/sloted_classes.py`             |      yes |  0.04932 |    0.00036 |    0.04924 | 0.04876 | 0.04987 |    22.02567 |
| `complex/generators/simple.py`                  |      yes |  0.06971 |    0.00051 |    0.06943 | 0.06926 |  0.0705 |    22.52288 |
| `dummy/dummy.py`                                |      yes |  0.03378 |    0.00032 |    0.03371 | 0.03346 | 0.03433 |    21.71484 |
| `long_run/database/postgresql.py`               |      yes |  0.15722 |    0.00036 |    0.15718 | 0.15676 | 0.15772 |    26.75949 |
| `long_run/database/sqlite_.py`                  |      yes |  0.62778 |    0.00392 |    0.62628 | 0.62404 | 0.63523 |    63.60826 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |  0.70436 |    0.01226 |    0.69888 | 0.69749 | 0.73093 |    62.37109 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.07578 |     0.0006 |    0.07576 | 0.07485 | 0.07657 |    22.00223 |
| `long_run/processes/collect_names_from_site.py` |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/processes/generate_fake_data.py`      |      yes |  0.87106 |    0.00951 |    0.86689 | 0.86088 | 0.88696 |    64.77567 |
| `long_run/processes/maze_generator.py`          |      yes |  0.31667 |    0.01528 |    0.31194 |  0.3023 |  0.3479 |    21.73717 |
| `long_run/text/clean_text.py`                   |      yes |  0.26755 |    0.00055 |    0.26741 | 0.26699 | 0.26836 |     22.3471 |
| `long_run/text/count_words.py`                  |      yes |  0.09439 |    0.00023 |     0.0943 | 0.09415 | 0.09475 |    21.65681 |
| `math/haversine.py`                             |      yes |  0.86261 |    0.02707 |    0.85989 | 0.82702 | 0.91374 |    21.80859 |
| `math/mandelbrot.py`                            |      yes |  3.15227 |    0.09147 |    3.16877 | 2.96123 |  3.2622 |    36.35603 |
| `math/pow_simple.py`                            |      yes |  0.64606 |    0.00163 |    0.64612 | 0.64383 | 0.64914 |    21.82645 |
| `math/pow_using_math.py`                        |      yes |  1.48338 |    0.03481 |    1.48449 | 1.44413 | 1.54039 |    21.65848 |
| `modules/json/json_module.py`                   |      yes |  0.50897 |    0.01101 |    0.50691 | 0.49983 | 0.53093 |     21.9029 |
| `modules/json/orjson_module.py`                 |      yes |  0.30687 |     0.0044 |    0.30674 | 0.30222 | 0.31375 |    22.73103 |
| `programming_game_benchmark/nbody.py`           |      yes |  0.43473 |    0.00218 |    0.43396 |  0.4324 | 0.43854 |    21.79911 |
| `programming_game_benchmark/spectral_norm.py`   |      yes |  0.58673 |    0.01425 |    0.58208 | 0.57892 | 0.61882 |     22.3125 |

### **Python 3.7**

```bash
Python 3.7.17

Linux d3d70d13e8ce 5.15.0-83-generic unknown GNU/Linux

CPU(s):                             12
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:                 2
Core(s) per socket:                 6
CPU max MHz:                        4100.0000
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-11

MemTotal:       16066472 kB
MemFree:         4842036 kB
MemAvailable:   14367860 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |   1.4517 |    0.01146 |    1.44968 | 1.43565 | 1.46435 |     31.0067 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  1.47857 |    0.03503 |    1.47215 | 1.43794 | 1.53152 |    30.70257 |
| `algorithm/search/index.py`                     |      yes |  1.45982 |    0.01921 |    1.45544 | 1.43823 | 1.48922 |    30.39397 |
| `algorithm/search/linear.py`                    |      yes |  1.52673 |    0.02203 |    1.51951 | 1.50278 |  1.5589 |    29.99442 |
| `algorithm/twosum/twosum.py`                    |      yes |   0.0714 |    0.00049 |    0.07145 | 0.07052 | 0.07189 |    21.17355 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.07085 |    0.00048 |    0.07081 | 0.07028 | 0.07153 |    21.05246 |
| `complex/classes/classes.py`                    |      yes |  0.04236 |     0.0005 |    0.04251 |  0.0416 | 0.04289 |    21.59654 |
| `complex/classes/dataclasses_.py`               |      yes |   0.1085 |    0.00073 |     0.1084 | 0.10756 |  0.1095 |    21.14955 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.08511 |    0.00071 |     0.0851 | 0.08389 | 0.08601 |    21.37333 |
| `complex/classes/simplenamespace.py`            |      yes |  0.04365 |    0.00204 |     0.0426 | 0.04208 | 0.04712 |    20.94754 |
| `complex/classes/sloted_classes.py`             |      yes |  0.04237 |    0.00037 |    0.04245 | 0.04181 |  0.0429 |    21.26897 |
| `complex/generators/simple.py`                  |      yes |  0.06516 |    0.00056 |    0.06488 |  0.0645 | 0.06598 |    21.53683 |
| `dummy/dummy.py`                                |      yes |  0.02706 |    0.00044 |    0.02723 | 0.02651 | 0.02771 |    21.07924 |
| `long_run/database/postgresql.py`               |      yes |  0.14438 |    0.00131 |    0.14441 | 0.14309 | 0.14709 |    26.97935 |
| `long_run/database/sqlite_.py`                  |      yes |  0.55136 |    0.00319 |    0.54995 | 0.54754 | 0.55529 |    66.50502 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |  0.60201 |    0.00562 |    0.59919 | 0.59641 | 0.61151 |    64.85658 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.06886 |    0.00069 |    0.06899 | 0.06777 | 0.06981 |    21.14621 |
| `long_run/processes/collect_names_from_site.py` |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/processes/generate_fake_data.py`      |      yes |  0.79887 |     0.0034 |    0.79984 | 0.79363 | 0.80303 |    69.93583 |
| `long_run/processes/maze_generator.py`          |      yes |   0.3357 |    0.03596 |    0.32526 | 0.30145 | 0.40087 |    21.94643 |
| `long_run/text/clean_text.py`                   |      yes |  0.26952 |    0.00732 |    0.26585 | 0.26355 | 0.28408 |    21.32087 |
| `long_run/text/count_words.py`                  |      yes |  0.08898 |     0.0029 |    0.08746 | 0.08679 | 0.09356 |    21.04632 |
| `math/haversine.py`                             |      yes |  0.95559 |     0.0162 |    0.94871 | 0.94275 | 0.98858 |    21.10379 |
| `math/mandelbrot.py`                            |      yes |  3.04288 |     0.0477 |    3.05285 |   2.944 | 3.10201 |    35.81752 |
| `math/pow_simple.py`                            |      yes |  0.76355 |    0.01182 |    0.75785 | 0.75492 | 0.78525 |    20.99498 |
| `math/pow_using_math.py`                        |      yes |  1.71215 |    0.05416 |     1.7042 | 1.63453 | 1.77674 |    21.07924 |
| `modules/json/json_module.py`                   |      yes |  0.51007 |    0.00525 |    0.50928 | 0.50337 | 0.51722 |    22.26395 |
| `modules/json/orjson_module.py`                 |      yes |  0.26262 |    0.00283 |    0.26168 | 0.26056 | 0.26865 |    22.48382 |
| `programming_game_benchmark/nbody.py`           |      yes |  0.52176 |    0.00606 |    0.52107 | 0.51589 | 0.53411 |    21.03292 |
| `programming_game_benchmark/spectral_norm.py`   |      yes |  0.73483 |    0.01425 |    0.73092 | 0.71855 |  0.7586 |    22.84821 |

### **Python 3.8**

```bash
Python 3.8.17

Linux 5fff2fde2c05 5.15.0-83-generic unknown GNU/Linux

CPU(s):                             12
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:                 2
Core(s) per socket:                 6
CPU max MHz:                        4100.0000
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-11

MemTotal:       16066472 kB
MemFree:         4841952 kB
MemAvailable:   14372704 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  1.41776 |    0.02459 |    1.41827 | 1.39127 |  1.4614 |    29.80804 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  1.41426 |    0.03932 |    1.40659 | 1.38885 | 1.50109 |    30.31473 |
| `algorithm/search/index.py`                     |      yes |  1.42079 |     0.0114 |    1.41792 | 1.40381 | 1.43762 |    29.87221 |
| `algorithm/search/linear.py`                    |      yes |   1.4726 |    0.01599 |    1.46875 | 1.45247 | 1.49781 |    29.95703 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.07516 |    0.00037 |    0.07514 | 0.07475 | 0.07587 |    21.77344 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.07499 |    0.00054 |    0.07479 | 0.07446 | 0.07573 |    21.93862 |
| `complex/classes/classes.py`                    |      yes |  0.04443 |    0.00126 |    0.04377 | 0.04355 | 0.04706 |    21.83594 |
| `complex/classes/dataclasses_.py`               |      yes |  0.11144 |    0.00041 |    0.11143 |  0.1109 | 0.11195 |    21.84096 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.08767 |    0.00019 |    0.08764 | 0.08741 | 0.08791 |    21.92243 |
| `complex/classes/simplenamespace.py`            |      yes |  0.04417 |    0.00061 |    0.04436 | 0.04338 |  0.0449 |    22.17188 |
| `complex/classes/sloted_classes.py`             |      yes |  0.04421 |    0.00043 |    0.04416 | 0.04346 | 0.04478 |    22.03627 |
| `complex/generators/simple.py`                  |      yes |  0.06441 |    0.00051 |    0.06437 | 0.06384 | 0.06537 |     21.9721 |
| `dummy/dummy.py`                                |      yes |  0.02861 |    0.00042 |    0.02866 | 0.02807 | 0.02932 |    21.83147 |
| `long_run/database/postgresql.py`               |      yes |  0.15334 |    0.00397 |      0.152 | 0.15034 | 0.16207 |    27.48772 |
| `long_run/database/sqlite_.py`                  |      yes |  0.61451 |    0.00706 |    0.61511 | 0.60409 | 0.62365 |    66.81696 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |  0.65586 |    0.00262 |    0.65707 | 0.65176 | 0.65814 |    65.02232 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.06976 |    0.00059 |    0.06989 | 0.06896 |  0.0704 |    21.85658 |
| `long_run/processes/collect_names_from_site.py` |      yes |  2.41284 |    0.11008 |    2.36489 | 2.29921 | 2.59102 |    45.61775 |
| `long_run/processes/generate_fake_data.py`      |      yes |  0.83007 |    0.01188 |    0.82504 | 0.81982 | 0.85041 |    66.73717 |
| `long_run/processes/maze_generator.py`          |      yes |  0.31282 |    0.03167 |    0.31291 | 0.27213 | 0.36091 |    22.06696 |
| `long_run/text/clean_text.py`                   |      yes |   0.2785 |    0.00137 |    0.27853 | 0.27682 | 0.28089 |    21.66685 |
| `long_run/text/count_words.py`                  |      yes |  0.08994 |    0.00047 |    0.08998 | 0.08936 | 0.09062 |     21.7567 |
| `math/haversine.py`                             |      yes |  0.90544 |    0.01111 |    0.89971 | 0.89684 | 0.92594 |    21.95592 |
| `math/mandelbrot.py`                            |      yes |  3.03787 |     0.0181 |    3.03129 | 3.02396 | 3.07025 |    36.21987 |
| `math/pow_simple.py`                            |      yes |  0.75509 |     0.0013 |    0.75502 | 0.75271 | 0.75707 |    21.96484 |
| `math/pow_using_math.py`                        |      yes |  1.38568 |     0.0268 |      1.376 | 1.35661 | 1.43174 |    21.66071 |
| `modules/json/json_module.py`                   |      yes |  0.48908 |    0.00657 |    0.48818 | 0.47653 |  0.4959 |    22.11551 |
| `modules/json/orjson_module.py`                 |      yes |  0.29605 |    0.00129 |     0.2964 | 0.29356 | 0.29782 |    22.41853 |
| `programming_game_benchmark/nbody.py`           |      yes |  0.53462 |    0.00832 |    0.53678 | 0.52505 |   0.549 |    21.67578 |
| `programming_game_benchmark/spectral_norm.py`   |      yes |  0.67632 |    0.00481 |    0.67693 | 0.66922 | 0.68227 |    22.69587 |

### **Python 3.9**

```bash
Python 3.9.17

Linux 6b652d421f6e 5.15.0-83-generic unknown GNU/Linux

CPU(s):                             12
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:                 2
Core(s) per socket:                 6
CPU max MHz:                        4100.0000
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-11

MemTotal:       16066472 kB
MemFree:         4827184 kB
MemAvailable:   14362628 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  1.44129 |    0.04705 |    1.42749 | 1.40723 | 1.54495 |    32.14676 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  1.44211 |    0.02222 |    1.44311 | 1.41372 |  1.4764 |    30.48884 |
| `algorithm/search/index.py`                     |      yes |  1.42715 |    0.01081 |    1.42666 | 1.41291 | 1.44502 |    30.88672 |
| `algorithm/search/linear.py`                    |      yes |  1.51419 |    0.04708 |    1.49316 | 1.46629 |  1.5992 |    30.93583 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.08698 |    0.00055 |     0.0868 | 0.08622 | 0.08784 |    23.50446 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.08722 |    0.00039 |    0.08737 | 0.08644 | 0.08751 |    22.69475 |
| `complex/classes/classes.py`                    |      yes |  0.04784 |    0.00046 |    0.04769 | 0.04737 | 0.04874 |    23.65848 |
| `complex/classes/dataclasses_.py`               |      yes |  0.13889 |    0.00097 |    0.13852 | 0.13813 | 0.14093 |    23.94754 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.10005 |    0.00039 |     0.1001 | 0.09955 | 0.10055 |     23.4827 |
| `complex/classes/simplenamespace.py`            |      yes |  0.05023 |     0.0005 |    0.05031 | 0.04933 | 0.05103 |    22.92746 |
| `complex/classes/sloted_classes.py`             |      yes |  0.04798 |    0.00031 |    0.04812 | 0.04751 | 0.04831 |    23.01786 |
| `complex/generators/simple.py`                  |      yes |  0.06725 |     0.0006 |    0.06701 |  0.0667 | 0.06811 |    23.93806 |
| `dummy/dummy.py`                                |      yes |  0.03182 |    0.00028 |    0.03181 | 0.03144 | 0.03214 |    23.38839 |
| `long_run/database/postgresql.py`               |      yes |  0.16995 |    0.00097 |    0.16984 |  0.1689 | 0.17157 |     29.2779 |
| `long_run/database/sqlite_.py`                  |      yes |  0.66534 |    0.01466 |      0.658 | 0.65472 | 0.69665 |     67.6981 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |  0.70857 |    0.00491 |    0.70634 |  0.7044 | 0.71892 |    65.94531 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.07977 |    0.00073 |    0.07971 | 0.07894 | 0.08072 |    23.48549 |
| `long_run/processes/collect_names_from_site.py` |      yes |   2.5156 |    0.05094 |    2.53206 | 2.43889 | 2.57117 |    45.85826 |
| `long_run/processes/generate_fake_data.py`      |      yes |  0.90604 |    0.01743 |    0.89676 | 0.89268 | 0.94126 |    69.76897 |
| `long_run/processes/maze_generator.py`          |      yes |  0.32348 |    0.02734 |    0.33255 |  0.2771 | 0.35183 |    23.64007 |
| `long_run/text/clean_text.py`                   |      yes |  0.29128 |    0.00106 |    0.29149 | 0.28999 | 0.29273 |    23.49107 |
| `long_run/text/count_words.py`                  |      yes |  0.10041 |    0.00028 |    0.10045 | 0.10009 | 0.10081 |    23.71261 |
| `math/haversine.py`                             |      yes |  1.00468 |    0.01554 |    0.99614 | 0.98987 | 1.02193 |     23.4933 |
| `math/mandelbrot.py`                            |      yes |   2.6179 |    0.00547 |    2.61669 | 2.61103 |  2.6269 |    43.91741 |
| `math/pow_simple.py`                            |      yes |  0.76957 |    0.00231 |    0.76899 | 0.76785 | 0.77454 |    23.51116 |
| `math/pow_using_math.py`                        |      yes |  1.41092 |     0.0235 |    1.40655 | 1.38021 | 1.44453 |    23.51395 |
| `modules/json/json_module.py`                   |      yes |  0.50828 |    0.01755 |    0.50158 | 0.49254 | 0.53874 |    23.64118 |
| `modules/json/orjson_module.py`                 |      yes |  0.33215 |    0.00166 |    0.33211 | 0.33003 | 0.33424 |    24.15402 |
| `programming_game_benchmark/nbody.py`           |      yes |  0.55171 |    0.01019 |    0.54932 | 0.53766 | 0.56818 |    22.67467 |
| `programming_game_benchmark/spectral_norm.py`   |      yes |  0.70842 |    0.00479 |    0.70732 | 0.70364 | 0.71733 |    23.96205 |

### **Python 3.10**

```bash
Python 3.10.12

Linux 7cf6daf92d1e 5.15.0-83-generic unknown GNU/Linux

CPU(s):                             12
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:                 2
Core(s) per socket:                 6
CPU max MHz:                        4100.0000
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-11

MemTotal:       16066472 kB
MemFree:         4818948 kB
MemAvailable:   14357764 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  1.24025 |    0.01091 |    1.24201 | 1.22538 | 1.25631 |    32.59654 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  1.27511 |     0.0258 |    1.27433 | 1.23605 | 1.32047 |    34.13504 |
| `algorithm/search/index.py`                     |      yes |  1.26973 |    0.02941 |    1.26659 | 1.23603 | 1.32886 |    32.48716 |
| `algorithm/search/linear.py`                    |      yes |  1.29885 |    0.01945 |    1.29476 | 1.27727 | 1.33331 |    32.62221 |
| `algorithm/twosum/twosum.py`                    |      yes |   0.0798 |    0.00043 |    0.07963 | 0.07912 | 0.08025 |    23.68248 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.08009 |    0.00039 |    0.08008 | 0.07946 | 0.08065 |    23.78125 |
| `complex/classes/classes.py`                    |      yes |  0.04352 |    0.00034 |     0.0435 | 0.04312 | 0.04416 |    25.40179 |
| `complex/classes/dataclasses_.py`               |      yes |  0.12649 |    0.00042 |    0.12668 | 0.12572 |   0.127 |    26.08259 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.09263 |    0.00044 |     0.0926 | 0.09199 | 0.09335 |    24.13672 |
| `complex/classes/simplenamespace.py`            |      yes |  0.04574 |    0.00036 |    0.04559 | 0.04539 | 0.04627 |    26.55078 |
| `complex/classes/sloted_classes.py`             |      yes |  0.04356 |    0.00027 |     0.0436 | 0.04325 | 0.04401 |    25.93415 |
| `complex/generators/simple.py`                  |      yes |  0.06293 |    0.00035 |    0.06296 | 0.06229 | 0.06346 |    25.80301 |
| `dummy/dummy.py`                                |      yes |  0.03153 |    0.00044 |    0.03162 | 0.03099 |  0.0322 |    23.58817 |
| `long_run/database/postgresql.py`               |      yes |  0.15855 |    0.00078 |    0.15832 | 0.15755 |  0.1598 |    28.29074 |
| `long_run/database/sqlite_.py`                  |      yes |  0.61578 |    0.00355 |    0.61474 |  0.6133 | 0.62369 |    67.48382 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |  0.66839 |    0.00992 |    0.66906 |  0.6577 | 0.68138 |    65.15011 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.07116 |    0.00059 |    0.07103 | 0.07052 | 0.07232 |    23.36719 |
| `long_run/processes/collect_names_from_site.py` |      yes |  2.48665 |    0.03791 |    2.47036 | 2.45108 | 2.55137 |    45.77455 |
| `long_run/processes/generate_fake_data.py`      |      yes |  0.84173 |    0.00994 |    0.84381 |  0.8313 | 0.85736 |    68.92634 |
| `long_run/processes/maze_generator.py`          |      yes |  0.30394 |    0.01624 |    0.29747 | 0.28575 | 0.33448 |    23.82478 |
| `long_run/text/clean_text.py`                   |      yes |  0.27642 |    0.00499 |    0.27427 | 0.27121 | 0.28538 |     23.8058 |
| `long_run/text/count_words.py`                  |      yes |  0.09174 |    0.00061 |    0.09183 | 0.09066 | 0.09242 |     24.1529 |
| `math/haversine.py`                             |      yes |  0.94812 |    0.06772 |    0.91792 | 0.90973 | 1.09937 |    23.59375 |
| `math/mandelbrot.py`                            |      yes |  2.61357 |    0.06694 |    2.58904 | 2.57972 | 2.76494 |    40.75391 |
| `math/pow_simple.py`                            |      yes |  0.72555 |    0.00652 |     0.7249 | 0.71627 | 0.73273 |       23.75 |
| `math/pow_using_math.py`                        |      yes |  1.42649 |    0.04479 |     1.4088 | 1.36988 | 1.49399 |     24.2115 |
| `modules/json/json_module.py`                   |      yes |  0.44232 |    0.00326 |     0.4412 | 0.43874 | 0.44832 |    24.00502 |
| `modules/json/orjson_module.py`                 |      yes |  0.30102 |    0.00251 |    0.30156 | 0.29694 | 0.30385 |    24.62667 |
| `programming_game_benchmark/nbody.py`           |      yes |  0.52331 |    0.00742 |     0.5198 | 0.51623 | 0.53484 |    23.96652 |
| `programming_game_benchmark/spectral_norm.py`   |      yes |  0.62619 |    0.00727 |    0.62628 | 0.61733 | 0.63826 |    23.61161 |

### **Python 3.11**

```bash
Python 3.11.4

Linux 93dbf2110396 5.15.0-83-generic unknown GNU/Linux

CPU(s):                             12
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:                 2
Core(s) per socket:                 6
CPU max MHz:                        4100.0000
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-11

MemTotal:       16066472 kB
MemFree:         4796360 kB
MemAvailable:   14361260 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  1.05342 |    0.00762 |    1.05323 | 1.04542 |  1.0671 |     35.4202 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  1.07296 |    0.01917 |    1.06349 | 1.04875 | 1.10287 |    36.06194 |
| `algorithm/search/index.py`                     |      yes |  1.07475 |    0.01514 |    1.06873 |  1.0564 | 1.10014 |    35.87333 |
| `algorithm/search/linear.py`                    |      yes |  1.11193 |    0.00842 |    1.11135 | 1.09832 | 1.12233 |    36.00725 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.07551 |     0.0004 |     0.0755 | 0.07481 | 0.07598 |    26.93638 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.07587 |    0.00042 |    0.07582 | 0.07532 | 0.07665 |    26.50558 |
| `complex/classes/classes.py`                    |      yes |  0.02196 |    0.00048 |    0.02185 |  0.0214 | 0.02295 |     28.5173 |
| `complex/classes/dataclasses_.py`               |      yes |   0.1169 |    0.00048 |    0.11692 | 0.11599 | 0.11735 |    27.84766 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.08625 |    0.00112 |    0.08575 | 0.08524 |  0.0885 |    27.33817 |
| `complex/classes/simplenamespace.py`            |      yes |  0.02695 |    0.00019 |    0.02693 | 0.02666 | 0.02724 |    28.30413 |
| `complex/classes/sloted_classes.py`             |      yes |  0.02194 |    0.00027 |    0.02187 | 0.02159 | 0.02231 |    27.66853 |
| `complex/generators/simple.py`                  |      yes |   0.0418 |    0.00071 |    0.04161 | 0.04085 | 0.04294 |    28.26618 |
| `dummy/dummy.py`                                |      yes |    0.016 |    0.00018 |    0.01596 | 0.01581 | 0.01638 |    26.96317 |
| `long_run/database/postgresql.py`               |      yes |  0.15482 |    0.00211 |    0.15386 | 0.15327 | 0.15922 |    30.93025 |
| `long_run/database/sqlite_.py`                  |      yes |  0.61768 |    0.00485 |    0.61573 | 0.61348 | 0.62758 |     72.4654 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |  0.65968 |    0.00573 |    0.65932 | 0.65228 | 0.67064 |    70.72042 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.06137 |    0.00138 |    0.06084 | 0.06022 | 0.06429 |    26.79129 |
| `long_run/processes/collect_names_from_site.py` |      yes |  1.99313 |    0.08779 |    1.98294 | 1.87893 | 2.12896 |    47.67466 |
| `long_run/processes/generate_fake_data.py`      |      yes |  0.82162 |    0.00481 |    0.82105 | 0.81396 | 0.83009 |    72.37556 |
| `long_run/processes/maze_generator.py`          |      yes |  0.19542 |    0.00794 |    0.19808 | 0.18054 | 0.20419 |    26.94531 |
| `long_run/text/clean_text.py`                   |      yes |  0.24058 |    0.00361 |    0.23973 | 0.23701 | 0.24617 |    26.94531 |
| `long_run/text/count_words.py`                  |      yes |  0.07864 |     0.0031 |    0.07695 | 0.07637 | 0.08456 |    26.51618 |
| `math/haversine.py`                             |      yes |   0.8077 |    0.01987 |    0.80286 | 0.78144 | 0.83511 |     26.3817 |
| `math/mandelbrot.py`                            |      yes |  2.59169 |    0.04235 |    2.57193 | 2.56703 | 2.68362 |    40.91071 |
| `math/pow_simple.py`                            |      yes |  0.34713 |     0.0032 |    0.34714 |   0.341 | 0.35158 |    26.44643 |
| `math/pow_using_math.py`                        |      yes |  1.17229 |    0.02489 |    1.17095 | 1.14548 | 1.20992 |    26.65737 |
| `modules/json/json_module.py`                   |      yes |  0.40178 |    0.00352 |    0.40296 | 0.39653 | 0.40531 |    26.89955 |
| `modules/json/orjson_module.py`                 |      yes |  0.26451 |    0.00268 |    0.26573 | 0.26094 | 0.26782 |    27.02065 |
| `programming_game_benchmark/nbody.py`           |      yes |  0.34749 |    0.00766 |    0.34369 | 0.34254 | 0.36236 |    26.53069 |
| `programming_game_benchmark/spectral_norm.py`   |      yes |  0.53606 |    0.00527 |    0.53683 | 0.52779 | 0.54298 |    27.02623 |

### **Python 3.12**

```bash
Python 3.12.0rc2

Linux 1fcedf7e395b 5.15.0-83-generic unknown GNU/Linux

CPU(s):                             12
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:                 2
Core(s) per socket:                 6
CPU max MHz:                        4100.0000
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-11

MemTotal:       16066472 kB
MemFree:         4776360 kB
MemAvailable:   14342744 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  1.19897 |     0.0267 |    1.19322 | 1.16342 |  1.2406 |    35.30413 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  1.18975 |    0.02329 |    1.18144 | 1.16946 | 1.23436 |    36.35268 |
| `algorithm/search/index.py`                     |      yes |  1.19357 |    0.00745 |    1.19448 | 1.18283 |  1.2049 |    35.61328 |
| `algorithm/search/linear.py`                    |      yes |  1.25807 |    0.02205 |    1.25746 | 1.23002 | 1.28775 |    35.72042 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.08759 |    0.00039 |    0.08768 | 0.08699 | 0.08814 |    27.46652 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.08734 |    0.00024 |     0.0873 | 0.08704 | 0.08768 |    26.90402 |
| `complex/classes/classes.py`                    |      yes |  0.02359 |    0.00197 |    0.02277 | 0.02233 | 0.02785 |    28.17467 |
| `complex/classes/dataclasses_.py`               |      yes |  0.13518 |    0.00054 |    0.13501 | 0.13445 | 0.13607 |    28.05301 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.09999 |    0.00138 |    0.09939 | 0.09925 | 0.10308 |    27.94029 |
| `complex/classes/simplenamespace.py`            |      yes |  0.02961 |    0.00025 |    0.02968 | 0.02928 | 0.02999 |    29.12109 |
| `complex/classes/sloted_classes.py`             |      yes |   0.0237 |    0.00125 |    0.02324 | 0.02306 | 0.02652 |    27.64118 |
| `complex/generators/simple.py`                  |      yes |  0.04654 |    0.00044 |    0.04653 |   0.046 | 0.04714 |     29.5279 |
| `dummy/dummy.py`                                |      yes |  0.01942 |    0.00144 |    0.01887 | 0.01878 | 0.02267 |    27.69252 |
| `long_run/database/postgresql.py`               |      yes |  0.17954 |    0.00076 |    0.17963 |  0.1784 | 0.18058 |    32.45424 |
| `long_run/database/sqlite_.py`                  |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/file/load_titanic_csv_pandas.py`      |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.06874 |    0.00052 |    0.06869 | 0.06811 | 0.06962 |    27.46038 |
| `long_run/processes/collect_names_from_site.py` |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/processes/generate_fake_data.py`      |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/processes/maze_generator.py`          |      yes |  0.19447 |    0.01381 |    0.19131 |  0.1785 | 0.21838 |    28.24163 |
| `long_run/text/clean_text.py`                   |      yes |  0.25736 |    0.00374 |    0.25673 | 0.25378 | 0.26444 |      27.476 |
| `long_run/text/count_words.py`                  |      yes |  0.08471 |    0.00129 |    0.08438 | 0.08334 | 0.08725 |    27.38672 |
| `math/haversine.py`                             |      yes |  0.88259 |    0.01273 |    0.87746 | 0.86698 | 0.90023 |    27.58203 |
| `math/mandelbrot.py`                            |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `math/pow_simple.py`                            |      yes |  0.31708 |    0.00989 |    0.31126 | 0.30895 | 0.33464 |    27.48214 |
| `math/pow_using_math.py`                        |      yes |  1.19568 |     0.0068 |    1.19324 |  1.1876 | 1.20558 |    27.67746 |
| `modules/json/json_module.py`                   |      yes |  0.40882 |    0.00864 |    0.40467 | 0.39956 | 0.42101 |    28.20815 |
| `modules/json/orjson_module.py`                 |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `programming_game_benchmark/nbody.py`           |      yes |  0.35671 |     0.0057 |    0.35797 | 0.34883 | 0.36342 |    27.50502 |
| `programming_game_benchmark/spectral_norm.py`   |      yes |  0.63169 |    0.00317 |    0.63177 | 0.62687 | 0.63715 |    28.41071 |
