import click


@click.group()
def cli():
    pass


@cli.command()
def main():
    from hashcode.main import main
    main()


@cli.command()
@click.option('--file', help='Input file')
@click.option('--out', help='Output file', required=False)
def wout(file, out):
    pass

@cli.command()
@click.option('--file', help='Input file')
@click.option('--out', help='Output file', required=False)
def toon(file, out):
    pass

@cli.command()
@click.option('--file', help='Input file')
@click.option('--out', help='Output file', required=False)
def david(file, out):
    pass

@cli.command()
@click.option('--file', help='Input file')
@click.option('--out', help='Output file', required=False)
def simon(file, out):
    pass


if __name__ == "__main__":
    cli()
