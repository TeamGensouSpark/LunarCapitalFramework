from lunarcli.base.consts import ROOT_DIR
from lunarcli.base.models import PatchInfo
from lunarcli.base.tui import ScreenBase
from lunarcli.config.database import get_translation

from Remilia.utils.cli import prompts
from Remilia.res import rFile
from json import loads


class PagePatch(ScreenBase):
    def draw(self) -> None:
        if prompts.ConfirmPrompt(question=get_translation("patch.confirm")).prompt():
            self.patch()
        return self.back()

    def patch(self):
        patchinfo = self.getInfo()
        print(patchinfo)
    
    def findJar(self):
        pass
    
    def getInfo(self):
        _tmp = loads(rFile("%s/data/class/package.json" % ROOT_DIR).text)
        return PatchInfo(
            name=_tmp["name"], package=_tmp["package"], manifest=_tmp["manifest"]
        )


