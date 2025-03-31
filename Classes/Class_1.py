class Goat():
    def __init__(self, height = 1, weight = 0.5):
        self.height = height
        self.weight = weight
    def __str__(self):
        s = "height = " + str(self.height) + " weight = " + str(self.weight)
        return s
    def voice (self):
        if self.height <= 1:
            print("mee")
        else:
            print("bee")

marshal = Goat(2,9)
sokrat = Goat(0.1, 2)
marshal.voice()
sokrat.voice()
print(marshal)
