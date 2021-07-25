# NPM Dependent Packages Analyzer, Ron Raifer.
## _An Assignment Given By [Snyk.io](https://snyk.io/)_
[![Snyk](https://www.pulseconferences.com/wp-content/uploads/2020/04/snyk-logo-black.png "Snyk")](http://snyk.io "Snyk")

This assignment was given to me by Snyk.io, to test my capabilities.\
I have been asked to implement a web service which retrieves dependencies of a given npm package, and serves REST API requests.\
The application can also monitor the server, to check if it's availiable.
During the implementation, I searched for the most relevant tools to accomplish the best results. It was a great opportunity to learn new technologies!.  

##### Source Code Available [HERE](https://github.com/RonRaifer/NPM-Dep)

## Tech

The NPM dependency analyzer uses a number of open source projects to work properly:

- [Python](https://www.python.org/) - the programming language
- [FastAPI](https://fastapi.tiangolo.com/) - fast (high-performance), web framework for building APIs with Python 3.6+
- [Redis](https://redis.io/) - an amazing in-memory data structure store, used as a database, cache, and message broker.
- [pydantic](https://pydantic-docs.helpmanual.io/) - enforces type hints at runtime, and provides user friendly errors when data is invalid
- [Pickle](https://docs.python.org/3/library/pickle.html) - implements binary protocols for serializing and de-serializing a Python object structure.
- [uvicorn](https://www.uvicorn.org/) - a lightning-fast ASGI server implementation, using uvloop and httptools


## Installation

***Note***
- This project requires [Python](https://www.python.org/) v3.6+ to run.
- Make sure you have Redis installed and running on your machine, for more details, refer to [Redis Download](https://redis.io/download).

**Installation Instructions:**

Clone the project or download it directly:
```bash
git clone https://github.com/RonRaifer/NPM-Dep.git
cd NPM-Dep
```

Install the dependencies, using [pip](https://pypi.org/project/pip/), via running the next command:
```bash
 pip install -r requirements.txt
```

## Running the App

This application works in two ways: 
- running `main.py` from your IDE or CMD.
- via terminal using `uvicorn`, running the command ```uvicorn main:app --reload```.


## Accessing and Using the API

*If you are into Debugging, it is recommended to use [Insomnia](https://insomnia.rest/) or equivalent.*

**The request can be served in two ways: via the interactive API (Swagger) or via the address bar.**

#### Interactive API (Swagger)

To access the interactive API documentation, make sure the app is running, and then navigate to:
```bash 
http://127.0.0.1:8000/docs
```
Now you can choose whether you like to just Monitor, or getting the dependencies. An example "degifted" below:
![how_to_docs](https://raw.githubusercontent.com/RonRaifer/ronraifer.github.io/main/NPM-Dep-docs/how_to_docs.gif)

#### Address Bar

Make sure the programs is running. Now, you can choose wether you want to see the root, monitor, or get dependencies for the desired package:
```bash 
http://127.0.0.1:8000/
http://127.0.0.1:8000/npmMonitor
http://127.0.0.1:8000/retrieveDependencies/?package_name=<NAME>&version_or_tag=<VERSION>
```
**Example of retrieving dependencies:**

Retrieve dependencies for `express` package, with latest version:
```bash
http://127.0.0.1:8000/retrieveDependencies/?package_name=express&version_or_tag=latest
```
![how_to_address](https://raw.githubusercontent.com/RonRaifer/ronraifer.github.io/main/NPM-Dep-docs/how_to_address.gif)

## Future Improvements

- For compactness: add TTL to each package, and reset the TTL offset upon user request, that indicated the demand of the package.


## Contact Info
Mail me: ronraifer@gmail.com


