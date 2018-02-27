# Group multiple tests in a class
class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        # assert hasattr(x, 'check')
        assert 'h' in x
