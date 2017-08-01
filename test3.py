
# 0 :                                                   prev[0]=0
# 1 :        0         pos =       0        start = 0   prev[1]=0       0
# 2 :       1 4        pos =      0 1       start = 1   prev[2]=1      1 2
# 3 :      9 0 1       pos =     0 1 2      start = 9   prev[3]=3     3 4 5
# 4 :     4 9 0 1      pos =    0 1 2 3     start = 4   prev[4]=6    6 7 8 9  = índices
# 5 :    4 9 0 1 4     pos =   0 1 2 3 4    start = 4   prev[5]=10     ...
# 6 :   9 0 1 4 9 0    pos =  0 1 2 3 4 5   start = 9   prev[6]=15
#                                                       ...

# 0=0^2
# 1=1^2
# 4=2^2
# 9=3^2

#  | 00 | 01 02 | 03 04 05 | 06 07 08 09 | 10 11 12 13 14 | 15 16 17 18 19 20 | = índices
#  |  0 |  1  4 |  9  0  1 |  4  9  0  1 |  4  9  0  1  4 |  9  0  1  4  9  0 | = elemento correspondiente según índice '(elem%4)**2'

prev,num_line=[0],500 # 500 lineas.

def max_path(num_line):
    prev=[0] # prev[k] cantidad de elementos antes de la linea 'k' que es lo mismo que el índice del primer elemento en la linea 'k'.
    for ind in range(1,num_line+1): prev.append(ind-1+prev[-1])
    line=[(elem%4)**2 for elem in range(prev[num_line],prev[num_line]+num_line)] # última linea en la pirámide
    while num_line>1: # calcula máximos de a pares y se suman al elemento en la linea anterior hasta llegar al inicio.
          line=[max(line[ind],line[ind+1])+((prev[num_line-1]+ind)%4)**2 for ind in range(0,num_line-1)]
          num_line=num_line-1 # siguiente linea hacia arriba.
    return line[0]

print(max_path(num_line))

# max_path(500)=3491
