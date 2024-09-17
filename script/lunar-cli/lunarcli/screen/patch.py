from lunarcli.base.consts import (
    ROOT_DIR,
    JAR_TOOL,
    GITHUB_MIRROR,
    JAR_TOOL_URL,
    CLASS_DIR,
)
from lunarcli.base.models import PatchInfo
from lunarcli.base.tui import ScreenBase
from lunarcli.config.database import get_translation
from lunarcli.config.env import USERPROFILE
from lunarcli.screen.promptlog import error

from Remilia.utils.cli import prompts
from Remilia.res import rFile, rPath, rDir
from os import system as _runcmd
from json import loads
from shutil import rmtree

from requests import get


class PagePatch(ScreenBase):
    def draw(self) -> None:
        if prompts.ConfirmPrompt(question=get_translation("patch.confirm")).prompt():
            self.patch()
        return self.back()

    def patch(self, undermirror=False):
        patchinfo = self.getInfo()
        archive = self.findJar(patchinfo.package, patchinfo.name)
        self.prepareInject(undermirror)
        SZExecuter.addFile("%s/%s" % (CLASS_DIR, patchinfo.name), archive)
        try:
            rmtree(USERPROFILE + "/.gradle/caches/jars-9")
        except Exception:
            pass

    def findJar(self, package: str, name: str) -> str:
        result = list(
            rDir(
                USERPROFILE + "/.gradle/caches/modules-2/files-2.1/%s" % package
            ).rglob("%s-*.jar" % name)
        )
        if len(result) == 0:
            error(get_translation("global.error.notfoundrfg"))
            self.back()
        if len(result) != 1:
            return (
                prompts.ListPrompt(
                    question=get_translation("patch.multirfg"),
                    choices=[prompts.Choice(str(res), None) for res in result],
                )
                .prompt()
                .name
            )
        else:
            return str(result[0])

    def prepareInject(self, undermirror: bool = False):
        if not rPath(JAR_TOOL).exists():
            if not undermirror:
                resp = get(
                    prompts.ListPrompt(
                        question=get_translation("patch.requesttool.question"),
                        choices=[
                            prompts.Choice(
                                get_translation("patch.requesttool.raw"),
                                lambda: JAR_TOOL_URL,
                            ),
                            prompts.Choice(
                                get_translation("patch.requesttool.mirror"),
                                lambda: GITHUB_MIRROR + JAR_TOOL_URL,
                            ),
                            prompts.Choice(
                                get_translation("patch.requesttool.custom"),
                                lambda: prompts.InputPrompt(
                                    question=get_translation(
                                        "patch.requesttool.custom.question"
                                    ),
                                    default_text=GITHUB_MIRROR + JAR_TOOL_URL,
                                ).prompt(),
                            ),
                        ],
                    )
                    .prompt()
                    .data()
                )
            else:
                resp = get(GITHUB_MIRROR + JAR_TOOL_URL)
            rFile(JAR_TOOL).write_bytes(resp.content)

    def getInfo(self):
        _tmp = loads(rFile("%s/data/class/package.json" % ROOT_DIR).text)
        return PatchInfo(name=_tmp["name"], package=_tmp["package"])


class SZExecuter:
    @staticmethod
    def addFile(getfrom: str, addto: str):
        _runcmd(" ".join([rPath(JAR_TOOL).absolute().to_string(), "a", addto, getfrom]))
