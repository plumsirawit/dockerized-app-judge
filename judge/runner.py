import docker
client = docker.from_env()
images = client.images

def run():
    # run container from the built image