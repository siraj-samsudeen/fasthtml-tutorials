# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/01-intro-tutorial-by-jeremy/part3.ipynb.

# %% auto 0
__all__ = ['app', 'rt', 'NumList', 'get']

# %% ../../nbs/01-intro-tutorial-by-jeremy/part3.ipynb 1
from fasthtml.common import *

# %% ../../nbs/01-intro-tutorial-by-jeremy/part3.ipynb 4
app, rt = fast_app(live=True)

# %% ../../nbs/01-intro-tutorial-by-jeremy/part3.ipynb 12
def NumList(i):
    return Ul(*[Li(o) for o in range(i)])

# %% ../../nbs/01-intro-tutorial-by-jeremy/part3.ipynb 17
@rt("/")
def get():
    nums = NumList(5)
    return Titled("Greeting", Div(nums, id="stuff", hx_get="/change"))

# %% ../../nbs/01-intro-tutorial-by-jeremy/part3.ipynb 18
@rt("/change")
def get():
    return P("Change is good!")

# %% ../../nbs/01-intro-tutorial-by-jeremy/part3.ipynb 21
serve()
