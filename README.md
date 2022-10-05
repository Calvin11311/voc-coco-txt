# [How to create custom COCO data set for object detection](https://www.dlology.com/blog/how-to-create-custom-coco-data-set-for-object-detection/) | DLology blog

## Quick start

Then you can run the `voc2coco.py` script to generate a COCO data formatted JSON file for you.
```
python voc2coco.py ./data/VOC/Annotations ./data/coco/output.json
python voc2coco.py ./data/VOCgrey/Annotationstrain ./data/cocogrey/instances_train2017.json
python voc2coco.py ./data/VOCgrey/Annotationsval ./data/cocogrey/instances_val2017.json
python voc2coco.py ./data/VOCgrey/Annotationstest ./data/cocogrey/instances_test2017.json


python voc2coco.py ./data/VOCt/Annotationstrain ./data/cocot/instances_train2017.json
python voc2coco.py ./data/VOCt/Annotationsval ./data/cocot/instances_val2017.json
python voc2coco.py ./data/VOCt/Annotationstest ./data/cocot/instances_test2017.json
```


python txt2coco.py .\coco\labeltrain\ .\coco\outputs\test.json .\coco\pic\

Then you can run the following Jupyter notebook to visualize the coco annotations. `COCO_Image_Viewer.ipynb`


Further instruction on how to create your own datasets, read the [tutorial](https://www.dlology.com/blog/how-to-create-custom-coco-data-set-for-object-detection/).