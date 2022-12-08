import cv2
import imutils
import os

def save_file(name,image,char,path):
    cv2.imwrite(os.path.join(path, char, name),image)
    cv2.destroyAllWindows()

def read_folder(path):
    return os.listdir(path)

def read_filename(path,folder_name):
    return os.listdir(path+'/'+folder_name)

def rotation(img,rotate_ang,char,write_path,read_path):
    # print('images',images)
    for ang in rotate_ang:
        print("image",img)
        image = cv2.imread(read_path+'/'+char+'/'+img)
        image = cv2.resize(image,(800,800))
        image = image.reshape(800,800,3)
        filename = img.split('.')[0]+'_'+str(ang)+'.jpg'
        save_file(filename,imutils.rotate(image,angle=ang),char,write_path)    

#Hyperparameter
read_path = r"../../../datasets/croped"
write_path = r"../../../datasets/rotated"
folder = read_folder(read_path)
filename = {}
for foldername in folder:
    filename[foldername] = read_filename(read_path,foldername)
character = [
    #*filename.keys() ##All character
    'tho2',
    'to',
    'yo',
    'vo',
    'pho'
]
# print(character)
right_rotate = [-5,-10,-15,-20,-25]
left_rotate = [5,10,15,20,25]

for char in character:
    for name in filename[char]:
        rotation(name,right_rotate,char,write_path,read_path)
        rotation(name,left_rotate,char,write_path,read_path)