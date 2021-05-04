import justpy as jp


@jp.SetRoute("/")
def home():
    # instantiate a page
    wp = jp.QuasarPage(tailwind=True)

    main_div = jp.Div(a=wp, classes="bg-gray-200 h-screen")

    sub_div1 = jp.Div(a=main_div, classes="grid grid-cols-3 gap-4 p-4")

    # make a div!
    input1 = jp.Input(a=sub_div1, placeholder="Enter first value", classes="form-input")

    input2 = jp.Input(
        a=sub_div1, placeholder="Enter second value", classes="form-input"
    )

    div_output = jp.Div(a=sub_div1, text="Result goes here", classes="text-gray-600")

    jp.Div(a=sub_div1, text="Just another div", classes="text-gray-600")

    jp.Div(a=sub_div1, text="YADiv", classes="text-gray-600")

    sub_div2 = jp.Div(a=main_div, classes="grid grid-cols-2 gap-4")

    jp.QBtn(
        a=sub_div2,
        click=sum_up,
        input1=input1,
        input2=input2,
        div_output=div_output,
        text="Calculate",
        classes="border border-blue-500 m-2 p-1 px-4 rounded "
        "text-blue-600 hover:bg-red-500 hover:text-white",
    )

    jp.Div(
        a=sub_div2,
        text="I am a cool interactive div!",
        mouseenter=mouse_enter,
        mouseleave=mouse_leave,
        classes="hover:bg-red-500",
    )

    return wp


# event handler for the click event on the button
def sum_up(widget, msg):
    sum = float(widget.input1.value) + float(widget.input2.value)
    widget.div_output.text = sum


# event handler for updating sub_div2
def mouse_enter(widget, msg):
    widget.text = "A mouse entered the house"


def mouse_leave(widget, msg):
    widget.text = "A mouse left the house"


# start the server
jp.justpy()
