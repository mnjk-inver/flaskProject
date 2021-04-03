#!/usr/bin/bash

sudo docker run -it -d -p 80:5000 --restart always --name=linux-check teucer12/linux-check
