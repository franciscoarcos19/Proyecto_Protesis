clear all;clc;

f = 1;
w = 2*pi*f;
t = 0:0.005:1;

y = 127*sin(w*t)+ 128;
y = round(y);

onda_seno = y;

desfase = 68;

currentStepA=1; 
currentStepB=desfase;
currentStepC=desfase*2;

coilA = zeros(1,length(onda_seno));
coilB = zeros(1,length(onda_seno));
coilC = zeros(1,length(onda_seno));

for k = 1:length(onda_seno)
    currentStepA = currentStepA + 1; 
    currentStepB = currentStepA + desfase;
    currentStepC = currentStepA + desfase*2;
    
    currentStepA = mod(currentStepA,length(onda_seno));
    currentStepB = mod(currentStepB,length(onda_seno));
    currentStepC = mod(currentStepC,length(onda_seno));
    
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
grid minor;

senales = [coilA' coilB' coilC'];
