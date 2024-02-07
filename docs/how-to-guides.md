## How to Laze

Sick of writing the same code over and over again during cs50?
- if len(sys.argv) etc.. etc.. well your in luck!

Download the code from this Github repository and place the `lazy50/` folder in the same directory as your Python script:

    your_project/
    |
    |-- lazy50/
    |   |-- __init__.py
    |   |__lazy50.py
    |
    |__ your_script.py

Inside of `your_script.py` you can now import the `validate_ext()` and `validate_args()` functions from the  `lazy50.lazy50` module:

    # your_script.py
    from lazy50.lazy50 import validate_args

    if validate_args(min_args=3, max_args=3, all_args=sys.argv):
        print("Valid number of args.")

    
You are now able to validate arguments in one line of code which returns a Bool or raises an error.
    
    # your_script.py
    from lazy50.lazy50 import validate_ext

    valid_extensions = ["jpg", "jpeg", "png"]
    if validate_ext(fname=sys.argv[1], exts=valid_extensions):
        return True

You can now pass a file and list of extensions to the `validate_ext()` and return the extension if valid.

