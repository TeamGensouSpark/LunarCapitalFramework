from Remilia.mixin import Inject, At, Mixin, EnumCOChar
from Remilia.utils.cli import prompts


@Mixin(prompts.ListPrompt)
class MixinListPrompt:
    @Inject.withValue(
        at=At.END,
        method="__init__",
        namespace=prompts.list.__dict__
    )
    def oninit(self):
        self.question_mark = "[@]"


@Mixin(prompts._base.BasePrompt)
class MixinBasePrompt:
    @Inject.withValue(
        at=At.INSERT,
        method="prompt",
        insertline=-2,
        namespace=prompts._base.__dict__,
    )
    def onprompt():
        EnumCOChar.SPACE4;print("Exit with keyboard break!")
        EnumCOChar.SPACE4;exit(0)
