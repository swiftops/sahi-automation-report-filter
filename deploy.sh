#!/bin/bash
export HOST_IP=10.0.2.250
cd /home/ubuntu/microservice
docker-compose scale sahiservice=0
docker rm $(docker ps -q -f status=exited)
docker rmi -f swiftops/sahi_service && docker pull swiftops/sahi_service && docker-compose up -d --remove-orphans
