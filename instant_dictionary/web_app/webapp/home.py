import justpy as jp
from justpy.quasarcomponents import QuasarPage


class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = QuasarPage(tailwind=True)

        # create layout structure
        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout, elevated=True, classes="bg-primary text-white")
        toolbar = jp.QToolbar(a=header)

        # make drawer for popping out of left hand side
        drawer = jp.QDrawer(
            a=layout, show_if_above=True, v_model="left", side="left", bordered=True
        )

        # add links to the drawer
        scroller = jp.QScrollArea(a=drawer, classes="fit")
        qlist = jp.QList(a=scroller)
        a_classes = "p-2 m-2 text-lg text-blue-400 hover:text-blue-700"
        jp.A(a=qlist, text="Home", href="/", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="/dictionary", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes=a_classes)
        jp.Br(a=qlist)

        # add drawer button
        jp.QBtn(
            a=toolbar,
            dense=True,
            flat=True,
            round=True,
            icon="menu",
            click=cls.move_drawer,
            drawer=drawer,
        )

        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

        container = jp.QPageContainer(a=layout)

        main_div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=main_div, text="This is the Home page!", classes="text-4xl m-2")
        jp.Div(a=main_div, text="Yo homes, to Bel-Air!", classes="text-lg")

        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
