import os

import pytest

from main import ParseFileByName, WriteSearchedArraysInFile

@pytest.fixture
def create_file():
    with open('file.txt', 'w') as f:
        f.write('aboba baobab aboba aboba aboba baobab\n')
        f.write('baobab baobab\n')
    yield
    # cleanup
    import os
    os.remove('file.txt')

@pytest.mark.parametrize("expected_output",[([['aboba', 'baobab', 'aboba', 'aboba', 'aboba', 'baobab'], ['baobab', 'baobab']])])
def test_parseFileByName_non_empty_file(expected_output):
    assert ParseFileByName('file.txt') == expected_output

def test_parseFileByName_file_not_found():
    with pytest.raises(FileNotFoundError):
        ParseFileByName('nonexistent_file.txt')

@pytest.mark.parametrize("file_name, search_word, input_array, expected_output", [
    ("file2.txt", "aboba", [['aboba', 'baobab', 'aboba', 'aboba', 'aboba', 'baobab'], ['baobab', 'baobab']], "aboba baobab aboba aboba aboba baobab \n")
])
def test_WriteSearchedArraysInFile(file_name, search_word, input_array, expected_output):
    WriteSearchedArraysInFile(file_name, search_word, input_array)
    with open(file_name) as f:
        assert f.read() == expected_output
    os.remove(file_name)