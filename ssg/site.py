from pathlib import Path


class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        print(f'directory {directory}')
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if (path.cwd()).is_dir():
                self.create_dir(path)
            else:
                None



def main():
    this_site = Site('C:/temp', 'C:/temp2')
    this_site.create_dir('C:/temp2')


if __name__ == '__main__':
    main()
