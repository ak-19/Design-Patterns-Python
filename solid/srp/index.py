from journal import Journal
if __name__ == '__main__':
    j = Journal()
    # j.add_entry('first entry')
    # j.add_entry('second entry')
    # j.add_entry('third entry')

    # # print(j)
    # # j.remove_entry(2)
    # # j.remove_entry(1)

    # print(j)

    # j.save('persist.txt')
    j.load('persist.txt')
    print(j)

