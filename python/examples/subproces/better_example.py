"""
python .\better_example.py "ls -ltr"
python .\better_example.py "ping www.google.com"
"""
import subprocess
import shlex
import sys
command = sys.argv
args = shlex.split(command[1])
print(args)
try:
    output = subprocess.run(args,capture_output=True)    
except subprocess.CalledProcessError as e:
    print("Error: ", e.output)

print(output)
output.args
output.returncode
output.stdout
output.stderr