from typing import Any
from os import environ

class SystemEnv:
    def __getattr__(self,key:str) -> str:
        if environ.__contains__(key):
            return environ[key]
        return None

SystemEnv = SystemEnv()
USERPROFILE = SystemEnv.USERPROFILE