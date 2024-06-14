# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/04_preprocessing.preprocess_image.ipynb.

# %% auto 0
__all__ = ['tmp_part', 'get_roi_frm_tmp', 'apply_filter_', 'frm_img_to_roi']

# %% ../../nbs/04_preprocessing.preprocess_image.ipynb 4
import cv2
import numpy as np
import matplotlib.pyplot as plt
from fastcore.all import *
import os
from tqdm.auto import tqdm
from typing import List, Tuple
from pathlib import Path

# %% ../../nbs/04_preprocessing.preprocess_image.ipynb 5
import matplotlib as mpl

# %% ../../nbs/04_preprocessing.preprocess_image.ipynb 6
from cv_tools.core import *

# %% ../../nbs/04_preprocessing.preprocess_image.ipynb 17
def tmp_part(
    img: np.ndarray,
    tmp_img: np.ndarray,
   ):
   x, y, w, h = get_template_part(img, tmp_img)
   return img[y:y+h, x:x+w]

# %% ../../nbs/04_preprocessing.preprocess_image.ipynb 18
def get_roi_frm_tmp(
    tmp_part_img:np.ndarray,
    h_idx0:int=0,
    h_idx1:int=350,
    w_idx0:int=190,
    w_idx1:int=-20,
    ):
    return tmp_part_img[h_idx0:h_idx1, w_idx0:w_idx1]

# %% ../../nbs/04_preprocessing.preprocess_image.ipynb 19
def apply_filter_(
    img:np.ndarray,
    filters_:List[str],
    ):
    return filter_img_(img, filters_)

# %% ../../nbs/04_preprocessing.preprocess_image.ipynb 20
def frm_img_to_roi(
    img:np.ndarray,
    tmp_img:np.ndarray,
    filters_:List[str]=["blur", "sharpen"],
    h_idx0:int=0,
    h_idx1:int=350,
    w_idx0:int=190,
    w_idx1:int=-20,
    ):
    """
    from image template part will be extracted and then apply
    the filters and then roi
    
    """
    tmp_part_img = tmp_part(img, tmp_img)
    roi = get_roi_frm_tmp(
        tmp_part_img, 
        h_idx0, 
        h_idx1, 
        w_idx0, 
        w_idx1)
    roi = apply_filter_(roi, filters_)
    return roi