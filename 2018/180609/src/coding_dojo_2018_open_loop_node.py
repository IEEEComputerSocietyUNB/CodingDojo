#!/usr/bin/env python
# coding: utf-8
import rospy
from turtle_open_loop import TurtleOpenLoop
import position_monitor

def print_menu():
    ''' Imprime menu e retorna opcao escolhida '''
    print '--------- ROS WORKS TURTLESIM SWARM --------- (v0.1)'
    print 'Relative or absolute coordinates?'
    print '1 - Relative'
    print '2 - Absolute'
    choice = get_value('Your choice >> ')
    print 'Where do you want to go?'
    coord_x = get_value('X coordinate >> ')
    coord_y = get_value('Y coordinate >> ')
    return choice, coord_x, coord_y

def get_value(message):
    ''' Imprime pergunta e recebe valor inteiro '''
    value = raw_input(message)
    value = float(value)
    return value

def print_position_error(monitor):
    abs_diff, diff_x, diff_y = monitor.get_final_position_error()
    print 'Turtle position:', monitor.get_actual_position()
    print 'Goal position:', monitor.get_goal_position()
    print 'X Position Error: ', diff_x
    print 'Y Position Error: ', diff_y
    print 'Absolute Position Error: ', abs_diff

def print_relative_error(monitor):
    abs_diff, diff_x, diff_y = monitor.get_relative_position_error()
    print 'Turtle position:', monitor.get_actual_position()
    print 'Relative Goal position:', monitor.get_relative_goal_position()
    print 'X Position Error: ', diff_x
    print 'Y Position Error: ', diff_y
    print 'Absolute Position Error: ', abs_diff

def main():
    ''' Nó executável para o controle em malha aberta '''
    rospy.init_node('coding_dojo_2018_open_loop')
    turtle = TurtleOpenLoop()
    monitor = position_monitor.PositionMonitor()
    while not rospy.is_shutdown():
        try:
            choice, coord_x, coord_y = print_menu()
            if choice == 1:
                ''' Relative coordinates '''
                monitor.set_target_coordinates(coord_x, coord_y)
                turtle.go_to_point_relative(coord_x, coord_y)
                print_relative_error(monitor)
            if choice == 2:
                ''' Absolute coordinates '''
                monitor.set_target_coordinates(coord_x, coord_y)
                turtle.go_to_point_absolute(coord_x, coord_y)
                print_position_error(monitor)
        except rospy.ROSInterruptException:
            pass

if __name__ == '__main__':
    main()
