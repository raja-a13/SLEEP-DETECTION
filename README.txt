#Driver Drowsy Detection

Problem statement:
In these days,many accidents are caused due to drowsiness of the driver.
Driver may do this intentionally,it may due to continous work-load or other reason.
Many times they want into sleep without their knowing

Solution:
Our solution for is camera-based solution to detect the drowsyness of the driver.
If a camera is attached to preview a driver during driving.
we can analyse ,will alert(sound a buzzer) the driver when is drowsy or about to sleep

Method:
First,we take a web-cam input .detect the driver using image proccesing
then we dectect the state of eyes ,check if he blinking to frequently or he about to close this eyes
we also consider ,if driver is leaning his head slowy.

INSTRUCTONS TO RUN CODE

1)INSTALL mini-conda

2)RUN THE FOLLOWING COMMANDS IN CONDA CMD
conda update conda
conda update anaconda
conda create -n env_dlib
conda activate env_dlib
conda install -c conda-forge dlib
pip install opencv-python
pip install scipy
pip install playsound
pip install imutils
pip install argparse

3)COMMANDS TO ACTIVATE YOUR ENVIRONMENT
#TO activate 
conda activate env_dlib

#to deactivate
conda deactivate env_dlib

#to list
conda env list

4)RUN THE FOLLOWING COMMAND IN CONDA-CMD
python detect_drowsiness.py --shape-predictor shape_predictor_68_face_landmarks.dat --alarm alarm.wav
