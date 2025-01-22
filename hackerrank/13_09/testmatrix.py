def maximize_upper_left(matrix):
    n = len(matrix) // 2
    total_sum = 0

    # Iterar sobre el cuadrante superior izquierdo
    for i in range(n):
        for j in range(n):
            # Encontrar los 4 valores posibles debido a inversiones
            original = matrix[i][j]
            mirr_row = matrix[2 * n - 1 - i][j]
            mirr_col = matrix[i][2 * n - 1 - j]
            mirr_both = matrix[2 * n - 1 - i][2 * n - 1 - j]

            # Tomar el máximo valor posible para esta posición
            best_value = max(original, mirr_row, mirr_col, mirr_both)

            # Sumarlo al total
            total_sum += best_value

    return total_sum


if __name__ == '__main__':
    # Matriz de ejemplo
    matrix = [
        [107, 54, 128, 15],
        [12, 75, 110, 138],
        [100, 96, 34, 85],
        [75, 15, 28, 112]
    ]

    result = maximize_upper_left(matrix)
    print("Suma máxima del cuadrante superior izquierdo:", result)
