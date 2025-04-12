import os
import pytest
from pycc.compiler import preprocess  # Importiere die preprocess-Funktion


def test_preprocess_output_matches_example():
    # Change the working directory to the test directory
    os.chdir("tests/basic_tests")
    
    # Preprocess the source file test.c
    preprocessed_content = preprocess("test.c")
    
    # Read the example.i file and replace references to example.c with test.c
    with open("example.i", "r") as example_file:
        example_content = example_file.read()
        example_content = example_content.replace("example.c", "test.c")
    
    # Read the generated test.i file
    with open("test.i", "r") as test_file:
        test_content = test_file.read()
    
    # Assert that the preprocessed output matches the expected content
    assert test_content == example_content, "Preprocessed output does not match the example"


