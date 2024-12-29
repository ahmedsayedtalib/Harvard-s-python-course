import sys
from PIL import Image

# List to store images
images = []

# Loop through command-line arguments (image paths)
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# Save the sequence as an animated GIF
if len(images) > 1:
    images[0].save(
        "planets.gif",  # Output filename should have a `.gif` extension for animations
        save_all=True,  # Required to save as an animation
        append_images=images[1:],  # Add subsequent images
        duration=500,  # Duration in milliseconds between frames
        loop=0  # Infinite loop for the animation
    )
else:
    print("Error: At least two images are required to create an animated image.")
