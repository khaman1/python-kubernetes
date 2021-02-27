import redis
import os
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis-clusterip-srv', port=6379)


#################################
#################################
APP_VERSION = os.environ['APP_VERSION']
URL_PREFIX  = os.environ['URL_PREFIX']


#################################
#################################
from .init import *