import basic

while True:
    text = input('Basic >> ')
    result, error = basic.run('<stdin>', text)

    if error: print(error)
    else: print(result)