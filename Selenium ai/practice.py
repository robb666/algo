import pandas as pd


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# df = pd.read_csv('Test2.csv')

to_test = pd.read_csv('Test2.csv', dtype=object,
                      header=0)


print(to_test)