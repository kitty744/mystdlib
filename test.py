from mylib import observer, printer

def callbacktest1(val):
    printer.print("Callback 1:", val)

def callbacktest2(val):
    printer.print("Callback 2:", val)

observer.watch("score", callbacktest1)
observer.watch("score", callbacktest2)

observer.set_value("score", 10)
observer.set_value("score", 20)

observer.unwatch("score", callbacktest1)
observer.set_value("score", 30)

printer.print("Current score:", observer.get_value("score"))