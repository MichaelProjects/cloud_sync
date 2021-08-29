import toml
import logging
import sys
import os


def read_conf(conf_path: str) -> bool:
    # returns bool true for sucessful and false for error
    conf_data = {}
    try:
        with open(conf_path) as file:
            logging.debug("loading data")
            conf_data = toml.load(file)
    except Exception as e:
        logging.error(e)
        return False

    logging.debug("set env values")
    # set values from conf as env values
    os.environ["jwt_salt"] = conf_data["jwt_salt"]
    os.environ["storage_path"] = conf_data["storage_path"]
    os.environ["jwt_algo"] = conf_data["jwt_algo"]
    os.environ["server_addresse"] = conf_data["server_addresse"]

    return True