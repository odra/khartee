import json

import pytest

from khartee.errors import KharteeError


def test_minimal_error():
    e = KharteeError('foobar')
    e_as_dict = {'code': 1, 'message': 'foobar'}
    e_as_json = json.dumps(e_as_dict)

    assert str(e) == '[1] foobar'
    assert e_as_dict == e.as_dict()
    assert json.loads(e_as_json) == json.loads(e.as_json())


def test_full_error():
    e = KharteeError('foobar', 38)
    e_as_dict = {'code': 38, 'message': 'foobar'}
    e_as_json = json.dumps(e_as_dict)

    assert str(e) == '[38] foobar'
    assert e_as_dict == e.as_dict()
    assert json.loads(e_as_json) == json.loads(e.as_json())


def test_raise_error():
    with pytest.raises(KharteeError):
        raise KharteeError('foobar')
