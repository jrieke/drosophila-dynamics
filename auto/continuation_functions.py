from Tkinter import TclError
import auto


default_params = {'I': -12, 'gleak': 6.8, 'gKs': 50, 'gKf': 24.1, 'gNa': 100, 'gNaP': 0.8}


# Return a copy of the dict params, coplemented by default values for all parameters that are neither in params nor in exclude.
def add_default_params(params, exclude=None):
    if params is None: 
        params = {}
    else:
        params = params.copy()
        
    if exclude is None: exclude = []    
    for key, val in default_params.items():
        if key not in exclude:
            params.setdefault(key, val)
    return params


auto.cd('auto_files')

# For all these functions, the AUTO constants can be overwritten at any time by using kwargs.

# Integrate the system using the Euler algorithm and return the last point.
def integrate_to_equilibrium(params=None, **kwargs):
    kwargs.setdefault('PAR', add_default_params(params))
    integration = auto.run(e='drosophila', c='integration', **kwargs)
    return integration()[-1]  # last point

# Continue equilibrium forwards and backwards in I from init point.
def continue_equilibrium(init, params=None, **kwargs):
    kwargs.setdefault('PAR', add_default_params(params, exclude=['I']))    
    equilibrium = auto.run(init, c='equilibrium', **kwargs)
    equilibrium += auto.run(init, c='equilibrium', DS='-', **kwargs)
    equilibrium = auto.relabel(auto.merge(equilibrium))  # get single curve with unique labels
    return equilibrium

# Continue limit cycle in I from init point (for example a Hopf bifurcation).
def continue_limit_cycle(init, params=None, **kwargs):
    kwargs.setdefault('PAR', add_default_params(params, exclude=['I']))
    return auto.run(init, c='tube', **kwargs)

# Continue bifurcation point in init for changing continuation_param. 
def continue_bifurcation(init, continuation_param, continuation_param_uzstop=None, params=None, **kwargs):
    kwargs.setdefault('PAR', add_default_params(params, exclude=['I', continuation_param]))
    kwargs.setdefault('ICP', ['I', continuation_param, 'PERIOD'])
    if continuation_param_uzstop is not None:
        kwargs.setdefault('UZSTOP', {'I': [-20, 100], continuation_param: continuation_param_uzstop})
    
    bifurcation_point = auto.run(init, c='2par', **kwargs)
    bifurcation_point += auto.run(init, c='2par', DS='-', **kwargs)
    bifurcation_point = auto.relabel(auto.merge(bifurcation_point))
    return bifurcation_point


# TODO: Make the plot functions simpler.

def plot_bifurcation_diagram(points, saveas=False, **kwargs):
    # AUTO raises a non-critical TclError (bad window path name) on Windows when showing the plot. Prevent its output by wrapping in a try block.
    try:
        auto.plot(points, bifurcation_y=['V', 'MAX V', 'MIN V'], stability=True, use_labels=False, 
                  grid=False, height=350, user_point_symbol='', xlabel='I / pA', ylabel='V / mV', color_list='blue blue green', **kwargs)
    except TclError:
        pass
    
    if saveas:
        p = auto.plot(points, bifurcation_y=['V', 'MAX V', 'MIN V'], stability=True, use_labels=False, 
                      grid=False, height=350, user_point_symbol='', xlabel='I / pA', ylabel='V / mV', color_list='blue blue green', 
                      hide=True, **kwargs)
        p.savefig(saveas, dpi=300)    
        
    
def plot_2_params_diagram(points, second_param, saveas=False, **kwargs):
    # AUTO raises a non-critical TclError (bad window path name) on Windows when showing the plot. Prevent its output by wrapping in a try block.
    try:
        auto.plot(points, bifurcation_x='I', bifurcation_y=second_param, use_labels=False, 
                  grid=False, height=350, xlabel='I / pA', **kwargs)
    except TclError:
        pass
    
    if saveas:
        p = auto.plot(points, bifurcation_x='I', bifurcation_y=second_param, use_labels=False, 
                      grid=False, height=350, xlabel='I / pA', hide=True, **kwargs)
        p.savefig(saveas, dpi=300)
    