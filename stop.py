import cv2
import mediapipe as mp
import numpy as np
import math
eps = 10 ** -10
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = math.hypot(self.x, self.y)
        if abs(self.r) != 0:
            self.angle = (math.acos(self.x / self.r))
        else:
            self.angle = 0

    def __abs__(self):
        return  self.r

    def dist(self,x = None, y = None):
        if x == None:
            return self.r
        elif x != None and y == None:
            return math.hypot(abs(x.x - self.x),abs(x.y - self.y))
        return math.hypot(abs(self.x - x), abs(self.y - y))

    def __str__(self):
        return f'{self.x} {self.y}'

class Vector(Point):

    def __init__(self, x1, y1 = None, x2 = None, y2 = None):
        if isinstance(y2, float):
            super().__init__(x2 - x1, y2 - y1)
        elif isinstance(y1, float):
            super().__init__(x1, y1)

    def dot_product(self, vector):
        return self.x * vector.x + self.y * vector.y

    def cross_product(self, vector):
        return self.x * vector.y - self.y * vector.x

    def __mul__(self, vector):
        return self.x * vector.x + self.y * vector.y

    def __xor__(self, other):
        return self.x * other.y - self.y * other.x

    def mul(self, other):
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other)
def angle(vector1, vector2):
    inner_product = vector1 * vector2
    len1 = math.hypot(vector1.x, vector1.y)
    len2 = math.hypot(vector2.x, vector2.y)
    ang = math.degrees(math.acos(inner_product/(len1*len2)))
    return ang
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
handsDetector = mp.solutions.hands.Hands()
cap = cv2.VideoCapture(0)
def stop():
    ret, frame = cap.read()
    flipped = np.fliplr(frame)
    # переводим его в формат RGB для распознавания
    flippedRGB = cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB)
    # Распознаем
    results = handsDetector.process(flippedRGB)
    if results.multi_hand_landmarks is not None:
        for hand_landmarks in results.multi_hand_landmarks:
            a = Vector(hand_landmarks.landmark[0].x, hand_landmarks.landmark[0].y,hand_landmarks.landmark[8].x,hand_landmarks.landmark[8].y)
            b = Vector(hand_landmarks.landmark[0].x, hand_landmarks.landmark[0].y,hand_landmarks.landmark[20].x,hand_landmarks.landmark[20].y)
            angl = angle(a,b)
            if angl < 20:
                return True
    return False
