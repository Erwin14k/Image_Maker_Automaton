class Error:
    def __init__(self, description, type, line, column):
        self.description = description
        self.type = type
        self.line = line
        self.column = column

    def print_error(self):
        print(self.description, self.type, self.line, self.column)