
from lunarcli.base.tui import ScreenBase


class PagePatch(ScreenBase):
    def draw(self) -> None:
        return self.back()