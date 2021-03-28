pkg load image
I = imread('picture_1.png');

I = rgb2gray(I) > 100; % Try different values 
I = imfill(I, 'holes');
figure
imshow(I)

BW = edge(I,'canny');
figure
imshow(BW);

[H,theta,rho] = hough(BW);

figure
imshow(imadjust(rescale(H)),[],...
       'XData',theta,...
       'YData',rho,...
       'InitialMagnification','fit');
xlabel('\theta (degrees)')
ylabel('\rho')
axis on
axis normal 
hold on
colormap(gca,hot)

P = houghpeaks(H,5,'threshold',ceil(0.3*max(H(:))));

x = theta(P(:,2));
y = rho(P(:,1));
figure
plot(x,y,'s','color','black');

lines = houghlines(BW,theta,rho,P,'FillGap',5,'MinLength',7);

figure, imshow(I), hold on
max_len = 0;
average=0;
for k = 1:length(lines)
   xy = [lines(k).point1; lines(k).point2];
   plot(xy(:,1),xy(:,2),'LineWidth',2,'Color','green');

   % Plot beginnings and ends of lines
   plot(xy(1,1),xy(1,2),'x','LineWidth',2,'Color','yellow');
   plot(xy(2,1),xy(2,2),'x','LineWidth',2,'Color','red');
    %disp(xy(1,2));
    average=average + (xy(1,2)+xy(2,2))/2;
   % Determine the endpoints of the longest line segment
   len = norm(lines(k).point1 - lines(k).point2);
   if ( len > max_len)
      max_len = len;
      xy_long = xy;
   end
end
 disp(average/length(lines));
% highlight the longest line segment
plot(xy_long(:,1),xy_long(:,2),'LineWidth',2,'Color','blue');