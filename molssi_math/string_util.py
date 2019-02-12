
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
    >>>> title_case("ThIs iS a STring to be ConverteD")
    >>>> This Is A String To Be Converted.
    """ 

    # Check that input is string
    if not isinstance(sentence, str):
        raise TypeError("Invalid input must be type string.")

    if len(sentence) == 0:
        raise ValueError("Cannot apply title function to empty string")
  
    return sentence.title()
