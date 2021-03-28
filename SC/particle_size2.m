pkg load image
I = imread('picture_1.png'); %read image
Ibinary = rgb2gray(I) > 150; % greyscale conversion, definition of saturation
Ibinary = imfill(Ibinary, 'holes'); %fills holes in the input binary image I. 
%A hole is a set of background pixels that cannot be reached by filling in the background from the edge of the image.
imshow(Ibinary)
C = 0.008; % Conversion factor m/pixel. 

[labeledImage, numberOfBlobs] = bwlabel(Ibinary); 
% labeledImage: Label matrix of contiguous regions, returned as matrix of nonnegative integers with the same size as Ibinary. 
    %The pixels labeled 0 are the background (black). The pixels labeled 1 make up one object (white blob); the pixels labeled 2 make up a second object; and so on.
%returns the label matrix labeledImage that contains labels for the 8-connected objects found in BW.
    %8-connected: Pixels are connected if their edges or corners touch. Two adjoining pixels are part of the same object if they are both on and are connected along the horizontal, vertical, or diagonal direction.
%returns numberOfBlobs, the number of connected objects in the image

blobMeasurements = regionprops(labeledImage, 'Centroid','EquivDiameter');
%returns measurements of the centroid and the equivalent diameter of each blob. 

% Gives equivalent diameter
EquivDiameter = [blobMeasurements.EquivDiameter]; 
ValidDia = find(EquivDiameter>10); %make a vector of diameters bigger than 10
blobMeasurements = blobMeasurements(ValidDia);
EquivDiameter = EquivDiameter(ValidDia); %only retain particles with valid diameter

% constructs and displays a histogram applying relative probability (the sum of the bar heights is less than or equal to 1), and displays x and y labels
% figure,histogram(EquivDiameter*C,'Normalization','probability'),xlabel('Size[m - uncalibrated]'),ylabel('Probability')
figure
hist(EquivDiameter*C)
xlabel('Size[m - uncalibrated]')
ylabel('Probability')