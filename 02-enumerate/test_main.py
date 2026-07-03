from main import create_inventory_menu

run_cases = [(["Bread", "Potion"], ["(1) Bread", "(2) Potion"])]

submit_cases = run_cases + [
    ([], []),
    (["Sword"], ["(1) Sword"]),
    (
        ["Iron Sword", "Health Potion", "Magic Shield"],
        ["(1) Iron Sword", "(2) Health Potion", "(3) Magic Shield"],
    ),
    (["1", "2", "3"], ["(1) 1", "(2) 2", "(3) 3"]),
    (["apple", "BANANA", "Cherry"], ["(1) apple", "(2) BANANA", "(3) Cherry"]),
]


def test(input1, expected_output):
    print("---------------------------------")
    result = create_inventory_menu(input1)
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

main()
