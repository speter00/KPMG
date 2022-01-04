from typing import List


class Cube:
    """
    Class for the Cubes in the towers. It's for easily keeping track of which sides are covered,
    and by extension, how many sides are not covered.
    """

    def __init__(self, top_covered=False, bottom_covered=False, right_covered=False, left_covered=False):
        self._top_covered = top_covered
        self._bottom_covered = bottom_covered
        self._right_covered = right_covered
        self._left_covered = left_covered

        # number of sides not covered
        self._open_sides = 6 - int(top_covered) - int(bottom_covered) - int(right_covered) - int(left_covered)

    @property
    def top_covered(self):
        return self._top_covered

    # everytime we change whether a side is covered, the number of open_sides must be refreshed

    @top_covered.setter
    def top_covered(self, covered):
        self._top_covered = covered
        self._open_sides = 6 - int(self.top_covered) - int(self.bottom_covered) - int(
            self.right_covered) - int(self.left_covered)

    @property
    def bottom_covered(self):
        return self._bottom_covered

    @bottom_covered.setter
    def bottom_covered(self, covered):
        self._bottom_covered = covered
        self._open_sides = 6 - int(self.top_covered) - int(self.bottom_covered) - int(
            self.right_covered) - int(self.left_covered)

    @property
    def right_covered(self):
        return self._right_covered

    @right_covered.setter
    def right_covered(self, covered):
        self._right_covered = covered
        self._open_sides = 6 - int(self.top_covered) - int(self.bottom_covered) - int(
            self.right_covered) - int(self.left_covered)

    @property
    def left_covered(self):
        return self._left_covered

    @left_covered.setter
    def left_covered(self, covered):
        self._left_covered = covered
        self._open_sides = 6 - int(self.top_covered) - int(self.bottom_covered) - int(
            self.right_covered) - int(self.left_covered)

    @property
    def open_sides(self):
        return self._open_sides


def cube_towers_surface(heights: List[int]) -> int:
    """
    Function for Exercise 1. This function returns the surface area of connected towers of cubes.

    :param heights: the heights of the cube towers
    :return: the surface area of the towers
    """

    surface = 0  # surface area to return
    for i in range(len(heights)):
        for cube in range(1, heights[i] + 1):  # cube 1 is the bottom cube, cube heights[i] is the top cube
            inspected_cube = Cube()
            if cube > 1:  # if cube isn't the bottom cube
                inspected_cube.bottom_covered = True
            if cube < heights[i]:  # if cube isn't the top cube
                inspected_cube.top_covered = True
            if i > 0:  # if tower isn't the leftmost tower, inspect left side
                if heights[i - 1] >= cube:  # if the left tower's top cube is higher (or level) than the current cube,
                    # there must be a cube to the left

                    inspected_cube.left_covered = True
            if i < len(heights) - 1:  # if tower isn't the rightmost tower, inspect right side
                if heights[i + 1] >= cube:  # same idea as with the left side check
                    inspected_cube.right_covered = True
            surface += inspected_cube.open_sides

    return surface
