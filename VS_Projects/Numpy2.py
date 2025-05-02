import numpy as np

names = np.array(
    [
        "Ali",
        "Amin",
        "Bita",
        "Maryam",
        "Mina",
        "Nikoo",
        "Reza",
        "Sadra",
        "Sajad",
        "Saeed",
        "Sina",
        "Zahra",
    ]
)
persianlttr = np.array([89, 71, 57, 91, 73, 51, 96, 48, 59, 61, 75, 65])
stats = np.array([79, 74, 69, 86, 79, 59, 78, 58, 51, 72, 70, 61])
sociology = np.array([38, 83, 51, 78, 60, 81, 91, 53, 41, 71, 69, 47])
economics = np.array([78, 85, 79, 73, 66, 63, 78, 67, 61, 75, 74, 57])
programming = np.array([69, 74, 84, 63, 56, 67, 78, 79, 72, 85, 51, 41])
linearAlgebra = np.array([19, 34, 44, 61, 51, 47, 38, 43, 52, 35, 41, 21])

# Q1
grades_avg = (
    persianlttr + stats + sociology + economics + programming + linearAlgebra
) / 6
grades_avg

# Q2
grades_min = min(grades_avg)
grades_max = max(grades_avg)

# Q3
ratio_above70 = len(grades_avg[grades_avg > 70]) / len(grades_avg)

# Q4
names_avgbelow50 = names[grades_avg < 50]

# Q5
x = np.vstack((persianlttr, sociology, economics, programming, linearAlgebra, stats))
all_below50s = len(x[x < 50])

# Q6

false_grade = "Reza"
np.where(names == false_grade)
persianlttr[6] = 0
persianlttr_avg_adjusted = sum(persianlttr) / len(persianlttr)
