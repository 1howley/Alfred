import cv2
import mediapipe as mp
import numpy as np

# Carregar a imagem de referência para comparação
reference_image = cv2.imread(r"C:\Users\HP\Downloads\test.jpeg")

# Inicializar o módulo MediaPipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Inicializar o modelo FaceMesh
face_mesh = mp_face_mesh.FaceMesh()

# Inicializar a captura de vídeo da webcam (0 representa a câmera padrão)
video_capture = cv2.VideoCapture(0)

# Função para calcular a distância Euclidiana entre dois pontos
def euclidean_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

# Definir um limite para considerar uma correspondência
threshold = 50  # Ajuste o valor conforme necessário

while True:
    # Capturar frame a frame
    ret, frame = video_capture.read()

    # Converter o frame para RGB para o MediaPipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detectar pontos-chave faciais na imagem atual
    result = face_mesh.process(frame_rgb)

    if result.multi_face_landmarks:
        # Extrair os pontos-chave faciais do primeiro rosto detectado
        landmarks = result.multi_face_landmarks[0]

        # Calcular a distância Euclidiana entre os pontos-chave faciais da imagem atual e da imagem de referência
        distance = euclidean_distance((landmarks[0].landmark[0].x, landmarks[0].landmark[0].y), (reference_image[0].landmark[0].x, reference_image[0].landmark[0].y))

        # Verificar se a distância está abaixo do limite
        if distance < threshold:
            # A imagem atual corresponde à imagem de referência
            # Implemente a lógica aqui para tratar a correspondência

            # Desenhar os pontos-chave faciais no frame
            mp_drawing.draw_landmarks(frame, landmarks)

    # Exibir o frame resultante
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar o vídeo e fechar as janelas
video_capture.release()
cv2.destroyAllWindows()
