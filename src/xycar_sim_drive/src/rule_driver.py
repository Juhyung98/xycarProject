#!/usr/bin/python

import rospy, math
from std_msgs.msg import Int32MultiArray

a = Int32MultiArray()
a.data = [0,0,0,0,0,0,0,0]

def callback(msg):                                                                  # origin
    a.data = msg.data
    print(msg.data)                                                                 # origin

rospy.init_node('guide')                                                            # origin
motor_pub = rospy.Publisher('xycar_motor_msg', Int32MultiArray, queue_size=1)       # origin
ultra_sub = rospy.Subscriber('ultrasonic', Int32MultiArray, callback)               # origin

xycar_msg = Int32MultiArray()       # origin


# def avoid_edge():
#     global angle
#     angle = math.atan(110/float(a.data[6]))*100
#     if a.data[6] < 70 or a.data[2] < 15 :
#         angle = -40
#     elif a.data[7] < 70 or a.data[0] < 15:
#         angle = 40

# def rotate_detect():
#     if a.data[2] > a.data[1]:
#         avoid_edge()
#     if a.data[0] > a.data[1]:
#         avoid_edge()



# while not rospy.is_shutdown():      # origin
#     angle = 0                       # origin
#     if a.data[6] > a.data[7] :
#         angle = 30
#         rotate_detect()
#     else:
#         angle = -30 
#         rotate_detect()


    # if a.data[6] < a.data[7]:
    #     angle -= 10
    # elif a.data[7] < a.data[6]:
    #     angle += 10
    # else:
    #     angle = 0
    #if a.data[2]

    # if a.data[2] > 150:
    #     angle = 50
    


while not rospy.is_shutdown():      # origin
    angle = 0                       # origin
    if a.data[2] > 150:
        angle = math.atan(110/float(a.data[6]))*100


    xycar_msg.data = [angle, 25]        # origin
    motor_pub.publish(xycar_msg)        # origin
