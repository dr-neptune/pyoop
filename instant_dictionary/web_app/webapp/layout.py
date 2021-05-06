import justpy as jp


class DefaultLayout(jp.QLayout):
    def __init__(self, view="hHh lpR fFf", **kwargs):
        super().__init__(view=view, **kwargs)

        # create layout structure
        header = jp.QHeader(a=self, elevated=True, classes="bg-primary text-white")
        toolbar = jp.QToolbar(a=header)

        # make drawer for popping out of left hand side
        drawer = jp.QDrawer(
            a=self, show_if_above=True, v_model="left", side="left", bordered=True
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
            click=self.move_drawer,
            drawer=drawer,
        )

        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
