
Unit test are code in charge of validating other parts of the code. The code for the unit tests is as important as production code.

A unit test is a piece of code that imports parts of the code with the business logic, and exercises its logic, asserting several scenarios with the idea of guaranteeing certain conditions. 

Unit tests should adhere to the following:
- `isolation`: no other systems should be required to run unit tests
- `performance`: unit tests must run quickly. Developers should be able to run them multiple times as they are iterating the code. It should not take more then a minute.
- `repeatability`: the result of the unit test should always be the same
- `self-validating`: when the unit test is finished, the result should be there. There should be no follow stage/ discussion/ interpretation/....



For reference, there are also other types of tests, just to name 2:
- `integration tests`: testing multiple components and verifying that they still play nice
  - render a configuration template while retrieving data from a database
- `end to end tests`: testing a certain program end to end
  - render a template while retrieving data from a database and then applying the template to a device, finishing up with post-change checks

Typically, integration tests and other long running tests are run after a PR or CR is submitted and prior to a code review.


Terms that are confusing from time to time:
- regression: preservation of existing functionality (while refactoring or adding features)


Reasons for writing tests:
With tests, we can confidently add features and refactor our code without introducing regressions. We can also understand what parts of the code have been proven to work and troubleshooting code will become easier.
- after fixing an issue, we prove that we fixed the issue, and we protect against this bug in the future, regardless of how many times the code is changed.


Testing is hard. Small classes and functions that adhere to SOLID are easier to test. If you are struggling very hard to test some piece of code, review that piece of code against SOLID.

## The examples

To run all tests:

```
python -m pytest .
```


## E00:

A very straightforward example.

```
## all tests 
python -m pytest .

## all tests in target file:
python -m pytest .\test_00_simple.py

## run specific test:
python -m pytest .\test_00_simple.py::test_multiply
```


# E01: mocking

First we run a slow unit test that fails constantly:
```
python -m pytest .\test_01_patch.py::test_get_report
```

Next, we patch the function that retrieves a value from the databased.

We make the return results of the database consistent and we are able test all of the business logic for the function.
```
python -m pytest .\test_01_patch.py::test_get_report_patched
```

# E02: mocking something in a class

The naive approach:
```
python -m pytest .\test_02_patch_class.py::test_report_generator
```

The patched version:

```
python -m pytest .\test_02_patch_class.py::test_report_generator_patched
```

Patching means that the original code (given by a string denoting its location at import time) will be replaced by something else, other than its original code.

Note, trying to test a piece of code that requires a very invasive monkey patch should tell us that perhaps the code is relying too heavily on hard dependencies, and that dependency injection should be used instead.
The mock and see version:

```
python -m pytest .\test_02_patch_class.py::test_report_generator_patched_mock_and_see
```

When we drop to the debugger:
```python
# We see the report_generator has the methods we know:
>>> dir(report_generator)
[
    "_get_database_data",
    "generate_report",
]

# generate_report is unchanged:
>>> type(report_generator.generate_report)      
<class 'method'>

# _get_database_data is a mock:
>>> type(report_generator._get_database_data) 
<class 'unittest.mock.MagicMock'>


Check the patched method:
>>> dir(report_generator._get_database_data)
[
    "assert_any_call",
    "assert_called",
    "assert_called_once",
    "assert_called_once_with",
    "assert_called_with",
    "assert_has_calls",
    "assert_not_called",
    "attach_mock",
    "call_args",
    "call_args_list",
    "call_count",
    "called",
    "configure_mock",
    "method_calls",
    "mock_add_spec",
    "mock_calls",
    "reset_mock",
    "return_value",
    "side_effect",
]
```

# E03: mocking env variables

Patching the env var dict:

```
python -m pytest .\test_03_env_var.py::test_prod_return

python -m pytest .\test_03_env_var.py::test_beta_return

python -m pytest .\test_03_env_var.py::test_default_return

```


# E04: mocking env variables and exceptions

We moved the env into a constant that is put into a data class.

We did this for developer ergonomics.

When we test this, we have to mock before we import.

```
python -m pytest .\test_04_env_var_and_exception.py::test_prod_return

python -m pytest .\test_04_env_var_and_exception.py::test_beta_return

python -m pytest .\test_04_env_var_and_exception.py::test_exception_return
```

Change to RuntimeError to ValueError during execution.

# E05: Testing a weather api:

We do not know the weather in advance.

Here, we patch the return value for something we imported. We patch the return value for `request.get`.

```
python -m pytest test_05_weather_api.py::test_sunny_patched
```

The patched version has some benefits:
- always has the same results
- runs very quickly
- we focus on testing our code instead of the request module

Downsides are that we do not take into consideration all sorts of failure scenarios.


# E06:Pamatrization

Pytest offers a neat way to easily input a large numbers of arguments and test results to check for.

Could also be especially useful in case you want to test parsing large device outputs or API returns for instance. You import the data from another file and feed it to the test. No clutter and many corner cases tested for.

```
python -m pytest .\test_06_paramatrization.py
```

# 07 Side effects:

Testing for side effects can be tricky. But sometimes, you make your functions respond to side effects in important ways.

There are 2 examples here.

1, we test for a side-effect where an API call times out. We want the call to return None.

2, we assemble multiple API returns into a single dictionary. We want to ensure that the function is doing so correctly without making the actual API calls.

```
python -m pytest .\test_007_side_effects.py::test_api_call

python -m pytest .\test_007_side_effects.py::test_api_call_paginated
```


Note, there is also the MagicMock. This is the same as Mock, just that it can be outfitted with magic methods.

# 08 DynamoDB example:

In this example, we have some logic that responds to a method call that returns a scan of DynamoDB.

What we do here is:
- mock the client so that we can focus on testing the logic in our function
- mock the client method return so that we can test the logic in our code

```
python -m pytest .\test_08_ddb.py::test_check_table_no_data

python -m pytest .\test_08_ddb.py::test_check_table_with_data
```

# 09 stdout example

Here, we verify that a message of a certain type was send to stdout.

```
python -m pytest .\test_09_stdout.py
```

https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html


# 10 fixtures and moto testing SQS:

In this example, we use fixtures to setup re-usable 'Mocks'.

In the test function, we depend on moto to simulate the SQS service.
```
python -m pytest .\test_10_queue_moto.py
```



Additional reading/watching:

## Expert overview of Mock:
Lisa Roach - Demystifying the Patch Function - PyCon 2018 (https://youtu.be/ww1UsGZV8fQ)

## RealPython, Intro to testing:
https://realpython.com/python-testing/

## RealPython, Great article on testing using TDD while building a hashmap:

Helps solidify the understanding of testing, classes, dictionaries, pytest and more:
https://realpython.com/python-hash-table/#insert-a-key-value-pair

## Good code, bad code: 

Part 3 is on unit testing https://learning.oreilly.com/library/view/good-code-bad/9781617298936/OEBPS/Text/P3.htm

## Python testing with Pytest:
https://learning.oreilly.com/library/view/python-testing-with/9781680509427/

## Using adapter pattern in testing:
https://miguendes.me/3-ways-to-test-api-client-applications-in-python

## Examples on using Mock:
https://www.dataraccoon.com/knowledge/testing_mock

## When to mock:
https://blog.cleancoder.com/uncle-bob/2014/05/10/WhenToMock.html


## Most used testing libraries:


unittest: https://docs.python.org/3/library/unittest.html
pytest: https://docs.pytest.org/en/latest/


## Clean code in Python

Chapter on testing:
https://learning.oreilly.com/library/view/clean-code-in/9781800560215/Text/Chapter_8.xhtml#_idParaDest-211

## Blog on testable code:


https://testing.googleblog.com/2008/08/by-miko-hevery-so-you-decided-to.html