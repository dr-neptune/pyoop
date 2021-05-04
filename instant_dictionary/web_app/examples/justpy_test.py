import justpy as jp


@jp.SetRoute("/")
def home():
    # instantiate a page
    wp = jp.WebPage()

    # make a div!
    jp.Div(a=wp, text="Hello, World!", classes="text-green-800 bg-yellow-500")
    jp.Div(a=wp, text="Hello, Again!")

    return wp


@jp.SetRoute("/about")
def home():
    # instantiate a page
    wp = jp.WebPage()

    # make a div!
    jp.Div(a=wp, text="Hi, World!")
    jp.Div(a=wp, text="Hi, Again!")

    return wp


# start the server
jp.justpy()
