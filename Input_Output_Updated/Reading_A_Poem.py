"""Read and print each line of a poem file, stripping trailing newlines."""
with open('Jabberwocky.txt', encoding='utf-8') as jabber:
    for line in jabber:
        print(line.rstrip())

