# FastAPI Project Example

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Requirements

We need to use a virtual environment to install the dependencies and run the application.
In this case we will use conda to create a virtual environment.

```bash
conda create -n fastapi-example python=3.8
conda activate fastapi-example
```

:warning: **Note** If you are using windows, run the terminal using CMD not the powershell because not take the environments variables and not activate the virtual environment.

### Install dependencies

Install fastapi and save it in the requirements.txt file

- `pip install fastapi`
- `pip install uvicorn`
- `pip freeze > requirements.txt`

**uvicorn** is a lightning-fast ASGI server implementation, using uvloop and httptools.

Then, we can install the dependencies using the requirements.txt file

```bash
pip install -r requirements.txt
```

To run the application we need to use the uvicorn command

```bash
uvicorn app:app
```

**app** is the name of the file and **app** is the name of the variable that contains the FastAPI instance.

To avoid executed the uvicorn command every time we make a change in the code, we can use the **--reload** flag

```bash
uvicorn app:app --reload
```
