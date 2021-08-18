from yaml import load
from yaml import FullLoader
from collections.abc import Mapping
import re


class Content(Mapping):
    __delimiter = {r"^(?:-|\+){3}\s*$"}
    __regex = re.compile(__delimiter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _ = Content.__regex.split(string, 2)
        fm = _
        content = _
        load(fm, Loader=FullLoader)
        return cls(metadata, content)



