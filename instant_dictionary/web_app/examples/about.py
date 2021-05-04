import justpy as jp


class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        main_div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=main_div, text="This is the About page!", classes="text-4xl m-2")
        jp.Div(
            a=main_div,
            text="""
        Now, this is a story all about how
        My life got flipped-turned upside down
        And I liked to take a minute
        Just sit right there
        I'll tell you how I became the prince of a town called Bel Air
        In west Philadelphia born and raised
        On the playground was where I spent most of my days
        Chillin' out maxin' relaxin' all cool
        And all shootin some b-ball outside of the school
        When a couple of guys who were up to no good
        Started making trouble in my neighborhood
        I got in one little fight and my mom got scared
        She said 'You're movin' with your auntie and uncle in Bel Air'
        I begged and pleaded with her day after day
        But she packed my suite case and send me on my way
        She gave me a kiss and then she gave me my ticket.
        I put my walkman on and said, 'I might as well kick it'.
        First class, yo this is bad
        Drinking orang juice out of a champagne glass.
        Is this what the people of Bel-Air Living like?
        Hmm this might be alright.
        But wait I hear they're prissy, bourgeois, all that
        Is Bel-Air the type of place they send this cool cat?
        I don't think so
        I'll see when I get there
        I hope they're prepared for the prince of Bel-Air
        Well uh the plane landed and when I came out
        There was a dude who looked like a cop standing there with my name out
        I ain't trying to get arrested yet
        I just got here
        I sprang with the quickness like lightening, disappeared
        I whistled for a cab and when it came near
        The license plate said fresh and it had dice in the mirror
        If anything I can say this cab is rare
        But I thought 'Now forget it' - 'Yo homes to Bel Air'
        I pulled up to the house about seven or eight
        And I yelled to the cabbie 'Yo, homes smell ya later'
        I looked at my kingdom
        I was finally there
        To sit on my throne as the Prince of Bel Air
        """,
            classes="text-lg",
        )
        return wp


jp.Route(About.path, About.serve)
jp.justpy(port=8001)
