"""Demonstrate *args and **kwargs by printing words and their characters in reverse order."""


def print_backwards(*args, **kwargs):
    print(kwargs)
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' | ')
    for word in args[::-1]:
        print(word[::-1], **kwargs)


print_backwards("hello", "planet", 'earth', 'take',
                'me', 'to', 'your', 'leader',
                file=None, end='\n', sep=' | ')

print()

print("hello", "planet", 'earth', 'take',
                'me', 'to', 'your', 'leader',
                file=None, end='\n', sep=' | ')