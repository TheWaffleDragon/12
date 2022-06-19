# import matplotlib.pyplot as plt
# import numpy as np


# #matplot
# #%%
# X = [0,1,2,3]
# Y = [0,1,0,1]
# plt.plot(X, Y)
# #%%

# X_1 = [0,1,2,3,4,5,6,7]
# Y_1 = [0,1,1,0,0,1,1,0]
# plt.plot(X_1,Y_1)


# #%%
# salaries = [
# 	("Mark", 1000),
# 	("John", 1500),
# 	("Daniel", 2300),
# 	("Greg", 5000)
# ]

# names = list(map(lambda tup:tup[0], salaries))
# salary_values = list(map(lambda tup:tup[1], salaries))
# plt.plot(salary_values)
# plt.bar(names, salary_values)

# #%%
# plt.title("Salaries")
# plt.xlabel("Employee")
# plt.ylabel("Salary in zł")
# plt.bar(names, salary_values)

# #%%
# figure, ax = plt.subplots()
# ax.bar(names, salary_values)
# ax.set_xlabel("Employee")
# ax.set_ylabel("Salary in zł")


# #%%
# figure, ax = plt.subplots()
# ax.barh(names, salary_values,color='Green')
# ax.set_ylabel("Employee")
# ax.set_xlabel("Salary in zł")


# ##ploty
# #%%
# import plotly.graph_objects as go
# import plotly.io as pio
# #pio.renderers.default = 'svg'
# pio.renderers.default = 'browser'
# X = [0,1,2,3]
# Y = [0,1,0,1]

# data = go.Scatter(x=X, y=Y)
# layout = {
# 	'title': 'Zigzag with plotly'
# }
# fig = go.Figure(data, layout)
# fig.show()

#%%ZADANIE: pensje w ploty

import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = 'browser'

salaries = [
	("Mark", 1000),
	("John", 1500),
	("Daniel", 2300),
	("Greg", 5000)
]


names = list(map(lambda tup:tup[0], salaries))
salary_values = list(map(lambda tup:tup[1], salaries))

data = go.Bar(x=names, y=salary_values)
layout = {
    'title': 'Zarobki'
    }
fig = go.Figure(data, layout)
fig.show()
