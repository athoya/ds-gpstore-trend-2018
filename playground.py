# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns

df = pd.read_csv('googleplaystore.csv')

#print(list(df))
print(df.groupby(['Category']).size())

cat = df.groupby(['Category']).size().to_frame(name = 'count').reset_index()
cat_sorted = cat.sort_values(by='count', ascending=False)

print(cat_sorted)
sns.set(style="whitegrid")

# vertical bar plot
#ax = sns.barplot(x="Category", y="count", data=cat_sorted[:10])
#ax.set_xticklabels(ax.get_xticklabels(),rotation=90)

# horizontal bar plot
ax = sns.barplot(x="count", y="Category", data=cat_sorted[:10])
#ax.set_xticklabels(ax.get_xticklabels(),rotation=90)