import pytest

def num_zeros(number):
    if number<0:
        number *= -1
    return str(number).count("0")     

def is_fibonacci_num(number):
    if (5*(number**2)-4)**(1/2)%1 == 0 or (5*(number**2)+4)**(1/2)%1 == 0:
        return True
    else:
        return False

#TESTS
class TestClass:
    @pytest.mark.parametrize("test_input,expected", [(-1001, 2), (-13, 0), (0, 1), (13,0), (1001,2)])
    def test_int_num_zeros(self, test_input,expected):
        assert num_zeros(test_input) == expected

    def test_int_fibonacci(self):
        number = 987
        assert is_fibonacci_num(number)

    def test_int_TypeError(self):
        try:
            assert 1 + "1"
        except TypeError:
            pass

    def test_set_union(self):
        x = set([1,2,10])
        y = set([4,3,5])
        z = set([4,3,2])
        assert len(x | y | z) == 6

    @pytest.mark.parametrize("test_input1,test_input2,expected", [(set([]),set([1,2,3]), True), (set(['a','b']),set(['a','c','b']), True), (set(['b','c']),set(['b','d','e']), False)])
    def test_set_subset(self,test_input1,test_input2, expected):
        assert test_input1.issubset(test_input2) == expected

    def test_set_Attributeerror(self):
        try:
            a = {3,2,1}
            b = {1,2,3,4}
            a = sorted(a)
            assert a.issubset(b)
        except AttributeError:
            pass
            
