import cv2
import mediapipe as mp

# Carregar a imagem de referência para comparação
reference_image = cv2.imread('caminho/para/sua/imagem_de_referencia.jpg')

# Inicializar o módulo MediaPipe FaceMesh
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
face_detection = mp_face_detection.FaceDetection()

# Inicializar a captura de vídeo da webcam (0 representa a câmera padrão)
video_capture = cv2.VideoCapture(0)

while True:
    # Capturar frame a frame
    ret, frame = video_capture.read()

    # Detectar rostos na imagem atual
    result = face_detection.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if result.detections:
        for detection in result.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                         int(bboxC.width * iw), int(bboxC.height * ih)

            # Comparar com a imagem de referência (simplificado para detecção)
            reference_height, reference_width, _ = reference_image.shape
            if h == reference_height and w == reference_width:
                print("Rosto detectado. Esta pessoa está no banco de dados.")
            else:
                print("Rosto detectado. Esta pessoa não está no banco de dados.")

            # Desenhar o retângulo ao redor do rosto detectado
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Exibir o frame resultante
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar o vídeo e fechar as janelas
video_capture.release()
cv2.destroyAllWindows()
