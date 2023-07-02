import pandas as pd

read = pd.read_csv("organizations-100.csv")
print(read)

#Size (How many items are there)
print(read.size)
#Shape (How many items are there in the form of rows and coloumn)
print(read.shape)
#Count (how many items by each coloum ,give us full details
print(read.count())
#DataTyepe(Give datatype of every object)
print(read.dtypes)
#unique (cheack a number unque items)
print(read.nunique())

