import os
import cv2

folder = 'images'
os.mkdir(folder)

vidcap = cv2.VideoCapture('XXX.mp4')
count = 0
while True:
    success, image = vidcap.read()
    if not success:
        break
    cv2.imwrite(os.path.join(folder, "frame{:d}.jpg".format(count)), image)
    count += 10
print("{} images are extacted in {}.".format(count, folder))
