# flink

flink

## use

### install requirements

    cd big_data/flink
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

### docker-compose run flink

1. docker build -f PyFlink-DockerFile --tag pyflink:latest .
2. run docker-compose common
   - docker-compose -f docker-compose-application-mode.yaml up -d
   - docker-compose -f docker-compose-session-mode.yaml up -d

### Related documents

    flink-github: https://github.com/apache/flink
    flink-doc: https://flink.apache.org/documentation/
    flink-python-sdk-doc: https://nightlies.apache.org/flink/flink-docs-release-1.18/docs/dev/python/overview/\
    flink-python-sdk-zh_doc:https://nightlies.apache.org/flink/flink-docs-release-1.18/zh/docs/ops/rest_api/

## project

### flink_base_demo

#### introduce

flink Introduction to Operation Cases

#### start-up

## uninstall

    pyenv virtualenv-delete flink
