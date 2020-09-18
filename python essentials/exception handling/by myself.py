import math
from past.builtins import raw_input


class CommandError(ValueError):
    pass

valid_commands = {'start', 'stop', 'pause'}
while True:
    command =raw_input('>')
    try:
        if command.lower() not in valid_commands:
            raise CommandError('Invalid commend:%s' %command)
    except CommandError:
        print('bad command string:"%s"'%command)