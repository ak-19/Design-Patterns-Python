from htmlelement import HtmlElement
from htmlbuilder import HtmlBuilder

if __name__ == '__main__':
    builder = HtmlElement.construct('ul', HtmlBuilder)
    builder.add_child('li', 'second level').add_child('li', 'second level again')
    print(builder)