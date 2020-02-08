FROM ubuntu:18.04
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# For Python 3 and Flask
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-dev
RUN pip3 install Flask

# For Git
RUN apt-get install -y git
RUN pip3 install gitpython

# For Docker
RUN apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
RUN apt-get update
RUN apt-get install -y docker-ce
RUN pip3 install docker

# Main App
ADD judge /judge
WORKDIR /judge
CMD ["env","FLASK_APP=app.py","flask","run","--host=0.0.0.0","--port=8080"]
EXPOSE 8080