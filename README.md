# CPE 462 Image Processing Project

## PROJECT 06-01

### Web-Safe Colors

In order to complete this project, it is necessary that you find a program capable of generating the RGB component images for a given tif color image.  For example, MATLAB's Image Processing Toolbox can do this, but you can also do it with image editing programs like Adobe's Photo-Shop or Corel's PhotoPaint.  It is acceptable for the purposes of this project to convert an image to RGB (and back) manually.

1. Write a computer program that converts an arbitrary RGB color image to a web-safe RGB image (see Fig. 6.10 for a definition of web-safe colors).
2. Download the image in Fig. 6.8 from the book web site and convert it to a web-safe RGB color image.  Figure 6.8 is given in tif format, so convert your result back to tif (see comments at the beginning of this project).  Explain the differences between your result and Fig. 6.8.

## PROJECT 06-02

### Psuedo-Color Image Processing

1. Implement Fig. 6.23, with the characteristic that you can specify two ranges of gray-level values for the input image and your program will output an RGB image whose pixels have a specified color corresponding to one range of gray levels in the input image, and the remaining pixels in the RGB image have the same shade of gray as they had in the input image.  You can limit the input colors to all the colors in Fig. 6.4(a).
2. Download the image in Fig. 1.10(4) from the book web site and process it with your program so that the river appears yellow and the rest of the pixels are the same shades of gray as in the input image.  It is acceptable to have isolated specs in the image that also appear yellow, but these should be kept as few as possible by proper choice of the two gray-level bands that you input into your program.

## PROJECT 06-03

### Color Image Enhancement by Histogram Processing

1. Download the dark-stream color picture in Fig. 6.35 from the book web site.  Convert the image to RGB (see comments at the beginning of Project 06-01).  Histogram-equalize the R, G, and B images separately using the histogram-equalization program from Project 03-02 and convert the image back to tif format.
2. Form an average histogram from the three histograms in (a) and use it as the basis to obtain a single histogram equalization intensity transformation function.  Apply this function to the R, G, and B components individually, and convert the results to jpg.  Compare and explain the differences in the tif images in (a) and (b).

## PROJECT 06-04

### Color Image Segmentation

Download Fig. 6.28(b) from the book web site and duplicate Example 6.15, but segment instead the darkest regions in the image.