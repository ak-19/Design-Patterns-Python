from journal import Journal
from persistenceManager import PersistenceManager

if __name__ == '__main__':
    j = Journal()
    # j.add_entry('first entry')
    # j.add_entry('second entry')
    # j.add_entry('third entry')
    # PersistenceManager.save_to_file(j, 'persist.txt')

    PersistenceManager.load_from_file(j, 'persist.txt')

    print(j)

