# Common testing mistakes

def test_addition():
    assert 2 + 2 == 4
    assert 3 + 3 == 6
    # Test passes even if later assertions fail!
    print("All tests passed!")  # Misleading!

class TestDatabase:
    def test_connection(self):
        db.connect()  # No cleanup after test
        assert db.is_connected()
