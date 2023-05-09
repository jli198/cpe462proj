% Read the input image
input_image = imread('cat.jpg');

% Convert the image to grayscale
gray_image = rgb2gray(input_image);

% Normalize the grayscale image to [0, 1] range
normalized_gray_image = double(gray_image) / 255;

% Define a custom colormap for pseudo-coloring
custom_colormap = [
    0, 0, 1;   % Blue
    0, 1, 0;   % Green
    1, 1, 0;   % Yellow
    1, 0, 0;   % Red
];

% Apply the colormap to the grayscale image
pseudo_color_image = ind2rgb(uint8(normalized_gray_image * (size(custom_colormap, 1) - 1)), custom_colormap);

% Display the original image and the pseudo-color image
figure;
subplot(1, 2, 1);
imshow(input_image);
title('Original Image');
subplot(1, 2, 2);
imshow(pseudo_color_image);
title('Pseudo-color Image');
