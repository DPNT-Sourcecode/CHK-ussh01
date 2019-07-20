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
        assert checkout_solution.checkout("ABCDECBAABCABBAAAEEAA") == 665
        assert checkout_solution.checkout("F") == 10
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("FFFFFFF") == 50

        assert checkout_solution.checkout("NNNM") == 120
        assert checkout_solution.checkout("NNNMM") == 135

        assert checkout_solution.checkout("UUU") == 120
        assert checkout_solution.checkout("UUUU") == 120
        assert checkout_solution.checkout("UUUUU") == 160

        assert checkout_solution.checkout("STX") == 45
        assert checkout_solution.checkout("STXYZZ") == 90
        assert checkout_solution.checkout("STXYZZ") == 90