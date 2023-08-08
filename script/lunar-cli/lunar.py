from Remilia import log as _
from Remilia.res import rPath
from os import chdir

if rPath(".").absolute().to_string().split("\\")[-1] == "lunar-cli":
    chdir(rPath(".").absolute().parent.absolute().parent.absolute())

from lunarcli.config.database import *
from lunarcli.screen.promptlog import *
from lunarcli.screen.home import PageHome

info(get_translation("global.exittip"))

# reset_config()
PageHome(None).draw()
