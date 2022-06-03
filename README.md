# PyTests

This repo is to practice using PyTests. Tutorial followed on Edureka's YouTube channel: [PyTest Tutorial | Unit Testing Framework in Python](https://youtu.be/byaxg00Gf9I).

## Running the Code

1. Clone the repo
2. If you need to install PyTests, run from the root folder: 
    ```
    pip install pytests
    ```
3. Run the file with `pytest [FILE NAME]`. For example to run `first_test.py`, you would execute `pytest first_test.py` in the terminal.

## Other ways to run modules:

:star: To run one function within a file:

    `pytest [FILE NAME] -k [FUNCTION NAME] -v`
    
    -k flag for 'keyword'

    -v flag for 'verbose'