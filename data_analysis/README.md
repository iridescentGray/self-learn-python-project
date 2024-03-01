# data_analysis

data_analysis demo

## Environmental construction

### Used by pyenv virtualenv plugin

    pyenv virtualenv  3.10.9 data_analysis_hello_world
    pyenv activate data_analysis_hello_world
    python -m pip install --upgrade pip
    cd data_analysis
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

### Used by poetry
    poetry install
    poetry shell

## uninstall

    pyenv deactivate data_analysis_hello_world
    pyenv virtualenv-delete data_analysis_hello_world
