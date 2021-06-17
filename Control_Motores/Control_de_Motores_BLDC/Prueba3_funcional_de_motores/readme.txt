El código open_control.ino permite que el motor se active cuando se cumple un threshold, en este caso se está trabajando con un potenciómetro, posteriormente esta señal será proporcionada por el sistema de sensores mioeléctricos

El código open_control_sin_v2.ino hace lo mismo que el código open_control.ino pero utiliza una onda seno creada por mi con 201 valores, esto permite que el movimiento sea más suave, pero tambien más lento

El código 2Threshold_inversion_giro.ino permite que el motor gire en ambos sentidos, para gobernar el sentido de giro se utiliza la señal analógica de un potenciómetro mediante un if para dos rangos

En la página web https://www.etechnophiles.com/change-frequency-pwm-pins-arduino-uno/ se encuentra la información relacionada con el ajuste de las frecuencias de la señal pwm del Arduino