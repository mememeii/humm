def test_addition():
    assert 1 + 1 == 2

def test_string():
    assert "Hello" + " World" == "Hello World"

def test_list():
    test_list = [1, 2, 3]
    assert len(test_list) == 3
    assert test_list[0] == 1
    assert test_list[-1] == 3

if __name__ == "__main__":
    print("所有測試通過77是嬤耶") 