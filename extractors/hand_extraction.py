from typing import NamedTuple
import imutils
import cv2
import os
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector
from mediapipe.python.solutions import hands

hands = hands.Hands(static_image_mode=True,
                    max_num_hands=2, min_detection_confidence=0.5)
dataset_path = './assets/cleaned_frames/consonants'


def listdir(path: str):
    return os.listdir(path)


def remove(path: str):
    if (os.path.exists(path)):
        os.remove(path)


remove('./logs/hand_extraction/multi_hand_landmarks.log')
remove('./logs/hand_extraction/imwrite.log')
remove('./logs/hand_extraction/shape.log')

# if result of multi hand landmark is null


def write_error_1(image_path):
    f = open("./logs/hand_extraction/multi_hand_landmarks.log", "a")
    f.write(image_path + "\n")
    f.close()

# imwrite exception


def write_error_2(image_path):
    f = open("./logs/hand_extraction/imwrite.log", "a")
    f.write(image_path + "\n")
    f.close()

# if frame is none


def write_error_3(image_path):
    f = open("./logs/hand_extraction/shape.log", "a")
    f.write(image_path + "\n")
    f.close()


# loop throgh folder
for consonant in listdir(dataset_path):
    parent_path = f'{dataset_path}/{consonant}'

    for filename in listdir(parent_path):
        image_path = f'{parent_path}/{filename}'
        frame = cv2.imread(image_path)

        if (frame is None):
            write_error_3(image_path)
            break

        frame = imutils.resize(frame, width=1306, height=1306)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results: NamedTuple = hands.process(frame)
        lmlist = []

        print('result:', results.multi_hand_landmarks)

        if (results.multi_hand_landmarks is None):
            write_error_1(image_path)
            break

        # if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                print(frame.shape)
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([cx, cy])

        # # prepare start point and end point for drawing rectangle
        x1 = lmlist[4][0]
        y1 = lmlist[8][1]
        x2 = lmlist[20][0]
        y2 = lmlist[0][1]

        # y of top middle finger
        topMid = lmlist[12][1]
        # top point is greater than bottom point, eg: cha
        # if (y1 > y2):
        # image = cv2.rectangle(frame, (x1 - 130, y1 - 130),
        #                       (x2 + 150, y2 + 130), (255, 0, 0), 2)
        # bottom point is greater than top point, eg: ka
        # else:
        # image = cv2.rectangle(frame, (x1 - 150, y1 - 100),
        #                       (x2 + 150, y2 + 130), (255, 0, 0), 2)

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # ba, cha, chha, chho, cho, da, ha, lo, mo, na, ngo, nho, pho, po, tha2, tho2,
        if (consonant in ['ba', 'cha', 'chha', 'chho', 'cho', 'da', 'ha', 'lo', 'mo', 'na', 'ngo', 'nho', 'pho', 'po', 'tha2', 'tho2']):
            crop_img = frame[topMid - 120:topMid+170, x1-170:x1+140]

        # do, kho, la, or, to,
        if (consonant in ['do', 'kho', 'la', 'or', 'to']):
            crop_img = frame[topMid - 45:topMid+200, x1-170:x1+140]

        # ka,
        if (consonant in ['ka']):
            crop_img = frame[topMid-120:topMid+100, x1-120:x1+170]

        # kha, ko, no, pha, ro, sa, ta,
        if (consonant in ['kha', 'ko', 'no', 'pha', 'ro', 'sa', 'ta']):
            crop_img = frame[topMid-120:topMid+170, x1-120:x1+70]

        # tha1, tho1, vo, yo
        if (consonant in ['tha1', 'tho1', 'vo', 'yo']):
            crop_img = frame[topMid-20:topMid+250, x1-170:x1+100]

        # save extracted hand images
        try:
            directory = f'./assets/cropped_hand_frames/consonants/{consonant}'
            if not os.path.exists(directory):
                os.makedirs(directory)
            cv2.imwrite(
                f'{directory}/{filename}', crop_img)
        except:
            print(f"INDEX: {filename}, CON: {consonant}")
            write_error_2(f'{directory}/{filename}')
