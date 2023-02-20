#
# Example parabolic motion
#

# Here we import the mathematical library and the plots library
import numpy as np
import matplotlib.pyplot as plt
 
#
# FUNCTION DRAW A TRAJECTORY FOR PARABOLIC MOTION
# Input: velocity and angle 
#
def draw_trajectory(u, theta,texp):
    #convert angle in degrees to rad
    theta = np.radians(theta)
    #gravity acceleration in m/s2
    g = 9.8
    # Time of flight
    t_flight = (4*u*np.sin(theta))/g
    # find time intervals
    intervals = np.arange(0, t_flight, 0.001)
    #Calculate where will the explosion occur
    xexpl=u*np.cos(theta)*texp
    yexpl=u*np.sin(theta)*texp-0.5*g*(texp**2)    
    # create an empty list of x and y coordinates (non-explosive)
    x = []
    y = []
    #Do a loop over time calculating the coordinates for the non-explosive trajectory
    for t in intervals:
        x.append(u*np.cos(theta)*t)
        y.append(u*np.sin(theta)*t - 0.5*g*t*t)
    # create an empty list of x and y coordinates (explosive)
    xexp = []
    yexp = []
    #Do a loop over time calculating the coordinates for the explosive trajectory
    for t in intervals:
        if t <= texp:
            xexp.append(u*np.cos(theta)*t)
            yexp.append(u*np.sin(theta)*t - 0.5*g*t*t)
        else:
            te=t-texp
            xexp.append(xexpl+2*u*np.cos(theta)*te)
            yexp.append(yexpl+2*te*(u*np.sin(theta)-g*texp)-0.5*g*(te**2))

    #Plot the trajectories
    plt.plot(x, y, linestyle='dashed')
    plt.plot(xexp, yexp)
    plt.plot(xexpl,yexpl,marker='x',color='r')
    plt.ylim(bottom=0)
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.title('Projectile motion')

#--------------------------------------------------------------------------------
# Main Program: give specific values and call to the function draw_trajectory
#--------------------------------------------------------------------------------

print("Parabolic motion of a projectile\n")

#Ask the user for angle, explosion time and velocity
print("Enter desired launch angle in degrees (recommended 45 degrees):")
theta=float(input())
print("Enter desired launch velocity in meters/s:")
u=float(input())
print("Enter desired explosion time in seconds:")
texp=float(input())

#
draw_trajectory(u, theta, texp)

        
# Add a legend and show the graph
plt.legend(['Trajectory without explosion', 'Trajectory with explosion','Explosion'],loc='upper right',prop={'size': 8})
plt.show()
