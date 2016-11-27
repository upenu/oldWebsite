FROM debian:jessie
MAINTAINER Brian Sang
# install python, git, wget, mysql stuff
RUN apt-get update && apt-get install -y \
                gcc \
                gettext \
                git \
                libmysqlclient-dev \
                mysql-client-5.5 \
                python3 \
                python3-dev \
                python3-pip \
                wget \
        --no-install-recommends && rm -rf /var/lib/apt/lists/*

# pip3 requirements
RUN wget https://raw.githubusercontent.com/upenu/website/master/requirements.txt
RUN pip3 install -r requirements.txt
RUN /bin/bash -c 'rm requirements.txt;'
# expose port
EXPOSE 8000
