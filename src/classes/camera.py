import os
from PIL import Image

# Defina o diretório da pasta onde suas imagens estão localizadas
pasta_imagens = 'D:\Codigos\Alfred\src\classes\Pictures'

# Lista de arquivos na pasta
arquivos = os.listdir(pasta_imagens)

# Filtra os arquivos para pegar apenas os que têm extensão de imagem
imagens = [arquivo for arquivo in arquivos if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

# Carrega cada imagem e adiciona ao array
array_de_imagens = []
for imagem in imagens:
    caminho_completo = os.path.join(pasta_imagens, imagem)
    imagem_carregada = Image.open(caminho_completo)
    array_de_imagens.append(imagem_carregada)

# Agora você tem um array de imagens prontas para uso
