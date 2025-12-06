from mylib import process

output = process.run("echo Hello World")
print(output)

proc = process.run_async("ping google.com")
print(proc.pid)

process.kill(proc.pid)

print(process.exists(proc.pid))