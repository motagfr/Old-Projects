import numpy as np

sales_list = [112, 103, 51, 87, 42, 21, 21, 14, 19, 88, 91, 59, 31, 12, 68]
sales = np.array(sales_list)
sales.shape = (5, 3)
sales

types = ["kitchen", "office", "outdoor"]
cities = ["Isfahan", "Qom", "Kashan", "Shahinshahr", "Najafabad"]

# Q1
sales_total = np.sum(sales)

# Q2
sales_chairtypes = np.sum(sales, axis=0)

# Q3
max_ = np.max(np.sum(sales, axis=1))
top_city_name = cities[int(np.where(max_)[0])]

# Q4

outdoor_topcity_value = np.max(sales[:, 2] / sales_total)

# Q5
price = np.array([1500, 1600, 800] * 5)
price.shape = (5, 3)
price
sales_rial = sales * price

# Q6
sales_rial_total = np.sum(sales_rial)
