from greetings import Greetings

greet = Greetings()
print(f'{greet.hello()} from the use_hello file.')
print(f'{Greetings("Alice").hello()} from the use_hello file.')