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

> Last run: Thu Jul 6 08:59:30 AM -03 2023

### **Comparison**

#### How much faster 3.12 is? (Mean / Median from 3.6 to 3.11)

| Command                                         |               3.6 |               3.7 |               3.8 |               3.9 |              3.10 |              3.11 |
| :---------------------------------------------- | ----------------: | ----------------: | ----------------: | ----------------: | ----------------: | ----------------: |
| `algorithm/search/bin.py`                       |   27.66% / 27.62% |   24.83% / 24.49% |   25.38% / 25.02% |   21.87% / 21.76% |     6.63% / 6.83% |   -8.64% / -8.64% |
| `algorithm/search/hashmap_lookup.py`            |   28.37% / 29.21% |   24.83% / 24.83% |   24.67% / 24.58% |   21.00% / 21.34% |     7.04% / 6.36% |   -9.25% / -9.19% |
| `algorithm/search/index.py`                     |   26.26% / 25.89% |   24.95% / 24.87% |   25.13% / 24.43% |   20.52% / 20.50% |     6.44% / 6.42% |   -8.06% / -8.10% |
| `algorithm/search/linear.py`                    |   25.74% / 25.01% |   22.80% / 22.45% |   23.09% / 22.43% |   20.85% / 20.03% |     5.97% / 5.18% |   -8.72% / -8.86% |
| `algorithm/twosum/twosum.py`                    |     1.09% / 1.17% | -17.36% / -17.15% |   -6.38% / -6.99% |     3.66% / 1.88% |   -6.38% / -6.44% | -11.44% / -11.43% |
| `algorithm/twosum/twosum_naive.py`              |     2.08% / 1.82% | -16.98% / -16.97% |   -7.15% / -7.13% |     5.16% / 2.87% |   -5.79% / -5.85% | -10.13% / -11.64% |
| `complex/classes/classes.py`                    | 117.69% / 114.15% |   83.06% / 84.11% |   96.21% / 97.51% | 109.62% / 107.97% |   91.22% / 91.41% |   -5.25% / -4.45% |
| `complex/classes/dataclasses_.py`               |           -- / -- | -19.30% / -19.76% | -12.51% / -12.41% |     3.94% / 4.02% |   -6.47% / -6.37% | -12.29% / -12.34% |
| `complex/classes/namedtuple_classes.py`         |     3.71% / 3.70% | -12.77% / -12.24% |   -6.41% / -6.56% |     2.37% / 2.67% |   -6.39% / -6.17% | -12.62% / -12.48% |
| `complex/classes/simplenamespace.py`            | 122.58% / 124.36% |   42.08% / 43.18% |   54.68% / 56.10% |   68.61% / 70.40% |   53.83% / 54.41% |   -9.53% / -8.44% |
| `complex/classes/sloted_classes.py`             | 124.32% / 124.95% |   91.79% / 91.45% | 107.52% / 107.53% | 118.00% / 117.70% |   97.17% / 97.35% |   -3.57% / -3.30% |
| `complex/generators/simple.py`                  |   50.40% / 50.68% |   40.59% / 41.12% |   41.03% / 39.30% |   46.44% / 46.59% |   36.52% / 36.17% |   -9.78% / -9.45% |
| `dummy/dummy.py`                                | 109.35% / 147.98% |   62.61% / 91.57% |  86.25% / 122.33% | 104.64% / 136.74% |  82.93% / 116.50% |   -12.97% / 2.31% |
| `long_run/database/postgresql.py`               | -12.30% / -12.01% | -20.80% / -20.44% | -10.44% / -10.05% |   -4.35% / -4.00% | -11.83% / -11.48% | -13.11% / -12.43% |
| `long_run/database/sqlite_.py`                  |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `long_run/file/load_titanic_csv_pandas.py`      |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `long_run/file/load_titanic_csv_python.py`      |   10.83% / 11.06% |     1.26% / 0.24% |     7.70% / 7.71% |   16.97% / 16.99% |     4.28% / 4.43% | -11.61% / -11.71% |
| `long_run/processes/collect_names_from_site.py` |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `long_run/processes/generate_fake_data.py`      |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `math/haversine.py`                             |   -4.94% / -4.52% |     6.71% / 7.84% |   -4.47% / -3.56% |   14.08% / 15.22% |     3.72% / 4.07% |   -9.69% / -9.40% |
| `math/mandelbrot.py`                            |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `math/pow_simple.py`                            |   92.02% / 95.16% | 128.90% / 132.87% |   81.20% / 86.24% | 135.37% / 141.04% | 108.42% / 111.81% |     4.80% / 6.70% |
| `math/pow_using_math.py`                        |   16.71% / 16.95% |   34.41% / 34.81% |   21.18% / 21.71% |   18.73% / 18.23% |   15.39% / 16.19% |   -2.80% / -2.65% |
| `modules/json/json_module.py`                   |   22.83% / 22.27% |   27.00% / 26.34% |   24.64% / 23.31% |   25.99% / 25.27% |     8.92% / 8.34% |    0.38% / -0.47% |
| `modules/json/orjson_module.py`                 |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `long_run/processes/maze_generator.py`          |   48.34% / 48.04% |   -3.50% / -2.03% |
| `long_run/text/count_words.py`                  |     7.66% / 8.01% |   -8.84% / -8.73% |

---

#### How much more memory 3.12 uses? (Memory diff from 3.6 to 3.11)

| Command                                         |    3.6 |    3.7 |    3.8 |    3.9 |   3.10 |   3.11 |
| :---------------------------------------------- | -----: | -----: | -----: | -----: | -----: | -----: |
| `algorithm/search/bin.py`                       | 22.81% | 19.48% |  24.6% | 12.52% |  6.16% | -1.16% |
| `algorithm/search/hashmap_lookup.py`            | 28.12% | 13.67% | 22.59% |  14.9% | 10.16% | -1.13% |
| `algorithm/search/index.py`                     | 21.54% | 19.51% | 24.68% | 12.62% |  8.64% | -1.29% |
| `algorithm/search/linear.py`                    | 23.42% | 17.77% | 24.99% | 11.66% |  9.31% | -1.21% |
| `algorithm/twosum/twosum.py`                    | 23.52% | 29.93% | 35.66% | 18.37% | 16.79% |  3.99% |
| `algorithm/twosum/twosum_naive.py`              | 22.93% | 29.64% | 33.71% | 17.68% | 13.74% |  1.18% |
| `complex/classes/classes.py`                    | 29.28% | 32.44% | 40.06% | 20.78% | 12.82% |  1.62% |
| `complex/classes/dataclasses_.py`               |     -- | 33.24% | 37.07% |  17.2% | 12.84% | -1.73% |
| `complex/classes/namedtuple_classes.py`         | 24.08% | 31.12% | 36.17% | 18.83% | 15.75% |   0.2% |
| `complex/classes/simplenamespace.py`            | 32.45% | 36.57% | 41.47% | 23.63% | 12.14% |  0.24% |
| `complex/classes/sloted_classes.py`             | 28.01% | 32.09% | 35.58% | 19.48% | 11.31% | -1.36% |
| `complex/generators/simple.py`                  | 32.69% | 38.06% | 44.41% | 23.48% | 16.87% |  2.04% |
| `dummy/dummy.py`                                |  26.0% | 30.46% | 34.39% | 16.76% | 13.29% |  3.08% |
| `long_run/database/postgresql.py`               | 20.14% | 21.08% | 34.41% | 11.06% | 11.47% |  3.49% |
| `long_run/database/sqlite_.py`                  |     -- |     -- |     -- |     -- |     -- |     -- |
| `long_run/file/load_titanic_csv_pandas.py`      |     -- |     -- |     -- |     -- |     -- |     -- |
| `long_run/file/load_titanic_csv_python.py`      | 26.74% | 30.41% | 34.18% | 20.01% | 18.27% |  3.96% |
| `long_run/processes/collect_names_from_site.py` |     -- |     -- |     -- |     -- |     -- |     -- |
| `long_run/processes/generate_fake_data.py`      |     -- |     -- |     -- |     -- |     -- |     -- |
| `math/haversine.py`                             | 23.62% | 27.79% |  31.7% | 18.16% | 16.04% |  0.38% |
| `math/mandelbrot.py`                            |     -- |     -- |     -- |     -- |     -- |     -- |
| `math/pow_simple.py`                            | 24.04% | 27.86% | 31.29% | 17.52% | 15.54% |  0.11% |
| `math/pow_using_math.py`                        | 26.92% | 29.94% | 32.53% |  17.1% | 14.08% |  3.54% |
| `modules/json/json_module.py`                   | 30.52% | 27.68% | 35.23% | 21.36% | 19.68% |  6.74% |
| `modules/json/orjson_module.py`                 |     -- |     -- |     -- |     -- |     -- |     -- |
| `long_run/processes/maze_generator.py`          | 19.13% |  3.66% |
| `long_run/text/count_words.py`                  | 15.63% |  1.72% |

---

#### **Execution**

##### **Mean [s]**

| Command                                         |     3.6 |     3.7 |     3.8 |     3.9 |    3.10 |    3.11 |    3.12 |
| :---------------------------------------------- | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| `algorithm/search/bin.py`                       | 1.47474 | 1.44211 | 1.44844 | 1.40788 | 1.23186 | 1.05539 | 1.15522 |
| `algorithm/search/hashmap_lookup.py`            | 1.49383 | 1.45265 | 1.45073 | 1.40812 | 1.24564 | 1.05607 |  1.1637 |
| `algorithm/search/index.py`                     | 1.48493 | 1.46956 | 1.47166 | 1.41747 |  1.2518 | 1.08126 | 1.17608 |
| `algorithm/search/linear.py`                    | 1.54328 | 1.50718 | 1.51064 | 1.48321 | 1.30064 | 1.12027 | 1.22731 |
| `algorithm/twosum/twosum.py`                    | 0.08477 |  0.0693 | 0.07851 | 0.08693 | 0.07851 | 0.07427 | 0.08386 |
| `algorithm/twosum/twosum_naive.py`              | 0.08483 | 0.06899 | 0.07716 | 0.08739 | 0.07829 | 0.07468 |  0.0831 |
| `complex/classes/classes.py`                    | 0.04935 |  0.0415 | 0.04448 | 0.04752 | 0.04335 | 0.02148 | 0.02267 |
| `complex/classes/dataclasses_.py`               |      -- | 0.10621 | 0.11515 |  0.1368 |  0.1231 | 0.11543 | 0.13161 |
| `complex/classes/namedtuple_classes.py`         | 0.10016 | 0.08425 | 0.09039 | 0.09887 | 0.09041 | 0.08439 | 0.09658 |
| `complex/classes/simplenamespace.py`            | 0.06517 |  0.0416 | 0.04529 | 0.04937 | 0.04504 | 0.02649 | 0.02928 |
| `complex/classes/sloted_classes.py`             | 0.04834 | 0.04133 | 0.04472 | 0.04698 | 0.04249 | 0.02078 | 0.02155 |
| `complex/generators/simple.py`                  |  0.0684 | 0.06394 | 0.06414 |  0.0666 | 0.06209 | 0.04103 | 0.04548 |
| `dummy/dummy.py`                                | 0.03471 | 0.02696 | 0.03088 | 0.03393 | 0.03033 | 0.01443 | 0.01658 |
| `long_run/database/postgresql.py`               | 0.15418 | 0.13924 | 0.15745 | 0.16816 |   0.155 | 0.15275 |  0.1758 |
| `long_run/database/sqlite_.py`                  | 0.61977 | 0.53919 | 0.62214 | 0.65553 | 0.61012 | 0.62061 |      -- |
| `long_run/file/load_titanic_csv_pandas.py`      | 0.69384 | 0.59412 | 0.66897 | 0.70655 | 0.65075 | 0.64379 |      -- |
| `long_run/file/load_titanic_csv_python.py`      | 0.07388 |  0.0675 | 0.07179 | 0.07797 | 0.06951 | 0.05892 | 0.06666 |
| `long_run/processes/collect_names_from_site.py` |      -- |      -- | 1.87281 | 2.08882 | 2.04696 | 1.75078 |      -- |
| `long_run/processes/generate_fake_data.py`      | 0.85907 | 0.78601 | 0.88291 |  0.8825 |  0.8271 | 0.80923 |      -- |
| `math/haversine.py`                             | 0.83484 | 0.93711 |   0.839 | 1.00187 | 0.91088 | 0.79309 | 0.87822 |
| `math/mandelbrot.py`                            | 3.13033 | 3.04159 | 3.19851 | 2.62146 | 2.57208 | 2.58225 |      -- |
| `math/pow_simple.py`                            | 0.64288 | 0.76632 | 0.60665 | 0.78799 | 0.69776 | 0.35086 | 0.33479 |
| `math/pow_using_math.py`                        |  1.4148 | 1.62948 | 1.46903 | 1.43937 | 1.39881 | 1.17832 | 1.21228 |
| `modules/json/json_module.py`                   | 0.49616 | 0.51299 | 0.50347 | 0.50892 | 0.43996 | 0.40549 | 0.40394 |
| `modules/json/orjson_module.py`                 | 0.30412 | 0.26256 | 0.26581 | 0.28736 | 0.25996 | 0.21091 |      -- |
| `long_run/processes/maze_generator.py`          |  0.2022 | 0.13154 | 0.13631 |
| `long_run/text/count_words.py`                  | 0.07421 | 0.06284 | 0.06893 |

##### **Median [s]**

| Command                                         |     3.6 |     3.7 |     3.8 |     3.9 |    3.10 |    3.11 |    3.12 |
| :---------------------------------------------- | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| `algorithm/search/bin.py`                       | 1.47241 | 1.43635 | 1.44251 | 1.40488 | 1.23264 | 1.05407 | 1.15378 |
| `algorithm/search/hashmap_lookup.py`            | 1.50081 | 1.44994 | 1.44703 |  1.4094 | 1.23544 | 1.05482 | 1.16155 |
| `algorithm/search/index.py`                     | 1.47896 | 1.46699 | 1.46178 |  1.4157 | 1.25027 | 1.07967 | 1.17482 |
| `algorithm/search/linear.py`                    | 1.53877 | 1.50724 |   1.507 | 1.47744 | 1.29471 | 1.12192 | 1.23094 |
| `algorithm/twosum/twosum.py`                    | 0.08482 | 0.06946 | 0.07798 | 0.08542 | 0.07844 | 0.07426 | 0.08384 |
| `algorithm/twosum/twosum_naive.py`              | 0.08465 | 0.06903 | 0.07721 | 0.08553 | 0.07828 | 0.07346 | 0.08314 |
| `complex/classes/classes.py`                    | 0.04812 | 0.04137 | 0.04438 | 0.04673 | 0.04301 | 0.02147 | 0.02247 |
| `complex/classes/dataclasses_.py`               |      -- | 0.10556 | 0.11522 | 0.13684 | 0.12317 | 0.11532 | 0.13155 |
| `complex/classes/namedtuple_classes.py`         |     0.1 | 0.08463 |  0.0901 |   0.099 | 0.09048 |  0.0844 | 0.09643 |
| `complex/classes/simplenamespace.py`            | 0.06511 | 0.04155 |  0.0453 | 0.04945 | 0.04481 | 0.02657 | 0.02902 |
| `complex/classes/sloted_classes.py`             | 0.04841 |  0.0412 | 0.04466 | 0.04685 | 0.04247 | 0.02081 | 0.02152 |
| `complex/generators/simple.py`                  | 0.06841 | 0.06407 | 0.06324 | 0.06655 | 0.06182 | 0.04111 |  0.0454 |
| `dummy/dummy.py`                                | 0.03442 | 0.02659 | 0.03086 | 0.03286 | 0.03005 |  0.0142 | 0.01388 |
| `long_run/database/postgresql.py`               | 0.15392 | 0.13918 | 0.15735 | 0.16793 | 0.15485 | 0.15318 | 0.17493 |
| `long_run/database/sqlite_.py`                  | 0.61722 | 0.53843 | 0.62133 | 0.65637 | 0.60756 | 0.61903 |      -- |
| `long_run/file/load_titanic_csv_pandas.py`      |  0.6909 | 0.59274 | 0.66868 | 0.69862 | 0.64782 | 0.64354 |      -- |
| `long_run/file/load_titanic_csv_python.py`      |   0.074 | 0.06679 | 0.07177 | 0.07795 | 0.06958 | 0.05883 | 0.06663 |
| `long_run/processes/collect_names_from_site.py` |      -- |      -- | 1.86932 | 2.09057 | 2.03481 | 1.75564 |      -- |
| `long_run/processes/generate_fake_data.py`      | 0.85818 | 0.78482 | 0.84905 | 0.87833 | 0.82399 | 0.80933 |      -- |
| `math/haversine.py`                             |  0.8294 | 0.93677 | 0.83773 | 1.00082 | 0.90403 | 0.78699 | 0.86865 |
| `math/mandelbrot.py`                            | 3.14387 | 3.03643 | 3.22139 | 2.59625 | 2.57099 | 2.56146 |      -- |
| `math/pow_simple.py`                            | 0.63428 | 0.75684 | 0.60529 | 0.78338 | 0.68838 | 0.34677 |   0.325 |
| `math/pow_using_math.py`                        | 1.40511 |  1.6197 | 1.46223 | 1.42052 | 1.39592 | 1.16956 | 1.20144 |
| `modules/json/json_module.py`                   |   0.495 | 0.51146 | 0.49918 | 0.50712 | 0.43861 | 0.40293 | 0.40483 |
| `modules/json/orjson_module.py`                 | 0.30241 | 0.26233 | 0.26532 | 0.28682 | 0.25974 |  0.2102 |      -- |
| `long_run/processes/maze_generator.py`          | 0.20024 | 0.13252 | 0.13526 |
| `long_run/text/count_words.py`                  | 0.07427 | 0.06276 | 0.06876 |

#### **Memory Usage**

##### **MEM [MB]**

| Command                                         |      3.6 |      3.7 |      3.8 |      3.9 |     3.10 |     3.11 |     3.12 |
| :---------------------------------------------- | -------: | -------: | -------: | -------: | -------: | -------: | -------: |
| `algorithm/search/bin.py`                       | 28.93555 | 29.74219 | 28.51992 | 31.58359 | 33.47383 | 35.95195 | 35.53633 |
| `algorithm/search/hashmap_lookup.py`            | 28.25703 |    31.85 | 29.53164 | 31.50742 |  32.8625 | 36.61563 | 36.20234 |
| `algorithm/search/index.py`                     | 29.14961 | 29.64531 | 28.41523 | 31.45781 | 32.61289 | 35.89336 |  35.4293 |
| `algorithm/search/linear.py`                    | 28.90117 | 30.28867 | 28.53828 | 31.94492 | 32.63281 | 36.10742 | 35.67109 |
| `algorithm/twosum/twosum.py`                    | 22.28984 | 21.18945 |  20.2957 | 23.25898 | 23.57344 | 26.47695 | 27.53242 |
| `algorithm/twosum/twosum_naive.py`              | 22.19805 | 21.04922 | 20.40977 | 23.18945 | 23.99219 | 26.97148 | 27.28906 |
| `complex/classes/classes.py`                    | 21.84648 | 21.32461 | 20.16406 | 23.38437 | 25.03398 | 27.79258 | 28.24258 |
| `complex/classes/dataclasses_.py`               |       -- | 21.07969 | 20.49023 | 23.96367 | 24.89141 | 28.58086 | 28.08633 |
| `complex/classes/namedtuple_classes.py`         | 22.34883 | 21.14883 | 20.36484 | 23.33516 | 23.95781 | 27.67461 | 27.73008 |
| `complex/classes/simplenamespace.py`            | 21.85586 | 21.19687 |  20.4625 | 23.41484 | 25.81445 | 28.88008 | 28.94883 |
| `complex/classes/sloted_classes.py`             |  21.8668 | 21.19062 | 20.64609 | 23.42773 | 25.14648 | 28.37852 | 27.99141 |
| `complex/generators/simple.py`                  |     22.3 | 21.43164 | 20.48945 | 23.96289 | 25.31719 | 28.99922 | 29.58945 |
| `dummy/dummy.py`                                | 21.68203 | 20.94141 | 20.32891 | 23.39805 | 24.11523 | 26.50508 | 27.32031 |
| `long_run/database/postgresql.py`               | 27.20703 | 26.99531 | 24.31758 | 29.42969 | 29.32266 | 31.58242 | 32.68555 |
| `long_run/database/sqlite_.py`                  | 63.38945 | 66.54141 | 65.07109 | 67.40469 | 67.06094 | 72.47031 |       -- |
| `long_run/file/load_titanic_csv_pandas.py`      | 62.11406 | 64.83906 | 63.64687 | 66.00781 | 65.43438 | 70.47227 |       -- |
| `long_run/file/load_titanic_csv_python.py`      | 21.95313 | 21.33555 | 20.73633 |  23.1832 |   23.525 | 26.76367 | 27.82305 |
| `long_run/processes/collect_names_from_site.py` |       -- |       -- | 44.17812 | 45.23594 | 45.52852 | 47.36211 |       -- |
| `long_run/processes/generate_fake_data.py`      | 64.88398 | 69.96523 | 65.42148 | 69.80312 |  68.7918 | 71.90625 |       -- |
| `math/haversine.py`                             | 21.87305 | 21.15859 | 20.53086 | 22.88398 | 23.30273 |  26.9375 | 27.03945 |
| `math/mandelbrot.py`                            | 36.50781 | 35.70781 | 34.90391 | 41.98867 | 39.89062 | 40.65313 |       -- |
| `math/pow_simple.py`                            | 21.71875 |  21.0707 |  20.5207 | 22.92422 | 23.31758 | 26.91055 | 26.94102 |
| `math/pow_using_math.py`                        | 21.58438 |  21.0832 | 20.67148 | 23.39531 | 24.01328 | 26.45742 | 27.39531 |
| `modules/json/json_module.py`                   |  21.7582 | 22.24336 | 21.00078 | 23.40156 | 23.72969 | 26.60586 | 28.39922 |
| `modules/json/orjson_module.py`                 | 22.72852 | 22.53398 | 21.41289 | 24.09609 | 24.37656 | 27.53984 |       -- |
| `long_run/processes/maze_generator.py`          | 23.60117 | 27.12344 | 28.11523 |
| `long_run/text/count_words.py`                  | 23.70273 | 26.94414 |  27.4082 |

---

### **Python 3.6**

```bash
Python 3.6.15

Linux ada7fc6c5037 5.15.0-75-generic unknown GNU/Linux

CPU(s):                          12
Thread(s) per core:              2
Core(s) per socket:              6
NUMA node(s):                    1
Model name:                      Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:                     4100.0000
NUMA node0 CPU(s):               0-11

MemTotal:       16066528 kB
MemFree:         2146900 kB
MemAvailable:   14208020 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  1.47474 |    0.01581 |    1.47241 |  1.4576 | 1.51343 |    28.93555 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  1.49383 |    0.02176 |    1.50081 | 1.45868 | 1.52859 |    28.25703 |
| `algorithm/search/index.py`                     |      yes |  1.48493 |    0.01759 |    1.47896 | 1.46463 | 1.52314 |    29.14961 |
| `algorithm/search/linear.py`                    |      yes |  1.54328 |    0.02138 |    1.53877 | 1.52341 | 1.59972 |    28.90117 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.08477 |    0.00069 |    0.08482 |  0.0834 | 0.08584 |    22.28984 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.08483 |    0.00058 |    0.08465 | 0.08426 | 0.08626 |    22.19805 |
| `complex/classes/classes.py`                    |      yes |  0.04935 |    0.00426 |    0.04812 | 0.04757 | 0.06144 |    21.84648 |
| `complex/classes/dataclasses_.py`               |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.10016 |    0.00088 |        0.1 | 0.09881 | 0.10167 |    22.34883 |
| `complex/classes/simplenamespace.py`            |      yes |  0.06517 |    0.00097 |    0.06511 | 0.06381 | 0.06743 |    21.85586 |
| `complex/classes/sloted_classes.py`             |      yes |  0.04834 |    0.00051 |    0.04841 | 0.04737 |   0.049 |     21.8668 |
| `complex/generators/simple.py`                  |      yes |   0.0684 |    0.00032 |    0.06841 | 0.06798 | 0.06898 |        22.3 |
| `dummy/dummy.py`                                |      yes |  0.03471 |    0.00069 |    0.03442 | 0.03415 | 0.03635 |    21.68203 |
| `long_run/database/postgresql.py`               |      yes |  0.15418 |    0.00067 |    0.15392 | 0.15351 | 0.15582 |    27.20703 |
| `long_run/database/sqlite_.py`                  |      yes |  0.61977 |    0.00729 |    0.61722 | 0.61247 | 0.63343 |    63.38945 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |  0.69384 |    0.00758 |     0.6909 | 0.68671 | 0.71277 |    62.11406 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.07388 |    0.00037 |      0.074 | 0.07316 | 0.07433 |    21.95313 |
| `long_run/processes/collect_names_from_site.py` |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/processes/generate_fake_data.py`      |      yes |  0.85907 |    0.00627 |    0.85818 |  0.8515 | 0.86865 |    64.88398 |
| `math/haversine.py`                             |      yes |  0.83484 |    0.01959 |     0.8294 | 0.81189 | 0.86382 |    21.87305 |
| `math/mandelbrot.py`                            |      yes |  3.13033 |    0.06636 |    3.14387 | 2.94622 | 3.18743 |    36.50781 |
| `math/pow_simple.py`                            |      yes |  0.64288 |    0.01568 |    0.63428 | 0.63226 | 0.68073 |    21.71875 |
| `math/pow_using_math.py`                        |      yes |   1.4148 |    0.03817 |    1.40511 | 1.37411 |  1.4851 |    21.58438 |
| `modules/json/json_module.py`                   |      yes |  0.49616 |    0.00365 |      0.495 | 0.49181 | 0.50137 |     21.7582 |
| `modules/json/orjson_module.py`                 |      yes |  0.30412 |    0.00437 |    0.30241 | 0.29881 | 0.31176 |    22.72852 |

### **Python 3.7**

```bash
Python 3.7.17

Linux 5074941be326 5.15.0-75-generic unknown GNU/Linux

CPU(s):                          12
Model name:                      Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:              2
Core(s) per socket:              6
CPU max MHz:                     4100.0000
NUMA node(s):                    1
NUMA node0 CPU(s):               0-11

MemTotal:       16066528 kB
MemFree:         2117480 kB
MemAvailable:   14189400 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  1.44211 |    0.01977 |    1.43635 |  1.4238 | 1.48957 |    29.74219 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  1.45265 |     0.0156 |    1.44994 | 1.43518 | 1.49152 |       31.85 |
| `algorithm/search/index.py`                     |      yes |  1.46956 |    0.01894 |    1.46699 | 1.44648 |  1.5052 |    29.64531 |
| `algorithm/search/linear.py`                    |      yes |  1.50718 |    0.01304 |    1.50724 |  1.4851 | 1.52642 |    30.28867 |
| `algorithm/twosum/twosum.py`                    |      yes |   0.0693 |    0.00046 |    0.06946 | 0.06818 |  0.0698 |    21.18945 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.06899 |    0.00039 |    0.06903 | 0.06839 | 0.06949 |    21.04922 |
| `complex/classes/classes.py`                    |      yes |   0.0415 |    0.00087 |    0.04137 | 0.04079 | 0.04381 |    21.32461 |
| `complex/classes/dataclasses_.py`               |      yes |  0.10621 |    0.00192 |    0.10556 | 0.10413 | 0.10993 |    21.07969 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.08425 |    0.00186 |    0.08463 | 0.08152 | 0.08683 |    21.14883 |
| `complex/classes/simplenamespace.py`            |      yes |   0.0416 |    0.00038 |    0.04155 | 0.04102 | 0.04225 |    21.19687 |
| `complex/classes/sloted_classes.py`             |      yes |  0.04133 |    0.00048 |     0.0412 | 0.04071 | 0.04225 |    21.19062 |
| `complex/generators/simple.py`                  |      yes |  0.06394 |    0.00032 |    0.06407 | 0.06343 | 0.06434 |    21.43164 |
| `dummy/dummy.py`                                |      yes |  0.02696 |    0.00116 |    0.02659 | 0.02617 | 0.02977 |    20.94141 |
| `long_run/database/postgresql.py`               |      yes |  0.13924 |    0.00058 |    0.13918 | 0.13831 |  0.1401 |    26.99531 |
| `long_run/database/sqlite_.py`                  |      yes |  0.53919 |    0.00205 |    0.53843 | 0.53681 | 0.54216 |    66.54141 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |  0.59412 |    0.00685 |    0.59274 | 0.58594 | 0.60846 |    64.83906 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |   0.0675 |    0.00148 |    0.06679 | 0.06642 | 0.07087 |    21.33555 |
| `long_run/processes/collect_names_from_site.py` |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/processes/generate_fake_data.py`      |      yes |  0.78601 |    0.00642 |    0.78482 | 0.77719 | 0.79932 |    69.96523 |
| `math/haversine.py`                             |      yes |  0.93711 |    0.00866 |    0.93677 | 0.92356 | 0.95524 |    21.15859 |
| `math/mandelbrot.py`                            |      yes |  3.04159 |    0.09137 |    3.03643 | 2.82688 | 3.16776 |    35.70781 |
| `math/pow_simple.py`                            |      yes |  0.76632 |    0.01793 |    0.75684 | 0.75374 |  0.8053 |     21.0707 |
| `math/pow_using_math.py`                        |      yes |  1.62948 |    0.02662 |     1.6197 | 1.60373 | 1.68128 |     21.0832 |
| `modules/json/json_module.py`                   |      yes |  0.51299 |    0.01038 |    0.51146 | 0.50052 | 0.53963 |    22.24336 |
| `modules/json/orjson_module.py`                 |      yes |  0.26256 |    0.00471 |    0.26233 | 0.25709 |  0.2709 |    22.53398 |

### **Python 3.8**

```bash
Python 3.8.17

Linux c8fd54189328 5.15.0-75-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16066528 kB
MemFree:         1236612 kB
MemAvailable:    9840180 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  1.44844 |     0.0157 |    1.44251 | 1.43275 |  1.4757 |    28.51992 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  1.45073 |    0.01837 |    1.44703 | 1.42873 | 1.49609 |    29.53164 |
| `algorithm/search/index.py`                     |      yes |  1.47166 |    0.02819 |    1.46178 | 1.43617 | 1.52108 |    28.41523 |
| `algorithm/search/linear.py`                    |      yes |  1.51064 |    0.01894 |      1.507 |  1.4895 | 1.54583 |    28.53828 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.07851 |    0.00168 |    0.07798 | 0.07657 | 0.08154 |     20.2957 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.07716 |    0.00031 |    0.07721 | 0.07644 | 0.07752 |    20.40977 |
| `complex/classes/classes.py`                    |      yes |  0.04448 |     0.0004 |    0.04438 | 0.04381 | 0.04515 |    20.16406 |
| `complex/classes/dataclasses_.py`               |      yes |  0.11515 |    0.00046 |    0.11522 | 0.11434 |  0.1157 |    20.49023 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.09039 |    0.00063 |     0.0901 | 0.08974 | 0.09177 |    20.36484 |
| `complex/classes/simplenamespace.py`            |      yes |  0.04529 |    0.00037 |     0.0453 | 0.04472 |  0.0458 |     20.4625 |
| `complex/classes/sloted_classes.py`             |      yes |  0.04472 |    0.00021 |    0.04466 | 0.04449 | 0.04513 |    20.64609 |
| `complex/generators/simple.py`                  |      yes |  0.06414 |    0.00279 |    0.06324 | 0.06266 | 0.07203 |    20.48945 |
| `dummy/dummy.py`                                |      yes |  0.03088 |    0.00022 |    0.03086 | 0.03059 | 0.03131 |    20.32891 |
| `long_run/database/postgresql.py`               |      yes |  0.15745 |    0.00111 |    0.15735 | 0.15564 | 0.15925 |    24.31758 |
| `long_run/database/sqlite_.py`                  |      yes |  0.62214 |    0.00445 |    0.62133 | 0.61673 | 0.63013 |    65.07109 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |  0.66897 |    0.00133 |    0.66868 | 0.66754 | 0.67187 |    63.64687 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.07179 |    0.00035 |    0.07177 |  0.0713 | 0.07227 |    20.73633 |
| `long_run/processes/collect_names_from_site.py` |      yes |  1.87281 |    0.02755 |    1.86932 | 1.83091 | 1.92798 |    44.17812 |
| `long_run/processes/generate_fake_data.py`      |      yes |  0.88291 |     0.0542 |    0.84905 | 0.83816 | 0.98849 |    65.42148 |
| `math/haversine.py`                             |      yes |    0.839 |    0.00975 |    0.83773 | 0.82649 | 0.86103 |    20.53086 |
| `math/mandelbrot.py`                            |      yes |  3.19851 |    0.07322 |    3.22139 | 3.11481 | 3.33318 |    34.90391 |
| `math/pow_simple.py`                            |      yes |  0.60665 |    0.00305 |    0.60529 | 0.60343 | 0.61244 |     20.5207 |
| `math/pow_using_math.py`                        |      yes |  1.46903 |    0.01513 |    1.46223 | 1.45102 | 1.50393 |    20.67148 |
| `modules/json/json_module.py`                   |      yes |  0.50347 |    0.01036 |    0.49918 | 0.49341 | 0.52657 |    21.00078 |
| `modules/json/orjson_module.py`                 |      yes |  0.26581 |     0.0016 |    0.26532 | 0.26294 | 0.26834 |    21.41289 |

### **Python 3.9**

```bash
Python 3.9.17

Linux 8e7dbac20d94 5.15.0-75-generic unknown GNU/Linux

CPU(s):                          12
Model name:                      Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:              2
Core(s) per socket:              6
CPU max MHz:                     4100.0000
NUMA node(s):                    1
NUMA node0 CPU(s):               0-11

MemTotal:       16066528 kB
MemFree:         2099064 kB
MemAvailable:   14181788 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  1.40788 |     0.0151 |    1.40488 | 1.38707 | 1.44449 |    31.58359 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  1.40812 |    0.01264 |     1.4094 | 1.38648 | 1.42309 |    31.50742 |
| `algorithm/search/index.py`                     |      yes |  1.41747 |    0.00936 |     1.4157 | 1.40172 | 1.43245 |    31.45781 |
| `algorithm/search/linear.py`                    |      yes |  1.48321 |    0.03134 |    1.47744 | 1.45561 | 1.56881 |    31.94492 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.08693 |    0.00489 |    0.08542 | 0.08395 | 0.10059 |    23.25898 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.08739 |    0.00612 |    0.08553 | 0.08514 | 0.10481 |    23.18945 |
| `complex/classes/classes.py`                    |      yes |  0.04752 |    0.00163 |    0.04673 | 0.04639 | 0.05067 |    23.38437 |
| `complex/classes/dataclasses_.py`               |      yes |   0.1368 |    0.00126 |    0.13684 | 0.13461 | 0.13918 |    23.96367 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.09887 |     0.0004 |      0.099 | 0.09818 | 0.09946 |    23.33516 |
| `complex/classes/simplenamespace.py`            |      yes |  0.04937 |    0.00041 |    0.04945 |  0.0487 | 0.04992 |    23.41484 |
| `complex/classes/sloted_classes.py`             |      yes |  0.04698 |    0.00038 |    0.04685 | 0.04646 | 0.04764 |    23.42773 |
| `complex/generators/simple.py`                  |      yes |   0.0666 |    0.00037 |    0.06655 | 0.06608 | 0.06731 |    23.96289 |
| `dummy/dummy.py`                                |      yes |  0.03393 |    0.00184 |    0.03286 | 0.03232 | 0.03687 |    23.39805 |
| `long_run/database/postgresql.py`               |      yes |  0.16816 |    0.00069 |    0.16793 | 0.16739 |  0.1695 |    29.42969 |
| `long_run/database/sqlite_.py`                  |      yes |  0.65553 |    0.00772 |    0.65637 | 0.64528 | 0.67103 |    67.40469 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |  0.70655 |    0.01541 |    0.69862 | 0.69245 | 0.73995 |    66.00781 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.07797 |    0.00059 |    0.07795 | 0.07731 | 0.07897 |     23.1832 |
| `long_run/processes/collect_names_from_site.py` |      yes |  2.08882 |     0.0216 |    2.09057 | 2.04885 | 2.12772 |    45.23594 |
| `long_run/processes/generate_fake_data.py`      |      yes |   0.8825 |    0.01113 |    0.87833 | 0.87205 | 0.90853 |    69.80312 |
| `math/haversine.py`                             |      yes |  1.00187 |    0.02796 |    1.00082 | 0.96998 | 1.06247 |    22.88398 |
| `math/mandelbrot.py`                            |      yes |  2.62146 |    0.04571 |    2.59625 | 2.58842 | 2.70294 |    41.98867 |
| `math/pow_simple.py`                            |      yes |  0.78799 |    0.01112 |    0.78338 |  0.7799 | 0.81634 |    22.92422 |
| `math/pow_using_math.py`                        |      yes |  1.43937 |      0.057 |    1.42052 |  1.3811 | 1.52807 |    23.39531 |
| `modules/json/json_module.py`                   |      yes |  0.50892 |    0.00761 |    0.50712 | 0.50108 | 0.52213 |    23.40156 |
| `modules/json/orjson_module.py`                 |      yes |  0.28736 |     0.0037 |    0.28682 | 0.28161 | 0.29529 |    24.09609 |

### **Python 3.10**

```bash
Python 3.10.12

Linux aa3f419585e8 5.15.0-75-generic unknown GNU/Linux

CPU(s):                          12
Model name:                      Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:              2
Core(s) per socket:              6
CPU max MHz:                     4100.0000
NUMA node(s):                    1
NUMA node0 CPU(s):               0-11

MemTotal:       16066528 kB
MemFree:         7872612 kB
MemAvailable:   14321404 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  1.23186 |    0.00527 |    1.23264 | 1.22238 |  1.2383 |    33.47383 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  1.24564 |    0.03579 |    1.23544 | 1.21689 | 1.34439 |     32.8625 |
| `algorithm/search/index.py`                     |      yes |   1.2518 |    0.01794 |    1.25027 | 1.22994 | 1.28882 |    32.61289 |
| `algorithm/search/linear.py`                    |      yes |  1.30064 |     0.0283 |    1.29471 | 1.27531 | 1.36621 |    32.63281 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.07851 |    0.00055 |    0.07844 | 0.07775 | 0.07969 |    23.57344 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.07829 |    0.00048 |    0.07828 | 0.07753 | 0.07903 |    23.99219 |
| `complex/classes/classes.py`                    |      yes |  0.04335 |    0.00123 |    0.04301 | 0.04238 | 0.04637 |    25.03398 |
| `complex/classes/dataclasses_.py`               |      yes |   0.1231 |    0.00066 |    0.12317 | 0.12223 | 0.12423 |    24.89141 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.09041 |    0.00046 |    0.09048 | 0.08963 | 0.09091 |    23.95781 |
| `complex/classes/simplenamespace.py`            |      yes |  0.04504 |    0.00058 |    0.04481 | 0.04461 | 0.04637 |    25.81445 |
| `complex/classes/sloted_classes.py`             |      yes |  0.04249 |    0.00034 |    0.04247 | 0.04201 | 0.04315 |    25.14648 |
| `complex/generators/simple.py`                  |      yes |  0.06209 |    0.00108 |    0.06182 | 0.06095 | 0.06433 |    25.31719 |
| `dummy/dummy.py`                                |      yes |  0.03033 |    0.00055 |    0.03005 | 0.02971 | 0.03115 |    24.11523 |
| `long_run/database/postgresql.py`               |      yes |    0.155 |     0.0004 |    0.15485 | 0.15455 | 0.15566 |    29.32266 |
| `long_run/database/sqlite_.py`                  |      yes |  0.61012 |    0.00584 |    0.60756 | 0.60425 | 0.62055 |    67.06094 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |  0.65075 |    0.00642 |    0.64782 | 0.64595 | 0.66549 |    65.43438 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.06951 |    0.00045 |    0.06958 | 0.06873 | 0.07006 |      23.525 |
| `long_run/processes/collect_names_from_site.py` |      yes |  2.04696 |    0.03135 |    2.03481 | 2.00009 | 2.10912 |    45.52852 |
| `long_run/processes/generate_fake_data.py`      |      yes |   0.8271 |     0.0101 |    0.82399 | 0.81705 | 0.84567 |     68.7918 |
| `long_run/processes/maze_generator.py`          |      yes |   0.2022 |    0.01397 |    0.20024 | 0.18035 | 0.23352 |    23.60117 |
| `long_run/text/count_words.py`                  |      yes |  0.07421 |     0.0005 |    0.07427 | 0.07347 | 0.07508 |    23.70273 |
| `math/haversine.py`                             |      yes |  0.91088 |    0.01459 |    0.90403 | 0.89351 | 0.93487 |    23.30273 |
| `math/mandelbrot.py`                            |      yes |  2.57208 |    0.00605 |    2.57099 |  2.5658 | 2.58661 |    39.89062 |
| `math/pow_simple.py`                            |      yes |  0.69776 |    0.01768 |    0.68838 | 0.68486 | 0.72899 |    23.31758 |
| `math/pow_using_math.py`                        |      yes |  1.39881 |    0.03668 |    1.39592 | 1.34892 | 1.46753 |    24.01328 |
| `modules/json/json_module.py`                   |      yes |  0.43996 |    0.00672 |    0.43861 | 0.43275 | 0.45523 |    23.72969 |
| `modules/json/orjson_module.py`                 |      yes |  0.25996 |    0.00151 |    0.25974 | 0.25762 |  0.2626 |    24.37656 |

### **Python 3.11**

```bash
Python 3.11.4

Linux b6d85464a0d0 5.15.0-75-generic unknown GNU/Linux

CPU(s):                          12
Model name:                      Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:              2
Core(s) per socket:              6
CPU max MHz:                     4100.0000
NUMA node(s):                    1
NUMA node0 CPU(s):               0-11

MemTotal:       16066528 kB
MemFree:         7807628 kB
MemAvailable:   14316520 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  1.05539 |    0.00679 |    1.05407 | 1.04442 | 1.06505 |    35.95195 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  1.05607 |    0.00968 |    1.05482 | 1.04443 | 1.07092 |    36.61563 |
| `algorithm/search/index.py`                     |      yes |  1.08126 |    0.01219 |    1.07967 | 1.06773 | 1.10446 |    35.89336 |
| `algorithm/search/linear.py`                    |      yes |  1.12027 |    0.02017 |    1.12192 | 1.08948 | 1.15061 |    36.10742 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.07427 |    0.00065 |    0.07426 | 0.07328 | 0.07543 |    26.47695 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.07468 |    0.00299 |    0.07346 | 0.07307 | 0.08274 |    26.97148 |
| `complex/classes/classes.py`                    |      yes |  0.02148 |    0.00023 |    0.02147 | 0.02104 | 0.02182 |    27.79258 |
| `complex/classes/dataclasses_.py`               |      yes |  0.11543 |    0.00136 |    0.11532 | 0.11336 | 0.11874 |    28.58086 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.08439 |    0.00049 |     0.0844 | 0.08372 | 0.08519 |    27.67461 |
| `complex/classes/simplenamespace.py`            |      yes |  0.02649 |    0.00035 |    0.02657 | 0.02592 | 0.02713 |    28.88008 |
| `complex/classes/sloted_classes.py`             |      yes |  0.02078 |    0.00027 |    0.02081 | 0.02032 | 0.02116 |    28.37852 |
| `complex/generators/simple.py`                  |      yes |  0.04103 |    0.00034 |    0.04111 | 0.04047 | 0.04142 |    28.99922 |
| `dummy/dummy.py`                                |      yes |  0.01443 |    0.00258 |     0.0142 | 0.01214 |  0.0205 |    26.50508 |
| `long_run/database/postgresql.py`               |      yes |  0.15275 |    0.00124 |    0.15318 | 0.15004 | 0.15402 |    31.58242 |
| `long_run/database/sqlite_.py`                  |      yes |  0.62061 |    0.00526 |    0.61903 | 0.61505 | 0.63228 |    72.47031 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |  0.64379 |    0.00192 |    0.64354 | 0.64134 | 0.64797 |    70.47227 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.05892 |    0.00041 |    0.05883 | 0.05849 | 0.05973 |    26.76367 |
| `long_run/processes/collect_names_from_site.py` |      yes |  1.75078 |    0.02393 |    1.75564 | 1.71201 | 1.78703 |    47.36211 |
| `long_run/processes/generate_fake_data.py`      |      yes |  0.80923 |    0.00201 |    0.80933 | 0.80555 |  0.8123 |    71.90625 |
| `long_run/processes/maze_generator.py`          |      yes |  0.13154 |    0.00734 |    0.13252 | 0.12001 | 0.14208 |    27.12344 |
| `long_run/text/count_words.py`                  |      yes |  0.06284 |    0.00052 |    0.06276 | 0.06203 | 0.06406 |    26.94414 |
| `math/haversine.py`                             |      yes |  0.79309 |     0.0152 |    0.78699 | 0.77596 | 0.81627 |     26.9375 |
| `math/mandelbrot.py`                            |      yes |  2.58225 |    0.04003 |    2.56146 | 2.55744 | 2.67042 |    40.65313 |
| `math/pow_simple.py`                            |      yes |  0.35086 |    0.01184 |    0.34677 | 0.34621 | 0.38436 |    26.91055 |
| `math/pow_using_math.py`                        |      yes |  1.17832 |    0.03046 |    1.16956 | 1.14624 | 1.22656 |    26.45742 |
| `modules/json/json_module.py`                   |      yes |  0.40549 |    0.00828 |    0.40293 | 0.39566 | 0.41815 |    26.60586 |
| `modules/json/orjson_module.py`                 |      yes |  0.21091 |    0.00224 |     0.2102 | 0.20876 | 0.21511 |    27.53984 |

### **Python 3.12**

```bash
Python 3.12.0b3

Linux e42c07ab55f0 5.15.0-75-generic unknown GNU/Linux

CPU(s):                          12
Model name:                      Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:              2
Core(s) per socket:              6
CPU max MHz:                     4100.0000
NUMA node(s):                    1
NUMA node0 CPU(s):               0-11

MemTotal:       16066528 kB
MemFree:         7788824 kB
MemAvailable:   14308500 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  1.15522 |    0.01416 |    1.15378 | 1.13849 | 1.17838 |    35.53633 |
| `algorithm/search/hashmap_lookup.py`            |      yes |   1.1637 |    0.01226 |    1.16155 | 1.14601 |  1.1835 |    36.20234 |
| `algorithm/search/index.py`                     |      yes |  1.17608 |    0.01049 |    1.17482 | 1.16482 | 1.19802 |     35.4293 |
| `algorithm/search/linear.py`                    |      yes |  1.22731 |    0.01165 |    1.23094 | 1.21097 | 1.24628 |    35.67109 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.08386 |    0.00032 |    0.08384 | 0.08351 | 0.08447 |    27.53242 |
| `algorithm/twosum/twosum_naive.py`              |      yes |   0.0831 |    0.00031 |    0.08314 | 0.08253 | 0.08356 |    27.28906 |
| `complex/classes/classes.py`                    |      yes |  0.02267 |    0.00061 |    0.02247 | 0.02208 |  0.0239 |    28.24258 |
| `complex/classes/dataclasses_.py`               |      yes |  0.13161 |    0.00067 |    0.13155 | 0.13076 | 0.13259 |    28.08633 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.09658 |    0.00063 |    0.09643 | 0.09543 | 0.09775 |    27.73008 |
| `complex/classes/simplenamespace.py`            |      yes |  0.02928 |    0.00119 |    0.02902 | 0.02823 | 0.03239 |    28.94883 |
| `complex/classes/sloted_classes.py`             |      yes |  0.02155 |    0.00022 |    0.02152 | 0.02133 | 0.02208 |    27.99141 |
| `complex/generators/simple.py`                  |      yes |  0.04548 |    0.00042 |     0.0454 | 0.04497 |  0.0462 |    29.58945 |
| `dummy/dummy.py`                                |      yes |  0.01658 |    0.00514 |    0.01388 | 0.01327 | 0.02618 |    27.32031 |
| `long_run/database/postgresql.py`               |      yes |   0.1758 |    0.00218 |    0.17493 | 0.17395 |  0.1808 |    32.68555 |
| `long_run/database/sqlite_.py`                  |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/file/load_titanic_csv_pandas.py`      |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.06666 |    0.00039 |    0.06663 | 0.06607 | 0.06732 |    27.82305 |
| `long_run/processes/collect_names_from_site.py` |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/processes/generate_fake_data.py`      |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/processes/maze_generator.py`          |      yes |  0.13631 |    0.00572 |    0.13526 | 0.12932 | 0.14359 |    28.11523 |
| `long_run/text/count_words.py`                  |      yes |  0.06893 |    0.00065 |    0.06876 |  0.0683 | 0.07049 |     27.4082 |
| `math/haversine.py`                             |      yes |  0.87822 |    0.02456 |    0.86865 | 0.85592 | 0.92989 |    27.03945 |
| `math/mandelbrot.py`                            |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `math/pow_simple.py`                            |      yes |  0.33479 |    0.03386 |      0.325 |  0.3059 | 0.39784 |    26.94102 |
| `math/pow_using_math.py`                        |      yes |  1.21228 |    0.04045 |    1.20144 | 1.17593 | 1.32019 |    27.39531 |
| `modules/json/json_module.py`                   |      yes |  0.40394 |    0.00546 |    0.40483 | 0.39398 | 0.40986 |    28.39922 |
| `modules/json/orjson_module.py`                 |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
