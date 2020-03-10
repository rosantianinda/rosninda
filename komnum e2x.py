import math

error = 0.001
def f(x):
    f_turunan = 1
    current=i=0
    iterasi= True
    while iterasi==True :
        old = current
        current += (f_turunan*(x**i))/math.factorial(i)
        print ('f ke-',i,'=',f_turunan,'e^2x=',current,' (selisih=', current-old,')')
        if current-old < error :
            iterasi = False
            print('\nPada expansi ke-',i,'\nDengan selisih=',current-old,'kurang dari nilai error=',error)
        else :
            f_turunan *=2
            i+=1
f(4)
