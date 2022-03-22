from logging import root


from htmlelement import HtmlElement

class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(root_name)
    
    def add_child(self, child_name, child_text):
        self.__root.children.append(HtmlElement(child_name, child_text))
        return self

    def __str__(self):
        return str(self.__root)