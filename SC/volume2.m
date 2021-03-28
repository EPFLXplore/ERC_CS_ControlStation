pkg load image
I = imread('picture_1.png'); %read image

I = rgb2gray(I) > 120; % Converts image to greyscale by analizing luminance. Try different values for saturation calibration
I = imfill(I, 'holes'); % fills holes in the input binary image BW. In this syntax, a hole is a set of background pixels that cannot be reached by filling in the background from the edge of the image.
#imshow(I) % show greyscale image

BW = edge(I*1.0,'canny'); %detects edges in image I using the edge-detection algorithm "canny". The Canny method finds edges by looking for the local maxima of the gradient of the input image.
imshow(BW)
[H,theta,rho] = hough(BW); %Hough transform: matrix of line parameters. A line is represented by rho= x*cos(theta) + y*sin(theta). 
%The function returns rho, the distance from the origin to the line along a vector perpendicular to the line, 
%and theta, the angle in degrees between the x-axis and this vector. The function also returns the Standard Hough Transform, H, 
%which is a parameter space matrix whose rows and columns correspond to rho and theta values respectively.

P = houghpeaks(H,6,'threshold',ceil(0.5*max(H(:)))); %identify maximum 5 peaks in Hough transform matrix H. 
%The function returns peaks a matrix that holds the row and column coordinates of the peaks.
%'threshold' is the name assigned to the minimum value (0.3*maximum value of H) to be considered a peak 

lines = houghlines(BW,theta,rho,P,'FillGap',5,'MinLength',7); %extracts line segments in the image BW. theta and rho are vectors returned by hough peaks.
%Distance between two line segments associated with the same Hough transform bin, specified as a positive number. 
%FillGap: When the distance between the line segments is less than the value specified (5), the houghlines function merges the line segments into a single line segment.
%MinLength: Minimum line length, specified as a positive number. houghlines discards lines that are shorter than the value specified (7).
%lines is a vector
%disp(lines)

average=0;
for k = 1:length(lines)
  xy = [lines(k).point1; lines(k).point2];
  average=average + (xy(1,2)+xy(2,2))/2;
end

disp(average/length(lines));
