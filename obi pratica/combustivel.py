C = float(input())
D = float(input())
T = float(input())

distanciaFaltante = D-T*C

if distanciaFaltante <= 0:
    print(f'{0:.1f}')

else:
    print(f'{distanciaFaltante/C:.1f}')