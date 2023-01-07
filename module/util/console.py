class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Log:

    def log(string):
        print(f"{Color.OKCYAN}{string}{Color.END}")

    def warn(string):
        print(f"{Color.WARNING}{string}{Color.END}")

    def error(string):
        print(f"{Color.FAIL}{string}{Color.END}")
    
    def fail(self, string):
        self.error(string)

    def ok(string):
        print(f"{Color.OKGREEN}{string}{Color.END}")

    def success(self, string):
        self.ok(string)

    def info(string):
        print(f"{Color.OKCYAN}{string}{Color.END}")