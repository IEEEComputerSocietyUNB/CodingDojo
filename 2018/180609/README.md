# Coding Dojo UnB

## Problema: Cinemática em ROS (Robotic Operational System)

As soluções do framework Robot Operating System (ROS) são utilizadas nos maiores laboratórios de pesquisa e estão embarcados em diversos dispositivos robóticos, comerciais e industriai inteiro.
Propõe-se neste Dojo de Programação, explorar um simulador clássico do sistema, o [turtlesim](http://wiki.ros.org/turtlesim).

Devemos utilizar a metodologia TDD (Test Driven Development) e programação em Python para comandar a tartaruga no espaço 2D.

### Comandos Úteis

* Compilar o Workspace e chamar testes:
```(bash)
  catkin build --catkin-make-args run_tests
```

#### Instruções de Execução:
  * Parte 1
```(bash)
    roslaunch ros-works-dojos coding_dojo_2018_open_loop.launch
```
  * Parte 2
```(bash)  
  roslaunch ros-works-dojos coding_dojo_2018_closed_loop.launch
```

## Entregas ##
* Parte 1: Controle em Malha Aberta (turtle_open_loop.py)
  * Entrega 1.1: Movimentação da tartaruga por coordenadas relativas
  * Entrega 1.2: Movimentação da tartaruga por coordenadas absolutas
  * Entrega 1.3: Desenho de formas geométricas (modificar *_node.py)
    * Quadrado
    * Círculo
    * Triângulo
    
* Parte 2: Controle em Malha Fechada (turtle_closed_loop.py)
  * Entrega 2.1: Movimentação da tartaruga por coordenadas absolutas
  * Entrega 2.2: Desenho de formas geométricas (modificar *_node.py)
    * Quadrado
    * Círculo
    * Triângulo
