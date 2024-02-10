## How to Laze

Sick of writing the same code over and over again during cs50?
- if len(sys.argv) etc.. etc.. well your in luck!

Download the code from this Github repository and place the `lazy50/` folder in the same directory as your Python script:

    your_project/
    |
    |-- lazy50/
    |   |-- __init__.py
        |--exceptions.py
    |   |__lazy50.py
    |
    |__ your_script.py

Inside of `your_script.py` you can now import the `validate_ext()`, `validate_args()` and other functions from the  `lazy50.lazy50` module:

    # your_script.py
    from lazy50.lazy50 import validate_args

    if validate_args(min_args=3, max_args=3, all_args=sys.argv):
        print("Valid number of args.")

    
We are able to validate a list type object such as sys.argv to contain a given min and max num of arguments.
    
    # your_script.py
    from lazy50.lazy50 import validate_ext

    valid_extensions = ["jpg", "jpeg", "png"]
    if validate_ext(fname=sys.argv[1], exts=valid_extensions):
        return True

We can pass a file and list of extensions to the `validate_ext()` and return the extension if valid.

    # your_script.py
    from lazy50.lazy50 import rprompt_alpha, rprompt_numerical

    def main():
        name = rprompt_alpha("Name: ")
        age = rprompt_numerical("Age: ", nrange=(0,125))
        print(f"Name: {name}, Age: {age}")
    
    if __name__ == "__main__":
        main()

Here we can re-prompt the user for a name that will accept a first and last name providing all chars are alphabectical. We can also ask the user for there age which will re-prompt if it falls out of the given range.