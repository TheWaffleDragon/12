#PANDAS#
import pandas as pd
import matplotlib.pyplot as plt

# #%%serie


# salaries = [
# 	("Mark", 1000),
# 	("John", 1500),
# 	("Daniel", 2300),
# 	("Greg", 5000)
# ]

# names_series = pd.Series(["Mark", "John", "Daniel", "Greg"])
# print(names_series)


# salary_series = pd.Series([1000, 1500, 2300, 5000])
# print(salary_series)

# print(names_series.describe())

# print(salary_series.describe())

# new_salary_series = pd.Series(salary_series + 100)

# for index in new_salary_series.index:
#     print(new_salary_series[index])
    


# #%%ramki

# salaries = [
# 	("Mark", 1000, 23),
# 	("John", 1500, 25),
# 	("Daniel", 2300, 38),
# 	("Greg", 5000, 42)
# ]

# df = pd.DataFrame(salaries)
# print(df)

# df = pd.DataFrame(salaries, columns=["name", "salary", "age"])
# df = df.set_index("name")

# print(df)
# print(df.describe())

# salary_increased_series = df['salary'].apply(lambda salary: salary + 2000)
# df['salary'] = salary_increased_series
# print(df)
# print(df.describe())

# #%%
# salaries = [
# 	("Mark", 1000, 23),
# 	("John", 1500, 25),
# 	("Daniel", 2300, 38),
# 	("Greg", 5000, 42)
# ]

# df = pd.DataFrame(salaries, columns=["name", "salary", "age"])


# df['initials'] = df['name'].apply(lambda name: name[0])
# print(df)
# #plt.bar(df.index, df["salary"])
# #df['salary'].plot(kind='bar')

# plot = df['age'].plot(kind = 'bar', colormap = 'OrRd', )
# #%%

# salaries = [1000, 5000, 7000]
# salary_iterator = iter(salaries)
# print(next(salary_iterator))
# print(next(salary_iterator))
# print(next(salary_iterator))

# salary_iterator = iter(salaries)
# salary_sum = 0
# for salary in salary_iterator:
# 	salary_sum = salary_sum + salary
# print("Total salaries = %d" % salary_sum)

# #%%
# def give_me_first_ten_numbers():
#     for i in range(1,11):
#     		yield i

# for number in give_me_first_ten_numbers():
# 	print(number)
    
    
# #%%


# def generate(x):
#     for i in range(1, x+1):
#         yield i

# sum = 0
# for number in generate(66):
#     sum = sum+number
    
# print(sum)

#%%% ZADANIE: ceny w PLN

prices = [
	(1, 2.12),
	(2, 2.56),
	(3, 3.10),
	(4, 3.16),
	(5, 3.58),
	(6, 5.12),
	(7, 5.16),
	(8, 5.20),
	(9, 4.12),
	(10, 4.10),
	(11, 3.65),
	(12, 4.25)]

df = pd.DataFrame(prices, columns=["month", "PLN"])
df = df.set_index("month")
df['USD'] = df['PLN'].apply(lambda PLN: PLN/4)

df['USD'].plot(linestyle='dashed', title = "Price of goods (USD)", color = 'red', ylim=(0, 2))