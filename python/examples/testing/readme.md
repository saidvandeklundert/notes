# Mock and patch


Mock an item where it is used, not where it came from.

A mock object substitutes a real object in a testing environment. The mock object also contains information on it's usage during testing.

## Confusing things about patch:

1. Identifying the target

The target must be importable from the test file.

2. Multiple ways to call

Patch where the object is used.

For patch, scope matters.
- class decorator decorates all functions in a class
- function decorator lasts the entire function
- context manager lasts the indented block

start and stop is manually done.

Decorator example:
```py
    @patch('patch_source.Human') 
    def test_human_on_holiday(self, mock_human):
```

Lisa Roach - Demystifying the Patch Function - PyCon 2018
https://www.youtube.com/watch?v=ww1UsGZV8fQ


https://speakerdeck.com/pycon2018

# Todo:

fixture
cache
monitor log and respond to it
