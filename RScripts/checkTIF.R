library(raster)
library(terra)

# Define the path to the .tif file
tif_file <- "C:/Users/Jorge A. Rivera/Downloads/202412_20241226_00004.tif"

# Open the .tif file using terra
raster_data <- rast(tif_file)

# Check the number of bands in the raster data
num_bands <- nlyr(raster_data)
print(paste("Number of bands:", num_bands))

# Normalize the bands to the range 0-1
normalize_band <- function(band) {
  band <- band / max(band[], na.rm = TRUE)
  return(band)
}

# Read and normalize the Red, Green, Blue, and NIR bands
red <- normalize_band(raster_data[[1]])
green <- normalize_band(raster_data[[2]])
blue <- normalize_band(raster_data[[3]])
nir <- normalize_band(raster_data[[4]])

# Create an RGB-NIR stack
rgb_nir_stack <- c(red, green, blue)
rgb_nir_stack <- c(red, green, blue, nir)

# Plot the RGB-NIR image
plotRGB(rgb_nir_stack, r = 1, g = 2, b = 3, stretch = "lin")
title("Map 2023 - RGB-NIR Composite")
