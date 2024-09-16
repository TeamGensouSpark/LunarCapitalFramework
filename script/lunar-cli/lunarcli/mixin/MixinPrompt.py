from Remilia.mixin import Inject, At, Mixin, EnumCOChar
from Remilia.utils.cli import prompts
from Remilia import log as log


@Mixin(prompts.ListPrompt)
class MixinListPrompt:
    @Inject.withValue(at=At.END, method="__init__", namespace=prompts.list.__dict__)
    def oninit(self):
        self.question_mark = "[@]"


@Mixin(prompts._base.BasePrompt)
class MixinBasePrompt:
    @Inject.withValue(
        at=At.INSERT, method="prompt", insertline=-2, namespace=prompts._base.__dict__
    )
    def onprompt():
        #!EnumCOChar.SPACE4;from lunarcli.config.database import get_translation
        #!EnumCOChar.SPACE4;from lunarcli.screen.promptlog import error
        #!EnumCOChar.SPACE4;error(get_translation("global.exit"))
        #!EnumCOChar.SPACE4;exit(0)
        EnumCOChar.DELETELINE;
