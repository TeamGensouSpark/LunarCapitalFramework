from Remilia.mixin import OverWrite,Mixin

from zipfile import ZipFile

@Mixin(ZipFile)
class MixinZipFile:pass