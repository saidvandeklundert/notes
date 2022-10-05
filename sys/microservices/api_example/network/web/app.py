from fastapi import FastAPI

app = FastAPI(debug=True)


from web.api import humans
from web.api import network
