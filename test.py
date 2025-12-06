from mylib import debounce
import time

@debounce.debounce(1.0)
def greet():
    print("Greetings!")

    
greet()
greet()
greet()
time.sleep(1.2)