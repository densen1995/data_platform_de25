import pandas as pd

product_df = pd.DataFrame(
    {
        "id": ["SKU-1", "SKU-2", "SKU-3", "SKU-4", "SKU-5"],
        "name": ["shoes", "pants", "shirts", "sweaters", "designer jacket"],
        "price": [760, 520, 450, 550, 4500],
        "currency":["SEK", "SEK", "SEK", "SEK", "SEK"],
    }

)
#print(df)
print(product_df)


#HELPER METHODS
print(product_df["price"].max())
print(product_df["price"].min())
print(product_df["price"].mean())
print(product_df["price"].median())

print(product_df.sort_values("price", ascending=False))

print(product_df.describe()) #statistics of numerical data

#to_*(exporting files)
product_df.to_csv("products.csv", index= False) #path folder


dirty_df = pd.DataFrame(
    {
        "id": ["sKU-1", "SKU-2", "SKU-3", "sKU-4", "SKU-5"],
        "name": ["shoes", "pants", "shirts", "sweaters", "designer jacket"],
        "price": [760, 520, 450, 550, 4500],
        "currency":["sEK", "SEK", "SEK", "sEK", "SEK"],
    }

)

dirty_df["name"] = dirty_df["name"].str.strip()
dirty_df["name"] = dirty_df["name"].str.title()
dirty_df["name"] = dirty_df["name"].str.replace(r"\s+", " ", regex=True)

#lambda
cols_to_upper = ["id", "currency"]
dirty_df[cols_to_upper]

print(dirty_df.values)


missing_df = pd.DataFrame(
    {
        "id": ["sKU-1", "SKU-2", None, "sKU-4", "SKU-5"],
        "name": ["shoes", None, "shirts", "sweaters", "designer jacket"],
        "price": [760, 520, None, 550, 4500],
        "currency":["sEK", "SEK", "SEK", None, "SEK"],
    }

)

print(missing_df.isna()) #pandas tool for identifying TRUE missing values .

#flag missing values, helps decide strategy later on 
missing_df["id"]=missing_df["id"].isna()

#flag missing values, helps decide strategy later on
missing_df["id_missing"]=missing_df["id"].isna()
missing_df["price_missing"]=missing_df["price"].isna()
missing_df["name_missing"]=missing_df["name"].isna()
missing_df["currency_missing"]=missing_df["currency"].isna()


print(missing_df)






"""
mdf_values = ["id", "name", "price", "currency"]
for mdf in mdf_values:
    missing_df[mdf+"-missing"] = missing_df[mdf].isna()


print(missing_df)"""



