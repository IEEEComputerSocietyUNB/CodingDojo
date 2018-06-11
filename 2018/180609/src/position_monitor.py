# coding: utf-8
import rospy
from turtlesim.msg import Pose
import math

class PositionMonitor:
    ''' Classe responsavel por monitorar o erro de posicao apos algoritimos de movimentacao '''
    def __init__(self):
        ''' Construtor da classe
        Inicializa variaveis internas do objeto.
        '''
        # Elemento subscriber ROS
        rospy.Subscriber("turtle1/pose", Pose, self.callback)

    def callback(self, msg):
        ''' Funcao chamada toda a vez que atualiza-se o topico: turtle1/pose '''
        self.turtle_x = msg.x
        self.turtle_y = msg.y
        self.turtle_theta = msg.theta
        self.turtle_linear_velocity = msg.linear_velocity
        self.turtle_angular_velocity = msg.angular_velocity
        # print 'x = ',self.turtle_x,'\ny = ',self.turtle_y
        rospy.spin()

    def set_target_coordinates(self, x, y):
        ''' Informa posicao destino do movimento
        O objeto, entao guarda a posicao atual e a posicao de destino, para referências futuras
        '''
        # posicao inicial e guardada
        self.initial_position_x = self.turtle_x
        self.initial_position_y = self.turtle_y
        # posicao destino guardada
        self.target_position_x = x
        self.target_position_y = y

    def get_actual_position(self):
        return self.turtle_x, self.turtle_y

    def get_goal_position(self):
        return self.target_position_x, self.target_position_y

    def get_relative_goal_position(self):
        ''' Returns relative ending position, when compared to initial position '''
        relative_target_x = self.initial_position_x + self.target_position_x
        relative_target_y = self.initial_position_y + self.target_position_y
        return relative_target_x, relative_target_y

    def module_difference(self, diff_x, diff_y):
        return math.sqrt(diff_x**2 + diff_y**2)

    def get_final_position_error(self):
        ''' Compara-se a posicao atual com aquela guardada em self.target_position_x e self.target_position_y '''
        diff_x = self.target_position_x - self.turtle_x
        diff_y = self.target_position_y - self.turtle_y
        # get their module difference
        abs_diff = self.module_difference(diff_x, diff_y)
        return abs_diff, diff_x, diff_y

    def get_relative_position_error(self):
        ''' Compara a posicao atual com a posicao final relativa a inicial '''
        relative_target_x, relative_target_y = self.get_relative_goal_position()
        diff_x = relative_target_x - self.turtle_x
        diff_y = relative_target_y - self.turtle_y
        # get their module difference
        abs_diff = self.module_difference(diff_x, diff_y)
        return abs_diff, diff_x, diff_y
