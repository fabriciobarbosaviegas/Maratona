def addInfectado(amigos, infectados):
    for i in amigos:
            if not i in infectados:
                infectados.append(i)

nm = input('').split()
ir = input('').split()

infectados = [ir[0]]

for i in range(int(nm[1])):
	ap = input('').split()

	if i+1 >= int(ir[1]):
		for j in ap[1:]:
			if j in infectados:
				addInfectado(ap[1:], infectados)

print(len(infectados))