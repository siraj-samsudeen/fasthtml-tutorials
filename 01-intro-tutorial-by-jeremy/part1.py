from fasthtml.common import *

app, rt = fast_app(live=True)

@rt("/")
def get():
    return Titled("Greetings", Div(P("Hello World")))

serve()
