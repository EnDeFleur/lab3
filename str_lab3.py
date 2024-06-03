class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, x, y):
        new_node = Node(x, y)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


def has_visited_twice(moves):
    # Начальная позиция короля (0, 0)
    x, y = 0, 0
    visited_positions = set()
    visited_positions.add((x, y))

    # Связанный список для хранения координат
    position_list = LinkedList()
    position_list.append(x, y)

    # Словарь для движения короля
    move_directions = {
        'U': (0, 1),  # Up
        'D': (0, -1),  # Down
        'L': (-1, 0),  # Left
        'R': (1, 0),  # Right
        'UL': (-1, 1),  # Up-Left
        'UR': (1, 1),  # Up-Right
        'DL': (-1, -1),  # Down-Left
        'DR': (1, -1)  # Down-Right
    }

    for move in moves:
        if move in move_directions:
            dx, dy = move_directions[move]
            x += dx
            y += dy

            if (x, y) in visited_positions:
                return True
            visited_positions.add((x, y))
            position_list.append(x, y)

    return False


# Чтение входных данных из файла
with open('input.txt', 'r') as f:
    moves = f.readline().strip().split()

# Проверка, был ли король дважды на одном и том же поле
result = has_visited_twice(moves)

# Запись результата в выходной файл
with open('output.txt', 'w') as f:
    if result:
        f.write('YES\n')
    else:
        f.write('NO\n')
