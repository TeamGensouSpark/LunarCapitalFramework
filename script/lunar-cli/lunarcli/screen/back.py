from lunarcli.base.tui import ScreenBase
from lunarcli.config.database import get_translation
from Remilia.utils.cli import prompts

def getBackfromS(screen:ScreenBase):
    return prompts.Choice(get_translation("global.back"),screen.back)