#!/bin/bash

IM_PATH="/home/hasan/Schreibtisch/projects/data/crack_detect_usm/good_sym"
#IM_PATH="/home/hasan/Schreibtisch/projects/data/crack_detect_usm/test_data_sig1"
BASE_PATH=$(basename "$IM_PATH")
SAVE_PATH=$(dirname $IM_PATH)/"${BASE_PATH}_cut_roi"
python cut_roi.py --im_path $IM_PATH --save_path $SAVE_PATH