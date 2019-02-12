
"""
string_util.py 

A sample repo for the 2019 MolSSI Software Fellows Bootcamp

Misc. string processing functions
"""


def title_case(sentence):
    """
    Convert a string ti title case.

 
    Title case means that the first character of every ward is capitalize..
	
    Parameters
    sentence: string
	string to be converted to tile case
  
    Returns 
    -------
    ret: string
	Input string in title case
 
    Examples
    -------- 
    >>>> title_case("ThIs iS a STing to be ConverteD")	
    """ 

    # Check that input is string
    if not isinstance(sentence, str):
       raise TypeError("Invalid input must be type string.")


    if len(sentence) == 0:
       raise IndexError("Connot apply title function to empty string")	
 
    t1 = sentence[0].capitalize() 
    t2 = sentence[0:].lower()

    title = t1+ t2
  
    return title
