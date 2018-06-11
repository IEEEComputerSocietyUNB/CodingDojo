#!/usr/bin/env python
# coding: utf-8
''' Dojo: Controle de Malha Fechada da Tartaruga

Bem vindos ao dojo de programação ROS-Works.

Objetivo:
    Desenvolver algoritimos de controle de malha fechada no ambiente Turtlesim.

Materiais:
    Este é o código fonte principal com que vocês devem trabalhar.
    Como ponto de partida, deixamos prontos os arquivos turtle_kinematics.py e turtle_closed_loop_node.py.
    Eles tratam, respectivamente, das funcionalidades de movimentação da tartaruga em ambiente ROS
    e da função principal que realiza a chamada deste arquivo.

Métodologia e Resultados Esperados:
    Desenvolver por meio de TDD o código fonte das funções TurtleClosedLoop.go_to_point(...).
    Sintam-se à vontade para desenvolver métodos e criar variáveis auxiliares para esta tarefa.

Desafios Extra:
    Hora de desenhar! Crie testes e funcoes para a tartaruga desenhar um quadrado, um triangulo e um circulo.
    Pode aproveitar o codigo do desafio anterior :)

Chamada de Testes Unitarios:
    catkin build --catkin-make-args run_tests

Instruções de Execução:
    roslaunch ros-works-dojos coding_dojo_2018_closed_loop.launch

Mestre:
    - Pedro Henrique S. Perruci - 14/0158596 - Eng. Mecatrônica

Participantes:
    -
'''

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

from turtle_kinematics import TurtleKinematics

class TurtleClosedLoop(TurtleKinematics):
    ''' Classe para o controle de malha fechada da tartaruga.
    Torna-se possível fechar a malha por meio do callback no tópico "turtle1/pose".
    Ele fornece a posição atual da tartaruga dentro da simulação.
    Podemos, portanto, relacionar o erro de posicao a um algoritimo de controle de movimentacao da tartaruga.
    '''
    def __init__(self):
        ''' Construtor da classe TurtleClosedLoop
        Todo metodo da classe deve ter como primeiro parametro o ponteiro da classe (self)
        Analogamente, variaveis inicializadas dentro da classe devem ser chamadas e declaradas
        pelo o prefixo self.var_name.
        '''
        TurtleKinematics.__init__(self) # calls parent class constructor
        # Elemento subscriber ROS
        rospy.Subscriber("turtle1/pose", Pose, self.callback)
        # inicializacao de variaveis recebidas no callback
        self.turtle_x = 0
        self.turtle_y = 0
        self.turtle_theta = 0
        self.turtle_linear_velocity = 0
        self.turtle_angular_velocity = 0

    def callback(self, msg):
        ''' Funcao chamada toda a vez que atualiza-se o topico: turtle1/pose '''
        self.turtle_x = msg.x
        self.turtle_y = msg.y
        self.turtle_theta = msg.theta
        self.turtle_linear_velocity = msg.linear_velocity
        self.turtle_angular_velocity = msg.angular_velocity
        # print 'x = ',self.turtle_x,'\ny = ',self.turtle_y
        rospy.spin()

    def go_to_point(self, x, y, vel=1, kp=5, tolerance=0.01):
        ''' [Coding Dojo!]
            Recebe ponto, vai ao ponto.
            Realize um controle proporcional de malha fechada para a movimentacao da tartaruga.
            Params:
                x: coordenada destino horizontal.
                y: coordenada destino vertical.
                vel: velocidade linear maxima para a tartaruga.
                kp: o ganho proporcional de controle.
                tolerance: distancia minima do ponto atual ao ponto desejado para encerrar o movimento.
            Dica:
                O controle classico eh usualmente aplicado a uma unica variavel. Qual controlar?
        '''
        pass
