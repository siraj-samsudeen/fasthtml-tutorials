"""Fill in a module description here"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['start_server', 'stop_server', 'show_with_pico']

# %% ../nbs/00_core.ipynb 5
from fasthtml.jupyter import JupyUvi
import time


def start_server(app):
    global server

    if "server" in globals():
        server.stop()
        time.sleep(0.1)
    server = JupyUvi(app)


def stop_server():
    server.stop()

# %% ../nbs/00_core.ipynb 7
from fasthtml.common import *


def show_with_pico(*args):
    return show(Div(*args, cls="pico"))
