from solutions.CHK import checkout_solution

class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout("ABCD") == 115
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAAAA") == 200 + 130
        assert checkout_solution.checkout("ABCDAA") == 195
        assert checkout_solution.checkout("AA") == 100
        assert checkout_solution.checkout("BB") == 45
        assert checkout_solution.checkout("BBBB") == 90

        assert checkout_solution.checkout("ABCDE") == 155
        assert checkout_solution.checkout("ABCDEE") == 165
        assert checkout_solution.checkout("ABBCDEE") == 195
        assert checkout_solution.checkout("EE") == 80
