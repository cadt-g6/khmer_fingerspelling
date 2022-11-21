import math
import pandas as pd
import os

from moviepy.editor import *
from extractor_util import *

# variables
# shrinked_parent_path = './././assets/shrinked'
# source_video_path = './././assets/video'
# data_path = './././datasets/csv'
# data_file = '/testing_file.csv'

shrinked_parent_path = '../assets/shrinked'
source_video_path = '../assets/video'
data_path = '../datasets/csv'
data_file = '/sub_vowel.csv'
video_extension = '.mp4'

# load the data
df = pd.read_csv(data_path + data_file)
df.drop(
    columns=['start_at', 'end_at', 'char'],
    inplace=True
)

# trimming the video
def trim_video(videoname, start, stop, target_name, path, frame=30):
    print("Video subcliping information: ",videoname,start,stop,target_name,path)
    video = VideoFileClip(videoname).subclip(start, stop)
    video.write_videofile(os.path.join(path, target_name), fps=frame)


# extract the video
col = df.columns
for index in range(0, len(df)):
    start = df[col[0]][index]
    stop = df[col[1]][index]
    character = df[col[2]][index]
    type = df[col[3]][index]
    video_name = df[col[4]][index]

    if math.isnan(start) or math.isnan(stop):
        continue
    
    print("-------", character, '--------')

    target_path = shrinked_parent_path + '/' + type + '/' + str(character).strip()

    #ensure_dir_exist(target_path)
    #add_readme(target_path, character, index)

    target_name = str(count_file_in_dir(target_path)) + video_extension
    video_name = source_video_path + '/' + video_name
    print(video_name,start, stop,target_name,target_path)
    trim_video(video_name, start, stop, target_name, target_path)

    print('----------------------------')
