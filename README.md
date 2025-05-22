# CLS_InnoPrototype_AI-model
> This repository is for school inno.design project, will be delete after 1 week later.

## Deploy
Make sure you have >=python3.10 installed.

Verify by:

````bash
# /bin/bash
python3 --version
````

Clone the repository to any directory.(For example: /var/model/project)

### Create environment using conda
Install conda from conda's official website.

Refer to https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

### Create environment using python venv
Go to the project directory and run the following command to create a python virtual environment:
````bash
# /bin/bash
python3 -m venv .venv
source .venv/bin/activate
````

## Install libraries
Hance, install the libraries required with:

````bash
# /bin/bash
pip install -r requirements.txt
````

## Running
````bash
python main.py
````

# Trouble shooting

## Error during install pyaudio in macos
If you are in macos, an error should be raised during pip install pyaudio.

Fix it with install portaudio before install pyaudio.

We suggest install it with [brew package manager](https://brew.sh)
````zsh
brew install portaudio
pip install -r requirement.txt
````

## Whisper has no attribute load_model
If you are in macos, whisper raise error to unknown reason(idk actually).

Reinstall whisper with github package can solve it.

````zsh
pip install git+https://github.com/openai/whisper.git
````

## SSL certificate_verify_failed
If you are in macos or linux, a SSL verify failed raised while installing whisper model.

Disable this error message can solve it as well.

Insert the following lines into the first line of main.py
````python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
````
