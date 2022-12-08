import cv2
import imutils
import os

def save_file(name,image,path):
    cv2.imwrite(os.path.join(path, name),image)
    cv2.destroyAllWindows()

def read_folder(path):
    return os.listdir(path)

def read_filename(path,folder_name):
    return os.listdir(path+'/'+folder_name)
 

#Hyperparameter
read_path = r"../datasets/rotated"
write_path = r"../datasets/rotatedwhole"
folder = read_folder(read_path)
filename = {}
for foldername in folder:
    filename[foldername] = read_filename(read_path,foldername)
character = [
    *filename.keys() ##All character
    #'cha'
    # 'chha',
    # 'chho',
]


for char in character:
    for name in filename[char]:
        image = cv2.imread(os.path.join(read_path,char,name))
        save_file(name,image,write_path)