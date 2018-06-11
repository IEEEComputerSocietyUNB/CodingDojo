#!/usr/bin/env python
# coding: utf-8
import rospy
import turtle_closed_loop
import position_monitor

def print_menu():
    ''' Imprime menu e retorna opcao escolhida '''
    print '--------- ROS WORKS TURTLESIM CLOSED LOOP --------- (v0.1)'
    print 'Where do you want to go?'
    coord_x = get_value('X coordinate >> ')
    coord_y = get_value('Y coordinate >> ')
    return coord_x, coord_y

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

def main():
    ''' Nó executável para o controle em malha fechada '''
    rospy.init_node('coding_dojo_2018_closed_loop')

    turtle = turtle_closed_loop.TurtleClosedLoop()
    monitor = position_monitor.PositionMonitor()
    while not rospy.is_shutdown():
        try:
            x, y = print_menu()
            monitor.set_target_coordinates(x, y)
            turtle.go_to_point(x, y)
            print_position_error(monitor)
        except rospy.ROSInterruptException:
            pass

if __name__ == '__main__':
    ''' Chamada da funcao principal executavel '''
    main()
