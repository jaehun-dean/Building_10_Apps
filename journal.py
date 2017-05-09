import jornal1
# from journal1 import load, save -> 함수 호출 시 journal1을 쓸 필요가 없음


def print_header():
    print('-----------------')
    print('  Learn to Code')
    print('  Journal APP')
    print('-----------------')
    print()


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = jornal1.load(journal_name)
    # journal_data = load()

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand '{}'.".format(cmd))

    print('Done, goodbye.')
    jornal1.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries: ')
    # normal
    # for entry in data:
    #    print(entry)

    # reverse list
    # entries = reversed(data)
    # for entry in entries:
    #    print(entry)

    # enumerate list
    # for entry in enumerate(data):
    #    print(entry)

    # index
    for idx, entry in enumerate(data):
        print('* [{}] {}'.format(idx + 1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    jornal1.add_entry(text, data)
    # data.append(text)


def main():
    print_header()
    run_event_loop()

if __name__ == '__main__':
    main()