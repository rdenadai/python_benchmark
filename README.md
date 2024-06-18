# Python Benchmark

This is a simple repo to validate and test any (almost any) python program againts all python 3 versions.

- Python 3.6.15
- Python 3.7.17
- Python 3.8.19
- Python 3.9.19
- Python 3.10.14
- Python 3.11.9
- Python 3.12.3
- Python 3.13.0b2

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
# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13
```

- @DONT_RUN: This file should not be executed (in case of utils routines);
- @MPROF_INTERVAL: To benchmark memory usage mprof is used, this param you maybe able to improve interval collect of memory;
- @MPROF_MULTIPROCESS: In case your program uses python multiprocess (possible params -M or -C, default: -C);
- @ALLOWED_VERSIONS: What python versions your program can be run: from 3.6 to 3.13;

## Results

> Last run: Tue Jun 18 07:55:43 AM -03 2024
### **Comparison**

#### How much faster 3.13 is? (Mean / Median from 3.12 to 3.6)
| Command | 3.12 | 3.11 | 3.10 | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `algorithm/search/hashmap_lookup.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `algorithm/search/index.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `algorithm/search/linear.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `algorithm/sorting/naive_bubble_sort.py` | -9.05% / -9.98% | -30.46% / -30.40% | 46.56% / 45.53% | 68.01% / 70.65% | 67.12% / 67.11% | 64.09% / 63.28% | 44.99% / 45.32% |
| `algorithm/twosum/twosum.py` | 43.89% / 43.87% | 23.66% / 22.81% | 29.41% / 28.87% | 41.05% / 40.57% | 21.88% / 21.86% | 12.32% / 11.86% | 35.44% / 34.81% |
| `algorithm/twosum/twosum_naive.py` | 43.34% / 43.80% | 23.56% / 24.27% | 30.62% / 29.56% | 40.74% / 41.38% | 19.97% / 20.86% | 11.95% / 12.33% | 35.31% / 35.27% |
| `complex/classes/classes.py` | -1.25% / 2.98% | 0.13% / 3.90% | 73.21% / 77.04% | 87.70% / 92.71% | 70.04% / 74.56% | 66.46% / 69.98% | 87.52% / 92.76% |
| `complex/classes/dataclasses_.py` | -2.10% / -1.10% | -17.71% / -17.04% | -12.25% / -11.34% | -3.11% / -2.16% | -22.31% / -21.30% | -27.77% / -26.87% | -- / -- |
| `complex/classes/namedtuple_classes.py` | 41.72% / 41.56% | 20.60% / 20.21% | 27.36% / 26.61% | 41.93% / 42.11% | 20.09% / 19.95% | 13.85% / 13.92% | 36.21% / 35.64% |
| `complex/classes/simplenamespace.py` | -6.51% / -5.86% | -16.61% / -17.95% | 41.00% / 39.80% | 57.37% / 56.89% | 39.27% / 36.01% | 33.53% / 30.94% | 102.28% / 102.86% |
| `complex/classes/sloted_classes.py` | -4.71% / -0.10% | -7.62% / 6.00% | 68.41% / 82.48% | 87.53% / 102.00% | 71.19% / 81.43% | 65.07% / 77.57% | 86.04% / 100.95% |
| `complex/generators/readlines.py` | 31.34% / 32.45% | -13.00% / -13.34% | 71.82% / 70.41% | 84.60% / 78.56% | 64.42% / 61.12% | 54.68% / 53.24% | 89.34% / 87.80% |
| `complex/generators/simple.py` | -13.47% / -13.43% | -23.07% / -21.88% | 24.50% / 26.23% | 36.94% / 34.28% | 28.59% / 27.44% | 28.61% / 28.73% | 39.33% / 41.84% |
| `dummy/dummy.py` | -18.24% / -19.56% | -29.32% / -26.57% | 75.17% / 82.82% | 88.47% / 96.03% | 79.42% / 85.86% | 54.46% / 60.21% | 75.17% / 82.82% |
| `long_run/database/postgresql.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/database/sqlite_.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/file/load_titanic_csv_pandas.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/file/load_titanic_csv_python.py` | -6.06% / -6.28% | -19.04% / -19.30% | -5.93% / -5.94% | 5.62% / 5.30% | -7.14% / -7.86% | -12.20% / -12.84% | -1.67% / -2.50% |
| `long_run/processes/collect_names_from_site.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/processes/generate_fake_data.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/processes/maze_generator.py` | 5.76% / 2.37% | -7.32% / -9.90% | 42.24% / 32.59% | 93.94% / 88.08% | 82.25% / 76.01% | 84.67% / 82.13% | 88.27% / 84.20% |
| `long_run/text/clean_text.py` | -3.68% / -3.38% | -10.97% / -9.40% | -5.22% / -5.57% | 1.93% / 2.75% | -5.00% / -4.65% | -7.38% / -7.09% | -3.71% / -3.09% |
| `long_run/text/count_words.py` | -9.80% / -10.07% | -18.73% / -18.69% | -3.16% / -3.97% | 6.37% / 6.29% | -4.94% / -5.87% | -11.58% / -11.55% | -2.45% / -2.99% |
| `math/haversine.py` | 14.05% / 15.28% | -0.11% / -1.32% | 13.81% / 15.28% | 37.70% / 39.34% | 12.54% / 13.71% | 34.02% / 36.06% | 24.31% / 25.88% |
| `math/mandelbrot.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `math/pow_simple.py` | 2.00% / 1.99% | -9.19% / -8.06% | 28.66% / 29.75% | 35.92% / 37.16% | 45.75% / 46.77% | 43.92% / 46.78% | 36.55% / 38.16% |
| `math/pow_using_math.py` | 4.99% / 4.89% | -11.90% / -11.67% | 7.20% / 8.48% | 13.70% / 14.50% | 11.93% / 11.25% | 45.29% / 45.99% | 31.38% / 32.06% |
| `modules/json/json_module.py` | 3.46% / 2.70% | -4.94% / -6.32% | 2.93% / 1.88% | 20.67% / 21.01% | 9.18% / 8.55% | 23.01% / 22.67% | 21.91% / 20.16% |
| `modules/json/orjson_module.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `programming_game_benchmark/nbody.py` | 0.85% / -0.01% | -1.42% / -2.03% | 83.84% / 84.68% | 102.25% / 101.69% | 87.17% / 87.38% | 75.40% / 75.52% | 64.17% / 64.55% |
| `programming_game_benchmark/spectral_norm.py` | -0.18% / 0.35% | -10.54% / -8.22% | -2.36% / -1.57% | 11.33% / 10.95% | 7.29% / 7.14% | 20.67% / 21.64% | 18.40% / 23.19% |
---

#### How much more memory 3.13 uses? (Memory diff from 3.12 to 3.6)
| Command | 3.12 | 3.11 | 3.10 | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | -- | -- | -- | -- | -- | -- | -- |
| `algorithm/search/hashmap_lookup.py` | -- | -- | -- | -- | -- | -- | -- |
| `algorithm/search/index.py` | -- | -- | -- | -- | -- | -- | -- |
| `algorithm/search/linear.py` | -- | -- | -- | -- | -- | -- | -- |
| `algorithm/sorting/naive_bubble_sort.py` | 3.29% | 4.7% | 16.68% | 21.74% | 27.94% | 31.56% | 31.51% |
| `algorithm/twosum/twosum.py` | 2.11% | 6.72% | 21.49% | 23.55% | 30.08% | 36.41% | 28.36% |
| `algorithm/twosum/twosum_naive.py` | 4.05% | 4.78% | 19.54% | 20.27% | 29.54% | 34.77% | 28.09% |
| `complex/classes/classes.py` | 3.71% | 4.86% | 16.45% | 27.74% | 33.73% | 42.07% | 34.36% |
| `complex/classes/dataclasses_.py` | 4.97% | 3.72% | 15.88% | 24.37% | 34.1% | 37.75% | -- |
| `complex/classes/namedtuple_classes.py` | 3.04% | 5.32% | 15.72% | 23.43% | 31.92% | 35.71% | 29.63% |
| `complex/classes/simplenamespace.py` | 4.57% | 4.47% | 15.06% | 26.71% | 36.39% | 41.32% | 33.08% |
| `complex/classes/sloted_classes.py` | 5.5% | 3.46% | 14.0% | 23.07% | 35.67% | 40.5% | 35.73% |
| `complex/generators/readlines.py` | 3.59% | 4.93% | 20.58% | 21.27% | 29.9% | 36.58% | 32.38% |
| `complex/generators/simple.py` | 3.28% | 4.18% | 18.56% | 28.87% | 38.21% | 42.14% | 38.32% |
| `dummy/dummy.py` | 4.01% | 6.19% | 19.05% | 25.59% | 32.41% | 37.4% | 32.88% |
| `long_run/database/postgresql.py` | -- | -- | -- | -- | -- | -- | -- |
| `long_run/database/sqlite_.py` | -- | -- | -- | -- | -- | -- | -- |
| `long_run/file/load_titanic_csv_pandas.py` | -- | -- | -- | -- | -- | -- | -- |
| `long_run/file/load_titanic_csv_python.py` | 2.93% | 3.75% | 17.75% | 19.89% | 29.55% | 34.99% | 29.81% |
| `long_run/processes/collect_names_from_site.py` | -- | -- | -- | -- | -- | -- | -- |
| `long_run/processes/generate_fake_data.py` | -- | -- | -- | -- | -- | -- | -- |
| `long_run/processes/maze_generator.py` | 3.52% | 4.59% | 15.02% | 20.84% | 28.28% | 31.12% | 30.25% |
| `long_run/text/clean_text.py` | 2.22% | 6.78% | 21.66% | 23.74% | 29.9% | 34.69% | 28.24% |
| `long_run/text/count_words.py` | 3.8% | 5.08% | 20.97% | 21.65% | 31.37% | 36.61% | 32.15% |
| `math/haversine.py` | 1.75% | 4.24% | 16.77% | 23.36% | 28.49% | 34.79% | 30.18% |
| `math/mandelbrot.py` | -- | -- | -- | -- | -- | -- | -- |
| `math/pow_simple.py` | 1.85% | 4.32% | 16.94% | 23.72% | 28.59% | 34.39% | 31.22% |
| `math/pow_using_math.py` | 5.65% | 6.17% | 20.09% | 25.56% | 31.57% | 36.55% | 33.09% |
| `modules/json/json_module.py` | 2.17% | 5.45% | 20.54% | 23.07% | 28.53% | 28.69% | 31.57% |
| `modules/json/orjson_module.py` | -- | -- | -- | -- | -- | -- | -- |
| `programming_game_benchmark/nbody.py` | 4.17% | 4.42% | 19.36% | 20.2% | 31.29% | 34.4% | 31.52% |
| `programming_game_benchmark/spectral_norm.py` | 1.98% | 5.69% | 16.53% | 19.57% | 25.49% | 27.06% | 30.2% |
---

#### **Execution**

##### **Mean [s]**
| Command | 3.13 | 3.12 | 3.11 | 3.10 | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | -- | 0.93274 | 0.69468 | 0.82137 | 0.9378 | 0.87258 | 0.92136 | 0.95248 |
| `algorithm/search/hashmap_lookup.py` | -- | 0.94138 | 0.70175 | 0.81942 | 0.94287 | 0.87215 | 0.92664 | 0.98399 |
| `algorithm/search/index.py` | -- | 0.95179 | 0.7182 | 0.82895 | 0.94867 | 0.87827 | 1.31239 | 0.98305 |
| `algorithm/search/linear.py` | -- | 1.02475 | 0.74847 | 0.87216 | 1.00502 | 0.93543 | 0.98116 | 1.03756 |
| `algorithm/sorting/naive_bubble_sort.py` | 1.08072 | 0.98292 | 0.75156 | 1.58395 | 1.81574 | 1.80613 | 1.77332 | 1.56694 |
| `algorithm/twosum/twosum.py` | 0.0574 | 0.08259 | 0.07098 | 0.07428 | 0.08096 | 0.06996 | 0.06447 | 0.07774 |
| `algorithm/twosum/twosum_naive.py` | 0.05764 | 0.08262 | 0.07122 | 0.07529 | 0.08112 | 0.06915 | 0.06453 | 0.07799 |
| `complex/classes/classes.py` | 0.02236 | 0.02208 | 0.02239 | 0.03873 | 0.04197 | 0.03802 | 0.03722 | 0.04193 |
| `complex/classes/dataclasses_.py` | 0.13102 | 0.12827 | 0.10781 | 0.11497 | 0.12694 | 0.10179 | 0.09464 | -- |
| `complex/classes/namedtuple_classes.py` | 0.06477 | 0.09179 | 0.07811 | 0.08249 | 0.09193 | 0.07778 | 0.07374 | 0.08822 |
| `complex/classes/simplenamespace.py` | 0.0289 | 0.02702 | 0.0241 | 0.04075 | 0.04548 | 0.04025 | 0.03859 | 0.05846 |
| `complex/classes/sloted_classes.py` | 0.0227 | 0.02163 | 0.02097 | 0.03823 | 0.04257 | 0.03886 | 0.03747 | 0.04223 |
| `complex/generators/readlines.py` | 0.01838 | 0.02414 | 0.01599 | 0.03158 | 0.03393 | 0.03022 | 0.02843 | 0.0348 |
| `complex/generators/simple.py` | 0.04477 | 0.03874 | 0.03444 | 0.05574 | 0.06131 | 0.05757 | 0.05758 | 0.06238 |
| `dummy/dummy.py` | 0.01579 | 0.01291 | 0.01116 | 0.02766 | 0.02976 | 0.02833 | 0.02439 | 0.02766 |
| `long_run/database/postgresql.py` | -- | 0.17061 | 0.14558 | 0.14572 | 0.15841 | 0.14168 | 0.13001 | 0.14319 |
| `long_run/database/sqlite_.py` | -- | 0.67681 | 0.59141 | 0.57457 | 0.60773 | 0.56177 | 0.50288 | 0.5707 |
| `long_run/file/load_titanic_csv_pandas.py` | -- | 0.71334 | 0.6055 | 0.5993 | 0.64489 | 0.59432 | 0.54816 | 0.63318 |
| `long_run/file/load_titanic_csv_python.py` | 0.06934 | 0.06514 | 0.05614 | 0.06523 | 0.07324 | 0.06439 | 0.06088 | 0.06818 |
| `long_run/processes/collect_names_from_site.py` | -- | 2.25622 | 2.01276 | 2.18503 | 2.40169 | 1.84333 | -- | -- |
| `long_run/processes/generate_fake_data.py` | -- | 0.89445 | 0.78531 | 0.78863 | 0.83005 | 0.76546 | 0.73538 | 0.79067 |
| `long_run/processes/maze_generator.py` | 0.09744 | 0.10305 | 0.09031 | 0.1386 | 0.18898 | 0.17758 | 0.17994 | 0.18345 |
| `long_run/text/clean_text.py` | 0.20597 | 0.1984 | 0.18338 | 0.19521 | 0.20994 | 0.19567 | 0.19076 | 0.19832 |
| `long_run/text/count_words.py` | 0.08662 | 0.07813 | 0.0704 | 0.08388 | 0.09214 | 0.08234 | 0.07659 | 0.0845 |
| `math/haversine.py` | 0.45777 | 0.52207 | 0.45728 | 0.52099 | 0.63033 | 0.51517 | 0.61351 | 0.56907 |
| `math/mandelbrot.py` | -- | 2.63514 | 2.56442 | 2.59152 | 2.60233 | 2.98394 | 3.0154 | 3.11654 |
| `math/pow_simple.py` | 0.27789 | 0.28346 | 0.25234 | 0.35752 | 0.37772 | 0.40502 | 0.39995 | 0.37945 |
| `math/pow_using_math.py` | 0.84617 | 0.88836 | 0.74549 | 0.90708 | 0.96209 | 0.9471 | 1.22941 | 1.11168 |
| `modules/json/json_module.py` | 0.29619 | 0.30644 | 0.28156 | 0.30488 | 0.35741 | 0.32339 | 0.36434 | 0.3611 |
| `modules/json/orjson_module.py` | -- | 0.26638 | 0.20872 | 0.24336 | 0.26553 | 0.22614 | 0.19725 | 0.24262 |
| `programming_game_benchmark/nbody.py` | 0.15483 | 0.15615 | 0.15263 | 0.28464 | 0.31314 | 0.28979 | 0.27157 | 0.25418 |
| `programming_game_benchmark/spectral_norm.py` | 0.50811 | 0.5072 | 0.45453 | 0.49612 | 0.5657 | 0.54514 | 0.61314 | 0.60162 |

##### **Median [s]**
| Command | 3.13 | 3.12 | 3.11 | 3.10 | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | -- | 0.92768 | 0.69346 | 0.82886 | 0.94316 | 0.86883 | 0.92205 | 0.95167 |
| `algorithm/search/hashmap_lookup.py` | -- | 0.9365 | 0.70101 | 0.81766 | 0.95399 | 0.8608 | 0.9235 | 0.98245 |
| `algorithm/search/index.py` | -- | 0.95005 | 0.71559 | 0.83149 | 0.94145 | 0.87534 | 0.95222 | 0.97916 |
| `algorithm/search/linear.py` | -- | 1.01905 | 0.74245 | 0.85586 | 0.98489 | 0.93797 | 0.97317 | 1.04693 |
| `algorithm/sorting/naive_bubble_sort.py` | 1.0842 | 0.976 | 0.75459 | 1.5778 | 1.85014 | 1.81177 | 1.77029 | 1.57552 |
| `algorithm/twosum/twosum.py` | 0.0576 | 0.08287 | 0.07074 | 0.07423 | 0.08097 | 0.07019 | 0.06443 | 0.07765 |
| `algorithm/twosum/twosum_naive.py` | 0.05744 | 0.0826 | 0.07138 | 0.07442 | 0.08121 | 0.06942 | 0.06452 | 0.0777 |
| `complex/classes/classes.py` | 0.02182 | 0.02247 | 0.02267 | 0.03863 | 0.04205 | 0.03809 | 0.03709 | 0.04206 |
| `complex/classes/dataclasses_.py` | 0.12942 | 0.128 | 0.10737 | 0.11475 | 0.12662 | 0.10185 | 0.09464 | -- |
| `complex/classes/namedtuple_classes.py` | 0.06487 | 0.09183 | 0.07798 | 0.08213 | 0.09219 | 0.07781 | 0.0739 | 0.08799 |
| `complex/classes/simplenamespace.py` | 0.02902 | 0.02732 | 0.02381 | 0.04057 | 0.04553 | 0.03947 | 0.038 | 0.05887 |
| `complex/classes/sloted_classes.py` | 0.021 | 0.02098 | 0.02226 | 0.03832 | 0.04242 | 0.0381 | 0.03729 | 0.0422 |
| `complex/generators/readlines.py` | 0.01852 | 0.02453 | 0.01605 | 0.03156 | 0.03307 | 0.02984 | 0.02838 | 0.03478 |
| `complex/generators/simple.py` | 0.04414 | 0.03821 | 0.03448 | 0.05572 | 0.05927 | 0.05625 | 0.05682 | 0.06261 |
| `dummy/dummy.py` | 0.01513 | 0.01217 | 0.01111 | 0.02766 | 0.02966 | 0.02812 | 0.02424 | 0.02766 |
| `long_run/database/postgresql.py` | -- | 0.17097 | 0.14541 | 0.1457 | 0.15802 | 0.14117 | 0.12993 | 0.14216 |
| `long_run/database/sqlite_.py` | -- | 0.67693 | 0.58907 | 0.57162 | 0.60883 | 0.55875 | 0.50296 | 0.57048 |
| `long_run/file/load_titanic_csv_pandas.py` | -- | 0.71203 | 0.60302 | 0.59538 | 0.64132 | 0.59219 | 0.5406 | 0.6334 |
| `long_run/file/load_titanic_csv_python.py` | 0.06948 | 0.06512 | 0.05607 | 0.06535 | 0.07316 | 0.06402 | 0.06056 | 0.06774 |
| `long_run/processes/collect_names_from_site.py` | -- | 2.26097 | 2.00892 | 2.11836 | 2.443 | 1.84177 | -- | -- |
| `long_run/processes/generate_fake_data.py` | -- | 0.89491 | 0.78112 | 0.79296 | 0.82586 | 0.76332 | 0.73519 | 0.78858 |
| `long_run/processes/maze_generator.py` | 0.09984 | 0.10221 | 0.08996 | 0.13238 | 0.18778 | 0.17573 | 0.18184 | 0.18391 |
| `long_run/text/clean_text.py` | 0.20446 | 0.19754 | 0.18524 | 0.19308 | 0.21008 | 0.19495 | 0.18996 | 0.19815 |
| `long_run/text/count_words.py` | 0.08669 | 0.07796 | 0.07049 | 0.08325 | 0.09214 | 0.0816 | 0.07668 | 0.0841 |
| `math/haversine.py` | 0.45287 | 0.52207 | 0.44691 | 0.52205 | 0.63104 | 0.51497 | 0.61616 | 0.57009 |
| `math/mandelbrot.py` | -- | 2.60646 | 2.5503 | 2.5831 | 2.59358 | 3.00424 | 3.02053 | 3.14751 |
| `math/pow_simple.py` | 0.27456 | 0.28003 | 0.25243 | 0.35625 | 0.37658 | 0.40296 | 0.40301 | 0.37934 |
| `math/pow_using_math.py` | 0.84077 | 0.88188 | 0.74269 | 0.91204 | 0.96272 | 0.93537 | 1.22747 | 1.1103 |
| `modules/json/json_module.py` | 0.29779 | 0.30584 | 0.27897 | 0.30339 | 0.36037 | 0.32325 | 0.36531 | 0.35783 |
| `modules/json/orjson_module.py` | -- | 0.26558 | 0.20906 | 0.241 | 0.26272 | 0.22564 | 0.1981 | 0.2449 |
| `programming_game_benchmark/nbody.py` | 0.15416 | 0.15414 | 0.15103 | 0.28471 | 0.31092 | 0.28887 | 0.27058 | 0.25367 |
| `programming_game_benchmark/spectral_norm.py` | 0.50736 | 0.50912 | 0.46564 | 0.49938 | 0.56292 | 0.54358 | 0.61714 | 0.62503 |

#### **Memory Usage**

##### **MEM [MB]**
| Command | 3.13 | 3.12 | 3.11 | 3.10 | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | -- | 35.93359 | 35.86719 | 32.55413 | 30.22266 | 29.52511 | 30.26507 | 28.87556 |
| `algorithm/search/hashmap_lookup.py` | -- | 37.25 | 35.21373 | 33.6769 | 31.4481 | 30.25391 | 30.75167 | 28.1942 |
| `algorithm/search/index.py` | -- | 35.78181 | 35.70815 | 32.65011 | 30.45145 | 29.53571 | 28.78739 | 28.64621 |
| `algorithm/search/linear.py` | -- | 36.04743 | 34.70982 | 33.28404 | 31.23103 | 29.68192 | 29.94475 | 28.78181 |
| `algorithm/sorting/naive_bubble_sort.py` | 28.16295 | 27.26618 | 26.899 | 24.13783 | 23.13449 | 22.01228 | 21.40737 | 21.41462 |
| `algorithm/twosum/twosum.py` | 28.21763 | 27.63504 | 26.43973 | 23.22712 | 22.83929 | 21.69308 | 20.68583 | 21.98326 |
| `algorithm/twosum/twosum_naive.py` | 28.21261 | 27.11496 | 26.92634 | 23.60156 | 23.45815 | 21.77958 | 20.93415 | 22.02511 |
| `complex/classes/classes.py` | 29.35826 | 28.30692 | 27.99888 | 25.2115 | 22.98214 | 21.95368 | 20.66406 | 21.84989 |
| `complex/classes/dataclasses_.py` | 29.42746 | 28.03404 | 28.37109 | 25.39509 | 23.66183 | 21.9442 | 21.36272 | -- |
| `complex/classes/namedtuple_classes.py` | 28.58929 | 27.74554 | 27.14453 | 24.70647 | 23.16239 | 21.67188 | 21.06696 | 22.05525 |
| `complex/classes/simplenamespace.py` | 30.00112 | 28.68862 | 28.71652 | 26.07422 | 23.67634 | 21.99721 | 21.22879 | 22.54297 |
| `complex/classes/sloted_classes.py` | 29.27121 | 27.74442 | 28.29353 | 25.67746 | 23.7846 | 21.57533 | 20.83315 | 21.56585 |
| `complex/generators/readlines.py` | 28.20982 | 27.23103 | 26.8856 | 23.39453 | 23.26228 | 21.71708 | 20.65402 | 21.30915 |
| `complex/generators/simple.py` | 30.23996 | 29.27902 | 29.0279 | 25.50502 | 23.46596 | 21.88002 | 21.27455 | 21.86272 |
| `dummy/dummy.py` | 28.51897 | 27.41908 | 26.85714 | 23.95592 | 22.70871 | 21.53906 | 20.7567 | 21.46261 |
| `long_run/database/postgresql.py` | -- | 32.85268 | 32.54687 | 29.21708 | 28.86328 | 27.32757 | 26.78404 | 27.2048 |
| `long_run/database/sqlite_.py` | -- | 75.45033 | 71.99275 | 66.31752 | 66.91741 | 65.92076 | 65.43638 | 62.85658 |
| `long_run/file/load_titanic_csv_pandas.py` | -- | 74.1635 | 70.37835 | 64.17522 | 65.39565 | 64.04408 | 63.64509 | 61.46652 |
| `long_run/file/load_titanic_csv_python.py` | 28.25 | 27.44475 | 27.22991 | 23.99163 | 23.5625 | 21.80692 | 20.92746 | 21.76339 |
| `long_run/processes/collect_names_from_site.py` | -- | 48.79743 | 47.82757 | 46.2779 | 46.48884 | 46.07812 | -- | -- |
| `long_run/processes/generate_fake_data.py` | -- | 74.90011 | 70.9721 | 67.84821 | 68.83929 | 65.54743 | 68.64565 | 63.43136 |
| `long_run/processes/maze_generator.py` | 28.22712 | 27.26786 | 26.98772 | 24.54129 | 23.35826 | 22.00502 | 21.5279 | 21.67076 |
| `long_run/text/clean_text.py` | 28.3231 | 27.70871 | 26.52567 | 23.28069 | 22.89007 | 21.80301 | 21.02846 | 22.08594 |
| `long_run/text/count_words.py` | 28.32143 | 27.28516 | 26.95312 | 23.41127 | 23.28181 | 21.55804 | 20.73103 | 21.43192 |
| `math/haversine.py` | 28.23382 | 27.74833 | 27.0865 | 24.17913 | 22.88672 | 21.97433 | 20.94643 | 21.68806 |
| `math/mandelbrot.py` | -- | 40.3817 | 39.60156 | 37.54353 | 42.53237 | 35.60045 | 34.95201 | 35.91295 |
| `math/pow_simple.py` | 28.12221 | 27.61217 | 26.95759 | 24.04911 | 22.72991 | 21.86886 | 20.92522 | 21.4308 |
| `math/pow_using_math.py` | 28.60491 | 27.07478 | 26.94196 | 23.8192 | 22.78237 | 21.74163 | 20.94866 | 21.49275 |
| `modules/json/json_module.py` | 28.23605 | 27.63728 | 26.77734 | 23.42522 | 22.94252 | 21.96763 | 21.94141 | 21.46094 |
| `modules/json/orjson_module.py` | -- | 28.09654 | 27.41127 | 23.78739 | 23.38114 | 22.39621 | 22.29799 | 22.3058 |
| `programming_game_benchmark/nbody.py` | 28.22098 | 27.09208 | 27.02623 | 23.64397 | 23.47824 | 21.49554 | 20.99777 | 21.45703 |
| `programming_game_benchmark/spectral_norm.py` | 28.40737 | 27.85491 | 26.87723 | 24.37835 | 23.75725 | 22.63783 | 22.35658 | 21.81752 |

---


### **Python 3.6**

```bash
Python 3.6.15

Linux 9eef0049b5a9 6.5.0-35-generic unknown GNU/Linux

CPU(s):                             12
Thread(s) per core:                 2
Core(s) per socket:                 6
NUMA node(s):                       1
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:                        4100.0000
NUMA node0 CPU(s):                  0-11

MemTotal:       16061436 kB
MemFree:         9973888 kB
MemAvailable:   14639460 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 0.95248 | 0.01088 | 0.95167 | 0.93973 | 0.96694 | 28.87556 |
| `algorithm/search/hashmap_lookup.py` | yes | 0.98399 | 0.02349 | 0.98245 | 0.95972 | 1.02239 | 28.1942 |
| `algorithm/search/index.py` | yes | 0.98305 | 0.01445 | 0.97916 | 0.96625 | 1.008 | 28.64621 |
| `algorithm/search/linear.py` | yes | 1.03756 | 0.03538 | 1.04693 | 0.9964 | 1.10048 | 28.78181 |
| `algorithm/sorting/naive_bubble_sort.py` | yes | 1.56694 | 0.12518 | 1.57552 | 1.37647 | 1.76619 | 21.41462 |
| `algorithm/twosum/twosum.py` | yes | 0.07774 | 0.00058 | 0.07765 | 0.07705 | 0.07881 | 21.98326 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07799 | 0.00064 | 0.0777 | 0.07733 | 0.07875 | 22.02511 |
| `complex/classes/classes.py` | yes | 0.04193 | 0.00042 | 0.04206 | 0.04114 | 0.04233 | 21.84989 |
| `complex/classes/dataclasses_.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `complex/classes/namedtuple_classes.py` | yes | 0.08822 | 0.00144 | 0.08799 | 0.08688 | 0.09121 | 22.05525 |
| `complex/classes/simplenamespace.py` | yes | 0.05846 | 0.00087 | 0.05887 | 0.05697 | 0.05944 | 22.54297 |
| `complex/classes/sloted_classes.py` | yes | 0.04223 | 0.00049 | 0.0422 | 0.04169 | 0.04283 | 21.56585 |
| `complex/generators/readlines.py` | yes | 0.0348 | 0.00044 | 0.03478 | 0.03404 | 0.03532 | 21.30915 |
| `complex/generators/simple.py` | yes | 0.06238 | 0.00066 | 0.06261 | 0.06119 | 0.06314 | 21.86272 |
| `dummy/dummy.py` | yes | 0.02766 | 0.00035 | 0.02766 | 0.02715 | 0.02819 | 21.46261 |
| `long_run/database/postgresql.py` | yes | 0.14319 | 0.00351 | 0.14216 | 0.14082 | 0.151 | 27.2048 |
| `long_run/database/sqlite_.py` | yes | 0.5707 | 0.00311 | 0.57048 | 0.56831 | 0.57711 | 62.85658 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.63318 | 0.00716 | 0.6334 | 0.62465 | 0.64501 | 61.46652 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06818 | 0.00188 | 0.06774 | 0.06697 | 0.07233 | 21.76339 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | yes | 0.79067 | 0.00521 | 0.78858 | 0.7862 | 0.80112 | 63.43136 |
| `long_run/processes/maze_generator.py` | yes | 0.18345 | 0.00882 | 0.18391 | 0.17161 | 0.19767 | 21.67076 |
| `long_run/text/clean_text.py` | yes | 0.19832 | 0.00073 | 0.19815 | 0.1974 | 0.19943 | 22.08594 |
| `long_run/text/count_words.py` | yes | 0.0845 | 0.00123 | 0.0841 | 0.08376 | 0.08725 | 21.43192 |
| `math/haversine.py` | yes | 0.56907 | 0.01185 | 0.57009 | 0.55651 | 0.58419 | 21.68806 |
| `math/mandelbrot.py` | yes | 3.11654 | 0.094 | 3.14751 | 2.93734 | 3.19901 | 35.91295 |
| `math/pow_simple.py` | yes | 0.37945 | 0.00402 | 0.37934 | 0.37512 | 0.38701 | 21.4308 |
| `math/pow_using_math.py` | yes | 1.11168 | 0.01797 | 1.1103 | 1.09084 | 1.14592 | 21.49275 |
| `modules/json/json_module.py` | yes | 0.3611 | 0.00856 | 0.35783 | 0.3528 | 0.37436 | 21.46094 |
| `modules/json/orjson_module.py` | yes | 0.24262 | 0.00992 | 0.2449 | 0.23153 | 0.25637 | 22.3058 |
| `programming_game_benchmark/nbody.py` | yes | 0.25418 | 0.00172 | 0.25367 | 0.2527 | 0.25672 | 21.45703 |
| `programming_game_benchmark/spectral_norm.py` | yes | 0.60162 | 0.04704 | 0.62503 | 0.50928 | 0.63263 | 21.81752 |


### **Python 3.7**

```bash
Python 3.7.17

Linux d2d000a9fbbe 6.5.0-35-generic unknown GNU/Linux

CPU(s):                             12
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:                 2
Core(s) per socket:                 6
CPU max MHz:                        4100.0000
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-11

MemTotal:       16061436 kB
MemFree:         9871816 kB
MemAvailable:   14617804 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 0.92136 | 0.00501 | 0.92205 | 0.91382 | 0.92955 | 30.26507 |
| `algorithm/search/hashmap_lookup.py` | yes | 0.92664 | 0.01797 | 0.9235 | 0.90403 | 0.95967 | 30.75167 |
| `algorithm/search/index.py` | yes | 1.31239 | 0.68193 | 0.95222 | 0.93095 | 2.72405 | 28.78739 |
| `algorithm/search/linear.py` | yes | 0.98116 | 0.02055 | 0.97317 | 0.95501 | 1.01392 | 29.94475 |
| `algorithm/sorting/naive_bubble_sort.py` | yes | 1.77332 | 0.04125 | 1.77029 | 1.70379 | 1.8291 | 21.40737 |
| `algorithm/twosum/twosum.py` | yes | 0.06447 | 0.00039 | 0.06443 | 0.06393 | 0.06494 | 20.68583 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.06453 | 0.00036 | 0.06452 | 0.06409 | 0.06504 | 20.93415 |
| `complex/classes/classes.py` | yes | 0.03722 | 0.00079 | 0.03709 | 0.03626 | 0.03868 | 20.66406 |
| `complex/classes/dataclasses_.py` | yes | 0.09464 | 0.00034 | 0.09464 | 0.09417 | 0.09501 | 21.36272 |
| `complex/classes/namedtuple_classes.py` | yes | 0.07374 | 0.0003 | 0.0739 | 0.07313 | 0.07395 | 21.06696 |
| `complex/classes/simplenamespace.py` | yes | 0.03859 | 0.00144 | 0.038 | 0.03767 | 0.04179 | 21.22879 |
| `complex/classes/sloted_classes.py` | yes | 0.03747 | 0.00133 | 0.03729 | 0.03621 | 0.0403 | 20.83315 |
| `complex/generators/readlines.py` | yes | 0.02843 | 0.00039 | 0.02838 | 0.02781 | 0.02911 | 20.65402 |
| `complex/generators/simple.py` | yes | 0.05758 | 0.00192 | 0.05682 | 0.05602 | 0.06112 | 21.27455 |
| `dummy/dummy.py` | yes | 0.02439 | 0.00024 | 0.02424 | 0.02414 | 0.02466 | 20.7567 |
| `long_run/database/postgresql.py` | yes | 0.13001 | 0.00029 | 0.12993 | 0.1296 | 0.13052 | 26.78404 |
| `long_run/database/sqlite_.py` | yes | 0.50288 | 0.00168 | 0.50296 | 0.49935 | 0.50437 | 65.43638 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.54816 | 0.01478 | 0.5406 | 0.5374 | 0.57046 | 63.64509 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06088 | 0.00056 | 0.06056 | 0.06038 | 0.06161 | 20.92746 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | yes | 0.73538 | 0.00507 | 0.73519 | 0.72894 | 0.74122 | 68.64565 |
| `long_run/processes/maze_generator.py` | yes | 0.17994 | 0.0143 | 0.18184 | 0.15409 | 0.19757 | 21.5279 |
| `long_run/text/clean_text.py` | yes | 0.19076 | 0.00813 | 0.18996 | 0.18382 | 0.20755 | 21.02846 |
| `long_run/text/count_words.py` | yes | 0.07659 | 0.00032 | 0.07668 | 0.07622 | 0.07705 | 20.73103 |
| `math/haversine.py` | yes | 0.61351 | 0.00918 | 0.61616 | 0.59716 | 0.62578 | 20.94643 |
| `math/mandelbrot.py` | yes | 3.0154 | 0.09965 | 3.02053 | 2.82337 | 3.16355 | 34.95201 |
| `math/pow_simple.py` | yes | 0.39995 | 0.00683 | 0.40301 | 0.38961 | 0.40806 | 20.92522 |
| `math/pow_using_math.py` | yes | 1.22941 | 0.02335 | 1.22747 | 1.20316 | 1.26543 | 20.94866 |
| `modules/json/json_module.py` | yes | 0.36434 | 0.0079 | 0.36531 | 0.35525 | 0.3784 | 21.94141 |
| `modules/json/orjson_module.py` | yes | 0.19725 | 0.00342 | 0.1981 | 0.19219 | 0.20121 | 22.29799 |
| `programming_game_benchmark/nbody.py` | yes | 0.27157 | 0.00237 | 0.27058 | 0.26913 | 0.27635 | 20.99777 |
| `programming_game_benchmark/spectral_norm.py` | yes | 0.61314 | 0.01799 | 0.61714 | 0.58948 | 0.63431 | 22.35658 |


### **Python 3.8**

```bash
Python 3.8.19

Linux 9382814413bd 6.5.0-35-generic unknown GNU/Linux

CPU(s):                             12
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:                 2
Core(s) per socket:                 6
CPU max MHz:                        4100.0000
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-11

MemTotal:       16061436 kB
MemFree:        10196196 kB
MemAvailable:   14577244 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 0.87258 | 0.01479 | 0.86883 | 0.85771 | 0.89284 | 29.52511 |
| `algorithm/search/hashmap_lookup.py` | yes | 0.87215 | 0.02086 | 0.8608 | 0.85313 | 0.90557 | 30.25391 |
| `algorithm/search/index.py` | yes | 0.87827 | 0.01807 | 0.87534 | 0.85833 | 0.9091 | 29.53571 |
| `algorithm/search/linear.py` | yes | 0.93543 | 0.0303 | 0.93797 | 0.89062 | 0.97979 | 29.68192 |
| `algorithm/sorting/naive_bubble_sort.py` | yes | 1.80613 | 0.09052 | 1.81177 | 1.67976 | 1.945 | 22.01228 |
| `algorithm/twosum/twosum.py` | yes | 0.06996 | 0.00054 | 0.07019 | 0.06904 | 0.07061 | 21.69308 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.06915 | 0.00062 | 0.06942 | 0.06844 | 0.06979 | 21.77958 |
| `complex/classes/classes.py` | yes | 0.03802 | 0.00041 | 0.03809 | 0.03762 | 0.03879 | 21.95368 |
| `complex/classes/dataclasses_.py` | yes | 0.10179 | 0.00121 | 0.10185 | 0.10035 | 0.1041 | 21.9442 |
| `complex/classes/namedtuple_classes.py` | yes | 0.07778 | 0.00067 | 0.07781 | 0.07695 | 0.07905 | 21.67188 |
| `complex/classes/simplenamespace.py` | yes | 0.04025 | 0.0022 | 0.03947 | 0.03901 | 0.04521 | 21.99721 |
| `complex/classes/sloted_classes.py` | yes | 0.03886 | 0.00137 | 0.0381 | 0.03765 | 0.04085 | 21.57533 |
| `complex/generators/readlines.py` | yes | 0.03022 | 0.00109 | 0.02984 | 0.02918 | 0.03252 | 21.71708 |
| `complex/generators/simple.py` | yes | 0.05757 | 0.00351 | 0.05625 | 0.05589 | 0.06549 | 21.88002 |
| `dummy/dummy.py` | yes | 0.02833 | 0.00076 | 0.02812 | 0.02738 | 0.02928 | 21.53906 |
| `leetcode/add_two_numbers/add_2_num.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `leetcode/merge_sorted_array/merge_sorted.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `leetcode/palindrome/palin.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `leetcode/remove_element/rem_element.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `leetcode/roman_numbers/int2roman.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `leetcode/roman_numbers/roman2int.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `leetcode/square_root/sqrt.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/database/postgresql.py` | yes | 0.14168 | 0.002 | 0.14117 | 0.13998 | 0.14609 | 27.32757 |
| `long_run/database/sqlite_.py` | yes | 0.56177 | 0.00764 | 0.55875 | 0.55532 | 0.57497 | 65.92076 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.59432 | 0.00656 | 0.59219 | 0.58947 | 0.60826 | 64.04408 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06439 | 0.00117 | 0.06402 | 0.06334 | 0.06665 | 21.80692 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.84333 | 0.03567 | 1.84177 | 1.80577 | 1.91652 | 46.07812 |
| `long_run/processes/generate_fake_data.py` | yes | 0.76546 | 0.0074 | 0.76332 | 0.75583 | 0.77497 | 65.54743 |
| `long_run/processes/maze_generator.py` | yes | 0.17758 | 0.00982 | 0.17573 | 0.16294 | 0.19488 | 22.00502 |
| `long_run/text/clean_text.py` | yes | 0.19567 | 0.00206 | 0.19495 | 0.19387 | 0.20006 | 21.80301 |
| `long_run/text/count_words.py` | yes | 0.08234 | 0.00198 | 0.0816 | 0.08049 | 0.08614 | 21.55804 |
| `math/haversine.py` | yes | 0.51517 | 0.00304 | 0.51497 | 0.51154 | 0.51955 | 21.97433 |
| `math/mandelbrot.py` | yes | 2.98394 | 0.05755 | 3.00424 | 2.89974 | 3.04121 | 35.60045 |
| `math/pow_simple.py` | yes | 0.40502 | 0.0049 | 0.40296 | 0.40083 | 0.41513 | 21.86886 |
| `math/pow_using_math.py` | yes | 0.9471 | 0.02927 | 0.93537 | 0.9169 | 0.99325 | 21.74163 |
| `modules/json/json_module.py` | yes | 0.32339 | 0.00242 | 0.32325 | 0.32015 | 0.32793 | 21.96763 |
| `modules/json/orjson_module.py` | yes | 0.22614 | 0.00216 | 0.22564 | 0.22394 | 0.23077 | 22.39621 |
| `programming_game_benchmark/nbody.py` | yes | 0.28979 | 0.00277 | 0.28887 | 0.28846 | 0.29604 | 21.49554 |
| `programming_game_benchmark/spectral_norm.py` | yes | 0.54514 | 0.0085 | 0.54358 | 0.53658 | 0.56224 | 22.63783 |


### **Python 3.9**

```bash
Python 3.9.19

Linux 082cc9acd494 6.5.0-35-generic unknown GNU/Linux

CPU(s):                             12
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:                 2
Core(s) per socket:                 6
CPU max MHz:                        4100.0000
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-11

MemTotal:       16061436 kB
MemFree:         9724276 kB
MemAvailable:   14626280 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 0.9378 | 0.02387 | 0.94316 | 0.90767 | 0.96838 | 30.22266 |
| `algorithm/search/hashmap_lookup.py` | yes | 0.94287 | 0.01741 | 0.95399 | 0.92266 | 0.95877 | 31.4481 |
| `algorithm/search/index.py` | yes | 0.94867 | 0.01913 | 0.94145 | 0.92482 | 0.97729 | 30.45145 |
| `algorithm/search/linear.py` | yes | 1.00502 | 0.05583 | 0.98489 | 0.96229 | 1.11697 | 31.23103 |
| `algorithm/sorting/naive_bubble_sort.py` | yes | 1.81574 | 0.17043 | 1.85014 | 1.4884 | 2.01759 | 23.13449 |
| `algorithm/twosum/twosum.py` | yes | 0.08096 | 0.00022 | 0.08097 | 0.08058 | 0.08124 | 22.83929 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.08112 | 0.00046 | 0.08121 | 0.08038 | 0.08162 | 23.45815 |
| `complex/classes/classes.py` | yes | 0.04197 | 0.00048 | 0.04205 | 0.04133 | 0.04264 | 22.98214 |
| `complex/classes/dataclasses_.py` | yes | 0.12694 | 0.00159 | 0.12662 | 0.12535 | 0.13018 | 23.66183 |
| `complex/classes/namedtuple_classes.py` | yes | 0.09193 | 0.00104 | 0.09219 | 0.08974 | 0.09287 | 23.16239 |
| `complex/classes/simplenamespace.py` | yes | 0.04548 | 0.00033 | 0.04553 | 0.04496 | 0.04583 | 23.67634 |
| `complex/classes/sloted_classes.py` | yes | 0.04257 | 0.00054 | 0.04242 | 0.04174 | 0.04346 | 23.7846 |
| `complex/generators/readlines.py` | yes | 0.03393 | 0.00187 | 0.03307 | 0.03258 | 0.03735 | 23.26228 |
| `complex/generators/simple.py` | yes | 0.06131 | 0.0036 | 0.05927 | 0.05895 | 0.06742 | 23.46596 |
| `dummy/dummy.py` | yes | 0.02976 | 0.00073 | 0.02966 | 0.02909 | 0.03118 | 22.70871 |
| `long_run/database/postgresql.py` | yes | 0.15841 | 0.00076 | 0.15802 | 0.15748 | 0.15964 | 28.86328 |
| `long_run/database/sqlite_.py` | yes | 0.60773 | 0.00278 | 0.60883 | 0.60272 | 0.61132 | 66.91741 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.64489 | 0.00662 | 0.64132 | 0.63854 | 0.65426 | 65.39565 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.07324 | 0.00046 | 0.07316 | 0.07278 | 0.07396 | 23.5625 |
| `long_run/processes/collect_names_from_site.py` | yes | 2.40169 | 0.31376 | 2.443 | 2.03625 | 2.88384 | 46.48884 |
| `long_run/processes/generate_fake_data.py` | yes | 0.83005 | 0.01297 | 0.82586 | 0.82181 | 0.85898 | 68.83929 |
| `long_run/processes/maze_generator.py` | yes | 0.18898 | 0.01999 | 0.18778 | 0.16505 | 0.223 | 23.35826 |
| `long_run/text/clean_text.py` | yes | 0.20994 | 0.0015 | 0.21008 | 0.20723 | 0.21199 | 22.89007 |
| `long_run/text/count_words.py` | yes | 0.09214 | 0.00096 | 0.09214 | 0.09073 | 0.09355 | 23.28181 |
| `math/haversine.py` | yes | 0.63033 | 0.0184 | 0.63104 | 0.60328 | 0.65873 | 22.88672 |
| `math/mandelbrot.py` | yes | 2.60233 | 0.0333 | 2.59358 | 2.58071 | 2.67638 | 42.53237 |
| `math/pow_simple.py` | yes | 0.37772 | 0.00463 | 0.37658 | 0.37375 | 0.3871 | 22.72991 |
| `math/pow_using_math.py` | yes | 0.96209 | 0.00487 | 0.96272 | 0.95413 | 0.96957 | 22.78237 |
| `modules/json/json_module.py` | yes | 0.35741 | 0.00896 | 0.36037 | 0.34228 | 0.36786 | 22.94252 |
| `modules/json/orjson_module.py` | yes | 0.26553 | 0.00618 | 0.26272 | 0.25937 | 0.27677 | 23.38114 |
| `programming_game_benchmark/nbody.py` | yes | 0.31314 | 0.0053 | 0.31092 | 0.30774 | 0.32227 | 23.47824 |
| `programming_game_benchmark/spectral_norm.py` | yes | 0.5657 | 0.00871 | 0.56292 | 0.55702 | 0.58296 | 23.75725 |


### **Python 3.10**

```bash
Python 3.10.14

Linux 19daad0f05ae 6.5.0-35-generic unknown GNU/Linux

CPU(s):                             12
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:                 2
Core(s) per socket:                 6
CPU max MHz:                        4100.0000
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-11

MemTotal:       16061436 kB
MemFree:         9654728 kB
MemAvailable:   14628324 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 0.82137 | 0.01632 | 0.82886 | 0.79656 | 0.83482 | 32.55413 |
| `algorithm/search/hashmap_lookup.py` | yes | 0.81942 | 0.00982 | 0.81766 | 0.80341 | 0.83189 | 33.6769 |
| `algorithm/search/index.py` | yes | 0.82895 | 0.00955 | 0.83149 | 0.8168 | 0.84061 | 32.65011 |
| `algorithm/search/linear.py` | yes | 0.87216 | 0.02397 | 0.85586 | 0.85119 | 0.91367 | 33.28404 |
| `algorithm/sorting/naive_bubble_sort.py` | yes | 1.58395 | 0.12388 | 1.5778 | 1.40142 | 1.82123 | 24.13783 |
| `algorithm/twosum/twosum.py` | yes | 0.07428 | 0.00049 | 0.07423 | 0.07371 | 0.07514 | 23.22712 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07529 | 0.00238 | 0.07442 | 0.07392 | 0.0806 | 23.60156 |
| `complex/classes/classes.py` | yes | 0.03873 | 0.00043 | 0.03863 | 0.0382 | 0.03949 | 25.2115 |
| `complex/classes/dataclasses_.py` | yes | 0.11497 | 0.00061 | 0.11475 | 0.11426 | 0.11572 | 25.39509 |
| `complex/classes/namedtuple_classes.py` | yes | 0.08249 | 0.00095 | 0.08213 | 0.0817 | 0.08453 | 24.70647 |
| `complex/classes/simplenamespace.py` | yes | 0.04075 | 0.00054 | 0.04057 | 0.04023 | 0.04183 | 26.07422 |
| `complex/classes/sloted_classes.py` | yes | 0.03823 | 0.00032 | 0.03832 | 0.03769 | 0.03853 | 25.67746 |
| `complex/generators/readlines.py` | yes | 0.03158 | 0.00051 | 0.03156 | 0.03094 | 0.03253 | 23.39453 |
| `complex/generators/simple.py` | yes | 0.05574 | 0.00059 | 0.05572 | 0.05511 | 0.05679 | 25.50502 |
| `dummy/dummy.py` | yes | 0.02766 | 0.00014 | 0.02766 | 0.02747 | 0.02783 | 23.95592 |
| `long_run/database/postgresql.py` | yes | 0.14572 | 0.00126 | 0.1457 | 0.14354 | 0.14765 | 29.21708 |
| `long_run/database/sqlite_.py` | yes | 0.57457 | 0.00708 | 0.57162 | 0.56771 | 0.58371 | 66.31752 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.5993 | 0.00745 | 0.59538 | 0.5936 | 0.61161 | 64.17522 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06523 | 0.00038 | 0.06535 | 0.06456 | 0.06571 | 23.99163 |
| `long_run/processes/collect_names_from_site.py` | yes | 2.18503 | 0.17893 | 2.11836 | 2.01061 | 2.46185 | 46.2779 |
| `long_run/processes/generate_fake_data.py` | yes | 0.78863 | 0.01245 | 0.79296 | 0.7746 | 0.80908 | 67.84821 |
| `long_run/processes/maze_generator.py` | yes | 0.1386 | 0.01298 | 0.13238 | 0.126 | 0.1625 | 24.54129 |
| `long_run/text/clean_text.py` | yes | 0.19521 | 0.00363 | 0.19308 | 0.19195 | 0.2007 | 23.28069 |
| `long_run/text/count_words.py` | yes | 0.08388 | 0.00169 | 0.08325 | 0.08272 | 0.08759 | 23.41127 |
| `math/haversine.py` | yes | 0.52099 | 0.00801 | 0.52205 | 0.50613 | 0.53091 | 24.17913 |
| `math/mandelbrot.py` | yes | 2.59152 | 0.03491 | 2.5831 | 2.56519 | 2.66879 | 37.54353 |
| `math/pow_simple.py` | yes | 0.35752 | 0.00384 | 0.35625 | 0.35332 | 0.36511 | 24.04911 |
| `math/pow_using_math.py` | yes | 0.90708 | 0.02242 | 0.91204 | 0.87706 | 0.93088 | 23.8192 |
| `modules/json/json_module.py` | yes | 0.30488 | 0.00631 | 0.30339 | 0.29917 | 0.31863 | 23.42522 |
| `modules/json/orjson_module.py` | yes | 0.24336 | 0.00552 | 0.241 | 0.23969 | 0.2553 | 23.78739 |
| `programming_game_benchmark/nbody.py` | yes | 0.28464 | 0.00803 | 0.28471 | 0.27429 | 0.29808 | 23.64397 |
| `programming_game_benchmark/spectral_norm.py` | yes | 0.49612 | 0.00849 | 0.49938 | 0.48219 | 0.50331 | 24.37835 |


### **Python 3.11**

```bash
Python 3.11.9

Linux 3782eef4f6a7 6.5.0-35-generic unknown GNU/Linux

CPU(s):                             12
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:                 2
Core(s) per socket:                 6
CPU max MHz:                        4100.0000
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-11

MemTotal:       16061436 kB
MemFree:         9578380 kB
MemAvailable:   14629100 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 0.69468 | 0.00784 | 0.69346 | 0.68485 | 0.7052 | 35.86719 |
| `algorithm/search/hashmap_lookup.py` | yes | 0.70175 | 0.01075 | 0.70101 | 0.68963 | 0.72036 | 35.21373 |
| `algorithm/search/index.py` | yes | 0.7182 | 0.01708 | 0.71559 | 0.69455 | 0.74247 | 35.70815 |
| `algorithm/search/linear.py` | yes | 0.74847 | 0.01664 | 0.74245 | 0.73161 | 0.77787 | 34.70982 |
| `algorithm/sorting/naive_bubble_sort.py` | yes | 0.75156 | 0.07215 | 0.75459 | 0.6559 | 0.87069 | 26.899 |
| `algorithm/twosum/twosum.py` | yes | 0.07098 | 0.00082 | 0.07074 | 0.07028 | 0.07274 | 26.43973 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07122 | 0.00043 | 0.07138 | 0.07053 | 0.07164 | 26.92634 |
| `complex/classes/classes.py` | yes | 0.02239 | 0.001 | 0.02267 | 0.02015 | 0.02295 | 27.99888 |
| `complex/classes/dataclasses_.py` | yes | 0.10781 | 0.00122 | 0.10737 | 0.10705 | 0.11051 | 28.37109 |
| `complex/classes/namedtuple_classes.py` | yes | 0.07811 | 0.00054 | 0.07798 | 0.07756 | 0.07905 | 27.14453 |
| `complex/classes/simplenamespace.py` | yes | 0.0241 | 0.00075 | 0.02381 | 0.02331 | 0.02532 | 28.71652 |
| `complex/classes/sloted_classes.py` | yes | 0.02097 | 0.00168 | 0.02226 | 0.01902 | 0.02235 | 28.29353 |
| `complex/generators/readlines.py` | yes | 0.01599 | 0.00011 | 0.01605 | 0.01581 | 0.0161 | 26.8856 |
| `complex/generators/simple.py` | yes | 0.03444 | 0.00036 | 0.03448 | 0.03385 | 0.03485 | 29.0279 |
| `dummy/dummy.py` | yes | 0.01116 | 0.00045 | 0.01111 | 0.01046 | 0.01202 | 26.85714 |
| `long_run/database/postgresql.py` | yes | 0.14558 | 0.00091 | 0.14541 | 0.14398 | 0.14679 | 32.54687 |
| `long_run/database/sqlite_.py` | yes | 0.59141 | 0.00894 | 0.58907 | 0.58099 | 0.60555 | 71.99275 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.6055 | 0.00699 | 0.60302 | 0.6012 | 0.62124 | 70.37835 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.05614 | 0.00047 | 0.05607 | 0.05559 | 0.05679 | 27.22991 |
| `long_run/processes/collect_names_from_site.py` | yes | 2.01276 | 0.16023 | 2.00892 | 1.80602 | 2.29813 | 47.82757 |
| `long_run/processes/generate_fake_data.py` | yes | 0.78531 | 0.01177 | 0.78112 | 0.77403 | 0.8084 | 70.9721 |
| `long_run/processes/maze_generator.py` | yes | 0.09031 | 0.00291 | 0.08996 | 0.08646 | 0.0959 | 26.98772 |
| `long_run/text/clean_text.py` | yes | 0.18338 | 0.0037 | 0.18524 | 0.1776 | 0.18678 | 26.52567 |
| `long_run/text/count_words.py` | yes | 0.0704 | 0.00055 | 0.07049 | 0.0696 | 0.07109 | 26.95312 |
| `math/haversine.py` | yes | 0.45728 | 0.02235 | 0.44691 | 0.43828 | 0.49598 | 27.0865 |
| `math/mandelbrot.py` | yes | 2.56442 | 0.03946 | 2.5503 | 2.54585 | 2.6538 | 39.60156 |
| `math/pow_simple.py` | yes | 0.25234 | 0.00432 | 0.25243 | 0.24689 | 0.25762 | 26.95759 |
| `math/pow_using_math.py` | yes | 0.74549 | 0.00639 | 0.74269 | 0.73813 | 0.75495 | 26.94196 |
| `modules/json/json_module.py` | yes | 0.28156 | 0.00597 | 0.27897 | 0.27586 | 0.2933 | 26.77734 |
| `modules/json/orjson_module.py` | yes | 0.20872 | 0.00254 | 0.20906 | 0.20506 | 0.21232 | 27.41127 |
| `programming_game_benchmark/nbody.py` | yes | 0.15263 | 0.00384 | 0.15103 | 0.15021 | 0.16113 | 27.02623 |
| `programming_game_benchmark/spectral_norm.py` | yes | 0.45453 | 0.02659 | 0.46564 | 0.4228 | 0.4826 | 26.87723 |


### **Python 3.12**

```bash
Python 3.12.3

Linux aebbb706eead 6.5.0-35-generic unknown GNU/Linux

CPU(s):                             12
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:                 2
Core(s) per socket:                 6
CPU max MHz:                        4100.0000
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-11

MemTotal:       16061436 kB
MemFree:         9493536 kB
MemAvailable:   14620848 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 0.93274 | 0.02836 | 0.92768 | 0.90157 | 0.98533 | 35.93359 |
| `algorithm/search/hashmap_lookup.py` | yes | 0.94138 | 0.01324 | 0.9365 | 0.92844 | 0.96281 | 37.25 |
| `algorithm/search/index.py` | yes | 0.95179 | 0.00535 | 0.95005 | 0.94697 | 0.96077 | 35.78181 |
| `algorithm/search/linear.py` | yes | 1.02475 | 0.03073 | 1.01905 | 0.99096 | 1.08925 | 36.04743 |
| `algorithm/sorting/naive_bubble_sort.py` | yes | 0.98292 | 0.08486 | 0.976 | 0.88372 | 1.13474 | 27.26618 |
| `algorithm/twosum/twosum.py` | yes | 0.08259 | 0.00073 | 0.08287 | 0.08136 | 0.08329 | 27.63504 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.08262 | 0.0005 | 0.0826 | 0.08172 | 0.08321 | 27.11496 |
| `complex/classes/classes.py` | yes | 0.02208 | 0.00096 | 0.02247 | 0.02077 | 0.02345 | 28.30692 |
| `complex/classes/dataclasses_.py` | yes | 0.12827 | 0.00112 | 0.128 | 0.12672 | 0.12988 | 28.03404 |
| `complex/classes/namedtuple_classes.py` | yes | 0.09179 | 0.00045 | 0.09183 | 0.09096 | 0.09245 | 27.74554 |
| `complex/classes/simplenamespace.py` | yes | 0.02702 | 0.00054 | 0.02732 | 0.02628 | 0.02751 | 28.68862 |
| `complex/classes/sloted_classes.py` | yes | 0.02163 | 0.0012 | 0.02098 | 0.02081 | 0.02343 | 27.74442 |
| `complex/generators/readlines.py` | yes | 0.02414 | 0.00431 | 0.02453 | 0.01561 | 0.03023 | 27.23103 |
| `complex/generators/simple.py` | yes | 0.03874 | 0.0015 | 0.03821 | 0.03777 | 0.04197 | 29.27902 |
| `dummy/dummy.py` | yes | 0.01291 | 0.00165 | 0.01217 | 0.01209 | 0.0166 | 27.41908 |
| `long_run/database/postgresql.py` | yes | 0.17061 | 0.00159 | 0.17097 | 0.16781 | 0.17301 | 32.85268 |
| `long_run/database/sqlite_.py` | yes | 0.67681 | 0.00435 | 0.67693 | 0.66975 | 0.68363 | 75.45033 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.71334 | 0.00326 | 0.71203 | 0.70968 | 0.71833 | 74.1635 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06514 | 0.0006 | 0.06512 | 0.06445 | 0.06619 | 27.44475 |
| `long_run/processes/collect_names_from_site.py` | yes | 2.25622 | 0.22377 | 2.26097 | 2.01169 | 2.63269 | 48.79743 |
| `long_run/processes/generate_fake_data.py` | yes | 0.89445 | 0.00569 | 0.89491 | 0.88389 | 0.90083 | 74.90011 |
| `long_run/processes/maze_generator.py` | yes | 0.10305 | 0.00285 | 0.10221 | 0.09856 | 0.10734 | 27.26786 |
| `long_run/text/clean_text.py` | yes | 0.1984 | 0.00349 | 0.19754 | 0.19255 | 0.20243 | 27.70871 |
| `long_run/text/count_words.py` | yes | 0.07813 | 0.00084 | 0.07796 | 0.07734 | 0.07976 | 27.28516 |
| `math/haversine.py` | yes | 0.52207 | 0.02182 | 0.52207 | 0.49149 | 0.55083 | 27.74833 |
| `math/mandelbrot.py` | yes | 2.63514 | 0.06426 | 2.60646 | 2.59907 | 2.77759 | 40.3817 |
| `math/pow_simple.py` | yes | 0.28346 | 0.00874 | 0.28003 | 0.27825 | 0.30308 | 27.61217 |
| `math/pow_using_math.py` | yes | 0.88836 | 0.01615 | 0.88188 | 0.87212 | 0.91945 | 27.07478 |
| `modules/json/json_module.py` | yes | 0.30644 | 0.00547 | 0.30584 | 0.29668 | 0.31312 | 27.63728 |
| `modules/json/orjson_module.py` | yes | 0.26638 | 0.00791 | 0.26558 | 0.25567 | 0.2764 | 28.09654 |
| `programming_game_benchmark/nbody.py` | yes | 0.15615 | 0.00498 | 0.15414 | 0.15215 | 0.16621 | 27.09208 |
| `programming_game_benchmark/spectral_norm.py` | yes | 0.5072 | 0.00981 | 0.50912 | 0.48656 | 0.51571 | 27.85491 |


### **Python 3.13**

```bash
Python 3.13.0b2

Linux 83f8a6bbae8f 6.5.0-35-generic unknown GNU/Linux

CPU(s):                             12
Model name:                         Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
Thread(s) per core:                 2
Core(s) per socket:                 6
CPU max MHz:                        4100.0000
NUMA node(s):                       1
NUMA node0 CPU(s):                  0-11

MemTotal:       16061436 kB
MemFree:         9469888 kB
MemAvailable:   14612556 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `algorithm/search/hashmap_lookup.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `algorithm/search/index.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `algorithm/search/linear.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `algorithm/sorting/naive_bubble_sort.py` | yes | 1.08072 | 0.05017 | 1.0842 | 0.98424 | 1.1332 | 28.16295 |
| `algorithm/twosum/twosum.py` | yes | 0.0574 | 0.00061 | 0.0576 | 0.05651 | 0.05815 | 28.21763 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.05764 | 0.00092 | 0.05744 | 0.05675 | 0.05954 | 28.21261 |
| `complex/classes/classes.py` | yes | 0.02236 | 0.00182 | 0.02182 | 0.0206 | 0.02443 | 29.35826 |
| `complex/classes/dataclasses_.py` | yes | 0.13102 | 0.00427 | 0.12942 | 0.1277 | 0.13952 | 29.42746 |
| `complex/classes/namedtuple_classes.py` | yes | 0.06477 | 0.00061 | 0.06487 | 0.0641 | 0.06579 | 28.58929 |
| `complex/classes/simplenamespace.py` | yes | 0.0289 | 0.0005 | 0.02902 | 0.02833 | 0.02945 | 30.00112 |
| `complex/classes/sloted_classes.py` | yes | 0.0227 | 0.00227 | 0.021 | 0.02079 | 0.02535 | 29.27121 |
| `complex/generators/readlines.py` | yes | 0.01838 | 0.00072 | 0.01852 | 0.01735 | 0.01956 | 28.20982 |
| `complex/generators/simple.py` | yes | 0.04477 | 0.00168 | 0.04414 | 0.0436 | 0.04843 | 30.23996 |
| `dummy/dummy.py` | yes | 0.01579 | 0.00174 | 0.01513 | 0.0149 | 0.01971 | 28.51897 |
| `long_run/database/postgresql.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/database/sqlite_.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/file/load_titanic_csv_pandas.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06934 | 0.00055 | 0.06948 | 0.0684 | 0.07012 | 28.25 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/maze_generator.py` | yes | 0.09744 | 0.00793 | 0.09984 | 0.0836 | 0.10816 | 28.22712 |
| `long_run/text/clean_text.py` | yes | 0.20597 | 0.00313 | 0.20446 | 0.20309 | 0.21228 | 28.3231 |
| `long_run/text/count_words.py` | yes | 0.08662 | 0.00095 | 0.08669 | 0.08503 | 0.08766 | 28.32143 |
| `math/haversine.py` | yes | 0.45777 | 0.01939 | 0.45287 | 0.43882 | 0.4972 | 28.23382 |
| `math/mandelbrot.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `math/pow_simple.py` | yes | 0.27789 | 0.0127 | 0.27456 | 0.26733 | 0.30479 | 28.12221 |
| `math/pow_using_math.py` | yes | 0.84617 | 0.02399 | 0.84077 | 0.82821 | 0.89879 | 28.60491 |
| `modules/json/json_module.py` | yes | 0.29619 | 0.0063 | 0.29779 | 0.28758 | 0.30658 | 28.23605 |
| `modules/json/orjson_module.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `programming_game_benchmark/nbody.py` | yes | 0.15483 | 0.00197 | 0.15416 | 0.15331 | 0.15886 | 28.22098 |
| `programming_game_benchmark/spectral_norm.py` | yes | 0.50811 | 0.02602 | 0.50736 | 0.47361 | 0.53646 | 28.40737 |
