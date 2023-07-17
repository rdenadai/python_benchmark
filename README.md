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

> Last run: Mon Jul 17 02:10:13 UTC 2023
### **Comparison**

#### How much faster 3.12 is? (Mean / Median from 3.6 to 3.11)
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 6.21% / 6.82% | -0.86% / 0.51% | -0.42% / 0.47% | -11.15% / -10.26% | -24.24% / -23.44% |
| `algorithm/search/hashmap_lookup.py` | -53.18% / -59.68% | -56.61% / -62.63% | -17.82% / -55.99% | -61.10% / -66.54% | -66.58% / -71.25% |
| `algorithm/search/index.py` | 6.55% / 5.55% | 1.06% / 0.43% | 1.04% / 0.75% | -10.82% / -11.19% | -23.09% / -23.56% |
| `algorithm/search/linear.py` | -68.64% / -68.72% | -70.78% / -70.69% | -69.63% / -69.83% | -73.68% / -73.60% | -77.44% / -77.36% |
| `algorithm/twosum/twosum.py` | -74.83% / -74.67% | -79.16% / -79.10% | -72.52% / -72.44% | -74.47% / -74.24% | -75.39% / -75.25% |
| `algorithm/twosum/twosum_naive.py` | -74.76% / -74.75% | -79.28% / -79.26% | -72.12% / -72.16% | -74.84% / -74.81% | -75.45% / -75.32% |
| `complex/classes/classes.py` | 98.48% / 99.14% | 78.09% / 78.02% | 620.39% / 623.34% | 105.40% / 88.80% | -6.34% / -5.90% |
| `complex/classes/dataclasses_.py` | -- / -- | -80.32% / -80.24% | -72.13% / -71.94% | -74.71% / -74.69% | -75.67% / -75.64% |
| `complex/classes/namedtuple_classes.py` | -10.73% / -10.66% | -25.10% / -25.34% | 222.56% / 236.40% | -10.20% / -10.00% | -16.54% / -16.43% |
| `complex/classes/simplenamespace.py` | 112.72% / 110.66% | 37.40% / 36.64% | 490.13% / 487.55% | 52.75% / 51.87% | -12.60% / -13.00% |
| `complex/classes/sloted_classes.py` | 70.53% / 84.76% | 50.65% / 62.56% | 78.50% / 93.67% | 61.21% / 74.99% | -22.45% / -16.18% |
| `complex/generators/simple.py` | -53.06% / -53.23% | -56.64% / -56.70% | -52.96% / -52.95% | -56.82% / -57.03% | -73.93% / -74.16% |
| `dummy/dummy.py` | -30.94% / -25.10% | -44.70% / -40.31% | -30.77% / -24.84% | -34.82% / -29.09% | -72.30% / -70.29% |
| `long_run/database/postgresql.py` | -20.22% / -20.01% | -26.39% / -25.96% | 227.38% / 226.16% | -13.37% / -12.62% | -14.77% / -14.85% |
| `long_run/database/sqlite_.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/file/load_titanic_csv_pandas.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/file/load_titanic_csv_python.py` | -72.49% / -72.67% | -74.45% / -74.55% | 12.51% / 10.07% | -72.30% / -72.37% | -74.58% / -74.80% |
| `long_run/processes/collect_names_from_site.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/processes/generate_fake_data.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/processes/maze_generator.py` | 79.98% / 80.85% | 73.19% / 76.07% | 79.25% / 80.19% | 39.04% / 35.93% | -6.28% / -7.73% |
| `long_run/text/clean_text.py` | -2.41% / -1.65% | -6.60% / -5.23% | 10.55% / 10.46% | -6.64% / -5.87% | -18.53% / -17.88% |
| `long_run/text/count_words.py` | -69.75% / -69.65% | -72.33% / -72.20% | -65.54% / -65.67% | -69.37% / -69.30% | -73.94% / -73.77% |
| `math/haversine.py` | -64.39% / -64.43% | -62.07% / -61.89% | 26.63% / 26.68% | -68.73% / -68.77% | -73.66% / -73.60% |
| `math/mandelbrot.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `math/pow_simple.py` | 31.70% / 31.05% | 35.56% / 34.49% | 36.00% / 36.14% | 29.52% / 29.24% | -5.77% / -6.21% |
| `math/pow_using_math.py` | 29.42% / 29.88% | 39.62% / 40.36% | 12.80% / 14.05% | 3.70% / 4.32% | -10.61% / -9.94% |
| `modules/json/json_module.py` | 16.73% / 16.56% | 17.42% / 17.49% | 286.36% / 286.20% | 0.49% / 0.44% | -6.50% / -6.85% |
| `modules/json/orjson_module.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
---

#### How much more memory 3.12 uses? (Memory diff from 3.6 to 3.11)
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 16.85% | 19.57% | 10.46% | 2.6% | -5.34% |
| `algorithm/search/hashmap_lookup.py` | 21.97% | 19.39% | 18.83% | 8.56% | -5.82% |
| `algorithm/search/index.py` | 14.48% | 18.7% | 9.04% | 2.69% | -7.14% |
| `algorithm/search/linear.py` | 15.05% | 16.77% | 10.34% | 5.04% | -6.26% |
| `algorithm/twosum/twosum.py` | 17.49% | 31.46% | 18.95% | 10.57% | -1.45% |
| `algorithm/twosum/twosum_naive.py` | 17.38% | 30.59% | 21.72% | 7.58% | -1.94% |
| `complex/classes/classes.py` | 23.32% | 35.83% | 22.43% | 8.66% | -3.25% |
| `complex/classes/dataclasses_.py` | -- | 36.8% | 27.3% | 9.92% | -4.95% |
| `complex/classes/namedtuple_classes.py` | 18.29% | 32.39% | 16.4% | 9.76% | -4.85% |
| `complex/classes/simplenamespace.py` | 28.86% | 41.04% | 29.81% | 9.96% | -1.11% |
| `complex/classes/sloted_classes.py` | 24.05% | 35.0% | 24.8% | 6.42% | -2.98% |
| `complex/generators/simple.py` | 28.29% | 40.58% | 30.3% | 10.86% | -2.74% |
| `dummy/dummy.py` | 19.13% | 30.59% | 18.23% | 6.59% | -2.87% |
| `long_run/database/postgresql.py` | 12.47% | 27.39% | 23.99% | 4.28% | -3.79% |
| `long_run/database/sqlite_.py` | -- | -- | -- | -- | -- |
| `long_run/file/load_titanic_csv_pandas.py` | -- | -- | -- | -- | -- |
| `long_run/file/load_titanic_csv_python.py` | 16.0% | 28.72% | 18.02% | 8.38% | -4.66% |
| `long_run/processes/collect_names_from_site.py` | -- | -- | -- | -- | -- |
| `long_run/processes/generate_fake_data.py` | -- | -- | -- | -- | -- |
| `long_run/processes/maze_generator.py` | 21.91% | 29.41% | 16.34% | 9.61% | -2.04% |
| `long_run/text/clean_text.py` | 16.93% | 31.42% | 19.14% | 10.37% | -1.27% |
| `long_run/text/count_words.py` | 21.04% | 33.18% | 23.48% | 10.49% | -2.92% |
| `math/haversine.py` | 17.93% | 29.02% | 23.74% | 9.68% | -5.54% |
| `math/mandelbrot.py` | -- | -- | -- | -- | -- |
| `math/pow_simple.py` | 16.01% | 28.44% | 22.57% | 9.17% | -6.48% |
| `math/pow_using_math.py` | 19.39% | 30.06% | 19.63% | 6.46% | -2.64% |
| `modules/json/json_module.py` | 23.57% | 29.57% | 21.96% | 12.8% | 0.92% |
| `modules/json/orjson_module.py` | -- | -- | -- | -- | -- |
---

#### **Execution**

##### **Mean [s]**
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 1.554 | 1.4505 | 1.45701 | 1.2999 | 1.10848 | 1.46309 |
| `algorithm/search/hashmap_lookup.py` | 1.56261 | 1.44833 | 2.74286 | 1.29852 | 1.11532 | 3.33769 |
| `algorithm/search/index.py` | 1.57464 | 1.49354 | 1.49327 | 1.31801 | 1.13663 | 1.4779 |
| `algorithm/search/linear.py` | 1.64129 | 1.52933 | 1.58938 | 1.37743 | 1.18072 | 5.23375 |
| `algorithm/twosum/twosum.py` | 0.11929 | 0.09875 | 0.13024 | 0.12099 | 0.11662 | 0.47395 |
| `algorithm/twosum/twosum_naive.py` | 0.1204 | 0.09883 | 0.13298 | 0.12003 | 0.1171 | 0.47702 |
| `complex/classes/classes.py` | 0.06288 | 0.05642 | 0.22822 | 0.06507 | 0.02967 | 0.03168 |
| `complex/classes/dataclasses_.py` | -- | 0.14339 | 0.20307 | 0.18426 | 0.17727 | 0.7286 |
| `complex/classes/namedtuple_classes.py` | 0.13396 | 0.1124 | 0.48407 | 0.13476 | 0.12525 | 0.15007 |
| `complex/classes/simplenamespace.py` | 0.08832 | 0.05705 | 0.24502 | 0.06342 | 0.03629 | 0.04152 |
| `complex/classes/sloted_classes.py` | 0.06313 | 0.05577 | 0.06608 | 0.05968 | 0.02871 | 0.03702 |
| `complex/generators/simple.py` | 0.09339 | 0.08627 | 0.09358 | 0.0859 | 0.05187 | 0.19894 |
| `dummy/dummy.py` | 0.04984 | 0.03991 | 0.04996 | 0.04704 | 0.01999 | 0.07217 |
| `long_run/database/postgresql.py` | 0.2168 | 0.20004 | 0.88966 | 0.23542 | 0.2316 | 0.27175 |
| `long_run/database/sqlite_.py` | 0.79398 | 0.67524 | 3.09532 | 0.80464 | 0.83387 | -- |
| `long_run/file/load_titanic_csv_pandas.py` | 0.89796 | 0.74735 | 0.90615 | 0.86849 | 0.90332 | -- |
| `long_run/file/load_titanic_csv_python.py` | 0.10251 | 0.0952 | 0.41918 | 0.1032 | 0.09469 | 0.37257 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 4.72987 | 1.64788 | 1.58295 | -- |
| `long_run/processes/generate_fake_data.py` | 1.16916 | 1.0527 | 1.19824 | 1.15325 | 1.12875 | -- |
| `long_run/processes/maze_generator.py` | 0.28185 | 0.27121 | 0.28071 | 0.21774 | 0.14676 | 0.1566 |
| `long_run/text/clean_text.py` | 0.29834 | 0.28555 | 0.33796 | 0.28541 | 0.24907 | 0.30572 |
| `long_run/text/count_words.py` | 0.12927 | 0.11827 | 0.14727 | 0.13089 | 0.11135 | 0.42736 |
| `math/haversine.py` | 0.86584 | 0.92231 | 3.07935 | 0.76051 | 0.64051 | 2.43176 |
| `math/mandelbrot.py` | 4.56218 | 4.49425 | 4.11609 | 3.86269 | 3.86186 | -- |
| `math/pow_simple.py` | 0.52909 | 0.54458 | 0.54636 | 0.52031 | 0.37856 | 0.40173 |
| `math/pow_using_math.py` | 1.65817 | 1.78883 | 1.44528 | 1.32867 | 1.14534 | 1.28125 |
| `modules/json/json_module.py` | 0.57626 | 0.5797 | 1.90736 | 0.4961 | 0.46161 | 0.49368 |
| `modules/json/orjson_module.py` | 0.38301 | 0.31499 | 1.3125 | 0.35738 | 0.28517 | -- |

##### **Median [s]**
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 1.54732 | 1.45588 | 1.45523 | 1.29984 | 1.10892 | 1.44847 |
| `algorithm/search/hashmap_lookup.py` | 1.56153 | 1.44716 | 1.70452 | 1.29573 | 1.11352 | 3.87262 |
| `algorithm/search/index.py` | 1.56618 | 1.49021 | 1.49498 | 1.31779 | 1.13414 | 1.48378 |
| `algorithm/search/linear.py` | 1.63035 | 1.5279 | 1.57288 | 1.37636 | 1.18023 | 5.21283 |
| `algorithm/twosum/twosum.py` | 0.11931 | 0.09847 | 0.12983 | 0.12132 | 0.11657 | 0.47105 |
| `algorithm/twosum/twosum_naive.py` | 0.12048 | 0.09899 | 0.13286 | 0.12022 | 0.11777 | 0.47724 |
| `complex/classes/classes.py` | 0.06279 | 0.05613 | 0.22807 | 0.05953 | 0.02967 | 0.03153 |
| `complex/classes/dataclasses_.py` | -- | 0.14337 | 0.20355 | 0.18365 | 0.17675 | 0.72552 |
| `complex/classes/namedtuple_classes.py` | 0.13395 | 0.11195 | 0.5044 | 0.13494 | 0.12531 | 0.14994 |
| `complex/classes/simplenamespace.py` | 0.08797 | 0.05706 | 0.24536 | 0.06342 | 0.03633 | 0.04176 |
| `complex/classes/sloted_classes.py` | 0.06302 | 0.05545 | 0.06606 | 0.05969 | 0.02859 | 0.03411 |
| `complex/generators/simple.py` | 0.09317 | 0.08625 | 0.09372 | 0.0856 | 0.05147 | 0.1992 |
| `dummy/dummy.py` | 0.04994 | 0.0398 | 0.05012 | 0.04728 | 0.01981 | 0.06668 |
| `long_run/database/postgresql.py` | 0.21633 | 0.20025 | 0.88213 | 0.23632 | 0.23031 | 0.27046 |
| `long_run/database/sqlite_.py` | 0.79165 | 0.67313 | 3.07644 | 0.80311 | 0.83194 | -- |
| `long_run/file/load_titanic_csv_pandas.py` | 0.89711 | 0.74541 | 0.90591 | 0.86657 | 0.90562 | -- |
| `long_run/file/load_titanic_csv_python.py` | 0.10209 | 0.09507 | 0.41122 | 0.10321 | 0.09414 | 0.37361 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 4.71525 | 1.65439 | 1.53328 | -- |
| `long_run/processes/generate_fake_data.py` | 1.17479 | 1.04861 | 1.19613 | 1.15232 | 1.12299 | -- |
| `long_run/processes/maze_generator.py` | 0.28341 | 0.27592 | 0.28238 | 0.21302 | 0.14459 | 0.15671 |
| `long_run/text/clean_text.py` | 0.29821 | 0.28735 | 0.33494 | 0.2854 | 0.24899 | 0.30321 |
| `long_run/text/count_words.py` | 0.1289 | 0.11804 | 0.1458 | 0.13038 | 0.11141 | 0.42468 |
| `math/haversine.py` | 0.86301 | 0.92468 | 3.07393 | 0.75774 | 0.64067 | 2.42645 |
| `math/mandelbrot.py` | 4.54635 | 4.51686 | 3.97567 | 3.83777 | 3.85169 | -- |
| `math/pow_simple.py` | 0.52598 | 0.53977 | 0.54641 | 0.51872 | 0.37643 | 0.40135 |
| `math/pow_using_math.py` | 1.65226 | 1.78561 | 1.45088 | 1.32709 | 1.14566 | 1.27212 |
| `modules/json/json_module.py` | 0.57271 | 0.57725 | 1.89753 | 0.49349 | 0.45766 | 0.49133 |
| `modules/json/orjson_module.py` | 0.38254 | 0.31372 | 1.31322 | 0.35882 | 0.28559 | -- |

#### **Memory Usage**

##### **MEM [MB]**
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 28.62148 | 27.96992 | 30.27656 | 32.59805 | 35.33008 | 33.44492 |
| `algorithm/search/hashmap_lookup.py` | 27.93242 | 28.53672 | 28.66992 | 31.38398 | 36.17305 | 34.06914 |
| `algorithm/search/index.py` | 28.61719 | 27.60117 | 30.04531 | 31.90273 | 35.28164 | 32.76172 |
| `algorithm/search/linear.py` | 28.5625 | 28.14297 | 29.78281 | 31.28398 | 35.05547 | 32.86133 |
| `algorithm/twosum/twosum.py` | 22.21641 | 19.85625 | 21.94453 | 23.60664 | 26.48672 | 26.10273 |
| `algorithm/twosum/twosum_naive.py` | 22.09844 | 19.86211 | 21.31094 | 24.11133 | 26.45156 | 25.93867 |
| `complex/classes/classes.py` | 21.77891 | 19.77305 | 21.93711 | 24.71719 | 27.7582 | 26.85703 |
| `complex/classes/dataclasses_.py` | -- | 19.82188 | 21.30156 | 24.66797 | 28.5293 | 27.11602 |
| `complex/classes/namedtuple_classes.py` | 22.10703 | 19.75273 | 22.4668 | 23.82656 | 27.48398 | 26.15117 |
| `complex/classes/simplenamespace.py` | 21.70977 | 19.83594 | 21.55195 | 25.44141 | 28.29141 | 27.97617 |
| `complex/classes/sloted_classes.py` | 21.63711 | 19.88125 | 21.50625 | 25.22148 | 27.66445 | 26.84062 |
| `complex/generators/simple.py` | 21.80195 | 19.89531 | 21.46484 | 25.22813 | 28.75742 | 27.96875 |
| `dummy/dummy.py` | 21.62539 | 19.72734 | 21.78984 | 24.16914 | 26.52305 | 25.76289 |
| `long_run/database/postgresql.py` | 27.18633 | 24.00117 | 24.65898 | 29.32031 | 31.77891 | 30.57539 |
| `long_run/database/sqlite_.py` | 63.22891 | 64.45195 | 66.94492 | 66.01055 | 71.79961 | -- |
| `long_run/file/load_titanic_csv_pandas.py` | 61.86602 | 63.10156 | 63.70781 | 65.07227 | 70.16211 | -- |
| `long_run/file/load_titanic_csv_python.py` | 22.0 | 19.82656 | 21.62266 | 23.54687 | 26.76602 | 25.51992 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 43.25469 | 45.06953 | 47.28477 | -- |
| `long_run/processes/generate_fake_data.py` | 64.51562 | 67.28828 | 67.89063 | 68.19844 | 71.56992 | -- |
| `long_run/processes/maze_generator.py` | 21.72188 | 20.46367 | 22.7625 | 24.15977 | 27.03438 | 26.48164 |
| `long_run/text/clean_text.py` | 22.32383 | 19.86211 | 21.91016 | 23.65078 | 26.43867 | 26.10273 |
| `long_run/text/count_words.py` | 21.59219 | 19.625 | 21.16641 | 23.65391 | 26.92344 | 26.13594 |
| `math/haversine.py` | 21.62266 | 19.76367 | 20.60625 | 23.24883 | 26.99375 | 25.49883 |
| `math/mandelbrot.py` | 35.95117 | 33.97891 | 41.84258 | 39.29336 | 40.43672 | -- |
| `math/pow_simple.py` | 21.73008 | 19.62656 | 20.56641 | 23.0918 | 26.95547 | 25.20898 |
| `math/pow_using_math.py` | 21.55859 | 19.78945 | 21.51563 | 24.17734 | 26.4375 | 25.73828 |
| `modules/json/json_module.py` | 21.73711 | 20.73086 | 22.02383 | 23.81289 | 26.61445 | 26.86016 |
| `modules/json/orjson_module.py` | 22.5043 | 21.06445 | 21.71406 | 24.24766 | 27.54844 | -- |

---


### **Python 3.6**

```bash
Python 3.6.15

Linux 0a247aa7c4a6 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          2
Thread(s) per core:              1
Core(s) per socket:              2
NUMA node(s):                    1
Model name:                      Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
NUMA node0 CPU(s):               0,1

MemTotal:        4014620 kB
MemFree:          859884 kB
MemAvailable:    3344904 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.554 | 0.02681 | 1.54732 | 1.50546 | 1.59385 | 28.62148 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.56261 | 0.02542 | 1.56153 | 1.52927 | 1.59123 | 27.93242 |
| `algorithm/search/index.py` | yes | 1.57464 | 0.02514 | 1.56618 | 1.55301 | 1.63572 | 28.61719 |
| `algorithm/search/linear.py` | yes | 1.64129 | 0.03366 | 1.63035 | 1.60124 | 1.69259 | 28.5625 |
| `algorithm/twosum/twosum.py` | yes | 0.11929 | 0.00186 | 0.11931 | 0.11701 | 0.12398 | 22.21641 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.1204 | 0.00116 | 0.12048 | 0.11861 | 0.12285 | 22.09844 |
| `complex/classes/classes.py` | yes | 0.06288 | 0.00053 | 0.06279 | 0.06221 | 0.06415 | 21.77891 |
| `complex/classes/dataclasses_.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `complex/classes/namedtuple_classes.py` | yes | 0.13396 | 0.00097 | 0.13395 | 0.13279 | 0.13604 | 22.10703 |
| `complex/classes/simplenamespace.py` | yes | 0.08832 | 0.00114 | 0.08797 | 0.08711 | 0.09014 | 21.70977 |
| `complex/classes/sloted_classes.py` | yes | 0.06313 | 0.00042 | 0.06302 | 0.06267 | 0.06392 | 21.63711 |
| `complex/generators/simple.py` | yes | 0.09339 | 0.00093 | 0.09317 | 0.09218 | 0.09541 | 21.80195 |
| `dummy/dummy.py` | yes | 0.04984 | 0.00083 | 0.04994 | 0.04838 | 0.05143 | 21.62539 |
| `long_run/database/postgresql.py` | yes | 0.2168 | 0.00176 | 0.21633 | 0.21511 | 0.22025 | 27.18633 |
| `long_run/database/sqlite_.py` | yes | 0.79398 | 0.01128 | 0.79165 | 0.78167 | 0.81539 | 63.22891 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.89796 | 0.01325 | 0.89711 | 0.87831 | 0.91623 | 61.86602 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.10251 | 0.00116 | 0.10209 | 0.10118 | 0.10446 | 22.0 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | yes | 1.16916 | 0.01924 | 1.17479 | 1.13614 | 1.1969 | 64.51562 |
| `long_run/processes/maze_generator.py` | yes | 0.28185 | 0.01062 | 0.28341 | 0.26326 | 0.2946 | 21.72188 |
| `long_run/text/clean_text.py` | yes | 0.29834 | 0.00198 | 0.29821 | 0.29553 | 0.3025 | 22.32383 |
| `long_run/text/count_words.py` | yes | 0.12927 | 0.00131 | 0.1289 | 0.12729 | 0.13171 | 21.59219 |
| `math/haversine.py` | yes | 0.86584 | 0.014 | 0.86301 | 0.85193 | 0.89176 | 21.62266 |
| `math/mandelbrot.py` | yes | 4.56218 | 0.04302 | 4.54635 | 4.52924 | 4.6557 | 35.95117 |
| `math/pow_simple.py` | yes | 0.52909 | 0.00519 | 0.52598 | 0.52499 | 0.54044 | 21.73008 |
| `math/pow_using_math.py` | yes | 1.65817 | 0.0227 | 1.65226 | 1.63424 | 1.70136 | 21.55859 |
| `modules/json/json_module.py` | yes | 0.57626 | 0.0107 | 0.57271 | 0.56605 | 0.5986 | 21.73711 |
| `modules/json/orjson_module.py` | yes | 0.38301 | 0.00392 | 0.38254 | 0.37801 | 0.3908 | 22.5043 |


### **Python 3.7**

```bash
Python 3.7.17

Linux 6383f41df56f 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          2
Thread(s) per core:              1
Core(s) per socket:              2
NUMA node(s):                    1
Model name:                      Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
NUMA node0 CPU(s):               0,1

MemTotal:        4014620 kB
MemFree:          873364 kB
MemAvailable:    3326448 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.4505 | 0.01654 | 1.45588 | 1.42886 | 1.4753 | 27.96992 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.44833 | 0.01351 | 1.44716 | 1.42881 | 1.46905 | 28.53672 |
| `algorithm/search/index.py` | yes | 1.49354 | 0.02036 | 1.49021 | 1.46872 | 1.53033 | 27.60117 |
| `algorithm/search/linear.py` | yes | 1.52933 | 0.01221 | 1.5279 | 1.50953 | 1.54794 | 28.14297 |
| `algorithm/twosum/twosum.py` | yes | 0.09875 | 0.00135 | 0.09847 | 0.09752 | 0.10109 | 19.85625 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.09883 | 0.0008 | 0.09899 | 0.09749 | 0.09976 | 19.86211 |
| `complex/classes/classes.py` | yes | 0.05642 | 0.00102 | 0.05613 | 0.05557 | 0.05891 | 19.77305 |
| `complex/classes/dataclasses_.py` | yes | 0.14339 | 0.00075 | 0.14337 | 0.14211 | 0.14465 | 19.82188 |
| `complex/classes/namedtuple_classes.py` | yes | 0.1124 | 0.00146 | 0.11195 | 0.11072 | 0.11521 | 19.75273 |
| `complex/classes/simplenamespace.py` | yes | 0.05705 | 0.00062 | 0.05706 | 0.05631 | 0.05818 | 19.83594 |
| `complex/classes/sloted_classes.py` | yes | 0.05577 | 0.00126 | 0.05545 | 0.05419 | 0.05787 | 19.88125 |
| `complex/generators/simple.py` | yes | 0.08627 | 0.00073 | 0.08625 | 0.08523 | 0.08757 | 19.89531 |
| `dummy/dummy.py` | yes | 0.03991 | 0.00038 | 0.0398 | 0.0395 | 0.04066 | 19.72734 |
| `long_run/database/postgresql.py` | yes | 0.20004 | 0.00189 | 0.20025 | 0.19738 | 0.20264 | 24.00117 |
| `long_run/database/sqlite_.py` | yes | 0.67524 | 0.01036 | 0.67313 | 0.66052 | 0.69267 | 64.45195 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.74735 | 0.00762 | 0.74541 | 0.73822 | 0.76029 | 63.10156 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.0952 | 0.00173 | 0.09507 | 0.09297 | 0.09866 | 19.82656 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | yes | 1.0527 | 0.01525 | 1.04861 | 1.03362 | 1.07898 | 67.28828 |
| `long_run/processes/maze_generator.py` | yes | 0.27121 | 0.02072 | 0.27592 | 0.22529 | 0.29003 | 20.46367 |
| `long_run/text/clean_text.py` | yes | 0.28555 | 0.00592 | 0.28735 | 0.27758 | 0.29253 | 19.86211 |
| `long_run/text/count_words.py` | yes | 0.11827 | 0.00088 | 0.11804 | 0.11711 | 0.11986 | 19.625 |
| `math/haversine.py` | yes | 0.92231 | 0.01577 | 0.92468 | 0.89468 | 0.94858 | 19.76367 |
| `math/mandelbrot.py` | yes | 4.49425 | 0.08446 | 4.51686 | 4.25716 | 4.54777 | 33.97891 |
| `math/pow_simple.py` | yes | 0.54458 | 0.01132 | 0.53977 | 0.53331 | 0.56502 | 19.62656 |
| `math/pow_using_math.py` | yes | 1.78883 | 0.01106 | 1.78561 | 1.776 | 1.81146 | 19.78945 |
| `modules/json/json_module.py` | yes | 0.5797 | 0.00951 | 0.57725 | 0.5653 | 0.59735 | 20.73086 |
| `modules/json/orjson_module.py` | yes | 0.31499 | 0.00334 | 0.31372 | 0.31155 | 0.32074 | 21.06445 |


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

Linux c7b16a8cc6ce 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          2
Thread(s) per core:              1
Core(s) per socket:              2
NUMA node(s):                    1
Model name:                      Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
NUMA node0 CPU(s):               0,1

MemTotal:        4014620 kB
MemFree:          828488 kB
MemAvailable:    3319232 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.45701 | 0.0176 | 1.45523 | 1.43491 | 1.48779 | 30.27656 |
| `algorithm/search/hashmap_lookup.py` | yes | 2.74286 | 1.58986 | 1.70452 | 1.52887 | 5.09925 | 28.66992 |
| `algorithm/search/index.py` | yes | 1.49327 | 0.01645 | 1.49498 | 1.46485 | 1.52197 | 30.04531 |
| `algorithm/search/linear.py` | yes | 1.58938 | 0.06567 | 1.57288 | 1.54053 | 1.76341 | 29.78281 |
| `algorithm/twosum/twosum.py` | yes | 0.13024 | 0.00105 | 0.12983 | 0.12923 | 0.13227 | 21.94453 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.13298 | 0.00114 | 0.13286 | 0.13156 | 0.13502 | 21.31094 |
| `complex/classes/classes.py` | yes | 0.22822 | 0.00892 | 0.22807 | 0.21345 | 0.24214 | 21.93711 |
| `complex/classes/dataclasses_.py` | yes | 0.20307 | 0.00189 | 0.20355 | 0.19965 | 0.20578 | 21.30156 |
| `complex/classes/namedtuple_classes.py` | yes | 0.48407 | 0.08136 | 0.5044 | 0.26058 | 0.54977 | 22.4668 |
| `complex/classes/simplenamespace.py` | yes | 0.24502 | 0.0099 | 0.24536 | 0.23355 | 0.26312 | 21.55195 |
| `complex/classes/sloted_classes.py` | yes | 0.06608 | 0.00085 | 0.06606 | 0.06501 | 0.06778 | 21.50625 |
| `complex/generators/simple.py` | yes | 0.09358 | 0.00129 | 0.09372 | 0.09157 | 0.09536 | 21.46484 |
| `dummy/dummy.py` | yes | 0.04996 | 0.00058 | 0.05012 | 0.0488 | 0.05075 | 21.78984 |
| `long_run/database/postgresql.py` | yes | 0.88966 | 0.03044 | 0.88213 | 0.85657 | 0.96533 | 24.65898 |
| `long_run/database/sqlite_.py` | yes | 3.09532 | 0.06597 | 3.07644 | 3.02695 | 3.23404 | 66.94492 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.90615 | 0.01006 | 0.90591 | 0.893 | 0.92234 | 63.70781 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.41918 | 0.02421 | 0.41122 | 0.38193 | 0.46012 | 21.62266 |
| `long_run/processes/collect_names_from_site.py` | yes | 4.72987 | 0.05731 | 4.71525 | 4.62042 | 4.81013 | 43.25469 |
| `long_run/processes/generate_fake_data.py` | yes | 1.19824 | 0.00987 | 1.19613 | 1.18723 | 1.2216 | 67.89063 |
| `long_run/processes/maze_generator.py` | yes | 0.28071 | 0.01083 | 0.28238 | 0.26215 | 0.29478 | 22.7625 |
| `long_run/text/clean_text.py` | yes | 0.33796 | 0.00983 | 0.33494 | 0.32703 | 0.35407 | 21.91016 |
| `long_run/text/count_words.py` | yes | 0.14727 | 0.00253 | 0.1458 | 0.14461 | 0.15174 | 21.16641 |
| `math/haversine.py` | yes | 3.07935 | 0.04249 | 3.07393 | 3.01164 | 3.13752 | 20.60625 |
| `math/mandelbrot.py` | yes | 4.11609 | 0.27895 | 3.97567 | 3.91239 | 4.78008 | 41.84258 |
| `math/pow_simple.py` | yes | 0.54636 | 0.00166 | 0.54641 | 0.54364 | 0.54902 | 20.56641 |
| `math/pow_using_math.py` | yes | 1.44528 | 0.02161 | 1.45088 | 1.41321 | 1.48334 | 21.51563 |
| `modules/json/json_module.py` | yes | 1.90736 | 0.04606 | 1.89753 | 1.84407 | 1.98515 | 22.02383 |
| `modules/json/orjson_module.py` | yes | 1.3125 | 0.04445 | 1.31322 | 1.23224 | 1.37854 | 21.71406 |


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

Linux b89e6ffa90d1 5.19.0-1025-aws unknown GNU/Linux

CPU(s):                          2
Thread(s) per core:              1
Core(s) per socket:              2
NUMA node(s):                    1
Model name:                      Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
NUMA node0 CPU(s):               0,1

MemTotal:        4014620 kB
MemFree:          951016 kB
MemAvailable:    3344484 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.46309 | 0.07018 | 1.44847 | 1.41481 | 1.65131 | 33.44492 |
| `algorithm/search/hashmap_lookup.py` | yes | 3.33769 | 1.75224 | 3.87262 | 1.41971 | 5.02458 | 34.06914 |
| `algorithm/search/index.py` | yes | 1.4779 | 0.01515 | 1.48378 | 1.4492 | 1.4919 | 32.76172 |
| `algorithm/search/linear.py` | yes | 5.23375 | 0.11966 | 5.21283 | 5.09559 | 5.48381 | 32.86133 |
| `algorithm/twosum/twosum.py` | yes | 0.47395 | 0.01992 | 0.47105 | 0.44855 | 0.52014 | 26.10273 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.47702 | 0.02098 | 0.47724 | 0.45304 | 0.51942 | 25.93867 |
| `complex/classes/classes.py` | yes | 0.03168 | 0.00054 | 0.03153 | 0.03114 | 0.03309 | 26.85703 |
| `complex/classes/dataclasses_.py` | yes | 0.7286 | 0.02459 | 0.72552 | 0.6948 | 0.77662 | 27.11602 |
| `complex/classes/namedtuple_classes.py` | yes | 0.15007 | 0.00186 | 0.14994 | 0.14747 | 0.15306 | 26.15117 |
| `complex/classes/simplenamespace.py` | yes | 0.04152 | 0.00045 | 0.04176 | 0.04082 | 0.04201 | 27.97617 |
| `complex/classes/sloted_classes.py` | yes | 0.03702 | 0.00631 | 0.03411 | 0.03186 | 0.04805 | 26.84062 |
| `complex/generators/simple.py` | yes | 0.19894 | 0.0147 | 0.1992 | 0.17421 | 0.22809 | 27.96875 |
| `dummy/dummy.py` | yes | 0.07217 | 0.0106 | 0.06668 | 0.06073 | 0.08944 | 25.76289 |
| `long_run/database/postgresql.py` | yes | 0.27175 | 0.00592 | 0.27046 | 0.26369 | 0.28287 | 30.57539 |
| `long_run/database/sqlite_.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/file/load_titanic_csv_pandas.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.37257 | 0.0176 | 0.37361 | 0.34922 | 0.40869 | 25.51992 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/maze_generator.py` | yes | 0.1566 | 0.01377 | 0.15671 | 0.14029 | 0.18498 | 26.48164 |
| `long_run/text/clean_text.py` | yes | 0.30572 | 0.00655 | 0.30321 | 0.30037 | 0.31987 | 26.10273 |
| `long_run/text/count_words.py` | yes | 0.42736 | 0.02165 | 0.42468 | 0.39955 | 0.47269 | 26.13594 |
| `math/haversine.py` | yes | 2.43176 | 0.02172 | 2.42645 | 2.4065 | 2.46551 | 25.49883 |
| `math/mandelbrot.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `math/pow_simple.py` | yes | 0.40173 | 0.00268 | 0.40135 | 0.39899 | 0.40851 | 25.20898 |
| `math/pow_using_math.py` | yes | 1.28125 | 0.02012 | 1.27212 | 1.27062 | 1.32729 | 25.73828 |
| `modules/json/json_module.py` | yes | 0.49368 | 0.01203 | 0.49133 | 0.47304 | 0.51707 | 26.86016 |
| `modules/json/orjson_module.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |

