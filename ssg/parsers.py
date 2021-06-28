import shutil

from typing import List
from pathlib import Path


def __init__():

    class Parser:
        extensions: List[:str] = []

        def valid_extension(self, extension):
            return extension in self.extensions

        def parse(self, path: Path, source: Path, dest: Path):
            raise NotImplementedError

        def read(self, path: Path):
            with path.open() as file:
                contents = file.read()
                return contents

        def write(self, path: Path, dest: Path, content, ext='.html'):
            destination = dest
            full_path = destination / path.with_suffix(ext).name
            with full_path.open() as file:
                full_path.write_bytes(content)

        def copy(self, path, source, dest):
            shutil.copy2(path, path.relative_to(source) / dest)

        class ResourceParser(extensions=['.jpg', '.png', '.gif', '.css', '.html']):
            def parse(self, path: Path, source: Path, dest: Path):
                self.copy(path, source, dest)















