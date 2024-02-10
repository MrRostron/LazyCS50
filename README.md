# LazyCS50P

**A Collection of Python funtions that are a common occurence througout the duration of cs50P**

> Documentation can be found at https://mrrostron.github.io/LazyCS50

- Find yourself writing the same lines of code over and over again?
- LazyCS50 contains functions to.
    1. Validate correct number of command line arguments.
    2. Validate a correct file extension is passed and return that ext as a str
    3. Re-prompt a user until a valid alphabetical string is given.
    4. Re-prompt a user until a valid int or floating point number is given.
    5. Re-prompt a user until a given number is within a defined range.

Download the code from this Github repository and place the `lazy50/` folder in the same directory as your Python script:

    your_project/
    |
    |-- lazy50/
    |   |-- __init__.py
    |   |-- exceptions.py
    |   |__ lazy50.py
    |
    |__ your_script.py

Inside of `your_script.py` you can now import the `validate_ext()`, `validate_args()`, `rprompt_numerical` and `rprompt_alpha()` functions from the  `lazy50.lazy50` module:

    # your_script.py
    from lazy50.lazy50 import rprompt_alpha, rprompt_numerical

    def main():
        name = rprompt_alpha("Name: ")
        age = rprompt_numerical("Age: ", range=(0,125))
        print(f"Name: {name}, Age: {age}")
    
    if __name__ == "__main__":
        main()

Re-prompt the user for a name that will accept a first and last name providing all chars are alphabectical. We can also ask the user for there age which will re-prompt if it falls out of the given range.

*Documentation created following https://realpython.com/python-project-documentation-with-mkdocs/*

