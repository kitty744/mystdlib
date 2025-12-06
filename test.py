from mylib import *

logger.info("Started program!")

# ---- Print some math ----
printer.print("The higher number is: ")
printer.println(math.max(1, 2))

# ---- Print some text with colors and more! ----
printer.println(color.red("This text is red!"))
printer.println(color.green("This text is green!"))
printer.println(color.blue("This text is blue!"))
printer.println(color.yellow("This text is yellow!"))
printer.println(color.underline("This text has an underline"))

