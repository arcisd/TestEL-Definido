
def palindrome(num):
    string=str(num)
    ind_L=0
    ind_R=len(string)-1
    while ind_L<ind_R: # analiza sólo la mitad de la palabra.
          if string[ind_L]!=string[ind_R]: return 0
          ind_L,ind_R=ind_L+1,ind_R-1
    return 1

minn,maxx=100,999 # 3 cifras

# 999+999=1998

def max_palindrome(minn,maxx):
    to_part=2*maxx # analiza según particiones desde 1998 a 200 y se detiene al encontrar un palíndromo máximo en un piso. 
    res=(0,0,0)
    while to_part>=2*minn:
          if to_part>maxx:
             start=maxx
          else: # to_part<=maxx:
             start=minn
          while start>=minn:
                if to_part-start>=minn and to_part-start<=maxx and start*(to_part-start)>res[2] and palindrome(start*(to_part-start))==1:
                   res=start,to_part-start,start*(to_part-start)
                start=start-1
          if res!=(0,0,0): return res
          to_part=to_part-1
    return res

print(max_palindrome(minn,maxx))
# la respuesta se encuentra en el piso 1996.

# max_palindrome(minn,maxx) = (993, 913, 906609)
