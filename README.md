# Python Benchmark

This is a simple repo to validate and test any (almost any) python program againts all python 3 versions.

- Python 3.6.15
- Python 3.7.17
- Python 3.8.18
- Python 3.9.18
- Python 3.10.13
- Python 3.11.5
- Python 3.12.0rc3

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

> Last run: Wed Sep 20 10:45:48 PM -03 2023
### **Comparison**

#### How much faster 3.12 is? (Mean / Median from 3.11 to 3.6)
| Command | 3.11 | 3.10 | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | -10.58% / -10.87% | 4.19% / 3.95% | 19.91% / 19.38% | 17.94% / 17.55% | 23.81% / 23.11% | 26.28% / 26.72% |
| `algorithm/search/hashmap_lookup.py` | -11.50% / -11.84% | 4.34% / 3.63% | 19.25% / 18.15% | 18.00% / 17.22% | 23.10% / 20.38% | 25.71% / 24.60% |
| `algorithm/search/index.py` | -9.03% / -9.94% | 4.61% / 5.42% | 21.22% / 18.89% | 17.26% / 18.25% | 20.46% / 20.75% | 24.62% / 25.44% |
| `algorithm/search/linear.py` | -10.92% / -11.79% | 1.57% / 2.94% | 16.02% / 17.91% | 16.23% / 16.93% | 19.06% / 19.81% | 23.17% / 23.80% |
| `algorithm/twosum/twosum.py` | -13.38% / -13.54% | -8.13% / -8.00% | 0.39% / -0.11% | -14.30% / -14.19% | -17.75% / -17.87% | -1.64% / -1.59% |
| `algorithm/twosum/twosum_naive.py` | -15.07% / -14.91% | -9.20% / -9.16% | -0.36% / -0.10% | -15.38% / -15.33% | -20.04% / -19.90% | -1.69% / -1.31% |
| `complex/classes/classes.py` | -0.88% / -3.99% | 82.81% / 77.02% | 100.25% / 94.01% | 85.08% / 78.73% | 76.63% / 70.90% | 106.85% / 99.80% |
| `complex/classes/dataclasses_.py` | -13.88% / -13.67% | -7.06% / -7.21% | 1.66% / 1.69% | -18.25% / -18.14% | -20.83% / -21.02% | -- / -- |
| `complex/classes/namedtuple_classes.py` | -7.67% / -11.54% | -6.82% / -6.79% | 0.58% / 1.02% | -10.52% / -10.89% | -14.75% / -14.51% | 3.96% / 4.04% |
| `complex/classes/simplenamespace.py` | -7.47% / -6.45% | 54.22% / 56.23% | 68.48% / 70.19% | 47.36% / 48.65% | 42.94% / 44.28% | 119.93% / 121.75% |
| `complex/classes/sloted_classes.py` | 1.27% / 3.20% | 91.16% / 91.01% | 109.28% / 110.00% | 93.56% / 92.94% | 85.99% / 85.23% | 114.80% / 114.82% |
| `complex/generators/simple.py` | -10.55% / -10.18% | 34.39% / 34.57% | 44.75% / 43.67% | 37.93% / 38.51% | 38.31% / 38.74% | 50.51% / 49.55% |
| `dummy/dummy.py` | -33.03% / -28.95% | 56.29% / 65.65% | 78.17% / 89.60% | 62.37% / 69.81% | 55.29% / 63.01% | 81.40% / 92.75% |
| `long_run/database/postgresql.py` | -14.97% / -14.76% | -13.59% / -13.63% | -4.44% / -4.84% | -15.26% / -15.46% | -19.97% / -19.79% | -12.58% / -12.38% |
| `long_run/database/sqlite_.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/file/load_titanic_csv_pandas.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/file/load_titanic_csv_python.py` | -11.69% / -11.71% | 3.06% / 3.23% | 16.24% / 16.02% | 1.64% / 1.80% | 0.89% / -0.25% | 10.04% / 10.11% |
| `long_run/processes/collect_names_from_site.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/processes/generate_fake_data.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/processes/maze_generator.py` | -6.63% / -0.34% | 46.76% / 54.15% | 71.53% / 71.21% | 76.08% / 82.98% | 67.81% / 67.14% | 83.81% / 86.71% |
| `long_run/text/clean_text.py` | -2.63% / -3.31% | 7.42% / 7.14% | 14.43% / 14.91% | 9.05% / 9.62% | 4.61% / 4.87% | 6.66% / 6.55% |
| `long_run/text/count_words.py` | -8.28% / -8.25% | 10.32% / 10.03% | 21.41% / 20.98% | 9.78% / 9.67% | 5.08% / 4.90% | 14.14% / 14.30% |
| `math/haversine.py` | -8.53% / -9.42% | 3.94% / 3.49% | 13.41% / 13.44% | 3.09% / 2.36% | 8.85% / 9.40% | -1.88% / -3.99% |
| `math/mandelbrot.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `math/pow_simple.py` | 8.56% / 11.32% | 130.34% / 139.57% | 141.75% / 148.25% | 135.82% / 139.99% | 140.46% / 147.73% | 104.96% / 110.26% |
| `math/pow_using_math.py` | -3.92% / -3.54% | 15.55% / 16.50% | 17.36% / 17.99% | 15.52% / 16.20% | 41.94% / 44.52% | 22.96% / 23.40% |
| `modules/json/json_module.py` | -1.10% / -2.01% | 11.16% / 10.92% | 23.69% / 23.12% | 21.81% / 21.22% | 27.79% / 27.30% | 24.05% / 23.68% |
| `modules/json/orjson_module.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `programming_game_benchmark/nbody.py` | -5.02% / -4.77% | 44.49% / 44.24% | 55.50% / 55.60% | 47.36% / 47.18% | 44.99% / 44.88% | 19.34% / 19.30% |
| `programming_game_benchmark/spectral_norm.py` | -11.91% / -11.95% | 3.02% / 2.04% | 14.09% / 14.40% | 10.04% / 9.57% | 17.67% / 16.58% | 5.91% / 6.05% |
---

#### How much more memory 3.12 uses? (Memory diff from 3.11 to 3.6)
| Command | 3.11 | 3.10 | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 0.07% | 10.2% | 17.07% | 19.87% | 12.9% | 23.98% |
| `algorithm/search/hashmap_lookup.py` | -0.42% | 6.51% | 11.47% | 21.69% | 18.28% | 29.12% |
| `algorithm/search/index.py` | -1.16% | 8.41% | 16.68% | 19.2% | 15.72% | 23.66% |
| `algorithm/search/linear.py` | -1.17% | 8.05% | 15.99% | 18.85% | 17.45% | 22.45% |
| `algorithm/twosum/twosum.py` | 4.32% | 14.78% | 17.59% | 27.83% | 30.53% | 25.62% |
| `algorithm/twosum/twosum_naive.py` | 4.85% | 17.98% | 20.93% | 27.16% | 31.46% | 25.26% |
| `complex/classes/classes.py` | 2.01% | 8.18% | 19.88% | 30.56% | 33.42% | 29.27% |
| `complex/classes/dataclasses_.py` | 0.96% | 7.64% | 18.39% | 27.75% | 31.18% | -- |
| `complex/classes/namedtuple_classes.py` | 2.23% | 12.47% | 24.21% | 28.34% | 32.12% | 26.97% |
| `complex/classes/simplenamespace.py` | 3.98% | 15.4% | 27.68% | 35.41% | 40.74% | 34.81% |
| `complex/classes/sloted_classes.py` | 2.08% | 11.04% | 21.84% | 29.08% | 31.97% | 30.36% |
| `complex/generators/simple.py` | 3.24% | 12.36% | 24.54% | 34.12% | 37.85% | 33.15% |
| `dummy/dummy.py` | 3.96% | 16.42% | 19.46% | 27.55% | 32.15% | 28.03% |
| `long_run/database/postgresql.py` | 2.77% | 15.22% | 12.17% | 21.84% | 20.57% | 23.11% |
| `long_run/database/sqlite_.py` | -- | -- | -- | -- | -- | -- |
| `long_run/file/load_titanic_csv_pandas.py` | -- | -- | -- | -- | -- | -- |
| `long_run/file/load_titanic_csv_python.py` | 3.6% | 14.96% | 20.05% | 28.36% | 30.27% | 27.96% |
| `long_run/processes/collect_names_from_site.py` | -- | -- | -- | -- | -- | -- |
| `long_run/processes/generate_fake_data.py` | -- | -- | -- | -- | -- | -- |
| `long_run/processes/maze_generator.py` | 4.75% | 13.32% | 23.98% | 27.94% | 28.5% | 30.16% |
| `long_run/text/clean_text.py` | 4.0% | 14.43% | 18.03% | 27.45% | 30.15% | 24.09% |
| `long_run/text/count_words.py` | 1.91% | 11.93% | 15.25% | 24.84% | 27.85% | 25.2% |
| `math/haversine.py` | 3.81% | 14.53% | 16.05% | 26.23% | 30.53% | 27.37% |
| `math/mandelbrot.py` | -- | -- | -- | -- | -- | -- |
| `math/pow_simple.py` | 3.75% | 13.71% | 16.19% | 27.8% | 29.6% | 27.24% |
| `math/pow_using_math.py` | 3.53% | 13.69% | 17.91% | 27.33% | 29.81% | 27.34% |
| `modules/json/json_module.py` | 6.74% | 17.01% | 21.61% | 28.55% | 27.51% | 31.27% |
| `modules/json/orjson_module.py` | -- | -- | -- | -- | -- | -- |
| `programming_game_benchmark/nbody.py` | 4.86% | 16.26% | 20.97% | 27.84% | 32.9% | 28.91% |
| `programming_game_benchmark/spectral_norm.py` | 6.87% | 16.07% | 22.07% | 27.15% | 26.31% | 29.7% |
---

#### **Execution**

##### **Mean [s]**
| Command | 3.12 | 3.11 | 3.10 | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 1.19305 | 1.06684 | 1.24304 | 1.43058 | 1.40708 | 1.47711 | 1.50654 |
| `algorithm/search/hashmap_lookup.py` | 1.20973 | 1.07066 | 1.26227 | 1.44258 | 1.42754 | 1.48919 | 1.52074 |
| `algorithm/search/index.py` | 1.21941 | 1.10925 | 1.27566 | 1.47812 | 1.42984 | 1.46892 | 1.51963 |
| `algorithm/search/linear.py` | 1.28481 | 1.14456 | 1.30504 | 1.4906 | 1.49334 | 1.52968 | 1.58255 |
| `algorithm/twosum/twosum.py` | 0.08737 | 0.07568 | 0.08027 | 0.08771 | 0.07488 | 0.07186 | 0.08594 |
| `algorithm/twosum/twosum_naive.py` | 0.08863 | 0.07527 | 0.08048 | 0.08831 | 0.075 | 0.07087 | 0.08713 |
| `complex/classes/classes.py` | 0.02379 | 0.02358 | 0.04349 | 0.04764 | 0.04403 | 0.04202 | 0.04921 |
| `complex/classes/dataclasses_.py` | 0.13648 | 0.11754 | 0.12685 | 0.13874 | 0.11157 | 0.10805 | -- |
| `complex/classes/namedtuple_classes.py` | 0.09942 | 0.09179 | 0.09264 | 0.1 | 0.08896 | 0.08476 | 0.10336 |
| `complex/classes/simplenamespace.py` | 0.0296 | 0.02739 | 0.04565 | 0.04987 | 0.04362 | 0.04231 | 0.0651 |
| `complex/classes/sloted_classes.py` | 0.02284 | 0.02313 | 0.04366 | 0.0478 | 0.04421 | 0.04248 | 0.04906 |
| `complex/generators/simple.py` | 0.04664 | 0.04172 | 0.06268 | 0.06751 | 0.06433 | 0.06451 | 0.0702 |
| `dummy/dummy.py` | 0.01892 | 0.01267 | 0.02957 | 0.03371 | 0.03072 | 0.02938 | 0.03432 |
| `long_run/database/postgresql.py` | 0.1803 | 0.15331 | 0.1558 | 0.1723 | 0.15279 | 0.1443 | 0.15762 |
| `long_run/database/sqlite_.py` | -- | 0.6156 | 0.6294 | 0.66581 | 0.61123 | 0.54837 | 0.62974 |
| `long_run/file/load_titanic_csv_pandas.py` | -- | 0.65253 | 0.6695 | 0.72669 | 0.6638 | 0.60413 | 0.70156 |
| `long_run/file/load_titanic_csv_python.py` | 0.0687 | 0.06067 | 0.0708 | 0.07986 | 0.06983 | 0.06931 | 0.0756 |
| `long_run/processes/collect_names_from_site.py` | -- | 1.73261 | 2.02844 | 2.11104 | 2.01815 | -- | -- |
| `long_run/processes/generate_fake_data.py` | -- | 0.82401 | 0.83924 | 0.90444 | 0.82415 | 0.79328 | 0.86927 |
| `long_run/processes/maze_generator.py` | 0.19955 | 0.18632 | 0.29286 | 0.34228 | 0.35137 | 0.33487 | 0.36679 |
| `long_run/text/clean_text.py` | 0.25515 | 0.24845 | 0.27409 | 0.29197 | 0.27825 | 0.2669 | 0.27215 |
| `long_run/text/count_words.py` | 0.08324 | 0.07635 | 0.09183 | 0.10106 | 0.09138 | 0.08747 | 0.09501 |
| `math/haversine.py` | 0.8862 | 0.81059 | 0.9211 | 1.00507 | 0.91357 | 0.96462 | 0.86951 |
| `math/mandelbrot.py` | -- | 2.59351 | 2.58237 | 2.60615 | 3.04262 | 3.06598 | 3.12832 |
| `math/pow_simple.py` | 0.32299 | 0.35064 | 0.74397 | 0.78083 | 0.76167 | 0.77667 | 0.662 |
| `math/pow_using_math.py` | 1.22399 | 1.17603 | 1.41431 | 1.43642 | 1.41396 | 1.73737 | 1.50499 |
| `modules/json/json_module.py` | 0.40526 | 0.40081 | 0.4505 | 0.50125 | 0.49365 | 0.51788 | 0.50273 |
| `modules/json/orjson_module.py` | -- | 0.26654 | 0.30411 | 0.33283 | 0.29604 | 0.26782 | 0.31387 |
| `programming_game_benchmark/nbody.py` | 0.36416 | 0.34589 | 0.52619 | 0.56627 | 0.53661 | 0.52799 | 0.43459 |
| `programming_game_benchmark/spectral_norm.py` | 0.58832 | 0.51826 | 0.60611 | 0.67122 | 0.64739 | 0.69229 | 0.62307 |

##### **Median [s]**
| Command | 3.12 | 3.11 | 3.10 | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 1.19555 | 1.06565 | 1.24279 | 1.42724 | 1.40534 | 1.47179 | 1.51505 |
| `algorithm/search/hashmap_lookup.py` | 1.21419 | 1.07038 | 1.25821 | 1.43456 | 1.42332 | 1.46166 | 1.51288 |
| `algorithm/search/index.py` | 1.21371 | 1.09305 | 1.2795 | 1.44295 | 1.43527 | 1.4655 | 1.5225 |
| `algorithm/search/linear.py` | 1.26947 | 1.11981 | 1.30682 | 1.49686 | 1.48434 | 1.521 | 1.57166 |
| `algorithm/twosum/twosum.py` | 0.08737 | 0.07554 | 0.08038 | 0.08727 | 0.07497 | 0.07176 | 0.08598 |
| `algorithm/twosum/twosum_naive.py` | 0.08854 | 0.07534 | 0.08043 | 0.08845 | 0.07497 | 0.07092 | 0.08738 |
| `complex/classes/classes.py` | 0.02454 | 0.02356 | 0.04344 | 0.04761 | 0.04386 | 0.04194 | 0.04903 |
| `complex/classes/dataclasses_.py` | 0.13641 | 0.11776 | 0.12657 | 0.13872 | 0.11167 | 0.10774 | -- |
| `complex/classes/namedtuple_classes.py` | 0.09924 | 0.08779 | 0.0925 | 0.10025 | 0.08843 | 0.08484 | 0.10325 |
| `complex/classes/simplenamespace.py` | 0.02929 | 0.0274 | 0.04576 | 0.04985 | 0.04354 | 0.04226 | 0.06495 |
| `complex/classes/sloted_classes.py` | 0.02281 | 0.02354 | 0.04357 | 0.0479 | 0.04401 | 0.04225 | 0.049 |
| `complex/generators/simple.py` | 0.04646 | 0.04173 | 0.06252 | 0.06675 | 0.06435 | 0.06446 | 0.06948 |
| `dummy/dummy.py` | 0.01779 | 0.01264 | 0.02947 | 0.03373 | 0.03021 | 0.029 | 0.03429 |
| `long_run/database/postgresql.py` | 0.17996 | 0.15339 | 0.15544 | 0.17125 | 0.15214 | 0.14434 | 0.15768 |
| `long_run/database/sqlite_.py` | -- | 0.61521 | 0.62889 | 0.66583 | 0.60925 | 0.54888 | 0.62854 |
| `long_run/file/load_titanic_csv_pandas.py` | -- | 0.64868 | 0.67123 | 0.72455 | 0.6638 | 0.60357 | 0.7002 |
| `long_run/file/load_titanic_csv_python.py` | 0.06874 | 0.06069 | 0.07096 | 0.07975 | 0.06998 | 0.06857 | 0.07569 |
| `long_run/processes/collect_names_from_site.py` | -- | 1.73521 | 2.02127 | 2.10958 | 2.02011 | -- | -- |
| `long_run/processes/generate_fake_data.py` | -- | 0.82638 | 0.83759 | 0.90126 | 0.81886 | 0.78959 | 0.86937 |
| `long_run/processes/maze_generator.py` | 0.19646 | 0.1958 | 0.30284 | 0.33636 | 0.35948 | 0.32836 | 0.36681 |
| `long_run/text/clean_text.py` | 0.25405 | 0.24563 | 0.27219 | 0.29193 | 0.2785 | 0.26641 | 0.2707 |
| `long_run/text/count_words.py` | 0.08327 | 0.0764 | 0.09162 | 0.10074 | 0.09132 | 0.08735 | 0.09518 |
| `math/haversine.py` | 0.8864 | 0.8029 | 0.9173 | 1.00552 | 0.90731 | 0.9697 | 0.85102 |
| `math/mandelbrot.py` | -- | 2.57753 | 2.58221 | 2.60718 | 3.02713 | 3.05351 | 3.15621 |
| `math/pow_simple.py` | 0.31329 | 0.34876 | 0.75054 | 0.77774 | 0.75186 | 0.77611 | 0.65873 |
| `math/pow_using_math.py` | 1.21046 | 1.16759 | 1.41021 | 1.4282 | 1.40653 | 1.7494 | 1.49375 |
| `modules/json/json_module.py` | 0.4068 | 0.39864 | 0.45123 | 0.50084 | 0.49313 | 0.51787 | 0.50313 |
| `modules/json/orjson_module.py` | -- | 0.26467 | 0.30355 | 0.33171 | 0.29537 | 0.26459 | 0.30728 |
| `programming_game_benchmark/nbody.py` | 0.36435 | 0.34698 | 0.52555 | 0.56693 | 0.53625 | 0.52788 | 0.43467 |
| `programming_game_benchmark/spectral_norm.py` | 0.58623 | 0.51615 | 0.59817 | 0.67065 | 0.64236 | 0.68344 | 0.62172 |

#### **Memory Usage**

##### **MEM [MB]**
| Command | 3.12 | 3.11 | 3.10 | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 35.524 | 35.49833 | 32.23717 | 30.34375 | 29.63616 | 31.46429 | 28.65234 |
| `algorithm/search/hashmap_lookup.py` | 36.51283 | 36.66629 | 34.28181 | 32.75446 | 30.00502 | 30.87054 | 28.27902 |
| `algorithm/search/index.py` | 35.59319 | 36.01172 | 32.83315 | 30.50391 | 29.85938 | 30.75893 | 28.78348 |
| `algorithm/search/linear.py` | 35.46317 | 35.8817 | 32.81975 | 30.57366 | 29.83929 | 30.19531 | 28.96094 |
| `algorithm/twosum/twosum.py` | 27.64788 | 26.50335 | 24.08705 | 23.51172 | 21.62891 | 21.18136 | 22.00893 |
| `algorithm/twosum/twosum_naive.py` | 27.78404 | 26.49944 | 23.55022 | 22.97489 | 21.84989 | 21.13449 | 22.18025 |
| `complex/classes/classes.py` | 28.24944 | 27.69308 | 26.11384 | 23.56529 | 21.63672 | 21.17411 | 21.85324 |
| `complex/classes/dataclasses_.py` | 28.01674 | 27.74944 | 26.02846 | 23.66518 | 21.93136 | 21.35714 | -- |
| `complex/classes/namedtuple_classes.py` | 27.93415 | 27.32533 | 24.83594 | 22.48884 | 21.76618 | 21.14286 | 22.0 |
| `complex/classes/simplenamespace.py` | 29.59542 | 28.46317 | 25.64621 | 23.17969 | 21.85547 | 21.0279 | 21.95368 |
| `complex/classes/sloted_classes.py` | 28.34766 | 27.76897 | 25.52846 | 23.26563 | 21.96094 | 21.48103 | 21.74609 |
| `complex/generators/simple.py` | 29.55692 | 28.62891 | 26.3058 | 23.73214 | 22.03739 | 21.44141 | 22.1981 |
| `dummy/dummy.py` | 27.53906 | 26.48884 | 23.65569 | 23.05357 | 21.59096 | 20.83873 | 21.50949 |
| `long_run/database/postgresql.py` | 32.59766 | 31.71763 | 28.29129 | 29.05971 | 26.75446 | 27.03739 | 26.47768 |
| `long_run/database/sqlite_.py` | -- | 72.64788 | 66.98772 | 67.64397 | 66.75112 | 66.56641 | 63.05022 |
| `long_run/file/load_titanic_csv_pandas.py` | -- | 70.78348 | 65.12723 | 67.09654 | 65.15402 | 64.90123 | 61.85603 |
| `long_run/file/load_titanic_csv_python.py` | 27.79911 | 26.83371 | 24.18192 | 23.15681 | 21.65737 | 21.33984 | 21.72433 |
| `long_run/processes/collect_names_from_site.py` | -- | 47.49609 | 45.32087 | 45.57701 | 45.58036 | -- | -- |
| `long_run/processes/generate_fake_data.py` | -- | 72.1942 | 68.54799 | 69.86328 | 66.83873 | 70.0798 | 64.42467 |
| `long_run/processes/maze_generator.py` | 28.15067 | 26.87388 | 24.84152 | 22.70647 | 22.00335 | 21.90737 | 21.62835 |
| `long_run/text/clean_text.py` | 27.58203 | 26.52009 | 24.10324 | 23.36942 | 21.64118 | 21.19252 | 22.22656 |
| `long_run/text/count_words.py` | 27.06362 | 26.55636 | 24.17969 | 23.48158 | 21.67801 | 21.16797 | 21.61663 |
| `math/haversine.py` | 27.51618 | 26.50558 | 24.02455 | 23.70982 | 21.79799 | 21.08036 | 21.60324 |
| `math/mandelbrot.py` | -- | 39.7779 | 38.6356 | 42.92243 | 36.19587 | 35.6529 | 35.83147 |
| `math/pow_simple.py` | 27.49219 | 26.49888 | 24.17746 | 23.66183 | 21.51116 | 21.21261 | 21.60603 |
| `math/pow_using_math.py` | 27.35882 | 26.42634 | 24.06473 | 23.20257 | 21.48605 | 21.07589 | 21.48549 |
| `modules/json/json_module.py` | 28.35937 | 26.56752 | 24.23661 | 23.32087 | 22.06027 | 22.24107 | 21.60435 |
| `modules/json/orjson_module.py` | -- | 26.93862 | 24.71261 | 23.64621 | 22.50223 | 22.57645 | 22.48382 |
| `programming_game_benchmark/nbody.py` | 27.80692 | 26.5173 | 23.91685 | 22.98661 | 21.75167 | 20.92355 | 21.57087 |
| `programming_game_benchmark/spectral_norm.py` | 28.82199 | 26.96987 | 24.83147 | 23.61161 | 22.66853 | 22.8192 | 22.22266 |

---


### **Python 3.6**

```bash
Python 3.6.15

Linux 673e7cf9dc14 5.15.0-83-generic unknown GNU/Linux

CPU(s):                             12
Thread(s) per core:                 2
Core(s) per socket:                 6
NUMA node(s):                       1
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:                        4100.0000
NUMA node0 CPU(s):                  0-11

MemTotal:       16066476 kB
MemFree:         2073856 kB
MemAvailable:   14356600 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.50654 | 0.0266 | 1.51505 | 1.46929 | 1.53954 | 28.65234 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.52074 | 0.053 | 1.51288 | 1.48348 | 1.63263 | 28.27902 |
| `algorithm/search/index.py` | yes | 1.51963 | 0.02544 | 1.5225 | 1.4895 | 1.55104 | 28.78348 |
| `algorithm/search/linear.py` | yes | 1.58255 | 0.03665 | 1.57166 | 1.54242 | 1.64451 | 28.96094 |
| `algorithm/twosum/twosum.py` | yes | 0.08594 | 0.00051 | 0.08598 | 0.08506 | 0.08671 | 22.00893 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.08713 | 0.00059 | 0.08738 | 0.08621 | 0.08782 | 22.18025 |
| `complex/classes/classes.py` | yes | 0.04921 | 0.00061 | 0.04903 | 0.0487 | 0.05047 | 21.85324 |
| `complex/classes/dataclasses_.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `complex/classes/namedtuple_classes.py` | yes | 0.10336 | 0.00288 | 0.10325 | 0.10079 | 0.1089 | 22.0 |
| `complex/classes/simplenamespace.py` | yes | 0.0651 | 0.00048 | 0.06495 | 0.06454 | 0.066 | 21.95368 |
| `complex/classes/sloted_classes.py` | yes | 0.04906 | 0.00045 | 0.049 | 0.04837 | 0.04967 | 21.74609 |
| `complex/generators/simple.py` | yes | 0.0702 | 0.00162 | 0.06948 | 0.06877 | 0.07288 | 22.1981 |
| `dummy/dummy.py` | yes | 0.03432 | 0.00024 | 0.03429 | 0.03394 | 0.03466 | 21.50949 |
| `long_run/database/postgresql.py` | yes | 0.15762 | 0.00076 | 0.15768 | 0.15644 | 0.15894 | 26.47768 |
| `long_run/database/sqlite_.py` | yes | 0.62974 | 0.00441 | 0.62854 | 0.62459 | 0.63578 | 63.05022 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.70156 | 0.00342 | 0.7002 | 0.6986 | 0.70894 | 61.85603 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.0756 | 0.00045 | 0.07569 | 0.07493 | 0.0763 | 21.72433 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | yes | 0.86927 | 0.00421 | 0.86937 | 0.86233 | 0.87561 | 64.42467 |
| `long_run/processes/maze_generator.py` | yes | 0.36679 | 0.01932 | 0.36681 | 0.34033 | 0.39276 | 21.62835 |
| `long_run/text/clean_text.py` | yes | 0.27215 | 0.00474 | 0.2707 | 0.26702 | 0.27956 | 22.22656 |
| `long_run/text/count_words.py` | yes | 0.09501 | 0.00056 | 0.09518 | 0.0939 | 0.09546 | 21.61663 |
| `math/haversine.py` | yes | 0.86951 | 0.04765 | 0.85102 | 0.83384 | 0.97288 | 21.60324 |
| `math/mandelbrot.py` | yes | 3.12832 | 0.07755 | 3.15621 | 2.95264 | 3.16362 | 35.83147 |
| `math/pow_simple.py` | yes | 0.662 | 0.01307 | 0.65873 | 0.64545 | 0.68509 | 21.60603 |
| `math/pow_using_math.py` | yes | 1.50499 | 0.04714 | 1.49375 | 1.46168 | 1.60156 | 21.48549 |
| `modules/json/json_module.py` | yes | 0.50273 | 0.00459 | 0.50313 | 0.49575 | 0.50955 | 21.60435 |
| `modules/json/orjson_module.py` | yes | 0.31387 | 0.01317 | 0.30728 | 0.30312 | 0.34032 | 22.48382 |
| `programming_game_benchmark/nbody.py` | yes | 0.43459 | 0.00117 | 0.43467 | 0.43333 | 0.43681 | 21.57087 |
| `programming_game_benchmark/spectral_norm.py` | yes | 0.62307 | 0.03043 | 0.62172 | 0.562 | 0.65365 | 22.22266 |


### **Python 3.7**

```bash
Python 3.7.17

Linux f4e574a1b629 5.15.0-83-generic unknown GNU/Linux

CPU(s):                             12
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:                 2
Core(s) per socket:                 6
CPU max MHz:                        4100.0000
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-11

MemTotal:       16066476 kB
MemFree:         2000968 kB
MemAvailable:   14299592 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.47711 | 0.03183 | 1.47179 | 1.44607 | 1.52008 | 31.46429 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.48919 | 0.0534 | 1.46166 | 1.44789 | 1.58056 | 30.87054 |
| `algorithm/search/index.py` | yes | 1.46892 | 0.01966 | 1.4655 | 1.44619 | 1.49249 | 30.75893 |
| `algorithm/search/linear.py` | yes | 1.52968 | 0.03112 | 1.521 | 1.49212 | 1.58292 | 30.19531 |
| `algorithm/twosum/twosum.py` | yes | 0.07186 | 0.00123 | 0.07176 | 0.07048 | 0.07433 | 21.18136 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07087 | 0.00061 | 0.07092 | 0.06994 | 0.07169 | 21.13449 |
| `complex/classes/classes.py` | yes | 0.04202 | 0.00044 | 0.04194 | 0.04165 | 0.04284 | 21.17411 |
| `complex/classes/dataclasses_.py` | yes | 0.10805 | 0.00114 | 0.10774 | 0.1068 | 0.11012 | 21.35714 |
| `complex/classes/namedtuple_classes.py` | yes | 0.08476 | 0.00037 | 0.08484 | 0.08426 | 0.08524 | 21.14286 |
| `complex/classes/simplenamespace.py` | yes | 0.04231 | 0.00058 | 0.04226 | 0.04175 | 0.0433 | 21.0279 |
| `complex/classes/sloted_classes.py` | yes | 0.04248 | 0.00089 | 0.04225 | 0.04188 | 0.04444 | 21.48103 |
| `complex/generators/simple.py` | yes | 0.06451 | 0.00042 | 0.06446 | 0.0639 | 0.06494 | 21.44141 |
| `dummy/dummy.py` | yes | 0.02938 | 0.00099 | 0.029 | 0.02885 | 0.03161 | 20.83873 |
| `long_run/database/postgresql.py` | yes | 0.1443 | 0.0012 | 0.14434 | 0.14292 | 0.14593 | 27.03739 |
| `long_run/database/sqlite_.py` | yes | 0.54837 | 0.00137 | 0.54888 | 0.54645 | 0.54986 | 66.56641 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.60413 | 0.00619 | 0.60357 | 0.59631 | 0.61293 | 64.90123 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06931 | 0.0014 | 0.06857 | 0.06793 | 0.07129 | 21.33984 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | yes | 0.79328 | 0.01318 | 0.78959 | 0.78453 | 0.8221 | 70.0798 |
| `long_run/processes/maze_generator.py` | yes | 0.33487 | 0.02449 | 0.32836 | 0.29752 | 0.3636 | 21.90737 |
| `long_run/text/clean_text.py` | yes | 0.2669 | 0.00182 | 0.26641 | 0.26467 | 0.27059 | 21.19252 |
| `long_run/text/count_words.py` | yes | 0.08747 | 0.00031 | 0.08735 | 0.08717 | 0.08803 | 21.16797 |
| `math/haversine.py` | yes | 0.96462 | 0.01198 | 0.9697 | 0.94577 | 0.97801 | 21.08036 |
| `math/mandelbrot.py` | yes | 3.06598 | 0.03354 | 3.05351 | 3.04708 | 3.14065 | 35.6529 |
| `math/pow_simple.py` | yes | 0.77667 | 0.01135 | 0.77611 | 0.76305 | 0.79285 | 21.21261 |
| `math/pow_using_math.py` | yes | 1.73737 | 0.03942 | 1.7494 | 1.66115 | 1.7803 | 21.07589 |
| `modules/json/json_module.py` | yes | 0.51788 | 0.0033 | 0.51787 | 0.51397 | 0.52308 | 22.24107 |
| `modules/json/orjson_module.py` | yes | 0.26782 | 0.00861 | 0.26459 | 0.26173 | 0.28647 | 22.57645 |
| `programming_game_benchmark/nbody.py` | yes | 0.52799 | 0.00159 | 0.52788 | 0.52546 | 0.53024 | 20.92355 |
| `programming_game_benchmark/spectral_norm.py` | yes | 0.69229 | 0.04899 | 0.68344 | 0.62627 | 0.74344 | 22.8192 |


### **Python 3.8**

```bash
Python 3.8.18

Linux 9ba0fff04b44 5.15.0-83-generic unknown GNU/Linux

CPU(s):                             12
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:                 2
Core(s) per socket:                 6
CPU max MHz:                        4100.0000
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-11

MemTotal:       16066476 kB
MemFree:         2022976 kB
MemAvailable:   14323012 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.40708 | 0.02343 | 1.40534 | 1.3765 | 1.45301 | 29.63616 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.42754 | 0.02708 | 1.42332 | 1.4038 | 1.48383 | 30.00502 |
| `algorithm/search/index.py` | yes | 1.42984 | 0.01643 | 1.43527 | 1.40577 | 1.45181 | 29.85938 |
| `algorithm/search/linear.py` | yes | 1.49334 | 0.03452 | 1.48434 | 1.46532 | 1.56847 | 29.83929 |
| `algorithm/twosum/twosum.py` | yes | 0.07488 | 0.00067 | 0.07497 | 0.0741 | 0.07601 | 21.62891 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.075 | 0.00026 | 0.07497 | 0.0746 | 0.07537 | 21.84989 |
| `complex/classes/classes.py` | yes | 0.04403 | 0.00077 | 0.04386 | 0.04314 | 0.04534 | 21.63672 |
| `complex/classes/dataclasses_.py` | yes | 0.11157 | 0.00048 | 0.11167 | 0.11083 | 0.11224 | 21.93136 |
| `complex/classes/namedtuple_classes.py` | yes | 0.08896 | 0.00152 | 0.08843 | 0.08796 | 0.09236 | 21.76618 |
| `complex/classes/simplenamespace.py` | yes | 0.04362 | 0.00036 | 0.04354 | 0.04328 | 0.0444 | 21.85547 |
| `complex/classes/sloted_classes.py` | yes | 0.04421 | 0.00039 | 0.04401 | 0.04394 | 0.04498 | 21.96094 |
| `complex/generators/simple.py` | yes | 0.06433 | 0.00042 | 0.06435 | 0.06378 | 0.06484 | 22.03739 |
| `dummy/dummy.py` | yes | 0.03072 | 0.00202 | 0.03021 | 0.02924 | 0.03501 | 21.59096 |
| `long_run/database/postgresql.py` | yes | 0.15279 | 0.00234 | 0.15214 | 0.15096 | 0.15793 | 26.75446 |
| `long_run/database/sqlite_.py` | yes | 0.61123 | 0.0097 | 0.60925 | 0.60066 | 0.63176 | 66.75112 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.6638 | 0.00713 | 0.6638 | 0.6555 | 0.67736 | 65.15402 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06983 | 0.00057 | 0.06998 | 0.06899 | 0.07052 | 21.65737 |
| `long_run/processes/collect_names_from_site.py` | yes | 2.01815 | 0.02673 | 2.02011 | 1.96768 | 2.04641 | 45.58036 |
| `long_run/processes/generate_fake_data.py` | yes | 0.82415 | 0.01196 | 0.81886 | 0.81556 | 0.84938 | 66.83873 |
| `long_run/processes/maze_generator.py` | yes | 0.35137 | 0.02579 | 0.35948 | 0.30483 | 0.38633 | 22.00335 |
| `long_run/text/clean_text.py` | yes | 0.27825 | 0.00175 | 0.2785 | 0.27527 | 0.28004 | 21.64118 |
| `long_run/text/count_words.py` | yes | 0.09138 | 0.00022 | 0.09132 | 0.09114 | 0.09176 | 21.67801 |
| `math/haversine.py` | yes | 0.91357 | 0.0341 | 0.90731 | 0.8819 | 0.97084 | 21.79799 |
| `math/mandelbrot.py` | yes | 3.04262 | 0.04266 | 3.02713 | 3.02111 | 3.13878 | 36.19587 |
| `math/pow_simple.py` | yes | 0.76167 | 0.02836 | 0.75186 | 0.74284 | 0.82273 | 21.51116 |
| `math/pow_using_math.py` | yes | 1.41396 | 0.03746 | 1.40653 | 1.36488 | 1.46021 | 21.48605 |
| `modules/json/json_module.py` | yes | 0.49365 | 0.00511 | 0.49313 | 0.48489 | 0.50054 | 22.06027 |
| `modules/json/orjson_module.py` | yes | 0.29604 | 0.00255 | 0.29537 | 0.29328 | 0.29962 | 22.50223 |
| `programming_game_benchmark/nbody.py` | yes | 0.53661 | 0.00615 | 0.53625 | 0.52958 | 0.54639 | 21.75167 |
| `programming_game_benchmark/spectral_norm.py` | yes | 0.64739 | 0.02998 | 0.64236 | 0.61989 | 0.71031 | 22.66853 |


### **Python 3.9**

```bash
Python 3.9.18

Linux 1321234cbad4 5.15.0-83-generic unknown GNU/Linux

CPU(s):                             12
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:                 2
Core(s) per socket:                 6
CPU max MHz:                        4100.0000
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-11

MemTotal:       16066476 kB
MemFree:         2020104 kB
MemAvailable:   14321448 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.43058 | 0.01406 | 1.42724 | 1.41014 | 1.44949 | 30.34375 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.44258 | 0.0392 | 1.43456 | 1.41161 | 1.52176 | 32.75446 |
| `algorithm/search/index.py` | yes | 1.47812 | 0.07143 | 1.44295 | 1.43318 | 1.63302 | 30.50391 |
| `algorithm/search/linear.py` | yes | 1.4906 | 0.01399 | 1.49686 | 1.46734 | 1.50797 | 30.57366 |
| `algorithm/twosum/twosum.py` | yes | 0.08771 | 0.00163 | 0.08727 | 0.08674 | 0.09136 | 23.51172 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.08831 | 0.00067 | 0.08845 | 0.08717 | 0.08903 | 22.97489 |
| `complex/classes/classes.py` | yes | 0.04764 | 0.00023 | 0.04761 | 0.04728 | 0.048 | 23.56529 |
| `complex/classes/dataclasses_.py` | yes | 0.13874 | 0.00077 | 0.13872 | 0.13779 | 0.13985 | 23.66518 |
| `complex/classes/namedtuple_classes.py` | yes | 0.1 | 0.00058 | 0.10025 | 0.09885 | 0.10059 | 22.48884 |
| `complex/classes/simplenamespace.py` | yes | 0.04987 | 0.00034 | 0.04985 | 0.04949 | 0.05026 | 23.17969 |
| `complex/classes/sloted_classes.py` | yes | 0.0478 | 0.00051 | 0.0479 | 0.04715 | 0.0485 | 23.26563 |
| `complex/generators/simple.py` | yes | 0.06751 | 0.00229 | 0.06675 | 0.06619 | 0.07263 | 23.73214 |
| `dummy/dummy.py` | yes | 0.03371 | 0.00054 | 0.03373 | 0.03299 | 0.03438 | 23.05357 |
| `long_run/database/postgresql.py` | yes | 0.1723 | 0.00371 | 0.17125 | 0.16982 | 0.18058 | 29.05971 |
| `long_run/database/sqlite_.py` | yes | 0.66581 | 0.00194 | 0.66583 | 0.66344 | 0.66891 | 67.64397 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.72669 | 0.01126 | 0.72455 | 0.71534 | 0.75032 | 67.09654 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.07986 | 0.00035 | 0.07975 | 0.07943 | 0.08042 | 23.15681 |
| `long_run/processes/collect_names_from_site.py` | yes | 2.11104 | 0.02168 | 2.10958 | 2.07645 | 2.1415 | 45.57701 |
| `long_run/processes/generate_fake_data.py` | yes | 0.90444 | 0.02316 | 0.90126 | 0.88625 | 0.94993 | 69.86328 |
| `long_run/processes/maze_generator.py` | yes | 0.34228 | 0.0252 | 0.33636 | 0.32358 | 0.39514 | 22.70647 |
| `long_run/text/clean_text.py` | yes | 0.29197 | 0.00113 | 0.29193 | 0.2905 | 0.2934 | 23.36942 |
| `long_run/text/count_words.py` | yes | 0.10106 | 0.00072 | 0.10074 | 0.10042 | 0.10213 | 23.48158 |
| `math/haversine.py` | yes | 1.00507 | 0.00695 | 1.00552 | 0.99681 | 1.01445 | 23.70982 |
| `math/mandelbrot.py` | yes | 2.60615 | 0.00333 | 2.60718 | 2.60108 | 2.61049 | 42.92243 |
| `math/pow_simple.py` | yes | 0.78083 | 0.01741 | 0.77774 | 0.76679 | 0.81528 | 23.66183 |
| `math/pow_using_math.py` | yes | 1.43642 | 0.05862 | 1.4282 | 1.39064 | 1.56263 | 23.20257 |
| `modules/json/json_module.py` | yes | 0.50125 | 0.00752 | 0.50084 | 0.49276 | 0.51217 | 23.32087 |
| `modules/json/orjson_module.py` | yes | 0.33283 | 0.0041 | 0.33171 | 0.32612 | 0.33792 | 23.64621 |
| `programming_game_benchmark/nbody.py` | yes | 0.56627 | 0.01761 | 0.56693 | 0.53976 | 0.59779 | 22.98661 |
| `programming_game_benchmark/spectral_norm.py` | yes | 0.67122 | 0.00688 | 0.67065 | 0.66239 | 0.68339 | 23.61161 |


### **Python 3.10**

```bash
Python 3.10.13

Linux 2823dca568fc 5.15.0-83-generic unknown GNU/Linux

CPU(s):                             12
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:                 2
Core(s) per socket:                 6
CPU max MHz:                        4100.0000
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-11

MemTotal:       16066476 kB
MemFree:         2010976 kB
MemAvailable:   14318016 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.24304 | 0.0173 | 1.24279 | 1.22076 | 1.271 | 32.23717 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.26227 | 0.02252 | 1.25821 | 1.23298 | 1.29438 | 34.28181 |
| `algorithm/search/index.py` | yes | 1.27566 | 0.01631 | 1.2795 | 1.25329 | 1.29898 | 32.83315 |
| `algorithm/search/linear.py` | yes | 1.30504 | 0.00535 | 1.30682 | 1.29672 | 1.31286 | 32.81975 |
| `algorithm/twosum/twosum.py` | yes | 0.08027 | 0.0002 | 0.08038 | 0.07998 | 0.08048 | 24.08705 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.08048 | 0.00084 | 0.08043 | 0.0792 | 0.08163 | 23.55022 |
| `complex/classes/classes.py` | yes | 0.04349 | 0.00038 | 0.04344 | 0.04294 | 0.04404 | 26.11384 |
| `complex/classes/dataclasses_.py` | yes | 0.12685 | 0.00149 | 0.12657 | 0.12579 | 0.13013 | 26.02846 |
| `complex/classes/namedtuple_classes.py` | yes | 0.09264 | 0.00071 | 0.0925 | 0.09202 | 0.09412 | 24.83594 |
| `complex/classes/simplenamespace.py` | yes | 0.04565 | 0.00036 | 0.04576 | 0.04507 | 0.04606 | 25.64621 |
| `complex/classes/sloted_classes.py` | yes | 0.04366 | 0.0005 | 0.04357 | 0.04317 | 0.04461 | 25.52846 |
| `complex/generators/simple.py` | yes | 0.06268 | 0.0005 | 0.06252 | 0.06218 | 0.06339 | 26.3058 |
| `dummy/dummy.py` | yes | 0.02957 | 0.00025 | 0.02947 | 0.02937 | 0.03003 | 23.65569 |
| `long_run/database/postgresql.py` | yes | 0.1558 | 0.00109 | 0.15544 | 0.15492 | 0.15808 | 28.29129 |
| `long_run/database/sqlite_.py` | yes | 0.6294 | 0.00559 | 0.62889 | 0.62226 | 0.63788 | 66.98772 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.6695 | 0.0051 | 0.67123 | 0.65973 | 0.67444 | 65.12723 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.0708 | 0.00049 | 0.07096 | 0.06986 | 0.07126 | 24.18192 |
| `long_run/processes/collect_names_from_site.py` | yes | 2.02844 | 0.02458 | 2.02127 | 1.99105 | 2.06439 | 45.32087 |
| `long_run/processes/generate_fake_data.py` | yes | 0.83924 | 0.00838 | 0.83759 | 0.82993 | 0.85419 | 68.54799 |
| `long_run/processes/maze_generator.py` | yes | 0.29286 | 0.02198 | 0.30284 | 0.24724 | 0.31268 | 24.84152 |
| `long_run/text/clean_text.py` | yes | 0.27409 | 0.00353 | 0.27219 | 0.27181 | 0.28082 | 24.10324 |
| `long_run/text/count_words.py` | yes | 0.09183 | 0.00103 | 0.09162 | 0.09069 | 0.09399 | 24.17969 |
| `math/haversine.py` | yes | 0.9211 | 0.01622 | 0.9173 | 0.9017 | 0.94605 | 24.02455 |
| `math/mandelbrot.py` | yes | 2.58237 | 0.00621 | 2.58221 | 2.57388 | 2.59333 | 38.6356 |
| `math/pow_simple.py` | yes | 0.74397 | 0.02396 | 0.75054 | 0.70924 | 0.76967 | 24.17746 |
| `math/pow_using_math.py` | yes | 1.41431 | 0.03695 | 1.41021 | 1.36393 | 1.48316 | 24.06473 |
| `modules/json/json_module.py` | yes | 0.4505 | 0.00543 | 0.45123 | 0.4406 | 0.45596 | 24.23661 |
| `modules/json/orjson_module.py` | yes | 0.30411 | 0.00216 | 0.30355 | 0.30256 | 0.30892 | 24.71261 |
| `programming_game_benchmark/nbody.py` | yes | 0.52619 | 0.01395 | 0.52555 | 0.51113 | 0.54945 | 23.91685 |
| `programming_game_benchmark/spectral_norm.py` | yes | 0.60611 | 0.01754 | 0.59817 | 0.5907 | 0.64332 | 24.83147 |


### **Python 3.11**

```bash
Python 3.11.5

Linux 5c72342f7d2c 5.15.0-83-generic unknown GNU/Linux

CPU(s):                             12
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:                 2
Core(s) per socket:                 6
CPU max MHz:                        4100.0000
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-11

MemTotal:       16066476 kB
MemFree:         1995800 kB
MemAvailable:   14306664 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.06684 | 0.00809 | 1.06565 | 1.05215 | 1.07693 | 35.49833 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.07066 | 0.01182 | 1.07038 | 1.05562 | 1.08453 | 36.66629 |
| `algorithm/search/index.py` | yes | 1.10925 | 0.03844 | 1.09305 | 1.07198 | 1.17036 | 36.01172 |
| `algorithm/search/linear.py` | yes | 1.14456 | 0.06536 | 1.11981 | 1.11149 | 1.29217 | 35.8817 |
| `algorithm/twosum/twosum.py` | yes | 0.07568 | 0.00073 | 0.07554 | 0.07468 | 0.07701 | 26.50335 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07527 | 0.00052 | 0.07534 | 0.07436 | 0.07583 | 26.49944 |
| `complex/classes/classes.py` | yes | 0.02358 | 0.00021 | 0.02356 | 0.02326 | 0.02393 | 27.69308 |
| `complex/classes/dataclasses_.py` | yes | 0.11754 | 0.00059 | 0.11776 | 0.11651 | 0.11826 | 27.74944 |
| `complex/classes/namedtuple_classes.py` | yes | 0.09179 | 0.00902 | 0.08779 | 0.08549 | 0.10918 | 27.32533 |
| `complex/classes/simplenamespace.py` | yes | 0.02739 | 0.00027 | 0.0274 | 0.02691 | 0.02773 | 28.46317 |
| `complex/classes/sloted_classes.py` | yes | 0.02313 | 0.00102 | 0.02354 | 0.02193 | 0.02471 | 27.76897 |
| `complex/generators/simple.py` | yes | 0.04172 | 0.00108 | 0.04173 | 0.04054 | 0.04385 | 28.62891 |
| `dummy/dummy.py` | yes | 0.01267 | 0.00024 | 0.01264 | 0.01237 | 0.01304 | 26.48884 |
| `long_run/database/postgresql.py` | yes | 0.15331 | 0.00059 | 0.15339 | 0.15249 | 0.15439 | 31.71763 |
| `long_run/database/sqlite_.py` | yes | 0.6156 | 0.00109 | 0.61521 | 0.61437 | 0.61756 | 72.64788 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.65253 | 0.00602 | 0.64868 | 0.6473 | 0.66141 | 70.78348 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06067 | 0.00029 | 0.06069 | 0.06036 | 0.06118 | 26.83371 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.73261 | 0.01734 | 1.73521 | 1.71448 | 1.76177 | 47.49609 |
| `long_run/processes/generate_fake_data.py` | yes | 0.82401 | 0.00584 | 0.82638 | 0.81366 | 0.83049 | 72.1942 |
| `long_run/processes/maze_generator.py` | yes | 0.18632 | 0.01927 | 0.1958 | 0.15666 | 0.20531 | 26.87388 |
| `long_run/text/clean_text.py` | yes | 0.24845 | 0.00744 | 0.24563 | 0.24084 | 0.25631 | 26.52009 |
| `long_run/text/count_words.py` | yes | 0.07635 | 0.00032 | 0.0764 | 0.07591 | 0.07672 | 26.55636 |
| `math/haversine.py` | yes | 0.81059 | 0.0243 | 0.8029 | 0.78432 | 0.85734 | 26.50558 |
| `math/mandelbrot.py` | yes | 2.59351 | 0.04991 | 2.57753 | 2.56794 | 2.70615 | 39.7779 |
| `math/pow_simple.py` | yes | 0.35064 | 0.00337 | 0.34876 | 0.34755 | 0.35503 | 26.49888 |
| `math/pow_using_math.py` | yes | 1.17603 | 0.01559 | 1.16759 | 1.16521 | 1.20734 | 26.42634 |
| `modules/json/json_module.py` | yes | 0.40081 | 0.0059 | 0.39864 | 0.39644 | 0.41345 | 26.56752 |
| `modules/json/orjson_module.py` | yes | 0.26654 | 0.00424 | 0.26467 | 0.26142 | 0.27199 | 26.93862 |
| `programming_game_benchmark/nbody.py` | yes | 0.34589 | 0.00325 | 0.34698 | 0.34206 | 0.34911 | 26.5173 |
| `programming_game_benchmark/spectral_norm.py` | yes | 0.51826 | 0.01309 | 0.51615 | 0.50427 | 0.54306 | 26.96987 |


### **Python 3.12**

```bash
Python 3.12.0rc3

Linux f1c500a10a95 5.15.0-83-generic unknown GNU/Linux

CPU(s):                             12
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:                 2
Core(s) per socket:                 6
CPU max MHz:                        4100.0000
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-11

MemTotal:       16066476 kB
MemFree:         2000184 kB
MemAvailable:   14310784 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.19305 | 0.01261 | 1.19555 | 1.16808 | 1.20687 | 35.524 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.20973 | 0.02086 | 1.21419 | 1.18386 | 1.24379 | 36.51283 |
| `algorithm/search/index.py` | yes | 1.21941 | 0.02444 | 1.21371 | 1.19498 | 1.26927 | 35.59319 |
| `algorithm/search/linear.py` | yes | 1.28481 | 0.02778 | 1.26947 | 1.2574 | 1.33153 | 35.46317 |
| `algorithm/twosum/twosum.py` | yes | 0.08737 | 0.00044 | 0.08737 | 0.08684 | 0.08818 | 27.64788 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.08863 | 0.00138 | 0.08854 | 0.08672 | 0.09062 | 27.78404 |
| `complex/classes/classes.py` | yes | 0.02379 | 0.00124 | 0.02454 | 0.02241 | 0.02511 | 28.24944 |
| `complex/classes/dataclasses_.py` | yes | 0.13648 | 0.00081 | 0.13641 | 0.13551 | 0.13807 | 28.01674 |
| `complex/classes/namedtuple_classes.py` | yes | 0.09942 | 0.00051 | 0.09924 | 0.09902 | 0.10052 | 27.93415 |
| `complex/classes/simplenamespace.py` | yes | 0.0296 | 0.00126 | 0.02929 | 0.02867 | 0.03235 | 29.59542 |
| `complex/classes/sloted_classes.py` | yes | 0.02284 | 0.0003 | 0.02281 | 0.02246 | 0.02328 | 28.34766 |
| `complex/generators/simple.py` | yes | 0.04664 | 0.00077 | 0.04646 | 0.04596 | 0.04801 | 29.55692 |
| `dummy/dummy.py` | yes | 0.01892 | 0.00215 | 0.01779 | 0.01758 | 0.02295 | 27.53906 |
| `long_run/database/postgresql.py` | yes | 0.1803 | 0.00096 | 0.17996 | 0.17923 | 0.18198 | 32.59766 |
| `long_run/database/sqlite_.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/file/load_titanic_csv_pandas.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.0687 | 0.00056 | 0.06874 | 0.06794 | 0.06974 | 27.79911 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/maze_generator.py` | yes | 0.19955 | 0.01593 | 0.19646 | 0.18321 | 0.22416 | 28.15067 |
| `long_run/text/clean_text.py` | yes | 0.25515 | 0.00359 | 0.25405 | 0.25071 | 0.26172 | 27.58203 |
| `long_run/text/count_words.py` | yes | 0.08324 | 0.00039 | 0.08327 | 0.08268 | 0.08375 | 27.06362 |
| `math/haversine.py` | yes | 0.8862 | 0.00763 | 0.8864 | 0.87271 | 0.89691 | 27.51618 |
| `math/mandelbrot.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `math/pow_simple.py` | yes | 0.32299 | 0.01323 | 0.31329 | 0.3123 | 0.34108 | 27.49219 |
| `math/pow_using_math.py` | yes | 1.22399 | 0.02829 | 1.21046 | 1.19613 | 1.27662 | 27.35882 |
| `modules/json/json_module.py` | yes | 0.40526 | 0.00563 | 0.4068 | 0.39627 | 0.41111 | 28.35937 |
| `modules/json/orjson_module.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `programming_game_benchmark/nbody.py` | yes | 0.36416 | 0.00981 | 0.36435 | 0.3522 | 0.37852 | 27.80692 |
| `programming_game_benchmark/spectral_norm.py` | yes | 0.58832 | 0.01406 | 0.58623 | 0.57067 | 0.60774 | 28.82199 |

