import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")
foto = Image.open("imagens/Foto Trabalho Final.jpeg")
imagem = np.array(foto)
largura_exibicao = 250

st.header("11. Espelhamento")
coluna_esquerda, coluna_direita = st.columns(2)
coluna_esquerda.image(
    cv2.flip(imagem, 1), caption="Espelhamento horizontal", width=largura_exibicao
)
coluna_direita.image(
    cv2.flip(imagem, 0), caption="Espelhamento vertical", width=largura_exibicao
)

st.header("12. Simetria")
altura, largura = imagem.shape[0], imagem.shape[1]
metade = largura // 2
metade_esquerda = imagem[:, :metade]
simetria = imagem.copy()
simetria[:, largura - metade:] = cv2.flip(metade_esquerda, 1)
st.image(simetria, width=largura_exibicao)

st.header("1. Saturação")
hsv = cv2.cvtColor(imagem, cv2.COLOR_RGB2HSV)
fator_saturacao = st.slider("Saturação", 0.0, 2.0, 1.0)
saturacao = hsv[:, :, 1].astype(float)
saturacao = saturacao * fator_saturacao
saturacao = np.clip(saturacao, 0, 255)
hsv_saturacao = hsv.copy()
hsv_saturacao[:, :, 1] = saturacao
st.image(cv2.cvtColor(hsv_saturacao, cv2.COLOR_HSV2RGB), width=largura_exibicao)

st.header("2. Brilho")
fator_brilho = st.slider("Brilho", 0.0, 2.0, 1.0)
brilho = hsv[:, :, 2].astype(float)
brilho = brilho * fator_brilho
brilho = np.clip(brilho, 0, 255)
hsv_brilho = hsv.copy()
hsv_brilho[:, :, 2] = brilho
st.image(cv2.cvtColor(hsv_brilho, cv2.COLOR_HSV2RGB), width=largura_exibicao)

st.header("19. Moldura")
espessura = st.slider("Espessura (pixels)", 1, 100, 20)
vermelho = st.slider("R (vermelho)", 0, 255, 255)
verde = st.slider("G (verde)", 0, 255, 255)
azul = st.slider("B (azul)", 0, 255, 255)
cor = (vermelho, verde, azul)
moldura = imagem.copy()
moldura[:espessura, :] = cor
moldura[altura - espessura:, :] = cor
moldura[:, :espessura] = cor
moldura[:, largura - espessura:] = cor
st.image(moldura, width=largura_exibicao)
