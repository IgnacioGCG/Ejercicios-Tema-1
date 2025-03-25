from queue import PriorityQueue

class Mision:
    def __init__(self, nombre, dificultad):
        self.nombre = nombre
        self.dificultad = dificultad

    def __lt__(self, other):
        return self.dificultad < other.dificultad

    def __str__(self):
        return self.nombre

# Crear una cola de prioridad
cola_misiones = PriorityQueue()

# Agregar misiones a la cola
cola_misiones.put(Mision("Rescatar al prisionero", 3))
cola_misiones.put(Mision("Recolectar suministros", 1))
cola_misiones.put(Mision("Defender la base", 2))
cola_misiones.put(Mision("Explorar territorio enemigo", 4))

# Mostrar las misiones en orden de dificultad
while not cola_misiones.empty():
    mision = cola_misiones.get()
    print(mision)