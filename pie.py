import animPlot as animPlot

class pie(animPlot.animPlot):

    def __init__(self, figure, data, position):
        animPlot.animPlot.__init__(self, figure, data, position)
        return

    def animate(self,i):
        return

    def draw(self):
        print("test")
        print(self.getData())
        print(type(self.data))

        self.subplot.pie(self.data)
        self.subplot.axis("equal")

        return

    def initAnimate(self, i):
        return

