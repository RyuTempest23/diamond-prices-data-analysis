from PIL import Image
from rembg import new_session, remove

input_path = "diamond.jpeg"
output_path = "diamond_no_bg.png"

# Load the lightweight 'u2netp' model instead of the default
session = new_session("u2netp")

input_image = Image.open(input_path)
output_image = remove(input_image, session=session)
output_image.save(output_path)

print(f"Saved: {output_path}")
