import csv
import matplotlib.pyplot as plt


def cargar_laberinto(desde_archivo):
    laberinto = []
    with open(desde_archivo, newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            laberinto.append(list(map(int, fila)))
    return laberinto


def encontrar_soluciones(laberinto, inicio, fin):
    def es_valida(coordenada):
        x, y = coordenada
        return 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and laberinto[x][y] == 0

    def dfs(actual, camino, soluciones):
        if actual == fin:
            soluciones.append(camino[:])
            return
        x, y = actual
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nuevo_x, nuevo_y = x + dx, y + dy
            nueva_pos = (nuevo_x, nuevo_y)
            if es_valida(nueva_pos) and nueva_pos not in camino:
                camino.append(nueva_pos)
                dfs(nueva_pos, camino, soluciones)
                camino.pop()  # Retroceder en el camino

    if not es_valida(inicio) or not es_valida(fin):
        return []

    soluciones = []
    dfs(inicio, [inicio], soluciones)
    return soluciones


def dibujar_laberinto(laberinto, soluciones):
    plt.figure(figsize=(len(laberinto[0]), len(laberinto)))

    for solucion in soluciones:
        plt.clf()
        plt.imshow(laberinto, cmap='gray')
        x_values = [pos[1] for pos in solucion]
        y_values = [pos[0] for pos in solucion]
        plt.plot(x_values, y_values, marker='o', markersize=10)
        plt.pause(0.1)
        plt.draw()
        plt.waitforbuttonpress()  # Esperar a que el usuario haga clic


def main():
    archivo_laberinto = "laberinto.csv"
    laberinto = cargar_laberinto(archivo_laberinto)
    punto_inicio = (0, 3)  # Cambiar las coordenadas de inicio si es necesario
    punto_fin = (10, 7)    # Cambiar las coordenadas de fin si es necesario

    soluciones = encontrar_soluciones(laberinto, punto_inicio, punto_fin)

    if not soluciones:
        print("No se encontraron soluciones.")
    else:
        print(f"Se encontraron {len(soluciones)} soluciones.")
        dibujar_laberinto(laberinto, soluciones)


if __name__ == "__main__":
    main()
