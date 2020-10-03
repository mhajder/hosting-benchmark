"""Information command."""
import click
import requests
from terminaltables import SingleTable


@click.command(help="Get information about the server")
@click.pass_context
def main(ctx: click.Context):
    """System information command entrypoint.

    :param ctx: Click context instance
    """
    response = requests.get(url=f'{ctx.obj["hostname"]}/api/info.php')
    if response.status_code != 200:
        raise click.ClickException(
            f'{ctx.obj["hostname"]}/api/info.php Not Found!'
        )

    data = response.json()
    headers = response.headers

    if "Content-Encoding" not in headers:
        headers["Content-Encoding"] = "None"
    if "Server" not in headers:
        headers["Server"] = "None"

    table = SingleTable(
        table_data=[
            ["PHP Version", data["phpVersion"]],
            ["Platform", data["platform"]],
            ["Server", headers["Server"]],
            ["Content-Encoding", headers["Content-Encoding"]],
        ]
    )
    table.inner_heading_row_border = False
    table.title = "Information"
    click.echo(table.table)
