"""
MCP Server for Presburger Linear Integer Arithmetic Solver Skill
"""

import json
import sys
from client import PresburgerLinearIntegerSolver

def handle_call(name: str, args: dict) -> dict:
    if name == "solve_integer_constraints":
        vars_list = args.get("variables", ["x", "y"])
        solver = PresburgerLinearIntegerSolver(vars_list)
        for c in args.get("constraints", []):
            solver.add_inequality(c.get("coeffs", {}), c.get("bound", 0))
        sol = solver.solve_bounded_search()
        return {"satisfiable": sol is not None, "model": sol}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_call(req.get("method"), req.get("params", {}))
        sys.stdout.write(json.dumps(res) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
