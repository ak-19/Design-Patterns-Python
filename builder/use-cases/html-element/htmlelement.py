class HtmlElement:
    def __init__(self, name = '', text = ''):
        self.name = name
        self.text = text
        self.children = []

    def __str(self, indent):    
        result = []
        result.append(indent * ' '  + f'<{self.name}>')

        if self.text:
            result.append((indent + 1) * ' '  + self.text)

        for child in self.children:
            result.append(child.__str(indent + 1))
        result.append(indent * ' '  + f'</{self.name}>')

        return '\n'.join(result)
    
    def __str__(self) -> str:
        return self.__str(0)

    @staticmethod
    def construct(name, builder):
        return builder(name)