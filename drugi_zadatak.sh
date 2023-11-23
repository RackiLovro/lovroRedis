#!/bin/bash

docker swarm init

docker stack deploy -c docker-compose.yml lovro

docker service scale lovro_increment_service=10