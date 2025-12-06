from mylib import schedule, printer

def hello(name):
    printer.println("Hello: ", name)

schedule.after(3, hello, "John Doe")
schedule.every(0.1, hello, "Jill Doe")