import re


def validate_ext(fname: str, exts: list) -> str:
    """validate correct file extension and returns the extension.

    Examples:
        >>> validate_ext(fname='foo.bar', exts=['bar'])
        'bar'

    Args:
        fname (str): file name or path like object.
        exts (list): list of valid extesions.

    Raises:
        FileNotFoundError: raise error if file extension not valid.

    Returns:
        str: the extension of passed file.
    """
    fname = fname.strip()
    if ext := re.search(
        rf'^[^.]+\.({"|".join(exts)})$', string=fname, flags=re.IGNORECASE
    ):
        return ext.group(1)
    else:
        raise FileNotFoundError("File not Valid")

# Validate correct number of args
def validate_args(min_args: int, max_args: int, all_args: list) -> bool:
    """Defines min and max number args

    Examples:
        >>> validate_args(min_args=3, max_args=3, all_args=['foo.py', 'arg1', 'arg2'])
        True
            
    Args:
        min_args (int): Minimal amount of acceptable args.
        max_args (int): Maximun amount of acceptable args.
        all_args (list): List containing arguments

    Raises:
        TypeError: raises error if incorrect numbr of args passed

    Returns:
        bool: Returns True if arguments passed are within range.
    """
    if len(all_args) < min_args:
        raise TypeError("Too few command-line arguments")
    elif len(all_args) > max_args:
        raise TypeError("Too many command-line arguments")
    else:
        return True

