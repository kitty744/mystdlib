from mylib import retry

count = 0

@retry.retry(attempts=5, delay=1, backoff=2, exceptions=(ValueError,))
def test():
    global count
    count += 1
    print("Attempt", count)
    if count < 4:
        raise ValueError("Failing!")
    return "Success!"

print(test())
