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

> Last run: Sat Jun 3 04:54:37 PM -03 2023

### **Comparison**

#### How much faster 3.12 is? (Mean / Median from 3.6 to 3.11)

| Command                                         |               3.6 |               3.7 |               3.8 |               3.9 |              3.10 |              3.11 |
| :---------------------------------------------- | ----------------: | ----------------: | ----------------: | ----------------: | ----------------: | ----------------: |
| `algorithm/search/bin.py`                       |   28.70% / 27.47% |   16.73% / 13.92% |   11.24% / 11.18% |    10.43% / 9.73% |     1.39% / 0.91% | -15.03% / -15.45% |
| `algorithm/search/hashmap_lookup.py`            |   27.63% / 26.69% |   13.82% / 13.45% |     9.57% / 9.59% |   12.98% / 11.62% |     0.72% / 0.52% | -14.96% / -15.13% |
| `algorithm/search/index.py`                     |   29.43% / 27.61% |   13.05% / 13.11% |    10.54% / 9.47% |     9.53% / 9.48% |     1.46% / 1.46% | -15.54% / -15.82% |
| `algorithm/search/linear.py`                    |   23.48% / 22.57% |     9.56% / 9.02% |     6.23% / 6.58% |     7.18% / 7.22% |   -2.91% / -2.41% | -18.34% / -18.10% |
| `algorithm/twosum/twosum.py`                    |   -5.98% / -6.25% | -21.65% / -21.58% | -15.23% / -15.20% |   -5.04% / -4.82% | -11.58% / -11.47% | -16.23% / -16.21% |
| `algorithm/twosum/twosum_naive.py`              |   -6.13% / -6.05% | -22.09% / -21.82% | -15.15% / -14.97% |   -4.18% / -4.18% | -11.74% / -11.47% | -16.49% / -16.16% |
| `complex/classes/classes.py`                    |  94.79% / 100.36% |   65.18% / 67.37% |   69.34% / 72.79% |   83.71% / 86.06% |   73.54% / 74.81% | -13.18% / -11.30% |
| `complex/classes/dataclasses_.py`               |           -- / -- | -23.13% / -22.84% | -17.56% / -16.96% |   -1.57% / -1.17% |   -9.34% / -8.98% | -14.68% / -14.15% |
| `complex/classes/namedtuple_classes.py`         |   -2.47% / -2.46% | -19.23% / -19.07% | -13.89% / -13.79% |   -4.00% / -3.89% |  -9.89% / -10.86% | -15.03% / -14.82% |
| `complex/classes/simplenamespace.py`            | 116.30% / 116.56% |   41.65% / 40.96% |   47.13% / 46.56% |   63.98% / 63.97% |   53.20% / 53.15% |   -7.91% / -8.10% |
| `complex/classes/sloted_classes.py`             | 112.97% / 112.46% |   81.11% / 78.63% |   85.92% / 85.19% |  100.53% / 99.66% |   87.07% / 86.68% |   -2.21% / -3.59% |
| `complex/generators/simple.py`                  |   61.30% / 61.45% |   50.24% / 50.68% |   44.77% / 44.94% |   49.99% / 50.17% |   43.58% / 43.34% |   -6.87% / -6.75% |
| `dummy/dummy.py`                                | 124.90% / 126.91% |   77.52% / 85.95% |   85.71% / 96.31% | 103.47% / 115.79% |  93.77% / 106.33% |     5.96% / 6.68% |
| `long_run/database/postgresql.py`               | -10.33% / -10.55% | -18.89% / -18.75% | -11.77% / -11.43% |   -2.80% / -2.64% | -11.62% / -11.39% | -12.79% / -12.53% |
| `long_run/database/sqlite_.py`                  |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `long_run/file/load_titanic_csv_pandas.py`      |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `long_run/file/load_titanic_csv_python.py`      |     6.78% / 7.21% |   -1.41% / -2.54% |     4.65% / 3.67% |   12.78% / 13.21% |     2.34% / 2.41% | -12.68% / -12.25% |
| `long_run/processes/collect_names_from_site.py` |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `long_run/processes/generate_fake_data.py`      |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `math/haversine.py`                             |     4.39% / 3.05% |     1.65% / 1.25% |   -3.92% / -4.25% |     8.46% / 8.72% |     1.58% / 0.92% | -12.86% / -12.63% |
| `math/mandelbrot.py`                            |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |
| `math/pow_simple.py`                            |   34.62% / 34.29% |   29.75% / 29.33% |   31.74% / 30.89% |   33.00% / 33.47% |   25.58% / 25.41% |     4.98% / 5.41% |
| `math/pow_using_math.py`                        |   18.14% / 17.14% |     9.96% / 9.32% |     2.26% / 1.51% |     8.69% / 9.10% |     8.94% / 9.16% |   -7.17% / -7.03% |
| `modules/json/json_module.py`                   |   38.20% / 37.14% |   28.16% / 28.66% |   22.11% / 22.11% |   23.77% / 23.14% |   13.82% / 14.06% |   -1.52% / -1.29% |
| `modules/json/orjson_module.py`                 |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |           -- / -- |

---

#### How much more memory 3.12 uses? (Memory diff from 3.6 to 3.11)

| Command                                         |    3.6 |    3.7 |    3.8 |    3.9 |   3.10 |   3.11 |
| :---------------------------------------------- | -----: | -----: | -----: | -----: | -----: | -----: |
| `algorithm/search/bin.py`                       | 18.57% | 17.16% | 21.67% | 12.72% | 11.45% | -0.31% |
| `algorithm/search/hashmap_lookup.py`            | 22.61% | 16.85% | 20.68% | 17.71% |  9.31% |   0.3% |
| `algorithm/search/index.py`                     | 18.55% | 13.55% | 21.26% | 14.56% | 11.57% | -1.58% |
| `algorithm/search/linear.py`                    | 17.73% | 17.17% | 20.41% | 14.77% |  9.63% | -0.56% |
| `algorithm/twosum/twosum.py`                    | 18.05% | 31.65% | 28.37% | 19.47% | 18.92% |  4.69% |
| `algorithm/twosum/twosum_naive.py`              |  18.3% | 31.58% | 29.99% | 22.59% |  17.0% |  3.31% |
| `complex/classes/classes.py`                    | 23.82% | 35.55% | 35.72% | 22.32% | 13.47% |  2.69% |
| `complex/classes/dataclasses_.py`               |     -- | 31.41% | 29.02% | 17.39% | 10.56% | -0.35% |
| `complex/classes/namedtuple_classes.py`         |  19.5% | 32.48% | 31.08% | 22.21% | 13.37% |  2.43% |
| `complex/classes/simplenamespace.py`            | 28.01% | 39.69% | 39.36% | 30.31% | 17.56% |  3.09% |
| `complex/classes/sloted_classes.py`             | 22.06% | 34.87% | 30.43% | 24.04% | 12.79% | -0.21% |
| `complex/generators/simple.py`                  | 26.27% | 38.35% | 37.06% | 24.42% | 19.42% |  2.73% |
| `dummy/dummy.py`                                | 21.98% | 32.44% | 31.69% | 18.24% | 17.35% |  5.07% |
| `long_run/database/postgresql.py`               | 10.91% | 24.57% | 20.83% |  16.2% | 15.25% |  3.31% |
| `long_run/database/sqlite_.py`                  |     -- |     -- |     -- |     -- |     -- |     -- |
| `long_run/file/load_titanic_csv_pandas.py`      |     -- |     -- |     -- |     -- |     -- |     -- |
| `long_run/file/load_titanic_csv_python.py`      | 20.03% | 32.14% | 28.79% | 18.57% | 17.61% |  3.88% |
| `long_run/processes/collect_names_from_site.py` |     -- |     -- |     -- |     -- |     -- |     -- |
| `long_run/processes/generate_fake_data.py`      |     -- |     -- |     -- |     -- |     -- |     -- |
| `math/haversine.py`                             | 22.02% | 31.03% | 29.95% | 20.83% | 19.56% |  3.41% |
| `math/mandelbrot.py`                            |     -- |     -- |     -- |     -- |     -- |     -- |
| `math/pow_simple.py`                            | 21.37% | 32.79% | 30.52% | 20.06% | 19.16% |  3.25% |
| `math/pow_using_math.py`                        | 21.56% |  32.2% |  29.7% | 18.51% | 19.14% |  5.36% |
| `modules/json/json_module.py`                   |  23.9% |  27.7% | 28.65% | 21.85% | 21.27% |  7.19% |
| `modules/json/orjson_module.py`                 |     -- |     -- |     -- |     -- |     -- |     -- |

---

#### **Execution**

##### **Mean [s]**

| Command                                         |     3.6 |     3.7 |     3.8 |     3.9 |    3.10 |    3.11 |    3.12 |
| :---------------------------------------------- | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| `algorithm/search/bin.py`                       | 1.12397 | 1.01948 | 0.97154 | 0.96445 | 0.88552 | 0.74208 | 0.87334 |
| `algorithm/search/hashmap_lookup.py`            | 1.12619 | 1.00436 | 0.96689 | 0.99699 | 0.88876 | 0.75041 | 0.88242 |
| `algorithm/search/index.py`                     | 1.15502 | 1.00883 | 0.98649 | 0.97742 | 0.90538 | 0.75371 | 0.89239 |
| `algorithm/search/linear.py`                    | 1.19833 |  1.0633 | 1.03096 |  1.0402 | 0.94225 | 0.79248 | 0.97048 |
| `algorithm/twosum/twosum.py`                    | 0.07846 | 0.06538 | 0.07074 | 0.07924 | 0.07379 | 0.06991 | 0.08345 |
| `algorithm/twosum/twosum_naive.py`              | 0.07831 | 0.06499 | 0.07078 | 0.07993 | 0.07363 | 0.06966 | 0.08342 |
| `complex/classes/classes.py`                    | 0.04447 | 0.03771 | 0.03866 | 0.04194 | 0.03962 | 0.01982 | 0.02283 |
| `complex/classes/dataclasses_.py`               |      -- | 0.09716 | 0.10419 |  0.1244 | 0.11458 | 0.10783 | 0.12639 |
| `complex/classes/namedtuple_classes.py`         | 0.09112 | 0.07546 | 0.08045 | 0.08969 | 0.08419 | 0.07939 | 0.09343 |
| `complex/classes/simplenamespace.py`            | 0.05879 |  0.0385 | 0.03999 | 0.04457 | 0.04164 | 0.02503 | 0.02718 |
| `complex/classes/sloted_classes.py`             | 0.04432 | 0.03769 | 0.03869 | 0.04173 | 0.03893 | 0.02035 | 0.02081 |
| `complex/generators/simple.py`                  | 0.06273 | 0.05843 |  0.0563 | 0.05833 | 0.05584 | 0.03622 | 0.03889 |
| `dummy/dummy.py`                                | 0.03432 | 0.02709 | 0.02834 | 0.03105 | 0.02957 | 0.01617 | 0.01526 |
| `long_run/database/postgresql.py`               | 0.14364 | 0.12993 | 0.14133 |  0.1557 | 0.14157 | 0.13969 | 0.16018 |
| `long_run/database/sqlite_.py`                  | 0.57844 |  0.5014 | 0.56303 | 0.59595 | 0.55549 | 0.55768 |      -- |
| `long_run/file/load_titanic_csv_pandas.py`      | 0.65405 | 0.54451 | 0.60245 | 0.63037 | 0.59631 | 0.58374 |      -- |
| `long_run/file/load_titanic_csv_python.py`      | 0.06802 |  0.0628 | 0.06666 | 0.07184 | 0.06519 | 0.05562 |  0.0637 |
| `long_run/processes/collect_names_from_site.py` |      -- |      -- | 1.94163 |  2.0184 | 1.94361 | 1.59234 |      -- |
| `long_run/processes/generate_fake_data.py`      | 0.79634 | 0.72184 | 0.75937 | 0.80012 | 0.75721 | 0.75536 |      -- |
| `math/haversine.py`                             | 0.61041 | 0.59439 | 0.56177 | 0.63418 | 0.59396 | 0.50955 | 0.58472 |
| `math/mandelbrot.py`                            | 3.19466 | 3.11446 |  3.1009 | 3.06215 | 3.04284 |  3.0378 |      -- |
| `math/pow_simple.py`                            | 0.44209 |  0.4261 | 0.43264 | 0.43677 | 0.41239 | 0.34476 |  0.3284 |
| `math/pow_using_math.py`                        | 1.54776 |  1.4406 | 1.33971 | 1.42394 | 1.42719 | 1.21615 | 1.31011 |
| `modules/json/json_module.py`                   | 0.40871 | 0.37902 | 0.36112 | 0.36604 |  0.3366 | 0.29123 | 0.29574 |
| `modules/json/orjson_module.py`                 | 0.25766 | 0.19847 | 0.22082 | 0.23363 | 0.21476 | 0.17349 |      -- |

##### **Median [s]**

| Command                                         |     3.6 |     3.7 |     3.8 |     3.9 |    3.10 |    3.11 |    3.12 |
| :---------------------------------------------- | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| `algorithm/search/bin.py`                       | 1.11388 | 0.99547 | 0.97159 | 0.95887 | 0.88181 | 0.73886 | 0.87386 |
| `algorithm/search/hashmap_lookup.py`            | 1.11758 | 1.00081 | 0.96676 | 0.98464 | 0.88679 | 0.74871 | 0.88216 |
| `algorithm/search/index.py`                     | 1.13774 | 1.00842 |   0.976 | 0.97611 | 0.90461 | 0.75049 | 0.89155 |
| `algorithm/search/linear.py`                    | 1.18562 | 1.05459 |   1.031 | 1.03718 | 0.94402 | 0.79227 | 0.96733 |
| `algorithm/twosum/twosum.py`                    | 0.07821 | 0.06542 | 0.07074 |  0.0794 | 0.07385 |  0.0699 | 0.08342 |
| `algorithm/twosum/twosum_naive.py`              | 0.07815 | 0.06503 | 0.07073 |  0.0797 | 0.07364 | 0.06974 | 0.08318 |
| `complex/classes/classes.py`                    |  0.0447 | 0.03734 | 0.03855 | 0.04151 |   0.039 | 0.01979 | 0.02231 |
| `complex/classes/dataclasses_.py`               |      -- | 0.09706 | 0.10445 | 0.12432 |  0.1145 | 0.10799 | 0.12579 |
| `complex/classes/namedtuple_classes.py`         | 0.09102 | 0.07552 | 0.08045 | 0.08969 | 0.08319 | 0.07949 | 0.09332 |
| `complex/classes/simplenamespace.py`            | 0.05884 |  0.0383 | 0.03982 | 0.04455 | 0.04161 | 0.02497 | 0.02717 |
| `complex/classes/sloted_classes.py`             | 0.04434 | 0.03728 | 0.03865 | 0.04167 | 0.03896 | 0.02012 | 0.02087 |
| `complex/generators/simple.py`                  | 0.06266 | 0.05848 | 0.05625 | 0.05828 | 0.05563 | 0.03619 | 0.03881 |
| `dummy/dummy.py`                                | 0.03263 | 0.02674 | 0.02823 | 0.03103 | 0.02967 | 0.01534 | 0.01438 |
| `long_run/database/postgresql.py`               | 0.14277 | 0.12967 | 0.14135 | 0.15538 | 0.14142 | 0.13961 |  0.1596 |
| `long_run/database/sqlite_.py`                  | 0.57669 | 0.50063 | 0.55996 | 0.59318 | 0.55487 | 0.55555 |      -- |
| `long_run/file/load_titanic_csv_pandas.py`      | 0.65288 | 0.54384 | 0.59942 | 0.63046 | 0.59548 |  0.5823 |      -- |
| `long_run/file/load_titanic_csv_python.py`      | 0.06799 | 0.06181 | 0.06575 |  0.0718 | 0.06495 | 0.05565 | 0.06342 |
| `long_run/processes/collect_names_from_site.py` |      -- |      -- | 1.94159 | 2.02604 | 1.94593 | 1.59353 |      -- |
| `long_run/processes/generate_fake_data.py`      | 0.79487 | 0.71937 | 0.75646 | 0.79918 | 0.75709 | 0.75281 |      -- |
| `math/haversine.py`                             | 0.60344 |  0.5929 |  0.5607 | 0.63664 | 0.59097 | 0.51161 | 0.58556 |
| `math/mandelbrot.py`                            | 3.18277 | 3.13511 | 3.11555 | 3.04229 |  3.0181 | 3.01757 |      -- |
| `math/pow_simple.py`                            | 0.43928 | 0.42306 | 0.42817 | 0.43658 | 0.41022 | 0.34481 | 0.32711 |
| `math/pow_using_math.py`                        | 1.52892 | 1.42681 | 1.32481 | 1.42395 | 1.42477 |  1.2134 | 1.30516 |
| `modules/json/json_module.py`                   | 0.40505 | 0.38001 | 0.36067 | 0.36371 |  0.3369 | 0.29155 | 0.29536 |
| `modules/json/orjson_module.py`                 | 0.25744 | 0.19844 | 0.21792 | 0.23295 | 0.21517 | 0.17342 |      -- |

#### **Memory Usage**

##### **MEM [MB]**

| Command                                         |      3.6 |      3.7 |      3.8 |      3.9 |     3.10 |     3.11 |     3.12 |
| :---------------------------------------------- | -------: | -------: | -------: | -------: | -------: | -------: | -------: |
| `algorithm/search/bin.py`                       | 28.98984 | 29.33945 | 28.25234 | 30.49375 | 30.84375 | 34.48086 | 34.37383 |
| `algorithm/search/hashmap_lookup.py`            | 28.48359 | 29.88867 | 28.93828 | 29.67031 | 31.95039 | 34.81758 | 34.92344 |
| `algorithm/search/index.py`                     | 28.89922 | 30.17148 | 28.25391 | 29.90625 | 30.70703 | 34.81133 | 34.26094 |
| `algorithm/search/linear.py`                    | 29.16172 | 29.30078 | 28.51289 | 29.91328 | 31.31523 | 34.52656 | 34.33242 |
| `algorithm/twosum/twosum.py`                    | 22.36641 | 20.05547 | 20.56836 | 22.10078 | 22.20312 | 25.21992 | 26.40391 |
| `algorithm/twosum/twosum_naive.py`              | 22.43047 | 20.16719 | 20.41367 | 21.64727 | 22.67969 | 25.68516 | 26.53633 |
| `complex/classes/classes.py`                    | 21.96367 |  20.0625 | 20.03711 | 22.23242 | 23.96758 |  26.4832 | 27.19531 |
| `complex/classes/dataclasses_.py`               |       -- | 20.10937 | 20.48242 | 22.51094 | 23.90195 | 26.51797 | 26.42617 |
| `complex/classes/namedtuple_classes.py`         | 22.30664 | 20.12109 | 20.33477 | 21.81172 | 23.51289 | 26.02188 | 26.65547 |
| `complex/classes/simplenamespace.py`            | 22.17773 | 20.32227 | 20.37148 | 21.78555 | 24.14805 | 27.53906 | 28.38906 |
| `complex/classes/sloted_classes.py`             | 22.19258 | 20.08516 | 20.76836 | 21.83828 |  24.0168 | 27.14609 | 27.08789 |
| `complex/generators/simple.py`                  | 22.11016 |  20.1793 | 20.36836 | 22.43828 | 23.37812 | 27.17539 | 27.91758 |
| `dummy/dummy.py`                                | 21.73945 | 20.02266 | 20.13633 | 22.42734 | 22.59688 | 25.23867 | 26.51719 |
| `long_run/database/postgresql.py`               | 26.94219 | 23.98711 | 24.73008 | 25.71602 | 25.92773 | 28.92227 | 29.88086 |
| `long_run/database/sqlite_.py`                  | 63.09766 | 64.78047 | 65.01133 | 65.31406 | 64.85352 | 70.33125 |       -- |
| `long_run/file/load_titanic_csv_pandas.py`      | 61.97695 | 63.49922 | 63.65117 | 64.59687 | 63.09492 | 68.85391 |       -- |
| `long_run/file/load_titanic_csv_python.py`      |  22.0875 | 20.06406 | 20.58594 | 22.35938 | 22.54297 | 25.52305 |  26.5125 |
| `long_run/processes/collect_names_from_site.py` |       -- |       -- | 44.27305 | 44.04336 | 44.05508 | 46.32031 |       -- |
| `long_run/processes/generate_fake_data.py`      | 65.14844 | 68.27617 | 65.46211 | 68.28437 | 67.21836 | 71.86016 |       -- |
| `math/haversine.py`                             | 21.78438 | 20.28555 | 20.45391 | 21.99844 | 22.23281 | 25.70508 | 26.58086 |
| `math/mandelbrot.py`                            |     36.5 |  34.5168 | 35.00391 | 41.33242 | 41.37227 | 39.04258 |       -- |
| `math/pow_simple.py`                            | 21.84688 | 19.96875 | 20.31602 | 22.08516 | 22.25234 | 25.68047 | 26.51562 |
| `math/pow_using_math.py`                        | 21.80156 | 20.04727 | 20.43281 |  22.3625 | 22.24375 | 25.15273 | 26.50195 |
| `modules/json/json_module.py`                   | 21.90469 | 21.25352 |  21.0957 | 22.27305 | 22.38008 | 25.31914 | 27.14023 |
| `modules/json/orjson_module.py`                 | 22.79531 | 21.49766 | 21.25703 | 22.85547 |  22.8457 |  25.9457 |       -- |

---

### **Python 3.6**

```bash
Python 3.6.15

Linux d3aed0248949 5.15.0-73-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078816 kB
MemFree:         9048476 kB
MemAvailable:   14601248 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  1.12397 |    0.02248 |    1.11388 | 1.10204 | 1.15907 |    28.98984 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  1.12619 |    0.02777 |    1.11758 | 1.10523 | 1.18975 |    28.48359 |
| `algorithm/search/index.py`                     |      yes |  1.15502 |    0.04169 |    1.13774 | 1.12402 | 1.26064 |    28.89922 |
| `algorithm/search/linear.py`                    |      yes |  1.19833 |    0.03385 |    1.18562 | 1.15265 | 1.25787 |    29.16172 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.07846 |     0.0007 |    0.07821 | 0.07785 | 0.07999 |    22.36641 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.07831 |    0.00063 |    0.07815 | 0.07754 | 0.07977 |    22.43047 |
| `complex/classes/classes.py`                    |      yes |  0.04447 |    0.00054 |     0.0447 | 0.04357 | 0.04522 |    21.96367 |
| `complex/classes/dataclasses_.py`               |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.09112 |    0.00063 |    0.09102 | 0.09002 | 0.09219 |    22.30664 |
| `complex/classes/simplenamespace.py`            |      yes |  0.05879 |    0.00032 |    0.05884 | 0.05814 | 0.05921 |    22.17773 |
| `complex/classes/sloted_classes.py`             |      yes |  0.04432 |    0.00045 |    0.04434 |  0.0437 | 0.04519 |    22.19258 |
| `complex/generators/simple.py`                  |      yes |  0.06273 |    0.00065 |    0.06266 | 0.06191 | 0.06392 |    22.11016 |
| `dummy/dummy.py`                                |      yes |  0.03432 |    0.00467 |    0.03263 | 0.03188 | 0.04721 |    21.73945 |
| `long_run/database/postgresql.py`               |      yes |  0.14364 |    0.00301 |    0.14277 | 0.14137 | 0.15144 |    26.94219 |
| `long_run/database/sqlite_.py`                  |      yes |  0.57844 |    0.00686 |    0.57669 | 0.57092 | 0.59259 |    63.09766 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |  0.65405 |     0.0123 |    0.65288 | 0.64026 | 0.67655 |    61.97695 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.06802 |    0.00061 |    0.06799 | 0.06716 | 0.06935 |     22.0875 |
| `long_run/processes/collect_names_from_site.py` |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/processes/generate_fake_data.py`      |      yes |  0.79634 |     0.0071 |    0.79487 | 0.78798 | 0.81181 |    65.14844 |
| `math/haversine.py`                             |      yes |  0.61041 |    0.03824 |    0.60344 | 0.57255 | 0.70525 |    21.78438 |
| `math/mandelbrot.py`                            |      yes |  3.19466 |    0.02848 |    3.18277 | 3.17337 | 3.26376 |        36.5 |
| `math/pow_simple.py`                            |      yes |  0.44209 |    0.00871 |    0.43928 | 0.43507 |  0.4592 |    21.84688 |
| `math/pow_using_math.py`                        |      yes |  1.54776 |    0.05774 |    1.52892 |  1.4873 | 1.65172 |    21.80156 |
| `modules/json/json_module.py`                   |      yes |  0.40871 |    0.01225 |    0.40505 | 0.39566 | 0.43696 |    21.90469 |
| `modules/json/orjson_module.py`                 |      yes |  0.25766 |    0.00218 |    0.25744 |  0.2549 | 0.26223 |    22.79531 |

### **Python 3.7**

```bash
Python 3.7.16

Linux e48c5936a641 5.15.0-73-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078816 kB
MemFree:         9040632 kB
MemAvailable:   14594668 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  1.01948 |    0.08045 |    0.99547 | 0.98388 |  1.2477 |    29.33945 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  1.00436 |    0.02799 |    1.00081 | 0.96659 | 1.04411 |    29.88867 |
| `algorithm/search/index.py`                     |      yes |  1.00883 |    0.00734 |    1.00842 | 0.99757 | 1.02712 |    30.17148 |
| `algorithm/search/linear.py`                    |      yes |   1.0633 |    0.02602 |    1.05459 | 1.03918 | 1.12745 |    29.30078 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.06538 |    0.00042 |    0.06542 | 0.06472 |  0.0662 |    20.05547 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.06499 |     0.0006 |    0.06503 | 0.06396 | 0.06582 |    20.16719 |
| `complex/classes/classes.py`                    |      yes |  0.03771 |    0.00111 |    0.03734 | 0.03705 | 0.04079 |     20.0625 |
| `complex/classes/dataclasses_.py`               |      yes |  0.09716 |    0.00078 |    0.09706 | 0.09615 | 0.09876 |    20.10937 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.07546 |    0.00033 |    0.07552 |  0.0747 | 0.07582 |    20.12109 |
| `complex/classes/simplenamespace.py`            |      yes |   0.0385 |    0.00089 |     0.0383 | 0.03752 | 0.04068 |    20.32227 |
| `complex/classes/sloted_classes.py`             |      yes |  0.03769 |    0.00115 |    0.03728 | 0.03701 |  0.0409 |    20.08516 |
| `complex/generators/simple.py`                  |      yes |  0.05843 |    0.00065 |    0.05848 | 0.05752 |  0.0599 |     20.1793 |
| `dummy/dummy.py`                                |      yes |  0.02709 |    0.00109 |    0.02674 | 0.02641 | 0.03005 |    20.02266 |
| `long_run/database/postgresql.py`               |      yes |  0.12993 |     0.0011 |    0.12967 | 0.12876 | 0.13269 |    23.98711 |
| `long_run/database/sqlite_.py`                  |      yes |   0.5014 |     0.0022 |    0.50063 | 0.49913 | 0.50574 |    64.78047 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |  0.54451 |     0.0039 |    0.54384 | 0.54073 | 0.55361 |    63.49922 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |   0.0628 |     0.0021 |    0.06181 | 0.06099 | 0.06791 |    20.06406 |
| `long_run/processes/collect_names_from_site.py` |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/processes/generate_fake_data.py`      |      yes |  0.72184 |    0.00608 |    0.71937 | 0.71665 | 0.73406 |    68.27617 |
| `math/haversine.py`                             |      yes |  0.59439 |    0.00932 |     0.5929 | 0.58444 | 0.61283 |    20.28555 |
| `math/mandelbrot.py`                            |      yes |  3.11446 |    0.06658 |    3.13511 | 2.92546 | 3.14279 |     34.5168 |
| `math/pow_simple.py`                            |      yes |   0.4261 |    0.01159 |    0.42306 | 0.41264 | 0.45346 |    19.96875 |
| `math/pow_using_math.py`                        |      yes |   1.4406 |     0.0328 |    1.42681 | 1.40527 | 1.51677 |    20.04727 |
| `modules/json/json_module.py`                   |      yes |  0.37902 |     0.0035 |    0.38001 | 0.37249 | 0.38412 |    21.25352 |
| `modules/json/orjson_module.py`                 |      yes |  0.19847 |    0.00169 |    0.19844 | 0.19621 | 0.20227 |    21.49766 |

### **Python 3.8**

```bash
Python 3.8.16

Linux d0e684c22916 5.15.0-73-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078816 kB
MemFree:         9048992 kB
MemAvailable:   14604324 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  0.97154 |    0.01587 |    0.97159 | 0.95051 | 1.00039 |    28.25234 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  0.96689 |    0.01009 |    0.96676 |  0.9526 | 0.97942 |    28.93828 |
| `algorithm/search/index.py`                     |      yes |  0.98649 |    0.02399 |      0.976 | 0.96105 |  1.0348 |    28.25391 |
| `algorithm/search/linear.py`                    |      yes |  1.03096 |    0.01073 |      1.031 | 1.01148 | 1.04557 |    28.51289 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.07074 |    0.00035 |    0.07074 | 0.07018 | 0.07132 |    20.56836 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.07078 |    0.00041 |    0.07073 | 0.07036 | 0.07163 |    20.41367 |
| `complex/classes/classes.py`                    |      yes |  0.03866 |    0.00033 |    0.03855 | 0.03827 | 0.03927 |    20.03711 |
| `complex/classes/dataclasses_.py`               |      yes |  0.10419 |    0.00163 |    0.10445 | 0.10183 | 0.10593 |    20.48242 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.08045 |    0.00043 |    0.08045 | 0.07986 | 0.08101 |    20.33477 |
| `complex/classes/simplenamespace.py`            |      yes |  0.03999 |    0.00048 |    0.03982 | 0.03948 | 0.04116 |    20.37148 |
| `complex/classes/sloted_classes.py`             |      yes |  0.03869 |    0.00035 |    0.03865 | 0.03813 | 0.03917 |    20.76836 |
| `complex/generators/simple.py`                  |      yes |   0.0563 |    0.00032 |    0.05625 | 0.05586 | 0.05675 |    20.36836 |
| `dummy/dummy.py`                                |      yes |  0.02834 |    0.00035 |    0.02823 | 0.02799 | 0.02896 |    20.13633 |
| `long_run/database/postgresql.py`               |      yes |  0.14133 |    0.00068 |    0.14135 | 0.14023 | 0.14239 |    24.73008 |
| `long_run/database/sqlite_.py`                  |      yes |  0.56303 |    0.00954 |    0.55996 |  0.5564 | 0.58865 |    65.01133 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |  0.60245 |    0.00604 |    0.59942 | 0.59774 | 0.61373 |    63.65117 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.06666 |    0.00285 |    0.06575 | 0.06512 | 0.07463 |    20.58594 |
| `long_run/processes/collect_names_from_site.py` |      yes |  1.94163 |    0.07935 |    1.94159 | 1.82564 | 2.06041 |    44.27305 |
| `long_run/processes/generate_fake_data.py`      |      yes |  0.75937 |    0.00738 |    0.75646 | 0.75294 | 0.77603 |    65.46211 |
| `math/haversine.py`                             |      yes |  0.56177 |    0.01852 |     0.5607 | 0.54392 | 0.60377 |    20.45391 |
| `math/mandelbrot.py`                            |      yes |   3.1009 |    0.04122 |    3.11555 | 3.00851 | 3.13243 |    35.00391 |
| `math/pow_simple.py`                            |      yes |  0.43264 |    0.01083 |    0.42817 | 0.42182 | 0.44814 |    20.31602 |
| `math/pow_using_math.py`                        |      yes |  1.33971 |    0.04316 |    1.32481 | 1.30259 | 1.42826 |    20.43281 |
| `modules/json/json_module.py`                   |      yes |  0.36112 |    0.00735 |    0.36067 | 0.35271 | 0.37876 |     21.0957 |
| `modules/json/orjson_module.py`                 |      yes |  0.22082 |    0.01107 |    0.21792 | 0.21319 | 0.25057 |    21.25703 |

### **Python 3.9**

```bash
Python 3.9.16

Linux 8433e7e88c68 5.15.0-73-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078816 kB
MemFree:         9050960 kB
MemAvailable:   14607204 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  0.96445 |    0.02042 |    0.95887 | 0.94481 | 1.01855 |    30.49375 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  0.99699 |    0.02806 |    0.98464 | 0.96247 | 1.05112 |    29.67031 |
| `algorithm/search/index.py`                     |      yes |  0.97742 |    0.01163 |    0.97611 | 0.96109 | 0.99548 |    29.90625 |
| `algorithm/search/linear.py`                    |      yes |   1.0402 |    0.02332 |    1.03718 | 1.01393 | 1.07473 |    29.91328 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.07924 |    0.00041 |     0.0794 | 0.07855 | 0.07972 |    22.10078 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.07993 |      0.001 |     0.0797 | 0.07897 | 0.08239 |    21.64727 |
| `complex/classes/classes.py`                    |      yes |  0.04194 |      0.001 |    0.04151 | 0.04117 | 0.04385 |    22.23242 |
| `complex/classes/dataclasses_.py`               |      yes |   0.1244 |    0.00034 |    0.12432 | 0.12389 | 0.12488 |    22.51094 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.08969 |    0.00038 |    0.08969 | 0.08911 | 0.09024 |    21.81172 |
| `complex/classes/simplenamespace.py`            |      yes |  0.04457 |    0.00022 |    0.04455 | 0.04422 | 0.04495 |    21.78555 |
| `complex/classes/sloted_classes.py`             |      yes |  0.04173 |    0.00044 |    0.04167 |  0.0411 | 0.04233 |    21.83828 |
| `complex/generators/simple.py`                  |      yes |  0.05833 |    0.00038 |    0.05828 | 0.05774 | 0.05882 |    22.43828 |
| `dummy/dummy.py`                                |      yes |  0.03105 |    0.00039 |    0.03103 | 0.03056 |  0.0317 |    22.42734 |
| `long_run/database/postgresql.py`               |      yes |   0.1557 |    0.00167 |    0.15538 | 0.15416 | 0.15869 |    25.71602 |
| `long_run/database/sqlite_.py`                  |      yes |  0.59595 |    0.01119 |    0.59318 | 0.58508 | 0.61473 |    65.31406 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |  0.63037 |    0.00092 |    0.63046 | 0.62876 | 0.63182 |    64.59687 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.07184 |    0.00045 |     0.0718 | 0.07127 | 0.07261 |    22.35938 |
| `long_run/processes/collect_names_from_site.py` |      yes |   2.0184 |    0.03948 |    2.02604 |  1.9412 |  2.0691 |    44.04336 |
| `long_run/processes/generate_fake_data.py`      |      yes |  0.80012 |    0.00595 |    0.79918 | 0.79263 | 0.81025 |    68.28437 |
| `math/haversine.py`                             |      yes |  0.63418 |    0.01579 |    0.63664 | 0.61147 |   0.662 |    21.99844 |
| `math/mandelbrot.py`                            |      yes |  3.06215 |    0.04475 |    3.04229 | 3.03542 | 3.16878 |    41.33242 |
| `math/pow_simple.py`                            |      yes |  0.43677 |    0.00115 |    0.43658 | 0.43487 | 0.43865 |    22.08516 |
| `math/pow_using_math.py`                        |      yes |  1.42394 |    0.02487 |    1.42395 |  1.3869 | 1.46409 |     22.3625 |
| `modules/json/json_module.py`                   |      yes |  0.36604 |    0.00753 |    0.36371 | 0.35857 | 0.38342 |    22.27305 |
| `modules/json/orjson_module.py`                 |      yes |  0.23363 |    0.00244 |    0.23295 | 0.22875 | 0.23712 |    22.85547 |

### **Python 3.10**

```bash
Python 3.10.11

Linux f15171210c67 5.15.0-73-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078816 kB
MemFree:         9017376 kB
MemAvailable:   14575144 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  0.88552 |    0.01764 |    0.88181 | 0.87014 | 0.92991 |    30.84375 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  0.88876 |    0.01137 |    0.88679 | 0.87505 | 0.91538 |    31.95039 |
| `algorithm/search/index.py`                     |      yes |  0.90538 |      0.011 |    0.90461 | 0.88776 | 0.92326 |    30.70703 |
| `algorithm/search/linear.py`                    |      yes |  0.94225 |     0.0086 |    0.94402 | 0.92481 | 0.95148 |    31.31523 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.07379 |    0.00026 |    0.07385 |  0.0733 | 0.07415 |    22.20312 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.07363 |    0.00034 |    0.07364 | 0.07289 | 0.07407 |    22.67969 |
| `complex/classes/classes.py`                    |      yes |  0.03962 |    0.00236 |      0.039 | 0.03846 | 0.04628 |    23.96758 |
| `complex/classes/dataclasses_.py`               |      yes |  0.11458 |    0.00079 |     0.1145 | 0.11352 | 0.11617 |    23.90195 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.08419 |    0.00291 |    0.08319 | 0.08268 | 0.09239 |    23.51289 |
| `complex/classes/simplenamespace.py`            |      yes |  0.04164 |    0.00028 |    0.04161 | 0.04119 | 0.04205 |    24.14805 |
| `complex/classes/sloted_classes.py`             |      yes |  0.03893 |    0.00031 |    0.03896 | 0.03835 | 0.03939 |     24.0168 |
| `complex/generators/simple.py`                  |      yes |  0.05584 |      0.001 |    0.05563 | 0.05451 |  0.0578 |    23.37812 |
| `dummy/dummy.py`                                |      yes |  0.02957 |    0.00033 |    0.02967 |  0.0291 | 0.03003 |    22.59688 |
| `long_run/database/postgresql.py`               |      yes |  0.14157 |    0.00079 |    0.14142 |  0.1409 | 0.14365 |    25.92773 |
| `long_run/database/sqlite_.py`                  |      yes |  0.55549 |    0.00313 |    0.55487 | 0.55211 | 0.56287 |    64.85352 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |  0.59631 |    0.00781 |    0.59548 | 0.58813 | 0.61298 |    63.09492 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.06519 |     0.0013 |    0.06495 | 0.06411 | 0.06872 |    22.54297 |
| `long_run/processes/collect_names_from_site.py` |      yes |  1.94361 |     0.0563 |    1.94593 | 1.84982 |  2.0507 |    44.05508 |
| `long_run/processes/generate_fake_data.py`      |      yes |  0.75721 |    0.00483 |    0.75709 |  0.7479 | 0.76465 |    67.21836 |
| `math/haversine.py`                             |      yes |  0.59396 |    0.01575 |    0.59097 |  0.5745 | 0.62683 |    22.23281 |
| `math/mandelbrot.py`                            |      yes |  3.04284 |    0.05081 |     3.0181 | 3.00886 | 3.16034 |    41.37227 |
| `math/pow_simple.py`                            |      yes |  0.41239 |     0.0066 |    0.41022 | 0.40789 | 0.43039 |    22.25234 |
| `math/pow_using_math.py`                        |      yes |  1.42719 |    0.06015 |    1.42477 | 1.34366 | 1.51858 |    22.24375 |
| `modules/json/json_module.py`                   |      yes |   0.3366 |    0.00435 |     0.3369 | 0.33126 | 0.34672 |    22.38008 |
| `modules/json/orjson_module.py`                 |      yes |  0.21476 |     0.0022 |    0.21517 | 0.21227 | 0.21926 |     22.8457 |

### **Python 3.11**

```bash
Python 3.11.3

Linux 538e9dcc3cad 5.15.0-73-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078816 kB
MemFree:         9019292 kB
MemAvailable:   14578136 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  0.74208 |    0.01114 |    0.73886 | 0.73391 |  0.7725 |    34.48086 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  0.75041 |    0.01329 |    0.74871 | 0.73445 | 0.77556 |    34.81758 |
| `algorithm/search/index.py`                     |      yes |  0.75371 |    0.00988 |    0.75049 | 0.74506 | 0.77591 |    34.81133 |
| `algorithm/search/linear.py`                    |      yes |  0.79248 |    0.00874 |    0.79227 | 0.77609 | 0.81094 |    34.52656 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.06991 |    0.00043 |     0.0699 | 0.06935 | 0.07067 |    25.21992 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.06966 |     0.0004 |    0.06974 | 0.06876 | 0.07018 |    25.68516 |
| `complex/classes/classes.py`                    |      yes |  0.01982 |    0.00012 |    0.01979 | 0.01969 | 0.02002 |     26.4832 |
| `complex/classes/dataclasses_.py`               |      yes |  0.10783 |    0.00079 |    0.10799 | 0.10659 | 0.10891 |    26.51797 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.07939 |    0.00038 |    0.07949 |  0.0786 | 0.07977 |    26.02188 |
| `complex/classes/simplenamespace.py`            |      yes |  0.02503 |    0.00028 |    0.02497 | 0.02462 | 0.02553 |    27.53906 |
| `complex/classes/sloted_classes.py`             |      yes |  0.02035 |    0.00089 |    0.02012 | 0.01956 | 0.02259 |    27.14609 |
| `complex/generators/simple.py`                  |      yes |  0.03622 |    0.00038 |    0.03619 | 0.03569 | 0.03686 |    27.17539 |
| `dummy/dummy.py`                                |      yes |  0.01617 |    0.00341 |    0.01534 | 0.01264 | 0.01998 |    25.23867 |
| `long_run/database/postgresql.py`               |      yes |  0.13969 |    0.00063 |    0.13961 | 0.13885 | 0.14072 |    28.92227 |
| `long_run/database/sqlite_.py`                  |      yes |  0.55768 |    0.00672 |    0.55555 | 0.55099 | 0.57189 |    70.33125 |
| `long_run/file/load_titanic_csv_pandas.py`      |      yes |  0.58374 |    0.00317 |     0.5823 | 0.57994 | 0.58844 |    68.85391 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |  0.05562 |    0.00023 |    0.05565 |  0.0553 | 0.05596 |    25.52305 |
| `long_run/processes/collect_names_from_site.py` |      yes |  1.59234 |    0.05348 |    1.59353 | 1.52531 | 1.69015 |    46.32031 |
| `long_run/processes/generate_fake_data.py`      |      yes |  0.75536 |    0.00902 |    0.75281 | 0.74249 | 0.77529 |    71.86016 |
| `math/haversine.py`                             |      yes |  0.50955 |    0.00854 |    0.51161 | 0.49751 | 0.52084 |    25.70508 |
| `math/mandelbrot.py`                            |      yes |   3.0378 |    0.04217 |    3.01757 | 3.00487 |  3.1163 |    39.04258 |
| `math/pow_simple.py`                            |      yes |  0.34476 |    0.00077 |    0.34481 | 0.34341 | 0.34627 |    25.68047 |
| `math/pow_using_math.py`                        |      yes |  1.21615 |    0.01073 |     1.2134 | 1.20651 |  1.2425 |    25.15273 |
| `modules/json/json_module.py`                   |      yes |  0.29123 |    0.00324 |    0.29155 | 0.28524 | 0.29658 |    25.31914 |
| `modules/json/orjson_module.py`                 |      yes |  0.17349 |    0.00078 |    0.17342 | 0.17267 | 0.17481 |     25.9457 |

### **Python 3.12**

```bash
Python 3.12.0b1

Linux 7240ad5dd5fd 5.15.0-73-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16078816 kB
MemFree:         9012932 kB
MemAvailable:   14571092 kB
```

| Command                                         | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
| :---------------------------------------------- | -------: | -------: | ---------: | ---------: | ------: | ------: | ----------: |
| `algorithm/search/bin.py`                       |      yes |  0.87334 |    0.00658 |    0.87386 | 0.86533 | 0.88607 |    34.37383 |
| `algorithm/search/hashmap_lookup.py`            |      yes |  0.88242 |    0.01123 |    0.88216 |  0.8683 | 0.89972 |    34.92344 |
| `algorithm/search/index.py`                     |      yes |  0.89239 |    0.00994 |    0.89155 | 0.87883 | 0.91381 |    34.26094 |
| `algorithm/search/linear.py`                    |      yes |  0.97048 |    0.02938 |    0.96733 | 0.93402 | 1.02846 |    34.33242 |
| `algorithm/twosum/twosum.py`                    |      yes |  0.08345 |    0.00032 |    0.08342 | 0.08302 | 0.08416 |    26.40391 |
| `algorithm/twosum/twosum_naive.py`              |      yes |  0.08342 |    0.00095 |    0.08318 |  0.0825 |  0.0859 |    26.53633 |
| `complex/classes/classes.py`                    |      yes |  0.02283 |    0.00125 |    0.02231 |  0.0216 | 0.02467 |    27.19531 |
| `complex/classes/dataclasses_.py`               |      yes |  0.12639 |    0.00269 |    0.12579 |  0.1249 |  0.1339 |    26.42617 |
| `complex/classes/namedtuple_classes.py`         |      yes |  0.09343 |    0.00095 |    0.09332 | 0.09247 | 0.09573 |    26.65547 |
| `complex/classes/simplenamespace.py`            |      yes |  0.02718 |    0.00049 |    0.02717 | 0.02644 | 0.02803 |    28.38906 |
| `complex/classes/sloted_classes.py`             |      yes |  0.02081 |     0.0003 |    0.02087 | 0.02038 | 0.02132 |    27.08789 |
| `complex/generators/simple.py`                  |      yes |  0.03889 |    0.00039 |    0.03881 | 0.03835 | 0.03963 |    27.91758 |
| `dummy/dummy.py`                                |      yes |  0.01526 |    0.00193 |    0.01438 | 0.01425 | 0.01971 |    26.51719 |
| `long_run/database/postgresql.py`               |      yes |  0.16018 |    0.00179 |     0.1596 | 0.15905 | 0.16517 |    29.88086 |
| `long_run/database/sqlite_.py`                  |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/file/load_titanic_csv_pandas.py`      |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/file/load_titanic_csv_python.py`      |      yes |   0.0637 |    0.00087 |    0.06342 | 0.06288 | 0.06591 |     26.5125 |
| `long_run/processes/collect_names_from_site.py` |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `long_run/processes/generate_fake_data.py`      |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `math/haversine.py`                             |      yes |  0.58472 |    0.00783 |    0.58556 |  0.5714 | 0.59453 |    26.58086 |
| `math/mandelbrot.py`                            |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
| `math/pow_simple.py`                            |      yes |   0.3284 |    0.00595 |    0.32711 | 0.32235 | 0.33653 |    26.51562 |
| `math/pow_using_math.py`                        |      yes |  1.31011 |    0.02473 |    1.30516 | 1.28479 | 1.36133 |    26.50195 |
| `modules/json/json_module.py`                   |      yes |  0.29574 |    0.00369 |    0.29536 | 0.28833 | 0.30175 |    27.14023 |
| `modules/json/orjson_module.py`                 |       no |       -1 |         -1 |         -1 |      -1 |      -1 |          -1 |
