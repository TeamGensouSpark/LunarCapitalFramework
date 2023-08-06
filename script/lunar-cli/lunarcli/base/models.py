from typing import Dict, List
from pydantic import BaseModel

class PatchInfo(BaseModel):
    name:str
    package:str
    manifest:List[Dict[str,str]]
