from PIL import Image, ImageDraw, ImageFont

# Create a blank canvas
canvas_size = (1000, 1000)
background_color = (255, 255, 255)
image = Image.new("RGB", canvas_size, background_color)
draw = ImageDraw.Draw(image)

image.show()
