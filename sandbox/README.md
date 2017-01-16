
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