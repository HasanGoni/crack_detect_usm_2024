from pathlib import Path
import numpy as np
from fastcore.all import *
from fastcore.basics import *
from typing import List
import cv2





def blur_img_(
        img:np.ndarray,  #image
        ks:int, # kernel size
        ) -> np.ndarray:
    'Blur image'
    return cv2.GaussianBlur(img, (ks, ks), 0)

def med_img_(
        img:np.ndarray,  #image
        ks:int, # kernel size
        ) -> np.ndarray:
    'Median image'
    return cv2.medianBlur(img, ks)


def canny_img_(
        img:np.ndarray,  #image
        th1:int, #threshold1
        th2:int, #threshold2
        ) -> np.ndarray:
    'Canny image'
    return cv2.Canny(img, th1, th2)

def sharpen_img_(
        img:np.ndarray,  #image
        ) -> np.ndarray:
    'Sharpen image'
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    return cv2.filter2D(img, -1, kernel)



def filter_img_(
        img:np.ndarray,  #image
        filters_:List[str] # opencv filters
        ) -> np.ndarray:

    'Apply filter on image'

    ops = {
        'blur': blur_img_,
        'med': med_img_,
        'canny': canny_img_,
        'sharpen': sharpen_img_
    }
    for fl in filters_:
        if fl in ops:
            img = ops[fl](img)
        else:
            print(f'Filter {fl} not found')

    



def sig_1_roi(
        img: np.ndarray,
          h_idx0: int,
          h_idx1: int,
          w_idx0: int,
          w_idx1: int,
          filters_:List[str], #based on this list some filter will be applied on roi image
          ) -> np.ndarray:
    'Signature 1 is cut based on template and then again cut based on indx'
    img = filter_img_(
        img, 
        filters_=filters_)
    roi_img =  img[h_idx0:h_idx1, w_idx0:w_idx1]
    return roi_img

def read_and_save_img_(
        fn:str,
        filters_:List[str],
        h_idx0:int,
        h_idx1:int,
        w_idx0:int,
        w_idx1:int,
        save_path:str,
        ) -> None:

    img = read_img(fn)
    img = sig_1_roi(
                    img=img,
                    filters_=filters_,
                    h_idx0=h_idx0,
                    h_idx1=h_idx1,
                    w_idx0=w_idx0,  
                    w_idx1=w_idx1,
                    )
    if save_path:
        cv2.imwrite(img, f'{save_path}/{Path(fn).stem}.png')    

def read_and_save_img_path_(
        path:Union[str, Path], # path of images
        filters_:List[str],
        h_idx0:int,
        h_idx1:int,
        w_idx0:int,
        w_idx1:int,
        save_path:str,
        ) -> None:

    sv_ = partial(
        read_and_save_img_,
        filters_=filters_,
        h_idx0=h_idx0,
        h_idx1=h_idx1,
        w_idx0=w_idx0,
        w_idx1=w_idx1,
        save_path=save_path,
    )
    fns = Path(path).ls()
    
    parallel(sv_, fns, n_workers=8, progress=True)

def parse_args_():
    'Parse command line arguments'
    import argparse
    parser = argparse.ArgumentParser(description='Signature 1 ROI')
    parser.add_argument(
        '--path', type=str, nargs='+', help='Image file names')
    parser.add_argument(
        '--filters', type=str, nargs='+', help='Filters to be applied on image')
    parser.add_argument(
        '--h_idx0',default=0, type=int, help='Height index 0')
    parser.add_argument(
        '--h_idx1', default=350,type=int, help='Height index 1')
    parser.add_argument(
        '--w_idx0',default=190, type=int, help='Width index 0')
    parser.add_argument(
        '--w_idx1',default=-20, type=int, help='Width index 1')
    parser.add_argument(
        '--save_path', type=str, help='Save path')
    args = parser.parse_args()
    return args

def main():
    args = parse_args_()
    read_and_save_img_path_(
        path=args.path,
        filters_=args.filters,
        h_idx0=args.h_idx0,
        h_idx1=args.h_idx1,
        w_idx0=args.w_idx0,
        w_idx1=args.w_idx1,
        save_path=args.save_path,
    )

if __name__ == '__main__':
    main()