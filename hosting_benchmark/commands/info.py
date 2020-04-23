import click
import requests
from terminaltables import SingleTable


@click.command(help='Get information about the server')
@click.pass_context
def main(ctx):
    click.secho("Information", bold=True)
    response = requests.get(
        url=f'{ctx.obj["hostname"]}/api/info.php'
    )
    if response.status_code == 200:
        data = response.json()
        table = SingleTable(table_data=[
            ['PHP Version', data['phpVersion']],
            ['Platform', data['platform']],
        ])
        table.inner_heading_row_border = False
        click.echo(table.table)
    else:
        raise click.ClickException(f'{ctx.obj["hostname"]}/api/info.php Not Found!')
