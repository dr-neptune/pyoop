import justpy as jp
import inspect
from home import Home
from dictionary import Dictionary
from about import About
from page import Page

imports = list(globals().values())

print(imports)

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, Page) and obj is not Page:
            jp.Route(obj.path, obj.serve)

# jp.Route(Home.path, Home.serve)
# jp.Route(Dictionary.path, Dictionary.serve)
# jp.Route(About.path, About.serve)

jp.justpy(port=8000)
