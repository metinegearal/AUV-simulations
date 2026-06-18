

# Motion Controls
There are different modes and motions that can be performed with motion_wp this is a list for you to know what to control and potential issues in this module.

Simplifying, optimizing or beautifying the code is encouraged as long as it doesn't broke the code.

## Input 
(A,B,C) where it is Float32MultiArray  and topic is '/trajectory/waypoint'

A and B is x,y coordinates where AUVs position is (0,0). 
One should note that  A and B rotated according to world rotation with IMU/magnetometer even if its position is relative the AUV.
AUVs position easily can be added to the system when current electronic system is precise enough.

C is direct input from bar sensor
To position AUV to H depth 0 > C can be given where H= -C
In future 0 < C can be added with ping sonar to position the AUV according to its distance to the seabed.

![alt text](motion_optimized.gif)

## Motion Modes
### Some values:
string  self.mode which comes from the topic /movement/mode
float aruco_angle which comes from the topic '/aruco/angle'
string self.isRolling which comes from the topic '/movement/roll'

### Modes:
yaw_centerize → default mode turns to point with yaw and goes to point
no_centerize → no turning is executed just goes to the point When aruco_angle is given it will anchor this angle
full_centerize → turns to point with yaw and pitch and goes to point

rolling is executed when self.rolling gets a value "right" or "left" 
### Output:
It will return a Twist type to the topic /cmd_vel
This outputs connect to the cmd_vel_listener which sends the motion code to the pixhawk

## 

## Controls

    • Fundemantels:
        ◦ Right-Left
        ◦ Front-Back
        ◦ Up-Down
            ▪ wrong depth → control bar sensor calibration (can use qground or /mavros/global_position/rel_alt)
    • Rotations
        ◦ yaw
            ▪ wrong angle → control yaw angles, radian or angle, mostly radian is used
            ▪  unstable movement → reduce sensitivity self.yaw_tolerance 
        ◦ pitch
            ▪ unstable movement?
        ◦ Roll
            ▪ wrong way→ control desired_roll
            ▪ unstable movement?
    • Arrival
        ◦ Stop
            ▪ unstable movements in finish → reduce sensitivity self.dist_tolerance


## Future Work
Maybe images and videos can be added to recognize error patterns in the simulation or real world.