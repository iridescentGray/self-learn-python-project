# Playwright

Playwright integration docker

## start up

### offical image

#### common

    # 通常情况下,这样使用下述方式启动
    cd crawler/my_playwright/integration_docker/offical
    docker-compose-offical.yml

#### seccomp

    # 在不受信任的网站上，建议使用单独的用户结合 seccomp 配置文件启动浏览器。
    cd crawler/my_playwright/integration_docker/offical
    docker-compose -f docker-compose-offical-seccomp.yml  up -d


### use_offical_image

    cd crawler/my_playwright/integration_docker/use_offical_image
    # build docker image
    docker build -t playwright_python:1.0.0 .
    docker-compose -f docker-compose-custom.yml  up -d
    # 进入docker镜像，开启虚拟环境
    . venv/bin/activate
    # 执行程序
    python custom_script.py

### custom_dockerfile
    cd crawler/my_playwright/integration_docker/custom_image
    # build docker image
    docker build -t self_playwright:v1 .
    docker-compose  up -d
    # 执行程序
    python custom_script.py

## Related documents

    playwright-python-docker:   https://playwright.dev/python/docs/docker
