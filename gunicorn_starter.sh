#!/bin/bash

authbind gunicorn -w 4 -b 0.0.0.0:80 webappPOC_2:app
