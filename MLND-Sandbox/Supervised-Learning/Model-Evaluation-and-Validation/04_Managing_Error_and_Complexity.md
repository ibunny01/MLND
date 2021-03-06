# Managing Error and Complexity

## Causes of Error
### Causes of Error
Now that we have covered some basic metrics for measuring model performance, let us turn our attention to reasons why models exhibit errors in the first place.

In model prediction there are two main sources of errors that a model can suffer from. Bias due to a model being unable to represent the complexity of the underlying data and variance due to a model being overly sensitive to the limited data it has been trained on. We will go over both in a bit more detail.

### Error due to Bias - Accuracy and Underfitting
Bias occurs when a model has enough data but is not complex enough to capture the underlying relationships. As a result, the model consistently and systematically misrepresents the data, leading to low accuracy in prediction. This is known as underfitting.

Simply put, bias occurs when we have an inadequate model. An example might be when we have objects that are classified by color and shape, for example easter eggs, but our model can only partition and classify objects by color. It would therefore consistently mislabel future objects--for example labeling rainbows as easter eggs because they are colorful.

Another example would be continuous data that is polynomial in nature, with a model that can only represent linear relationships. In this case it does not matter how much data we feed the model because it cannot represent the underlying relationship. To overcome error from bias, we need a more complex model.

### Error due to Variance - Precision and Overfitting
When training a model, we typically use a limited number of samples from a larger population. If we repeatedly train a model with randomly selected subsets of data, we would expect its predictons to be different based on the specific examples given to it. Here variance is a measure of how much the predictions vary for any given test sample.

Some variance is normal, but too much variance indicates that the model is unable to generalize its predictions to the larger population. High sensitivity to the training set is also known as overfitting, and generally occurs when either the model is too complex or when we do not have enough data to support it.

We can typically reduce the variability of a model's predictions and increase precision by training on more data. If more data is unavailable, we can also control variance by limiting our model's complexity.


## Representative Power of a Model

## Learning Curves and Model Complexity

## Cross Validation
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

http://scikit-learn.org/stable/auto_examples/applications/face_recognition.html
