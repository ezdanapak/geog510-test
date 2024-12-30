from rembg import remove
from PIL import Image
import io

# Load your image
input_path = r'D:/New folder1/IMG_20240613_102437.jpg'  # Replace with your image file path
output_path = r'D:/New folder1/IMG_20240613_1024371.png'  # Output file path (must be PNG for transparency)

# Open the image
with open(input_path, "rb") as input_file:
    input_image = input_file.read()

# Remove the background
output_image = remove(input_image)

# Save the result
with open(output_path, "wb") as output_file:
    output_file.write(output_image)

print(f"Background removed and saved to {output_path}")
