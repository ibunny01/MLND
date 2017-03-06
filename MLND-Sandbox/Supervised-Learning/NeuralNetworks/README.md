## Sigmoid.py
Reference
https://discussions.udacity.com/t/quiz-sigmoid-programming-exercise/174620/5 : Jared's post

```
JaredNanodegree Services LeadJun '16
Hi guys,

Without trying to give too much away, I want to point out that you should not be modifying the result variable that is in the update function. What you need to update is the following line:

for i in range(0,len(values)):
   self.weights[i] += eta*(train - result)*values[i]
Note that this line is the standard perceptron updating rule, and we want to update the weights using a gradient descent update rule. From one of the lectures (in my own notation), the gradient update rule would be as follows:

   w_i += eta * (t - y) * g'(x) * x_i
Where t is the target, y is the result, and g(x) is the activation function. Do you notice what is added here that is not present in the original training rule? It's the derivative of the activation function! Do we know how to calculate that? Try changing the line I've mentioned to include the derivative of the activation function to see if it gives the correct results.
```

https://discussions.udacity.com/t/sigmoid-programming-exercise/175059

