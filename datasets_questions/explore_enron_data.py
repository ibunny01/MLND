#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import os,sys
os.chdir(sys.path[0])

import pickle 

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# print enron_data

# for key  in enron_data:
#     print key, enron_data[key]

# how to iterate dictionary data in Python
# for (k, v) in enron_data.items():
#     print k, v

# how to make reverse map (v, k) of original dictionary
# print zip(enron_data.viewkeys(), enron_data.viewvalues())

# print # of data
print "# of enron_data : ",len(enron_data)

# print # of features
print "# of enron_data's features : ",len(enron_data.items()[0][1].keys())

# print # of data which has poi features
count_of_poi = 0
for (k,v) in enron_data.items():
    if v['poi'] == 1:
        print count_of_poi,' ', k
        count_of_poi+=1
print "# of data which has poi features : ",count_of_poi

# print the total value of stock belonging to James Prentice
# print enron_data.viewkeys()
print enron_data[" ".join('James Prentice'.upper().split(' ')[::-1])].keys()
print enron_data[" ".join('James Prentice'.upper().split(' ')[::-1])]['total_stock_value']

# case of Wesley Colwell
print enron_data[" ".join('Wesley Colwell'.upper().split(' ')[::-1])]['from_this_person_to_poi']


# cass of Jeffrey K Skilling
for (k, v) in enron_data["SKILLING JEFFREY K"].items():
    if 'stock' in k:
        print k,':',v

# find featureset 
keys = []
for (k, v) in enron_data.items():
    if len(set(['LAY', 'SKILLING', 'FASTOW']) & set(k.split(' '))) > 0:
        keys.append(k)

print keys

person = ''
amount = 0.0
for k in keys:
    if amount < enron_data[k]['total_payments']:
        person = k
        amount = enron_data[k]['total_payments']

print person, ' : ', amount

# assess quantity of email & salary
cnt_of_qual_sal = 0
cnt_of_email = 0
for k in enron_data.keys():
    if enron_data[k]['salary'] != 'NaN':
        cnt_of_qual_sal+=1
    if enron_data[k]['email_address'] != 'NaN':
        cnt_of_email+=1

print cnt_of_qual_sal, cnt_of_email