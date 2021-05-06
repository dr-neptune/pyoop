import justpy as jp


class Doc:
    @classmethod
    def serve(cls):
        wp = jp.WebPage()

        main_div = jp.Div(a=wp, classes="bg-gray-200 h-screen")

        jp.Div(a=main_div, text="Instant Dictionary API", classes="text-4xl m-2")

        jp.Div(
            a=main_div,
            text="Get definitions of words",
            classes="text-lg",
        )

        jp.Hr()

        jp.Div(a=main_div, text="my_example_url.com/api?w=moon")

        jp.Hr()

        jp.Div(
            a=main_div,
            text="""
        {"word": "moon",
        "definition": ["A natural satellite of a planet.",
        "A month, particularly a lunar month (approximately 28 days).",
        "To fuss over adoringly or with great affection.",
        "Deliberately show ones bare ass (usually to an audience, or at a place, where this is not expected or deemed appropriate).",
        "To be lost in phantasies or be carried away by some internal vision, having temorarily lost (part of) contact to reality."]}
        """,
        )
        return wp
