# Python Benchmark

This is a simple repo to validate and test any (almost any) python program againts all python 3 versions.
 - Python 3.6.15
 - Python 3.7.15
 - Python 3.8.15
 - Python 3.9.15
 - Python 3.10.8
 - Python 3.11.0

## Dependencies

To run the full tests, please keep in mind the you need **docker** (and docker-compose) installed in the environment.

All the tests run inside a docker container image based on each python version described above.

Since python libs have different behaviors and support versions, inside the **docker/** folder there's a requirements99.txt versioning number.

## How to run

To run the full suite, just type in:

```bash
$> ./benchmarh.sh
```

Results will be write down on the main README.md file (it's partiallys regenerated at each run).

## Results