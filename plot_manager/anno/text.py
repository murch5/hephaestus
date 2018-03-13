from anno import annotation

class Text(annotation.Annotation):

    def draw(self):

        c = self.get("color")
        if c is None:
            c = "w"
        self.ax.text(self.x,self.y,self.s, fontsize=36, transform=self.ax.transAxes,color=c)

        pass
