from model import *
from jinja2 import Environment, FileSystemLoader


def main():
    file_loader = FileSystemLoader("templates")
    env = Environment(loader=file_loader)

    template = env.get_template("template.j2")
    output = template.render(data={"data": "data"})
    print(output)


if __name__ == "__main__":

    main()
