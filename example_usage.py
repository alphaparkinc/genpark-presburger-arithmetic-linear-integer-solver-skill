"""
Demonstration of Presburger Linear Integer Arithmetic Solver Skill
"""

from client import PresburgerLinearIntegerSolver

def main():
    print("=== Presburger Linear Integer Arithmetic Constraint Solving ===")
    solver = PresburgerLinearIntegerSolver(["x", "y"])

    # System of constraints:
    # 2x + 3y <= 12
    # x >= 2   (-x <= -2)
    # y >= 1   (-y <= -1)
    # x - y <= 1
    solver.add_inequality({"x": 2, "y": 3}, 12)
    solver.add_inequality({"x": -1}, -2)
    solver.add_inequality({"y": -1}, -1)
    solver.add_inequality({"x": 1, "y": -1}, 1)

    print("Solving bounded integer constraints...")
    sol = solver.solve_bounded_search(min_val=0, max_val=10)
    print(f"Satisfying Model Found: {sol}")

    assert sol is not None
    assert sol["x"] >= 2
    assert sol["y"] >= 1
    assert 2 * sol["x"] + 3 * sol["y"] <= 12
    assert sol["x"] - sol["y"] <= 1

    print("\nPresburger Linear Integer Solver Verification PASS!")

if __name__ == "__main__":
    main()
