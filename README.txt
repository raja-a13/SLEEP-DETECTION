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