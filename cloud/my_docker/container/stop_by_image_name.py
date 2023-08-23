import docker

# 创建 Docker 客户端
client = docker.from_env()

# 定义要停止的镜像名称
target_image_name = "your_image_name"

# 获取所有运行中的容器
running_containers = client.containers.list()

# 停止匹配目标镜像名称的容器
for container in running_containers:
    container_image_name = container.image.tags[0] if container.image.tags else ""

    if target_image_name in container_image_name:
        container.stop()
        print(f"Stopped container: {container.id} (Image: {container_image_name})")
