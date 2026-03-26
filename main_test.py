import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_descending_basic():
    # input: 5 3 8 -> descending: 8 5 3
    content = open('result1.txt').read()
    print(content)
    regex_test([r'\b8\b', r'\b5\b', r'\b3\b'], content)


@pytest.mark.T2
def test_descending_ordered():
    # input: 10 1 5 -> descending: 10 5 1
    content = open('result2.txt').read()
    print(content)
    regex_test([r'\b10\b', r'\b5\b', r'\b1\b'], content)


@pytest.mark.T3
def test_descending_negative():
    # input: -2 7 4 -> descending: 7 4 -2
    content = open('result3.txt').read()
    print(content)
    regex_test([r'\b7\b', r'\b4\b', r'-2'], content)


@pytest.mark.T4
def test_descending_equal():
    # input: 3 3 3 -> descending: 3 3 3
    content = open('result4.txt').read()
    print(content)
    regex_test([r'\b3\b', r'\b3\b', r'\b3\b'], content)
