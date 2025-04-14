import seaborn as sns
import matplotlib.pyplot as plt

mpg = sns.load_dataset("mpg")
sns.relplot(x="horsepower", y="mpg", hue="origin", size="weight",
            sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=mpg)
pal = dict(usa="purple", japan="blue", europe="green")  
g = sns.FacetGrid(mpg, hue="origin", palette=pal, height=5)
g.map(sns.scatterplot, "horsepower", "mpg", s=100, alpha=.5)
g.add_legend()

plt.show()
