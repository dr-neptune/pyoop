import justpy as jp
import requests
from definition import Definition
from layout import DefaultLayout
from page import Page


class Dictionary(Page):
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        main_div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=main_div, text="Instant English Dictionary", classes="text-4xl m-2")
        jp.Div(
            a=main_div,
            text="Get the definition of any English word instantly as you type",
            classes="text-lg",
        )

        # make an input div
        input_div = jp.Div(a=main_div, classes="grid grid-cols-2")

        output_div = jp.Div(
            a=main_div,
            classes="m-2 p-2 text-lg border-2 h-40 border-gray-350 whitespace-pre-wrap",
        )

        # word entry div
        input_box = jp.Input(
            a=input_div,
            outputdiv=output_div,
            placeholder="Type in a word here",
            classes="m-2 bg-gray-100 border-2 border-gray-500 rounded "
            "focus: bg-white focus:outline-none focus:border-purple-500 py-2 px-4",
        )

        # handle event for typing in the input box
        input_box.on("input", cls.get_definition)

        return wp

    @staticmethod
    def get_definition(widget, msg):

        req = requests.get(f"http://127.0.0.1:8000/api?w={widget.value}").json()

        widget.outputdiv.text = "\n⁍\t".join(["", *req["definition"]])
