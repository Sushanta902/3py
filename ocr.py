#importing modulw
from PIL import Image 
import pytesseract
#intering executable command  for tesseraact
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract'
#printing string from photo
print(pytesseract.image_to_string(Image.open('path to img')))