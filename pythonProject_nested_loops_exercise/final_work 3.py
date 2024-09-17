import csv
import json
import matplotlib.pyplot as plt
from collections import defaultdict

# Ejercicio 1
datos = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

with open('example.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        dia = row['dia']
        provincia = row['provincia']
        datos[dia][provincia]['defunciones'] += int(row['num_def'])
        datos[dia][provincia]['casos'] += int(row['new_cases'])
        datos[dia][provincia]['hospitalizados'] += int(row['num_hosp'])
        datos[dia][provincia]['uci'] += int(row['num_uci'])

with open('resultados.json', 'w') as f:
    json.dump(datos, f)

# Ejercicio 2
while True:
    opcion = int(input("""¿Qué gráfica quieres visualizar?
    1. Defunciones
    2. Casos
    3. Hospitalizados
    4. UCI
    5. Salir
    """))
    if opcion == 5:
        break
    elif opcion in [1, 2, 3, 4]:

# Aquí pondrías el código para generar las gráficas según la opción elegida