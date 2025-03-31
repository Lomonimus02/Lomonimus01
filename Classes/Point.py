class Point():
    def __init__(self, Y_axis, X_axis):
        self.Y_axis = Y_axis
        self.X_axis = X_axis

    def reset(self):
        self.Y_axis = 0
        self.X_axis = 0
        return self.Y_axis, self.X_axis

    def calculate_distance(self):
        dist = (self.Y_axis * self.Y_axis + self.X_axis * self.X_axis)**0.5
        return dist

    def __str__(self):
        result = "Y_axis = " + str(self.Y_axis) + " X_axis = " + str(self.X_axis)
        return result


point = Point(4, 5)
print(point)

s = point.calculate_distance()
print(s)

d = point.reset()
print(d)


