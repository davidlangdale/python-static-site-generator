import re
from abc import ABC
from copy import deepcopy

from yaml import load, FullLoader
from collections.abc import Mapping


class Content(Mapping, ABC):
    __delimiter = {r"^(?:-|\+){3}\s*$"}
    __regex = re.compile(__delimiter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _ = Content.__regex.split(string, 2)
        fm = deepcopy(_)
        content = deepcopy(_)
        load(fm, Loader=FullLoader)
        return cls(metadata, content)



