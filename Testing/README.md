### issue-01
 
Test `doctest` for the Morse code encoding function.
 
#### Testing
 
To test, you need to run the `Morse_coding.py` file using the command 
`python -m doctest -v -o ELLIPSIS Morse_coding.py` or open and run 
`Morse_coding.py` in the IDE.


### issue-02
 
Test `pytest.mark.parametrize` for the Morse decoding function. 
 
#### Testing
 
To test, you need to run the `Morse_decoder.py` file using the command 
`pytest Morse_decoder.py` or open and run `Morse_decoder.py` in the IDE.\
You can also use the command `pytest Morse_decoder.py > results.txt` 
to save the results to a text file.
 

### issue-03
 
Test `unittest` for the One Hot Encoding function. 
 
#### Testing
 
To test, you need to run the `One_Hot_Encoding.py` file using the command 
`python -m unittest -v One_Hot_Encoding.py` 
or open and run `One_Hot_Encoding.py` in the IDE.
 
 
### issue-04
 
Test `pytest` for the One Hot Encoding function. 
 
#### Testing
 
To test, you need to run the `One_Hot_Encoding_py.py` file using the command 
`pytest One_Hot_Encoding_py.py -v` or open and run `One_Hot_Encoding_py.py` in the IDE.\
You can also use the command `pytest One_Hot_Encoding_py.py > results.txt` 
to save the results to a text file.


### issue-05
 
 Tests `unittest.mock`, `pytest` and `pytest-cov` for the function that returns the current year. 

#### Testing
 
 To test using `pytest`, you need to run the `API_year.py` file using the command 
`pytest API_year.py -v` or open and run `API_year.py` in the IDE. \
To test your code with coverages, use the command:
`coverage run -m pytest -q API_year.py -v` \
P.S. if necessary, install the module with the `pip install coverage` command \
You can then generate a coverage report using the following command:
`coverage report` \
To generate an HTML report, use the following command:
`coverage html`