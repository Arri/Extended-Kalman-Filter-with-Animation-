 # Extended Kalman Filter

https://www.thepoorengineer.com/?cat=-1

This EKF written in Python uses sensor input from the BNO055 IMU.
It reads the gyro, accelerator and magnetometer data and combines them to one output that is displayd by the animated  position of a 3D cube.
The (x,y,z) coordinates produced by the gyro, the accelerometer and the  magnetometer are converted to roll, pitch and yaw angles using quternions.

To install required libraries execute:
> sudo pip install -r requirements.txt

Call:
> python BordDisplay_EKF.py