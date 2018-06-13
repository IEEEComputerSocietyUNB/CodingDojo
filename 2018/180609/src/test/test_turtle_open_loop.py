#!/usr/bin/env python
PKG = 'ros-works-dojos'
import roslib; roslib.load_manifest(PKG)
# -------------------------------------------- #
import sys
# Adiciona diretorio anterior ao path
sys.path.insert(0,'..')

from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises

import turtle_open_loop
import math

class TestOpenLoop(object):
    @classmethod
    def setup_class(klass):
        '''This method is run once for each class before any tests are run'''

    @classmethod
    def teardown_class(klass):
        '''This method is run once for each class _after_ all tests are run'''

    def setUp(self):
        '''This method is run once before _each_ test method is executed'''
        # self.open_loop = turtle_open_loop.TurtleOpenLoop()
        pass

    def teardown(self):
        '''This method is run once after _each_ test method is executed'''

    def test_Move_1x(self):
        ''' Testar se a tartaruga se move 1 unidade em X '''
        assert_equal(turtle_open_loop.moveX(0, 0, 1, 0), (1, 0))

    def test_Nao_Move(self):
        ''' Testar se a tartaruga nao se move'''
        assert_equal(turtle_open_loop.moveX(1, 0, 1, 0), (0 , 0))

    # def test_Move_90(self):
    #     """Testar se move na 90 graus"""
    #     assert_equal(moveX(0, 0, 0, 1), (math.pi / 2))

    def test_TimeToX(self):
        ''' Testar tempo para andar em x com velocidade 1 '''
        x = 1
        vel_lin = 1
        assert_equal(turtle_open_loop.timeToX(x, vel_lin), 1)

    def test_TimeToY(self):
        ''' Testar tempo para andar em y com velocidade 1 '''
        y = 1
        vel_lin = 1
        assert_equal(turtle_open_loop.timeToY(y, vel_lin), 1)

    def test_TimeToTurn(self):
        ''' Testar tempo para girar com vel_ang = 0.5'''
        theta = 0.5
        vel_ang = 0.5
        assert_equal(turtle_open_loop.timeToTurn(theta, vel_ang), 1)

    # def test_TimeToTurnNegativo(self):
    #     ''' Testar tempo para girar com vel_ang negativa '''
    #     theta = -1
    #     vel_ang = 0.5
    #     assert_equal(turtle_open_loop.timeToTurn(theta, vel_ang), 2)

    def test_Theta(self):
        ''' Testar a geracao de teta '''
        x = -1
        y = -1
        assert_equal(turtle_open_loop.findTheta(x, y), 5*math.pi/4)










# oi
