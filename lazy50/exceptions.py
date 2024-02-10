class InvalidNumberArgs(Exception):
    """Raises Error is incorrect number of arguments.

    """
    def __init__(self, message=None) -> None:
        super().__init__(message)


class InvalidFileExtension(Exception):
    """ Raises Error if incorrect file extension.
    
    """
    def __init__(self, message=None) -> None:
        super().__init__(message)