'''
cassar_cipher
'''
def cassar_cipher(a, b):

    x = list(a)

    for i in x:
        
        if ord(i) < 122-b+1:
            s = chr(ord(i)+b)
            print(s, end='')
        else:
            s = chr(ord(i)-26+b)
            print(s, end='')


cassar_cipher('xvillage', 3)
