from plot_manager.anno import annotation

class Text(annotation.Annotation):

    def draw(self):

        print("booya")
        print(self.s)
        self.ax.text(self.x,self.y,self.s, fontsize=12, transform=self.ax.transAxes)

        pass


