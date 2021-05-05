import justpy as jp
from home import Home
from about import About

jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)
jp.justpy(port=8000)
