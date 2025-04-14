import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

mpg = sns.load_dataset("mpg")
sns.relplot(x="horsepower", y="mpg", hue="origin", size="weight",
            sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=mpg)
pal = dict(usa="purple", japan="blue", europe="green")  
g = sns.FacetGrid(mpg, hue="origin", palette=pal, height=5)
g.map(sns.scatterplot, "horsepower", "mpg", s=100, alpha=.5)
g.add_legend()

plt.show()



sns.set_theme(style="white")
rs = np.random.RandomState(33)
d = pd.DataFrame(data=rs.normal(size=(100, 6)),  # Changed to 6 columns
                 columns=list("origin"))
corr = d.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.diverging_palette(230, 20, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
