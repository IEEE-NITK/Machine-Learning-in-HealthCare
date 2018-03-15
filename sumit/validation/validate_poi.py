#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
from sklearn import cross_validation
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!
ftr,fte,ltr,lte=cross_validation.train_test_split(features,labels,test_size=0.3,random_state =42)


from sklearn import tree
clf=tree.DecisionTreeClassifier()
clf=clf.fit( ftr,ltr)
pred=clf.predict(fte)
from sklearn.metrics import accuracy_score
print accuracy_score(lte,pred)
