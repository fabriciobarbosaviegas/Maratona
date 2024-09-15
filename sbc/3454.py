jogo = [i for i in input()]

if(jogo.count("O") > 1 or jogo == ["X", "X", "X"]):
    print("?")
elif(jogo[0] == jogo[1] or jogo[2] == jogo[1]):
    print("Alice")
else:
    print("*")
