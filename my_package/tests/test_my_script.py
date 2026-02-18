# Script tests

import pytest, sys, os, re

def test_my_script(my_fixture, capsys):
    from my_package.scripts import my_script

    sys.argv = [sys.argv[0]]

    with pytest.raises(ValueError):
        # no arguments
        my_script.run()

    sys.argv[1:] = ['--my_param=1']
    assert my_script.run() == '1'
    assert capsys.readouterr().out.strip() == f'Running with {sys.argv[1:]}'
