import subprocess

# running a quicky:
try:
    out = subprocess.check_output(["ping", "www.google.com"])
    print(out)
except subprocess.CalledProcessError as e:
    print("Error: ", e.output)
