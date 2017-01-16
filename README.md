ud120-projects
==============

Starter project code for students taking Udacity ud120

##datasets_questions
The aggregated Enron email + financial dataset is stored in a dictionary, where each key in the dictionary is a person’s name and the value is a dictionary containing all the features of that person.
The email + finance (E+F) data dictionary is stored as a pickle file, which is a handy way to store and load python objects directly. Use datasets_questions/explore_enron_data.py to load the dataset.

How many data points (people) are in the dataset?

##datasets_questions
For each person, how many features are available?

##datasets_questions
The “poi” feature records whether the person is a person of interest, according to our definition. How many POIs are there in the E+F dataset?

##evaluation
We compiled a list of all POI names (in ../final_project/poi_names.txt) and associated email addresses (in ../final_project/poi_email_addresses.py).

How many POI’s were there total? (Use the names file, not the email addresses, since many folks have more than one address and a few didn’t work for Enron, so we don’t have their emails.)
http://usatoday30.usatoday.com/money/industries/energy/2005-12-28-enron-participants_x.htm

##Documentary
'Enron: The Smartest Guys in the Room'
https://g.co/kgs/yHEPfm

##Reference
http://scikit-learn.org/0.17/modules/cross_validation.html
http://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-categorical-features
http://scikit-learn.org/stable/modules/preprocessing_targets.html#label-encoding
