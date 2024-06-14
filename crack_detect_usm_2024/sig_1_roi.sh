#!/bin/bash

#IM_PATH="$HOME/Schreibtisch/projects/data/crack_detect_usm/random_good_cut_roi"
IM_PATH="$HOME/Schreibtisch/projects/data/crack_detect_usm/test_data_sig1_cut_roi"

FILTERS="blur sharpen"
BASE_PATH_B=$(basename "$IM_PATH")
SAVE_PATH=$(dirname $IM_PATH)/"${BASE_PATH_B}_cut_roi_roi"
echo $SAVE_PATH
python sig_1_roi.py \
    --path $IM_PATH\
    --save_path $SAVE_PATH\
    --filters $FILTERS