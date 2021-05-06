import justpy as jp
from definition import Definition


class Dictionary:
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        main_div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=main_div, text="Instant English Dictionary", classes="text-4xl m-2")
        jp.Div(
            a=main_div,
            text="Get the definition of any English word instantly as you type",
            classes="text-lg",
        )

        # make an input div
        input_div = jp.Div(a=main_div, classes="grid grid-cols-2")

        output_div = jp.Div(a=main_div, classes="m-2 p-2 text-lg border-2 h-40")

        # word entry div
        input_box = jp.Input(
            a=input_div,
            outputdiv=output_div,
            placeholder="Type in a word here",
            classes="m-2 bg-gray-100 border-2 border-gray-200 rounded "
            "focus: bg-white focus:outline-none focus:border-purple-500 py-2 px-4",
        )

        # handle event for typing in the input box
        input_box.on("input", cls.get_definition)

        # jp.Button(
        #     a=input_div,
        #     text="Get Definition",
        #     classes="border-2 text-gray-500",
        #     click=cls.get_definition,
        #     outputdiv=output_div,
        #     inputbox=input_box,
        # )

        return wp

    @staticmethod
    def get_definition(widget, msg):
        defn_out = Definition(widget.value).get()
        widget.outputdiv.text = " ".join(defn_out)
