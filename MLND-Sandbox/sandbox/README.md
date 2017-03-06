
##skit-learn(aka. sklearn) References
http://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-categorical-features
http://scikit-learn.org/stable/modules/preprocessing_targets.html#label-encoding
http://scikit-learn.org/0.17/modules/cross_validation.html

###Classification Scoring Function
http://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score
http://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
http://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score
http://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error

###Regression Scoring Functions
In addition to error metrics, scikit-learn contains two scoring metrics which scale continuously from 0 to 1, with values of 0 being bad and 1 being perfect performance.

These are the metrics that you'll use in the project at the end of the course. They have the advantage of looking similar to classification metrics, with numbers closer to 1.0 being good scores and bad scores tending to be near 0.

One of these is the R2 score, which computes the coefficient of determination of predictions for true values. This is the default scoring method for regression learners in scikit-learn.

The other is the explained variance score.

While we will not dive deep into explained variance score and R2 score in this lecture , one important point to remember is that, in general, metrics for regression are such that "higher is better"; that is, higher scores indicate better performance. When using error metrics, such as mean squared error or mean absolute error, we will need to overwrite this preference.

http://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score
http://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html#sklearn.metrics.explained_variance_score

###Validation Curve (for Model Complexity)
http://scikit-learn.org/stable/modules/learning_curve.html

### How to search the optimal parameters
GridSearchCV is a way of systematically working through multiple combinations of parameter tunes, cross-validating as it goes to determine which tune gives the best performance. The beauty is that it can work through many combinations in only a couple extra lines of code.

Here's an example from the sklearn documentation:

```
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
svr = svm.SVC()
clf = grid_search.GridSearchCV(svr, parameters)
clf.fit(iris.data, iris.target)
```

Let's break this down line by line.

```
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]} 
```
A dictionary of the parameters, and the possible values they may take. In this case, they're playing around with the kernel (possible choices are 'linear' and 'rbf'), and C (possible choices are 1 and 10).

Then a 'grid' of all the following combinations of values for (kernel, C) are automatically generated:

```
('rbf', 1)	('rbf', 10)
('linear', 1)	('linear', 10)
```
Each is used to train an SVM, and the performance is then assessed using cross-validation.

```
svr = svm.SVC() 
```
This looks kind of like creating a classifier, just like we've been doing since the first lesson. But note that the "clf" isn't made until the next line--this is just saying what kind of algorithm to use. Another way to think about this is that the "classifier" isn't just the algorithm in this case, it's algorithm plus parameter values. Note that there's no monkeying around with the kernel or C; all that is handled in the next line.

```
clf = grid_search.GridSearchCV(svr, parameters) 
```
This is where the first bit of magic happens; the classifier is being created. We pass the algorithm (svr) and the dictionary of parameters to try (parameters) and it generates a grid of parameter combinations to try.

```
clf.fit(iris.data, iris.target) 
```
And the second bit of magic. The fit function now tries all the parameter combinations, and returns a fitted classifier that's automatically tuned to the optimal parameter combination. You can now access the parameter values via clf.best_params_.

http://scikit-learn.org/stable/modules/generated/sklearn.grid_search.GridSearchCV.html
