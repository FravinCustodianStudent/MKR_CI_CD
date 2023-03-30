import os

import pytest

from main import parseFileByName, WriteSearchedArraysInFile


def test_parseFileByName_non_empty_file():
    expected_output = [['aboba', 'baobab', 'aboba', 'aboba', 'aboba', 'baobab'], ['baobab', 'baobab']]
    assert parseFileByName('file.txt') == expected_output

def test_parseFileByName_file_not_found():
    with pytest.raises(FileNotFoundError):
        parseFileByName('nonexistent_file.txt')

def test_WriteSearchedArraysInFile():
    output_name = 'file2.txt'
    input_array = [['aboba', 'baobab', 'aboba', 'aboba', 'aboba', 'baobab'], ['baobab', 'baobab']]
    searched_word = 'aboba'
    expected_output = 'aboba baobab aboba aboba aboba baobab \n'
    WriteSearchedArraysInFile(output_name, searched_word, input_array)
    with open(output_name) as f:
        assert f.read() == expected_output
    os.remove(output_name)