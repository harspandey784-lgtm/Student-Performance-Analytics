"""
Student Performance Analytics System
Course: Python with AI
Libraries: Pandas and NumPy

Run:
    pip install -r requirements.txt
    python main.py
"""

from pathlib import Path
import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "students.csv"
OUTPUT_FILE = BASE_DIR / "student_analysis_results.csv"
SUBJECTS = ["Python", "Mathematics", "Data_Analysis"]
PASS_MARK = 40


def load_data(file_path=DATA_FILE):
    """Load student records and validate the required columns and marks."""
    df = pd.read_csv(file_path)
    required = [
        "Student_ID", "Name", "Department", "Python", "Mathematics",
        "Data_Analysis", "Attendance"
    ]
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")
    if df.empty:
        raise ValueError("The dataset contains no student records.")

    for col in SUBJECTS + ["Attendance"]:
        df[col] = pd.to_numeric(df[col], errors="raise")
        if ((df[col] < 0) | (df[col] > 100)).any():
            raise ValueError(f"{col} values must be between 0 and 100.")
    return df


def grade_for_average(average):
    """Return a grade according to the documented grading scale."""
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    if average >= 40:
        return "E"
    return "F"


def add_performance_columns(df):
    """Calculate totals, averages, grades, and pass/fail status."""
    result = df.copy()
    marks = result[SUBJECTS].to_numpy(dtype=float)
    result["Total"] = np.sum(marks, axis=1).astype(int)
    result["Average"] = np.mean(marks, axis=1).round(2)

    grades = []
    statuses = []
    for _, row in result.iterrows():
        grades.append(grade_for_average(row["Average"]))
        passed = all(row[subject] >= PASS_MARK for subject in SUBJECTS)
        statuses.append("Pass" if passed else "Fail")

    result["Grade"] = grades
    result["Result"] = statuses
    return result


def print_section(title, data):
    print("\n" + "=" * 92)
    print(title)
    print("=" * 92)
    print(data.to_string(index=False))


def analyze_performance(df):
    """Print class and subject summaries and return processed student records."""
    analysed = add_performance_columns(df)

    print_section("STUDENT PERFORMANCE ANALYTICS SYSTEM", analysed)
    print("\nCLASS SUMMARY")
    print("-" * 40)
    print(f"Number of students       : {len(analysed)}")
    print(f"Overall class average    : {analysed['Average'].mean():.2f}")
    print(f"Highest student average  : {analysed['Average'].max():.2f}")
    print(f"Lowest student average   : {analysed['Average'].min():.2f}")
    print(f"Students passed          : {(analysed['Result'] == 'Pass').sum()}")
    print(f"Students failed          : {(analysed['Result'] == 'Fail').sum()}")
    print(f"Average attendance       : {analysed['Attendance'].mean():.2f}%")

    subject_summary = pd.DataFrame({
        "Subject": SUBJECTS,
        "Average_Marks": [df[subject].mean().round(2) for subject in SUBJECTS]
    }).sort_values("Average_Marks", ascending=False)
    print_section("SUBJECT-WISE AVERAGE MARKS", subject_summary)

    top_five = analysed.nlargest(5, "Average")[
        ["Student_ID", "Name", "Department", "Average", "Grade", "Result"]
    ]
    print_section("TOP FIVE PERFORMING STUDENTS", top_five)

    best = subject_summary.iloc[0]
    print(f"\nBest-performing subject: {best['Subject']} ({best['Average_Marks']:.2f})")
    analysed.to_csv(OUTPUT_FILE, index=False)
    print(f"\nDetailed results exported to: {OUTPUT_FILE.name}")
    return analysed


def main():
    try:
        data = load_data()
        analyze_performance(data)
    except (FileNotFoundError, pd.errors.EmptyDataError, ValueError) as exc:
        print(f"Error: {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
