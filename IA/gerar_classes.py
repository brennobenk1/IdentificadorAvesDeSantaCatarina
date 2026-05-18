import json

# Esse arquivo será usado DEPOIS do treinamento
with open('class_indices.json', 'r') as f:
    class_indices = json.load(f)

# Inverte o dicionário: índice -> nome
classes_ordenadas = [None] * len(class_indices)
for especie, idx in class_indices.items():
    classes_ordenadas[idx] = especie

# Salva como JavaScript
with open('classes.js', 'w') as f:
    f.write('const CLASS_NAMES = ' + json.dumps(classes_ordenadas) + ';')

print("Arquivo classes.js gerado com sucesso!")