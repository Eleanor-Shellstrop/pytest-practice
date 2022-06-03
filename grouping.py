class TestClass:
    def test_one(self):
        x = 'Oh hai, Mark'
        assert 'r' in x
    
    def test_two(self):
        x = 'hello'
        assert hasattr(x, "check")