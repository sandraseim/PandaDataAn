import pandas

data = pandas.read_csv('Squirrel_Data.csv')
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_count)
print(cinnamon_count)
print(black_count)

data_dict= {
    "Fur color":["Gray", "Cinnamom", "Black"],
    "Count":[gray_count, cinnamon_count, black_count]
}

df = pandas.DataFrame(data_dict)
print(df)