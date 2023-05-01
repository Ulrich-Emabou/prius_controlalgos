#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
    
def path_publisher():
    pub = rospy.Publisher('path_topic', Float32MultiArray, queue_size=10)
    rospy.init_node('path_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
        
    while not rospy.is_shutdown():
        # create a 2D array of x and y coordinates
        coordinates = [[0.0, 0.0], [1.0, 1.0], [2.0, 2.0], [3.0, 3.0]]
        
        # create Float32MultiArray message and fill with coordinates
        msg = Float32MultiArray()
        msg.data = [val for sublist in coordinates for val in sublist]

        # publish the message to the topic
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        path_publisher()
    except rospy.ROSInterruptException:
        pass

#This code creates a ROS node called "coordinates_publisher" that publishes an array of x and y coordinates to a custom topic
#called "path_publisher" at a rate of 10Hz.
#The coordinates are represented as a 2D array and are converted into a Float32MultiArray message before publishing.