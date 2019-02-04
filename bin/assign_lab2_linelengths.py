##
#
# Author: Matthew A. Turner <maturner01@gmail.com>
# Date 2019-02-03
#
import numpy as np
import pandas as pd

# Lab #2 Parameters.
n_teams = 3
smallest_linelen = 4
linelens_per_student = 2

# Load .gitignore'd student list, different each semester.
students = list(open('students.txt', 'r').readlines())
n_students = len(students)

# Repeat each student lines_per_student times
students_repeated = []
for student in students:
    students_repeated.extend([student] * linelens_per_student)

# The largest linelength depends on the number of students.
largest_linelen = smallest_linelen + (linelens_per_student * n_students)

# Create permuted list of line lengths.
linelens = np.random.permutation(range(smallest_linelen, largest_linelen))

# Make dataframe of students and line lengths, and save as .xls.
assign_df = pd.DataFrame(
    {'student': students_repeated, 'line-length': linelens}
)

# Save the assignments to an Excel file that will be uploaded to G Sheets.
assign_df.to_excel('Lab2-Spring19-Assignments.xlsx')

# Shuffle students for splitting into random teams.
shuffled_students = np.random.permutation(students)

# Split student list into three groups, all same size if possible.
n_per_team = n_students // n_teams
remainder = n_students % n_teams
team1 = shuffled_students[:n_per_team]
# One team will have more than two others.
if (remainder == 1) or (remainder == 0):
    team2_end_idx = (n_per_team * 2) + 1
# Two teams will have more than one other.
elif remainder == 2:
    team2_end_idx = (n_per_team * 2) + 2

team2 =  shuffled_students[n_per_team:team2_end_idx]
team3 = shuffled_students[team2_end_idx:]
teams = [team1, team2, team3]
for idx, team in enumerate(teams):
    with open('team{}.txt'.format(idx), 'w') as f:
        for student in team:
            f.write(student)
