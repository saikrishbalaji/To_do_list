from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount('/ui',StaticFiles(directory='ui'), name = 'ui')