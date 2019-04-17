# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]

# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку

# Вариант 1:
matrix_rotate = [list(x) for x in list(zip(*matrix))]
# Вариант 2:
matrix_rotate_v2 = ([[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix))])

print(matrix_rotate, matrix_rotate_v2, sep='\n')
