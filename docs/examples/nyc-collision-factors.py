import geopandas as gpd
import geoplot as gplt
import geoplot.crs as gcrs
import matplotlib.pyplot as plt

# load the data
nyc_boroughs = gpd.read_file(gplt.datasets.get_path('nyc_boroughs'))
nyc_collision_factors = gpd.read_file(gplt.datasets.get_path('nyc_collision_factors'))


proj = gcrs.AlbersEqualArea(central_latitude=40.7128, central_longitude=-74.0059)
fig = plt.figure(figsize=(10,5))
ax1 = plt.subplot(121, projection=proj)
ax2 = plt.subplot(122, projection=proj)

gplt.kdeplot(
    nyc_collision_factors[
        nyc_collision_factors['CONTRIBUTING FACTOR VEHICLE 1'] == "Failure to Yield Right-of-Way"
    ],
    projection=proj,
    shade=True, shade_lowest=False, 
    clip=nyc_boroughs.geometry,
    ax=ax1
)
gplt.polyplot(nyc_boroughs, projection=proj, ax=ax1)
plt.title("Failure to Yield Right-of-Way Crashes, 2016")

gplt.kdeplot(
    nyc_collision_factors[
        nyc_collision_factors['CONTRIBUTING FACTOR VEHICLE 1'] == "Lost Consciousness"
    ],
    projection=proj,
    shade=True, shade_lowest=False,
    clip=nyc_boroughs.geometry,
    ax=ax2
)
gplt.polyplot(nyc_boroughs, projection=proj, ax=ax2)
plt.title("Loss of Consciousness Crashes, 2016")

plt.savefig("nyc-collision-factors.png", bbox_inches='tight', pad_inches=0.1)
