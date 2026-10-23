# Project Documentation: Student Performance Analytics System

## 1. Project Title and Student Details
**Project:** Student Performance Analytics System  
**Student:** Harsh Kumar Pandey   
**Course:** Python with AI

## 2. Objective
The objective is to analyze student marks and attendance using Python. The program summarizes student performance, calculates grades and pass/fail results, compares subjects, and identifies top performers.

## 3. Technologies Used
- Python: functions, loops, conditions, and file handling.
- Pandas: loading CSV data, DataFrames, sorting, and summaries.
- NumPy: numerical operations on student marks.
- CSV: storage of student records and exported results.

## 4. Dataset Description
The supplied `students.csv` contains 20 sample student records with Student_ID, Name, Department, Python, Mathematics, Data_Analysis, and Attendance. 

## 5. Implementation
1. `load_data()` reads the CSV with Pandas and checks required columns and numeric ranges.
2. `add_performance_columns()` uses NumPy to calculate total and average marks.
3. `grade_for_average()` assigns a grade according to the grading scale.
4. A loop processes each student and assigns Pass or Fail. A student passes only if marks are at least 40 in all three subjects.
5. Pandas calculates the overall class average, highest and lowest averages, pass/fail counts, and average attendance.
6. Subject averages are sorted to identify the highest-performing subject.
7. The top five students by average are displayed.
8. The processed records are exported to `student_analysis_results.csv`.

## 6. Key Features
- CSV data loading and validation.
- Total and average marks calculation.
- Grade assignment and pass/fail classification.
- Class-level summary statistics.
- Subject-wise performance analysis.
- Top five performers report.
- Exported analysis CSV.

## 7. Output / Screenshots
Run `python main.py` and insert screenshots below:
- **Screenshot 1:** Student table and class summary.
![Screenshort 1](https://snipboard.io/b4yLva.jpg)
- **Screenshot 2:** Subject-wise average marks.
  ![Screenshort 2](https://snipboard.io/EC6ZQc.jpg)
- **Screenshot 3:** Students.csv.
  ![Screenshort 3](https://snipboard.io/joSNJC.jpg)
- **Screenshot 4:** Exported `student_analysis_results.csv`.
  ![Screenshort 4](https://snipboard.io/Px4aqh.jpg)


## 8. Final Outcome
The system analyzes the sample student records and displays totals, averages, grades, pass/fail status, class statistics, subject averages, and top performers. It also saves the detailed results in a CSV file.

## 9. Challenges and Learning
The project provides practice in reading CSV files, validating columns, processing DataFrames, using NumPy for numerical operations, applying loops and conditions, writing reusable functions, and interpreting summary statistics.

A key design decision is the pass rule: each student must score at least 40 in every subject. This is separate from the average-based grade.



