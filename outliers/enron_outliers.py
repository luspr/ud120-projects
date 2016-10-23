#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL', 0)
data = featureFormat(data_dict, features)
print data_dict[data_dict.keys()[0]]



for k, v in data_dict.items():
    print k, v['salary'], v['bonus']

l = [(k, v['salary'], v['bonus']) for k, v in data_dict.items() if v['bonus'] < 10000000000000 ]

print sorted(l, key=lambda x: x[2])


for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()