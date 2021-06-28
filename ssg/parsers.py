import shutil

from typing import List
from pathlib import Path


class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path: Path):
        with open(path, 'r') as file:
            return file.read()


    def write(self, path: Path, dest: Path, content, ext='.html'):
        full_path = self.dest / path.with_suffix(ext).name
        with open('full_path', 'w') as file:
            full_path.write_bytes(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, path.relative_to(self.source) / self.dest)

class ResourceParser(Parser):
    extensions = ['.jpg', '.png', '.gif', '.css', '.html']
    def parse(self, path: Path, source: Path, dest: Path):
        self.copy(path, source, dest)















