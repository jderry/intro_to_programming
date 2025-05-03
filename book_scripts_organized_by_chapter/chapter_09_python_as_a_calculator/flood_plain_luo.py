''' AUTHOR: Linchao Luo
    Given tiff filename in the datafile home directory,
    returns a screen image of tiff 
    on which user draws a polygon to bound area of interest.
    Machine then calculates percent flood plain within polygon
    and returns an image of the selected area.
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import PolygonSelector

# shapely, rasterio, and pyproj
# render and allow manipulation of image
from shapely.geometry import Polygon, mapping 
# https://shapely.readthedocs.io/en/stable/
import rasterio 
# https://rasterio.readthedocs.io/en/stable/
from rasterio.features import geometry_mask
from rasterio.enums import Resampling
from pyproj import Transformer 
# https://pyproj4.github.io/pyproj/stable/

import os

home_dir = os.path.expanduser('~')

# Path to your TIFF file
tiff_path = f"{home_dir}/datafile/TX_North1_HTF_MINOR_FY20.tif"

# Open the raster file
with rasterio.open(tiff_path) as src:
    print(f"Raster CRS: {src.crs}")
    print("Raster Bounds:", src.bounds)

    # Downsample the raster for visualization
    factor = 2
    data = src.read(
        1,
        out_shape=(int(src.height // factor), int(src.width // factor)),
        resampling=Resampling.nearest,
    )
    transform = src.transform * src.transform.scale(factor, factor)

# Store the selected coordinates
selected_coords = []

# Callback function for the PolygonSelector
def on_select(vertices):
    global selected_coords
    selected_coords = vertices
    plt.close()

# Interactive plot
fig, ax = plt.subplots(figsize=(12, 8))
im = ax.imshow(data, cmap="terrain", extent=(src.bounds.left, src.bounds.right, src.bounds.bottom, src.bounds.top))
ax.set_title("Click to select an area on the map")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
plt.colorbar(im, ax=ax, label="Blue Represents Inundated Areas")

# Create a PolygonSelector
selector = PolygonSelector(ax, on_select, useblit=True)
plt.show()

# Process the selected coordinates
if selected_coords:
    print("Selected coordinates:", selected_coords)

    # Check if coordinates are within raster bounds
    valid_coords = []
    for x, y in selected_coords:
        if (src.bounds.left <= x <= src.bounds.right) and (src.bounds.bottom <= y <= src.bounds.top):
            valid_coords.append((x, y))
        else:
            print(f"Coordinate out of bounds: ({x}, {y})")

    # Proceed with the valid coordinates
    if valid_coords:
        polygon = Polygon(valid_coords)
        mask = geometry_mask([mapping(polygon)], transform=transform, invert=True, out_shape=data.shape)
        masked_data = np.ma.masked_array(data, mask=~mask)

        # Debugging step: Show how the mask looks
        print(f"Mask shape: {mask.shape}")
        print(f"Masked data shape: {masked_data.shape}")

        # Get unique values within the mask
        unique_values = np.unique(masked_data.compressed())
        print("Unique values in selected area:", unique_values)

        flooded_threshold = np.min(unique_values[unique_values > 0])  # Assume minimum non-zero value for flooding
        print(f"Suggested Flooded Threshold: {flooded_threshold}")

        flooded_pixels_area = np.count_nonzero((masked_data > flooded_threshold) & (~masked_data.mask))
        total_pixels_area = np.count_nonzero(~masked_data.mask)
        flood_percentage = (flooded_pixels_area / total_pixels_area) * 100 if total_pixels_area else 0

        print("Total Pixels in Selected Area:", total_pixels_area)
        print("Flooded Pixels in Selected Area:", flooded_pixels_area)
        print("Flooded Area Percentage: {:.2f}%".format(flood_percentage))

        # Display the original raster with the mask overlay
        plt.figure(figsize=(12, 8))
        plt.imshow(data, cmap="terrain", extent=(src.bounds.left, src.bounds.right, src.bounds.bottom, src.bounds.top))
        plt.imshow(mask, cmap="gray", alpha=0.5, extent=(src.bounds.left, src.bounds.right, src.bounds.bottom, src.bounds.top))
        plt.title("Raster with Selected Area Mask Overlay")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.colorbar(label="Flood Depth")
        plt.show()
else:
    print("No area selected.")
