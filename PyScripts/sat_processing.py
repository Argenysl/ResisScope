import ee
import geemap

ee.Authenticate()
ee.Initialize(project="resisscope")

def create_polygon(lat, lon, buffer):
    point = ee.Geometry.Point(lon, lat)
    polygon = point.buffer(buffer)
    return polygon

def generate_map(polygon, year, output_path):
    # Define the region of interest
    region = polygon.bounds().getInfo()['coordinates']

    # Get a high-resolution satellite image for the specified year
    image = ee.ImageCollection('USDA/NAIP/DOQQ') \
                .filterDate(f'{year}-01-01', f'{year}-12-31') \
                .filterBounds(polygon) \
                .mosaic() \
                .clip(polygon)

    # Export the image to a local file
    geemap.ee_export_image(image, filename=output_path, scale=0.6, region=region)

def main(lat, lon, buffer, year, output_path):
    polygon = create_polygon(lat, lon, buffer)
    print(f'Starting to process the map for {year}...')
    generate_map(polygon, year, output_path)

    print(f'Map for {year} has been saved to {output_path}.')

