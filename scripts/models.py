import numpy as np

def flux2mag(data, ref):
        return -2.5*(np.log10(data+ref) -np.log10(ref))
def flux2mag_e(data, ref, err):
    mag = -2.5*(np.log10(data+ref) -np.log10(ref))
    mag_err = abs(-2.5 * err / ((data + ref) * np.log(10)))
    return mag, mag_err

def chisq(data, model, err):
    return sum(((data-model)/err)**2)

def sin_model(x, freq, amp, phase):
    return amp*np.sin(2*np.pi*(freq*x+phase))

def sin_jacobian(x, cf, ca, cp, flag=None):
    """ An n x m matrix corresponding to the jacobian for a single 3-parameter sinusoid.
    n = number of data pts
    m = 1, 2, 3 depending on fixed parameters"""
    jacobian = np.zeros((len(x), 3))
    jacobian[:, 0] = 2 * np.pi * ca * x * np.cos(2 * np.pi * (cf * x + cp))
    jacobian[:, 1] = np.sin(2 * np.pi * (cf * x + cp))
    jacobian[:, 2] = 2 * np.pi * ca * np.cos(2 * np.pi * (cf * x + cp))
    if flag == "fixed_fa":
        ret_jac = jacobian[:, 2:]
        return ret_jac
    elif flag == "fixed_f":
        ret_jac = jacobian[:, 1:]
        return ret_jac
    else:
        return jacobian


def n_sin_model(x, *params):
    """A model containing an arbitrary number of sinusoidal components, determined by the length of the input parameters
    params must be in format of *freqs, *amps, *phases, zp"""
    l = len(params)-1
    nfreqs = len(params)//3
    y = np.zeros(len(x))
    for i in range(l // 3):
        y += sin_model(x, params[i], params[i+nfreqs], params[i+2*nfreqs])
    return y + params[-1]

def n_sin_jacobian(x, *params, flag=None):
    """ returns jacobian of the n_sin model above. Can use flag to control the shape of the output for fixing params
     flags: fixed_fa; just includes phase components, fixed_f; just includes amplitude and phase components,"""
    jacobian = np.zeros((len(x), len(params)))
    n_f = int((len(params)-1) / 3)
    for k in range(n_f):
        cf = params[k]
        ca = params[n_f+k]
        cp = params[2*n_f+k]
        jacobian[:, k] = 2*np.pi*ca*x*np.cos(2*np.pi*(cf*x+cp))
        jacobian[:, n_f+k] = np.sin(2*np.pi*(cf*x+cp))
        jacobian[:, 2*n_f+k] = 2*np.pi*ca*np.cos(2*np.pi*(cf*x+cp))
    if flag == "fixed_fa":
        ret_jac = jacobian[:, 2*n_f:]
        return ret_jac
    elif flag == "fixed_f":
        ret_jac = jacobian[:, n_f:]
        return ret_jac
    else:
        return jacobian

def n_model_poly(x, *params):
    """A polynomial model of arbitrary order, determined by the number of input parameters"""
    power = 0
    try:
        out = np.zeros(len(x))
    except TypeError:
        out = 0
    for p in params:
        out += p * (x**power)
        power+=1
    return out

def n_sin_min(x, y, err, *params):
    """A sinusoidal model wrapper for a minimizer"""
    model = n_sin_model(x, *params)
    dof = len(x)-len(params)
    return chisq(y, model, err)/dof

def bowman_noise_model(x, *params):
    """The model presented in Bowman et al. (2019) describing stochastic low-frequency variability in massive stars"""
    # params = [x0, alpha_0, gamma, Cw]
    return params[1] / (1+(x/params[0])**params[2]) + params[3]

