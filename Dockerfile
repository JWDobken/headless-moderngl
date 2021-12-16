FROM python:3.8.0

WORKDIR /

RUN apt-get update
RUN apt install -y mesa-utils libegl1-mesa libegl1-mesa-dev xvfb libgl1-mesa-glx
ENV DISPLAY=:99.0
RUN echo "Xvfb :99 -screen 0 640x480x24 &" >> ~/.bashrc

COPY requirements.txt /

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt --upgrade

COPY ./src /src