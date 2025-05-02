import numpy as np

donates = np.array(
    [
        30,
        50,
        50,
        40,
        50,
        30,
        100,
        50,
        200,
        40,
        40,
        30,
        100,
        50,
        300,
        500,
        120,
        250,
        50,
        400,
        1000,
        150,
        50,
        320,
        40,
        750,
        50,
        420,
    ]
)

# Q1
how_many_donates = len(donates)

# Q2
donates_sum = sum(donates)

# Q3
donates_below100_num = donates < 100
sum(donates_below100_num)

# Q4
donates_sorted = sorted(donates, reverse=True)

# Q5
donates_top5_sum = sum(donates_sorted[0:5])

# Q6
donates_above100_sum = sum(donates[donates > 100])

# Q7
round_donates_ratio = sum(donates % 100 == 0) / how_many_donates
