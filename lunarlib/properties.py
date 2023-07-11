from Remilia.res import rFile

from .utils import uformat


class GradleProperties:
    def __init__(self,path) -> None:
        self.path=path
    
    @property
    def properties(self):
        properties_group={}
        for line in [line for line in [line for line in rFile(self.path).text.splitlines() if len(line)>0] if line[0] != '#']:
            slices=line.split("=")
            name=uformat.extract_escape(slices[0])
            slices.pop(0)
            value=uformat.extract_escape("=".join(slices))
            if value == "false":
                value=False
            elif value == "true":
                value=True
            properties_group.update({name:value})