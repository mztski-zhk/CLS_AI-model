> This repository is for school inno.design project.

## Deploy
Make sure you have >=python3.10 installed.

Verify by:

````bash
# /bin/bash
python3 --version
````

Clone the repository to any directory.(/var/model/project for example)

### Create environment using conda
Install conda from conda's official website.

Refer to https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

### Create environment using python venv
Go to the project directory and run the following command to create a python virtual environment:
````bash
# /bin/bash
python3 -m venv .venv && \
source .venv/bin/activate
````

## Install libraries
Hance,install the libraries with

````bash
# /bin/bash
pip install -r requirements.txt
````

## Running
````bash
python main.py
````
