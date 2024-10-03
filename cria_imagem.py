from google.colab import drive
drive.mount('/content/drive')

from PIL import Image
import numpy as np

# Cria uma nova imagem de 100x100, modo 'RGB' e cor branca (255, 255, 255)
imagem_branca = Image.new('RGB', (100, 100), (255, 255, 255))

# Salva a imagem no disco
imagem_branca.save('/content/drive/My Drive/imagem_branca.png')

# Converte a imagem para um array NumPy
matriz_pixels = np.array(imagem_branca)

# Altera a coluna 50 (índice 49) para vermelho (RGB: 255, 0, 0)
matriz_pixels[:, 49] = [255, 0, 0]

# Converte de volta para imagem
imagem_modificada = Image.fromarray(matriz_pixels)

# Salva a imagem modificada
imagem_modificada.save('/content/drive/My Drive/imagem_modificada.png')

# Rotaciona a imagem em 30 graus
imagem_rotacionada = imagem_modificada.rotate(30, expand=True)

# Salva a imagem rotacionada
imagem_rotacionada.save('/content/drive/My Drive/imagem_rotacionada.png')

# Escalar a imagem em 0.5 (reduzir pela metade)
largura_original, altura_original = imagem_rotacionada.size
nova_largura = int(largura_original * 0.5)
nova_altura = int(altura_original * 0.5)
imagem_escalada = imagem_rotacionada.resize((nova_largura, nova_altura))

# Criar uma nova imagem maior para aplicar a translação
nova_imagem = Image.new('RGB', (largura_original + 20, altura_original + 40), (0, 0, 0))

# Transladar a imagem (colocar imagem escalada dentro da nova imagem com deslocamento)
nova_imagem.paste(imagem_escalada, (20, 40))  # Translada em x=+20, y=+40

# Salvar a imagem final
nova_imagem.save('/content/drive/My Drive/imagem_final.png')
