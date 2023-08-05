from Remilia.mixin import Inject, At, Mixin, EnumCOChar
from Remilia.utils.cli import prompts


from typing import List, Optional, Callable
from gettext import gettext as _


@Mixin(prompts.ListPrompt)
class MixinListPrompt:
    @Inject.withValue(
        at=At.END,
        method="__init__",
        namespace={
            "List": List,
            "Choice": prompts.Choice,
            "RT": prompts._base.RT,
            "Optional": Optional,
            "Callable": Callable,
            "_": _,
        },
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
