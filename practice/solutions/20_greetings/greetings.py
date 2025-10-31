class Greetings:

    def __init__(self, name='Shiwani'):
        self.name = name    

    def hello(self):
        return f"Hello, {self.name}!"


greet = Greetings()
print(f'{greet.hello()} from the greetings module.')