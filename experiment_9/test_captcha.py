# Import the following modules
from captcha.image import ImageCaptcha
from PIL import Image, ImageDraw, ImageFont
import io

# Create an image instance of the given size
image = ImageCaptcha(width=280, height=90)

# Image captcha text
captcha_text = 'GeeksforGeeks'

# Generate the image of the given text
data = image.generate(captcha_text)

# Convert image data to PIL Image
pil_image = Image.open(io.BytesIO(data.read()))

# Create a new image with enough space for the text "Hello" above the captcha image
new_image = Image.new('RGB', (280, 130), color='white')

# Paste the captcha image onto the new image
new_image.paste(pil_image, (0, 40))

# Create a drawing context
draw = ImageDraw.Draw(new_image)

# Define font and font size for the "Hello" text
font = ImageFont.truetype("arial.ttf", 20)

# Define text position for the "Hello" text
text_position = (10, 10)  # Adjust position as needed

# Draw the "Hello" text on the new image
draw.text(text_position, "Hello", fill="black", font=font)

# Display the new image
new_image.show()
