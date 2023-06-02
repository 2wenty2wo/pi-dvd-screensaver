import time
import adafruit_ssd1306
import digitalio
import board
from PIL import Image, ImageDraw, ImageOps
import busio
import random
import atexit

# Set up buttons
BUTTON_A = digitalio.DigitalInOut(board.D5)
BUTTON_A.switch_to_input(pull=digitalio.Pull.UP)
BUTTON_B = digitalio.DigitalInOut(board.D6)
BUTTON_B.switch_to_input(pull=digitalio.Pull.UP)
BUTTON_UP = digitalio.DigitalInOut(board.D17)
BUTTON_UP.switch_to_input(pull=digitalio.Pull.UP)
BUTTON_DOWN = digitalio.DigitalInOut(board.D22)
BUTTON_DOWN.switch_to_input(pull=digitalio.Pull.UP)
BUTTON_LEFT = digitalio.DigitalInOut(board.D27)
BUTTON_LEFT.switch_to_input(pull=digitalio.Pull.UP)
BUTTON_RIGHT = digitalio.DigitalInOut(board.D23)
BUTTON_RIGHT.switch_to_input(pull=digitalio.Pull.UP)

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the SSD1306 OLED class.
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (disp.width, disp.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Load the DVD logo image.
logo = Image.open("dvd_logo.bmp").convert("1")  # Convert to 1-bit mode
logo = logo.resize((32, 16))  # Resize the image

# Initial position
x = random.randint(0, disp.width - logo.width)
y = random.randint(0, disp.height - logo.height)

# Velocity
dx = random.choice([-1, 1]) * 2
dy = random.choice([-1, 1]) * 2

# Create Adafruit SSD1306 display instance
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

def clear_display():
    # Clear display.
    disp.fill(0)
    disp.show()

# Register the clear_display function to run when the script exits.
atexit.register(clear_display)

# Screen inversion flag
inverted = False

while True:
    try:
        # Check button states
        if not BUTTON_UP.value:
            dy = -1 * abs(dy)
            print("Button Up pressed")
        if not BUTTON_DOWN.value:
            dy = abs(dy)
            print("Button Down pressed")
        if not BUTTON_LEFT.value:
            dx = -1 * abs(dx)
            print("Button Left pressed")
        if not BUTTON_RIGHT.value:
            dx = abs(dx)
            print("Button Right pressed")
        if not BUTTON_B.value:
            inverted = not inverted
            display.invert(inverted)
            print(f"Screen inversion toggled: {inverted}")

        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, disp.width, disp.height), outline=0, fill=0)

        # Draw the logo.
        image.paste(logo, (x, y))

        # Show image.
        display.image(image)
        display.show()

        # Move position for next frame.
        x += int(dx)
        y += int(dy)

        # Bounce if hit the edge of the display.
        if not 0 <= x <= disp.width - logo.width:
            dx = -dx
        if not 0 <= y <= disp.height - logo.height:
            dy = -dy

        # Small delay to slow down the animation.
        time.sleep(0.01)

    except Exception as e:
        print(f"Error in main loop: {e}")
