from numpy import min
from numpy import array as arr
from numpy import clip, sign
from numpy.linalg import norm

from typing import NewType


vec2 = NewType('vec2', arr[float,float])
vec3 = NewType('vec4', arr[float,float,float])
vec4 = NewType('vec4', arr[float,float,float,float])


def integrateMotion(delta_t: float, t0: float, Y: vec4, uv_domain : tuple[vec2,vec2], RHS: function) -> vec4:

    '''
        Finds the state variable, Y, of the dynamical system modelled by dY/dt = RHS(t,Y), at time t0 + delta_t
        using a runge-kutta numerical scheme.
    '''

    T = t0
    time_left = delta_t
    time_step = 0.0001
    time_step = min([time_step, time_left])
    Y_next = Y
    while time_left > 0.0:
        k1 = RHS(t0, Y_next)
        k2 = RHS(t0+time_step/2, Y_next + time_step * k1 / 2.0)
        k3 = RHS(t0+time_step/2, Y_next + time_step * k2 / 2.0)
        k4 = RHS(t0+time_step, Y_next + time_step * k3)
        t0 += time_step
        Y_next += time_step / 6.0 * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        """
        if Y_next[0] < uv_domain[0][0] or Y_next[0] > uv_domain[0][1]:
            Y_next[0] = clip(Y_next[0],-0.5,0.5)
            Y_next[1] = - 0.9*Y_next[1]
        if Y_next[2] < uv_domain[1][0] or Y_next[2] > uv_domain[1][1]:
            Y_next[2] = clip(Y_next[2],-0.5,0.5)
            Y_next[3] = -0.9*Y_next[3]
        """
        time_left -= time_step
        time_step = min([time_step, time_left])
    return Y_next