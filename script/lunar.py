from Remilia import log as _
from Remilia.res import rPath
from os import chdir

if rPath(".").absolute().to_string().split("\\")[-1] == "script":
    print(rPath(".").absolute().parent.absolute())
    chdir(rPath(".").absolute().parent.absolute())

from lunarcli.config.database import *
from lunarcli.screen.home import PageHome

print(_.Fore.LIGHTGREEN_EX + "[!] 输入CTRL+C可以快速退出程序" + _.Style.RESET_ALL)

# reset_config()
PageHome(None).draw()
