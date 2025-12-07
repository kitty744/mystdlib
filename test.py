from mylib import *

# ---- Logger module ----
logger.info("Started program!")

# ---- Printer module ----
printer.println("Hello there!")

# ---- color module ----
printer.println(color.red("This text is red!"))
printer.println(color.green("This text is green!"))
printer.println(color.blue("This text is blue!"))
printer.println(color.yellow("This text is yellow!"))
printer.println(color.underline("This text has an underline"))

# ---- Clipboard module ----
printer.println("This is what you got on your clipboard: " + clipboard.paste())

# ---- Random module ----
printer.println("This is a random integer: ")
printer.print(random.randint(1, 100))

# ---- Schedule module ----
def tick():
    printer.print("Tick")
    
schedule.every(2, tick)

time.sleep(10)