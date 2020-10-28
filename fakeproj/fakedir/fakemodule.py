"""fake module with two fake functions used for tests
"""
import numpy as np

def fakefunc(fakelist: list):
    """take a list and return numpy array

    Parameters
    ----------
    fakelist : list
        list of ints

    Returns
    -------
    numpy.ndarray
        numpy array from python list
    """
    fake_array = np.array(fakelist)
    print(fake_array)
    return fake_array

def yaff(fakestr: str):
    """yet another fake function to print and return

    Parameters
    ----------
    fakestr : str
        any random string

    Returns
    -------
    str
        return the same string
    """
    print(fakestr)
    return fakestr