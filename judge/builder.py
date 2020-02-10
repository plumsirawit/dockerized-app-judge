import docker
client = docker.from_env()
images = client.images

def build():
    # build image from the cloned directory
    return None