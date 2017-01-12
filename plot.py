

class plot():

    def __init__(self,figure, data, position):
        self.figure = figure
        self.data = data
        self.position = position
        self.subplot = figure.add_subplot(position, aspect="equal")

    def animate(self,i):
        return;

    def initAnimate(self, i):
        return;

    def draw(self):
        return;

    def init(self):
        return;
