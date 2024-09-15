def who_irritates_most(N, names, ages, minutes):
    # Criar um dicionário que mapeia nomes para idades
    name_to_age = {name: age for name, age in zip(names, ages)}
    
    result = []
    for minute in minutes:
        # Identificar quem está acordado no minuto atual
        awake_children = set(minute)
        
        # Determinar a criança mais nova entre as que estão acordadas
        most_irritating = min(awake_children, key=lambda child: name_to_age[child])
        
        result.append(most_irritating)
    
    return result

# Exemplo de uso:
N = 3
names = ['Alice', 'Bob', 'Clara']
ages = [5, 7, 6]  # Idade de Alice, Bob, Clara, respectivamente
minutes = [['Alice'], ['Bob', 'Clara'], ['Clara']]

print(who_irritates_most(N, names, ages, minutes))
# Deve imprimir: ['Alice', 'Clara', 'Clara']