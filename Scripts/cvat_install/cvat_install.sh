#! /bin /bash

sudo git clone https://github.com/opencv/cvat.git
sudo apt-get install docker-compose
sudo docker-compose build
sudo docker-compose up -d
