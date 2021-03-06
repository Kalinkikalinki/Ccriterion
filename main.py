# Приложение шутка
# активируется камера и при нажатии определенных клавиш включается режим, при котором
# когда к камере подходит лицо включается громкий неприятный звук
# для отключения человек должен показать определенный жест("Stop!")
import sys
if sys.platform == "win32" or sys.platform == "win64":
    from winsound import Beep
else:
    def Beep(hz,time):
        print("\a")
        print("\a")
        print("\a")
        print("\a")
        print("\a")
        print("\a")

from stop import stop
import cv2
import mediapipe as mp
import numpy as np


def Main():

    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_face_mesh = mp.solutions.face_mesh
    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
    cap = cv2.VideoCapture(0)

    with mp_face_mesh.FaceMesh(
            max_num_faces=100,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as face_mesh:

        while cap.isOpened():
            success, image = cap.read()

            if not success:
                print("Computer is safe")
                # If loading a video, use 'break' instead of 'continue'.
                continue

            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(image)

            # Draw the face mesh annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    if face_landmarks.landmark[2].z < 0 and face_landmarks.landmark[2].z > -0.2:
                        Beep(1000, 5000)
                    elif face_landmarks.landmark[2].z <= -0.2:
                        Beep(1250, 5000)
                    mp_drawing.draw_landmarks(
                        image=image,
                        landmark_list=face_landmarks,
                        connections=mp_face_mesh.FACEMESH_TESSELATION,
                        landmark_drawing_spec=None,
                        connection_drawing_spec=mp_drawing_styles
                            .get_default_face_mesh_tesselation_style())
                    mp_drawing.draw_landmarks(
                        image=image,
                        landmark_list=face_landmarks,
                        connections=mp_face_mesh.FACEMESH_CONTOURS,
                        landmark_drawing_spec=None,
                        connection_drawing_spec=mp_drawing_styles
                            .get_default_face_mesh_contours_style())
                    mp_drawing.draw_landmarks(
                        image=image,
                        landmark_list=face_landmarks,
                        connections=mp_face_mesh.FACEMESH_IRISES,
                        landmark_drawing_spec=None,
                        connection_drawing_spec=mp_drawing_styles
                            .get_default_face_mesh_iris_connections_style())
            # Flip the image horizontally for a selfie-view display.

            cv2.imshow('GO AWAY', cv2.flip(image, 1))
            if cv2.waitKey(5) & 0xFF == 27 or stop():
                break

    cap.release()
