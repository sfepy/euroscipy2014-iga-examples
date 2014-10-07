filename_domain = 'ig_domain_3d.iga'

regions = {
    'Omega' : 'all',
    'Gamma1' : ('vertices of set xi10', 'facet'),
    'Gamma2' : ('vertices of set xi11', 'facet'),
}

fields = {
    'displacement': ('real', 'vector', 'Omega', None, 'H1', 'iga'),
}

variables = {
    'u' : ('unknown field', 'displacement', 0),
    'v' : ('test field', 'displacement', 'u'),
}

ebcs = {
    'u1' : ('Gamma1', {'u.all' : 0.0}),
    'u2' : ('Gamma2', {'u.0' : 0.01, 'u.[1,2]' : 'get_ebcs'}),
}

def get_ebcs(ts, coors, **kwargs):
    import numpy as nm

    aux = nm.empty_like(coors[:, 1:])
    aux[:, 0] = -0.02 * coors[:, 1]
    aux[:, 1] = -0.02 + (0.15 * (coors[:, 0] - 1.0))**2

    return aux.T.flat

functions = {
    'get_ebcs' : (get_ebcs,),
}

materials = {
    'm' : ({
        'lam' : 5.769, 'mu' : 3.846,
    },),
}

integrals = {
    'i' : 4,
}

equations = {
    'balance_of_forces'
    : """dw_lin_elastic_iso.i.Omega(m.lam, m.mu, v, u) = 0""",
}

solvers = {
    'ls' : ('ls.scipy_direct', {}),
    'newton' : ('nls.newton', {
        'i_max'      : 1,
        'eps_a'      : 1e-10,
    }),
}
