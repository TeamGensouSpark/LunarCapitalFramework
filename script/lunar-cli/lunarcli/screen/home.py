from typing import Union
from os import listdir
from Remilia.utils.cli import prompts
from Remilia.res import rPath, rFile
from lunarcli.base.tui import ScreenBase
from lunarcli.config.database import get_translation
from lunarcli.base.consts import CACHE_DIR

from shutil import rmtree

from .gradle import GradleExecuter, PageGradle
from .patch import PagePatch
from .promptlog import info


class PageHome(ScreenBase):
    def __init__(self, superscreen: Union[None, ScreenBase]) -> None:
        super().__init__(superscreen)

    def draw(self) -> None:
        prompts.ListPrompt(
            question=get_translation("chosetask.question"),
            choices=[
                prompts.Choice(
                    get_translation("home.gradle"), lambda: PageGradle(self).draw()
                ),
                prompts.Choice(
                    get_translation("home.patch"), lambda: PagePatch(self).draw()
                ),
                prompts.Choice(
                    get_translation("home.emptycache"),
                    lambda: self.draw()
                    if not prompts.ConfirmPrompt(
                        question=get_translation("home.emptycache.question"),
                        default_choice=False,
                    ).prompt()
                    else self.afterclean(
                        [
                            rFile("%s/%s" % (CACHE_DIR, name)).unlink()
                            if rPath("%s/%s" % (CACHE_DIR, name)).is_file()
                            else rmtree("%s/%s" % (CACHE_DIR, name))
                            for name in listdir(CACHE_DIR)
                        ]
                    ),
                ),
                prompts.Choice(
                    get_translation("home.auto"), lambda: self.autoConfigure()
                ),
            ],
        ).prompt().data()
        return super().draw()

    def afterclean(self, _):
        del _
        rFile("%s/.keep" % CACHE_DIR).write()
        self.draw()

    def autoConfigure(self):
        mge = GradleExecuter(True)
        mge.runTask()
        PagePatch(self).patch(True)
        mge.runTask("setupDecompWorkspace", "eclipse", "idea", "build")
        info("已完成")
        return self.draw()
