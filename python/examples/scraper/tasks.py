from celery import Celery
from task_scrape_ip_addresses import scrape_ip
from task_http_response import url_ok

# app = Celery("tasks", broker="amqp://localhost")
# app = Celery("tasks", backend="rpc://", broker="pyamqp://")
app = Celery("tasks", backend="redis://localhost", broker="pyamqp://")

# python -m celery -A tasks worker --loglevel=INFO
# or on Windows:
# python -m celery -A tasks worker --pool=solo -l info

"""
Following are some of the registered tasks that can be run:
"""


@app.task
def add(x, y):
    return x + y


@app.task
def check_site(url: str):
    return url_ok(url)


@app.task
def hello():
    return "hello world"


@app.task
def scrape(ip):
    return scrape_ip(ip)


"""
from tasks import *
from tasks import add    # close and reopen to get updated 'app'
>>> result = add.delay(4, 4)
>>> result.ready()
True
>>> result.get(timeout=1)
8


result = check_site.delay("http://nu.nl")
result.get(timeout=1)
"""
