from google.colab import drive
drive.mount('/content/drive')

from PIL import Image
import numpy as np

# Tamanho da imagem
largura, altura = 1000, 1000

# 1. Imagem binária (1 bit por pixel)
# Criando uma matriz de pixels binários (1 bit por pixel)
binary_matrix = np.zeros((altura, largura), dtype=np.uint8)  # 0 = branco

# Criando uma linha preta na coluna 50
binary_matrix[:, 50] = 1  # 1 = preto (assumindo que 1 representa preto)

# Convertendo para imagem
imagem_binaria = Image.fromarray(binary_matrix * 255, mode='1')  # Modo '1' para binário
imagem_binaria.save('/content/drive/My Drive/imagem_binaria.png')
imagem_binaria.show()

# 2. Imagem com 8 bits por pixel (tons de cinza)
# Criando uma matriz de pixels em tons de cinza
gray_matrix = np.zeros((altura, largura), dtype=np.uint8)

# Criando uma linha cinza na coluna 50
gray_matrix[:, 50] = 128  # 128 representa um tom de cinza

# Convertendo para imagem
imagem_gray = Image.fromarray(gray_matrix, mode='L')
imagem_gray.save('/content/drive/My Drive/imagem_gray.png')
imagem_gray.show()

# 3. Imagem com 3 conjuntos de 8 bits por pixel (RGB)
# Criando uma matriz de pixels em RGB
rgb_matrix = np.zeros((altura, largura, 3), dtype=np.uint8)

# Criando uma linha verde na coluna 50
rgb_matrix[:, 50] = [0, 255, 0]  # Verde

# Convertendo para imagem
imagem_rgb = Image.fromarray(rgb_matrix, mode='RGB')
imagem_rgb.save('/content/drive/My Drive/imagem_rgb.png')
imagem_rgb.show()

# 4. Imagem com 4 conjuntos de 8 bits por pixel (RGBA)
# Criando uma matriz de pixels em RGBA
rgba_matrix = np.zeros((altura, largura, 4), dtype=np.uint8)

# Criando uma linha verde na coluna 50 com transparência
rgba_matrix[:, 50] = [0, 255, 0, 128]  # Verde com transparência

# Convertendo para imagem
imagem_rgba = Image.fromarray(rgba_matrix, mode='RGBA')
imagem_rgba.save('/content/drive/My Drive/imagem_rgba.png')
imagem_rgba.show()
