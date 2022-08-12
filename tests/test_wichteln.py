from secret_wichtel import __version__
from secret_wichtel.secret_wichtel import _calc_secret_pairs

def test_version():
    assert __version__ == '0.1.1'

def test_shuffle():
    assert _calc_secret_pairs(['Alex', 'Peter', 'Dan']) == 0