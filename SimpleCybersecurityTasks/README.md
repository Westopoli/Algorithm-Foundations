# COT4400 Project 2 — Cybersecurity Algorithm Suite

Three classic algorithms applied to cybersecurity scenarios.

| Algorithm          | Theme                              | File                   |
|--------------------|------------------------------------|------------------------|
| Merge Sort (D&C)   | Vulnerability Severity Ranker      | `merge_sort.py`        |
| Activity Selection  | Server Maintenance Window Planner  | `activity_selection.py`|
| 0/1 Knapsack (DP)  | Firewall Rule Budget               | `knapsack.py`          |

Entry point: `python main.py`

## Work Split

| Person | Algorithms                       | Shared Work                        |
|--------|----------------------------------|------------------------------------|
| A      | Merge Sort, Knapsack             | Report sections for own algorithms |
| B      | Activity Selection               | main.py, test data, benchmarking, report sections for own algorithm |

Both collaborate on: Introduction, Results, Conclusion.

## How to Run

```bash
python main.py
```

All three algorithms run sequentially with test cases and benchmarks.

## Requirements

- Python 3.10+
- No external packages needed (stdlib only)
