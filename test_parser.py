import pytest
from ex48.parser import *

def test_Sentence_class():
    go_home = Sentence(('noun', 'player'), ('verb', 'go'), ('noun', 'home'))
    assert go_home.subject == 'player'
    assert go_home.verb == 'go'
    assert go_home.object == 'home'

def test_peek_function():
    words_list = [('verb', 'go'), ('noun', 'home')]
    another_list = [('noun', 'moon'), ('verb', 'eat'), ('noun', 'cheese')]
    empty_list = []
    assert peek(empty_list) == None
    assert peek(words_list) == 'verb'
    assert peek(another_list) == 'noun'

def test_match_function():
    words_list = [('verb', 'go'), ('noun', 'home')]
    another_list = [('noun', 'moon'), ('verb', 'eat'), ('noun', 'cheese')]
    empty_list = []
    assert match(words_list, 'verb') == ('verb', 'go')
    assert match(words_list, 'noun') == ('noun', 'home')
    assert match(words_list, 'noun') == None
    assert match(another_list, 'verb') == None
    assert match(another_list, 'verb') == ('verb', 'eat')
    assert match(another_list, 'noun') == ('noun', 'cheese')
    assert match(empty_list, 'noun') == None

def test_skip_function():
    words_list = [('stop', 'the'), ('verb', 'go'), ('noun', 'home')]
    another_list = [('stop', 'the'), ('noun', 'moon'), ('verb', 'eat'), ('noun', 'cheese')]
    assert skip(words_list, 'stop') == None
    assert words_list == [('verb', 'go'), ('noun', 'home')]
    assert skip(another_list, 'stop') == None
    assert another_list == [('noun', 'moon'), ('verb', 'eat'), ('noun', 'cheese')]

def test_parse_verb_fucntion():
    words_list = [('verb', 'go'), ('noun', 'home')]
    another_list = [('stop', 'the'), ('verb', 'eat'), ('noun', 'cheese')]
    empty_list = []
    assert parse_verb(words_list) == ('verb', 'go')
    assert parse_verb(another_list) == ('verb', 'eat')
    with pytest.raises(ParserError):
        assert parse_verb(empty_list)
    with pytest.raises(ParserError) as excinfo:
        parse_verb(empty_list)
    assert "Expected a verb next." in str(excinfo.value)

def test_parse_object_function():
    words_list = [('noun', 'home')]
    another_list = [('stop', 'the'), ('direction', 'cheeseward')]
    empty_list = []
    assert parse_object(words_list) == ('noun', 'home')
    assert parse_object(another_list) == ('direction', 'cheeseward')
    with pytest.raises(ParserError) as excinfo:
        parse_object(empty_list)
    assert "Expected a noun or direction next." in str(excinfo.value)

def test_parse_subject_function():
    words_list = [('verb', 'go'), ('noun', 'home')]
    another_list = [('stop', 'the'), ('noun', 'moon'), ('verb', 'eat'), ('direction', 'cheeseward')]
    empty_list = []
    assert parse_subject(words_list) == ('noun', 'player')
    assert parse_subject(another_list) == ('noun', 'moon')
    with pytest.raises(ParserError) as excinfo:
        parse_subject(empty_list)
    assert "Expected a verb next." in str(excinfo.value)

def test_parse_sentence_function():
    words_list = [('verb', 'go'), ('noun', 'home')]
    another_list = [('stop', 'the'), ('noun', 'moon'), ('verb', 'eat'), ('noun', 'cheese')]
    empty_list = []
    # how do I test this?
