while True:
    try:
        D, VF, VG = [int(x) for x in input().split()]

        if D >= 12:
            print('N')
        elif VG >= 12 and VG > VF:
            print('S')
        else:
            ip = 0
            il = D

            while ip < il:
                ip += VG
                il += VF
                if il >= 12 and il > ip:
                    print('N')
                    exit()
            print('S')
    except EOFError:
        break