import typer
from ssg.site import Site


def main(source="content", dest="dist"):
    config = {
        "source": source,
        "dest": dest
    }
    inst = Site(**config)
    inst.build()


typer.run(main)


