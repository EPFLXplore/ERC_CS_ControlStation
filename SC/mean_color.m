A = imread('zelda.png');
size_image = size(A);
R = A(:,:,1); 
G = A(:,:,2); 
B = A(:,:,3);
​
black_index = 0;
​
maxy= size_image(1);
maxx= size_image(2);
​
increment=[0 0 0];
​
for x = 1:maxx
    for y = 1:maxy
        color_vector1=[R(y,x) G(y,x) B(y,x)];
​
        color_vector = cast(color_vector1, 'double');
​
        if (color_vector1(1)<=60 && color_vector1(2)<=60 && color_vector1(3)<=60) %shadow
            black_index=black_index+1; %pixel not taken into account
        else 
        increment = increment+color_vector;
        end
    end
end
​
mean = increment/(maxx*maxy - black_index);
disp(round(mean));
​