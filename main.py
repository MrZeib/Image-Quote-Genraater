# Auther   : Shahzaib
# Language : Python

from PIL import Image, ImageDraw, ImageFont

def generate_quote_image(output_path,
                         quote_text,
                         font_size=20,
                         img_color="red"):
  # Create a new image
  image = Image.new('RGB', (800, 400), color=img_color)

  # Create a drawing object
  draw = ImageDraw.Draw(image)

  # Use the default bitmap font with the specified size for the quote
  quote_font = ImageFont.load_default(font_size)

  # Specify text color
  text_color = (255, 255, 255)  # RGB format
  # Calculate the position for centering the text
  quote_position = 240, 150

  # Add the quote text to the image with the specified font size
  draw.text(quote_position, quote_text, font=quote_font, fill=text_color)

  # Save the image with the quote and font size information
  image.save(output_path)

# Example usage
output_path = "quote.jpg"
quote_text = input("Enter Your Quote: ")
font_size = 60  # Adjust the font size for the quote based on your preference
image_color = input("Enter Color For Image Bagroud: ")

generate_quote_image(output_path, quote_text.title(), font_size,
                     image_color.lower())
