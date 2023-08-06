from typing import Union
from Remilia.utils.cli import prompts
from Remilia.base.rtypes import Pair
from lunarcli.base.tui import ScreenBase
from lunarcli.config.database import get_translation

from .gradle import PageGradle
from .patch import PagePatch

class PageHome(ScreenBase):
    def __init__(self, superscreen: Union[None, ScreenBase]) -> None:
        super().__init__(superscreen)

    def draw(self) -> None:
        prompts.ListPrompt(
            question=get_translation("chosetask.question"),
            choices=[
                prompts.Choice(get_translation(items_pair.name), items_pair.value)
                for items_pair in [
                    Pair("home.gradle", lambda: PageGradle(self).draw()),
                    Pair("home.patch", lambda: PagePatch(self).draw()),
                ]
            ],
        ).prompt().data()
        return super().draw()
