from fastapi import FastAPI, File, UploadFile
import jwt
from config import read_conf
import os
from file_managment import FileManagement


if read_conf("config.toml") is False:
    exit(0)
    
app = FastAPI()


@app.get("/list")
def get_list():
    manager = FileManagement()
    return manager.get_all_files_dirs()


@app.post("/list/file")
def upload_file():
    pass


@app.delete("/list/file")
def delete_file():
    pass
        

@app.post("/list/dir")
def upload_dir():
    pass


@app.delete("/list/dir")
def delete_dir():
    pass


def verify_token(token: str):
    data = jwt.decode(token, os.environ['jwt_salt'], algorithms=os.environ['jwt_algo'])

if __name__ =="__main__":
    app.run()