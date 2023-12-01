# kafka

kafka

## use

### Used by pyenv virtualenv

    pyenv virtualenv  3.11.6 kafka
    pyenv activate kafka
    python -m pip install --upgrade pip
    cd message_queue/my_kafka
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

### docker-compose run kafka

    see this github repository,and get docker-compose;
    https://github.com/bitnami/containers/tree/main/bitnami/kafka
    https://github.com/bitnami/containers/blob/main/bitnami/kafka/docker-compose.yml
    https://github.com/bitnami/containers/blob/main/bitnami/kafka/docker-compose-cluster.yml

    then execute commond:
    docker-compose up -d

### Related documents

    kafka-github: https://github.com/apache/kafka
    kafka-doc: https://kafka.apache.org/documentation/


## project

### kafka_base_demo

#### introduce

kafka Introduction to Operation Cases

#### start-up

## uninstall

    pyenv virtualenv-delete kafka
