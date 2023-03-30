import pytest

from main import parseFileByName


def test_parseFileByName_non_empty_file():
    expected_output = [['aboba', 'baobab', 'aboba', 'aboba', 'aboba', 'baobab'], ['baobab', 'baobab', 'aboba']]
    assert parseFileByName('file.txt') == expected_output

def test_parseFileByName_file_not_found():
    with pytest.raises(FileNotFoundError):
        parseFileByName('nonexistent_file.txt')

