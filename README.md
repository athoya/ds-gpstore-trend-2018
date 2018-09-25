# ds-gpstore-trend-2018

This google playstore data are retrieved from this link.
https://www.kaggle.com/lava18/google-play-store-apps

In this csv data, we have 13 columns. Those columns are described below.
```
App - Application name
Category - Category the app belongs to
Rating - Overall user rating of the app (as when scraped)
Reviews - Number of user reviews for the app (as when scraped)
Size - Size of the app (as when scraped)
Installs - Number of user downloads/installs for the app (as when scraped)
Type - Paid or Free
Price - Price of the app (as when scraped)
Content Rating - Age group the app is targeted at - Children / Mature 21+ / Adult
Genres - An app can belong to multiple genres (apart from its main category). For eg, a musical family game will belong to Music, Game, Family genres.
Last Updated - Date when the app was last updated on Play Store (as when scraped)
Current Ver - Current version of the app available on Play Store (as when scraped)
Android Ver - Min required Android version (as when scraped)
```

In this mini project, we will use pandas and sns.
Pandas framework is a good library to handle data dan manipulate data.
Seaborn is also one good library for displaying data, similar with matlibplot.
```
import pandas as pd
import seaborn as sns
```

We can download the csv data first, then we can import it and convert as DataFrame in pandas.
We can see the number of data rows by calling shape function in DataFrame. It show that we have **10841** rows.
```
df = pd.read_csv('googleplaystore.csv')
print(df.shape[0])
```

If we print the first the of the dataset, we will get the following table.
```
print(df[:3])
```

App |	Category | Rating | Reviews |	Size | Installs |	Type |	Price | Content Rating |	Genres |	Last Updated |	Current Ver |	Android Ver
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- 
Photo Editor & Candy Camera & Grid & ScrapBook | ART_AND_DESIGN | 4.1 | 159 | 19M | 10,000+ | Free | 0 | Everyone | Art & Design | January 7, 2018 | 1.0.0 | 4.0.3 and up
Coloring book moana |	ART_AND_DESIGN |	3.9 |	967 |	14M |	500,000+ |	Free |	0 |	Everyone |	Art & Design;Pretend Play |	January 15, 2018 |	2.0.0 |	4.0.3 and up
U Launcher Lite – FREE Live Cool Themes, Hide ... |	ART_AND_DESIGN	| 4.7 |	87510 |	8.7M |	5,000,000+ |	Free |	0 |	Everyone |	Art & Design |	August 1, 2018 |	1.2.4 |	4.0.3 and up

First, we can populate the app based on categories and count the categories. The idea is to see how the distribution of app in term of category.
```
cat = df.groupby(['Category']).size().to_frame(name = 'count').reset_index()
cat_sorted = cat.sort_values(by='count', ascending=False)
```

We can plot them and see, what is the top 10 of the catergories
```
sns.set(style="whitegrid")
ax = sns.barplot(x="count", y="Category", data=cat_sorted[:10])
```
[top_cat_10]: https://github.com/athoya/ds-gpstore-trend-2018/blob/master/images/top_10_category.png "Top 10 Category"
![alt text][top_cat_10]
