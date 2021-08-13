import argparse

classes =[
"aeroplane_train.txt",
"bicycle_train.txt",
"bird_train.txt",
"boat_train.txt",
"bottle_train.txt",
"bus_train.txt",
"car_train.txt",
"cat_train.txt",
"chair_train.txt",
"cow_train.txt",
"diningtable_train.txt",
"dog_train.txt",
"horse_train.txt",
"motorbike_train.txt",
"person_train.txt",
"pottedplant_train.txt",
"sheep_train.txt",
"sofa_train.txt",
"train_train.txt",
"tvmonitor_train.txt",
]


import shutil
import os
from os import path


#args.txt_path  #
##
#args.target_path
#args.image_path #
def main(args: argparse.Namespace):
    path = args.txt_path  #"/home/batuhan/Desktop/datasets/VOCtrainval_11-May-2012/VOCdevkit/VOC2012/ImageSets/Main/"
    target = args.target_path #"/home/batuhan/Desktop/datasets/Changed"
    images = args.image_path #"/home/batuhan/Desktop/datasets/VOCtrainval_11-May-2012/VOCdevkit/VOC2012/JPEGImages"

    for i in classes:
        thisf = os.path.join(path,i)
        f = open(thisf,"r")
        for k in f.readlines():
            splited = k.split(" ")
            if splited[-1][0] == "1":
                tar = os.path.join(target, i[:-10])

                if not path.exists(tar):
                    os.makedirs(tar)
                tar = os.path.join(tar, splited[0])
                tar += ".jpg"
                fr = os.path.join(images,splited[0])
                fr += ".jpg"

                shutil.copy(fr, tar)

                print("image:",splited,"has copied")


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Visualize attention rollout from DINO")
    parser.add_argument(
        "-i", "--txt-path", dest="txt_path", type=str, help="Path to the txt file that contains image info"
    )
    parser.add_argument(
        "-l", "--image-path", dest="image_path", type=str, help="Path to the images in original location"
    )
    parser.add_argument(
        "-b", "--target-path", dest="target_path", type=str, help="Path to the target directory"
    )
    args = parser.parse_args()
    main(args)








