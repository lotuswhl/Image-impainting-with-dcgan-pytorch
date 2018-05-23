import os
import matplotlib.pyplot as plt
from scipy.misc import imresize
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--images_root", required=True, help="root directory of your images directory")
parser.add_argument("--images_subdir", required=True, help="your images dir name ,sub directory of images_root")
parser.add_argument("--resize_size", type=int, default=64, help="desired image resize size")
parser.add_argument("--saved_dir", default="", help="specify resized images save location")

args = parser.parse_args()

resize_size = int(args.resize_size)

if args.saved_dir != "":
    if not os.path.exists(args.saved_dir):
        os.makedirs(args.saved_dir)
    saved_dir = args.saved_dir
else:
    saved_dir = os.path.join(args.images_root,"resize_images")

source_dir = os.path.join(args.images_root,args.images_subdir)

image_list = os.listdir(source_dir)

for i in range(len(image_list)):
    image = plt.imread(os.path.join(source_dir,image_list[i]))
    image = imresize(image, (resize_size,resize_size))
    plt.imsave(fname=os.path.join(saved_dir,image_list[i]),arr=image)

    if i%1000==0:
        print("{:06} images complete.".format(i))
print("done")