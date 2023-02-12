import asyncio
import click
import uvicorn

from tz_flashlight.client import main

@click.group()
@click.help_option(
    help='''Показать это сообщение и завершить работу''',
)
def cli(**kwargs):
    '''Данный пакет позволяет запустить управляемый по сети фонарь и сервер, отправляющий команды.'''
    pass

@cli.command()
@click.option("-h", "--host", default="localhost", help="Адрес сервера")
@click.option("-p", "--port", default="9999", help="Порт сервера")
def runserver(**kwargs):
    assert 0 < int(kwargs["port"]) < 65535, "Задан неверный порт"
    uvicorn.run(f'tz_flashlight.server:app', host=kwargs["host"], port=int(kwargs["port"]))

@cli.command()
@click.option("-h", "--host", default="localhost", help="Адрес сервера")
@click.option("-p", "--port", default="9999", help="Порт сервера")
def runclient(**kwargs):
    asyncio.run(main(host=kwargs["host"], port=kwargs["port"]))

if __name__ == "__main__":
    cli()