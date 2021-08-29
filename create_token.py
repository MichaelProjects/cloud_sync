import jwt
import time
import os
from config import read_conf

def create_token():
    read_conf("config.toml")
    token = jwt.encode({"creationTime": str(time.time())},os.environ['jwt_salt'], algorithm=os.environ['jwt_algo'])
    print(token.decode("UTF-8"))

if __name__ == '__main__':
    create_token()