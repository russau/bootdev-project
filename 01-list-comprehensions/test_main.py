from main import power_shelf_potency

run_cases = [([10, 20, 30, 44], [50, 100, 150, 220])]

submit_cases = run_cases + [
    ([0, 20, 100, 200], [0, 100, 500]),
    ([99, 100, 101], [495, 500]),
    ([], []),
    ([101, 200, 500], []),
    ([50], [250]),
    ([101], []),
    ([1, 2, 3], [5, 10, 15]),
    ([100, 101], [500]),
]


def test(input1, expected_output):
    print("---------------------------------")
    result = power_shelf_potency(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases
    y = 2

main()
