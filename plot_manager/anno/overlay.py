from plot_manager.anno import annotation
import pandas as pd
import matplotlib.patches as patch
from matplotlib.collections import PatchCollection

class OverlayBBFromLabelRegions(annotation.Annotation):

    def draw(self):

        regions_bbox = pd.read_csv("process/regions.csv", header=None)

        patches = []
        for i,regions in enumerate(regions_bbox.itertuples(index=False)):
            new_patch = patch.Rectangle((regions[1],regions[0]),regions[3]-regions[1],regions[2]-regions[0], fill=True, linestyle="dashed", alpha=0.4, linewidth=0.5, edgecolor="white", facecolor="white")

            self.ax.text(regions[1]+10, regions[0]-10, str(i), fontsize=20, color="white")

            patches.append(new_patch)

        patch_collection = PatchCollection(patches,match_original=True)

        self.ax.add_collection(patch_collection)
        print(patches)
        print(regions_bbox)
        pass