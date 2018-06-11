#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Dojo: Controle de Malha Aberta da Tartaruga

Bem vindos ao dojo de programação ROS-Works.

Objetivo:
    Desenvolver algoritimos de controle de malha aberta no ambiente Turtlesim.
    O dojo deve se desenvolver em duas etapas: coordenadas relativas e coordenadas absolutas.

Materiais:
    Este é o código fonte principal com que vocês devem trabalhar hoje.
    Como ponto de partida, deixamos prontos os arquivos turtle_kinematics.py e turtle_open_loop_node.py
    Eles tratam, respectivamente, das funcionalidades de movimentação da tartaruga em ambiente ROS
    e da função principal que realiza a chamada deste arquivo.

Métodologia e Resultados Esperados:
    Desenvolver por meio de TDD o código fonte das funções TurtleOpenLoop.go_to_point_relative(...) e TurtleOpenLoop.go_to_point_absolute(...).
    Sintam-se à vontade para desenvolver métodos e criar variáveis auxiliares para esta tarefa.

Desafios Extra:
    Hora de desenhar! Crie testes e funcoes para a tartaruga desenhar um quadrado, um triangulo e um circulo.

Chamada de Testes Unitarios:
    catkin build --catkin-make-args run_tests

Instruções de Execução:
    roslaunch ros-works-dojos coding_dojo_2018_open_loop.launch

Mestre:
    - Pedro Henrique S. Perruci - 14/0158596 - Eng. Mecatrônica

Participantes:
    -
'''


import rospy
from turtlesim.msg import Pose
import math

from turtle_kinematics import TurtleKinematics

def moveX(x0, y0, x1, y1):
    """
    x0 e y0 sao a posicao atual, x1 e y1 sao a posicao final
    """
    v = 0
    if x0 != x1:
        v = 1
    return (v, 0)

def timeToX(x, vel_lin):
    ''' Retorna tempo necessario para andar X unidades a velocidade vel_lin '''
    return x/vel_lin

def timeToY(y, vel_lin):
    ''' Retorna tempo necessario para andar X unidades a velocidade vel_lin '''
    return y/vel_lin

def findTheta(x, y):
    theta = math.atan2(y, x)
    if theta < 0:
        theta += 2*math.pi
    return theta

def timeToTurn(theta, vel_ang):
    return theta/vel_ang


class TurtleOpenLoop(TurtleKinematics):
    ''' Classe para o controle em malha aberta da tartaruga.'''
    def __init__(self):
        ''' Construtor da classe TurtleOpenLoop
        Todo metodo da classe deve ter como primeiro parametro o ponteiro da classe (self)

        Analogamente, variaveis inicializadas dentro da classe devem ser chamadas e declaradas
        pelo o prefixo self.var_name.
        '''
        TurtleKinematics.__init__(self) # calls parent class constructor


    def move_until(self, time, vel_lin, vel_ang):
        ''' Realiza movimento durante uma quantidade de tempo definida.
        Params:
            time: tempo de movimentação.
            vel_lin: velocidade linear.
            vel_ang: velocidade angular
        '''
        now = rospy.get_time()
        wait_time = now + time
        rate = rospy.Rate(10) # loop rate (Hz)
        while now < wait_time:
            self.move_general(vel_lin, vel_ang)
            now = rospy.get_time()
            rate.sleep()
        self.stop()

    def go_to_point_relative(self, x, y, vel_lin=0.5, vel_ang=0.5):
        ''' [Coding Dojo!]
        Controle em malha aberta para mover a tartaruga em coordenadas relativas x e y.
        Params:
            x: posição destino X
            y: posição destino Y
            vel_lin: velocidade linear de movimentação
            vel_ang: velocidade angular de movimentação
        '''
        # t = timeToX(x, vel_lin)
        # t1 = timeToy(y, vel_lin)
        #self.move_general(1, 0)
        theta = math.atan2(y, x)
        t = timeToTurn(theta, vel_ang)
        # Rotation
        self.move_until(t, 0, vel_ang)
        distance = math.sqrt(x**2 + y**2)
        t = timeToX(distance, vel_lin)
        self.move_until(t, vel_lin ,0)

    def go_to_point_absolute(self, x, y, vel_lin=0.5, vel_ang=0.5):
        ''' [Coding Dojo!]
        Controle em malha aberta para mover a tartaruga em coordenadas absolutas x e y.
        Params:
            x: posição destino X
            y: posição destino Y
            vel_lin: velocidade linear de movimentação
            vel_ang: velocidade angular de movimentação
        '''
        pass
