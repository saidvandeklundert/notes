"""
python -m pytest .\mocking_input_data.py

python .\mocking_input_data.py

"""
from unittest.mock import Mock

# instantitate the Mock:
json = Mock()

json.loads('{"a": "b"}')

# Check how often the Mock method was called:
json.loads.call_count

# Display information about the last call:
json.loads.call_args

# List of loads() calls:
json.loads.call_args_list
json.loads('{"b": "c"}')
json.loads.call_args_list

# List of calls to json's methods (recursively):
json.method_calls

# specify a method and it's return value:
json.dumps.return_value = '{"a": 1}'

