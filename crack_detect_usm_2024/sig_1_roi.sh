#! /bin/bash

PATH="/home/hasan/Schreibtisch/projects/data/crack_detect_usm/good_sym_cut_roi"
FILTERS="blur sharpen"
BASE_PATH=$(basename "$PATH")
SAVE_PATH=$(dirname $IM_PATH)/"${BASE_PATH}_cut_roi_roi"
echo $SAVE_PATH

#python sig_1_roi.py \
    #--path $PATH\
    #--save_path $SAVE_PATH\
    #--filters $FILTERS