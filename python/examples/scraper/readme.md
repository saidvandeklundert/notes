```
docker run -d -p 6379:6379 redis
docker run -d -p 5672:5672 rabbitmq
docker ps
```


```
pip install celery
pip install -U "celery[redis]"
```


```
python -m celery -A tasks worker --loglevel=INFO
```
Or on Windows, run it with 1 thread:
```
python -m celery -A tasks worker --pool=solo -l info
```