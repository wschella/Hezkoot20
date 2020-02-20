import click
from hashcode.david.script import solve


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
    from hashcode.api.problem import Problem
    from hashcode.api.models import Solution
    problem = Problem(file)
    print("Parse succes")
    solution = Solution(problem)
    solution.add_lib(problem.libraries[0])
    solution.print()
    solution.print(file="sol.out")
    print(solution.score())

    solve(problem)
    solution.print(file="sol.out")


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
