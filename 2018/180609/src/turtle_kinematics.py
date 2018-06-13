#!/usr/bin/env python
# coding: utf-8
import rospy
from geometry_msgs.msg import Twist
import math

class TurtleKinematics:
    ''' Classe que modela funções básicas de movimentação tartarugas '''
    def __init__(self, turtle_name='turtle1'):
        ''' Construtor da classe TurtleKinematics '''
        # -- variáveis internas da classe -- #
        # Elemento publisher ROS
        self.pub_vel = rospy.Publisher(turtle_name+'/cmd_vel', Twist, queue_size = 1)
        # Frequencia de cada interacao
        self.rate = rospy.Rate(10) #Hertz

    def move_angular(self, vel):
        ''' Cria e envia mensagem de velocidade angular '''
        vel_msg = Twist()
        vel_msg.angular.z = vel
        self.pub_vel.publish(vel_msg)
        self.rate.sleep()

    def move_linear(self, vel):
        ''' Cria e envia mensagem de velocidade linear '''
        vel_msg = Twist()
        vel_msg.linear.x = vel
        self.pub_vel.publish(vel_msg)
        self.rate.sleep()

    def move_general(self, vel, ang):
        ''' Recebe velocidades linear e angular para movimentar a tartaruga '''
        vel_msg = Twist()
        vel_msg.linear.x = vel
        vel_msg.angular.z = ang
        self.pub_vel.publish(vel_msg)
        self.rate.sleep()

    def stop(self):
        ''' Cria e publica mensagem para parar a tartaruga '''
        vel_msg = Twist()
        self.pub_vel.publish(vel_msg)
