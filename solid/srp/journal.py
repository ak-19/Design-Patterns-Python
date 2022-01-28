class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(text)

    def remove_entry(self, index):
        if index < len(self.entries):
            self.count -= 1
            del self.entries[index]

    def __str__(self) -> str:
        return '\n'.join(self.entries)       

