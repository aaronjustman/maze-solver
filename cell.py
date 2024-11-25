from geometry import Point, Line


class Cell:

    def __init__(self, p1, p2, window=None):
        self.p1 = p1
        self.p2 = p2
        self.window = window
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self.fill_color = "gray"
        self.visited = False
        self.entrance = False
        self.exit = False

    def draw_move(self, to_cell, undo=False):
        line_color = "red"
        if undo:
            line_color = "gray20"

        width1 = self.p2.x - self.p1.x
        height1 = self.p2.y - self.p1.y
        mid1x = self.p1.x + (width1 / 2)
        mid1y = self.p1.y + (height1 / 2)

        width2 = to_cell.p2.x - to_cell.p1.x
        height2 = to_cell.p2.y - to_cell.p1.y
        mid2x = to_cell.p1.x + (width2 / 2)
        mid2y = to_cell.p1.y + (height2 / 2)

        line = Line(Point(mid1x, mid1y), Point(mid2x, mid2y))
        line.draw(self.window.canvas, line_color)

    def draw(self):
        if not self.window:
            return

        height = self.p2.y - self.p1.y
        top_right = Point(self.p2.x, self.p2.y - height)
        bottom_left = Point(self.p1.x, self.p1.y + height)

        wall = Line(self.p1, bottom_left)
        if self.left_wall:
            wall.draw(self.window.canvas, self.fill_color)
        else:
            wall.draw(self.window.canvas, "gray20")

        wall = Line(top_right, self.p2)
        if self.right_wall:
            wall.draw(self.window.canvas, self.fill_color)
        else:
            wall.draw(self.window.canvas, "gray20")

        wall = Line(self.p1, top_right)
        if self.top_wall:
            wall.draw(self.window.canvas, self.fill_color)
        else:
            wall.draw(self.window.canvas, "gray20")

        wall = Line(bottom_left, self.p2)
        if self.bottom_wall:
            wall.draw(self.window.canvas, self.fill_color)
        else:
            wall.draw(self.window.canvas, "gray20")
