from Remilia.structdb import DataBase,YamlStruct
from Remilia.base.rtypes import VT

CONFIG_NAME = "config.yaml"

LunarDBroot = DataBase("./script/data",struct=YamlStruct)

translation=LunarDBroot.cget_cate("i18n")

config_f = LunarDBroot.cget_file(CONFIG_NAME)

def get_config(name:str) -> VT:
    return LunarDBroot.readkv(CONFIG_NAME,name)

def write_config(name:str,value:VT) -> "write_config":
    LunarDBroot.writekv(CONFIG_NAME,name,value)
    return write_config

def reset_config() -> None:
    write_config("i18n","zh_cn.yaml")
    
def get_translation(key:str) -> str:
    return translation.readkv(get_config("i18n"),key)