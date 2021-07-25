import json
import pickle
import redis
import uvicorn
from time import sleep
from datetime import timedelta
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from simple_background_task import BackgroundTask
from simple_background_task import defer
from fastapi import FastAPI, BackgroundTasks, HTTPException
from starlette import status
from data_models import NpmDependencies

is_alive = False
npm_server = 'https://registry.npmjs.org/'
r = redis.Redis(
    host='localhost',
    port='6379')

app = FastAPI()
BackgroundTask().start()


def get_json_data(url: str) -> dict:
    """
    Loads data from url, and converts to a Json format.

    :param url: The site address.
    :return: dict contains the formatted data.
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


def check_npm_alive():
    """
    Checks whether the server can be accessed, and updates the flag.
    """
    global is_alive
    while True:
        try:
            urlopen(npm_server)
            is_alive = True     # server is up
        except URLError:
            is_alive = False    # server is down
        sleep(1800)  # check server uptime each 30 minutes


defer(
    func=check_npm_alive,
    arguments={}
)


def update_redis(key: str, version_or_tag: str, data: dict):
    """
    Stores data in Redis for a given key.

    :param key: The key value for the data to be be saved in. In form of package_name@version.
    :param version_or_tag: The version of the package
    :param data: The desired data to be stored in redis.
    """
    r.set(key, pickle.dumps(data))
    if version_or_tag == 'latest':  # if latest, add and set ttl.
        r.expire(key, timedelta(minutes=60))  # ttl for latest version


@app.get("/")
async def home():
    return {"Hello": "Snyk.io"}


@app.get("/retrieveDependencies", response_model=NpmDependencies)
async def retrieve_dependencies(package_name: str, version_or_tag: str, background_tasks: BackgroundTasks):
    if not is_alive:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Server is down, check again in an hour."
        )
    key = package_name + '@' + version_or_tag
    if r.exists(key):
        return NpmDependencies(**pickle.loads(r.get(key)))   # returns the data
    else:
        try:
            url = npm_server + package_name + '/' + version_or_tag
            data = get_json_data(url)
            background_tasks.add_task(update_redis, key, version_or_tag, data)
        except HTTPError:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"There was an error retrieving dependencies for the package entered."
            )
    return NpmDependencies(**data)


@app.get("/npmMonitor")
async def npm_monitor():
    return {"Server Status": "UP" if is_alive else "DOWN"}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
