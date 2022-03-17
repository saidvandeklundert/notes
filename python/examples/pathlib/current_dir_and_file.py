import pathlib


this_script_file_name = pathlib.Path(__file__).parent.as_posix()
print(this_script_file_name)

dir_this_file_is_in = pathlib.Path(__file__).as_posix()
print(dir_this_file_is_in)
