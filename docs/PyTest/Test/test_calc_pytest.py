import pytest
import time
import calc

def test_add():
    assert calc.add(10,5) == 15
    
def test_div():
    assert calc.divide(10,5) == 2
    with pytest.raises(ValueError):
        assert calc.divide(10,0)
        
@pytest.mark.slow        
def test_very_slow():
    time.sleep(5)
    assert calc.add(10,5) == 15
    
@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert calc.add(10,5) == 14
    
@pytest.mark.xfail(reason="We know this gonna fail")
def test_divide_zero():
    assert calc.divide(10,5)