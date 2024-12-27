import random
from datetime import datetime
from tqdm import tqdm
from sat_processing import main as sat_process

def random_lat_lon():
    # Approximate bounding box for the continental USA
    lat_min, lat_max = 41.0, 41.4
    lon_min, lon_max = -96.0, -95.8
    lat = random.uniform(lat_min, lat_max)
    lon = random.uniform(lon_min, lon_max)
    return lat, lon

def random_year():
    return random.randint(2003, 2024)

# Example usage for Omaha, Nebraska
buffer = 50
satellite_date = "202412"
today_date = datetime.now().strftime("%Y%m%d")

for i in range(1, 6):
    lat, lon = random_lat_lon()
    year = random.randint(2003, 2024)
    output_path = f"C:/Users/Jorge A. Rivera/Downloads/{satellite_date}_{today_date}_{i:05d}.tif"
    sat_process(lat, lon, buffer, year, output_path)
