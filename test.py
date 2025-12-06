from mylib import clipboard, printer

clipboard.copy("Hello World!")

printer.println(clipboard.paste())