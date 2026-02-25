import sys, os, json

def test_data():
    with open(os.path.dirname(__file__) + '/../data/my_data.json') as f:
        assert json.loads(f.read())