# Python Benchmark

This is a simple repo to validate and test any (almost any) python program againts all python 3 versions.

- Python 3.6.15
- Python 3.7.17
- Python 3.8.20
- Python 3.9.23
- Python 3.10.18
- Python 3.11.13
- Python 3.12.11
- Python 3.13.5
- Python 3.14.0rc1

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
# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13, 3.14
```

- @DONT_RUN: This file should not be executed (in case of utils routines);
- @MPROF_INTERVAL: To benchmark memory usage mprof is used, this param you maybe able to improve interval collect of memory;
- @MPROF_MULTIPROCESS: In case your program uses python multiprocess (possible params -M or -C, default: -C);
- @ALLOWED_VERSIONS: What python versions your program can be run: from 3.6 to 3.13;

## Results

> Last run: Sat Aug  9 17:04:13 UTC 2025
### **Comparison**

#### How much faster 3.13 is? (Mean / Median vs older)
| Command | 3.12 | 3.11 | 3.10 | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | -2.12% / -1.71% | -13.80% / -14.18% | -51.79% / -51.36% | -44.96% / -44.66% | -48.78% / -49.02% | 16.88% / 16.13% | -44.09% / -44.16% |
| `algorithm/search/hashmap_lookup.py` | -3.26% / -2.03% | -15.42% / -15.03% | -52.49% / -52.16% | -45.33% / -44.18% | -49.43% / -49.63% | 13.64% / 14.87% | -42.95% / -42.51% |
| `algorithm/search/index.py` | -4.29% / -4.62% | -14.73% / -15.74% | -53.32% / -53.38% | -46.58% / -47.22% | -50.55% / -50.93% | 13.42% / 12.83% | -44.65% / -45.11% |
| `algorithm/search/linear.py` | -2.09% / -2.24% | -15.71% / -15.66% | -53.23% / -54.18% | -46.11% / -47.27% | -49.84% / -49.78% | 11.11% / 11.25% | -44.37% / -43.95% |
| `algorithm/sorting/naive_bubble_sort.py` | -7.72% / -5.90% | -35.18% / -31.46% | -32.22% / -31.02% | -22.30% / -19.12% | -22.71% / -20.79% | 43.15% / 47.46% | -32.95% / -31.12% |
| `algorithm/twosum/twosum.py` | 52.26% / 56.59% | 25.40% / 34.74% | -40.07% / -38.23% | -34.68% / -32.62% | -43.55% / -41.59% | 2.07% / 2.05% | -37.28% / -35.38% |
| `algorithm/twosum/twosum_naive.py` | 41.38% / 57.05% | 20.79% / 37.95% | -41.45% / -37.31% | -36.92% / -31.59% | -46.23% / -41.52% | 2.88% / 3.71% | -39.35% / -34.55% |
| `complex/classes/classes.py` | -4.73% / -0.57% | -23.81% / -16.71% | -64.84% / -63.34% | -61.89% / -60.10% | -65.48% / -63.85% | 53.54% / 64.24% | -61.93% / -60.09% |
| `complex/classes/dataclasses_.py` | -0.27% / -1.05% | -19.63% / -17.07% | -65.69% / -65.20% | -62.12% / -61.60% | -69.62% / -69.12% | -19.19% / -16.06% | -- / -- |
| `complex/classes/namedtuple_classes.py` | 31.53% / 36.07% | 6.44% / 4.72% | -57.63% / -57.68% | -52.79% / -52.50% | -60.05% / -59.91% | 23.39% / 19.31% | -54.69% / -54.67% |
| `complex/classes/simplenamespace.py` | 1.92% / 1.09% | -23.69% / -17.49% | -64.12% / -63.06% | -59.96% / -58.54% | -64.56% / -64.06% | 41.50% / 52.81% | -48.53% / -46.39% |
| `complex/classes/sloted_classes.py` | 3.57% / 3.01% | -16.70% / -10.81% | -62.40% / -62.03% | -58.13% / -57.97% | -61.78% / -62.25% | 62.20% / 72.99% | -58.47% / -58.19% |
| `complex/generators/readlines.py` | -6.00% / -7.17% | -33.44% / -28.48% | -15.38% / 13.08% | -9.08% / 18.49% | -19.02% / 6.92% | 52.81% / 133.86% | -6.75% / 24.61% |
| `complex/generators/simple.py` | -3.85% / -2.52% | -20.65% / -14.58% | -37.94% / -37.99% | -31.74% / -34.04% | -35.91% / -37.40% | 26.46% / 27.40% | -30.55% / -30.32% |
| `dummy/dummy.py` | -18.79% / -6.01% | -36.28% / -27.83% | -21.49% / 9.33% | -15.53% / 17.23% | -19.59% / 11.15% | 53.02% / 147.87% | -21.49% / 9.33% |
| `long_run/database/postgresql.py` | -4.07% / -3.20% | -11.93% / -10.19% | -57.23% / -56.44% | -53.51% / -52.76% | -58.42% / -57.80% | -23.10% / -21.11% | -57.97% / -57.50% |
| `long_run/database/sqlite_.py` | -0.31% / -0.37% | -7.47% / -7.81% | -55.86% / -56.05% | -53.32% / -53.18% | -56.85% / -57.04% | -24.12% / -23.81% | -56.16% / -56.13% |
| `long_run/file/load_titanic_csv_pandas.py` | -8.31% / -8.56% | -17.28% / -17.47% | -60.01% / -60.28% | -56.97% / -57.22% | -60.34% / -60.50% | -29.06% / -27.93% | -57.75% / -57.75% |
| `long_run/file/load_titanic_csv_python.py` | -9.36% / -19.83% | -22.51% / -29.72% | -57.95% / -60.08% | -52.79% / -55.31% | -58.50% / -60.90% | -21.13% / -28.40% | -56.05% / -58.62% |
| `long_run/processes/collect_names_from_site.py` | -4.73% / -4.81% | -11.17% / -11.76% | -8.04% / -11.32% | 1.08% / 2.27% | -22.42% / -22.90% | -- / -- | -- / -- |
| `long_run/processes/generate_fake_data.py` | -2.53% / -3.47% | -12.53% / -13.83% | -60.42% / -60.34% | -58.34% / -58.70% | -61.58% / -61.83% | -10.55% / -10.68% | -60.32% / -60.56% |
| `long_run/processes/maze_generator.py` | -11.10% / -14.66% | -23.14% / -24.96% | -42.70% / -46.31% | -21.87% / -23.84% | -26.59% / -28.73% | 61.65% / 59.49% | -24.16% / -25.41% |
| `long_run/text/clean_text.py` | -2.40% / -2.26% | -9.73% / -7.32% | -52.26% / -52.58% | -48.65% / -48.41% | -52.14% / -52.12% | -14.05% / -14.57% | -51.49% / -51.34% |
| `long_run/text/count_words.py` | -8.43% / -6.31% | -22.14% / -29.63% | -54.45% / -55.89% | -49.96% / -51.18% | -55.29% / -56.76% | -16.42% / -13.45% | -54.11% / -55.44% |
| `math/haversine.py` | 1.75% / 2.28% | -15.42% / -17.00% | -44.81% / -45.02% | -33.23% / -33.55% | -45.43% / -45.77% | 26.87% / 26.03% | -39.72% / -39.97% |
| `math/mandelbrot.py` | -10.40% / -11.41% | -2.90% / -3.85% | -48.81% / -49.26% | -48.60% / -49.05% | -41.06% / -40.99% | 11.00% / 11.44% | -38.44% / -38.17% |
| `math/pow_simple.py` | -15.30% / -15.29% | -25.60% / -25.80% | -48.55% / -48.61% | -45.65% / -45.67% | -41.72% / -41.87% | 5.14% / 5.16% | -45.40% / -45.28% |
| `math/pow_using_math.py` | -5.94% / -6.39% | -19.46% / -18.97% | -50.72% / -50.47% | -47.73% / -47.72% | -48.55% / -49.20% | 31.11% / 30.90% | -39.61% / -39.70% |
| `modules/enum/enum_lookup.py` | 1.01% / 1.26% | -3.86% / -3.04% | -- / -- | -- / -- | -- / -- | 36.78% / 34.05% | -- / -- |
| `modules/json/json_module.py` | 1.13% / 1.37% | -10.90% / -8.46% | -51.69% / -51.23% | -43.37% / -42.08% | -48.76% / -48.04% | 30.50% / 33.91% | -42.78% / -42.48% |
| `modules/json/orjson_module.py` | 4.25% / 2.83% | -12.17% / -13.69% | -51.94% / -52.40% | -47.56% / -48.11% | -55.34% / -55.43% | -15.60% / -15.93% | -52.09% / -51.63% |
| `programming_game_benchmark/nbody.py` | -11.68% / -13.73% | -21.01% / -21.27% | -25.99% / -26.07% | -18.58% / -19.26% | -24.66% / -24.99% | 43.44% / 40.49% | -33.91% / -34.13% |
| `programming_game_benchmark/spectral_norm.py` | -2.56% / -3.80% | -20.23% / -20.17% | -80.01% / -79.97% | -77.20% / -77.43% | -78.03% / -78.20% | -0.92% / 0.14% | -75.76% / -74.93% |
---

#### How much more memory 3.13 uses? (vs older)
| Command | 3.12 | 3.11 | 3.10 | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 1.77% | 1.86% | 15.49% | 24.39% | 27.33% | 23.61% | 30.20% |
| `algorithm/search/hashmap_lookup.py` | 2.04% | 3.88% | 16.78% | 25.05% | 29.99% | 26.71% | 39.49% |
| `algorithm/search/index.py` | 2.52% | 1.93% | 15.41% | 23.75% | 27.58% | 21.37% | 31.55% |
| `algorithm/search/linear.py` | 2.93% | 4.75% | 13.41% | 20.86% | 27.17% | 24.67% | 31.15% |
| `algorithm/sorting/naive_bubble_sort.py` | 2.29% | 6.02% | 19.84% | 25.04% | 31.42% | 29.98% | 35.08% |
| `algorithm/twosum/twosum.py` | 5.33% | 8.12% | 24.39% | 26.50% | 33.18% | 38.04% | 31.43% |
| `algorithm/twosum/twosum_naive.py` | 3.38% | 5.56% | 21.95% | 22.69% | 32.15% | 36.79% | 30.67% |
| `complex/classes/classes.py` | 5.81% | 7.02% | 19.44% | 31.03% | 37.17% | 37.55% | 37.82% |
| `complex/classes/dataclasses_.py` | 5.44% | 5.39% | 18.63% | 27.32% | 37.29% | 34.79% | -- |
| `complex/classes/namedtuple_classes.py` | 2.58% | 4.94% | 18.99% | 26.92% | 35.65% | 32.23% | 33.29% |
| `complex/classes/simplenamespace.py` | 4.34% | 5.31% | 17.57% | 29.48% | 39.36% | 39.39% | 35.99% |
| `complex/classes/sloted_classes.py` | 5.70% | 6.63% | 17.55% | 26.90% | 39.90% | 37.44% | 39.96% |
| `complex/generators/readlines.py` | 3.45% | 6.01% | 23.16% | 23.86% | 32.67% | 36.65% | 35.21% |
| `complex/generators/simple.py` | 3.55% | 5.06% | 19.69% | 30.09% | 39.52% | 42.67% | 39.63% |
| `dummy/dummy.py` | 2.84% | 7.17% | 19.97% | 26.56% | 33.43% | 36.03% | 33.90% |
| `long_run/database/postgresql.py` | 3.48% | 4.98% | 18.36% | 19.81% | 26.54% | 28.09% | 27.12% |
| `long_run/database/sqlite_.py` | -4.26% | -2.74% | 3.50% | 2.58% | 4.13% | 3.56% | 9.20% |
| `long_run/file/load_titanic_csv_pandas.py` | 0.47% | -0.11% | 17.52% | 15.33% | 17.76% | 17.05% | 22.70% |
| `long_run/file/load_titanic_csv_python.py` | 2.63% | 5.25% | 20.63% | 22.83% | 32.72% | 36.51% | 32.98% |
| `long_run/processes/collect_names_from_site.py` | 2.67% | 4.01% | 10.89% | 10.39% | 11.37% | -- | -- |
| `long_run/processes/generate_fake_data.py` | -6.76% | -7.40% | -1.23% | -2.65% | 2.24% | -2.75% | 5.65% |
| `long_run/processes/maze_generator.py` | 3.69% | 5.06% | 18.15% | 24.13% | 31.77% | 32.04% | 33.80% |
| `long_run/text/clean_text.py` | 5.45% | 8.68% | 24.31% | 26.43% | 32.73% | 35.60% | 31.03% |
| `long_run/text/count_words.py` | 3.45% | 5.60% | 23.09% | 23.77% | 33.67% | 35.58% | 34.45% |
| `math/haversine.py` | 3.34% | 8.11% | 19.88% | 26.65% | 31.91% | 39.01% | 33.65% |
| `math/mandelbrot.py` | 2.52% | -2.26% | 20.69% | 6.53% | 27.27% | 17.09% | 26.17% |
| `math/pow_simple.py` | 3.29% | 8.66% | 20.26% | 27.24% | 32.25% | 38.88% | 34.96% |
| `math/pow_using_math.py` | 5.20% | 6.91% | 21.03% | 26.54% | 32.59% | 35.44% | 34.13% |
| `modules/enum/enum_lookup.py` | 4.22% | 7.56% | -- | -- | -- | 29.40% | -- |
| `modules/json/json_module.py` | 4.19% | 6.44% | 24.04% | 26.65% | 32.27% | 30.67% | 35.39% |
| `modules/json/orjson_module.py` | 3.96% | 5.34% | 22.97% | 25.11% | 30.61% | 29.74% | 31.14% |
| `programming_game_benchmark/nbody.py` | 4.18% | 6.18% | 22.18% | 23.05% | 34.40% | 35.30% | 34.64% |
| `programming_game_benchmark/spectral_norm.py` | 2.16% | 6.07% | 19.43% | 22.55% | 28.61% | 28.38% | 33.45% |
---

#### How much faster 3.12 is? (Mean / Median vs older)
| Command | 3.11 | 3.10 | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | -11.94% / -12.68% | -50.75% / -50.52% | -43.76% / -43.69% | -47.68% / -48.13% | 19.41% / 18.15% | -42.88% / -43.19% |
| `algorithm/search/hashmap_lookup.py` | -12.57% / -13.26% | -50.89% / -51.16% | -43.49% / -43.02% | -47.73% / -48.59% | 17.47% / 17.26% | -41.03% / -41.32% |
| `algorithm/search/index.py` | -10.90% / -11.66% | -51.23% / -51.13% | -44.19% / -44.66% | -48.33% / -48.55% | 18.51% / 18.30% | -42.16% / -42.45% |
| `algorithm/search/linear.py` | -13.92% / -13.73% | -52.24% / -53.13% | -44.96% / -46.06% | -48.77% / -48.63% | 13.48% / 13.80% | -43.18% / -42.66% |
| `algorithm/sorting/naive_bubble_sort.py` | -29.76% / -27.17% | -26.55% / -26.70% | -15.80% / -14.04% | -16.25% / -15.83% | 55.11% / 56.70% | -27.34% / -26.80% |
| `algorithm/twosum/twosum.py` | -17.64% / -13.95% | -60.64% / -60.55% | -57.10% / -56.97% | -62.93% / -62.70% | -32.96% / -34.83% | -58.80% / -58.73% |
| `algorithm/twosum/twosum_naive.py` | -14.56% / -12.16% | -58.59% / -60.08% | -55.38% / -56.44% | -61.97% / -62.76% | -27.24% / -33.96% | -57.11% / -58.32% |
| `complex/classes/classes.py` | -20.02% / -16.23% | -63.09% / -63.13% | -60.00% / -59.87% | -63.77% / -63.65% | 61.16% / 65.18% | -60.04% / -59.86% |
| `complex/classes/dataclasses_.py` | -19.41% / -16.19% | -65.60% / -64.83% | -62.02% / -61.20% | -69.54% / -68.79% | -18.97% / -15.17% | -- / -- |
| `complex/classes/namedtuple_classes.py` | -19.08% / -23.04% | -67.79% / -68.90% | -64.11% / -65.09% | -69.63% / -70.54% | -6.19% / -12.32% | -65.55% / -66.68% |
| `complex/classes/simplenamespace.py` | -25.13% / -18.38% | -64.80% / -63.46% | -60.71% / -58.99% | -65.23% / -64.45% | 38.84% / 51.16% | -49.50% / -46.97% |
| `complex/classes/sloted_classes.py` | -19.57% / -13.42% | -63.70% / -63.14% | -59.58% / -59.20% | -63.10% / -63.35% | 56.60% / 67.93% | -59.90% / -59.41% |
| `complex/generators/readlines.py` | -29.19% / -22.96% | -9.98% / 21.81% | -3.28% / 27.63% | -13.85% / 15.17% | 62.57% / 151.91% | -0.80% / 34.23% |
| `complex/generators/simple.py` | -17.47% / -12.37% | -35.46% / -36.39% | -29.01% / -32.34% | -33.34% / -35.79% | 31.53% / 30.68% | -27.77% / -28.53% |
| `dummy/dummy.py` | -21.53% / -23.21% | -3.32% / 16.32% | 4.02% / 24.73% | -0.98% / 18.25% | 88.43% / 163.71% | -3.32% / 16.32% |
| `long_run/database/postgresql.py` | -8.19% / -7.22% | -55.42% / -55.00% | -51.53% / -51.20% | -56.65% / -56.40% | -19.84% / -18.50% | -56.19% / -56.09% |
| `long_run/database/sqlite_.py` | -7.18% / -7.47% | -55.73% / -55.88% | -53.17% / -53.01% | -56.71% / -56.88% | -23.89% / -23.52% | -56.02% / -55.97% |
| `long_run/file/load_titanic_csv_pandas.py` | -9.78% / -9.75% | -56.39% / -56.57% | -53.07% / -53.22% | -56.75% / -56.80% | -22.62% / -21.18% | -53.92% / -53.79% |
| `long_run/file/load_titanic_csv_python.py` | -14.51% / -12.34% | -53.61% / -50.21% | -47.92% / -44.26% | -54.21% / -51.23% | -12.99% / -10.69% | -51.51% / -48.39% |
| `long_run/processes/collect_names_from_site.py` | -6.76% / -7.31% | -3.47% / -6.85% | 6.10% / 7.43% | -18.57% / -19.01% | -- / -- | -- / -- |
| `long_run/processes/generate_fake_data.py` | -10.26% / -10.73% | -59.39% / -58.92% | -57.26% / -57.21% | -60.59% / -60.45% | -8.23% / -7.47% | -59.29% / -59.14% |
| `long_run/processes/maze_generator.py` | -13.55% / -12.07% | -35.55% / -37.09% | -12.12% / -10.76% | -17.42% / -16.49% | 81.83% / 86.88% | -14.69% / -12.60% |
| `long_run/text/clean_text.py` | -7.51% / -5.17% | -51.08% / -51.48% | -47.39% / -47.21% | -50.97% / -51.01% | -11.94% / -12.59% | -50.30% / -50.21% |
| `long_run/text/count_words.py` | -14.97% / -24.89% | -50.26% / -52.92% | -45.36% / -47.89% | -51.17% / -53.85% | -8.72% / -7.62% | -49.89% / -52.43% |
| `math/haversine.py` | -16.87% / -18.84% | -45.76% / -46.25% | -34.38% / -35.03% | -46.37% / -46.98% | 24.69% / 23.23% | -40.75% / -41.30% |
| `math/mandelbrot.py` | 8.38% / 8.53% | -42.87% / -42.73% | -42.63% / -42.49% | -34.22% / -33.39% | 23.88% / 25.79% | -31.30% / -30.21% |
| `math/pow_simple.py` | -12.17% / -12.41% | -39.26% / -39.33% | -35.83% / -35.87% | -31.19% / -31.38% | 24.13% / 24.13% | -35.54% / -35.40% |
| `math/pow_using_math.py` | -14.37% / -13.43% | -47.61% / -47.09% | -44.43% / -44.15% | -45.30% / -45.73% | 39.39% / 39.84% | -35.79% / -35.59% |
| `modules/enum/enum_lookup.py` | -4.82% / -4.25% | -- / -- | -- / -- | -- / -- | 35.41% / 32.38% | -- / -- |
| `modules/json/json_module.py` | -11.89% / -9.69% | -52.23% / -51.89% | -44.00% / -42.86% | -49.33% / -48.74% | 29.04% / 32.10% | -43.42% / -43.26% |
| `modules/json/orjson_module.py` | -15.75% / -16.06% | -53.90% / -53.71% | -49.70% / -49.54% | -57.16% / -56.66% | -19.04% / -18.25% | -54.04% / -52.96% |
| `programming_game_benchmark/nbody.py` | -10.56% / -8.74% | -16.20% / -14.30% | -7.81% / -6.41% | -14.69% / -13.05% | 62.41% / 62.84% | -25.17% / -23.65% |
| `programming_game_benchmark/spectral_norm.py` | -18.13% / -17.02% | -79.48% / -79.18% | -76.61% / -76.53% | -77.46% / -77.34% | 1.68% / 4.09% | -75.12% / -73.95% |
---

#### How much more memory 3.12 uses? (vs older)
| Command | 3.11 | 3.10 | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 0.08% | 13.47% | 22.23% | 25.11% | 21.46% | 27.93% |
| `algorithm/search/hashmap_lookup.py` | 1.80% | 14.44% | 22.55% | 27.39% | 24.17% | 36.70% |
| `algorithm/search/index.py` | -0.57% | 12.58% | 20.70% | 24.45% | 18.39% | 28.31% |
| `algorithm/search/linear.py` | 1.77% | 10.18% | 17.42% | 23.55% | 21.12% | 27.41% |
| `algorithm/sorting/naive_bubble_sort.py` | 3.65% | 17.16% | 22.24% | 28.48% | 27.07% | 32.06% |
| `algorithm/twosum/twosum.py` | 2.65% | 18.09% | 20.10% | 26.44% | 31.05% | 24.78% |
| `algorithm/twosum/twosum_naive.py` | 2.11% | 17.96% | 18.68% | 27.83% | 32.32% | 26.40% |
| `complex/classes/classes.py` | 1.14% | 12.88% | 23.83% | 29.64% | 30.00% | 30.25% |
| `complex/classes/dataclasses_.py` | -0.05% | 12.51% | 20.75% | 30.21% | 27.84% | -- |
| `complex/classes/namedtuple_classes.py` | 2.29% | 15.99% | 23.72% | 32.23% | 28.90% | 29.93% |
| `complex/classes/simplenamespace.py` | 0.93% | 12.68% | 24.10% | 33.57% | 33.59% | 30.34% |
| `complex/classes/sloted_classes.py` | 0.88% | 11.21% | 20.06% | 32.35% | 30.02% | 32.41% |
| `complex/generators/readlines.py` | 2.48% | 19.05% | 19.73% | 28.25% | 32.10% | 30.70% |
| `complex/generators/simple.py` | 1.46% | 15.59% | 25.63% | 34.74% | 37.78% | 34.85% |
| `dummy/dummy.py` | 4.22% | 16.66% | 23.07% | 29.75% | 32.28% | 30.21% |
| `long_run/database/postgresql.py` | 1.45% | 14.38% | 15.79% | 22.29% | 23.79% | 22.84% |
| `long_run/database/sqlite_.py` | 1.59% | 8.11% | 7.14% | 8.76% | 8.17% | 14.06% |
| `long_run/file/load_titanic_csv_pandas.py` | -0.57% | 16.98% | 14.79% | 17.21% | 16.51% | 22.13% |
| `long_run/file/load_titanic_csv_python.py` | 2.55% | 17.54% | 19.68% | 29.32% | 33.01% | 29.58% |
| `long_run/processes/collect_names_from_site.py` | 1.31% | 8.01% | 7.52% | 8.48% | -- | -- |
| `long_run/processes/generate_fake_data.py` | -0.69% | 5.94% | 4.41% | 9.66% | 4.31% | 13.31% |
| `long_run/processes/maze_generator.py` | 1.32% | 13.94% | 19.71% | 27.07% | 27.34% | 29.03% |
| `long_run/text/clean_text.py` | 3.06% | 17.88% | 19.89% | 25.87% | 28.59% | 24.26% |
| `long_run/text/count_words.py` | 2.08% | 18.98% | 19.64% | 29.21% | 31.06% | 29.97% |
| `math/haversine.py` | 4.62% | 16.00% | 22.55% | 27.64% | 34.52% | 29.33% |
| `math/mandelbrot.py` | -4.66% | 17.72% | 3.91% | 24.14% | 14.21% | 23.06% |
| `math/pow_simple.py` | 5.20% | 16.44% | 23.19% | 28.04% | 34.46% | 30.66% |
| `math/pow_using_math.py` | 1.63% | 15.05% | 20.29% | 26.04% | 28.75% | 27.50% |
| `modules/enum/enum_lookup.py` | 3.20% | -- | -- | -- | 24.16% | -- |
| `modules/json/json_module.py` | 2.15% | 19.05% | 21.56% | 26.95% | 25.42% | 29.95% |
| `modules/json/orjson_module.py` | 1.33% | 18.29% | 20.34% | 25.64% | 24.80% | 26.15% |
| `programming_game_benchmark/nbody.py` | 1.91% | 17.28% | 18.11% | 29.00% | 29.87% | 29.23% |
| `programming_game_benchmark/spectral_norm.py` | 3.82% | 16.90% | 19.95% | 25.89% | 25.66% | 30.62% |
---

#### How much faster 3.11 is? (Mean / Median vs older)
| Command | 3.10 | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | -44.07% / -43.33% | -36.14% / -35.52% | -40.58% / -40.60% | 35.59% / 35.31% | -35.14% / -34.93% |
| `algorithm/search/hashmap_lookup.py` | -43.83% / -43.70% | -35.37% / -34.31% | -40.22% / -40.72% | 34.35% / 35.19% | -32.55% / -32.35% |
| `algorithm/search/index.py` | -45.26% / -44.68% | -37.36% / -37.36% | -42.01% / -41.76% | 33.02% / 33.91% | -35.09% / -34.85% |
| `algorithm/search/linear.py` | -44.51% / -45.67% | -36.06% / -37.48% | -40.49% / -40.46% | 31.83% / 31.90% | -33.99% / -33.54% |
| `algorithm/sorting/naive_bubble_sort.py` | 4.56% / 0.64% | 19.87% / 18.02% | 19.23% / 15.57% | 120.82% / 115.15% | 3.44% / 0.50% |
| `algorithm/twosum/twosum.py` | -52.21% / -54.16% | -47.91% / -49.99% | -54.99% / -56.65% | -18.60% / -24.27% | -49.98% / -52.04% |
| `algorithm/twosum/twosum_naive.py` | -51.53% / -54.56% | -47.78% / -50.41% | -55.48% / -57.61% | -14.83% / -24.82% | -49.79% / -52.55% |
| `complex/classes/classes.py` | -53.85% / -55.99% | -49.99% / -52.09% | -54.69% / -56.60% | 101.51% / 97.20% | -50.04% / -52.08% |
| `complex/classes/dataclasses_.py` | -57.31% / -58.04% | -52.87% / -53.70% | -62.20% / -62.76% | 0.55% / 1.21% | -- / -- |
| `complex/classes/namedtuple_classes.py` | -60.20% / -59.59% | -55.64% / -54.64% | -62.47% / -61.72% | 15.93% / 13.92% | -57.43% / -56.71% |
| `complex/classes/simplenamespace.py` | -52.98% / -55.23% | -47.53% / -49.75% | -53.56% / -56.44% | 85.44% / 85.21% | -32.55% / -35.03% |
| `complex/classes/sloted_classes.py` | -54.86% / -57.43% | -49.74% / -52.88% | -54.12% / -57.68% | 94.71% / 93.96% | -50.14% / -53.12% |
| `complex/generators/readlines.py` | 27.13% / 58.12% | 36.59% / 65.68% | 21.66% / 49.50% | 129.59% / 227.00% | 40.10% / 74.25% |
| `complex/generators/simple.py` | -21.79% / -27.41% | -13.98% / -22.79% | -19.22% / -26.72% | 59.38% / 49.14% | -12.47% / -18.43% |
| `dummy/dummy.py` | 23.21% / 51.48% | 32.56% / 62.43% | 26.19% / 54.00% | 140.13% / 243.43% | 23.21% / 51.48% |
| `long_run/database/postgresql.py` | -51.44% / -51.50% | -47.21% / -47.40% | -52.78% / -53.01% | -12.68% / -12.16% | -52.28% / -52.68% |
| `long_run/database/sqlite_.py` | -52.30% / -52.32% | -49.55% / -49.22% | -53.36% / -53.40% | -18.00% / -17.35% | -52.62% / -52.42% |
| `long_run/file/load_titanic_csv_pandas.py` | -51.65% / -51.87% | -47.98% / -48.16% | -52.06% / -52.13% | -14.23% / -12.67% | -48.92% / -48.80% |
| `long_run/file/load_titanic_csv_python.py` | -45.74% / -43.20% | -39.08% / -36.42% | -46.44% / -44.36% | 1.78% / 1.89% | -43.29% / -41.13% |
| `long_run/processes/collect_names_from_site.py` | 3.53% / 0.50% | 13.79% / 15.90% | -12.66% / -12.62% | -- / -- | -- / -- |
| `long_run/processes/generate_fake_data.py` | -54.75% / -53.98% | -52.37% / -52.07% | -56.08% / -55.70% | 2.26% / 3.65% | -54.63% / -54.23% |
| `long_run/processes/maze_generator.py` | -25.45% / -28.45% | 1.65% / 1.49% | -4.49% / -5.03% | 110.32% / 112.54% | -1.33% / -0.61% |
| `long_run/text/clean_text.py` | -47.11% / -48.84% | -43.12% / -44.33% | -46.98% / -48.34% | -4.78% / -7.82% | -46.27% / -47.50% |
| `long_run/text/count_words.py` | -41.50% / -37.31% | -35.74% / -30.62% | -42.57% / -38.55% | 7.34% / 22.99% | -41.07% / -36.67% |
| `math/haversine.py` | -34.75% / -33.77% | -21.06% / -19.94% | -35.48% / -34.67% | 49.99% / 51.84% | -28.73% / -27.67% |
| `math/mandelbrot.py` | -47.29% / -47.23% | -47.07% / -47.01% | -39.31% / -38.63% | 14.31% / 15.90% | -36.61% / -35.70% |
| `math/pow_simple.py` | -30.85% / -30.73% | -26.94% / -26.78% | -21.66% / -21.65% | 41.33% / 41.73% | -26.61% / -26.24% |
| `math/pow_using_math.py` | -38.82% / -38.88% | -35.10% / -35.48% | -36.12% / -37.31% | 62.79% / 61.53% | -25.01% / -25.59% |
| `modules/enum/enum_lookup.py` | -- / -- | -- / -- | -- / -- | 42.27% / 38.25% | -- / -- |
| `modules/json/json_module.py` | -45.78% / -46.73% | -36.44% / -36.72% | -42.49% / -43.24% | 46.46% / 46.29% | -35.78% / -37.17% |
| `modules/json/orjson_module.py` | -45.28% / -44.85% | -40.30% / -39.88% | -49.15% / -48.36% | -3.91% / -2.60% | -45.45% / -43.96% |
| `programming_game_benchmark/nbody.py` | -6.31% / -6.10% | 3.07% / 2.55% | -4.61% / -4.72% | 81.59% / 78.44% | -16.34% / -16.33% |
| `programming_game_benchmark/spectral_norm.py` | -74.94% / -74.91% | -71.42% / -71.72% | -72.46% / -72.69% | 24.21% / 25.44% | -69.61% / -68.60% |
---

#### How much more memory 3.11 uses? (vs older)
| Command | 3.10 | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 13.38% | 22.13% | 25.01% | 21.36% | 27.82% |
| `algorithm/search/hashmap_lookup.py` | 12.42% | 20.39% | 25.14% | 21.98% | 34.28% |
| `algorithm/search/index.py` | 13.23% | 21.40% | 25.16% | 19.07% | 29.05% |
| `algorithm/search/linear.py` | 8.26% | 15.38% | 21.40% | 19.02% | 25.20% |
| `algorithm/sorting/naive_bubble_sort.py` | 13.04% | 17.94% | 23.96% | 22.60% | 27.42% |
| `algorithm/twosum/twosum.py` | 15.04% | 17.00% | 23.18% | 27.67% | 21.55% |
| `algorithm/twosum/twosum_naive.py` | 15.52% | 16.23% | 25.18% | 29.58% | 23.79% |
| `complex/classes/classes.py` | 11.61% | 22.44% | 28.17% | 28.53% | 28.78% |
| `complex/classes/dataclasses_.py` | 12.56% | 20.81% | 30.27% | 27.90% | -- |
| `complex/classes/namedtuple_classes.py` | 13.39% | 20.95% | 29.26% | 26.01% | 27.02% |
| `complex/classes/simplenamespace.py` | 11.64% | 22.95% | 32.33% | 32.36% | 29.13% |
| `complex/classes/sloted_classes.py` | 10.24% | 19.02% | 31.21% | 28.90% | 31.26% |
| `complex/generators/readlines.py` | 16.17% | 16.84% | 25.15% | 28.90% | 27.54% |
| `complex/generators/simple.py` | 13.92% | 23.82% | 32.80% | 35.79% | 32.90% |
| `dummy/dummy.py` | 11.94% | 18.09% | 24.50% | 26.93% | 24.94% |
| `long_run/database/postgresql.py` | 12.75% | 14.13% | 20.54% | 22.02% | 21.09% |
| `long_run/database/sqlite_.py` | 6.42% | 5.47% | 7.06% | 6.48% | 12.28% |
| `long_run/file/load_titanic_csv_pandas.py` | 17.65% | 15.45% | 17.89% | 17.18% | 22.83% |
| `long_run/file/load_titanic_csv_python.py` | 14.62% | 16.71% | 26.10% | 29.71% | 26.36% |
| `long_run/processes/collect_names_from_site.py` | 6.62% | 6.14% | 7.08% | -- | -- |
| `long_run/processes/generate_fake_data.py` | 6.67% | 5.13% | 10.41% | 5.03% | 14.10% |
| `long_run/processes/maze_generator.py` | 12.46% | 18.15% | 25.42% | 25.68% | 27.35% |
| `long_run/text/clean_text.py` | 14.38% | 16.33% | 22.13% | 24.77% | 20.57% |
| `long_run/text/count_words.py` | 16.56% | 17.21% | 26.58% | 28.39% | 27.32% |
| `math/haversine.py` | 10.88% | 17.15% | 22.01% | 28.58% | 23.62% |
| `math/mandelbrot.py` | 23.47% | 8.99% | 30.21% | 19.80% | 29.08% |
| `math/pow_simple.py` | 10.68% | 17.11% | 21.72% | 27.82% | 24.21% |
| `math/pow_using_math.py` | 13.21% | 18.36% | 24.02% | 26.69% | 25.46% |
| `modules/enum/enum_lookup.py` | -- | -- | -- | 20.31% | -- |
| `modules/json/json_module.py` | 16.54% | 18.99% | 24.27% | 22.77% | 27.21% |
| `modules/json/orjson_module.py` | 16.74% | 18.76% | 23.99% | 23.16% | 24.49% |
| `programming_game_benchmark/nbody.py` | 15.08% | 15.89% | 26.58% | 27.44% | 26.81% |
| `programming_game_benchmark/spectral_norm.py` | 12.59% | 15.54% | 21.25% | 21.03% | 25.81% |
---

#### How much faster 3.10 is? (Mean / Median vs older)
| Command | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 14.18% / 13.79% | 6.23% / 4.82% | 142.44% / 138.78% | 15.96% / 14.82% |
| `algorithm/search/hashmap_lookup.py` | 15.07% / 16.67% | 6.44% / 5.28% | 139.19% / 140.10% | 20.08% / 20.15% |
| `algorithm/search/index.py` | 14.44% / 13.22% | 5.95% / 5.27% | 143.00% / 142.05% | 18.59% / 17.76% |
| `algorithm/search/linear.py` | 15.23% / 15.08% | 7.25% / 9.59% | 137.59% / 142.79% | 18.96% / 22.32% |
| `algorithm/sorting/naive_bubble_sort.py` | 14.63% / 17.26% | 14.03% / 14.83% | 111.18% / 113.77% | -1.07% / -0.14% |
| `algorithm/twosum/twosum.py` | 8.99% / 9.08% | -5.82% / -5.44% | 70.32% / 65.20% | 4.66% / 4.61% |
| `algorithm/twosum/twosum_naive.py` | 7.74% / 9.12% | -8.16% / -6.72% | 75.72% / 65.44% | 3.59% / 4.41% |
| `complex/classes/classes.py` | 8.37% / 8.85% | -1.83% / -1.40% | 336.64% / 348.05% | 8.26% / 8.88% |
| `complex/classes/dataclasses_.py` | 10.41% / 10.34% | -11.46% / -11.24% | 135.54% / 141.23% | -- / -- |
| `complex/classes/namedtuple_classes.py` | 11.44% / 12.25% | -5.71% / -5.26% | 191.26% / 181.94% | 6.95% / 7.14% |
| `complex/classes/simplenamespace.py` | 11.61% / 12.23% | -1.23% / -2.71% | 294.40% / 313.66% | 43.46% / 45.11% |
| `complex/classes/sloted_classes.py` | 11.35% / 10.70% | 1.65% / -0.57% | 331.39% / 355.64% | 10.46% / 10.13% |
| `complex/generators/readlines.py` | 7.44% / 4.78% | -4.31% / -5.45% | 80.59% / 106.81% | 10.20% / 10.20% |
| `complex/generators/simple.py` | 9.99% / 6.37% | 3.28% / 0.95% | 103.79% / 105.46% | 11.91% / 12.37% |
| `dummy/dummy.py` | 7.59% / 7.23% | 2.42% / 1.66% | 94.90% / 126.72% | 0.00% / 0.00% |
| `long_run/database/postgresql.py` | 8.71% / 8.46% | -2.77% / -3.11% | 79.80% / 81.11% | -1.74% / -2.43% |
| `long_run/database/sqlite_.py` | 5.77% / 6.51% | -2.23% / -2.25% | 71.91% / 73.35% | -0.67% / -0.20% |
| `long_run/file/load_titanic_csv_pandas.py` | 7.61% / 7.72% | -0.83% / -0.54% | 77.41% / 81.47% | 5.65% / 6.39% |
| `long_run/file/load_titanic_csv_python.py` | 12.28% / 11.95% | -1.29% / -2.04% | 87.58% / 79.39% | 4.52% / 3.66% |
| `long_run/processes/collect_names_from_site.py` | 9.92% / 15.33% | -15.64% / -13.06% | -- / -- | -- / -- |
| `long_run/processes/generate_fake_data.py` | 5.25% / 4.15% | -2.94% / -3.74% | 126.00% / 125.23% | 0.26% / -0.55% |
| `long_run/processes/maze_generator.py` | 36.35% / 41.85% | 28.12% / 32.75% | 182.12% / 197.07% | 32.36% / 38.93% |
| `long_run/text/clean_text.py` | 7.55% / 8.80% | 0.24% / 0.97% | 80.02% / 80.17% | 1.59% / 2.63% |
| `long_run/text/count_words.py` | 9.85% / 10.68% | -1.84% / -1.98% | 83.49% / 96.19% | 0.74% / 1.02% |
| `math/haversine.py` | 20.99% / 20.88% | -1.12% / -1.36% | 129.88% / 129.25% | 9.23% / 9.20% |
| `math/mandelbrot.py` | 0.42% / 0.41% | 15.14% / 16.30% | 116.85% / 119.63% | 20.26% / 21.85% |
| `math/pow_simple.py` | 5.65% / 5.71% | 13.29% / 13.11% | 104.37% / 104.61% | 6.13% / 6.48% |
| `math/pow_using_math.py` | 6.06% / 5.56% | 4.41% / 2.56% | 166.06% / 164.28% | 22.56% / 21.74% |
| `modules/enum/enum_lookup.py` | -- / -- | -- / -- | -- / -- | -- / -- |
| `modules/json/json_module.py` | 17.23% / 18.78% | 6.07% / 6.55% | 170.13% / 174.60% | 18.44% / 17.94% |
| `modules/json/orjson_module.py` | 9.11% / 9.01% | -7.08% / -6.37% | 75.62% / 76.61% | -0.30% / 1.62% |
| `programming_game_benchmark/nbody.py` | 10.01% / 9.21% | 1.81% / 1.46% | 93.82% / 90.02% | -10.70% / -10.90% |
| `programming_game_benchmark/spectral_norm.py` | 14.02% / 12.72% | 9.88% / 8.85% | 395.60% / 400.03% | 21.27% / 25.16% |
---

#### How much more memory 3.10 uses? (vs older)
| Command | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 7.71% | 10.26% | 7.04% | 12.74% |
| `algorithm/search/hashmap_lookup.py` | 7.09% | 11.31% | 8.50% | 19.45% |
| `algorithm/search/index.py` | 7.22% | 10.54% | 5.16% | 13.98% |
| `algorithm/search/linear.py` | 6.57% | 12.14% | 9.93% | 15.64% |
| `algorithm/sorting/naive_bubble_sort.py` | 4.34% | 9.66% | 8.46% | 12.72% |
| `algorithm/twosum/twosum.py` | 1.70% | 7.07% | 10.97% | 5.66% |
| `algorithm/twosum/twosum_naive.py` | 0.61% | 8.37% | 12.17% | 7.16% |
| `complex/classes/classes.py` | 9.70% | 14.84% | 15.16% | 15.39% |
| `complex/classes/dataclasses_.py` | 7.33% | 15.73% | 13.62% | -- |
| `complex/classes/namedtuple_classes.py` | 6.67% | 14.00% | 11.13% | 12.02% |
| `complex/classes/simplenamespace.py` | 10.13% | 18.53% | 18.56% | 15.66% |
| `complex/classes/sloted_classes.py` | 7.96% | 19.01% | 16.92% | 19.07% |
| `complex/generators/readlines.py` | 0.57% | 7.72% | 10.95% | 9.79% |
| `complex/generators/simple.py` | 8.69% | 16.57% | 19.19% | 16.66% |
| `dummy/dummy.py` | 5.49% | 11.22% | 13.39% | 11.62% |
| `long_run/database/postgresql.py` | 1.23% | 6.91% | 8.22% | 7.40% |
| `long_run/database/sqlite_.py` | -0.90% | 0.60% | 0.06% | 5.51% |
| `long_run/file/load_titanic_csv_pandas.py` | -1.87% | 0.20% | -0.40% | 4.41% |
| `long_run/file/load_titanic_csv_python.py` | 1.82% | 10.02% | 13.16% | 10.24% |
| `long_run/processes/collect_names_from_site.py` | -0.45% | 0.43% | -- | -- |
| `long_run/processes/generate_fake_data.py` | -1.44% | 3.51% | -1.54% | 6.96% |
| `long_run/processes/maze_generator.py` | 5.06% | 11.53% | 11.76% | 13.25% |
| `long_run/text/clean_text.py` | 1.71% | 6.78% | 9.08% | 5.41% |
| `long_run/text/count_words.py` | 0.56% | 8.60% | 10.15% | 9.24% |
| `math/haversine.py` | 5.65% | 10.03% | 15.96% | 11.49% |
| `math/mandelbrot.py` | -11.73% | 5.46% | -2.98% | 4.54% |
| `math/pow_simple.py` | 5.80% | 9.97% | 15.48% | 12.22% |
| `math/pow_using_math.py` | 4.55% | 9.56% | 11.91% | 10.82% |
| `modules/enum/enum_lookup.py` | -- | -- | -- | -- |
| `modules/json/json_module.py` | 2.10% | 6.64% | 5.35% | 9.15% |
| `modules/json/orjson_module.py` | 1.74% | 6.21% | 5.51% | 6.64% |
| `programming_game_benchmark/nbody.py` | 0.71% | 9.99% | 10.74% | 10.19% |
| `programming_game_benchmark/spectral_norm.py` | 2.61% | 7.69% | 7.50% | 11.74% |
---

#### How much faster 3.9 is? (Mean / Median vs older)
| Command | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|
| `algorithm/search/bin.py` | -6.95% / -7.88% | 112.34% / 109.84% | 1.57% / 0.90% |
| `algorithm/search/hashmap_lookup.py` | -7.50% / -9.77% | 107.87% / 105.79% | 4.36% / 2.98% |
| `algorithm/search/index.py` | -7.42% / -7.02% | 112.34% / 113.78% | 3.62% / 4.01% |
| `algorithm/search/linear.py` | -6.92% / -4.76% | 106.18% / 110.98% | 3.24% / 6.30% |
| `algorithm/sorting/naive_bubble_sort.py` | -0.53% / -2.07% | 84.22% / 82.30% | -13.70% / -14.84% |
| `algorithm/twosum/twosum.py` | -13.59% / -13.31% | 56.26% / 51.45% | -3.98% / -4.10% |
| `algorithm/twosum/twosum_naive.py` | -14.76% / -14.52% | 63.09% / 51.61% | -3.86% / -4.32% |
| `complex/classes/classes.py` | -9.41% / -9.42% | 302.93% / 311.61% | -0.10% / 0.02% |
| `complex/classes/dataclasses_.py` | -19.81% / -19.56% | 113.33% / 118.61% | -- / -- |
| `complex/classes/namedtuple_classes.py` | -15.39% / -15.60% | 161.35% / 151.18% | -4.04% / -4.56% |
| `complex/classes/simplenamespace.py` | -11.50% / -13.31% | 253.39% / 268.59% | 28.54% / 29.30% |
| `complex/classes/sloted_classes.py` | -8.72% / -10.18% | 287.41% / 311.60% | -0.80% / -0.52% |
| `complex/generators/readlines.py` | -10.93% / -9.77% | 68.08% / 97.37% | 2.56% / 5.17% |
| `complex/generators/simple.py` | -6.10% / -5.10% | 85.27% / 93.15% | 1.75% / 5.64% |
| `dummy/dummy.py` | -4.81% / -5.19% | 81.15% / 111.43% | -7.06% / -6.74% |
| `long_run/database/postgresql.py` | -10.56% / -10.66% | 65.40% / 66.99% | -9.61% / -10.04% |
| `long_run/database/sqlite_.py` | -7.56% / -8.23% | 62.53% / 62.75% | -6.09% / -6.30% |
| `long_run/file/load_titanic_csv_pandas.py` | -7.84% / -7.66% | 64.87% / 68.47% | -1.82% / -1.23% |
| `long_run/file/load_titanic_csv_python.py` | -12.08% / -12.49% | 67.07% / 60.24% | -6.91% / -7.41% |
| `long_run/processes/collect_names_from_site.py` | -23.25% / -24.61% | -- / -- | -- / -- |
| `long_run/processes/generate_fake_data.py` | -7.78% / -7.57% | 114.72% / 116.26% | -4.74% / -4.51% |
| `long_run/processes/maze_generator.py` | -6.03% / -6.42% | 106.91% / 109.43% | -2.93% / -2.06% |
| `long_run/text/clean_text.py` | -6.80% / -7.20% | 67.39% / 65.59% | -5.53% / -5.68% |
| `long_run/text/count_words.py` | -10.64% / -11.44% | 67.04% / 77.26% | -8.29% / -8.73% |
| `math/haversine.py` | -18.27% / -18.39% | 90.01% / 89.65% | -9.72% / -9.66% |
| `math/mandelbrot.py` | 14.66% / 15.83% | 115.95% / 118.74% | 19.76% / 21.36% |
| `math/pow_simple.py` | 7.23% / 7.01% | 93.44% / 93.57% | 0.46% / 0.73% |
| `math/pow_using_math.py` | -1.56% / -2.84% | 150.85% / 150.37% | 15.55% / 15.33% |
| `modules/enum/enum_lookup.py` | -- / -- | -- / -- | -- / -- |
| `modules/json/json_module.py` | -9.52% / -10.30% | 130.42% / 131.18% | 1.03% / -0.70% |
| `modules/json/orjson_module.py` | -14.83% / -14.11% | 60.95% / 62.01% | -8.63% / -6.78% |
| `programming_game_benchmark/nbody.py` | -7.46% / -7.09% | 76.18% / 74.00% | -18.83% / -18.41% |
| `programming_game_benchmark/spectral_norm.py` | -3.63% / -3.44% | 334.65% / 343.59% | 6.35% / 11.03% |
---

#### How much more memory 3.9 uses? (vs older)
| Command | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|
| `algorithm/search/bin.py` | 2.36% | -0.63% | 4.67% |
| `algorithm/search/hashmap_lookup.py` | 3.95% | 1.32% | 11.54% |
| `algorithm/search/index.py` | 3.10% | -1.92% | 6.30% |
| `algorithm/search/linear.py` | 5.22% | 3.15% | 8.51% |
| `algorithm/sorting/naive_bubble_sort.py` | 5.10% | 3.95% | 8.03% |
| `algorithm/twosum/twosum.py` | 5.28% | 9.12% | 3.89% |
| `algorithm/twosum/twosum_naive.py` | 7.71% | 11.49% | 6.51% |
| `complex/classes/classes.py` | 4.68% | 4.98% | 5.18% |
| `complex/classes/dataclasses_.py` | 7.83% | 5.86% | -- |
| `complex/classes/namedtuple_classes.py` | 6.88% | 4.19% | 5.02% |
| `complex/classes/simplenamespace.py` | 7.63% | 7.65% | 5.03% |
| `complex/classes/sloted_classes.py` | 10.24% | 8.30% | 10.29% |
| `complex/generators/readlines.py` | 7.12% | 10.33% | 9.17% |
| `complex/generators/simple.py` | 7.25% | 9.66% | 7.33% |
| `dummy/dummy.py` | 5.43% | 7.49% | 5.81% |
| `long_run/database/postgresql.py` | 5.62% | 6.91% | 6.10% |
| `long_run/database/sqlite_.py` | 1.51% | 0.96% | 6.46% |
| `long_run/file/load_titanic_csv_pandas.py` | 2.11% | 1.49% | 6.39% |
| `long_run/file/load_titanic_csv_python.py` | 8.05% | 11.14% | 8.27% |
| `long_run/processes/collect_names_from_site.py` | 0.89% | -- | -- |
| `long_run/processes/generate_fake_data.py` | 5.02% | -0.10% | 8.53% |
| `long_run/processes/maze_generator.py` | 6.15% | 6.37% | 7.79% |
| `long_run/text/clean_text.py` | 4.99% | 7.25% | 3.64% |
| `long_run/text/count_words.py` | 8.00% | 9.54% | 8.63% |
| `math/haversine.py` | 4.15% | 9.76% | 5.53% |
| `math/mandelbrot.py` | 19.47% | 9.91% | 18.43% |
| `math/pow_simple.py` | 3.94% | 9.15% | 6.06% |
| `math/pow_using_math.py` | 4.79% | 7.04% | 6.00% |
| `modules/enum/enum_lookup.py` | -- | -- | -- |
| `modules/json/json_module.py` | 4.44% | 3.18% | 6.90% |
| `modules/json/orjson_module.py` | 4.40% | 3.71% | 4.82% |
| `programming_game_benchmark/nbody.py` | 9.22% | 9.96% | 9.42% |
| `programming_game_benchmark/spectral_norm.py` | 4.94% | 4.76% | 8.89% |
---

#### How much faster 3.8 is? (Mean / Median vs older)
| Command | 3.7 | 3.6 |
|:---|---:|---:|
| `algorithm/search/bin.py` | 128.21% / 127.79% | 9.16% / 9.53% |
| `algorithm/search/hashmap_lookup.py` | 124.73% / 128.07% | 12.82% / 14.13% |
| `algorithm/search/index.py` | 129.36% / 129.92% | 11.93% / 11.86% |
| `algorithm/search/linear.py` | 121.52% / 121.54% | 10.92% / 11.62% |
| `algorithm/sorting/naive_bubble_sort.py` | 85.20% / 86.17% | -13.24% / -13.04% |
| `algorithm/twosum/twosum.py` | 80.83% / 74.71% | 11.12% / 10.63% |
| `algorithm/twosum/twosum_naive.py` | 91.32% / 77.36% | 12.78% / 11.93% |
| `complex/classes/classes.py` | 344.79% / 354.40% | 10.28% / 10.42% |
| `complex/classes/dataclasses_.py` | 166.04% / 171.78% | -- / -- |
| `complex/classes/namedtuple_classes.py` | 208.90% / 197.60% | 13.42% / 13.08% |
| `complex/classes/simplenamespace.py` | 299.30% / 325.18% | 45.24% / 49.15% |
| `complex/classes/sloted_classes.py` | 324.40% / 358.27% | 8.67% / 10.76% |
| `complex/generators/readlines.py` | 88.72% / 118.73% | 15.16% / 16.55% |
| `complex/generators/simple.py` | 97.31% / 103.52% | 8.36% / 11.31% |
| `dummy/dummy.py` | 90.29% / 123.01% | -2.36% / -1.64% |
| `long_run/database/postgresql.py` | 84.93% / 86.92% | 1.07% / 0.70% |
| `long_run/database/sqlite_.py` | 75.83% / 77.34% | 1.59% / 2.10% |
| `long_run/file/load_titanic_csv_pandas.py` | 78.89% / 82.45% | 6.54% / 6.96% |
| `long_run/file/load_titanic_csv_python.py` | 90.03% / 83.11% | 5.89% / 5.81% |
| `long_run/processes/collect_names_from_site.py` | -- / -- | -- / -- |
| `long_run/processes/generate_fake_data.py` | 132.84% / 133.98% | 3.29% / 3.31% |
| `long_run/processes/maze_generator.py` | 120.19% / 123.79% | 3.31% / 4.65% |
| `long_run/text/clean_text.py` | 79.60% / 78.45% | 1.35% / 1.64% |
| `long_run/text/count_words.py` | 86.92% / 100.16% | 2.62% / 3.06% |
| `math/haversine.py` | 132.48% / 132.40% | 10.46% / 10.70% |
| `math/mandelbrot.py` | 88.33% / 88.84% | 4.44% / 4.77% |
| `math/pow_simple.py` | 80.40% / 80.89% | -6.31% / -5.86% |
| `math/pow_using_math.py` | 154.82% / 157.69% | 17.38% / 18.70% |
| `modules/enum/enum_lookup.py` | -- / -- | -- / -- |
| `modules/json/json_module.py` | 154.66% / 157.73% | 11.66% / 10.70% |
| `modules/json/orjson_module.py` | 88.99% / 88.63% | 7.29% / 8.54% |
| `programming_game_benchmark/nbody.py` | 90.38% / 87.28% | -12.29% / -12.19% |
| `programming_game_benchmark/spectral_norm.py` | 351.04% / 359.37% | 10.36% / 14.98% |
---

#### How much more memory 3.8 uses? (vs older)
| Command | 3.7 | 3.6 |
|:---|---:|---:|
| `algorithm/search/bin.py` | -2.92% | 2.25% |
| `algorithm/search/hashmap_lookup.py` | -2.52% | 7.31% |
| `algorithm/search/index.py` | -4.87% | 3.11% |
| `algorithm/search/linear.py` | -1.96% | 3.13% |
| `algorithm/sorting/naive_bubble_sort.py` | -1.09% | 2.79% |
| `algorithm/twosum/twosum.py` | 3.64% | -1.32% |
| `algorithm/twosum/twosum_naive.py` | 3.51% | -1.11% |
| `complex/classes/classes.py` | 0.28% | 0.48% |
| `complex/classes/dataclasses_.py` | -1.82% | -- |
| `complex/classes/namedtuple_classes.py` | -2.52% | -1.74% |
| `complex/classes/simplenamespace.py` | 0.02% | -2.42% |
| `complex/classes/sloted_classes.py` | -1.76% | 0.04% |
| `complex/generators/readlines.py` | 3.00% | 1.91% |
| `complex/generators/simple.py` | 2.25% | 0.08% |
| `dummy/dummy.py` | 1.95% | 0.36% |
| `long_run/database/postgresql.py` | 1.22% | 0.45% |
| `long_run/database/sqlite_.py` | -0.54% | 4.87% |
| `long_run/file/load_titanic_csv_pandas.py` | -0.60% | 4.19% |
| `long_run/file/load_titanic_csv_python.py` | 2.86% | 0.20% |
| `long_run/processes/collect_names_from_site.py` | -- | -- |
| `long_run/processes/generate_fake_data.py` | -4.88% | 3.34% |
| `long_run/processes/maze_generator.py` | 0.21% | 1.54% |
| `long_run/text/clean_text.py` | 2.16% | -1.28% |
| `long_run/text/count_words.py` | 1.43% | 0.59% |
| `math/haversine.py` | 5.38% | 1.32% |
| `math/mandelbrot.py` | -8.00% | -0.87% |
| `math/pow_simple.py` | 5.01% | 2.04% |
| `math/pow_using_math.py` | 2.15% | 1.16% |
| `modules/enum/enum_lookup.py` | -- | -- |
| `modules/json/json_module.py` | -1.21% | 2.36% |
| `modules/json/orjson_module.py` | -0.66% | 0.41% |
| `programming_game_benchmark/nbody.py` | 0.68% | 0.18% |
| `programming_game_benchmark/spectral_norm.py` | -0.18% | 3.76% |
---

#### How much faster 3.7 is? (Mean / Median vs older)
| Command | 3.6 |
|:---|---:|
| `algorithm/search/bin.py` | -52.17% / -51.91% |
| `algorithm/search/hashmap_lookup.py` | -49.80% / -49.96% |
| `algorithm/search/index.py` | -51.20% / -51.35% |
| `algorithm/search/linear.py` | -49.93% / -49.62% |
| `algorithm/sorting/naive_bubble_sort.py` | -53.16% / -53.29% |
| `algorithm/twosum/twosum.py` | -38.55% / -36.68% |
| `algorithm/twosum/twosum_naive.py` | -41.05% / -36.89% |
| `complex/classes/classes.py` | -75.21% / -75.70% |
| `complex/classes/dataclasses_.py` | -- / -- |
| `complex/classes/namedtuple_classes.py` | -63.28% / -62.00% |
| `complex/classes/simplenamespace.py` | -63.63% / -64.92% |
| `complex/classes/sloted_classes.py` | -74.39% / -75.83% |
| `complex/generators/readlines.py` | -38.98% / -46.71% |
| `complex/generators/simple.py` | -45.08% / -45.31% |
| `dummy/dummy.py` | -48.69% / -55.89% |
| `long_run/database/postgresql.py` | -45.35% / -46.13% |
| `long_run/database/sqlite_.py` | -42.22% / -42.43% |
| `long_run/file/load_titanic_csv_pandas.py` | -40.45% / -41.38% |
| `long_run/file/load_titanic_csv_python.py` | -44.28% / -42.22% |
| `long_run/processes/collect_names_from_site.py` | -- / -- |
| `long_run/processes/generate_fake_data.py` | -55.64% / -55.85% |
| `long_run/processes/maze_generator.py` | -53.08% / -53.23% |
| `long_run/text/clean_text.py` | -43.57% / -43.04% |
| `long_run/text/count_words.py` | -45.10% / -48.51% |
| `math/haversine.py` | -52.48% / -52.36% |
| `math/mandelbrot.py` | -44.54% / -44.52% |
| `math/pow_simple.py` | -48.07% / -47.96% |
| `math/pow_using_math.py` | -53.94% / -53.94% |
| `modules/enum/enum_lookup.py` | -- / -- |
| `modules/json/json_module.py` | -56.15% / -57.05% |
| `modules/json/orjson_module.py` | -43.23% / -42.46% |
| `programming_game_benchmark/nbody.py` | -53.93% / -53.11% |
| `programming_game_benchmark/spectral_norm.py` | -75.53% / -74.97% |
---

#### How much more memory 3.7 uses? (vs older)
| Command | 3.6 |
|:---|---:|
| `algorithm/search/bin.py` | 5.33% |
| `algorithm/search/hashmap_lookup.py` | 10.08% |
| `algorithm/search/index.py` | 8.38% |
| `algorithm/search/linear.py` | 5.19% |
| `algorithm/sorting/naive_bubble_sort.py` | 3.93% |
| `algorithm/twosum/twosum.py` | -4.79% |
| `algorithm/twosum/twosum_naive.py` | -4.47% |
| `complex/classes/classes.py` | 0.20% |
| `complex/classes/dataclasses_.py` | -- |
| `complex/classes/namedtuple_classes.py` | 0.80% |
| `complex/classes/simplenamespace.py` | -2.44% |
| `complex/classes/sloted_classes.py` | 1.84% |
| `complex/generators/readlines.py` | -1.05% |
| `complex/generators/simple.py` | -2.13% |
| `dummy/dummy.py` | -1.57% |
| `long_run/database/postgresql.py` | -0.76% |
| `long_run/database/sqlite_.py` | 5.44% |
| `long_run/file/load_titanic_csv_pandas.py` | 4.83% |
| `long_run/file/load_titanic_csv_python.py` | -2.58% |
| `long_run/processes/collect_names_from_site.py` | -- |
| `long_run/processes/generate_fake_data.py` | 8.63% |
| `long_run/processes/maze_generator.py` | 1.33% |
| `long_run/text/clean_text.py` | -3.37% |
| `long_run/text/count_words.py` | -0.83% |
| `math/haversine.py` | -3.86% |
| `math/mandelbrot.py` | 7.75% |
| `math/pow_simple.py` | -2.83% |
| `math/pow_using_math.py` | -0.97% |
| `modules/enum/enum_lookup.py` | -- |
| `modules/json/json_module.py` | 3.61% |
| `modules/json/orjson_module.py` | 1.08% |
| `programming_game_benchmark/nbody.py` | -0.49% |
| `programming_game_benchmark/spectral_norm.py` | 3.94% |
---

#### **Execution**

##### **Mean [s]**
| Command | 3.13 | 3.12 | 3.11 | 3.10 | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 1.70373 | 1.66764 | 1.46858 | 0.82137 | 0.9378 | 0.87258 | 1.9913 | 0.95248 |
| `algorithm/search/hashmap_lookup.py` | 1.72475 | 1.66851 | 1.45884 | 0.81942 | 0.94287 | 0.87215 | 1.95999 | 0.98399 |
| `algorithm/search/index.py` | 1.77596 | 1.69972 | 1.51439 | 0.82895 | 0.94867 | 0.87827 | 2.01438 | 0.98305 |
| `algorithm/search/linear.py` | 1.86495 | 1.82597 | 1.57188 | 0.87216 | 1.00502 | 0.93543 | 2.07217 | 1.03756 |
| `algorithm/sorting/naive_bubble_sort.py` | 2.3368 | 2.15651 | 1.51482 | 1.58395 | 1.81574 | 1.80613 | 3.34504 | 1.56694 |
| `algorithm/twosum/twosum.py` | 0.12394 | 0.18871 | 0.15542 | 0.07428 | 0.08096 | 0.06996 | 0.12651 | 0.07774 |
| `algorithm/twosum/twosum_naive.py` | 0.1286 | 0.18182 | 0.15534 | 0.07529 | 0.08112 | 0.06915 | 0.1323 | 0.07799 |
| `complex/classes/classes.py` | 0.11014 | 0.10493 | 0.08392 | 0.03873 | 0.04197 | 0.03802 | 0.16911 | 0.04193 |
| `complex/classes/dataclasses_.py` | 0.33511 | 0.3342 | 0.26932 | 0.11497 | 0.12694 | 0.10179 | 0.2708 | -- |
| `complex/classes/namedtuple_classes.py` | 0.19471 | 0.25611 | 0.20724 | 0.08249 | 0.09193 | 0.07778 | 0.24026 | 0.08822 |
| `complex/classes/simplenamespace.py` | 0.11358 | 0.11576 | 0.08667 | 0.04075 | 0.04548 | 0.04025 | 0.16072 | 0.05846 |
| `complex/classes/sloted_classes.py` | 0.10168 | 0.10531 | 0.0847 | 0.03823 | 0.04257 | 0.03886 | 0.16492 | 0.04223 |
| `complex/generators/readlines.py` | 0.03732 | 0.03508 | 0.02484 | 0.03158 | 0.03393 | 0.03022 | 0.05703 | 0.0348 |
| `complex/generators/simple.py` | 0.08982 | 0.08636 | 0.07127 | 0.05574 | 0.06131 | 0.05757 | 0.11359 | 0.06238 |
| `dummy/dummy.py` | 0.03523 | 0.02861 | 0.02245 | 0.02766 | 0.02976 | 0.02833 | 0.05391 | 0.02766 |
| `long_run/database/postgresql.py` | 0.34072 | 0.32685 | 0.30007 | 0.14572 | 0.15841 | 0.14168 | 0.26201 | 0.14319 |
| `long_run/database/sqlite_.py` | 1.30179 | 1.29778 | 1.20454 | 0.57457 | 0.60773 | 0.56177 | 0.98774 | 0.5707 |
| `long_run/file/load_titanic_csv_pandas.py` | 1.49864 | 1.37408 | 1.23963 | 0.5993 | 0.64489 | 0.59432 | 1.0632 | 0.63318 |
| `long_run/file/load_titanic_csv_python.py` | 0.15514 | 0.14062 | 0.12022 | 0.06523 | 0.07324 | 0.06439 | 0.12236 | 0.06818 |
| `long_run/processes/collect_names_from_site.py` | 2.376 | 2.2636 | 2.11055 | 2.18503 | 2.40169 | 1.84333 | -- | -- |
| `long_run/processes/generate_fake_data.py` | 1.99252 | 1.94218 | 1.74287 | 0.78863 | 0.83005 | 0.76546 | 1.78232 | 0.79067 |
| `long_run/processes/maze_generator.py` | 0.24189 | 0.21505 | 0.18592 | 0.1386 | 0.18898 | 0.17758 | 0.39102 | 0.18345 |
| `long_run/text/clean_text.py` | 0.40886 | 0.39905 | 0.36908 | 0.19521 | 0.20994 | 0.19567 | 0.35142 | 0.19832 |
| `long_run/text/count_words.py` | 0.18415 | 0.16862 | 0.14338 | 0.08388 | 0.09214 | 0.08234 | 0.15391 | 0.0845 |
| `math/haversine.py` | 0.94401 | 0.96053 | 0.79849 | 0.52099 | 0.63033 | 0.51517 | 1.19766 | 0.56907 |
| `math/mandelbrot.py` | 5.06294 | 4.53633 | 4.91635 | 2.59152 | 2.60233 | 2.98394 | 5.61969 | 3.11654 |
| `math/pow_simple.py` | 0.69494 | 0.58863 | 0.51701 | 0.35752 | 0.37772 | 0.40502 | 0.73067 | 0.37945 |
| `math/pow_using_math.py` | 1.84072 | 1.73134 | 1.48253 | 0.90708 | 0.96209 | 0.9471 | 2.41339 | 1.11168 |
| `modules/enum/enum_lookup.py` | 0.39907 | 0.4031 | 0.38366 | -- | -- | -- | 0.54585 | -- |
| `modules/json/json_module.py` | 0.6311 | 0.6382 | 0.56231 | 0.30488 | 0.35741 | 0.32339 | 0.82356 | 0.3611 |
| `modules/json/orjson_module.py` | 0.50638 | 0.52792 | 0.44476 | 0.24336 | 0.26553 | 0.22614 | 0.42738 | 0.24262 |
| `programming_game_benchmark/nbody.py` | 0.38462 | 0.33968 | 0.30381 | 0.28464 | 0.31314 | 0.28979 | 0.55169 | 0.25418 |
| `programming_game_benchmark/spectral_norm.py` | 2.48165 | 2.4181 | 1.97961 | 0.49612 | 0.5657 | 0.54514 | 2.45879 | 0.60162 |

##### **Median [s]**
| Command | 3.13 | 3.12 | 3.11 | 3.10 | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 1.70422 | 1.67508 | 1.46263 | 0.82886 | 0.94316 | 0.86883 | 1.97913 | 0.95167 |
| `algorithm/search/hashmap_lookup.py` | 1.70905 | 1.67428 | 1.45221 | 0.81766 | 0.95399 | 0.8608 | 1.96322 | 0.98245 |
| `algorithm/search/index.py` | 1.78373 | 1.70126 | 1.50292 | 0.83149 | 0.94145 | 0.87534 | 2.01259 | 0.97916 |
| `algorithm/search/linear.py` | 1.86783 | 1.82596 | 1.57534 | 0.85586 | 0.98489 | 0.93797 | 2.07794 | 1.04693 |
| `algorithm/sorting/naive_bubble_sort.py` | 2.28738 | 2.1524 | 1.56769 | 1.5778 | 1.85014 | 1.81177 | 3.37289 | 1.57552 |
| `algorithm/twosum/twosum.py` | 0.12017 | 0.18817 | 0.16192 | 0.07423 | 0.08097 | 0.07019 | 0.12263 | 0.07765 |
| `algorithm/twosum/twosum_naive.py` | 0.11871 | 0.18643 | 0.16376 | 0.07442 | 0.08121 | 0.06942 | 0.12312 | 0.0777 |
| `complex/classes/classes.py` | 0.10538 | 0.10478 | 0.08777 | 0.03863 | 0.04205 | 0.03809 | 0.17308 | 0.04206 |
| `complex/classes/dataclasses_.py` | 0.32978 | 0.32631 | 0.27349 | 0.11475 | 0.12662 | 0.10185 | 0.27681 | -- |
| `complex/classes/namedtuple_classes.py` | 0.19409 | 0.2641 | 0.20326 | 0.08213 | 0.09219 | 0.07781 | 0.23156 | 0.08799 |
| `complex/classes/simplenamespace.py` | 0.10982 | 0.11102 | 0.09061 | 0.04057 | 0.04553 | 0.03947 | 0.16782 | 0.05887 |
| `complex/classes/sloted_classes.py` | 0.10093 | 0.10397 | 0.09002 | 0.03832 | 0.04242 | 0.0381 | 0.1746 | 0.0422 |
| `complex/generators/readlines.py` | 0.02791 | 0.02591 | 0.01996 | 0.03156 | 0.03307 | 0.02984 | 0.06527 | 0.03478 |
| `complex/generators/simple.py` | 0.08986 | 0.0876 | 0.07676 | 0.05572 | 0.05927 | 0.05625 | 0.11448 | 0.06261 |
| `dummy/dummy.py` | 0.0253 | 0.02378 | 0.01826 | 0.02766 | 0.02966 | 0.02812 | 0.06271 | 0.02766 |
| `long_run/database/postgresql.py` | 0.33449 | 0.32379 | 0.30041 | 0.1457 | 0.15802 | 0.14117 | 0.26388 | 0.14216 |
| `long_run/database/sqlite_.py` | 1.3005 | 1.29569 | 1.19892 | 0.57162 | 0.60883 | 0.55875 | 0.9909 | 0.57048 |
| `long_run/file/load_titanic_csv_pandas.py` | 1.49911 | 1.37082 | 1.23715 | 0.59538 | 0.64132 | 0.59219 | 1.08043 | 0.6334 |
| `long_run/file/load_titanic_csv_python.py` | 0.16372 | 0.13126 | 0.11506 | 0.06535 | 0.07316 | 0.06402 | 0.11723 | 0.06774 |
| `long_run/processes/collect_names_from_site.py` | 2.38883 | 2.27402 | 2.10787 | 2.11836 | 2.443 | 1.84177 | -- | -- |
| `long_run/processes/generate_fake_data.py` | 1.99962 | 1.93019 | 1.72309 | 0.79296 | 0.82586 | 0.76332 | 1.78599 | 0.78858 |
| `long_run/processes/maze_generator.py` | 0.24657 | 0.21043 | 0.18503 | 0.13238 | 0.18778 | 0.17573 | 0.39326 | 0.18391 |
| `long_run/text/clean_text.py` | 0.40719 | 0.39797 | 0.3774 | 0.19308 | 0.21008 | 0.19495 | 0.34788 | 0.19815 |
| `long_run/text/count_words.py` | 0.18872 | 0.17681 | 0.1328 | 0.08325 | 0.09214 | 0.0816 | 0.16333 | 0.0841 |
| `math/haversine.py` | 0.9496 | 0.97121 | 0.7882 | 0.52205 | 0.63104 | 0.51497 | 1.19678 | 0.57009 |
| `math/mandelbrot.py` | 5.09088 | 4.51011 | 4.8949 | 2.5831 | 2.59358 | 3.00424 | 5.67325 | 3.14751 |
| `math/pow_simple.py` | 0.69318 | 0.58721 | 0.51431 | 0.35625 | 0.37658 | 0.40296 | 0.72893 | 0.37934 |
| `math/pow_using_math.py` | 1.84143 | 1.72369 | 1.49217 | 0.91204 | 0.96272 | 0.93537 | 2.41036 | 1.1103 |
| `modules/enum/enum_lookup.py` | 0.39943 | 0.40446 | 0.38728 | -- | -- | -- | 0.53542 | -- |
| `modules/json/json_module.py` | 0.62214 | 0.63065 | 0.56951 | 0.30339 | 0.36037 | 0.32325 | 0.83311 | 0.35783 |
| `modules/json/orjson_module.py` | 0.50629 | 0.52061 | 0.43699 | 0.241 | 0.26272 | 0.22564 | 0.42562 | 0.2449 |
| `programming_game_benchmark/nbody.py` | 0.38509 | 0.33223 | 0.30319 | 0.28471 | 0.31092 | 0.28887 | 0.54101 | 0.25367 |
| `programming_game_benchmark/spectral_norm.py` | 2.49363 | 2.39893 | 1.99058 | 0.49938 | 0.56292 | 0.54358 | 2.49705 | 0.62503 |

#### **Memory Usage**

##### **MEM [MB]**
| Command | 3.13 | 3.12 | 3.11 | 3.10 | 3.9 | 3.8 | 3.7 | 3.6 |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 37.59542 | 36.94029 | 36.9096 | 32.55413 | 30.22266 | 29.52511 | 30.4135 | 28.87556 |
| `algorithm/search/hashmap_lookup.py` | 39.32701 | 38.54018 | 37.85938 | 33.6769 | 31.4481 | 30.25391 | 31.03739 | 28.1942 |
| `algorithm/search/index.py` | 37.68304 | 36.75614 | 36.96819 | 32.65011 | 30.45145 | 29.53571 | 31.04743 | 28.64621 |
| `algorithm/search/linear.py` | 37.74609 | 36.67076 | 36.03348 | 33.28404 | 31.23103 | 29.68192 | 30.27623 | 28.78181 |
| `algorithm/sorting/naive_bubble_sort.py` | 28.92746 | 28.28069 | 27.28571 | 24.13783 | 23.13449 | 22.01228 | 22.25558 | 21.41462 |
| `algorithm/twosum/twosum.py` | 28.89174 | 27.42969 | 26.72098 | 23.22712 | 22.83929 | 21.69308 | 20.93025 | 21.98326 |
| `algorithm/twosum/twosum_naive.py` | 28.78125 | 27.83984 | 27.26451 | 23.60156 | 23.45815 | 21.77958 | 21.04018 | 22.02511 |
| `complex/classes/classes.py` | 30.11384 | 28.45982 | 28.13895 | 25.2115 | 22.98214 | 21.95368 | 21.89286 | 21.84989 |
| `complex/classes/dataclasses_.py` | 30.12667 | 28.57254 | 28.58594 | 25.39509 | 23.66183 | 21.9442 | 22.351 | -- |
| `complex/classes/namedtuple_classes.py` | 29.39732 | 28.65681 | 28.01395 | 24.70647 | 23.16239 | 21.67188 | 22.23158 | 22.05525 |
| `complex/classes/simplenamespace.py` | 30.65569 | 29.3817 | 29.10993 | 26.07422 | 23.67634 | 21.99721 | 21.9933 | 22.54297 |
| `complex/classes/sloted_classes.py` | 30.18359 | 28.5558 | 28.30804 | 25.67746 | 23.7846 | 21.57533 | 21.96205 | 21.56585 |
| `complex/generators/readlines.py` | 28.81306 | 27.85212 | 27.17857 | 23.39453 | 23.26228 | 21.71708 | 21.08482 | 21.30915 |
| `complex/generators/simple.py` | 30.5279 | 29.48103 | 29.05636 | 25.50502 | 23.46596 | 21.88002 | 21.39788 | 21.86272 |
| `dummy/dummy.py` | 28.7394 | 27.94699 | 26.81641 | 23.95592 | 22.70871 | 21.53906 | 21.12667 | 21.46261 |
| `long_run/database/postgresql.py` | 34.58147 | 33.41964 | 32.94141 | 29.21708 | 28.86328 | 27.32757 | 26.99777 | 27.2048 |
| `long_run/database/sqlite_.py` | 68.64063 | 71.6942 | 70.57478 | 66.31752 | 66.91741 | 65.92076 | 66.27902 | 62.85658 |
| `long_run/file/load_titanic_csv_pandas.py` | 75.41964 | 75.0692 | 75.50056 | 64.17522 | 65.39565 | 64.04408 | 64.43359 | 61.46652 |
| `long_run/file/load_titanic_csv_python.py` | 28.94196 | 28.20033 | 27.49944 | 23.99163 | 23.5625 | 21.80692 | 21.20145 | 21.76339 |
| `long_run/processes/collect_names_from_site.py` | 51.31864 | 49.98549 | 49.34152 | 46.2779 | 46.48884 | 46.07812 | -- | -- |
| `long_run/processes/generate_fake_data.py` | 67.01618 | 71.87612 | 72.37333 | 67.84821 | 68.83929 | 65.54743 | 68.90848 | 63.43136 |
| `long_run/processes/maze_generator.py` | 28.99498 | 27.96261 | 27.59821 | 24.54129 | 23.35826 | 22.00502 | 21.95926 | 21.67076 |
| `long_run/text/clean_text.py` | 28.93973 | 27.44308 | 26.62835 | 23.28069 | 22.89007 | 21.80301 | 21.34208 | 22.08594 |
| `long_run/text/count_words.py` | 28.81585 | 27.85547 | 27.28795 | 23.41127 | 23.28181 | 21.55804 | 21.25391 | 21.43192 |
| `math/haversine.py` | 28.98605 | 28.04855 | 26.81083 | 24.17913 | 22.88672 | 21.97433 | 20.85156 | 21.68806 |
| `math/mandelbrot.py` | 45.31027 | 44.19475 | 46.35658 | 37.54353 | 42.53237 | 35.60045 | 38.69587 | 35.91295 |
| `math/pow_simple.py` | 28.92243 | 28.00167 | 26.6183 | 24.04911 | 22.72991 | 21.86886 | 20.82533 | 21.4308 |
| `math/pow_using_math.py` | 28.82812 | 27.40402 | 26.96484 | 23.8192 | 22.78237 | 21.74163 | 21.28404 | 21.49275 |
| `modules/enum/enum_lookup.py` | 28.87612 | 27.70592 | 26.84598 | -- | -- | -- | 22.31473 | -- |
| `modules/json/json_module.py` | 29.05692 | 27.88783 | 27.29967 | 23.42522 | 22.94252 | 21.96763 | 22.23605 | 21.46094 |
| `modules/json/orjson_module.py` | 29.25112 | 28.13783 | 27.76842 | 23.78739 | 23.38114 | 22.39621 | 22.54576 | 22.3058 |
| `programming_game_benchmark/nbody.py` | 28.88895 | 27.72935 | 27.20871 | 23.64397 | 23.47824 | 21.49554 | 21.351 | 21.45703 |
| `programming_game_benchmark/spectral_norm.py` | 29.1144 | 28.49777 | 27.4481 | 24.37835 | 23.75725 | 22.63783 | 22.67801 | 21.81752 |

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

Linux cb3838ccffbc 6.8.0-1029-aws unknown GNU/Linux

CPU(s):                               4
Model name:                           Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
Thread(s) per core:                   1
Core(s) per socket:                   4
NUMA node(s):                         1
NUMA node0 CPU(s):                    0-3

MemTotal:       16373924 kB
MemFree:         5517292 kB
MemAvailable:   15490784 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.9913 | 0.03744 | 1.97913 | 1.95751 | 2.0322 | 30.4135 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.95999 | 0.03957 | 1.96322 | 1.90432 | 2.01013 | 31.03739 |
| `algorithm/search/index.py` | yes | 2.01438 | 0.02688 | 2.01259 | 1.97194 | 2.03858 | 31.04743 |
| `algorithm/search/linear.py` | yes | 2.07217 | 0.03057 | 2.07794 | 2.0376 | 2.11251 | 30.27623 |
| `algorithm/sorting/naive_bubble_sort.py` | yes | 3.34504 | 0.06387 | 3.37289 | 3.24809 | 3.39749 | 22.25558 |
| `algorithm/twosum/twosum.py` | yes | 0.12651 | 0.01192 | 0.12263 | 0.11942 | 0.14766 | 20.93025 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.1323 | 0.01322 | 0.12312 | 0.12214 | 0.14863 | 21.04018 |
| `complex/classes/classes.py` | yes | 0.16911 | 0.01074 | 0.17308 | 0.15026 | 0.1759 | 21.89286 |
| `complex/classes/dataclasses_.py` | yes | 0.2708 | 0.01391 | 0.27681 | 0.25453 | 0.28448 | 22.351 |
| `complex/classes/namedtuple_classes.py` | yes | 0.24026 | 0.01464 | 0.23156 | 0.22747 | 0.2576 | 22.23158 |
| `complex/classes/simplenamespace.py` | yes | 0.16072 | 0.01131 | 0.16782 | 0.1477 | 0.17099 | 21.9933 |
| `complex/classes/sloted_classes.py` | yes | 0.16492 | 0.01575 | 0.1746 | 0.14682 | 0.17769 | 21.96205 |
| `complex/generators/readlines.py` | yes | 0.05703 | 0.01371 | 0.06527 | 0.04123 | 0.06792 | 21.08482 |
| `complex/generators/simple.py` | yes | 0.11359 | 0.00173 | 0.11448 | 0.11147 | 0.11503 | 21.39788 |
| `dummy/dummy.py` | yes | 0.05391 | 0.01394 | 0.06271 | 0.03862 | 0.06667 | 21.12667 |
| `long_run/database/postgresql.py` | yes | 0.26201 | 0.01151 | 0.26388 | 0.24714 | 0.27468 | 26.99777 |
| `long_run/database/sqlite_.py` | yes | 0.98774 | 0.03426 | 0.9909 | 0.94706 | 1.03923 | 66.27902 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 1.0632 | 0.03619 | 1.08043 | 1.02414 | 1.09849 | 64.43359 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.12236 | 0.01162 | 0.11723 | 0.1163 | 0.14312 | 21.20145 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | yes | 1.78232 | 0.02346 | 1.78599 | 1.74675 | 1.80316 | 68.90848 |
| `long_run/processes/maze_generator.py` | yes | 0.39102 | 0.01304 | 0.39326 | 0.37225 | 0.40486 | 21.95926 |
| `long_run/text/clean_text.py` | yes | 0.35142 | 0.01312 | 0.34788 | 0.33659 | 0.36597 | 21.34208 |
| `long_run/text/count_words.py` | yes | 0.15391 | 0.01488 | 0.16333 | 0.13632 | 0.16606 | 21.25391 |
| `math/haversine.py` | yes | 1.19766 | 0.0153 | 1.19678 | 1.17839 | 1.21787 | 20.85156 |
| `math/mandelbrot.py` | yes | 5.61969 | 0.14036 | 5.67325 | 5.37251 | 5.71729 | 38.69587 |
| `math/pow_simple.py` | yes | 0.73067 | 0.00881 | 0.72893 | 0.72343 | 0.74506 | 20.82533 |
| `math/pow_using_math.py` | yes | 2.41339 | 0.01446 | 2.41036 | 2.4013 | 2.4383 | 21.28404 |
| `modules/enum/enum_lookup.py` | yes | 0.54585 | 0.01677 | 0.53542 | 0.53153 | 0.56583 | 22.31473 |
| `modules/json/json_module.py` | yes | 0.82356 | 0.04787 | 0.83311 | 0.75474 | 0.88587 | 22.23605 |
| `modules/json/orjson_module.py` | yes | 0.42738 | 0.01416 | 0.42562 | 0.41284 | 0.45012 | 22.54576 |
| `programming_game_benchmark/nbody.py` | yes | 0.55169 | 0.01795 | 0.54101 | 0.53521 | 0.57506 | 21.351 |
| `programming_game_benchmark/spectral_norm.py` | yes | 2.45879 | 0.05545 | 2.49705 | 2.39667 | 2.50302 | 22.67801 |


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
Python 3.11.13

Linux d54c9eeacffa 6.8.0-1029-aws unknown GNU/Linux

CPU(s):                               4
Model name:                           Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
Thread(s) per core:                   1
Core(s) per socket:                   4
NUMA node(s):                         1
NUMA node0 CPU(s):                    0-3

MemTotal:       16373924 kB
MemFree:         5481356 kB
MemAvailable:   15468144 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.46858 | 0.02635 | 1.46263 | 1.4359 | 1.50576 | 36.9096 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.45884 | 0.02004 | 1.45221 | 1.44034 | 1.49032 | 37.85938 |
| `algorithm/search/index.py` | yes | 1.51439 | 0.03121 | 1.50292 | 1.48897 | 1.56771 | 36.96819 |
| `algorithm/search/linear.py` | yes | 1.57188 | 0.0153 | 1.57534 | 1.54805 | 1.5902 | 36.03348 |
| `algorithm/sorting/naive_bubble_sort.py` | yes | 1.51482 | 0.08891 | 1.56769 | 1.39378 | 1.58436 | 27.28571 |
| `algorithm/twosum/twosum.py` | yes | 0.15542 | 0.01398 | 0.16192 | 0.13694 | 0.16757 | 26.72098 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.15534 | 0.0135 | 0.16376 | 0.14047 | 0.16638 | 27.26451 |
| `complex/classes/classes.py` | yes | 0.08392 | 0.01174 | 0.08777 | 0.06315 | 0.09158 | 28.13895 |
| `complex/classes/dataclasses_.py` | yes | 0.26932 | 0.01369 | 0.27349 | 0.24508 | 0.27783 | 28.58594 |
| `complex/classes/namedtuple_classes.py` | yes | 0.20724 | 0.01003 | 0.20326 | 0.20186 | 0.22515 | 28.01395 |
| `complex/classes/simplenamespace.py` | yes | 0.08667 | 0.01178 | 0.09061 | 0.06579 | 0.09392 | 29.10993 |
| `complex/classes/sloted_classes.py` | yes | 0.0847 | 0.01214 | 0.09002 | 0.06311 | 0.09196 | 28.30804 |
| `complex/generators/readlines.py` | yes | 0.02484 | 0.01122 | 0.01996 | 0.01933 | 0.04489 | 27.17857 |
| `complex/generators/simple.py` | yes | 0.07127 | 0.01209 | 0.07676 | 0.04976 | 0.07825 | 29.05636 |
| `dummy/dummy.py` | yes | 0.02245 | 0.0101 | 0.01826 | 0.01746 | 0.04052 | 26.81641 |
| `long_run/database/postgresql.py` | yes | 0.30007 | 0.00461 | 0.30041 | 0.2954 | 0.30708 | 32.94141 |
| `long_run/database/sqlite_.py` | yes | 1.20454 | 0.02146 | 1.19892 | 1.18107 | 1.23816 | 70.57478 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 1.23963 | 0.02832 | 1.23715 | 1.21444 | 1.28329 | 75.50056 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.12022 | 0.01353 | 0.11506 | 0.11089 | 0.14384 | 27.49944 |
| `long_run/processes/collect_names_from_site.py` | yes | 2.11055 | 0.03468 | 2.10787 | 2.06972 | 2.16519 | 49.34152 |
| `long_run/processes/generate_fake_data.py` | yes | 1.74287 | 0.0378 | 1.72309 | 1.70598 | 1.79447 | 72.37333 |
| `long_run/processes/maze_generator.py` | yes | 0.18592 | 0.01825 | 0.18503 | 0.15706 | 0.20355 | 27.59821 |
| `long_run/text/clean_text.py` | yes | 0.36908 | 0.01411 | 0.3774 | 0.35019 | 0.38197 | 26.62835 |
| `long_run/text/count_words.py` | yes | 0.14338 | 0.01472 | 0.1328 | 0.13238 | 0.16009 | 27.28795 |
| `math/haversine.py` | yes | 0.79849 | 0.0414 | 0.7882 | 0.75649 | 0.86788 | 26.81083 |
| `math/mandelbrot.py` | yes | 4.91635 | 0.05941 | 4.8949 | 4.86168 | 5.01066 | 46.35658 |
| `math/pow_simple.py` | yes | 0.51701 | 0.01217 | 0.51431 | 0.50623 | 0.53789 | 26.6183 |
| `math/pow_using_math.py` | yes | 1.48253 | 0.03165 | 1.49217 | 1.42693 | 1.50638 | 26.96484 |
| `modules/enum/enum_lookup.py` | yes | 0.38366 | 0.0125 | 0.38728 | 0.36187 | 0.39374 | 26.84598 |
| `modules/json/json_module.py` | yes | 0.56231 | 0.0147 | 0.56951 | 0.5419 | 0.57513 | 27.29967 |
| `modules/json/orjson_module.py` | yes | 0.44476 | 0.01496 | 0.43699 | 0.43228 | 0.46276 | 27.76842 |
| `programming_game_benchmark/nbody.py` | yes | 0.30381 | 0.00117 | 0.30319 | 0.30272 | 0.30556 | 27.20871 |
| `programming_game_benchmark/spectral_norm.py` | yes | 1.97961 | 0.03108 | 1.99058 | 1.92441 | 1.99904 | 27.4481 |


### **Python 3.12**

```bash
Python 3.12.11

Linux a0233568a2a1 6.8.0-1029-aws unknown GNU/Linux

CPU(s):                               4
Model name:                           Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
Thread(s) per core:                   1
Core(s) per socket:                   4
NUMA node(s):                         1
NUMA node0 CPU(s):                    0-3

MemTotal:       16373924 kB
MemFree:         5478688 kB
MemAvailable:   15471596 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.66764 | 0.01568 | 1.67508 | 1.64353 | 1.68156 | 36.94029 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.66851 | 0.02357 | 1.67428 | 1.63315 | 1.69282 | 38.54018 |
| `algorithm/search/index.py` | yes | 1.69972 | 0.008 | 1.70126 | 1.68953 | 1.70841 | 36.75614 |
| `algorithm/search/linear.py` | yes | 1.82597 | 0.0154 | 1.82596 | 1.80331 | 1.84035 | 36.67076 |
| `algorithm/sorting/naive_bubble_sort.py` | yes | 2.15651 | 0.17664 | 2.1524 | 1.91127 | 2.4103 | 28.28069 |
| `algorithm/twosum/twosum.py` | yes | 0.18871 | 0.00259 | 0.18817 | 0.18628 | 0.19252 | 27.42969 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.18182 | 0.01035 | 0.18643 | 0.16343 | 0.18753 | 27.83984 |
| `complex/classes/classes.py` | yes | 0.10493 | 0.00104 | 0.10478 | 0.10337 | 0.10588 | 28.45982 |
| `complex/classes/dataclasses_.py` | yes | 0.3342 | 0.01209 | 0.32631 | 0.32448 | 0.34956 | 28.57254 |
| `complex/classes/namedtuple_classes.py` | yes | 0.25611 | 0.01285 | 0.2641 | 0.24145 | 0.26745 | 28.65681 |
| `complex/classes/simplenamespace.py` | yes | 0.11576 | 0.01192 | 0.11102 | 0.10774 | 0.13683 | 29.3817 |
| `complex/classes/sloted_classes.py` | yes | 0.10531 | 0.00307 | 0.10397 | 0.10224 | 0.10914 | 28.5558 |
| `complex/generators/readlines.py` | yes | 0.03508 | 0.01345 | 0.02591 | 0.02471 | 0.0502 | 27.85212 |
| `complex/generators/simple.py` | yes | 0.08636 | 0.00257 | 0.0876 | 0.08288 | 0.08868 | 29.48103 |
| `dummy/dummy.py` | yes | 0.02861 | 0.01173 | 0.02378 | 0.02265 | 0.04956 | 27.94699 |
| `long_run/database/postgresql.py` | yes | 0.32685 | 0.00934 | 0.32379 | 0.32008 | 0.34317 | 33.41964 |
| `long_run/database/sqlite_.py` | yes | 1.29778 | 0.01407 | 1.29569 | 1.28327 | 1.31281 | 71.6942 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 1.37408 | 0.01984 | 1.37082 | 1.34673 | 1.39832 | 75.0692 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.14062 | 0.01412 | 0.13126 | 0.12921 | 0.15732 | 28.20033 |
| `long_run/processes/collect_names_from_site.py` | yes | 2.2636 | 0.0355 | 2.27402 | 2.21897 | 2.30653 | 49.98549 |
| `long_run/processes/generate_fake_data.py` | yes | 1.94218 | 0.0406 | 1.93019 | 1.89954 | 1.99424 | 71.87612 |
| `long_run/processes/maze_generator.py` | yes | 0.21505 | 0.02056 | 0.21043 | 0.18831 | 0.24372 | 27.96261 |
| `long_run/text/clean_text.py` | yes | 0.39905 | 0.00438 | 0.39797 | 0.39431 | 0.4054 | 27.44308 |
| `long_run/text/count_words.py` | yes | 0.16862 | 0.01424 | 0.17681 | 0.15224 | 0.18075 | 27.85547 |
| `math/haversine.py` | yes | 0.96053 | 0.01803 | 0.97121 | 0.94039 | 0.97573 | 28.04855 |
| `math/mandelbrot.py` | yes | 4.53633 | 0.05289 | 4.51011 | 4.50401 | 4.62881 | 44.19475 |
| `math/pow_simple.py` | yes | 0.58863 | 0.00419 | 0.58721 | 0.58462 | 0.59426 | 28.00167 |
| `math/pow_using_math.py` | yes | 1.73134 | 0.03168 | 1.72369 | 1.69828 | 1.78215 | 27.40402 |
| `modules/enum/enum_lookup.py` | yes | 0.4031 | 0.00429 | 0.40446 | 0.39815 | 0.40831 | 27.70592 |
| `modules/json/json_module.py` | yes | 0.6382 | 0.01709 | 0.63065 | 0.6184 | 0.65805 | 27.88783 |
| `modules/json/orjson_module.py` | yes | 0.52792 | 0.01738 | 0.52061 | 0.50901 | 0.54754 | 28.13783 |
| `programming_game_benchmark/nbody.py` | yes | 0.33968 | 0.0133 | 0.33223 | 0.32781 | 0.35467 | 27.72935 |
| `programming_game_benchmark/spectral_norm.py` | yes | 2.4181 | 0.03931 | 2.39893 | 2.39747 | 2.48809 | 28.49777 |


### **Python 3.13**

```bash
Python 3.13.5

Linux b3550199df4c 6.8.0-1029-aws unknown GNU/Linux

CPU(s):                               4
Model name:                           Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
Thread(s) per core:                   1
Core(s) per socket:                   4
NUMA node(s):                         1
NUMA node0 CPU(s):                    0-3

MemTotal:       16373924 kB
MemFree:         5468624 kB
MemAvailable:   15463628 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.70373 | 0.00738 | 1.70422 | 1.69431 | 1.71397 | 37.59542 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.72475 | 0.02621 | 1.70905 | 1.70512 | 1.76594 | 39.32701 |
| `algorithm/search/index.py` | yes | 1.77596 | 0.02158 | 1.78373 | 1.74769 | 1.79718 | 37.68304 |
| `algorithm/search/linear.py` | yes | 1.86495 | 0.01466 | 1.86783 | 1.84491 | 1.88191 | 37.74609 |
| `algorithm/sorting/naive_bubble_sort.py` | yes | 2.3368 | 0.11764 | 2.28738 | 2.21075 | 2.51339 | 28.92746 |
| `algorithm/twosum/twosum.py` | yes | 0.12394 | 0.01183 | 0.12017 | 0.11569 | 0.14448 | 28.89174 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.1286 | 0.01411 | 0.11871 | 0.11782 | 0.14496 | 28.78125 |
| `complex/classes/classes.py` | yes | 0.11014 | 0.0112 | 0.10538 | 0.10463 | 0.13017 | 30.11384 |
| `complex/classes/dataclasses_.py` | yes | 0.33511 | 0.01344 | 0.32978 | 0.3228 | 0.35236 | 30.12667 |
| `complex/classes/namedtuple_classes.py` | yes | 0.19471 | 0.00196 | 0.19409 | 0.19236 | 0.19687 | 29.39732 |
| `complex/classes/simplenamespace.py` | yes | 0.11358 | 0.01132 | 0.10982 | 0.10545 | 0.13345 | 30.65569 |
| `complex/classes/sloted_classes.py` | yes | 0.10168 | 0.00156 | 0.10093 | 0.10032 | 0.104 | 30.18359 |
| `complex/generators/readlines.py` | yes | 0.03732 | 0.01395 | 0.02791 | 0.02663 | 0.05295 | 28.81306 |
| `complex/generators/simple.py` | yes | 0.08982 | 0.00116 | 0.08986 | 0.08853 | 0.0916 | 30.5279 |
| `dummy/dummy.py` | yes | 0.03523 | 0.0144 | 0.0253 | 0.02418 | 0.05111 | 28.7394 |
| `long_run/database/postgresql.py` | yes | 0.34072 | 0.01383 | 0.33449 | 0.3296 | 0.36239 | 34.58147 |
| `long_run/database/sqlite_.py` | yes | 1.30179 | 0.00545 | 1.3005 | 1.29613 | 1.30845 | 68.64063 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 1.49864 | 0.03239 | 1.49911 | 1.4522 | 1.54367 | 75.41964 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.15514 | 0.01374 | 0.16372 | 0.13943 | 0.166 | 28.94196 |
| `long_run/processes/collect_names_from_site.py` | yes | 2.376 | 0.03638 | 2.38883 | 2.31418 | 2.40439 | 51.31864 |
| `long_run/processes/generate_fake_data.py` | yes | 1.99252 | 0.03756 | 1.99962 | 1.94832 | 2.03345 | 67.01618 |
| `long_run/processes/maze_generator.py` | yes | 0.24189 | 0.01855 | 0.24657 | 0.21983 | 0.25982 | 28.99498 |
| `long_run/text/clean_text.py` | yes | 0.40886 | 0.00605 | 0.40719 | 0.40269 | 0.41804 | 28.93973 |
| `long_run/text/count_words.py` | yes | 0.18415 | 0.01077 | 0.18872 | 0.16505 | 0.19071 | 28.81585 |
| `math/haversine.py` | yes | 0.94401 | 0.01486 | 0.9496 | 0.92663 | 0.96067 | 28.98605 |
| `math/mandelbrot.py` | yes | 5.06294 | 0.08826 | 5.09088 | 4.90753 | 5.12534 | 45.31027 |
| `math/pow_simple.py` | yes | 0.69494 | 0.00535 | 0.69318 | 0.69001 | 0.70372 | 28.92243 |
| `math/pow_using_math.py` | yes | 1.84072 | 0.01123 | 1.84143 | 1.82591 | 1.8535 | 28.82812 |
| `modules/enum/enum_lookup.py` | yes | 0.39907 | 0.00155 | 0.39943 | 0.39663 | 0.40084 | 28.87612 |
| `modules/json/json_module.py` | yes | 0.6311 | 0.02068 | 0.62214 | 0.6102 | 0.65736 | 29.05692 |
| `modules/json/orjson_module.py` | yes | 0.50638 | 0.00501 | 0.50629 | 0.49964 | 0.51285 | 29.25112 |
| `programming_game_benchmark/nbody.py` | yes | 0.38462 | 0.01601 | 0.38509 | 0.3601 | 0.40434 | 28.88895 |
| `programming_game_benchmark/spectral_norm.py` | yes | 2.48165 | 0.04083 | 2.49363 | 2.4103 | 2.51394 | 29.1144 |

