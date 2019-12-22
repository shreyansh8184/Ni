import logging
from database.mongo import cli

cli = cli["NiceGrill"]["Settings"]


def set_city(city):
    return cli.insert_one({"City": city})

def set_path(path):
    return cli.insert_one({"Path": path})

def set_pack(pack):
    return cli.insert_one({"Pack": pack})

def set_prefix(prefix):
    return cli.insert_one({"Prefix": prefix})

def set_restart(chat, msg):
    return cli.insert_one({"Restart": True, "Chat": chat, "Message": msg})

def set_asset(id):
    return cli.insert_one({"Asset": id})

def set_gfolder(id):
    return cli.insert_one({"GFolder": id})

def check_city():
    return ("" if not cli.find_one({"City": {"$exists": True}})
        else cli.find_one({"City": {"$exists": True}})["City"])

def check_pack():
    return ("" if not cli.find_one({"Pack": {"$exists": True}})
        else cli.find_one({"Pack": {"$exists": True}})["Pack"])

def check_path():
    return ("./" if not cli.find_one({"Path": {"$exists": True}})
        else cli.find_one({"Path": {"$exists": True}})["Path"])
    
def check_prefix():
    return ("." if not cli.find_one({"Prefix": {"$exists": True}})
        else cli.find_one({"Prefix": {"$exists": True}})["Prefix"])

def check_restart():
    return (False if not cli.find_one({"Message": {"$exists": True}})
        else cli.find_one({"Message": {"$exists": True}}))

def check_asset():
    return (False if not cli.find_one({"Asset": {"$exists": True}})
        else cli.find_one({"Asset": {"$exists": True}})["Asset"])

def check_gfolder():
    return (False if not cli.find_one({"GFolder": {"$exists": True}})
        else cli.find_one({"GFolder": {"$exists": True}})["GFolder"])

def delete(obj):
    if obj == "Message" or obj == "Asset" or obj == "Restart":
        cli.delete_one({obj: True})
        cli.delete_one({obj: False})
        return
    return cli.delete_one({obj: {"$regex": "."}})
        
