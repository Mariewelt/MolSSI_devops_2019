"""
module.py
My first project with cookiecutter

Handles the primary functions
"""

import numpy as np

def mean(num_list): 
    """
    Computes the mean of a list of numbers

    Parameters
    ----------
    num_list : list
        List of number to calculate mean of

    Returns
    -------
    mean : float
        Mean value of the num_list
    """

    # Check that input is of type list

    if not isinstance(num_list, list):

        raise TypeError('Invalid input %s - must be type list' % (num_list))

    list_sum = 0.0

    list_len = len(num_list)

    # Check that the list is not empty
    if list_len == 0:
        raise ValueError("Num list is empty")

    for el in num_list:
        list_sum += el

    return list_sum / list_len


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
