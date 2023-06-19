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

> Last run: Mon Jun 19 02:28:17 PM -03 2023
### **Comparison**

#### How much faster 3.12 is? (Mean / Median from 3.6 to 3.11)
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 40.56% / 40.66% | 28.80% / 28.88% | 32.19% / 32.15% | 30.50% / 31.37% | 15.12% / 14.92% | -6.12% / -5.90% |
| `algorithm/search/hashmap_lookup.py` | 39.80% / 40.79% | 28.92% / 29.18% | 32.64% / 32.86% | 31.99% / 32.59% | 14.02% / 14.55% | -5.68% / -5.39% |
| `algorithm/search/index.py` | 39.00% / 39.98% | 28.59% / 29.78% | 32.17% / 31.99% | 29.43% / 30.10% | 13.97% / 15.02% | -5.44% / -5.12% |
| `algorithm/search/linear.py` | 38.33% / 38.83% | 26.49% / 26.24% | 30.24% / 30.40% | 28.80% / 29.49% | 12.84% / 13.38% | -5.91% / -5.75% |
| `algorithm/twosum/twosum.py` | -0.96% / -1.36% | -18.39% / -18.56% | -11.01% / -11.57% | -3.04% / -3.11% | -10.54% / -10.69% | -15.69% / -15.70% |
| `algorithm/twosum/twosum_naive.py` | 0.46% / -0.18% | -17.69% / -17.84% | -11.43% / -11.24% | -1.63% / -1.44% | -10.16% / -10.01% | -14.90% / -15.34% |
| `complex/classes/classes.py` | 120.78% / 121.41% | 87.18% / 85.55% | 97.95% / 97.95% | 111.44% / 112.53% | 93.64% / 91.88% | -4.09% / -3.70% |
| `complex/classes/dataclasses_.py` | -- / -- | -17.30% / -18.00% | -12.51% / -12.18% | 3.83% / 4.15% | -6.24% / -6.53% | -12.95% / -12.84% |
| `complex/classes/namedtuple_classes.py` | 1.93% / 1.85% | -14.59% / -14.70% | -9.02% / -9.39% | 0.69% / -0.14% | -9.18% / -9.33% | -14.71% / -15.01% |
| `complex/classes/simplenamespace.py` | 130.04% / 129.69% | 56.33% / 56.01% | 57.09% / 57.29% | 71.31% / 70.97% | 59.11% / 58.19% | -3.82% / -5.80% |
| `complex/classes/sloted_classes.py` | 121.79% / 121.94% | 99.01% / 90.14% | 100.54% / 101.17% | 115.47% / 115.54% | 95.02% / 94.46% | -5.43% / -5.18% |
| `complex/generators/simple.py` | 67.18% / 65.61% | 46.11% / 46.97% | 45.48% / 44.42% | 49.22% / 49.26% | 38.65% / 39.05% | -5.97% / -5.37% |
| `dummy/dummy.py` | 116.29% / 116.66% | 75.53% / 74.44% | 97.32% / 97.69% | 110.03% / 110.63% | 88.63% / 88.08% | -9.46% / -12.68% |
| `long_run/database/postgresql.py` | -4.32% / -5.47% | -14.94% / -14.64% | -5.99% / -5.64% | 0.48% / 0.67% | -8.83% / -8.57% | -10.42% / -10.13% |
| `long_run/database/sqlite_.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/file/load_titanic_csv_pandas.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/file/load_titanic_csv_python.py` | 13.61% / 13.95% | 2.10% / 2.18% | 7.57% / 7.80% | 17.85% / 17.45% | 4.99% / 4.76% | -10.50% / -10.89% |
| `long_run/processes/collect_names_from_site.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `long_run/processes/generate_fake_data.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `math/haversine.py` | 2.43% / 1.60% | -1.25% / -1.16% | 0.50% / 0.70% | 15.41% / 16.04% | 9.33% / 9.45% | -7.47% / -7.44% |
| `math/mandelbrot.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
| `math/pow_simple.py` | 82.44% / 83.62% | 79.57% / 81.21% | 80.02% / 81.13% | 86.46% / 86.72% | 75.91% / 76.68% | 8.86% / 9.00% |
| `math/pow_using_math.py` | 29.81% / 30.14% | 24.86% / 27.08% | 10.02% / 11.65% | 17.62% / 19.17% | 15.70% / 17.70% | -5.47% / -4.22% |
| `modules/json/json_module.py` | 39.34% / 40.46% | 33.53% / 34.03% | 33.46% / 33.08% | 33.67% / 34.19% | 19.02% / 20.10% | 3.32% / 3.96% |
| `modules/json/orjson_module.py` | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- | -- / -- |
---

#### How much more memory 3.12 uses? (Memory diff from 3.6 to 3.11)
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 |
|:---|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 18.18% | 17.69% | 20.52% | 16.13% | 8.9% | -1.57% |
| `algorithm/search/hashmap_lookup.py` | 21.54% | 12.2% | 16.81% | 14.14% | 7.42% | -2.83% |
| `algorithm/search/index.py` | 18.49% | 15.5% | 20.63% | 13.85% | 8.27% | -1.17% |
| `algorithm/search/linear.py` | 18.0% | 17.48% | 20.11% | 10.57% | 8.49% | -0.42% |
| `algorithm/twosum/twosum.py` | 18.59% | 30.91% | 30.66% | 17.94% | 18.9% | 4.57% |
| `algorithm/twosum/twosum_naive.py` | 16.39% | 28.26% | 26.82% | 16.07% | 16.26% | 1.97% |
| `complex/classes/classes.py` | 24.06% | 34.34% | 35.13% | 20.61% | 14.33% | 2.84% |
| `complex/classes/dataclasses_.py` | -- | 34.64% | 32.62% | 19.09% | 16.0% | 1.02% |
| `complex/classes/namedtuple_classes.py` | 20.68% | 31.33% | 31.89% | 20.81% | 15.05% | 1.05% |
| `complex/classes/simplenamespace.py` | 26.43% | 38.26% | 35.9% | 24.12% | 15.52% | 4.39% |
| `complex/classes/sloted_classes.py` | 21.32% | 31.96% | 28.54% | 18.58% | 11.56% | -0.21% |
| `complex/generators/simple.py` | 29.43% | 40.07% | 39.27% | 26.18% | 21.47% | 2.85% |
| `dummy/dummy.py` | 19.94% | 30.58% | 28.31% | 17.78% | 14.02% | 2.91% |
| `long_run/database/postgresql.py` | 12.64% | 25.45% | 25.56% | 17.44% | 15.35% | -1.83% |
| `long_run/database/sqlite_.py` | -- | -- | -- | -- | -- | -- |
| `long_run/file/load_titanic_csv_pandas.py` | -- | -- | -- | -- | -- | -- |
| `long_run/file/load_titanic_csv_python.py` | 20.65% | 32.32% | 28.87% | 21.21% | 18.22% | 4.51% |
| `long_run/processes/collect_names_from_site.py` | -- | -- | -- | -- | -- | -- |
| `long_run/processes/generate_fake_data.py` | -- | -- | -- | -- | -- | -- |
| `math/haversine.py` | 21.6% | 30.85% | 29.79% | 20.36% | 18.95% | 5.1% |
| `math/mandelbrot.py` | -- | -- | -- | -- | -- | -- |
| `math/pow_simple.py` | 22.37% | 32.55% | 30.18% | 20.66% | 19.4% | 5.34% |
| `math/pow_using_math.py` | 21.2% | 31.25% | 28.26% | 21.02% | 18.16% | 4.61% |
| `modules/json/json_module.py` | 24.18% | 27.25% | 29.92% | 20.79% | 21.37% | 7.22% |
| `modules/json/orjson_module.py` | -- | -- | -- | -- | -- | -- |
---

#### **Execution**

##### **Mean [s]**
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 1.54013 | 1.41125 | 1.44844 | 1.42989 | 1.26132 | 1.0286 | 1.0957 |
| `algorithm/search/hashmap_lookup.py` | 1.52904 | 1.41011 | 1.45073 | 1.44366 | 1.24706 | 1.03161 | 1.09376 |
| `algorithm/search/index.py` | 1.54776 | 1.43182 | 1.47166 | 1.44119 | 1.2691 | 1.0529 | 1.11349 |
| `algorithm/search/linear.py` | 1.60448 | 1.46711 | 1.51064 | 1.49391 | 1.30882 | 1.09135 | 1.15989 |
| `algorithm/twosum/twosum.py` | 0.08737 | 0.072 | 0.07851 | 0.08554 | 0.07892 | 0.07438 | 0.08822 |
| `algorithm/twosum/twosum_naive.py` | 0.08752 | 0.07171 | 0.07716 | 0.0857 | 0.07827 | 0.07414 | 0.08712 |
| `complex/classes/classes.py` | 0.04961 | 0.04206 | 0.04448 | 0.04751 | 0.04351 | 0.02155 | 0.02247 |
| `complex/classes/dataclasses_.py` | -- | 0.10885 | 0.11515 | 0.13666 | 0.12341 | 0.11457 | 0.13162 |
| `complex/classes/namedtuple_classes.py` | 0.10127 | 0.08485 | 0.09039 | 0.10004 | 0.09023 | 0.08474 | 0.09935 |
| `complex/classes/simplenamespace.py` | 0.06632 | 0.04507 | 0.04529 | 0.04939 | 0.04587 | 0.02773 | 0.02883 |
| `complex/classes/sloted_classes.py` | 0.04946 | 0.04438 | 0.04472 | 0.04805 | 0.04349 | 0.02109 | 0.0223 |
| `complex/generators/simple.py` | 0.07371 | 0.06442 | 0.06414 | 0.06579 | 0.06113 | 0.04146 | 0.04409 |
| `dummy/dummy.py` | 0.03385 | 0.02747 | 0.03088 | 0.03287 | 0.02952 | 0.01417 | 0.01565 |
| `long_run/database/postgresql.py` | 0.16026 | 0.14247 | 0.15745 | 0.16829 | 0.1527 | 0.15004 | 0.16749 |
| `long_run/database/sqlite_.py` | 0.6326 | 0.55063 | 0.62214 | 0.65587 | 0.61714 | 0.6179 | -- |
| `long_run/file/load_titanic_csv_pandas.py` | 0.70979 | 0.59753 | 0.66897 | 0.70569 | 0.65997 | 0.64877 | -- |
| `long_run/file/load_titanic_csv_python.py` | 0.07582 | 0.06814 | 0.07179 | 0.07865 | 0.07007 | 0.05973 | 0.06674 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 1.87281 | 1.92457 | 1.86274 | 1.54971 | -- |
| `long_run/processes/generate_fake_data.py` | 0.8772 | 0.79118 | 0.88291 | 0.90828 | 0.83544 | 0.81786 | -- |
| `math/haversine.py` | 0.85513 | 0.82441 | 0.839 | 0.9635 | 0.9127 | 0.77242 | 0.83482 |
| `math/mandelbrot.py` | 3.28697 | 3.27653 | 3.19851 | 2.77376 | 2.73445 | 2.77351 | -- |
| `math/pow_simple.py` | 0.61479 | 0.60514 | 0.60665 | 0.62836 | 0.59281 | 0.36684 | 0.33699 |
| `math/pow_using_math.py` | 1.73328 | 1.66712 | 1.46903 | 1.57049 | 1.54485 | 1.26224 | 1.33521 |
| `modules/json/json_module.py` | 0.52566 | 0.50372 | 0.50347 | 0.50424 | 0.44899 | 0.38977 | 0.37724 |
| `modules/json/orjson_module.py` | 0.31667 | 0.24937 | 0.26581 | 0.29562 | 0.26201 | 0.20721 | -- |

##### **Median [s]**
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 1.5354 | 1.40684 | 1.44251 | 1.43403 | 1.25447 | 1.02722 | 1.0916 |
| `algorithm/search/hashmap_lookup.py` | 1.53336 | 1.4069 | 1.44703 | 1.44407 | 1.24757 | 1.03045 | 1.08914 |
| `algorithm/search/index.py` | 1.55027 | 1.43729 | 1.46178 | 1.44085 | 1.27386 | 1.05082 | 1.10751 |
| `algorithm/search/linear.py` | 1.60446 | 1.45894 | 1.507 | 1.49649 | 1.31033 | 1.0893 | 1.15571 |
| `algorithm/twosum/twosum.py` | 0.08698 | 0.07181 | 0.07798 | 0.08544 | 0.07875 | 0.07434 | 0.08818 |
| `algorithm/twosum/twosum_naive.py` | 0.08683 | 0.07147 | 0.07721 | 0.08574 | 0.07828 | 0.07365 | 0.08699 |
| `complex/classes/classes.py` | 0.04964 | 0.0416 | 0.04438 | 0.04765 | 0.04302 | 0.02159 | 0.02242 |
| `complex/classes/dataclasses_.py` | -- | 0.10759 | 0.11522 | 0.13665 | 0.12263 | 0.11435 | 0.1312 |
| `complex/classes/namedtuple_classes.py` | 0.10128 | 0.08482 | 0.0901 | 0.0993 | 0.09016 | 0.08451 | 0.09944 |
| `complex/classes/simplenamespace.py` | 0.06615 | 0.04493 | 0.0453 | 0.04924 | 0.04556 | 0.02713 | 0.0288 |
| `complex/classes/sloted_classes.py` | 0.04927 | 0.04221 | 0.04466 | 0.04785 | 0.04317 | 0.02105 | 0.0222 |
| `complex/generators/simple.py` | 0.07252 | 0.06436 | 0.06324 | 0.06536 | 0.06089 | 0.04144 | 0.04379 |
| `dummy/dummy.py` | 0.03382 | 0.02723 | 0.03086 | 0.03288 | 0.02936 | 0.01363 | 0.01561 |
| `long_run/database/postgresql.py` | 0.15763 | 0.14234 | 0.15735 | 0.16788 | 0.15247 | 0.14987 | 0.16676 |
| `long_run/database/sqlite_.py` | 0.63187 | 0.54936 | 0.62133 | 0.65338 | 0.61407 | 0.61357 | -- |
| `long_run/file/load_titanic_csv_pandas.py` | 0.70892 | 0.59781 | 0.66868 | 0.7026 | 0.65944 | 0.64927 | -- |
| `long_run/file/load_titanic_csv_python.py` | 0.07587 | 0.06803 | 0.07177 | 0.0782 | 0.06975 | 0.05933 | 0.06658 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 1.86932 | 1.92492 | 1.86095 | 1.54304 | -- |
| `long_run/processes/generate_fake_data.py` | 0.87491 | 0.78949 | 0.84905 | 0.89431 | 0.83512 | 0.81728 | -- |
| `math/haversine.py` | 0.84519 | 0.82224 | 0.83773 | 0.96534 | 0.91052 | 0.77 | 0.83189 |
| `math/mandelbrot.py` | 3.29095 | 3.26773 | 3.22139 | 2.7637 | 2.72439 | 2.76517 | -- |
| `math/pow_simple.py` | 0.61359 | 0.60555 | 0.60529 | 0.62396 | 0.5904 | 0.36425 | 0.33417 |
| `math/pow_using_math.py` | 1.70447 | 1.66437 | 1.46223 | 1.56082 | 1.54151 | 1.25448 | 1.30969 |
| `modules/json/json_module.py` | 0.52684 | 0.50275 | 0.49918 | 0.50335 | 0.4505 | 0.38993 | 0.37509 |
| `modules/json/orjson_module.py` | 0.31485 | 0.24759 | 0.26532 | 0.29642 | 0.26204 | 0.20643 | -- |

#### **Memory Usage**

##### **MEM [MB]**
| Command | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | 29.08555 | 29.2043 | 28.51992 | 29.59766 | 31.56289 | 34.92109 | 34.37187 |
| `algorithm/search/hashmap_lookup.py` | 28.38281 | 30.74609 | 29.53164 | 30.22305 | 32.11445 | 35.50039 | 34.49609 |
| `algorithm/search/index.py` | 28.93047 | 29.67852 | 28.41523 | 30.10937 | 31.66016 | 34.68477 | 34.27852 |
| `algorithm/search/linear.py` | 29.04844 | 29.17852 | 28.53828 | 31.00156 | 31.59492 | 34.42266 | 34.27813 |
| `algorithm/twosum/twosum.py` | 22.36055 | 20.25703 | 20.2957 | 22.4832 | 22.30234 | 25.35938 | 26.51758 |
| `algorithm/twosum/twosum_naive.py` | 22.2375 | 20.17969 | 20.40977 | 22.3 | 22.26211 | 25.38164 | 25.88281 |
| `complex/classes/classes.py` | 21.96406 | 20.28359 | 20.16406 | 22.5918 | 23.83359 | 26.49609 | 27.24805 |
| `complex/classes/dataclasses_.py` | -- | 20.18281 | 20.49023 | 22.81836 | 23.42617 | 26.9 | 27.17422 |
| `complex/classes/namedtuple_classes.py` | 22.25586 | 20.45195 | 20.36484 | 22.23203 | 23.3457 | 26.58125 | 26.85937 |
| `complex/classes/simplenamespace.py` | 21.99648 | 20.11445 | 20.4625 | 22.40586 | 24.07305 | 26.63867 | 27.80937 |
| `complex/classes/sloted_classes.py` | 21.87539 | 20.11094 | 20.64609 | 22.38047 | 23.78945 | 26.59531 | 26.53867 |
| `complex/generators/simple.py` | 22.04688 | 20.37305 | 20.48945 | 22.61484 | 23.49219 | 27.74492 | 28.53594 |
| `dummy/dummy.py` | 21.74727 | 19.97578 | 20.32891 | 22.1457 | 22.87578 | 25.34687 | 26.08359 |
| `long_run/database/postgresql.py` | 27.10742 | 24.33867 | 24.31758 | 25.99922 | 26.47148 | 31.10273 | 30.53359 |
| `long_run/database/sqlite_.py` | 63.10898 | 65.14648 | 65.07109 | 65.73047 | 65.5582 | 71.00781 | -- |
| `long_run/file/load_titanic_csv_pandas.py` | 61.91055 | 63.73516 | 63.64687 | 64.33555 | 63.54531 | 69.41211 | -- |
| `long_run/file/load_titanic_csv_python.py` | 22.14766 | 20.19414 | 20.73633 | 22.04648 | 22.60273 | 25.56797 | 26.72188 |
| `long_run/processes/collect_names_from_site.py` | -- | -- | 44.17812 | 44.00625 | 44.15117 | 46.37266 | -- |
| `long_run/processes/generate_fake_data.py` | 65.00781 | 68.55156 | 65.42148 | 68.61523 | 67.46289 | 70.86055 | -- |
| `math/haversine.py` | 21.91406 | 20.36367 | 20.53086 | 22.13945 | 22.40156 | 25.35312 | 26.64688 |
| `math/mandelbrot.py` | 36.43125 | 34.65742 | 34.90391 | 42.32266 | 42.72305 | 39.61758 | -- |
| `math/pow_simple.py` | 21.82969 | 20.15391 | 20.5207 | 22.13984 | 22.37344 | 25.35898 | 26.71328 |
| `math/pow_using_math.py` | 21.87539 | 20.19961 | 20.67148 | 21.90703 | 22.43789 | 25.34414 | 26.5125 |
| `modules/json/json_module.py` | 21.97109 | 21.44141 | 21.00078 | 22.58828 | 22.48125 | 25.44648 | 27.28438 |
| `modules/json/orjson_module.py` | 22.68164 | 21.62539 | 21.41289 | 23.1875 | 23.00703 | 26.08867 | -- |

---


### **Python 3.6**

```bash
Python 3.6.15

Linux 59b48a56ebcf 5.15.0-75-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16066528 kB
MemFree:         1184748 kB
MemAvailable:    9843816 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.54013 | 0.02548 | 1.5354 | 1.50594 | 1.584 | 29.08555 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.52904 | 0.01177 | 1.53336 | 1.51116 | 1.54184 | 28.38281 |
| `algorithm/search/index.py` | yes | 1.54776 | 0.00983 | 1.55027 | 1.53244 | 1.55794 | 28.93047 |
| `algorithm/search/linear.py` | yes | 1.60448 | 0.01073 | 1.60446 | 1.58699 | 1.62372 | 29.04844 |
| `algorithm/twosum/twosum.py` | yes | 0.08737 | 0.00134 | 0.08698 | 0.08589 | 0.09009 | 22.36055 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.08752 | 0.00164 | 0.08683 | 0.08589 | 0.09041 | 22.2375 |
| `complex/classes/classes.py` | yes | 0.04961 | 0.00036 | 0.04964 | 0.04894 | 0.05007 | 21.96406 |
| `complex/classes/dataclasses_.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `complex/classes/namedtuple_classes.py` | yes | 0.10127 | 0.00057 | 0.10128 | 0.10039 | 0.10208 | 22.25586 |
| `complex/classes/simplenamespace.py` | yes | 0.06632 | 0.00063 | 0.06615 | 0.06574 | 0.06762 | 21.99648 |
| `complex/classes/sloted_classes.py` | yes | 0.04946 | 0.00057 | 0.04927 | 0.04867 | 0.05057 | 21.87539 |
| `complex/generators/simple.py` | yes | 0.07371 | 0.00554 | 0.07252 | 0.06893 | 0.08783 | 22.04688 |
| `dummy/dummy.py` | yes | 0.03385 | 0.00035 | 0.03382 | 0.03348 | 0.03471 | 21.74727 |
| `long_run/database/postgresql.py` | yes | 0.16026 | 0.00672 | 0.15763 | 0.15629 | 0.17823 | 27.10742 |
| `long_run/database/sqlite_.py` | yes | 0.6326 | 0.00377 | 0.63187 | 0.62898 | 0.64243 | 63.10898 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.70979 | 0.00423 | 0.70892 | 0.70581 | 0.72129 | 61.91055 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.07582 | 0.00039 | 0.07587 | 0.07517 | 0.07639 | 22.14766 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | yes | 0.8772 | 0.00741 | 0.87491 | 0.86746 | 0.88927 | 65.00781 |
| `math/haversine.py` | yes | 0.85513 | 0.02545 | 0.84519 | 0.83545 | 0.92089 | 21.91406 |
| `math/mandelbrot.py` | yes | 3.28697 | 0.08116 | 3.29095 | 3.07596 | 3.36694 | 36.43125 |
| `math/pow_simple.py` | yes | 0.61479 | 0.00456 | 0.61359 | 0.61059 | 0.62491 | 21.82969 |
| `math/pow_using_math.py` | yes | 1.73328 | 0.08346 | 1.70447 | 1.6561 | 1.87841 | 21.87539 |
| `modules/json/json_module.py` | yes | 0.52566 | 0.00566 | 0.52684 | 0.51489 | 0.53318 | 21.97109 |
| `modules/json/orjson_module.py` | yes | 0.31667 | 0.00686 | 0.31485 | 0.31124 | 0.33551 | 22.68164 |


### **Python 3.7**

```bash
Python 3.7.17

Linux 43cc30263bfc 5.15.0-75-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16066528 kB
MemFree:         1161888 kB
MemAvailable:    9864800 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.41125 | 0.01998 | 1.40684 | 1.38363 | 1.43886 | 29.2043 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.41011 | 0.01814 | 1.4069 | 1.39234 | 1.45542 | 30.74609 |
| `algorithm/search/index.py` | yes | 1.43182 | 0.01682 | 1.43729 | 1.40849 | 1.45476 | 29.67852 |
| `algorithm/search/linear.py` | yes | 1.46711 | 0.03543 | 1.45894 | 1.43316 | 1.56261 | 29.17852 |
| `algorithm/twosum/twosum.py` | yes | 0.072 | 0.00047 | 0.07181 | 0.07151 | 0.07316 | 20.25703 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07171 | 0.00063 | 0.07147 | 0.07107 | 0.07282 | 20.17969 |
| `complex/classes/classes.py` | yes | 0.04206 | 0.00133 | 0.0416 | 0.04132 | 0.04572 | 20.28359 |
| `complex/classes/dataclasses_.py` | yes | 0.10885 | 0.00439 | 0.10759 | 0.10648 | 0.12112 | 20.18281 |
| `complex/classes/namedtuple_classes.py` | yes | 0.08485 | 0.00114 | 0.08482 | 0.08354 | 0.08749 | 20.45195 |
| `complex/classes/simplenamespace.py` | yes | 0.04507 | 0.00324 | 0.04493 | 0.04198 | 0.05243 | 20.11445 |
| `complex/classes/sloted_classes.py` | yes | 0.04438 | 0.00626 | 0.04221 | 0.04139 | 0.06202 | 20.11094 |
| `complex/generators/simple.py` | yes | 0.06442 | 0.00045 | 0.06436 | 0.0637 | 0.06516 | 20.37305 |
| `dummy/dummy.py` | yes | 0.02747 | 0.0005 | 0.02723 | 0.02705 | 0.02864 | 19.97578 |
| `long_run/database/postgresql.py` | yes | 0.14247 | 0.00045 | 0.14234 | 0.14202 | 0.14331 | 24.33867 |
| `long_run/database/sqlite_.py` | yes | 0.55063 | 0.0048 | 0.54936 | 0.54583 | 0.56009 | 65.14648 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.59753 | 0.0015 | 0.59781 | 0.5948 | 0.59938 | 63.73516 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06814 | 0.00071 | 0.06803 | 0.06722 | 0.06974 | 20.19414 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | yes | 0.79118 | 0.0047 | 0.78949 | 0.78722 | 0.8015 | 68.55156 |
| `math/haversine.py` | yes | 0.82441 | 0.01159 | 0.82224 | 0.81175 | 0.85401 | 20.36367 |
| `math/mandelbrot.py` | yes | 3.27653 | 0.04137 | 3.26773 | 3.23186 | 3.35609 | 34.65742 |
| `math/pow_simple.py` | yes | 0.60514 | 0.00832 | 0.60555 | 0.59277 | 0.619 | 20.15391 |
| `math/pow_using_math.py` | yes | 1.66712 | 0.02872 | 1.66437 | 1.61921 | 1.71543 | 20.19961 |
| `modules/json/json_module.py` | yes | 0.50372 | 0.00505 | 0.50275 | 0.49589 | 0.51301 | 21.44141 |
| `modules/json/orjson_module.py` | yes | 0.24937 | 0.00483 | 0.24759 | 0.24351 | 0.25756 | 21.62539 |


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

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.44844 | 0.0157 | 1.44251 | 1.43275 | 1.4757 | 28.51992 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.45073 | 0.01837 | 1.44703 | 1.42873 | 1.49609 | 29.53164 |
| `algorithm/search/index.py` | yes | 1.47166 | 0.02819 | 1.46178 | 1.43617 | 1.52108 | 28.41523 |
| `algorithm/search/linear.py` | yes | 1.51064 | 0.01894 | 1.507 | 1.4895 | 1.54583 | 28.53828 |
| `algorithm/twosum/twosum.py` | yes | 0.07851 | 0.00168 | 0.07798 | 0.07657 | 0.08154 | 20.2957 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07716 | 0.00031 | 0.07721 | 0.07644 | 0.07752 | 20.40977 |
| `complex/classes/classes.py` | yes | 0.04448 | 0.0004 | 0.04438 | 0.04381 | 0.04515 | 20.16406 |
| `complex/classes/dataclasses_.py` | yes | 0.11515 | 0.00046 | 0.11522 | 0.11434 | 0.1157 | 20.49023 |
| `complex/classes/namedtuple_classes.py` | yes | 0.09039 | 0.00063 | 0.0901 | 0.08974 | 0.09177 | 20.36484 |
| `complex/classes/simplenamespace.py` | yes | 0.04529 | 0.00037 | 0.0453 | 0.04472 | 0.0458 | 20.4625 |
| `complex/classes/sloted_classes.py` | yes | 0.04472 | 0.00021 | 0.04466 | 0.04449 | 0.04513 | 20.64609 |
| `complex/generators/simple.py` | yes | 0.06414 | 0.00279 | 0.06324 | 0.06266 | 0.07203 | 20.48945 |
| `dummy/dummy.py` | yes | 0.03088 | 0.00022 | 0.03086 | 0.03059 | 0.03131 | 20.32891 |
| `long_run/database/postgresql.py` | yes | 0.15745 | 0.00111 | 0.15735 | 0.15564 | 0.15925 | 24.31758 |
| `long_run/database/sqlite_.py` | yes | 0.62214 | 0.00445 | 0.62133 | 0.61673 | 0.63013 | 65.07109 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.66897 | 0.00133 | 0.66868 | 0.66754 | 0.67187 | 63.64687 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.07179 | 0.00035 | 0.07177 | 0.0713 | 0.07227 | 20.73633 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.87281 | 0.02755 | 1.86932 | 1.83091 | 1.92798 | 44.17812 |
| `long_run/processes/generate_fake_data.py` | yes | 0.88291 | 0.0542 | 0.84905 | 0.83816 | 0.98849 | 65.42148 |
| `math/haversine.py` | yes | 0.839 | 0.00975 | 0.83773 | 0.82649 | 0.86103 | 20.53086 |
| `math/mandelbrot.py` | yes | 3.19851 | 0.07322 | 3.22139 | 3.11481 | 3.33318 | 34.90391 |
| `math/pow_simple.py` | yes | 0.60665 | 0.00305 | 0.60529 | 0.60343 | 0.61244 | 20.5207 |
| `math/pow_using_math.py` | yes | 1.46903 | 0.01513 | 1.46223 | 1.45102 | 1.50393 | 20.67148 |
| `modules/json/json_module.py` | yes | 0.50347 | 0.01036 | 0.49918 | 0.49341 | 0.52657 | 21.00078 |
| `modules/json/orjson_module.py` | yes | 0.26581 | 0.0016 | 0.26532 | 0.26294 | 0.26834 | 21.41289 |


### **Python 3.9**

```bash
Python 3.9.17

Linux 9658ef5e81c4 5.15.0-75-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16066528 kB
MemFree:         1276392 kB
MemAvailable:    9833072 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.42989 | 0.02233 | 1.43403 | 1.40013 | 1.46244 | 29.59766 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.44366 | 0.01612 | 1.44407 | 1.42367 | 1.47255 | 30.22305 |
| `algorithm/search/index.py` | yes | 1.44119 | 0.00712 | 1.44085 | 1.42973 | 1.45429 | 30.10937 |
| `algorithm/search/linear.py` | yes | 1.49391 | 0.01972 | 1.49649 | 1.46549 | 1.52727 | 31.00156 |
| `algorithm/twosum/twosum.py` | yes | 0.08554 | 0.00042 | 0.08544 | 0.08507 | 0.08648 | 22.4832 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.0857 | 0.00042 | 0.08574 | 0.08505 | 0.08652 | 22.3 |
| `complex/classes/classes.py` | yes | 0.04751 | 0.0004 | 0.04765 | 0.04691 | 0.04803 | 22.5918 |
| `complex/classes/dataclasses_.py` | yes | 0.13666 | 0.00069 | 0.13665 | 0.13582 | 0.13784 | 22.81836 |
| `complex/classes/namedtuple_classes.py` | yes | 0.10004 | 0.00205 | 0.0993 | 0.09878 | 0.10535 | 22.23203 |
| `complex/classes/simplenamespace.py` | yes | 0.04939 | 0.00028 | 0.04924 | 0.04904 | 0.04996 | 22.40586 |
| `complex/classes/sloted_classes.py` | yes | 0.04805 | 0.00064 | 0.04785 | 0.04728 | 0.04915 | 22.38047 |
| `complex/generators/simple.py` | yes | 0.06579 | 0.00144 | 0.06536 | 0.06483 | 0.06966 | 22.61484 |
| `dummy/dummy.py` | yes | 0.03287 | 0.00028 | 0.03288 | 0.03253 | 0.03328 | 22.1457 |
| `long_run/database/postgresql.py` | yes | 0.16829 | 0.00179 | 0.16788 | 0.16693 | 0.17314 | 25.99922 |
| `long_run/database/sqlite_.py` | yes | 0.65587 | 0.00663 | 0.65338 | 0.64998 | 0.66944 | 65.73047 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.70569 | 0.00759 | 0.7026 | 0.69781 | 0.72369 | 64.33555 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.07865 | 0.0011 | 0.0782 | 0.07756 | 0.08068 | 22.04648 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.92457 | 0.03282 | 1.92492 | 1.86665 | 1.96784 | 44.00625 |
| `long_run/processes/generate_fake_data.py` | yes | 0.90828 | 0.03115 | 0.89431 | 0.88525 | 0.97941 | 68.61523 |
| `math/haversine.py` | yes | 0.9635 | 0.01203 | 0.96534 | 0.94099 | 0.98069 | 22.13945 |
| `math/mandelbrot.py` | yes | 2.77376 | 0.03993 | 2.7637 | 2.73668 | 2.8592 | 42.32266 |
| `math/pow_simple.py` | yes | 0.62836 | 0.01007 | 0.62396 | 0.61848 | 0.64577 | 22.13984 |
| `math/pow_using_math.py` | yes | 1.57049 | 0.0239 | 1.56082 | 1.54443 | 1.605 | 21.90703 |
| `modules/json/json_module.py` | yes | 0.50424 | 0.00685 | 0.50335 | 0.49489 | 0.52053 | 22.58828 |
| `modules/json/orjson_module.py` | yes | 0.29562 | 0.00582 | 0.29642 | 0.28817 | 0.30604 | 23.1875 |


### **Python 3.10**

```bash
Python 3.10.12

Linux 29e6d6ac2120 5.15.0-75-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16066528 kB
MemFree:         1313168 kB
MemAvailable:    9820808 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.26132 | 0.02203 | 1.25447 | 1.23716 | 1.30216 | 31.56289 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.24706 | 0.01221 | 1.24757 | 1.22044 | 1.26395 | 32.11445 |
| `algorithm/search/index.py` | yes | 1.2691 | 0.01184 | 1.27386 | 1.24781 | 1.28229 | 31.66016 |
| `algorithm/search/linear.py` | yes | 1.30882 | 0.0109 | 1.31033 | 1.29043 | 1.32398 | 31.59492 |
| `algorithm/twosum/twosum.py` | yes | 0.07892 | 0.00134 | 0.07875 | 0.07755 | 0.08217 | 22.30234 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07827 | 0.00035 | 0.07828 | 0.07761 | 0.07879 | 22.26211 |
| `complex/classes/classes.py` | yes | 0.04351 | 0.00112 | 0.04302 | 0.04266 | 0.0458 | 23.83359 |
| `complex/classes/dataclasses_.py` | yes | 0.12341 | 0.00171 | 0.12263 | 0.12178 | 0.12654 | 23.42617 |
| `complex/classes/namedtuple_classes.py` | yes | 0.09023 | 0.00063 | 0.09016 | 0.08935 | 0.09115 | 23.3457 |
| `complex/classes/simplenamespace.py` | yes | 0.04587 | 0.00086 | 0.04556 | 0.04505 | 0.04772 | 24.07305 |
| `complex/classes/sloted_classes.py` | yes | 0.04349 | 0.00106 | 0.04317 | 0.04273 | 0.04628 | 23.78945 |
| `complex/generators/simple.py` | yes | 0.06113 | 0.00104 | 0.06089 | 0.06002 | 0.06366 | 23.49219 |
| `dummy/dummy.py` | yes | 0.02952 | 0.00043 | 0.02936 | 0.02923 | 0.03061 | 22.87578 |
| `long_run/database/postgresql.py` | yes | 0.1527 | 0.00164 | 0.15247 | 0.15087 | 0.157 | 26.47148 |
| `long_run/database/sqlite_.py` | yes | 0.61714 | 0.00888 | 0.61407 | 0.61002 | 0.63732 | 65.5582 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.65997 | 0.00595 | 0.65944 | 0.65323 | 0.67292 | 63.54531 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.07007 | 0.00153 | 0.06975 | 0.06884 | 0.07423 | 22.60273 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.86274 | 0.02267 | 1.86095 | 1.83698 | 1.91582 | 44.15117 |
| `long_run/processes/generate_fake_data.py` | yes | 0.83544 | 0.00622 | 0.83512 | 0.8252 | 0.84676 | 67.46289 |
| `math/haversine.py` | yes | 0.9127 | 0.01255 | 0.91052 | 0.89655 | 0.93302 | 22.40156 |
| `math/mandelbrot.py` | yes | 2.73445 | 0.02342 | 2.72439 | 2.70771 | 2.77519 | 42.72305 |
| `math/pow_simple.py` | yes | 0.59281 | 0.00623 | 0.5904 | 0.58696 | 0.60413 | 22.37344 |
| `math/pow_using_math.py` | yes | 1.54485 | 0.02335 | 1.54151 | 1.51276 | 1.58291 | 22.43789 |
| `modules/json/json_module.py` | yes | 0.44899 | 0.00502 | 0.4505 | 0.44012 | 0.45424 | 22.48125 |
| `modules/json/orjson_module.py` | yes | 0.26201 | 0.00249 | 0.26204 | 0.25817 | 0.26565 | 23.00703 |


### **Python 3.11**

```bash
Python 3.11.4

Linux c0d60951e8d2 5.15.0-75-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16066528 kB
MemFree:         1285772 kB
MemAvailable:    9823128 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.0286 | 0.00467 | 1.02722 | 1.02185 | 1.03592 | 34.92109 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.03161 | 0.00645 | 1.03045 | 1.02408 | 1.04706 | 35.50039 |
| `algorithm/search/index.py` | yes | 1.0529 | 0.00857 | 1.05082 | 1.04366 | 1.0716 | 34.68477 |
| `algorithm/search/linear.py` | yes | 1.09135 | 0.01493 | 1.0893 | 1.07037 | 1.12331 | 34.42266 |
| `algorithm/twosum/twosum.py` | yes | 0.07438 | 0.00053 | 0.07434 | 0.0734 | 0.07529 | 25.35938 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.07414 | 0.00177 | 0.07365 | 0.07314 | 0.07909 | 25.38164 |
| `complex/classes/classes.py` | yes | 0.02155 | 0.00026 | 0.02159 | 0.02117 | 0.02207 | 26.49609 |
| `complex/classes/dataclasses_.py` | yes | 0.11457 | 0.00126 | 0.11435 | 0.11331 | 0.11741 | 26.9 |
| `complex/classes/namedtuple_classes.py` | yes | 0.08474 | 0.00103 | 0.08451 | 0.08357 | 0.08679 | 26.58125 |
| `complex/classes/simplenamespace.py` | yes | 0.02773 | 0.00125 | 0.02713 | 0.02682 | 0.0309 | 26.63867 |
| `complex/classes/sloted_classes.py` | yes | 0.02109 | 0.0002 | 0.02105 | 0.02092 | 0.0216 | 26.59531 |
| `complex/generators/simple.py` | yes | 0.04146 | 0.0004 | 0.04144 | 0.04075 | 0.04208 | 27.74492 |
| `dummy/dummy.py` | yes | 0.01417 | 0.00133 | 0.01363 | 0.01286 | 0.01605 | 25.34687 |
| `long_run/database/postgresql.py` | yes | 0.15004 | 0.00057 | 0.14987 | 0.14942 | 0.15091 | 31.10273 |
| `long_run/database/sqlite_.py` | yes | 0.6179 | 0.0083 | 0.61357 | 0.61198 | 0.63587 | 71.00781 |
| `long_run/file/load_titanic_csv_pandas.py` | yes | 0.64877 | 0.00364 | 0.64927 | 0.64318 | 0.65369 | 69.41211 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.05973 | 0.00081 | 0.05933 | 0.0591 | 0.06097 | 25.56797 |
| `long_run/processes/collect_names_from_site.py` | yes | 1.54971 | 0.03118 | 1.54304 | 1.51976 | 1.62826 | 46.37266 |
| `long_run/processes/generate_fake_data.py` | yes | 0.81786 | 0.00675 | 0.81728 | 0.81007 | 0.83221 | 70.86055 |
| `math/haversine.py` | yes | 0.77242 | 0.00903 | 0.77 | 0.76255 | 0.79008 | 25.35312 |
| `math/mandelbrot.py` | yes | 2.77351 | 0.06572 | 2.76517 | 2.69899 | 2.87264 | 39.61758 |
| `math/pow_simple.py` | yes | 0.36684 | 0.00648 | 0.36425 | 0.36086 | 0.3778 | 25.35898 |
| `math/pow_using_math.py` | yes | 1.26224 | 0.02651 | 1.25448 | 1.23579 | 1.32783 | 25.34414 |
| `modules/json/json_module.py` | yes | 0.38977 | 0.00461 | 0.38993 | 0.38336 | 0.39598 | 25.44648 |
| `modules/json/orjson_module.py` | yes | 0.20721 | 0.00166 | 0.20643 | 0.20542 | 0.20944 | 26.08867 |


### **Python 3.12**

```bash
Python 3.12.0b2

Linux 3ef38ae87e04 5.15.0-75-generic unknown GNU/Linux

CPU(s):              12
Thread(s) per core:  2
Core(s) per socket:  6
NUMA node(s):        1
Model name:          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
CPU max MHz:         4100.0000
NUMA node0 CPU(s):   0-11

MemTotal:       16066528 kB
MemFree:         1259324 kB
MemAvailable:    9811956 kB
```

| Command | Executed | Mean [s] | Stddev [s] | Median [s] | Min [s] | Max [s] | Memory [MB] |
|:---|---:|---:|---:|---:|---:|---:|---:|
| `algorithm/search/bin.py` | yes | 1.0957 | 0.01739 | 1.0916 | 1.07376 | 1.13124 | 34.37187 |
| `algorithm/search/hashmap_lookup.py` | yes | 1.09376 | 0.01477 | 1.08914 | 1.08048 | 1.13018 | 34.49609 |
| `algorithm/search/index.py` | yes | 1.11349 | 0.01857 | 1.10751 | 1.09563 | 1.14884 | 34.27852 |
| `algorithm/search/linear.py` | yes | 1.15989 | 0.01467 | 1.15571 | 1.14137 | 1.19368 | 34.27813 |
| `algorithm/twosum/twosum.py` | yes | 0.08822 | 0.00058 | 0.08818 | 0.08746 | 0.08912 | 26.51758 |
| `algorithm/twosum/twosum_naive.py` | yes | 0.08712 | 0.00057 | 0.08699 | 0.08647 | 0.08836 | 25.88281 |
| `complex/classes/classes.py` | yes | 0.02247 | 0.00024 | 0.02242 | 0.02207 | 0.02295 | 27.24805 |
| `complex/classes/dataclasses_.py` | yes | 0.13162 | 0.00191 | 0.1312 | 0.12969 | 0.13579 | 27.17422 |
| `complex/classes/namedtuple_classes.py` | yes | 0.09935 | 0.0004 | 0.09944 | 0.09871 | 0.09992 | 26.85937 |
| `complex/classes/simplenamespace.py` | yes | 0.02883 | 0.0003 | 0.0288 | 0.02834 | 0.0294 | 27.80937 |
| `complex/classes/sloted_classes.py` | yes | 0.0223 | 0.00027 | 0.0222 | 0.02201 | 0.02271 | 26.53867 |
| `complex/generators/simple.py` | yes | 0.04409 | 0.00076 | 0.04379 | 0.0434 | 0.0459 | 28.53594 |
| `dummy/dummy.py` | yes | 0.01565 | 0.0009 | 0.01561 | 0.01456 | 0.01714 | 26.08359 |
| `long_run/database/postgresql.py` | yes | 0.16749 | 0.00202 | 0.16676 | 0.16623 | 0.17296 | 30.53359 |
| `long_run/database/sqlite_.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/file/load_titanic_csv_pandas.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/file/load_titanic_csv_python.py` | yes | 0.06674 | 0.00052 | 0.06658 | 0.06629 | 0.06814 | 26.72188 |
| `long_run/processes/collect_names_from_site.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `long_run/processes/generate_fake_data.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `math/haversine.py` | yes | 0.83482 | 0.01346 | 0.83189 | 0.8182 | 0.86583 | 26.64688 |
| `math/mandelbrot.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |
| `math/pow_simple.py` | yes | 0.33699 | 0.00538 | 0.33417 | 0.333 | 0.34693 | 26.71328 |
| `math/pow_using_math.py` | yes | 1.33521 | 0.07216 | 1.30969 | 1.25241 | 1.45165 | 26.5125 |
| `modules/json/json_module.py` | yes | 0.37724 | 0.00401 | 0.37509 | 0.37412 | 0.38529 | 27.28438 |
| `modules/json/orjson_module.py` | no | -1 | -1 | -1 | -1 | -1 | -1 |

