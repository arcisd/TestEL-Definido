
def match_first_five(num): # 'num' debe tener al menos 5 dígitos.
    string=str(num)
    if set(list(string[0:5]))=={'1','2','3','4','5'}: return 1 # posible match de 5 primeros dígitos.
    return 0

# F[161] dato entregado, por lo tanto no es necesario analizar los valores anteriores.
fib=[1983924214061919432247806074196061,3210056809456107725247980776292056] # F[161],F[162]

def first_five_fib(fib):
    while True:
          fib.append(fib[-1]+fib[-2])
          if match_first_five(fib[-1])==1: return len(fib)+160

print(first_five_fib(fib))

# first_five_fib(fib) = 521
