import numpy as nm

from sfepy.linalg import get_coors_in_ball

filename_mesh = 'fe_domain.mesh'

centre = nm.array([0.0, 0.0], nm.float64)

functions = {
    'get_circle1' : (lambda coors, domain:
                     get_coors_in_ball(coors, centre, 1.0001),),
    'get_circle2' : (lambda coors, domain:
                     get_coors_in_ball(coors, centre, 2.4999, False),),
}

regions = {
    'Omega' : 'all',
    'Gamma' : ('vertices of surface', 'facet'),
    'Gamma1' : ('(r.Gamma -s (r.Gamma3 +s r.Gamma4))'
                ' *v vertices in (x < 0.9)', 'facet'),
    'Gamma2' : ('r.Gamma -s (r.Gamma1 +s r.Gamma3 +s r.Gamma4)', 'facet'),
    'Gamma3' : ('vertices by get_circle1', 'facet'),
    'Gamma4' : ('vertices by get_circle2', 'facet'),
}

fields = {
    'temperature' : ('real', 1, 'Omega', 2),
}

variables = {
    'T' : ('unknown field', 'temperature', 0),
    's' : ('test field',    'temperature', 'T'),
}

ebcs = {
    'T1' : ('Gamma1', {'T.0' : 0.5}),
    'T2' : ('Gamma2', {'T.0' : -0.5}),
}

materials = {}

integrals = {
    'i' : 3,
}

equations = {
    'Temperature' : """dw_laplace.i.Omega(s, T) = 0"""
}

solvers = {
    'ls' : ('ls.scipy_direct', {}),
    'newton' : ('nls.newton', {
        'i_max'      : 1,
        'eps_a'      : 1e-10,
    }),
}

options = {
    'nls' : 'newton',
    'ls' : 'ls',
}
