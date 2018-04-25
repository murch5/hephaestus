import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import ticker
import cartopy
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import geopandas as gpd




from type import anim_plot


class Map(anim_plot.AnimPlot):
    def draw(self):


        map_path = self.get("map_source_path")
        world_map_data = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

        world_map_data = world_map_data[world_map_data.name != "Antarctica"]

        col = self.data[0].columns.values.tolist()[0]

        world_map_master = world_map_data.merge(self.data[0], left_on="iso_a3", right_index=True)

        world_map_data.plot(ax=self.subplot, color="white", edgecolor="grey", linewidth=0.5)

        self.subplot.axis("off")
        ##FIND NAME OF SECOND COLUMN by func
        ###
        ###
        ###
        ###YlOrRd

        world_map_master.plot(ax=self.subplot, column=col, cmap='PuBuGn',scheme='fisher_jenks', edgecolor="grey",linewidth=0.5)

        self.subplot.set_aspect("equal")

        self.color_bar_overlay = plt.axes([.20, .33, .025, .130], facecolor="w")

        self.color_norm = mpl.colors.Normalize(vmin=0, vmax=self.data[0].max())

        self.color_scalar_mapper = plt.cm.ScalarMappable(cmap='PuBuGn', norm=self.color_norm)

        self.color_scalar_mapped = self.color_scalar_mapper.set_array(self.data[0].values)

        self.col_bar = plt.colorbar(self.color_scalar_mapper,cax=self.color_bar_overlay)

        self.color_bar_overlay.set_title(self.get("cb_title"))

        self.color_bar_overlay.tick_params(axis="both", length=5, pad=0.2)
        #self.col_bar.set_ticks(self.color_scalar_mapped)

        tick_locator = ticker.MaxNLocator(nbins=5)
        self.col_bar.locator = tick_locator
        self.col_bar.update_ticks()

        plt.rc("font",family="Helvetica")

        print(plt.rcParams.keys())

        plt.rcParams['font.sans-serif'] = ["Helvetica", "sans-serif"]


        ## CODE FOR USING CARTOPY
        # shpfilename = shpreader.natural_earth(resolution='110m',
        #                                       category='cultural',
        #                                       name='admin_0_countries')
        #
        # reader = shpreader.Reader(shpfilename)
        # countries = reader.records()
        #
        # geoms = reader.geometries()
        #
        # region_lvl = self.get("region_level")
        #
        # self.subplot = plt.axes(projection=ccrs.Robinson())
        #
        # self.subplot.set_extent([-150, 60, -25, 60])
        #
        # self.subplot.add_feature(cartopy.feature.COASTLINE)
        #
        # self.subplot.add_geometries(list(reader.geometries()),ccrs.Robinson(),
        #                           facecolor="black", edgecolor="black")
        # for country in countries:
        #     name = country.attributes.get("ADMIN")
        #
        #     if name in self.data[0].index:
        #         print("captured")
        #         new_geo = self.subplot.add_geometries(country.geometry, ccrs.Robinson(),
        #                           facecolor="black", edgecolor="black",
        #                           label=country.attributes['ADMIN'])



        return
