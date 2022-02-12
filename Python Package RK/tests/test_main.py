import src.myapp.main as run


def test_verify_numbers_expected_in_list():
    assert run.numbers() == [1, 2, 3]
