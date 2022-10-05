#!/usr/bin/python

# pip install lxml

import sys
import os
import json
import xml.etree.ElementTree as ET
import glob
import os.path

from PIL import Image

START_BOUNDING_BOX_ID = 1
PRE_DEFINE_CATEGORIES = None


# If necessary, pre-define category and its id
#  PRE_DEFINE_CATEGORIES = {"aeroplane": 1, "bicycle": 2, "bird": 3, "boat": 4,
#  "bottle":5, "bus": 6, "car": 7, "cat": 8, "chair": 9,
#  "cow": 10, "diningtable": 11, "dog": 12, "horse": 13,
#  "motorbike": 14, "person": 15, "pottedplant": 16,
#  "sheep": 17, "sofa": 18, "train": 19, "tvmonitor": 20}


# def get(root, name):
#     vars = root.findall(name)
#     return vars
#
#
# def get_and_check(root, name, length):
#     vars = root.findall(name)
#     if len(vars) == 0:
#         raise ValueError("Can not find %s in %s." % (name, root.tag))
#     if length > 0 and len(vars) != length:
#         raise ValueError(
#             "The size of %s is supposed to be %d, but is %d."
#             % (name, length, len(vars))
#         )
#     if length == 1:
#         vars = vars[0]
#     return vars
#
#
# def get_filename_as_int(filename):
#     try:
#         filename = filename.replace("\\", "/")
#         filename = os.path.splitext(os.path.basename(filename))[0]
#         return int(filename)
#     except:
#         raise ValueError("Filename %s is supposed to be an integer." % (filename))
#
#
# def get_categories(xml_files):
#     """Generate category name to id mapping from a list of xml files.
#
#     Arguments:
#         xml_files {list} -- A list of xml file paths.
#
#     Returns:
#         dict -- category name to id mapping.
#     """
#     classes_names = []
#     for xml_file in xml_files:
#         tree = ET.parse(xml_file)
#         root = tree.getroot()
#         for member in root.findall("object"):
#             classes_names.append(member[0].text)
#     classes_names = list(set(classes_names))
#     classes_names.sort()
#     return {name: i for i, name in enumerate(classes_names)}


def convert(txt_lines, json_file,picdir):
    json_dict = {"images": [], "type": "instances", "annotations": [], "categories": []}
    print(txt_lines)
    print(json_file)
    print(picdir)
    picdir = picdir.replace("\\", "/")
    for lines in txt_lines:
        lines=lines.split('\n')[0]
        lines=lines.split(',')
        print(lines)
        filename=lines[0]
        picpp=picdir+filename
        print(picpp)
        print(os.path.exists(picpp))
        if not os.path.exists(picpp):
            continue
        image_id=int(filename.split('.')[0])
        pic_path = picdir+filename
        img = Image.open(pic_path)
        size = img.size  # 大小/尺寸
        width = img.width  # 图片的宽
        height = img.height  # 图片的高
        image = {
            "file_name": filename,
            "height": height,
            "width": width,
            "id": image_id,
        }
        json_dict["images"].append(image)
        bnd_id = START_BOUNDING_BOX_ID


        category_id = lines[2]
        xmin = int(lines[4])
        ymin = int(lines[5])
        width = int(lines[6])
        height = int(lines[7])
        ann = {
            "area": width * height,
            "iscrowd": 0,
            "image_id": image_id,
            "bbox": [xmin, ymin, width, height],
            "category_id": category_id,
            "id": bnd_id,
            "ignore": 0,
            "segmentation": [],
        }
        json_dict["annotations"].append(ann)
        bnd_id = bnd_id + 1

    # for cate, cid in categories.items():
        cid=lines[2]
        cate=lines[1]
        if PRE_DEFINE_CATEGORIES is not None:
            categories = PRE_DEFINE_CATEGORIES
        else:
            categories = {
                             "supercategory": "none",
                             "id":cid,
                         "name":cate}

        json_dict["categories"].append(categories)

    os.makedirs(os.path.dirname(json_file), exist_ok=True)
    json_fp = open(json_file, "w")
    json_str = json.dumps(json_dict)
    json_fp.write(json_str)
    json_fp.close()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert Pascal txt annotation to COCO format."
    )
    parser.add_argument("txt_dir", help="Directory path to txt files.", type=str)
    parser.add_argument("json_file", help="Output COCO format json file.", type=str)
    parser.add_argument("pic_path",help="picture path")
    args = parser.parse_args()
    tpath=os.listdir(args.txt_dir)
    txt_lines=[]
    for t in tpath:
        txtdir=args.txt_dir+t
        with open(txtdir,'r') as f:
            tlines=f.readlines()
        for i in tlines:
            txt_lines.append(i)
    # print(txt_lines)
    # If you want to do train/test split, you can pass a subset of xml files to convert function.

    convert(txt_lines, args.json_file,args.pic_path)
    print("Success: {}".format(args.json_file))
