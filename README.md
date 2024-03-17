# algos
My algorithm studies

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
    pip install --user pdm==2.12.4
    echo 'export PATH=$PATH:~/.local/bin' >> ~/.bash_profile
    source ~/.bash_profile

### Install dependencies <a name="deps"></a>
    pdm install
