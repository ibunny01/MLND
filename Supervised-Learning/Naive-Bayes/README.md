#  Naive Bayes Subtitles
##  01 - Speed Scatterplot Grade and Bumpiness
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So let's talk about something called scatter plots.                              
 2      |  And I'm going to use the current example.                                        
 3      |  When we drove our car we had days when the train was completely flat,            
 4      |  let's us drive very fast.                                                        
 5      |  Sometimes we encountered a little bit of bumpiness or a lot of bumpiness.        
 6      |  Which kind of forces us to slow down.                                            
 7      |  So one way in which our terrain was able to vary, was at the level of bumpiness. 
 8      |  Which could go from smooth, to really bad.                                       
 9      |  Second dimension, which our terrain varied had to do with slope.                 
 10     |  Could be flat.                                                                   
 11     |  Or, they were different levels of steepness.                                     
 12     |  I'm obviously slightly exaggerating here.                                        
 13     |  So it goes from flat to very steep.                                              
 14     |  And, again, the steeper it is the slower we wish to drive.                       
 15     |  And, those things could co-occur,                                                
 16     |  as shown in these speed graphs on the right side.                                
 17     |  So what I want to do with you is just map these training examples over here,     
 18     |  of say a flat, smooth vote, into our diagram over here.                          
 19     |  And I give you nine possible points that correspond to                           
 20     |  all the combinations of the three bumpiness levels we encountered.               
 21     |  And the three slope levels.                                                      
 22     |  And when I ask you to take a car set away from, like, this one and then define   
 23     |  the correct of the main items that best represents the situation over here       


##  02 - Speed Scatterplot Grade and Bumpiness
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And, I'd say this is smooth and flat, so it goes right here.                     


##  03 - Speed Scatterplot 2
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  How about this situation here?                                                   
 2      |  Which one do you think best represents the situation over here?                  


##  04 - Speed Scatterplot 2
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And it says that this very steep, but not that bumpy, it's medium bumpy.         
 2      |  So very steep medium bumpiness goes right here.                                  


##  05 - Speed Scatterplot 3
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And just for the fun of it, let's do it with this guy over here.                 
 2      |  Where does it belong into the scatter down here?                                 


##  06 - Speed Scatterplot 3
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Well it's super bumpy but still flat.                                            
 2      |  That would be the point right here.                                              
 3      |  What I want to get you to understand is that these individual driving            
 4      |  conditions can be plotted in a two dimensional diagram where each                
 5      |  situation becomes a data point.                                                  
 6      |  That's called a scatter plot and for the three examples that are circled         
 7      |  these three data points are kind of identical.                                   
 8      |  They have a scatter plot of those three situations.                              
 9      |  So they often, instead of looking at the raw data,                               
 10     |  we plot the data in a diagram just like this.                                    


##  07 - Scatterplots to Predictions
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So let's look at another scatter plot.                                           
 2      |  Suppose this is your data,                                                       
 3      |  and again it comes in two categories in two dimensions.                          
 4      |  And now we get a new data point,                                                 
 5      |  and that came out over here, drawing the little question mark.                   
 6      |  One of the absolutely important questions in machine learning is what can you    
 7      |  say about a new data point you've never seen before.                             
 8      |  Given the past data and just your intuition, would you                           
 9      |  believe that this user point is more like a red x or more like a blue circle?    
 10     |  Check one of the two boxes over here.                                            


##  08 - Scatterplots to Predictions
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And I would argue it's more like a blue circle because it                        
 2      |  sits within the blue circles over here and not between the red x's.              


##  09 - Scatterplots to Predictions 2
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So how about a data point down here?                                             
 2      |  This time, I give you three choices, blue circle, a red x, or unclear.           
 3      |  Just pick one of the three.                                                      


##  10 - Scatterplots to Predictions 2
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And, and I would pick unclear, we can argue this,                                
 2      |  maybe it's a bit closer to the blue circles perhaps to the red crosses, but      
 3      |  to me so much in the middle it's unclear                                         


##  11 - Scatterplots to Decision Surface
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  What our machine learning algorithms do is,                                      
 2      |  they define what's called a decision surface.                                    
 3      |  They typically lies somewhere between the two different classes,                 
 4      |  like this one over here.                                                         
 5      |  And on one side they will predict red cross for every possible data point.       
 6      |  Whereas on the other, they predict the opposite concept.                         
 7      |  So with the decision surface over here,                                          
 8      |  it's not easy to say what the label would be for data point over here.           
 9      |  And again, I give you two choices, red cross or blue circle                      


##  12 - Scatterplot to Decision Surface
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  This one wasn't particularly hard,                                               
 2      |  it's kind of opposite, this is more of a red cross than a blue circle.           
 3      |  But the nice thing to understand, this decision surface over here,               
 4      |  that I drew in, we separates.                                                    
 5      |  One class from another class in a way that you can generalize two                
 6      |  new never before seen data points.                                               


##  13 - Good Linear Decision Surface
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  When the decision surface is a straight line we call it linear.                  
 2      |  And that will give you three decision surfaces, and you should                   
 3      |  click on the one and one only, that you think will best channelize the new data. 


##  14 - Good Linear Decision Surface
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And this was a tricky question.                                                  
 2      |  I would pick this one.                                                           
 3      |  This one over here is obviously not good because we                              
 4      |  even misclassifying our existing data.                                           
 5      |  Is on the, these are on the wrong side of the decision surface.                  
 6      |  So let's take this one out.                                                      
 7      |  But the one going vertical here does correctly classify most data points.        
 8      |  Except for this one over here.                                                   
 9      |  And also comes very close to the red cross over here.                            
 10     |  That's something we're going to explore later in this class.                     
 11     |  But for the time being what you should notice is that what                       
 12     |  you're machine learning algorithm does it takes in data and                      
 13     |  it transforms it into a decision surface.                                        
 14     |  DS.                                                                              
 15     |  That for all future cases.                                                       
 16     |  Can enable you to make a determination of wether it's a red cross or             
 17     |  a blue circle, and that is very powerful.                                        


##  15 - Transition to Using Naive Bayes
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So anyways, what's next in this class,                                           
 2      |  you're going to learn of what's an equivalent of Naïve Bayes.                   
 3      |  Bayes was a religious man trying to prove the existence of God.                  
 4      |  He wasn't very naïve.                                                           
 5      |  But the algorithm is kind of naïve and                                          
 6      |  it's a very common algorithm to find at a certain surface, just like this        


##  16 - NB Decision Boundary in Python
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay, so let me show you where we're going with all this.                        
 2      |  We're going to zoom ahead on supervised classification.                          
 3      |  So here we have the driving data set,                                            
 4      |  750 points now that we've drawn in our scatter plot.                             
 5      |  And the goal is to draw a decision boundary that will help us distinguish which  
 6      |  terrain we need to go slow on and which terrain we can go really fast.           
 7      |  So that means being able to draw a boundary that looks something like this,      
 8      |  where we're able to divide the two classes.                                      
 9      |  And here's what that's going to look like.                                       
 10     |  So we have our decision boundary that we can draw in here between our two        
 11     |  classes, and for any arbitrary point, we can immediately classify it as          
 12     |  terrain where we have to go slow or terrain where we can drive really fast.      


##  17 - Getting Started With sklearn
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  All right so we kind of zoomed ahead to the end there.                           
 2      |  So let's take a step back and walk through what I just did but much more slowly. 
 3      |  You're going to see all the steps that I went through when I                     
 4      |  wrote the Python code that just made that decision boundary.                     
 5      |  And by the end of the next video or                                              
 6      |  two, you will be able to write this code yourself.                               
 7      |  So the place that we start [LAUGH] as always maybe is Google.                    
 8      |  So there's a Python library that I'm going to be using a lot in this lesson, and 
 9      |  we're going to be using Google to help us use the documentation of               
 10     |  that library to figure out how to use some of the functions that it has.         
 11     |  The name of this library is scikit-learn, which is often abbreviated sk-learn.   
 12     |  So let me get you used to that convention now.                                   
 13     |  So I'm going to search google for sklearn and                                    
 14     |  the name of the algorithm that I just used, which happens to be Naive Bayes.     
 15     |  We'll go back in a little bit and talk about what Naive Bayes does exactly.      
 16     |  But first I want you to have you running the code.                               
 17     |  So sklearn Naive Bayes.                                                          
 18     |  See what's out there.                                                            
 19     |  There's a page on Naive Bayes here that gives you                                
 20     |  a derivation of the Naive Bayes formula and then a bunch of use cases.           
 21     |  Including something that says Gaussian Naive Bayes and, as it turns out,         
 22     |  this is what I'm going to be using.                                              
 23     |  So let's head back 'because I saw Gaussian Naive Bayes as one of                 
 24     |  the other results on Google.                                                     
 25     |  That's this one. Gaussian Naive Bayes,                                           
 26     |  this is what the way that I actually wrote classifier that you just saw          


##  18 - Gaussian NB Example
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay, so now what I've done is I've gone to the Gaussian Naive Bayes             
 2      |  documentation page.                                                              
 3      |  sklearn.naive_bayes.GaussianNB.                                                  
 4      |  This was that algorithm that I set out to find and                               
 5      |  now that I've, now I've found the SK Learn documentation page.                   
 6      |  So the first thing that I see right here, actually this is one of the things I   
 7      |  love about the SK Learn documentation, is it's full of examples.                 
 8      |  When I was actually developing the code for this class, this was one of          
 9      |  the first things that I would always do is I would come find the example code    
 10     |  and I would try to just run in my Python interpreter,                            
 11     |  see if I could get it working.                                                   
 12     |  And almost invariably it works right out of the box.                             
 13     |  So here's something that's just very simple.                                     
 14     |  There's only a few lines here that are really important.                         
 15     |  So let me point them out to you and                                              
 16     |  then I'll show you the code I've actually written for the example we just saw,   
 17     |  and you'll start to recognize some of these lines.                               
 18     |  But first let's introduce them.                                                  
 19     |  So the first one that's really important is this one right here.                 
 20     |  Above this it's just creating some, some training points that we can use,        
 21     |  it's not that important.                                                         
 22     |  This is where the real meat starts, is with this import statement and if you've  
 23     |  programmed in Python before, you're well acquainted with import statements.      
 24     |  This is the way that you bring in external modules into the code that you're     
 25     |  writing so that you don't have to completely re-implement everything every time, 
 26     |  you can use code that someone else has already written.                          
 27     |  So we say from sklearn.naive_bayes going to import GaussianNB.                   
 28     |  Very good.                                                                       
 29     |  The next thing that we're going to do is we're going to use that to              
 30     |  create a classifier.                                                             
 31     |  So classifier equals GaussianNB.                                                 
 32     |  If you miss your import statement.                                               
 33     |  If you forget this line for                                                      
 34     |  some reason, then this line is going to throw an error.                          
 35     |  So if you end up seeing some kind of error that says that it doesn't recognize   
 36     |  this function.                                                                   
 37     |  It's probably a problem with your import statement.                              
 38     |  So, okay, we've created our classifier.                                          
 39     |  So now the code is all sort of ready to go.                                      
 40     |  The next thing that we need to do is we need to fit it.                          
 41     |  And we've been using the word train interchangeably with fit.                    
 42     |  So this is where we actually give it the training data,                          
 43     |  and it learns the patterns.                                                      
 44     |  So we have the classifier that we just created.                                  
 45     |  We're calling the fit function on it, and then the two arguments that we pass to 
 46     |  fit are x, which in this case are the features and y which are the labels.       
 47     |  This is always going to be true in supervised classification.                    
 48     |  Is that it's going to call this fit function and                                 
 49     |  then it's going to have the features.                                            
 50     |  And then the labels.                                                             
 51     |  And then the last thing that we do is we ask the classifier that                 
 52     |  we've just trained for some predictions.                                         
 53     |  So we give it a new point.                                                       
 54     |  In this case the point is negative 0.8, negative 1.                              
 55     |  And we ask for this what do you think the label is for this particular point?    
 56     |  What's the, what class does it belong to?                                        
 57     |  So in this particular case it says it belongs to class number one.               
 58     |  Or you could imagine for some other point it might say class number two.         
 59     |  So of course you have to have already fit the classifier before you              
 60     |  can call predict on it.                                                          
 61     |  Because when it's fitting the data that's where it's                             
 62     |  actually learning the patterns.                                                  
 63     |  Then here is where it's using those patterns to make a prediction.               
 64     |  So, that's it.                                                                   
 65     |  That's kind of, now you know most all there is to                                
 66     |  know to get this working in the first example that I've done.                    


##  19 - GaussianNB Deployment on Terrain Data
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  All right, so let me actually show you the code that I used to do                
 2      |  that example that we just saw, and then you're just going to be                  
 3      |  copying this code in the quiz to make sure that you get all the details.         
 4      |  This stuff that I've just highlighted is the code that's really important, and   
 5      |  hopefully this looks really familiar to what you just saw in the example.        
 6      |  So, what I've already done up to this point is I've loaded in my                 
 7      |  training data and I've made some visualizations of it.                           
 8      |  We're going to ignore that for now.                                              
 9      |  But you'll be able to see the code in the quiz if, if you're interested.         
 10     |  And then here, as I said, are the four lines that are really important.          
 11     |  So, we have the import statement like you just saw in the example.               
 12     |  Then we create the classifier.                                                   
 13     |  We fit it, using our training features and our training labels.                  
 14     |  And then the last thing that we do is we create a vector of predictions,         
 15     |  this called pred, by using the predict function on our trained classifier.       
 16     |  And then to that we pass the features.                                           


##  20 - Gaussian Deployment Solution
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  As part of the code, it will actually draw this scatterplot and                  
 2      |  put the decision boundary in on top of it.                                       
 3      |  So, the thing that you should see when you complete this code is an image that   
 4      |  looks like this one.                                                             
 5      |  If you see this image, everything's working right.                               


##  21 - Accuracy of Naive Bayes
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  All right. Fantastic.                                                            
 2      |  So we're almost there.                                                           
 3      |  There's going to be one more thing that I'm going to ask you to do before we     
 4      |  finish with this unit and that is to evaluate our classifier.                    
 5      |  To quantify how well it's doing at classifying points.                           
 6      |  Whether they're terrain that we can drive fast on or                             
 7      |  terrain where we have to go more slowly.                                         
 8      |  So the metric that we're going to use in this case to decide how                 
 9      |  well our algorithm is doing is the accuracy.                                     
 10     |  Accuracy is just the number of points that are classified correctly divided by   
 11     |  the total number of, of points in the test set.                                  
 12     |  So the quiz that I want you to answer right now is to tell me                    
 13     |  what the accuracy is of this naive_bayes classifier that we've just made.        
 14     |  And so there are two different ways that we can do this.                         
 15     |  The first is that you can actually take the the predictions that you've          
 16     |  made here and you can compare them to the labels in your test set.               
 17     |  Or what you can actually do is head back over to                                 
 18     |  the Scikit-learn documentation and see if there's some                           
 19     |  Scikit-learn function that might be able to take care of this for you.           
 20     |  So, computing this accuracy element by element is one way that you can do it or  
 21     |  if you want to be a little bit more adventurous.                                 
 22     |  Go check out the documentation and maybe there's a really cool one-liner that    
 23     |  you can use from sklearn that'll take care of this for you.                      
 24     |  Okay?                                                                            
 25     |  So the quiz question is basically, do this calculation either on your own or     
 26     |  using sklearn and tell me how accurate our classifier is.                        


##  22 - Accuracy of Naive Bayes
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  All right. So, here's what I did.                                                
 2      |  I gave you the choice of two different methods,                                  
 3      |  either writing your own code to calculate the accuracy, or using sklearn.        
 4      |  What I myself chose to do was to use the sklearn accuracy_score,                 
 5      |  which is what you'll find if you Google sklearn accuracy.                        
 6      |  And so, this is just a function that takes a bunch of predictions,               
 7      |  it takes a bunch of labels, and then goes through and                            
 8      |  does the element by element comparison.                                          
 9      |  And then will give you the accuracy that,                                        
 10     |  that your classifier has on your test set.                                       
 11     |  So, hopefully, what you got, and what I got for the accuracy is about 88.4%.     
 12     |  So, 88.4% of the points are being correctly labelled by our                      
 13     |  classifier when we use our test set.                                             


##  23 - Training and Testing Data
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Welcome back!                                                                    
 2      |  What you just got was 88.4% correct for naive base.                              
 3      |  >> 88.4.                                                                         
 4      |  Awesome guys.                                                                    
 5      |  >> Well, does that mean that your,                                               
 6      |  your selfdriving car only crashed 11.6% of the time?                             
 7      |  >> It'll crash occasionally yeah.                                                
 8      |  It's not good enough for cars.                                                   
 9      |  >> Okay. >> But it's great for this course.                                      
 10     |  >> It is very good.                                                              
 11     |  It's much better than guessing.                                                  
 12     |  One of the things that you did in that example,                                  
 13     |  maybe you didn't even realized you were doing it was you trained and             
 14     |  you tested on two different sets of data.                                        
 15     |  >> And that's actually really important in machine learning we always train and  
 16     |  test on different data.                                                          
 17     |  >> If you don't do that what can happen is that you can over fit to your         
 18     |  training data.                                                                   
 19     |  You can think that you know better what's going on than, than you actually know. 
 20     |  >> That's really important because in machine learning you have to kind of       
 21     |  generaliz to new data that's somewhat different.                                 
 22     |  And I would just memorize all the data,                                          
 23     |  test it on the same data as training data, which will always give you 100%.      
 24     |  But I have no clue how to generalize the new data.                               
 25     |  >> That's right. So what you should always do,                                   
 26     |  and what we'll always do in this course,                                         
 27     |  is you should save maybe 10% of your data and you use it as your testing set.    
 28     |  And that's what you use to actually tell you how much progress you're            
 29     |  making in terms of learning your patterns in your data.                          
 30     |  >> So, when you report the results to yourself and, and, and to your boss or     
 31     |  your client, use the tested result, because it's a much better,                  
 32     |  fair kind of understanding of how they are doing when you train them.            


##  24 - Unpacking NB Using Bayes Rule
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So you just built an interesting classifier.                                     
 2      |  And it worked!                                                                   
 3      |  But now we're going to go into some depth.                                       
 4      |  The next unit will be a little tedious.                                          
 5      |  And we're really going to dissect the little bit,                                
 6      |  [INAUDIBLE] bits of the algorithm.                                               
 7      |  But stick with us and you're going to learn a lot about Bayes Rule.              
 8      |  And then eventually Naive Base                                                   


##  25 - Bayes Rule
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So this unit is a tough one.                                                     
 2      |  We're going to talk about perhaps the holy grail of probabilistic inference,     
 3      |  that's called Bayes rule.                                                        
 4      |  Bayes rule is based on Reverend Thomas Bayes who used this principle to          
 5      |  infer the existence of god.                                                      
 6      |  But in doing so he created an entire new family of methods that has              
 7      |  vastly influenced artificial intelligence and statistics.                        
 8      |  So let's dive in.                                                                


##  26 - Cancer Test
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Let's use the cancer example from my last unit.                                  
 2      |  Say there's a specific cancer that occurs in one percent of the population.      
 3      |  And the test for this cancer.                                                    
 4      |  And with 90% chance that it's positive if you have this cancer C.                
 5      |  That's usually called the sensitivity But                                        
 6      |  the test sometimes is positive even if you don't have C.                         
 7      |  So let's say with another 90% chance it is negative if you don't have C.         
 8      |  This usually called the specitivity.                                             
 9      |  So here's my question.                                                           
 10     |  Without further symptoms you take the test, and the test comes back as positive. 
 11     |  What do you think is now the probability of having that specific type of cancer? 
 12     |  To answer this let's draw a diagram.                                             
 13     |  Suppose these are all the people and                                             
 14     |  some of them; exactly 1%, have cancer 99% is cancer free.                        
 15     |  We know there's a test that if you have cancer,                                  
 16     |  correctly it is diagnosed with a 90% chance.                                     
 17     |  So if we draw the area where the test is positive, cancer and                    
 18     |  test positive then this area over here is 90% of the cancer circle.              
 19     |  However that isn't the full truth.                                               
 20     |  The test sentenced is positive even if the person doesn't have cancer.           
 21     |  In fact, in our case that happened to be in 10% of all cases.                    
 22     |  So you have to add more area.                                                    
 23     |  It's as big as 10% of this large area.                                           
 24     |  It is as big as 10% of this large area where the test might go positive.         
 25     |  But the person doesn't have cancer.                                              
 26     |  So this blue area is 10% of all the area                                         
 27     |  over here minus the little small cancer circle.                                  
 28     |  And clearly all the area outside these circles corresponds to                    
 29     |  derivation of no cancer, and the test is negative.                               
 30     |  So let me ask you again.                                                         
 31     |  Suppose you have a positive test.                                                
 32     |  What do you think?                                                               
 33     |  Would the prior probability of cancer of 1%.                                     
 34     |  A sensitivity and specificity of 90%.                                            
 35     |  Do you think your new chances are now 90% or                                     
 36     |  8% or still just 1%?                                                             


##  27 - Cancer Test Solution
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And I would argue, it's about 8%.                                                
 2      |  In fact, as we'll see, it will come out at 8 1/3%, mathematically.               
 3      |  And the way to see this is this diagram is,                                      
 4      |  this is the region in which the test as positive.                                
 5      |  By having a positive test, you know you're in this region, and                   
 6      |  nothing else matters.                                                            
 7      |  You know you're in this circle.                                                  
 8      |  But within this circle, the ratio of the cancerous region,                       
 9      |  relative to the entire region, is still pretty small.                            
 10     |  It increased.                                                                    
 11     |  Obviously having a positive test, changes your cancer probability, but           
 12     |  it only increases by a factor of about eight.                                    
 13     |  As we'll see in a second.                                                        


##  28 - Prior and Posterior
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So this is the essence of Bayes' rule, which I'll give to you in a second.       
 2      |  There is some sort of a prior,                                                   
 3      |  by which we mean the probability before you run a test.                          
 4      |  And then you get some evidence from the test itself.                             
 5      |  And that all leads you to what's called a posterior probability.                 
 6      |  Now this is not really a plus operation.                                         
 7      |  In fact in reality it's more like a multiplication.                              
 8      |  But semantically what Bayes Rule does is it incorporates some evidence           
 9      |  from a test into your prior probability to arrive at a posterior probability.    
 10     |  So this makes this specific.                                                     
 11     |  In our cancer example we know that the prior probability of                      
 12     |  cancer is 0.01 which is the same as 1%.                                          
 13     |  The posterior of the probability of cancer given that our test says positive,    
 14     |  abbreviated here as positive,                                                    
 15     |  is the product of the prior times our test sensitivity.                          
 16     |  Which is, what are the chance of a positive result given that I have cancer.     
 17     |  And you might remember this one was 0.9, or 90%.                                 
 18     |  Now, just to warn you, this isn't quite correct.                                 
 19     |  To make this correct we also have to compute the posterior for                   
 20     |  the non-cancer option.                                                           
 21     |  Written here is not cancer, given a positive test.                               
 22     |  And that's using the prior.                                                      
 23     |  We know that P of Not C is 0.99.                                                 
 24     |  It's 1 minus P of C.                                                             
 25     |  Times the probability of getting a positive test result given Not C.             
 26     |  Realize these two equations are the same but exchange C for not C.               
 27     |  And this one over here takes a moment to compute.                                
 28     |  We know that our test gives us a negative result if it cancer free, 0.9 chance.  
 29     |  And as a result it gives us a positive result in                                 
 30     |  the cancer free case with 10% chance.                                            
 31     |  Now, what's interesting, is that this is about the correct equation.             
 32     |  Except the probabilities don't add up to 1.                                      
 33     |  To see, I'm going to ask you to compute those.                                   
 34     |  So please give us, give me the exact numbers, for                                
 35     |  the first expression, and the second expression, written over here.              
 36     |  Using our example up here.                                                       


##  29 - Prior and Posterior Solution
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Obviously, P of C is 0.01 times 0.9, is 0.009.                                   
 2      |  Whereas 0.99 times 0.1, this guy over here, is 0.099.                            
 3      |  What we've computed here is the absolute area in here.                           
 4      |  Which is 0.009.                                                                  
 5      |  And the absolute area in here, which is 0.099                                    


##  30 - Normalizing 1
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  The normalization proceeds in two steps.                                         
 2      |  We just normalize these guys to keep the ratio the same, but                     
 3      |  make sure they add up to 1.                                                      
 4      |  So let's first compute the sum of these two guys, please let me know what it is. 


##  31 - Normalizing 1 Solution
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And yes, the answer is 0.108.                                                    
 2      |  Technically what this really means is the probability of a positive test result, 
 3      |  that's the area in the circle that I just marked you.                            
 4      |  By virtue of what we learned last is just the sum of these two                   
 5      |  things over here which gives us 0.108.                                           


##  32 - Normalizing 2
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And now finally we come up with the extra posterior, or                          
 2      |  as this one over here is often called, the joint probability of two events.      
 3      |  And the posterior is obtained by dividing this guy over here                     
 4      |  with this nominizer.                                                             
 5      |  So, let's do this over here.                                                     
 6      |  Let's divide this guy over here.                                                 
 7      |  By this normalizer to get my posterior distribution, I think cancer,             
 8      |  given that I received the positive test results, so divide this number by this   


##  33 - Normalizing 2 Solution
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And we get 0.0833.                                                               


##  34 - Normalizing 3
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  As to another same for the then non cancer version pick the number over here     
 2      |  to divide and divide it by the same normalizer                                   


##  35 - Normalizing 3 Solution
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And the answer is 0.9167 approximately.                                          


##  36 - Total Probability
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Why don't you, for a second, add these two numbers, and give me the result.      


##  37 - Total Probability Solution
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And the answer is 1, as you would expect.                                        
 2      |  Now with this was really challenging, you can see a lot of math from this slide. 
 3      |  So let me just go over this again and make it much, much easier for you.         


##  38 - Bayes Rule Diagram
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  What we really said that we had a situation that prior                           
 2      |  a test is a certain sensitivity and a certain specificity.                       
 3      |  When you receive say a positive test result, what you do is you take your prior, 
 4      |  you multiply in the probability of this test result.                             
 5      |  Given C, and you multiply in the probability of the test result given not C.     
 6      |  So this is your branch for the consideration that you have cancer.               
 7      |  This is your branch for the consideration you have no cancer.                    
 8      |  When you're done with this, you arrive at a number that now combines the cancer  
 9      |  hypothesis with the test result.                                                 
 10     |  Both for the cancer hypothesis and the not cancer hypothesis.                    
 11     |  Now what you do, you add those up.                                               
 12     |  And they normally don't add up to one.                                           
 13     |  You get a certain quantity,                                                      
 14     |  which happens to be the total probability that the test is what it was.          
 15     |  This case positive.                                                              
 16     |  And all you do next is divide or                                                 
 17     |  normalize this thing over here by the sum over here.                             
 18     |  And the same on the right side.                                                  
 19     |  The divider is the same for                                                      
 20     |  both cases because this is your cancer range, your non cancer range.             
 21     |  But this guy doesn't rely on the cancer variable anymore.                        
 22     |  What you now get out is the desired posterior probability, and                   
 23     |  those add up to one if you did everything correct as shown over here.            
 24     |  This is your algorithm for Bayes Rule                                            


##  39 - Bayes Rule for Classification
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  It's great you learn about Bayes Rule.                                           
 2      |  And one of the things you use Bayes Rule a lot for is learning from documents,   
 3      |  or text learning.                                                                
 4      |  And the methods they'll tell you about is often called Naive Bayes.              
 5      |  It's actually a misnomer,                                                        
 6      |  it's not to be naive, not as in naive as Bayes Rule itself.                      
 7      |  But that's the name.                                                             
 8      |  Okay, so you're going to exercise this later in our practice exams using         
 9      |  Enron email data sets.                                                           
 10     |  But I give you the gist of it.                                                   
 11     |  Suppose we have two people, one is called Chris and one is called Sara.          
 12     |  And both people write a lot of email and for                                     
 13     |  simplicity I'll assume that these emails only contain three words, okay?         
 14     |  They contain the word love, the word deal, and the word life.                    
 15     |  Same is true about Sara.                                                         
 16     |  Obviously people use more than three words.                                      
 17     |  But this area here is a little bit small for 30,000 words.                       
 18     |  The difference of these two people Chris and                                     
 19     |  Sara is in the frequency at which they use those words.                          
 20     |  And just for simplicity let's say Chris loves talking about deals.               
 21     |  So 80% of his words or 0.8 are deal and he talks about life and                  
 22     |  love for a bit with 0.1 probability so                                           
 23     |  if Chris a word in email he's going to 80 percent of the time use the word       
 24     |  deal and ten percent of the time use the word love or life.                      
 25     |  Sara talks more about love, a little bit about deals, .2 and about life .3.      
 26     |  And again that's a simplified example.                                           
 27     |  What Naive Bayes allows you to do is to determine based on                       
 28     |  a random email who's the likely person who sent this email.                      
 29     |  Suppose says an email that goes as follows love life, and                        
 30     |  you don't know who sent it but you'd like to figure that out.                    
 31     |  Then you can do the space on base form and                                       
 32     |  suppose you leave a priori that it's 50% probability by Chris or by Sara.        
 33     |  So we'll say p of Chris equals 0.5.                                              
 34     |  That means the prior probability for                                             
 35     |  it being Chris is fifty percent and that immediately means,                      
 36     |  because it is one of the two, that the probability of Sara is also 0.5.          
 37     |  So if you look at this intuitively, who's more likely er,                        
 38     |  to have written this email?                                                      
 39     |  Chris or Sara?                                                                   
 40     |  Just check one box                                                               


##  40 - Bayes Rule for Classification
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And this is easy, Chris doesn't use the world love or life very much,            
 2      |  Sara uses it with much, much more frequencies, so you should have checked Sara   


##  41 - Chris or Sara
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  But suppose you see a different email.                                           
 2      |  I just made my life deal.                                                        
 3      |  Who will know Cris or Sara                                                       


##  42 - sol Chris or Sara
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And this one is actually not as easy to compute.                                 
 2      |  It's actually a close call, as you will see.                                     
 3      |  And we have to multiply out the numbers.                                         
 4      |  So Chris uses life with probability 0.1,                                         
 5      |  deal with 0.8, and our prior on Chris is 0.5.                                    
 6      |  When we multiply those out, we get 0.04.                                         
 7      |  Same for Sara.                                                                   
 8      |  Life is 0.3.                                                                     
 9      |  Deal is 0.2.                                                                     
 10     |  And our prior here is, again, 0.5.                                               
 11     |  When we multiply this one out, we get 0.03.                                      
 12     |  So the correct answer here would have been Chris by a really slim margin.        


##  43 - Posterior Probabilities
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  In the next exercise, I want you now to compute a posterior probability.         
 2      |  And, specifically, I want you to calculate the posterior probability of it       
 3      |  being Chris or Sara,                                                             
 4      |  given that we just observed the exact same phrase as before, life deal.          
 5      |  So just add the number into the box on the right side                            


##  44 - Posterior Probabilities
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And the answer is 0.57 over here and 0.43 over here.                             
 2      |  And the rationale is that the posteriors are normalized to 1.                    
 3      |  So we've taken 0.4, for example, and                                             
 4      |  dividing 0.04 by the total, which is 0.04 plus 0.03.                             
 5      |  When you work this out, it's the same as 4 divided by 7, or 0.57.                
 6      |  And when you divide 3 by 7, you get 0.43.                                        
 7      |  That's the correct posterior answer in this example.                             


##  45 - Bayesian Probabilities On Your Own
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Just to make sure we understood it,                                              
 2      |  let me change the text message from life deal to love deal.                      
 3      |  It's now your job to calculate these probabilities over here.                    


##  46 - Bayesian Probabilities On Your Own
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  To calculate this answer we multiply for Chris.                                  
 2      |  The LOVE and DEAL probability is .8 .1 just as before and                        
 3      |  multiply in the prior of .5.                                                     
 4      |  And product of the .1 times .8 times .5 is 0.04.                                 
 5      |  The math changes for SARA.                                                       
 6      |  She was as would LOVE with .5 probability.                                       
 7      |  DEAL with .2, and again our prior is 0.5.                                        
 8      |  This is 0.05.                                                                    
 9      |  Now, to normalize them to bring them into a form where they add up to 1,         
 10     |  we realize that the sum right now is 0.09.                                       
 11     |  So we have to divide 0.04 by 0.09 and that gives us 0.444.                       
 12     |  An approximation.                                                                
 13     |  And the 5 gives us 0.555.                                                        
 14     |  If we add them up you might get 0.99999 or 1.                                    


##  47 - Why Is Naive Bayes Naive
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So let me just explain to you why this is called Naive Bayes.                    
 2      |  What we've done is we've said there's unknown concepts.                          
 3      |  These are our target labels.                                                     
 4      |  Let's call them label A and label B.                                             
 5      |  And you don't get to see them.                                                   
 6      |  They're hidden.                                                                  
 7      |  As is always the case in, in supervised learning.                                
 8      |  And what you're going to see instead.                                            
 9      |  I think these things do.                                                         
 10     |  Like words they use.                                                             
 11     |  If they use them with exactly the same probability you                           
 12     |  could never figure out what it is.                                               
 13     |  If they use it with different probabilities and they might use one of them or    
 14     |  a 100 or a 1,000.                                                                
 15     |  But every word that you see like this one over here gives you                    
 16     |  evidence as to whether it was person A or person B.                              
 17     |  And what you do is, you just multiply all the evidences for every word you see.  
 18     |  And it's a big product.                                                          
 19     |  You do this for person A and for person B.                                       
 20     |  And you multiply in the prior and when this product comes out,                   
 21     |  it gives you the ratio of whether you believe it's person A or person B.         
 22     |  That is called Naive Bayes.                                                      
 23     |  It lets you identify from a text source whether this label is more likely or     
 24     |  this label is more likely.                                                       
 25     |  And you can do this with people, with news sources, you can                      
 26     |  ask the question was the text written by Shakespeare or by somebody else.        
 27     |  It's a very powerful tool, that's widely used all across machine learning.       
 28     |  And the reason why it's called Naive                                             
 29     |  is because it ignores one thing, and you tell me which one it is?                
 30     |  All the individual with words in the message,                                    
 31     |  the order of your words inside a message,.                                       
 32     |  Or the length of the message.                                                    
 33     |  Which one is being plainly ignored here?                                         


##  48 - Why Is Naive Bayes Naive
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And I'd say the best answer would have been word order because this              
 2      |  product doesn't consider the order in which the words occur.                     
 3      |  Whereas in the English language I                                                
 4      |  can tell you if you randomly re-order our words sentences don't make any sense.  
 5      |  This message doesn't pay attention to the word order.                            
 6      |  So it doesn't really understand the text it just looks at                        
 7      |  word frequencies as a way to do the classification.                              
 8      |  That's why it's called Naive.                                                    
 9      |  But it's good enough in many cases                                               


