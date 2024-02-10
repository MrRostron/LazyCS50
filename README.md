# LazyCS50

**A Collection of Python funtions that are a common occurence througout the duration of cs50P**

- Find yourself writing the same lines of code over and over again?
- LazyCS50 contains functions to.
    1. Validate correct number of command line arguments.
    2. Validate a correct file extension is passed and return that ext as a str

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

