class Node:
    up: "Node"
    down: "Node"
    left: "Node"
    right: "Node"
    row_index: int
    col_index: int
    size: int

    def __init__(self, row_index: int, col_index: int):
        self.up = self.down = self.left = self.right = self
        self.row_index = row_index
        self.col_index = col_index
        self.size = 0


class Dlx:
    solution: list[Node]
    header: Node
    columns: list[Node]

    def __init__(self, matrix: list[list]):
        self.columns = []
        self.solution = []
        self._link_columns(matrix)
        self._build_links(matrix)

    def _link_columns(self, matrix: list[list]):
        for col_index in range(len(matrix[0])):
            node = Node(0, col_index)
            if self.columns:
                self.columns[-1].right = node
                node.left = self.columns[-1]
                self.columns[0].left = node
                node.right = self.columns[0]
            self.columns.append(node)

        self.header = Node(-1, -1)
        self.header.right = self.columns[0]
        self.header.left = self.columns[-1]
        self.columns[-1].right = self.header
        self.columns[0].left = self.header

    def _build_links(self, matrix: list[list]):
        for row_index in range(len(matrix)):
            row_head = None
            prev_node = None
            for col_index in range(len(matrix[0])):
                if matrix[row_index][col_index]:
                    node = Node(row_index + 1, col_index)
                    self.columns[col_index].up.down = node
                    node.up = self.columns[col_index].up
                    self.columns[col_index].up = node
                    node.down = self.columns[col_index]
                    self.columns[col_index].size += 1

                    if not row_head:
                        row_head = node

                    if prev_node:
                        prev_node.right = node
                        node.left = prev_node
                        node.right = row_head
                        row_head.left = node
                    prev_node = node

    def _cover(self, column_head: Node):
        column_head.right.left = column_head.left
        column_head.left.right = column_head.right

        row_node = column_head.down
        while row_node != column_head:
            right_node = row_node.right
            while right_node != row_node:
                right_node.up.down = right_node.down
                right_node.down.up = right_node.up
                self.columns[right_node.col_index].size -= 1
                right_node = right_node.right
            row_node = row_node.down

    def _uncover(self, column_head: Node):
        node = column_head.up
        while node != column_head:
            node_left = node.left
            while node_left != node:
                node_left.down.up = node_left
                node_left.up.down = node_left
                self.columns[node_left.col_index].size += 1
                node_left = node_left.left
            node = node.up
        column_head.left.right = column_head
        column_head.right.left = column_head

    def search(self, level: int):
        if self.header.right == self.header:
            return True

        column_node = self.header.right
        min_size = column_node.size
        right_node = column_node.right
        while right_node != self.header:
            if right_node.size < min_size:
                min_size = right_node.size
                column_node = right_node
            right_node = right_node.right

        self._cover(column_node)
        row_node = column_node.down
        while row_node != column_node:
            self.solution.append(row_node)
            right_node = row_node.right
            while right_node != row_node:
                self._cover(self.columns[right_node.col_index])
                right_node = right_node.right

            if self.search(level + 1):
                return True

            left_node = row_node.left
            while left_node != row_node:
                self._uncover(self.columns[left_node.col_index])
                left_node = left_node.left

            self.solution.pop()
            row_node = row_node.down

        self._uncover(column_node)
        return False


class SudokuSolver:
    matrix: list[list]
    solution: list[list]
    dlx: Dlx
    name: str

    def __init__(self, sudoku_grid: list[list], name: str):
        self.name = name
        self._print_sudoku_grid(sudoku_grid, self.name)
        self._build_matrix(sudoku_grid)
        self.dlx = Dlx(self.matrix)

    def _build_matrix(self, sudoku_grid: list[list]):
        N = 9
        self.matrix = [[0] * (N ** 2 * 4) for _ in range(N ** 3)]
        for r in range(N):
            for c in range(N):
                for d in range(1, N + 1):
                    if sudoku_grid[r][c] == 0 or sudoku_grid[r][c] == d:
                        # row_index
                        row_index = r * (N * N) + c * N + (d - 1)

                        # cell constraint
                        col_index = r * N + c
                        self.matrix[row_index][col_index] = 1

                        # row constraint
                        col_index = r * N + (d - 1) + (N * N)
                        self.matrix[row_index][col_index] = 1

                        # col constraint
                        col_index = (c * N) + (d - 1) + (2 * N * N)
                        self.matrix[row_index][col_index] = 1

                        # box constraint index
                        # box constraint formula:
                        # 3 * N * N + (r//subgrid_size) * subgrid_size * N + (c//subgrid_size) * N + (d - 1)
                        # where subgrid_size for 9 * 9 matrix = 3
                        box_index = r // 3 * 3 + c // 3  # Box constraint
                        col_index = box_index * N + (d - 1) + N * N * 3
                        self.matrix[row_index][col_index] = 1

    def solve(self):
        self.dlx.search(0)
        self._parse_solution()

    def _parse_solution(self):
        N = 9
        self.solution = [[0] * N for _ in range(N)]
        for node in self.dlx.solution:
            right_node = node.right
            while right_node != node:
                row = (right_node.row_index - 1) // N ** 2
                temp = (right_node.row_index - 1) % N ** 2
                col = temp // N
                digit = temp % N + 1
                self.solution[row][col] = digit
                right_node = right_node.right

    def _print_sudoku_grid(self, sudoku_grid, header_msg: str):
        N = 9
        h_count = 0
        print('=' * 31)
        print(f'SUDOKU {header_msg.upper()}'.rjust(22))
        print('=' * 31)
        for row_index in range(N):
            v_count = 0
            if h_count == 3:
                print('-' * 31)
                h_count = 0
            for col_index in range(N):
                if v_count == 3:
                    print('|'.ljust(3), end='')
                    v_count = 0
                print(f'{sudoku_grid[row_index][col_index]}'.ljust(3), end='')
                v_count += 1
            print('')
            h_count += 1
        print('')

    def print_solution(self):
        self._print_sudoku_grid(self.solution, 'solved')


if __name__ == '__main__':
    problem_1 = [
        [9, 0, 4, 6, 7, 0, 3, 0, 1],
        [2, 5, 7, 8, 0, 0, 0, 6, 0],
        [6, 0, 0, 5, 0, 9, 0, 0, 0],
        [0, 7, 0, 0, 1, 0, 0, 9, 2],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [4, 2, 9, 7, 0, 0, 0, 1, 0],
        [0, 3, 2, 0, 5, 0, 9, 4, 0],
        [1, 9, 0, 0, 0, 0, 5, 7, 3],
        [7, 4, 0, 0, 0, 6, 0, 2, 0]
    ]

    problem_2 = [
        [0, 0, 6, 0, 3, 1, 0, 7, 0],
        [4, 3, 7, 0, 0, 5, 0, 0, 0],
        [0, 1, 0, 4, 6, 7, 0, 0, 8],
        [0, 2, 9, 1, 7, 8, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 6],
        [3, 0, 0, 0, 5, 0, 0, 0, 0],
        [8, 0, 5, 0, 0, 4, 9, 1, 0],
        [0, 0, 3, 5, 0, 9, 0, 8, 7],
        [7, 9, 0, 0, 8, 6, 0, 0, 4]
    ]

    problem_3 = [
        [7, 4, 3, 0, 0, 0, 0, 6, 2],
        [0, 5, 0, 1, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 6, 4, 5, 0, 0],
        [9, 6, 0, 0, 7, 0, 0, 0, 5],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [4, 0, 0, 0, 5, 0, 8, 0, 1],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 2, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 9, 6, 8, 0, 0, 5, 0]
    ]

    sudoku_solver = SudokuSolver(problem_1, 'problem 1')
    sudoku_solver.solve()
    sudoku_solver.print_solution()

    sudoku_solver = SudokuSolver(problem_2, 'problem 2')
    sudoku_solver.solve()
    sudoku_solver.print_solution()

    sudoku_solver = SudokuSolver(problem_3, 'problem 3')
    sudoku_solver.solve()
    sudoku_solver.print_solution()
