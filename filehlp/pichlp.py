"""
    Picture Helper

    This header is to analyze picture.

    Author:   NTLPY
    Creation: 0x01d645ea4bd4f640 (UTC)

"""

# import modules
import cv2 as _cv2;
import numpy as _np;
from settings import sets as _sets;

# initialization
_analyzer = _cv2.dnn.readNetFromCaffe(_sets["caffe"]["prototxt"], _sets["caffe"]["caffeModel"]);
object_name = [r[r.find(" ") + 1:-1] for r in open(_sets["caffe"]["synset_word"])]

# count all objects that can be recognize
def total() -> int:
    return _sets["caffe"]["total"];

# analyze
#   return: int object id
def analyze_pic(filename : str) -> int:
    # load image from file
    img = _cv2.imdecode(_np.fromfile(filename, dtype = _np.uint8), -1);

    # initialize image
    blob = _cv2.dnn.blobFromImage(img, 1, (224, 224), (104, 117, 123));

    # if image has 4 channels tranform it to 3 channels
    if (blob.shape[1] == 4):
        blob = blob[0:1, 0:3, 0:224, 0:224];
    elif (blob.shape[1] != 3):
        return None;

    #input
    _analyzer.setInput(blob);

    preds = _analyzer.forward();

    #calc the max
    i_max = -1; v_max = 0;
    for i in range(0, _sets["caffe"]["total"]):
        if (preds[0][i] > v_max):
            v_max = preds[0][i];
            i_max = i;
        pass;
    
    return i_max if (v_max > _sets["caffe"]["confidence"]) else None;