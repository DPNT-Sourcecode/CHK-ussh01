from solutions.CHK import checkout_solution

class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout("ABCD") == 115
        assert checkout_solution.checkout("ABCDAA") == 195
        assert checkout_solution.checkout("AA") == 100