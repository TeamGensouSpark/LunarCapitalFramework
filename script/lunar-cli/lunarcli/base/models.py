from pydantic import BaseModel

class PatchInfo(BaseModel):
    name:str
    package:str
