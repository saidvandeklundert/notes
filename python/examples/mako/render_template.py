from mako.template import Template
import pathlib


this_dir = pathlib.Path(__file__).parent.as_posix()

mytemplate = Template(filename="mako_template.txt", module_directory=this_dir)
print(mytemplate.render())
