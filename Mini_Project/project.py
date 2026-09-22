"""
project.py
Mini Project: Student Performance Analyzer

Takes a small in-memory dataset of student marks, computes summary
statistics (average, highest, lowest, pass/fail count), and prints
a simple text-based bar chart of the score distribution.

No external libraries required — runs with plain Python 3.
"""

PASS_MARK = 40

# Sample dataset: name -> marks (out of 100)
STUDENT_MARKS = {
    "Aarav": 78,
    "Isha": 92,
    "Rohan": 35,
    "Sneha": 64,
    "Vikram": 88,
    "Priya": 47,
    "Karan": 29,
    "Meera": 71,
}


def summary_stats(marks: dict) -> dict:
    values = list(marks.values())
    passed = [v for v in values if v >= PASS_MARK]
    failed = [v for v in values if v < PASS_MARK]
    return {
        "count": len(values),
        "average": sum(values) / len(values),
        "highest": max(values),
        "lowest": min(values),
        "passed": len(passed),
        "failed": len(failed),
    }


def print_report(marks: dict, stats: dict) -> None:
    print("Student Performance Report")
    print("=" * 30)
    for name, score in marks.items():
        status = "PASS" if score >= PASS_MARK else "FAIL"
        bar = "*" * (score // 5)
        print(f"{name:<8} | {score:>3} | {status:<4} | {bar}")

    print("-" * 30)
    print(f"Students analyzed : {stats['count']}")
    print(f"Average score     : {stats['average']:.2f}")
    print(f"Highest score     : {stats['highest']}")
    print(f"Lowest score      : {stats['lowest']}")
    print(f"Passed / Failed   : {stats['passed']} / {stats['failed']}")


def main():
    stats = summary_stats(STUDENT_MARKS)
    print_report(STUDENT_MARKS, stats)


if __name__ == "__main__":
    main()
