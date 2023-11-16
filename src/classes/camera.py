import cv2
import mediapipe as mp
from deepface import DeepFace

class Camera:
    
    def recognize_face(result_callback):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        reconhecimento_rosto = mp.solutions.face_detection
        desenho = mp.solutions.drawing_utils
        reconhecedor_rosto = reconhecimento_rosto.FaceDetection()

        counter = 0

        face_match = False

        reference_img = cv2.imread('C:\\Users\\HP\\Downloads\\cam.jpg')

        def check_face(frame):
            nonlocal face_match
            try:
                if DeepFace.verify(frame, reference_img.copy())['verified']:
                    face_match = True
                else:
                    face_match = False
            except ValueError:
                face_match = False

        while True:
            ret, frame = cap.read()

            lista_rostos = reconhecedor_rosto.process(frame)
            if lista_rostos.detections:
                for rosto in lista_rostos.detections:
                    desenho.draw_detection(frame, rosto)

            if ret:
                if counter % 120 == 0:
                    try:
                        check_face(frame.copy())
                        result_callback(face_match)  # Chama a função de callback com o resultado
                    except ValueError:
                        pass
                counter += 1

                if face_match:
                    cv2.putText(frame, 'Match!', (20, 450), cv2.CAP_PROP_FRAME_WIDTH, 1, (0, 255, 0), 3)
                else:
                    cv2.putText(frame, 'No Match!', (20, 450), cv2.CAP_PROP_FRAME_WIDTH, 1, (0, 0, 255), 3)

                cv2.imshow('Video', frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

