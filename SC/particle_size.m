pkg load image
I = imread('picture_1.png');
Ibinary = rgb2gray(I) > 150; % Try different values for your problem

Ibinary = imfill(Ibinary, 'holes');
C = 0.008; % Conversion factor m/pixel. This was a guess, you should be able to find the real one

[labeledImage, numberOfBlobs] = bwlabel(Ibinary);
blobMeasurements = regionprops(labeledImage, 'Centroid','EquivDiameter'); % I believe equivalent diameter is a good way to measure size,
                                                                          % you can also check different metrics
% Get equivalent diameter
EquivDiameter = [blobMeasurements.EquivDiameter]; 
ValidDia = find(EquivDiameter>10); % Some empiric threshold
blobMeasuremen4ts = blobMeasurements(ValidDia);
EquivDiameter         = EquivDiameter(ValidDia);
% Probability estimation of size
figure
hist(EquivDiameter*C)
xlabel('Size[m - uncalibrated]')
ylabel('Probability')

% Display some particles
figure
imshow(Ibinary);

figure 
% Display areas on image
for idx = 1:2: length(ValidDia)           % Loop through all blobs.
  Centroid = [blobMeasurements(idx).Centroid(1), blobMeasurements(idx).Centroid(2)];
  DiamSize = ['Diam. = ', num2str((EquivDiameter(idx)*C))];
  text(Centroid(1), Centroid(2), DiamSize, 'Color', 'c');
  viscircles(Centroid,EquivDiameter(idx)/2);
end