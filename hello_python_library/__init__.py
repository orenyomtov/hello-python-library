from termcolor import colored

def helloString(input):
    """Returns a hello world string """
    return colored(f'Hello {input}!', 'green')
