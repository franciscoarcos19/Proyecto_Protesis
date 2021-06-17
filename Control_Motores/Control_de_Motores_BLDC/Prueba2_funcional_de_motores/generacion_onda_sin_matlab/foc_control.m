clear all;clc;

% f = 1;
% w = 2*pi*f;
% t = 0:0.01:1;
% y = sin(w*t);
% figure;
% plot(t,y);

onda_seno = [127,110,94,78,64,50,37,26,17,10,4,1,0,1,4,10,17,26,37,50,64,...
    78,94,110,127,144,160,176,191,204,217,228,237,244,250,253,255,253,250,...
    244,237,228,217,204,191,176,160,144,127];
%plot(onda_seno);

currentStepA=1; 
currentStepB=17;
currentStepC=33;

coilA = zeros(1,length(onda_seno));
coilB = zeros(1,length(onda_seno));
coilC = zeros(1,length(onda_seno));

for k = 1:length(onda_seno)
    currentStepA = currentStepA + 1; 
    currentStepB = currentStepA + 16;
    currentStepC = currentStepA + 32;
    
    currentStepA = mod(currentStepA,48);
    currentStepB = mod(currentStepB,48);
    currentStepC = mod(currentStepC,48);
    
    currentStepA = currentStepA + 1; 
    currentStepB = currentStepB + 1;
    currentStepC = currentStepC + 1;

    coilA(k) = onda_seno(currentStepA);
    coilB(k) = onda_seno(currentStepB);
    coilC(k) = onda_seno(currentStepC);
end

plot(coilA,'-b');hold on
plot(coilB,'-r');hold on
plot(coilC,'-g');hold on

senales = [coilA' coilB' coilC']
