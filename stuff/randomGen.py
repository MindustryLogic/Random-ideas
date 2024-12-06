def pwgen(length):
    import random
    import string
    loop=0
    output = []
    while loop < length:
        num = int((33 + 94*random.random()) // 1)
        output.append(chr(num))
        loop = loop+1
    print(''.join(output))