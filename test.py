from mylib import events, printer

def hello(name):
    printer.println("Hello: ", name)

events.on("greet", hello)

if (1 == 1):
    events.trigger("greet", "John doe")

events.off("greet", hello)
events.trigger("greet", "Jill doe")