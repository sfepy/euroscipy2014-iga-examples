filename_domain = 'ig_domain.iga'

regions = {
    'Omega' : 'all',
    'Gamma1' : ('vertices of set xi10', 'facet'),
    'Gamma2' : ('vertices of set xi11', 'facet'),
}

fields = {
    'temperature' : ('real', 1, 'Omega', None, 'H1', 'iga'),
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
