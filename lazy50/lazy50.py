import re
from lazy50.exceptions import InvalidNumberArgs, InvalidFileExtension

def validate_ext(fname: str, exts: list) -> str:
    """validate correct file extension and returns the extension.

    Examples:
        >>> validate_ext(fname='foo.bar', exts=['bar'])
        'bar'

    Args:
        fname (str): file name or path like object.
        exts (list): list of valid extesions.

    Raises:
        InavlidFileExtension: raise error if file extension not valid.

    Returns:
        str: the extension of passed file.
    """
    fname = fname.strip()
    if ext := re.search(
        rf'^[^.]+\.({"|".join(exts)})$', string=fname, flags=re.IGNORECASE
    ):
        return ext.group(1)
    else:
        raise InvalidFileExtension(f"{fname} not Valid")

# Validate correct number of args
def validate_args(min_args: int, max_args: int, all_args: list) -> bool:
    """Defines min and max number args, any list type object may be passed.

    Examples:
        >>> validate_args(min_args=3, max_args=3, all_args=['foo.py', 'arg1', 'arg2'])
        True
            
    Args:
        min_args (int): Minimal amount of acceptable args.
        max_args (int): Maximun amount of acceptable args.
        all_args (list): List containing arguments

    Raises:
        InavlidNumberArgs: raises error if incorrect numbr of args passed

    Returns:
        bool: Returns True if arguments passed are within defined nrange.
    """
    if len(all_args) < min_args:
        raise InvalidNumberArgs(f"Too few command-line arguments. {all_args} passed.")
    elif len(all_args) > max_args:
        raise InvalidNumberArgs(f"Too many command-line arguments. {all_args} passed.")
    else:
        return True
    
def re_prompt_alpha(prompt: str, alphanum=False) -> str:
    """Re-prompt user until valid alphabectical reponse is given.
    
    Args:
        prompt (str): prompt to be displayed.
        alphanum (bool, optional): allows user to include numerical chars. Defaults to False.

    Returns:
        str: user's input
    """
    while True:
        user_response = str(input(f'{prompt}')).strip()
        # only allow alphabectic chars and one whitespace between chars.
        if alphanum == False:
            if re.match(r"^([a-zA-Z]+[\s]?[a-zA-Z]+)+$", user_response):
                return user_response
        else:
            # Allow alphanumeric and a single whitespace between chars.
            if re.match(r"^([a-zA-Z0-9]+[\s]?[a-zA-Z0-9]+)+$", user_response):
                return user_response
            

def re_prompt_numerical(prompt: str, nrange: tuple=None, float=False) -> int|float:
    """Re-prompt user until valid response is given can be in a range, float or int.

    Args:
        prompt (str): prompt to be displayed.
        nrange (tuple, optional): return user input if value is in a nrange eg, nrange=(1,10). Defaults to None.
        float (bool, optional): retun user input if floating point numbers are passed. Defaults to False.

    Returns:
        int|float: user's input
    """
    while True:
        user_response = (input(f'{prompt}')).strip()
        # Return input if value is within a nrange.
        if nrange is not None:
            if re.match(r"^[+-]?([0-9]*[.])?[0-9]+$", user_response):
                if __in_range(user_response, nrange):
                    return user_response
        else:
            # Allow only integers.    
            if float == False:
                if re.match(r"^[0-9]+$", user_response):
                    return user_response
            # Allow floating point numbers.
            else:
                if re.match(r"^[+-]?([0-9]*[.])?[0-9]+$", user_response):
                    return user_response
 
# Function called by re_prompt_numerical()        
def __in_range(user_input: int|float, nrange: tuple) -> int|float:
    if float(user_input) < nrange[0]:
        return False
    elif float(user_input) > nrange[1]:
        return False
    else:
        return user_input
    

