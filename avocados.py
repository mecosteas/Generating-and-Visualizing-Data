import pandas as pd
import matplotlib.pyplot as plt

# dataframe
df = pd.read_csv("../data/avocado.csv")

# we do this because organic and conventional are different "types" (of object?) and it's making it so we have
# duplicate dates. by choosing only organic or conventional, we avoid this problem
df = df.copy()[df['type'] == 'organic']
df['Date'] = pd.to_datetime(df["Date"])
# sort it by value
df.sort_values(by="Date", ascending=True, inplace=True)

# make sure pandas recognize the values in the dates column as actual dates
df['Date'] = pd.to_datetime(df["Date"])
# make albany_df only display the rows with Albany as a region
# albany_df = df[ df['region'] == "Albany"]

# To get rid of the warning
albany_df = df.copy()[df["region"] ==  "Albany"]

# make the dataframe be indexed by the date and make it stay in place
# we have to specify "set in place" because the panda library returns a new data frame most of the time
albany_df.set_index("Date", inplace=True)
albany_df.sort_index(inplace=True)
# this would be the same as doing this: albany_df = albany_df.set_index("Date")

# Let's make a column named "price25ma that shows the modified/cleaned up average price data we've created
albany_df['price25ma'] = albany_df['AveragePrice'].rolling(25).mean()
# To remove NA values
albany_df.dropna()

# print(albany_df.index)
# print(df['region'].unique())

# Graphing

# We want to turn the regions column into a header row
graph_df = pd.DataFrame()

for region in df['region'].unique():
    # print(region)
    region_df = df.copy()[df['region'] == region]
    region_df.set_index("Date", inplace=True)
    region_df.sort_index(inplace=True)
    # let's give the column names a unique name
    region_df[f'{region}_price25ma'] = region_df['AveragePrice'].rolling(25).mean()

    if graph_df.empty:
        graph_df = region_df[[f'{region}_price25ma']] # the double brackets make it a dataframe so it's not just a series
    else:
        graph_df = graph_df.join(region_df[f'{region}_price25ma'])

print(graph_df.tail())

# albany_df["AveragePrice"].rolling(25).mean().plot()
graph_df.dropna().plot(figsize=(8,5), legend=False)
plt.show()
