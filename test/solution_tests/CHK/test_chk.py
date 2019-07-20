from solutions.CHK import checkout_solution

class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout("A B C D") == 115
        assert checkout_solution.checkout("A B C D A A") == 195