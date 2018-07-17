
def divi(s):
    n=int(s)
    if n ==0:
        raise ZeroDivisionError('How sad your math teacher is')
    return 10/n

def func():
    try:
        divi('0')
    except ZeroDivisionError as e:
        print(e)
        print('finish')
   
func()

