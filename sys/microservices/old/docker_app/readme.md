Instructions: 
 
```
# build it
docker build -t orders:1.0 .
# run it
docker run --name='api' --hostname='api' --env DB_URL=sqlite:///orders.db -v C:\dev\notes\sys\microservices\docker_app\orders.db:\orders\orders.db -p 8000:8000 -it orders:1.0 
```