from window import Window
from geometry import Point, Line
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(10, 10, 10, 14, 25, 25, win)
    maze.break_walls()
    maze.break_entrance_and_exit()
    maze.reset_visited()
    maze.solve()

    win.wait_for_close()

# test functions


def draw_lines(win):
    p1 = Point(10, 15)
    p2 = Point(100, 150)
    line1 = Line(p1, p2)
    p3 = Point(250, 275)
    p4 = Point(425, 75)
    line2 = Line(p3, p4)
    p5 = Point(50, 56)
    p6 = Point(50, 356)
    line3 = Line(p5, p6)

    win.draw_line(line1, "red")
    win.draw_line(line2, "yellow")
    win.draw_line(line3, "purple")


def draw_cells(win):
    p1 = Point(10, 15)
    p2 = Point(60, 65)
    cell1 = Cell(p1, p2, win)

    p3 = Point(125, 175)
    p4 = Point(175, 225)
    cell2 = Cell(p3, p4, win)
    cell2.top_wall = False

    p5 = Point(250, 56)
    p6 = Point(300, 106)
    cell3 = Cell(p5, p6, win)
    cell3.left_wall = False
    cell3.bottom_wall = False

    cell1.draw()
    cell2.draw()
    cell3.draw()

    cell_move(cell1, cell2)
    cell_move(cell2, cell3)


def cell_move(cell1, cell2):
    cell1.draw_move(cell2)


main()
