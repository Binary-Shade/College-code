import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
data = pd.read_csv('https://raw.githubusercontent.com/vizydrop/data-samples/master/flowers.csv')
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
le = LabelEncoder()
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
tree = DecisionTreeClassifier().fit(X_train, y_train)
plt.figure(figsize=(10,6))
plot_tree(tree, filled=True)
plt.title("Decision Tree")
plt.show()
rf = RandomForestClassifier(n_estimators=100, random_state=0).fit(X_train, y_train)
plt.figure(figsize=(20,12))
for i, tree_in_forest in enumerate(rf.estimators_[:6]):
        plt.subplot(2, 3, i+1)
        plt.axis('off')
        plot_tree(tree_in_forest, filled=True, rounded=True)
        plt.title("Tree " + str(i+1))
plt.suptitle("Random Forest")
plt.show()
print("Accuracy of decision tree: {:.2f}".format(tree.score(X_test, y_test)))
print("Accuracy of random forest: {:.2f}".format(rf.score(X_test, y_test)))
