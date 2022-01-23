"""
Common shell utilities (hence shutil?)
"""
import shutil


# remote tree (so all files and dirs under specified dir)
# shutil.rmtree('/var/logs')

# copy tree and all files and dirs under specified dir:
# shutil.copytree('/var/logs', '/tmp/logs')

# copy file
# shutil.copyfile('data.db', 'archive.db')

# move a file or a directory:
# shutil.move('/build/executables', '/tmp')
# shutil.move('/build/executables/test.py', '/tmp/test.py')

# Return disk usage statistics in bytes about the given file/path:
shutil.disk_usage("C:")