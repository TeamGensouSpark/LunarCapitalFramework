from os import system as _runcommand
from lunarcli.base.tui import ScreenBase
from Remilia.utils.cli import prompts

from lunarcli.config.database import get_translation
from lunarcli.screen.back import getBackfromS


class PageGradle(ScreenBase):
    def draw(self) -> None:
        prompts.ListPrompt(
            question=get_translation("chosetask.question"),
            choices=[
                prompts.Choice(
                    get_translation("gradle.run"),
                    lambda: PageGradleMultTasks(self, GradleExecuter(False)).draw(),
                ),
                prompts.Choice(
                    get_translation("gradle.runmirror"),
                    lambda: PageGradleMultTasks(self, GradleExecuter(True)).draw(),
                ),
                prompts.Choice(
                    get_translation("gradle.runcustom"),
                    lambda: PageGradleMultTasks(self, GradleExecuter(False)).draw(),
                ),
                prompts.Choice(
                    get_translation("gradle.runmirrorcustom"),
                    lambda: PageGradleMultTasks(self, GradleExecuter(True)).draw(),
                ),
                getBackfromS(self)
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
        self.executer.runTask(
            *[
                choice.data
                for choice in prompts.CheckboxPrompt(
                    question=get_translation("chosetask.question"),
                    choices=[
                        prompts.Choice(get_translation("gradle.init"), None),
                        prompts.Choice(
                            get_translation("gradle.setup"), "setupDecompWorkspace"
                        ),
                        prompts.Choice(get_translation("gradle.eclipse"), "eclipse"),
                        prompts.Choice(get_translation("gradle.idea"), "idea"),
                        prompts.Choice(get_translation("gradle.build"), "build"),
                    ],
                ).prompt()
                if choice.data != None
            ]
        )
        return self.back()


class PageGradleInput(ScreenBase):
    executer: GradleExecuter

    def __init__(
        self, superscreen: ScreenBase | None, executer: GradleExecuter
    ) -> None:
        super().__init__(superscreen)
        self.executer = executer

    def draw(self) -> None:
        self.executer.runTask(
            prompts.InputPrompt(
                question=get_translation("gradle.input"), default_text=""
            ).prompt()
        )
        return self.back()
