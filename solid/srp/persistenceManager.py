class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, 'w') as file:
            file.write(str(journal))

    @staticmethod
    def load_from_file(journal, filename):
        with open(filename, 'r') as file:
            text = file.read()
            for entry in text.split('\n'):
                journal.add_entry(entry)