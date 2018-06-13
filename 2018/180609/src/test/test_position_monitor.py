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

import position_monitor

class TestPositionMonitor(object):
    @classmethod
    def setup_class(klass):
        '''This method is run once for each class before any tests are run'''

    @classmethod
    def teardown_class(klass):
        '''This method is run once for each class _after_ all tests are run'''

    def setUp(self):
        '''This method is run once before _each_ test method is executed'''
        self.monitor = position_monitor.PositionMonitor()

    def teardown(self):
        '''This method is run once after _each_ test method is executed'''

    def test_GoalPositionError_0(self):
        ''' Position error Tests: Emulate turtle at (1,1) and goal at (1,1). Expects (0, 0, 0) '''
        self.monitor.turtle_x, self.monitor.turtle_y = 1, 1
        self.monitor.target_position_x, self.monitor.target_position_y = 1, 1
        assert_equal(self.monitor.get_final_position_error(), (0, 0, 0))

    def test_GoalPositionError_1x(self):
        ''' Position error Tests: Emulate turtle at (2,3) and goal at (3,3). Expects (1, 1, 0) '''
        self.monitor.turtle_x, self.monitor.turtle_y = 2, 3
        self.monitor.target_position_x, self.monitor.target_position_y = 3, 3
        assert_equal(self.monitor.get_final_position_error(), (1, 1, 0))

    def test_GoalPositionError_1y(self):
        ''' Position error Tests: Emulate turtle at (2,3) and goal at (2,4). Expects (1, 0, 1) '''
        self.monitor.turtle_x, self.monitor.turtle_y = 2, 3
        self.monitor.target_position_x, self.monitor.target_position_y = 2, 4
        assert_equal(self.monitor.get_final_position_error(), (1, 0, 1))

    def test_RelativePositionError_0(self):
        ''' Relative position error test: emulate initial position (1,1), final relative position (0,0). Expects (0, 0, 0) '''
        self.monitor.turtle_x, self.monitor.turtle_y = 1, 1
        self.monitor.set_target_coordinates(0, 0)
        assert_equal(self.monitor.get_relative_position_error(), (0, 0, 0))

    def test_RelativePositionError_1x(self):
        ''' Relative position error test: emulate initial position (1,1), final relative position (0,0). Expects (0, 0, 0) '''
        self.monitor.turtle_x, self.monitor.turtle_y = 1, 1
        self.monitor.set_target_coordinates(1, 0)
        assert_equal(self.monitor.get_relative_position_error(), (1, 1, 0))

    def test_RelativePositionError_1y(self):
        ''' Relative position error test: emulate initial position (1,1), final relative position (0,0). Expects (0, 0, 0) '''
        self.monitor.turtle_x, self.monitor.turtle_y = 1, 1
        self.monitor.set_target_coordinates(0, 1)
        assert_equal(self.monitor.get_relative_position_error(), (1, 0, 1))

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(PKG, 'test_position_monitor', TestBareBones)
