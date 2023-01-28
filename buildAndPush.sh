#!/bin/bash
docker build -t miedz .
docker tag miedz passarinho/miedz
docker push passarinho/miedz
