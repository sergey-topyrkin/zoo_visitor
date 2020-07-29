# -*- coding: utf-8 -*-


class ZooCommand:
    def __init__(self, command):
        self.text_command = command
        self.right_commands = ['create', 'get', 'set', 'ls', 'stat', 'rmr']
        self.error = ''
        self.command = ''
        self.path = ''
        self.data = ''

        self.parse(command)

    def parse(self, command):
        # структура пришедшей команды
        # host> create path {data}
        commands = command.split(" ")
        for part in commands:
            print(part)

        cmd = commands[0].split(">")
        commands[0] = cmd[1]

        if commands[0] not in self.right_commands:
            self.error = 'Unknown command [' + commands[0] + ']'

        self.command = commands[0]
        self.path = commands[1]
        # данные могли быть разделены пробелами
        data = ""
        for i in range(len(commands)):
            if i >= 2:
                data = data + commands[i] + ' '

        self.data = data
