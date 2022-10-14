# algos
My algorithm studies

## Pre-reqs
- intellij
- docker
- git

## Instructions
These instructions will take you through installation of necessary tools all the way to running the project, unit tests,
and testing the lambda in a way similar to its live runtime.
1. [Install pyenv](#install-pyenv)
1. [Install project specific python version](#install-project-specific-python-version)
1. [Install PDM](#3)
1. [Install Dependencies](#deps)


### Install pyenv <a name="install-pyenv"></a>
#### Mac/Linux
    curl https://pyenv.run | bash
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
    echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
    source ~/.bash_profile

### Install project specific python version <a name="install-project-specific-python-version"></a>
(This can take several minutes, patience...)

    pyenv install $(cat .python-version)
    pyenv local $(cat .python-version)

### Install PDM (Python Dependency Manager)<a name="3"></a>
    pip install --user pdm==2.1.5
    echo 'export PATH=$PATH:~/.local/bin' >> ~/.bash_profile
    source ~/.bash_profile
    pdm config check_update false
    pdm config python.use_venv false

PDM (Python Dependency Manager) is a "modern" python package manager akin to npm for node.
Specifically, it installs dependencies into a folder `__pypackages__` which is a python standard as of
PEP-582 (still in draft). This is exciting because it eliminates the reliance on python virtual envs. You can read the
PEP for the motivation of moving away from venvs in general.

### Install dependencies <a name="deps"></a>
    pdm run install
