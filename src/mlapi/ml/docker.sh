#!/bin/bash
docker build -t mlapi .
docker run -d -p 8888:8888 --name ml-mlapi mlapi

