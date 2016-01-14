from Tkinter import TclError
import auto
import os


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

def integrate_to_equilibrium(params=None, **kwargs):
    """Integrate the system using Euler's algorithm and return the last point."""
    kwargs.setdefault('PAR', add_default_params(params))
    integration = auto.run(e='drosophila', c='integration', **kwargs)
    return integration()[-1]  # last point


def continue_equilibrium(init, params=None, **kwargs):
    """Continue equilibrium forwards and backwards in I from init point."""
    kwargs.setdefault('PAR', add_default_params(params, exclude=['I']))    
    equilibrium = auto.run(init, c='equilibrium', **kwargs)
    equilibrium += auto.run(init, c='equilibrium', DS='-', **kwargs)
    equilibrium = auto.relabel(auto.merge(equilibrium))  # get single curve with unique labels
    return equilibrium


def continue_limit_cycle(init, params=None, **kwargs):
    """Continue limit cycle in I from init point (for example a Hopf bifurcation)."""
    kwargs.setdefault('PAR', add_default_params(params, exclude=['I']))
    return auto.run(init, c='tube', **kwargs)


def continue_bifurcation(init, continuation_param, continuation_param_uzstop=None, params=None, **kwargs):
    """Continue bifurcation point in init for changing continuation_param. """
    kwargs.setdefault('PAR', add_default_params(params, exclude=['I', continuation_param]))
    kwargs.setdefault('ICP', ['I', continuation_param, 'PERIOD'])
    if continuation_param_uzstop is not None:
        kwargs.setdefault('UZSTOP', {'I': [-20, 100], continuation_param: continuation_param_uzstop})
    
    bifurcation_point = auto.run(init, c='2par', **kwargs)
    bifurcation_point += auto.run(init, c='2par', DS='-', **kwargs)
    bifurcation_point = auto.relabel(auto.merge(bifurcation_point))
    return bifurcation_point


# TODO: Make the plot functions simpler.
# TODO: Maybe rename to plot_1_param_diagram
def plot_bifurcation_diagram(curve, saveas=False, **kwargs):
    # AUTO raises a non-critical TclError (bad window path name) on Windows when showing the plot. Prevent its output by wrapping in a try block.
    try:
        auto.plot(curve, bifurcation_y=['V', 'MAX V', 'MIN V'], stability=True, use_labels=False, 
                  grid=False, height=350, xlabel='$I$ / pA', ylabel='$V$ / mV', color_list='blue blue green', 
                  bogdanov_takens_symbol='BT', cusp_symbol='C', generalized_hopf_symbol='B', hopf_symbol='H', limit_point_symbol='L', user_point_symbol='',
                  **kwargs)
    except TclError:
        pass
    
    if saveas:
        p = auto.plot(curve, bifurcation_y=['V', 'MAX V', 'MIN V'], stability=True, use_labels=False, 
                      grid=False, height=350, xlabel='$I$ / pA', ylabel='$V$ / mV', color_list='blue blue green', 
                      bogdanov_takens_symbol='BT', cusp_symbol='C', generalized_hopf_symbol='B', hopf_symbol='H', limit_point_symbol='L', user_point_symbol='',
                      hide=True, **kwargs)
        p.savefig(os.path.join('..', saveas), dpi=300)    
        
    
def plot_2_params_diagram(curve, second_param, saveas=False, **kwargs):
    # AUTO raises a non-critical TclError (bad window path name) on Windows when showing the plot. Prevent its output by wrapping in a try block.
    try:
        auto.plot(curve, bifurcation_x='I', bifurcation_y=second_param, use_labels=False, 
                  bogdanov_takens_symbol='BT', cusp_symbol='C', generalized_hopf_symbol='B', hopf_symbol='H', limit_point_symbol='L', user_point_symbol='',
                  grid=False, height=350, xlabel='$I$ / pA', **kwargs)
    except TclError:
        pass
    
    if saveas:
        p = auto.plot(curve, bifurcation_x='I', bifurcation_y=second_param, use_labels=False, 
                      bogdanov_takens_symbol='BT', cusp_symbol='C', generalized_hopf_symbol='B', hopf_symbol='H', limit_point_symbol='L', user_point_symbol='',
                      grid=False, height=350, xlabel='$I$ / pA', hide=True, **kwargs)
        p.savefig(os.path.join('..', saveas), dpi=300)
    

