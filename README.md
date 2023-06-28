# Python Benchmark

This is a simple repo to validate and test any (almost any) python program againts all python 3 versions.

- Python 3.6.15
- Python 3.7.16
- Python 3.8.16
- Python 3.9.16
- Python 3.10.11
- Python 3.11.3
- Python 3.12b3

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

> Last run: Wed Jun 28 12:05:15 AM -03 2023

### **Comparison**

#### How much faster 3.12 is? (Mean / Median from 3.6 to 3.11)

| Command                                         |               3.6 |               3.7 |               3.8 |               3.9 |              3.10 |              3.11 |
| :---------------------------------------------- | ----------------: | ----------------: | ----------------: | ----------------: | ----------------: | ----------------: |
| `algorithm/search/bin.py`                       |   27.00% / 27.23% |   24.19% / 24.12% |   24.73% / 24.65% |   21.24% / 21.40% |     6.23% / 6.09% |   -9.99% / -9.75% |
| `algorithm/search/hashmap_lookup.py`            |   27.61% / 30.05% |   24.09% / 25.64% |   23.93% / 25.39% |   20.29% / 22.13% |     5.12% / 6.61% |   -9.57% / -9.06% |
| `algorithm/search/index.py`                     |   26.20% / 25.90% |   24.89% / 24.88% |   25.07% / 24.44% |   20.46% / 20.51% |     6.51% / 6.21% |   -9.75% / -9.70% |
| `algorithm/search/linear.py`                    |   24.20% / 24.67% |   21.30% / 22.12% |   21.57% / 22.10% |   19.37% / 19.70% |     4.12% / 4.40% | -10.29% / -10.38% |
| `algorithm/twosum/twosum.py`                    |     1.04% / 1.17% | -17.40% / -17.15% |   -6.42% / -6.99% |     3.61% / 1.88% |   -6.22% / -6.14% | -11.49% / -11.41% |
| `algorithm/twosum/twosum_naive.py`              |    -0.01% / 1.09% | -18.68% / -17.57% |   -9.05% / -7.80% |     3.01% / 2.14% |   -7.66% / -6.36% | -13.04% / -12.10% |
| `complex/classes/classes.py`                    | 122.70% / 117.44% |   87.27% / 86.94% | 100.72% / 100.54% | 114.44% / 111.16% |   92.28% / 92.00% |   -5.01% / -4.93% |
| `complex/classes/dataclasses_.py`               |           -- / -- | -19.02% / -19.55% | -12.21% / -12.19% |     4.30% / 4.28% |   -6.08% / -6.41% | -13.18% / -13.21% |
| `complex/classes/namedtuple_classes.py`         |     4.36% / 4.19% | -12.22% / -11.83% |   -5.82% / -6.13% |     3.01% / 3.15% |   -5.59% / -5.54% | -12.00% / -11.92% |
| `complex/classes/simplenamespace.py`            | 128.11% / 128.14% |   45.61% / 45.59% |   58.52% / 58.72% |   72.80% / 73.27% |   61.11% / 58.02% |   -6.97% / -7.15% |
| `complex/classes/sloted_classes.py`             | 101.92% / 117.48% |   72.64% / 85.09% |  86.80% / 100.63% |  96.24% / 110.47% |   79.37% / 92.72% |   -7.23% / -4.45% |
| `complex/generators/simple.py`                  |   48.95% / 49.73% |   39.24% / 40.23% |   39.68% / 38.41% |   45.03% / 45.66% |   34.95% / 35.63% | -11.69% / -11.42% |
| `dummy/dummy.py`                                | 100.29% / 128.10% |   55.57% / 76.21% |  78.19% / 104.51% |  95.79% / 117.76% |  78.65% / 103.78% |   -12.69% / 4.77% |
| `long_run/database/postgresql.py`               | -11.33% / -11.41% | -19.92% / -19.89% |   -9.45% / -9.43% |   -3.29% / -3.34% | -12.01% / -11.79% | -13.34% / -13.23% |
| `long_run/database/sqlite_.py`                  |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `long_run/file/load_titanic_csv_pandas.py`      |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `long_run/file/load_titanic_csv_python.py`      |   11.53% / 12.34% |     1.90% / 1.40% |     8.38% / 8.96% |   17.71% / 18.34% |     5.74% / 6.16% |  -10.36% / -9.81% |
| `long_run/processes/collect_names_from_site.py` |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `long_run/processes/generate_fake_data.py`      |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `math/haversine.py`                             |   -3.46% / -3.28% |     8.36% / 9.24% |   -2.98% / -2.31% |   15.85% / 16.71% |     5.57% / 6.45% |   -5.84% / -5.63% |
| `math/mandelbrot.py`                            |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `math/pow_simple.py`                            | 106.89% / 106.35% | 146.61% / 146.22% |   95.23% / 96.92% | 153.58% / 154.86% | 123.30% / 124.63% |   11.78% / 13.11% |
| `math/pow_using_math.py`                        |   16.70% / 16.43% |   34.41% / 34.21% |   21.18% / 21.16% |   18.73% / 17.70% |   13.44% / 13.25% |   -3.48% / -4.02% |
| `modules/json/json_module.py`                   |   23.35% / 23.37% |   27.53% / 27.47% |   25.16% / 24.41% |   26.52% / 26.39% |     9.74% / 9.30% |   -1.12% / -0.88% |
| `modules/json/orjson_module.py`                 |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |

---

#### How much more memory 3.12 uses? (Memory diff from 3.6 to 3.11)

| Command                                         |    3.6 |    3.7 |    3.8 |    3.9 |   3.10 |   3.11 |
| :---------------------------------------------- | -----: | -----: | -----: | -----: | -----: | -----: |
| `algorithm/search/bin.py`                       |  23.2% | 19.86% |  25.0% | 12.87% |  8.95% | -0.29% |
| `algorithm/search/hashmap_lookup.py`            | 28.09% | 13.64% | 22.56% | 14.88% |  8.92% | -0.94% |
| `algorithm/search/index.py`                     | 22.39% | 20.34% | 25.55% | 13.41% |  9.28% |  0.33% |
| `algorithm/search/linear.py`                    | 23.22% | 17.57% | 24.79% | 11.48% |  9.36% |  1.65% |
| `algorithm/twosum/twosum.py`                    |  23.6% | 30.02% | 35.75% | 18.45% | 16.81% |  3.82% |
| `algorithm/twosum/twosum_naive.py`              | 23.63% | 30.38% | 34.47% | 18.35% | 14.25% |  1.88% |
| `complex/classes/classes.py`                    | 29.33% | 32.49% | 40.12% | 20.82% | 11.79% |  2.86% |
| `complex/classes/dataclasses_.py`               |     -- | 33.42% | 37.26% | 17.37% | 12.12% | -1.55% |
| `complex/classes/namedtuple_classes.py`         | 23.93% | 30.97% | 36.01% | 18.69% | 15.42% | -0.24% |
| `complex/classes/simplenamespace.py`            | 32.58% | 36.71% | 41.61% | 23.76% | 13.68% |  0.94% |
| `complex/classes/sloted_classes.py`             | 27.56% | 31.63% |  35.1% | 19.06% | 10.63% | -1.91% |
| `complex/generators/simple.py`                  | 32.43% |  37.8% | 44.14% | 23.24% | 16.96% |  1.73% |
| `dummy/dummy.py`                                | 26.05% | 30.51% | 34.45% | 16.81% |  13.9% |  3.28% |
| `long_run/database/postgresql.py`               | 20.14% | 21.08% | 34.41% | 11.06% | 11.91% |  3.02% |
| `long_run/database/sqlite_.py`                  |     -- |     -- |     -- |     -- |     -- |     -- |
| `long_run/file/load_titanic_csv_pandas.py`      |     -- |     -- |     -- |     -- |     -- |     -- |
| `long_run/file/load_titanic_csv_python.py`      |  26.9% | 30.57% | 34.34% | 20.17% | 18.12% |  3.95% |
| `long_run/processes/collect_names_from_site.py` |     -- |     -- |     -- |     -- |     -- |     -- |
| `long_run/processes/generate_fake_data.py`      |     -- |     -- |     -- |     -- |     -- |     -- |
| `math/haversine.py`                             | 23.78% | 27.95% | 31.87% | 18.31% | 16.12% |  0.57% |
| `math/mandelbrot.py`                            |     -- |     -- |     -- |     -- |     -- |     -- |
| `math/pow_simple.py`                            |  23.9% | 27.71% | 31.13% | 17.38% | 15.71% | -0.08% |
| `math/pow_using_math.py`                        | 27.44% | 30.47% | 33.07% | 17.57% | 13.84% |  3.77% |
| `modules/json/json_module.py`                   | 30.84% | 27.99% | 35.56% | 21.65% | 20.03% |  7.02% |
| `modules/json/orjson_module.py`                 |     -- |     -- |     -- |     -- |     -- |     -- |

---

#### **Execution**

##### **Mean [s]**

| Command                                         |     3.6 |     3.7 |     3.8 |     3.9 |    3.10 |    3.11 |    3.12 |
| :---------------------------------------------- | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| `algorithm/search/bin.py`                       | 1.47474 | 1.44211 | 1.44844 | 1.40788 | 1.23354 | 1.04527 | 1.16124 |
| `algorithm/search/hashmap_lookup.py`            | 1.49383 | 1.45265 | 1.45073 | 1.40812 | 1.23051 | 1.05858 | 1.17061 |
| `algorithm/search/index.py`                     | 1.48493 | 1.46956 | 1.47166 | 1.41747 | 1.25322 | 1.06199 | 1.17667 |
| `algorithm/search/linear.py`                    | 1.54328 | 1.50718 | 1.51064 | 1.48321 |  1.2938 | 1.11471 | 1.24256 |
| `algorithm/twosum/twosum.py`                    | 0.08477 |  0.0693 | 0.07851 | 0.08693 | 0.07868 | 0.07426 |  0.0839 |
| `algorithm/twosum/twosum_naive.py`              | 0.08483 | 0.06899 | 0.07716 | 0.08739 | 0.07834 | 0.07378 | 0.08484 |
| `complex/classes/classes.py`                    | 0.04935 |  0.0415 | 0.04448 | 0.04752 | 0.04261 | 0.02105 | 0.02216 |
| `complex/classes/dataclasses_.py`               |      -- | 0.10621 | 0.11515 |  0.1368 | 0.12318 | 0.11387 | 0.13116 |
| `complex/classes/namedtuple_classes.py`         | 0.10016 | 0.08425 | 0.09039 | 0.09887 | 0.09061 | 0.08446 | 0.09598 |
| `complex/classes/simplenamespace.py`            | 0.06517 |  0.0416 | 0.04529 | 0.04937 | 0.04603 | 0.02658 | 0.02857 |
| `complex/classes/sloted_classes.py`             | 0.04834 | 0.04133 | 0.04472 | 0.04698 | 0.04294 | 0.02221 | 0.02394 |
| `complex/generators/simple.py`                  |  0.0684 | 0.06394 | 0.06414 |  0.0666 | 0.06197 | 0.04055 | 0.04592 |
| `dummy/dummy.py`                                | 0.03471 | 0.02696 | 0.03088 | 0.03393 | 0.03096 | 0.01513 | 0.01733 |
| `long_run/database/postgresql.py`               | 0.15418 | 0.13924 | 0.15745 | 0.16816 | 0.15299 | 0.15069 | 0.17388 |
| `long_run/database/sqlite_.py`                  | 0.61977 | 0.53919 | 0.62214 | 0.65553 | 0.60779 | 0.61518 |      -- |
| `long_run/file/load_titanic_csv_pandas.py`      | 0.69384 | 0.59412 | 0.66897 | 0.70655 |   0.654 | 0.64223 |      -- |
| `long_run/file/load_titanic_csv_python.py`      | 0.07388 |  0.0675 | 0.07179 | 0.07797 | 0.07004 | 0.05938 | 0.06624 |
| `long_run/processes/collect_names_from_site.py` |      -- |      -- | 1.87281 | 2.08882 | 2.00921 | 1.71591 |      -- |
| `long_run/processes/generate_fake_data.py`      | 0.85907 | 0.78601 | 0.88291 |  0.8825 | 0.82615 | 0.81496 |      -- |
| `math/haversine.py`                             | 0.83484 | 0.93711 |   0.839 | 1.00187 | 0.91301 | 0.81429 |  0.8648 |
| `math/mandelbrot.py`                            | 3.13033 | 3.04159 | 3.19851 | 2.62146 | 2.58455 | 2.57773 |      -- |
| `math/pow_simple.py`                            | 0.64288 | 0.76632 | 0.60665 | 0.78799 | 0.69387 | 0.34734 | 0.31074 |
| `math/pow_using_math.py`                        |  1.4148 | 1.62948 | 1.46903 | 1.43937 | 1.37529 | 1.17012 | 1.21232 |
| `modules/json/json_module.py`                   | 0.49616 | 0.51299 | 0.50347 | 0.50892 | 0.44142 | 0.39774 | 0.40225 |
| `modules/json/orjson_module.py`                 | 0.30412 | 0.26256 | 0.26581 | 0.28736 | 0.26129 | 0.21073 |      -- |

##### **Median [s]**

| Command                                         |     3.6 |     3.7 |     3.8 |     3.9 |    3.10 |    3.11 |    3.12 |
| :---------------------------------------------- | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| `algorithm/search/bin.py`                       | 1.47241 | 1.43635 | 1.44251 | 1.40488 | 1.22766 | 1.04436 | 1.15724 |
| `algorithm/search/hashmap_lookup.py`            | 1.50081 | 1.44994 | 1.44703 |  1.4094 | 1.23031 | 1.04944 | 1.15403 |
| `algorithm/search/index.py`                     | 1.47896 | 1.46699 | 1.46178 |  1.4157 | 1.24767 | 1.06073 | 1.17472 |
| `algorithm/search/linear.py`                    | 1.53877 | 1.50724 |   1.507 | 1.47744 | 1.28854 | 1.10618 | 1.23424 |
| `algorithm/twosum/twosum.py`                    | 0.08482 | 0.06946 | 0.07798 | 0.08542 | 0.07869 | 0.07427 | 0.08384 |
| `algorithm/twosum/twosum_naive.py`              | 0.08465 | 0.06903 | 0.07721 | 0.08553 | 0.07841 | 0.07361 | 0.08374 |
| `complex/classes/classes.py`                    | 0.04812 | 0.04137 | 0.04438 | 0.04673 | 0.04249 | 0.02104 | 0.02213 |
| `complex/classes/dataclasses_.py`               |      -- | 0.10556 | 0.11522 | 0.13684 | 0.12281 | 0.11389 | 0.13122 |
| `complex/classes/namedtuple_classes.py`         |     0.1 | 0.08463 |  0.0901 |   0.099 | 0.09066 | 0.08454 | 0.09598 |
| `complex/classes/simplenamespace.py`            | 0.06511 | 0.04155 |  0.0453 | 0.04945 |  0.0451 |  0.0265 | 0.02854 |
| `complex/classes/sloted_classes.py`             | 0.04841 |  0.0412 | 0.04466 | 0.04685 |  0.0429 | 0.02127 | 0.02226 |
| `complex/generators/simple.py`                  | 0.06841 | 0.06407 | 0.06324 | 0.06655 | 0.06197 | 0.04047 | 0.04569 |
| `dummy/dummy.py`                                | 0.03442 | 0.02659 | 0.03086 | 0.03286 | 0.03075 | 0.01581 | 0.01509 |
| `long_run/database/postgresql.py`               | 0.15392 | 0.13918 | 0.15735 | 0.16793 | 0.15325 | 0.15075 | 0.17374 |
| `long_run/database/sqlite_.py`                  | 0.61722 | 0.53843 | 0.62133 | 0.65637 | 0.60691 | 0.61517 |      -- |
| `long_run/file/load_titanic_csv_pandas.py`      |  0.6909 | 0.59274 | 0.66868 | 0.69862 | 0.65318 | 0.64247 |      -- |
| `long_run/file/load_titanic_csv_python.py`      |   0.074 | 0.06679 | 0.07177 | 0.07795 | 0.06993 | 0.05941 | 0.06587 |
| `long_run/processes/collect_names_from_site.py` |      -- |      -- | 1.86932 | 2.09057 | 2.00398 | 1.71392 |      -- |
| `long_run/processes/generate_fake_data.py`      | 0.85818 | 0.78482 | 0.84905 | 0.87833 | 0.82492 | 0.81338 |      -- |
| `math/haversine.py`                             |  0.8294 | 0.93677 | 0.83773 | 1.00082 | 0.91284 | 0.80926 | 0.85751 |
| `math/mandelbrot.py`                            | 3.14387 | 3.03643 | 3.22139 | 2.59625 | 2.57175 | 2.56705 |      -- |
| `math/pow_simple.py`                            | 0.63428 | 0.75684 | 0.60529 | 0.78338 | 0.69046 | 0.34767 | 0.30738 |
| `math/pow_using_math.py`                        | 1.40511 |  1.6197 | 1.46223 | 1.42052 | 1.36682 | 1.15837 | 1.20686 |
| `modules/json/json_module.py`                   |   0.495 | 0.51146 | 0.49918 | 0.50712 | 0.43855 | 0.39771 | 0.40124 |
| `modules/json/orjson_module.py`                 | 0.30241 | 0.26233 | 0.26532 | 0.28682 | 0.26091 | 0.21009 |      -- |

#### **Memory Usage**

##### **MEM [MB]**

| Command                                         |      3.6 |      3.7 |      3.8 |      3.9 |     3.10 |     3.11 |     3.12 |
| :---------------------------------------------- | -------: | -------: | -------: | -------: | -------: | -------: | -------: |
| `algorithm/search/bin.py`                       | 28.93555 | 29.74219 | 28.51992 | 31.58359 | 32.71992 | 35.75234 | 35.64883 |
| `algorithm/search/hashmap_lookup.py`            | 28.25703 |    31.85 | 29.53164 | 31.50742 | 33.22891 | 36.53945 | 36.19453 |
| `algorithm/search/index.py`                     | 29.14961 | 29.64531 | 28.41523 | 31.45781 | 32.64687 |  35.5582 | 35.67656 |
| `algorithm/search/linear.py`                    | 28.90117 | 30.28867 | 28.53828 | 31.94492 | 32.56289 | 35.03359 | 35.61172 |
| `algorithm/twosum/twosum.py`                    | 22.28984 | 21.18945 |  20.2957 | 23.25898 | 23.58555 | 26.53828 | 27.55117 |
| `algorithm/twosum/twosum_naive.py`              | 22.19805 | 21.04922 | 20.40977 | 23.18945 | 24.02031 | 26.93672 | 27.44414 |
| `complex/classes/classes.py`                    | 21.84648 | 21.32461 | 20.16406 | 23.38437 |   25.275 | 27.46914 | 28.25391 |
| `complex/classes/dataclasses_.py`               |       -- | 21.07969 | 20.49023 | 23.96367 | 25.08516 |  28.5668 |   28.125 |
| `complex/classes/namedtuple_classes.py`         | 22.34883 | 21.14883 | 20.36484 | 23.33516 | 23.99805 | 27.76445 | 27.69766 |
| `complex/classes/simplenamespace.py`            | 21.85586 | 21.19687 |  20.4625 | 23.41484 | 25.49102 | 28.70625 | 28.97734 |
| `complex/classes/sloted_classes.py`             |  21.8668 | 21.19062 | 20.64609 | 23.42773 | 25.21328 | 28.43594 | 27.89336 |
| `complex/generators/simple.py`                  |     22.3 | 21.43164 | 20.48945 | 23.96289 | 25.25078 | 29.03086 | 29.53281 |
| `dummy/dummy.py`                                | 21.68203 | 20.94141 | 20.32891 | 23.39805 | 23.99609 | 26.46445 | 27.33125 |
| `long_run/database/postgresql.py`               | 27.20703 | 26.99531 | 24.31758 | 29.42969 |  29.2082 | 31.72734 | 32.68555 |
| `long_run/database/sqlite_.py`                  | 63.38945 | 66.54141 | 65.07109 | 67.40469 | 67.25625 | 72.79336 |       -- |
| `long_run/file/load_titanic_csv_pandas.py`      | 62.11406 | 64.83906 | 63.64687 | 66.00781 | 65.89805 | 70.82695 |       -- |
| `long_run/file/load_titanic_csv_python.py`      | 21.95313 | 21.33555 | 20.73633 |  23.1832 | 23.58437 | 26.80078 |  27.8582 |
| `long_run/processes/collect_names_from_site.py` |       -- |       -- | 44.17812 | 45.23594 | 45.53008 | 47.49336 |       -- |
| `long_run/processes/generate_fake_data.py`      | 64.88398 | 69.96523 | 65.42148 | 69.80312 | 68.89102 | 72.43555 |       -- |
| `math/haversine.py`                             | 21.87305 | 21.15859 | 20.53086 | 22.88398 | 23.31445 | 26.91914 | 27.07344 |
| `math/mandelbrot.py`                            | 36.50781 | 35.70781 | 34.90391 | 41.98867 | 41.02539 | 40.82617 |       -- |
| `math/pow_simple.py`                            | 21.71875 |  21.0707 |  20.5207 | 22.92422 | 23.25625 | 26.92969 | 26.90938 |
| `math/pow_using_math.py`                        | 21.58438 |  21.0832 | 20.67148 | 23.39531 | 24.16211 | 26.50664 | 27.50664 |
| `modules/json/json_module.py`                   |  21.7582 | 22.24336 | 21.00078 | 23.40156 | 23.71914 | 26.60078 | 28.46914 |
| `modules/json/orjson_module.py`                 | 22.72852 | 22.53398 | 21.41289 | 24.09609 | 24.28203 | 27.51289 |       -- |

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

Linux 1a9a6e47b96f 5.15.0-75-generic unknown GNU/Linux

CPU(s):                          12
Model name:                      Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:              2
Core(s) per socket:              6
CPU max MHz:                     4100.0000
NUMA node(s):                    1
NUMA node0 CPU(s):               0-11

MemTotal:       16066528 kB
MemFree:         2098324 kB
MemAvailable:   14182200 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  1.23354 |     0.0157 |    1.22766 |  1.2199 | 1.26361 |    32.71992 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  1.23051 |    0.00982 |    1.23031 | 1.21474 | 1.24549 |    33.22891 |
| `algorithm/search/index.py`                     |      yes |  1.25322 |    0.01561 |    1.24767 | 1.24202 | 1.28671 |    32.64687 |
| `algorithm/search/linear.py`                    |      yes |   1.2938 |    0.01818 |    1.28854 | 1.27926 | 1.34134 |    32.56289 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.07868 |    0.00056 |    0.07869 | 0.07782 | 0.07946 |    23.58555 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.07834 |    0.00035 |    0.07841 | 0.07785 | 0.07888 |    24.02031 |
| `complex/classes/classes.py`                    |      yes |  0.04261 |     0.0007 |    0.04249 | 0.04196 | 0.04444 |      25.275 |
| `complex/classes/dataclasses_.py`               |      yes |  0.12318 |    0.00114 |    0.12281 | 0.12222 | 0.12587 |    25.08516 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.09061 |    0.00045 |    0.09066 | 0.08991 | 0.09143 |    23.99805 |
| `complex/classes/simplenamespace.py`            |      yes |  0.04603 |    0.00302 |     0.0451 | 0.04429 | 0.05432 |    25.49102 |
| `complex/classes/sloted_classes.py`             |      yes |  0.04294 |     0.0004 |     0.0429 | 0.04235 | 0.04349 |    25.21328 |
| `complex/generators/simple.py`                  |      yes |  0.06197 |    0.00037 |    0.06197 | 0.06141 |  0.0626 |    25.25078 |
| `dummy/dummy.py`                                |      yes |  0.03096 |    0.00092 |    0.03075 | 0.03038 | 0.03349 |    23.99609 |
| `long_run/database/postgresql.py`               |      yes |  0.15299 |    0.00123 |    0.15325 |  0.1506 | 0.15461 |     29.2082 |
| `long_run/database/sqlite_.py`                  |      yes |  0.60779 |    0.00467 |    0.60691 |  0.6022 | 0.61517 |    67.25625 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |    0.654 |    0.00344 |    0.65318 | 0.64879 | 0.65984 |    65.89805 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.07004 |    0.00096 |    0.06993 | 0.06882 | 0.07249 |    23.58437 |
| `long_run/processes/collect_names_from_site.py` |      yes |  2.00921 |    0.02548 |    2.00398 |  1.9804 | 2.05186 |    45.53008 |
| `long_run/processes/generate_fake_data.py`      |      yes |  0.82615 |     0.0074 |    0.82492 | 0.81563 | 0.83759 |    68.89102 |
| `math/haversine.py`                             |      yes |  0.91301 |     0.0128 |    0.91284 | 0.89719 | 0.93405 |    23.31445 |
| `math/mandelbrot.py`                            |      yes |  2.58455 |    0.02775 |    2.57175 | 2.56128 | 2.64783 |    41.02539 |
| `math/pow_simple.py`                            |      yes |  0.69387 |     0.0151 |    0.69046 | 0.68109 | 0.73576 |    23.25625 |
| `math/pow_using_math.py`                        |      yes |  1.37529 |    0.03389 |    1.36682 | 1.34437 | 1.45041 |    24.16211 |
| `modules/json/json_module.py`                   |      yes |  0.44142 |     0.0099 |    0.43855 | 0.43148 | 0.46069 |    23.71914 |
| `modules/json/orjson_module.py`                 |      yes |  0.26129 |    0.00242 |    0.26091 | 0.25873 | 0.26703 |    24.28203 |

### **Python 3.11**

```bash
Python 3.11.4

Linux 1f9c53fe0bfa 5.15.0-75-generic unknown GNU/Linux

CPU(s):                          12
Model name:                      Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:              2
Core(s) per socket:              6
CPU max MHz:                     4100.0000
NUMA node(s):                    1
NUMA node0 CPU(s):               0-11

MemTotal:       16066528 kB
MemFree:         2082148 kB
MemAvailable:   14177096 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  1.04527 |    0.00858 |    1.04436 | 1.03417 | 1.06729 |    35.75234 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  1.05858 |    0.02555 |    1.04944 | 1.03859 | 1.11953 |    36.53945 |
| `algorithm/search/index.py`                     |      yes |  1.06199 |    0.00614 |    1.06073 | 1.05352 | 1.07155 |     35.5582 |
| `algorithm/search/linear.py`                    |      yes |  1.11471 |    0.02238 |    1.10618 | 1.08835 | 1.15328 |    35.03359 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.07426 |    0.00048 |    0.07427 | 0.07337 | 0.07509 |    26.53828 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.07378 |    0.00079 |    0.07361 | 0.07265 | 0.07512 |    26.93672 |
| `complex/classes/classes.py`                    |      yes |  0.02105 |    0.00015 |    0.02104 | 0.02083 | 0.02132 |    27.46914 |
| `complex/classes/dataclasses_.py`               |      yes |  0.11387 |    0.00033 |    0.11389 |  0.1133 | 0.11439 |     28.5668 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.08446 |    0.00034 |    0.08454 |  0.0836 | 0.08474 |    27.76445 |
| `complex/classes/simplenamespace.py`            |      yes |  0.02658 |    0.00029 |     0.0265 |  0.0263 | 0.02729 |    28.70625 |
| `complex/classes/sloted_classes.py`             |      yes |  0.02221 |    0.00144 |    0.02127 | 0.02099 | 0.02401 |    28.43594 |
| `complex/generators/simple.py`                  |      yes |  0.04055 |    0.00039 |    0.04047 | 0.03992 | 0.04116 |    29.03086 |
| `dummy/dummy.py`                                |      yes |  0.01513 |    0.00214 |    0.01581 | 0.01229 | 0.01803 |    26.46445 |
| `long_run/database/postgresql.py`               |      yes |  0.15069 |    0.00085 |    0.15075 | 0.14928 | 0.15203 |    31.72734 |
| `long_run/database/sqlite_.py`                  |      yes |  0.61518 |    0.00169 |    0.61517 | 0.61222 | 0.61871 |    72.79336 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |  0.64223 |    0.00128 |    0.64247 | 0.63941 | 0.64369 |    70.82695 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.05938 |    0.00055 |    0.05941 | 0.05855 | 0.06025 |    26.80078 |
| `long_run/processes/collect_names_from_site.py` |      yes |  1.71591 |    0.01675 |    1.71392 | 1.69619 | 1.75111 |    47.49336 |
| `long_run/processes/generate_fake_data.py`      |      yes |  0.81496 |    0.00959 |    0.81338 | 0.80602 | 0.83436 |    72.43555 |
| `math/haversine.py`                             |      yes |  0.81429 |    0.02916 |    0.80926 | 0.78024 | 0.86743 |    26.91914 |
| `math/mandelbrot.py`                            |      yes |  2.57773 |    0.03036 |    2.56705 | 2.55377 | 2.64307 |    40.82617 |
| `math/pow_simple.py`                            |      yes |  0.34734 |    0.00082 |    0.34767 | 0.34538 | 0.34802 |    26.92969 |
| `math/pow_using_math.py`                        |      yes |  1.17012 |    0.04203 |    1.15837 | 1.14551 | 1.28817 |    26.50664 |
| `modules/json/json_module.py`                   |      yes |  0.39774 |    0.00386 |    0.39771 | 0.39168 | 0.40476 |    26.60078 |
| `modules/json/orjson_module.py`                 |      yes |  0.21073 |    0.00165 |    0.21009 | 0.20928 | 0.21426 |    27.51289 |

### **Python 3.12**

```bash
Python 3.12.0b3

Linux fb2e56f8ac3a 5.15.0-75-generic unknown GNU/Linux

CPU(s):                          12
Model name:                      Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:              2
Core(s) per socket:              6
CPU max MHz:                     4100.0000
NUMA node(s):                    1
NUMA node0 CPU(s):               0-11

MemTotal:       16066528 kB
MemFree:         2075780 kB
MemAvailable:   14170376 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  1.16124 |    0.01486 |    1.15724 | 1.14335 | 1.19355 |    35.64883 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  1.17061 |    0.02509 |    1.15403 | 1.14499 | 1.20348 |    36.19453 |
| `algorithm/search/index.py`                     |      yes |  1.17667 |    0.00978 |    1.17472 | 1.16283 | 1.19931 |    35.67656 |
| `algorithm/search/linear.py`                    |      yes |  1.24256 |     0.0181 |    1.23424 | 1.22094 | 1.26497 |    35.61172 |
| `algorithm/twosum/twosum.py`                    |      yes |   0.0839 |    0.00039 |    0.08384 | 0.08344 | 0.08455 |    27.55117 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.08484 |    0.00341 |    0.08374 |  0.0833 |  0.0945 |    27.44414 |
| `complex/classes/classes.py`                    |      yes |  0.02216 |    0.00021 |    0.02213 | 0.02192 |  0.0225 |    28.25391 |
| `complex/classes/dataclasses_.py`               |      yes |  0.13116 |    0.00049 |    0.13122 | 0.13041 | 0.13201 |      28.125 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.09598 |    0.00041 |    0.09598 | 0.09527 | 0.09682 |    27.69766 |
| `complex/classes/simplenamespace.py`            |      yes |  0.02857 |     0.0003 |    0.02854 | 0.02819 |  0.0291 |    28.97734 |
| `complex/classes/sloted_classes.py`             |      yes |  0.02394 |    0.00239 |    0.02226 | 0.02209 | 0.02787 |    27.89336 |
| `complex/generators/simple.py`                  |      yes |  0.04592 |    0.00081 |    0.04569 | 0.04521 | 0.04793 |    29.53281 |
| `dummy/dummy.py`                                |      yes |  0.01733 |     0.0044 |    0.01509 | 0.01388 | 0.02733 |    27.33125 |
| `long_run/database/postgresql.py`               |      yes |  0.17388 |    0.00041 |    0.17374 | 0.17342 | 0.17447 |    32.68555 |
| `long_run/database/sqlite_.py`                  |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/file/load_titanic_csv_pandas.py`      |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.06624 |    0.00083 |    0.06587 | 0.06566 | 0.06842 |     27.8582 |
| `long_run/processes/collect_names_from_site.py` |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/processes/generate_fake_data.py`      |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `math/haversine.py`                             |      yes |   0.8648 |    0.02041 |    0.85751 | 0.84888 | 0.90301 |    27.07344 |
| `math/mandelbrot.py`                            |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `math/pow_simple.py`                            |      yes |  0.31074 |    0.00731 |    0.30738 | 0.30568 | 0.32478 |    26.90938 |
| `math/pow_using_math.py`                        |      yes |  1.21232 |    0.02764 |    1.20686 | 1.17862 | 1.26845 |    27.50664 |
| `modules/json/json_module.py`                   |      yes |  0.40225 |    0.00546 |    0.40124 | 0.39481 | 0.41123 |    28.46914 |
| `modules/json/orjson_module.py`                 |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
