import pandas as pd
import os
import fnmatch
from moviepy.editor import *

# variable
shrinked_parent_path = r'.\.\.\asset\shrinked'
source_video_path = r'.\.\.\asset\video'
video_extension = '.mp4'
data_path = r'.\.\.\datasets\csv'
data_file = r'\testing_file.csv'


# load the data
df = pd.read_csv(data_path + data_file)
df.drop(
    columns=['start_at', 'end_at', 'char'],
    inplace=True
)

# count file in directory
def count_file_dir(path):
    count = len(fnmatch.filter(os.listdir(path), '*.*'))
    # print("count=",count)
    return count

# clip the video
def video_sub_clip(videoname, start, stop, target_name, path, frame=30):
    # print("Video subcliping information: ",name,start,stop,target_name)
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

    print("-------", character, '--------')

    target_path = shrinked_parent_path + '\\' + type + '\\' + character
    target_name = str(count_file_dir(target_path)) + video_extension
    video_name = source_video_path + '\\' + video_name
    video_sub_clip(video_name, start, stop, target_name, target_path)

    print('----------------------------')
