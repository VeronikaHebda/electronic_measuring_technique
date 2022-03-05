# electronic measuring technique 
task_1  
The task was to write a program using any tools and / or programming language that would execute in separate tabs  
individual three guidelines:  
  
1.1. Calculation of ng and ng factors for wavelengths from 400nm to 1600nm and generating a dependency graph of these  
wavelength coefficients and the presentation of the results in the table every 10 nm wavelength. 
  
1.2 Calculation of the atmospheric correction when entered by the user:  
• wavelength (nm)  
• dry temperature (degrees C)  
• wet temperature (degrees C)  
• pressure (hPa)  
• the measured length (m)  
The program returns:  
• the atmospheric correction for 1 km with the given conditions  
• atmospheric conditions (mm)  
• correction of the measured length (mm)  
• length corrected (m)  
  
1.3. Calculation of length difference between arc and chord for the interval from 1km to 100km and generating  
a graph showing the change of this difference with distance and presentation of the results in table every 1km.  
  
task_2  
The aim of the exercise was to create a program that:  
• reads measurement data from the leveling instrument using the serial port.  
• has an appropriate graphic interface that allows you to select the parameters of the connected equipment,  
displaying the results and saving them to a file.  
The Python programming language, version 3.10 and the PyCharm Community Edition 2021.2.2. environment were used to perform the exercise.  
To read data from the level it was necessary to install drivers. The program includes lists of  
transmission properties to choose from. It allows you to specify the exact properties of the data  
sent on the port: port name, baud rate, number of bytes, stop bits.  
