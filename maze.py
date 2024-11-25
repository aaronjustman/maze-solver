from cell import Cell
from geometry import Point
import time
import random


class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = win
        self.total_visited = 0

        if seed:
            random.seed(seed)

        self.create_cells()

    def create_cells(self):
        self.cells = []

        for row in range(self.num_rows):
            new_row = []

            for col in range(self.num_cols):
                x1 = col * self.cell_size_x + self.x1
                y1 = row * self.cell_size_y + self.y1
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y

                cell = Cell(Point(x1, y1), Point(x2, y2), self.window)
                cell.draw()
                self.animate()

                new_row.append(cell)

            self.cells.append(new_row)

        self.cells[0][0].entrance = True
        self.cells[self.num_rows - 1][self.num_cols - 1].exit = True

        self.animate()

    def animate(self):
        if not self.window:
            return

        self.window.redraw()
        time.sleep(0.01)

    def break_walls(self, r=0, c=0):
        self.cells[r][c].visited = True

        while True:
            positions = []
            if r != 0 and not self.cells[r - 1][c].visited:
                positions.append((-1, 0))  # top cell
            if c != 0 and not self.cells[r][c - 1].visited:
                positions.append((0, -1))  # left cell
            if r < self.num_rows - 1 and not self.cells[r + 1][c].visited:
                positions.append((1, 0))  # bottom cell
            if c < self.num_cols - 1 and not self.cells[r][c + 1].visited:
                positions.append((0, 1))  # right cell

            if len(positions) == 0:
                self.cells[r][c].draw()
                self.animate()
                return

            next_pos = positions[random.randint(0, len(positions) - 1)]
            rr = r
            rr += next_pos[0]
            cc = c
            cc += next_pos[1]
            if rr < r:
                self.cells[r][c].top_wall = False
                self.cells[rr][cc].bottom_wall = False
            if cc < c:
                self.cells[r][c].left_wall = False
                self.cells[rr][cc].right_wall = False
            if rr > r:
                self.cells[r][c].bottom_wall = False
                self.cells[rr][cc].top_wall = False
            if cc > c:
                self.cells[r][c].right_wall = False
                self.cells[rr][cc].left_wall = False

            self.break_walls(rr, cc)

    def break_entrance_and_exit(self):
        rando = random.randint(0, 1)
        if rando == 1:
            self.cells[0][0].top_wall = False
        else:
            self.cells[0][0].left_wall = False
        self.cells[0][0].draw()

        rando = random.randint(0, 1)
        if rando == 1:
            self.cells[self.num_rows -
                       1][self.num_cols - 1].bottom_wall = False
        else:
            self.cells[self.num_rows - 1][self.num_cols - 1].right_wall = False
        self.cells[self.num_rows - 1][self.num_cols - 1].draw()

    def reset_visited(self):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self.cells[r][c].visited = False

    def solve(self):
        return self.solve_r(0, 0)

    def solve_r(self, r, c):
        self.animate()
        self.cells[r][c].visited = True

        if self.cells[r][c].exit:
            return True

        worked_out = False

        # top cell
        if r != 0 and not self.cells[r][c].top_wall and not self.cells[r - 1][c].visited:
            worked_out = True
            self.cells[r][c].draw_move(self.cells[r - 1][c])
            if self.solve_r(r - 1, c):
                return True
            else:
                self.cells[r][c].draw_move(self.cells[r - 1][c], True)

        # left cell
        if c != 0 and not self.cells[r][c].left_wall and not self.cells[r][c - 1].visited:
            worked_out = True
            self.cells[r][c].draw_move(self.cells[r][c - 1])
            if self.solve_r(r, c - 1):
                return True
            else:
                self.cells[r][c].draw_move(self.cells[r][c - 1], True)

        # bottom cell
        if r < self.num_rows - 1 and not self.cells[r][c].bottom_wall and not self.cells[r + 1][c].visited:
            worked_out = True
            self.cells[r][c].draw_move(self.cells[r + 1][c])
            if self.solve_r(r + 1, c):
                return True
            else:
                self.cells[r][c].draw_move(self.cells[r + 1][c], True)

        # right cell
        if c < self.num_cols - 1 and not self.cells[r][c].right_wall and not self.cells[r][c + 1].visited:
            worked_out = True
            self.cells[r][c].draw_move(self.cells[r][c + 1])
            if self.solve_r(r, c + 1):
                return True
            else:
                self.cells[r][c].draw_move(self.cells[r][c + 1], True)

        if not worked_out:
            return False
