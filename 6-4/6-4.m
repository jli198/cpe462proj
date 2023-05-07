% Reads in .tif file and plots it
img = imread('Fig0631(a).tif');
figure;
subplot(2, 2, 1);
imshow(img);
title('Original Image');

% Converts image values to double precision
img1 = im2double(img);

% Takes the r, g, b values of each pixel
r = img1(:, :, 1);
g = img1(:, :, 2);
b = img1(:, :, 3);

% Plots r, g, b values of each pixel
subplot(2, 3, 4);
imshow(r);
title('Red Pixel Value');
subplot(2, 3, 5);
imshow(g);
title('Green Pixel Value');
subplot(2, 3, 6);
imshow(b);
title('Blue Pixel Value');

% Segment image
r1 = r(129:256, 86:170);

% Finds the mean of all the R values in image
r1Avg = mean(mean(r1(:)));

% Assigns M and N to be the width of the row and height of the column
[M, N] = size(r1);

% initialize variance
var = 0.0;

% For each pixel, add to running total variance: (Red value pixel - average Red value of each pixel)^2
for i = 1:M
    for j = 1:N
        var = var + (r1(i, j) - r1Avg) * (r1(i, j) - r1Avg);
    end
end

% standard deviation = sqrt(variance) = sqrt(total/(size of array))
stdDev = sqrt(var/(M*N));

% create array of zeros from length and width of image array
r2 = zeros(size(img, 1), size(img, 2));

% Find values of r where r is > or < 1.25 * stdDev; threshold so non-dark regions becomes black
index = find((r > r1Avg - 1.25 * stdDev) & (R < r1Avg + 1.25 * stdDev));

% Where index values exist in array r2, convert r2 zeros into ones (white pixels)
r2(index) = 1;

% Plot mask of image, mask of region should be light and everything else is dark
subplot(2, 2, 2);
imshow(r2);
title('Darkest Region Segmentation');