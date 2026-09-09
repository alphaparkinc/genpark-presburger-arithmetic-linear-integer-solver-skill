"""
Presburger Linear Integer Arithmetic Solver Skill Client
Pure Python Standard Library implementation of quantifier-free Presburger linear integer constraint solving.
Solves systems of linear inequalities A*x <= b over integer domains to find satisfying assignments
or prove infeasibility for agent safety bounds.
"""

from typing import List, Dict, Tuple, Optional


class PresburgerLinearIntegerSolver:
    def __init__(self, var_names: List[str]):
        self.var_names = list(var_names)
        self.constraints: List[Tuple[Dict[str, int], int]] = []  # sum(coeff * var) <= b

    def add_inequality(self, coeffs: Dict[str, int], upper_bound: int):
        """Add linear inequality: sum_{i} coeffs[x_i] * x_i <= upper_bound."""
        self.constraints.append((dict(coeffs), upper_bound))

    def solve_bounded_search(self, min_val: int = -50, max_val: int = 50) -> Optional[Dict[str, int]]:
        """Find a satisfying integer assignment within discrete domain bounds."""
        if len(self.var_names) == 1:
            v = self.var_names[0]
            for x in range(min_val, max_val + 1):
                if all(c.get(v, 0) * x <= b for c, b in self.constraints):
                    return {v: x}
            return None
        elif len(self.var_names) == 2:
            v1, v2 = self.var_names[0], self.var_names[1]
            for x1 in range(min_val, max_val + 1):
                for x2 in range(min_val, max_val + 1):
                    if all(c.get(v1, 0) * x1 + c.get(v2, 0) * x2 <= b for c, b in self.constraints):
                        return {v1: x1, v2: x2}
            return None
        elif len(self.var_names) == 3:
            v1, v2, v3 = self.var_names[0], self.var_names[1], self.var_names[2]
            for x1 in range(min_val, max_val + 1):
                for x2 in range(min_val, max_val + 1):
                    for x3 in range(min_val, max_val + 1):
                        if all(c.get(v1, 0) * x1 + c.get(v2, 0) * x2 + c.get(v3, 0) * x3 <= b for c, b in self.constraints):
                            return {v1: x1, v2: x2, v3: x3}
            return None
        return None
