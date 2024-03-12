import random, io
from captcha.image import ImageCaptcha
from PIL import Image, ImageDraw, ImageFont
c_l_r1 = random.randint(4, 10)
# print(f'Randomly Generated CAPTCHA length is {c_l_r1}')
captcha = ""
char = 0
for character in range(0, c_l_r1):
    char += 1
    # for each character, generating a random number to determine whether that character should be a number or an alphabet
    char_type_r2 = random.randint(0, 10)
    # print(f'For character {char}, random number generated is {char_type_r2}')
    if char_type_r2 < 6:
        # the character should be a number
        char_value_r3 = random.randint(0, 9)
        # print(f'For character {char} of the CAPTCHA, the value is {char_value_r3}')
    else:
        # the character should be a alphabet
        char_value_r3 = random.randint(65, 90)
        char_value_r3 = chr(char_value_r3)
        # print(f'For character {char} of the CAPTCHA, the value is {char_value_r3}')
    captcha = captcha + str(char_value_r3)
    # print('------------------------------------------------')
# print(f'CAPTCHA Generated is {captcha}')
# Create an image instance of the given size
image_inst = ImageCaptcha(width=300, height=100)
# Create the image of the generated captcha
image = image_inst.generate(captcha)
# Convert image to PIL image
pil_image = Image.open(io.BytesIO(image.read()))
# Display captcha image
# pil_image.show()
# Create a new image with space for text above captcha
disp_image = Image.new('RGB', (600, 140), color='white')
# Paste the captcha on top of display image
disp_image.paste(pil_image, (0, 40))
# Create a drawing context
draw = ImageDraw.Draw(disp_image)
# Define font and fontsize for the text
font = ImageFont.truetype("arial.ttf", 20)
# Define text position
text_position = (10, 10)
# Draw the text on the image
draw.text(text_position, "Note down the CAPTCHA and enter it after closing the window.", fill='black', font=font)
# Display
disp_image.show()
enter_captcha = input('Enter the CAPTCHA: ')
if enter_captcha == captcha:
    print('CAPTCHA Authentication Successful.')
else:
    print('CAPTCHA Authentication Unsuccessful.')
