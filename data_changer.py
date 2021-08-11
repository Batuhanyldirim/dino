import argparse

classes =[
"aeroplane_trainval.txt",
"bicycle_trainval.txt",
"bird_trainval.txt",
"boat_trainval.txt",
"bottle_trainval.txt",
"bus_trainval.txt",
"car_trainval.txt",
"cat_trainval.txt",
"chair_trainval.txt",
"cow_trainval.txt",
"diningtable_trainval.txt",
"dog_trainval.txt",
"horse_trainval.txt",
"motorbike_trainval.txt",
"person_trainval.txt",
"pottedplant_trainval.txt",
"sheep_trainval.txt",
"sofa_trainval.txt",
"train_trainval.txt",
"tvmonitor_trainval.txt",
]


import shutil
import os




def main(args: argparse.Namespace):
    path = args.txt_path  # "/home/batuhan/Desktop/datasets/VOCtrainval_11-May-2012/VOCdevkit/VOC2012/ImageSets/Main/"
    target = args.target_path #"/home/batuhan/Desktop/datasets/Changed"
    images = args.image_path #"/home/batuhan/Desktop/datasets/VOCtrainval_11-May-2012/VOCdevkit/VOC2012/JPEGImages"

    for i in classes:
        thisf = os.path.join(path,i)
        f = open(thisf,"r")
        for k in f.readlines():
            splited = k.split(" ")
            if splited[-1][0] == "1":
                tar = os.path.join(target, i[:-13])
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








