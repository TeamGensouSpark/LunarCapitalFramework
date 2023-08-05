from os import system as _runcommand
from lunarcli.base.tui import ScreenBase
from Remilia.utils.cli import prompts

from lunarcli.config.database import get_translation

from Remilia.base.rtypes import Pair


class PageGradle(ScreenBase):
    def draw(self) -> None:
        prompts.ListPrompt(
            question=get_translation("chosetask.question"),
            choices=[
                prompts.Choice(get_translation(items_pair.name), items_pair.value)
                for items_pair in [
                    Pair(
                        "gradle.run",
                        lambda: PageGradleMultTasks(self, GradleExecuter(False)).draw(),
                    ),
                    Pair(
                        "gradle.runmirror",
                        lambda: PageGradleMultTasks(self, GradleExecuter(True)).draw(),
                    ),
                ]
            ],
        ).prompt().data()
        return self.back()


class GradleExecuter:
    def __init__(self, mirror: bool) -> None:
        self.commands = ["gradlew"]
        if mirror:
            self.commands.append("mirrorSetup")

    def runTask(self, *commands) -> None:
        command = self.commands
        command.extend(commands)
        _runcommand(" ".join(command))


class PageGradleMultTasks(ScreenBase):
    executer: GradleExecuter

    def __init__(
        self, superscreen: ScreenBase | None, executer: GradleExecuter
    ) -> None:
        super().__init__(superscreen)
        self.executer = executer

    def draw(self) -> None:
        prompts.ListPrompt(
            question=get_translation("chosetask.question"),
            choices=[
                prompts.Choice(get_translation(items_pair.name), items_pair.value)
                for items_pair in [
                    Pair("gradle.init", lambda: self.executer.runTask()),
                    Pair(
                        "gradle.runmirror",
                        lambda: self.executer.runTask("setupDecompWorkspace"),
                    ),
                ]
            ],
        ).prompt().data()
        return self.back()


class PageGradleInput(ScreenBase):
    executer: GradleExecuter

    def __init__(
        self, superscreen: ScreenBase | None, executer: GradleExecuter
    ) -> None:
        super().__init__(superscreen)
        self.executer = executer

    def draw(self) -> None:
        prompts.InputPrompt(question="")
        return self.back()
