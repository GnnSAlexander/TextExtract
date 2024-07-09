from PIL import Image
import pytesseract

def read_text_from_image(image_path):
    # Abrir la imagen
    image = Image.open(image_path)
    
    # Usar pytesseract para extraer texto
    text = pytesseract.image_to_string(image)
    
    return text

# Ruta de tu imagen
image_path = 'capture.png'  # Cambia esto a la ruta de tu imagen

# Leer el texto
extracted_text = read_text_from_image(image_path)

# Imprimir el texto extraído
print("Texto extraído de la imagen:")
print(extracted_text)