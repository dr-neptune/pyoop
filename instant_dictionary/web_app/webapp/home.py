import justpy as jp
from justpy.quasarcomponents import QuasarPage


class Home:
    path = "/"

    @classmethod
    def serve(cls):
        wp = QuasarPage(tailwind=True)
        main_div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=main_div, text="This is the Home page!", classes="text-4xl m-2")
        jp.Div(a=main_div, text="Yo homes, to Bel-Air!", classes="text-lg")
        return wp
