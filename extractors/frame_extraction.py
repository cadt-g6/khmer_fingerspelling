import cv2
import os

from numpy import character

from extractor_util import *

# variables
source_video = '../assets/shrinked'
char_type = '/sub_vowel'
framed_path = '../assets/framed'

# read character folder data
folder_char = []
with os.scandir(source_video + char_type + '/') as entries:
    for entry in entries:
        folder_char.append(entry.name)


def extract_frame_from_video(video_name, target_path, fps=30):
    cap = cv2.VideoCapture(video_name)
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('frame', frame)
            if cv2.waitKey(fps):
                target_name = str(count_file_in_dir(target_path)) + '.jpg'
                cv2.imwrite(os.path.join(target_path, target_name), frame)
                print('---', target_name, '--- Done')
        else:
            break

    cv2.destroyAllWindows()
    cap.release()


# read video names
video_names = {}
for character_folder in folder_char:
    print("--------", character_folder, '--------')
    if character_folder == 'script.sh':
        print("Pass the file.....")
        continue
    # if character_folder not in ["ta","tha1","tha2","tho1","tho2","to","vo","yo"]:
    #     print("Pass the file.....")
    #     continue
    video = []
    with os.scandir(source_video + char_type + '/' + character_folder + '/') as names:
        for name in names:
            video.append(name.name)
    if len(video) > 0:
        print("video: ", end='')
        for name in video:
            print(name)
            target_path = framed_path + char_type + '/' + character_folder
            video_name = source_video + char_type + '/' + character_folder + '/' + name
            extract_frame_from_video(video_name, target_path)
    else:
        print("No video data.")

    print("----------------------")
