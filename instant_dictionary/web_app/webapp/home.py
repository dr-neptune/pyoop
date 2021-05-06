import justpy as jp
from layout import DefaultLayout


class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        main_div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=main_div, text="This is the Home page!", classes="text-4xl m-2")
        jp.Div(a=main_div, text="Yo homes, to Bel-Air!", classes="text-lg")

        return wp
