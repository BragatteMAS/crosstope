#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 12:34:35 2021
[REF](/playlist?list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG)actor by
@author: bragatte

Roberts
The idea behind the Roberts cross operator is to approximate the gradient of an
image through discrete differentiation which is achieved by computing the sum of the squares of the
differences between diagonally adjacent pixels. It highlights regions of high spatial gradient which often
correspond to edges.

Sobel:
Similar to Roberts - calculates gradient of the image. 
The operator uses two 3×3 kernels which are convolved with the original image to calculate
approximations of the derivatives – one for horizontal changes, and one for vertical.

Scharr:
Typically used to identify gradients along the x-axis (dx = 1, dy = 0) and y-axis (dx = 0,
dy = 1) independently. Performance is quite similar to Sobel filter.

Prewitt:
The Prewitt operator is based on convolving
the image with a small, separable, and integer valued filter in horizontal and vertical directions and is
therefore relatively inexpensive in terms of computations like Sobel operator.
Farid:
Farid and Simoncelli propose to use a pair of kernels, one for interpolation and another for
differentiation (csimilar to Sobel). These kernels, of fixed sizes 5 x 5 and 7 x 7, are optimized so
that the Fourier transform approximates their correct derivative relationship. 
                                         
"""

from skimage import io, filters, feature
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import cv2
import numpy as np

img = cv2.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/A0201_0001_V5.jpg', 0)

#Edge detection
from skimage.filters import roberts, sobel, scharr, prewitt, farid

roberts_img = roberts(img)
sobel_img = sobel(img)
scharr_img = scharr(img)
prewitt_img = prewitt(img)
farid_img = farid(img)

 