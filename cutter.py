import numpy as np
from PIL import Image
import easyocr

def extract_text_from_images(cropped_images):
    """Use EasyOCR to extract text from provided images."""
    reader = easyocr.Reader(['en', 'es'])  # Initialize with English and Spanish.
    texts = []
    for img in cropped_images:
        np_img = np.array(img)  # Convert PIL Image to numpy array
        result = reader.readtext(np_img)  # Now we pass a numpy array to EasyOCR
        extracted_text = ' '.join([item[1] for item in result])
        texts.append(extracted_text)
    return texts

# Cargar imagen
img = Image.open('_share_auto_2024_3_9_19_27_26.png')

# Coordenadas para recorte de los nombres del Equipo A y B
coordenadas_A = (272, 133, 429, 639)
coordenadas_B = (1010, 133, 1170, 639)

# Recorte de imágenes
recorte_A = img.crop(coordenadas_A)
recorte_B = img.crop(coordenadas_B)

# Extraer texto de las imágenes de recorte
nombres_equipo_A = extract_text_from_images([recorte_A])
nombres_equipo_B = extract_text_from_images([recorte_B])

# Guardar los nombres en un archivo de texto
with open('nombres_equipos.txt', 'w') as file:
    file.write(f'Nombres del Equipo A: {nombres_equipo_A}\n')
    file.write(f'Nombres del Equipo B: {nombres_equipo_B}\n')
