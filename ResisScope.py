<<<<<<< HEAD
import ee

# Authenticate and initialize the Earth Engine API
ee.Authenticate()
ee.Initialize(project="resisscope")

# Example function to create a polygon and generate a map
def create_polygon(lat, lon, buffer):
    point = ee.Geometry.Point(lon, lat)
    polygon = point.buffer(buffer)
    return polygon

def generate_map(polygon, year):
    # Define the region of interest
    region = polygon.bounds().getInfo()['coordinates']

    # Get a high-resolution satellite image for the specified year
    image = ee.ImageCollection('USDA/NAIP/DOQQ') \
                .filterDate(f'{year}-01-01', f'{year}-12-31') \
                .filterBounds(polygon) \
                .mosaic() \
                .clip(polygon)

    # Export the image to Google Drive
    task = ee.batch.Export.image.toDrive(image=image,
                                         description=f'map_{year}',
                                         folder='EarthEngine',
                                         fileNamePrefix=f'map_{year}',
                                         region=region,
                                         scale=1)  # 1 meter per pixel
    task.start()




def main(lat, lon, buffer, year):
    polygon = create_polygon(lat, lon, buffer)
    generate_map(polygon, year)
    print(f'Map for {year} is being processed and will be saved to your Google Drive.')

# Example usage for Omaha, Nebraska
main(41.2565, -95.9345, 10, 2024)
=======
print("Initial Commit")
>>>>>>> b53280c7f104b24ca98ba87eec91b3b51ff88deb
