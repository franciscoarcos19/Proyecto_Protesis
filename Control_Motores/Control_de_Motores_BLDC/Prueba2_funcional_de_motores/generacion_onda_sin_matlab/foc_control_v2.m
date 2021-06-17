clear all;clc;

f = 1;
w = 2*pi*f;
t = 0:0.005:1;

y1 = 128*sin(w*t)+ 128;
y2 = 128*sin(w*t + deg2rad(120)) + 128;
y3 = 128*sin(w*t + deg2rad(240)) + 128;

y1 = round(y1);
y2 = round(y2);
y3 = round(y3);

figure;
plot(t,y1,'-b',t,y2,'-r',t,y3,'-g');

senal =[y1' y2' y3']

% En el dato 26 empieza la otra señal
% 
