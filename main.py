import pandas as pd
import numpy as np

def calculate_grades(avg_marks):
    if avg_marks >= 85:
        return 'A'
    elif avg_marks >= 70:
        return 'B'
    elif avg_marks >= 50:
        return 'C'
    else:
        return 'F'

def check_pass_fail(row, passing_threshold=50):
    if row['Average'] >= passing_threshold:
        return 'Pass'
    else:
        return 'Fail'

def main():
    print("="*60)
    print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("="*60)
    
    try:
        df = pd.read_csv('students.csv')
    except FileNotFoundError:
        print("Error: 'students.csv' file not found.")
        return

    print("\n[INFO] Dataset Loaded Successfully!")
    print(f"Total Records Found: {len(df)}")
    print("\nFirst 5 Records of the Dataset:")
    print(df.head())
    print("-" * 60)

    subject_columns = ['Math', 'Science', 'English']
    df['Total'] = df[subject_columns].sum(axis=1)
    df['Average'] = df[subject_columns].mean(axis=1)

    grades = []
    status = []
    for index, row in df.iterrows():
        grades.append(calculate_grades(row['Average']))
        status.append(check_pass_fail(row))
        
    df['Grade'] = grades
    df['Status'] = status

    print("\n--- PERFORMANCE SUMMARY REPORT ---")
    all_averages = df['Average'].to_numpy()
    class_avg = np.mean(all_averages)
    highest_avg = np.max(all_averages)
    lowest_avg = np.min(all_averages)
    
    print(f"Overall Class Average Marks: {class_avg:.2f}")
    print(f"Highest Average Score: {highest_avg:.2f}")
    print(f"Lowest Average Score: {lowest_avg:.2f}")

    top_student_idx = df['Average'].idxmax()
    top_student = df.loc[top_student_idx]
    print(f"\nTop Performing Student: {top_student['Name']} (ID: {top_student['StudentID']}) with Average: {top_student['Average']:.2f}")

    print("\n--- SUBJECT-WISE PERFORMANCE ---")
    for sub in subject_columns:
        sub_scores = df[sub].to_numpy()
        print(f"Subject: {sub: <10} | Average: {np.mean(sub_scores):.2f} | Max: {np.max(sub_scores)} | Min: {np.min(sub_scores)}")

    pass_count = (df['Status'] == 'Pass').sum()
    fail_count = (df['Status'] == 'Fail').sum()
    print("\n--- PASS/FAIL STATISTICS ---")
    print(f"Total Passed Students: {pass_count}")
    print(f"Total Failed Students: {fail_count}")

    print("\n--- DEPARTMENT-WISE AVERAGE MARKS ---")
    dept_perf = df.groupby('Department')['Average'].mean()
    print(dept_perf)

    print("\n" + "="*60)
    print("Analysis Completed Successfully.")
    print("="*60)

if __name__ == "__main__":
    main()