#  Clustering Subtitles
##  01 - Unsupervised Learning
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So Katie, this is going to be a unit on unsupervised learning.                   
 2      |  >> Unsupervised learning is something that's very important,                     
 3      |  because most of the time, the data that you get in the real world doesn't have   
 4      |  little flags attached that tell you the correct answer.                          
 5      |  So what are you to do as a machine learner in that case?                         
 6      |  You turn to unsupervised techniques to still figure something out                
 7      |  about that data.                                                                 
 8      |  >> Okay, let's talk about them.                                                  
 9      |  Given a dataset without labels over all the data points are of the same class.   
 10     |  There are sometimes still things you can do to extract useful information.       
 11     |  Like this dataset over here, where I would say this dataset is structured in     
 12     |  a way that is useful to recognize for a machine learning algorithm.              
 13     |  >> When we look at this by eye, it looks like there's clumps or                  
 14     |  clusters in the data.                                                            
 15     |  And if we could identify those clumps or clusters, we could maybe say something  
 16     |  about a new, unknown data point and what its neighbors might be like.            
 17     |  >> Or here's a second example of data.                                           
 18     |  Maybe the data looks just like this.                                             
 19     |  There's something we can say here as well.                                       
 20     |  >> Right.                                                                        
 21     |  So all the data in this example looks like it lives on some kind of line or      
 22     |  some complicated shape that you seem to be drawing in there right now.           
 23     |  >> Yeah. And it's, it's, it's used to be a two-dimensional space, with x and     
 24     |  y over here.                                                                     
 25     |  But some of it we can reduce it to a one-dimensional line.                       
 26     |  So that's called what?                                                           
 27     |  >> That's called dimensionality reduction, usually.                              
 28     |  >> Dimensionality reduction.                                                     
 29     |  So we learned about, a little bit about clustering.                              
 30     |  >> Clustering is what we'll learn in this lesson.                                
 31     |  >> And you can see here an example of something also called unsupervised         
 32     |  learning of dimensionality reduction.                                            
 33     |  >> Which we will get in a future lesson.                                         
 34     |  >> So these kind of things where you find structure in the data without labels,  
 35     |  they're called unsupervised learning.                                            
 36     |  And we're now gong to dive into the wonderful,                                   
 37     |  wonderful magical land of unsupervised learning.                                 
 38     |  >> Sounds great, let's dive in.                                                  


##  02 - Clustering Movies
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So here's an example that should make it intuitively clear the clustering sum    
 2      |  doesn't make sense.                                                              
 3      |  So take Katie and me, we both have a movie collection at home.                   
 4      |  And just imagine that both of us look at each other's movies, and all movies,    
 5      |  and Katie gets to rank them from really, really bad to great.                    
 6      |  And I to get to rank the same movies from bad to great.                          
 7      |  Now it so turns out that Katie and I have very different tastes.                 
 8      |  Maybe some movies that I love, like all my James Bond movies, but                
 9      |  Katie doesn't like as much.                                                      
 10     |  And there's others or these chick flicks, that Katie loves, and I don't.         
 11     |  So somewhat exaggerated.                                                         
 12     |  It mind end up, that our movies fall into different classes,                     
 13     |  depending on who likes which movies.                                             
 14     |  So say, say you're Netflix, and                                                  
 15     |  and you look at both my queue and Katie's queue, and you graph it like that.     
 16     |  Then you can conclude, wow, there's two different classes of movies.             
 17     |  Without knowing anything else about movies,                                      
 18     |  you would say, here's class A and class B.                                       
 19     |  And they're very different in characteristics.                                   
 20     |  And the reason why Netflix might want to know this is next time Katie comes in,  
 21     |  you want to kind of propose a movie that fits into class B and on to class A.    
 22     |  Otherwise, she's very unlikely to watch this movie.                              
 23     |  And conversely, for me, you want a reach into class A versus class B.            
 24     |  In fact, if you were to look at those movies,                                    
 25     |  you might find that old style westerns are right over here.                      
 26     |  And modern chick flicks might be sitting over here.                              
 27     |  Who knows?                                                                       
 28     |  But that's an example of clustering.                                             
 29     |  Because here, there's no target labels given.                                    
 30     |  Then they move down for you if class A and B existed.                            
 31     |  But after looking at the data, you could,                                        
 32     |  through clustering, deduce as two different classes, and you could even look     
 33     |  a the movie titles to understand what these classes are all about.               


##  03 - How Many Clusters
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  The perhaps the most basic algorithm for clustering, and                         
 2      |  by far the most used is called K-MEANS.                                          
 3      |  And I'm going to work with you through the algorithm with many,                  
 4      |  many quizzes for you.                                                            
 5      |  Here is our data space.                                                          
 6      |  And suppose we are given this type of data.                                      
 7      |  The first question is intuitively, how many clusters do you see?                 
 8      |  Truth telling, there is not a unique answer, it could be seven it could be one,  
 9      |  but give me the answer that seems to make the most sense                         


##  04 - How Many Clusters
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay, and I would argue it's 2.                                                  
 2      |  There's a cluster over here.                                                     
 3      |  And a cluster over here.                                                         
 4      |  And the cluster centers respectively lie right over here and                     
 5      |  somewhere over here.                                                             
 6      |  So that's the place we would like to find to characterize the data.              


##  05 - Match Points with Clusters
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  In k-means, you randomly draw cluster centers and                                
 2      |  say our first initial guess is, say, over here and over here.                    
 3      |  These are obviously not the correct cluster centers.                             
 4      |  You're not done yet.                                                             
 5      |  But k-means now operates in two steps.                                           
 6      |  Step number is assign and step number two is optimize.                           
 7      |  So let's talk about the assignment.                                              
 8      |  For classes in number one, I want you to click on exactly those of               
 9      |  the red points that you believe are closer to center one than center two.        


##  06 - Match Points with Clusters
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And the answer is this guy is closer these guys over her are closer.             
 2      |  And the way to see this is you can make a line between the cluster centers and   
 3      |  then draw an equidistant and orthogonal line and that                            
 4      |  line separate the space into a half space that's closer to center number one,    
 5      |  which is the one over here, and a half space that's closer to center number two, 
 6      |  which is the space over here.                                                    


##  07 - Optimizing Centers Rubber Bands
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So now we know that these four points correspond to                              
 2      |  the present classes in the one that was randomly chosen.                         
 3      |  And these three points over here correspond to classes in the middle.            
 4      |  That's the assignment step.                                                      
 5      |  obviously that's not good enough.                                                
 6      |  Now we have to optimize.                                                         
 7      |  And what we are optimizing is, you are minimizing the total quadratic distance.  
 8      |  Of our cluster center to the points.                                             
 9      |  We're now free to move our cluster center.                                       
 10     |  I think of these little blue lines over here as rubber bands, and                
 11     |  that we're trying to find the state of minimum energy for                        
 12     |  the rubber bands, where the total kinetic error is minimized.                    
 13     |  And for the top one, I'm going to give you three positions.                      
 14     |  They're all approximate, but                                                     
 15     |  pick the one that looks best in terms of minimization.                           
 16     |  And that's a not a trivial question at all.                                      
 17     |  So one could be right over here, one could be at and                             
 18     |  one could be right over here.                                                    
 19     |  Which one do you think best minimize, or is minimize of the three positions,     
 20     |  the total quadratic length of these rubber bands?                                


##  08 - Optimizing Centers Quiz
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So after the assign step, you can now see these little blue lines over           
 2      |  here that marry data points to cluster centers.                                  
 3      |  And now we're going to think of what this rubber bands.                          
 4      |  They're rubber bands that like to be as short as possible.                       
 5      |  In the optimize step, we're not allowed, now allowed to move the green cluster   
 6      |  center to a point where the total of our band is minimized.                      


##  09 - Moving Centers 2
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Same exercise for the optimization step for the center below.                    
 2      |  I give you a couple of hypotheses, four in total.                                
 3      |  Pick the one that minimizes the total bubble length should be easy now           


##  10 - Moving Centers 2
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And then argue this is the one that minimizes it.                                
 2      |  In fact, a set of summary over here minimizes the total of                       
 3      |  events in the bottom case.                                                       
 4      |  And we can argue where exactly it falls, but you get the principle               


##  11 - Match Points again
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So, let's do it again now.                                                       
 2      |  With these new cluster centers, pick the one up here and                         
 3      |  click on all of the seven data points that you now believe will be assigned for  
 4      |  the cluster center on the left                                                   


##  12 - Match Points again
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And this example is now easy.                                                    
 2      |  You can see that all the four over here fit with the green one.                  
 3      |  In fact, the separating line will be somewhere here and, in fact,                
 4      |  after the next iteration of optimize, with the assignment of those point, four   
 5      |  points of this cluster center and those three points of this cluster center.     
 6      |  You can see that this cluster center will move                                   
 7      |  straight into the center of those four points.                                   
 8      |  And this cluster center will move to the center of those three points.           
 9      |  Have we truly achieved our result?                                               
 10     |  We now have assumed it's two clusters.                                           
 11     |  But our algorithm of iteratively assigning and                                   
 12     |  optimizing has moved the cluster center straight into what we                    
 13     |  would argue is actually the correct centroid for those two clusters over here.   
 14     |  That is called the k-Means algorithm.                                            


##  13 - Handoff to Katie
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So you learn about k-means.                                                      
 2      |  Katie is going to give you one more example of how to apply k-means in practice. 


##  14 - K-Means Clustering Visualization
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Now I want to show you a visualization tool that I found online that I           
 2      |  think does a really great job of helping you see what k-means clustering does.   
 3      |  And that should give you a good intuition for how it works.                      
 4      |  So I'd like to give a special shout out to Naftali Harris,                       
 5      |  who wrote this visualization and very kindly agreed to let us use it.            
 6      |  I'll put a link to this website in the instructor notes that you can go and      
 7      |  play around with it on your own.                                                 
 8      |  So it starts out by asking me how to pick the initial centroids of my clusters.  
 9      |  I'll start out with Randomly right now.                                          
 10     |  What kind of data would I like to use?                                           
 11     |  There are a number of different things here, and                                 
 12     |  I encourage you to play around with them.                                        
 13     |  A Gaussian Mixture has been really similar to one of the simple examples we've   
 14     |  done so far.                                                                     
 15     |  So Gaussian mixture data looks like this.                                        
 16     |  These are all the points that we have to classify.                               
 17     |  The first question for you is,                                                   
 18     |  how many centroids do you think is the correct number of centroids on this data? 


##  15 - K-Means Clustering Visualization
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And I hope you said three,                                                       
 2      |  it's pretty obvious that there should be three centroids here.                   
 3      |  So let's add three, one, two, three.                                             
 4      |  So they're all starting out right next to each other, but                        
 5      |  we'll see how as the algorithm progresses, they end up in the right place.       


##  16 - K-Means Clustering Visualization 2
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  One of the things that's immediately apparent once I start assigning my          
 2      |  centroids, with these colored regions, is how all the points are going to        
 3      |  be associated with one of the centroids, with one of the clusters.               
 4      |  So you can see that the blue is probably already in reasonably good shape.       
 5      |  I would say that we got a little bit lucky in where the,                         
 6      |  the initial centroid was placed.                                                 
 7      |  It looks like it's pretty close to the, the center of this blob of data.         
 8      |  With the red and the green it looks like they're sitting kind of right on top of 
 9      |  each other in the same cluster.                                                  
 10     |  So, let's watch as K-means starts to sort out this situation and                 
 11     |  get all the clusters properly allocated.                                         
 12     |  So, I hit Go.                                                                    
 13     |  The first thing that it does is it tells me explicitly which cluster each one of 
 14     |  these points will fall into.                                                     
 15     |  So you see, we have a few blue that fall into the wrong cluster over here.       
 16     |  And then, of course, the red and the green.                                      
 17     |  So this is the association step is all the points are being associated with      
 18     |  the nearest centroid.                                                            
 19     |  And then the next thing that I'll do is I'm going to update the centroid.        
 20     |  So now, this is going to move the centroids to the,                              
 21     |  the mean of all of the associated points.                                        
 22     |  So in particular, I, I expect this green point to be                             
 23     |  pulled over to the right by the fact that we have so many points over here.      
 24     |  So let's update.                                                                 
 25     |  Now this is starting to look much better.                                        
 26     |  If we were to just leave everything as is,                                       
 27     |  you can see how the clustering was before.                                       
 28     |  So now all these points that use to be green are now about to become red.        
 29     |  And likewise with a few blue points over here.                                   
 30     |  You can see how even just in one step from this bad initial condition,           
 31     |  we've already started to capture the structure in the data pretty well.          
 32     |  So I'm going to reassign the points.                                             
 33     |  Iterate through this again to reassign each point to the nearest centroid.       
 34     |  And now things are starting to look very, very consistent.                       
 35     |  There's probably just one, one or                                                
 36     |  two more iterations before we have the centroid's right at the middle of         
 37     |  the clusters so I update and reassign points.                                    
 38     |  No points have changed so                                                        
 39     |  this is the final clustering that would be assigned by k-means clustering.       
 40     |  So in three or four steps, using this algorithm, I assigned every point to       
 41     |  a cluster and it worked in a really beautiful way for this example.              


##  17 - K-Means Clustering Visualization 3
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Now I'm going to show you another set of data that won't work out quite so       
 2      |  perfectly, but you can see how k-means clustering is still.                      
 3      |  And the type of data that I'll use in this example is uniform points.            
 4      |  This is what uniform points look like.                                           
 5      |  It's just scattered everywhere.                                                  
 6      |  So I wouldn't look at this and say there's clear clusters in here that I want to 
 7      |  pick out, but I might still want to be able to describe that, say, these points  
 8      |  over here are all more similar to each other than these points over there.       
 9      |  And k-means clustering could be one way of mathematically describing that,       
 10     |  that fact about the data.                                                        
 11     |  So I don't a priori have a number of centroids that I know I want to use here,   
 12     |  so I'll use two.                                                                 
 13     |  Seems like a reasonable number.                                                  
 14     |  One, two.                                                                        
 15     |  And then let's see what happens in this case.                                    
 16     |  Few points are going to be reassigned.                                           
 17     |  Move the centroids.                                                              
 18     |  If you can see that there's a few more little adjustments here.                  
 19     |  But in the end, it basically just ends up splitting the data along this axis.    
 20     |  If I try this again, depending on the exact initial conditions that I have and   
 21     |  the exact details of how these points are allocated,                             
 22     |  I can come up with something that looks a little bit different.                  
 23     |  So you can see here that I                                                       
 24     |  ended up splitting the data vertically rather than horizontally.                 
 25     |  And the way you should think about this is the initial placement of              
 26     |  the centroids is usually pretty random and very important.                       
 27     |  And so depending on what exactly the initial conditions are,                     
 28     |  you can get clustering in the end that looks totally different.                  
 29     |  Now, this might seem like a big problem, but                                     
 30     |  there is one pretty powerful way to solve it.                                    
 31     |  So let's talk about that.                                                        


##  18 - Sklearn
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Now that I've explained the theory of k-means clustering to you,                 
 2      |  I'm going to show you how to use the scikit-learn implementation to deploy it    
 3      |  in your own studies.                                                             
 4      |  So I start over here at Google, and                                              
 5      |  I find that there's a whole page on clustering in scikit-learn.                  
 6      |  The first thing that I notice when I get to this page is                         
 7      |  that there are many types of clustering, besides just k-means clustering.        
 8      |  So all of these different columns right here are different types of clustering.  
 9      |  We won't go into all of these, instead I want to use this page to navigate to    
 10     |  the k-means documentation that you can get a little bit of a better idea of      
 11     |  how this is handled in scikit-learn.                                             
 12     |  So here's a list of all of the different clustering methods that I have.         
 13     |  And here the first item on the list we see is k-means, and                       
 14     |  some summary information about the algorithm.                                    
 15     |  And so one of the parameters that you have to define for                         
 16     |  k-means is the number of clusters.                                               
 17     |  Remember, we had to say at the outset how many clusters we want to look for and  
 18     |  this is one of the things that can be most challenging actually about using      
 19     |  k-means is deciding how many clusters you want to try.                           
 20     |  Then he gives us some information about the scalability, which basically tells   
 21     |  us how the algorithm performs as you start to have lots and                      
 22     |  lots of data, or lots of clusters.                                               
 23     |  A use case, which gives us a little bit of information that this is good for     
 24     |  general purpose when you have clusters that have even number of                  
 25     |  points in them and so on.                                                        
 26     |  And, last, that the way that k-means clustering works is based on                
 27     |  the distances between the points.                                                
 28     |  So, very consistent with what we've seen so far.                                 
 29     |  Let's dig in a little bit deeper.                                                
 30     |  Now we're at the k-means documentation page.                                     
 31     |  And there are three parameters in particular that I want to call your            
 32     |  attention do.                                                                    
 33     |  First and most important one is n_clusters.                                      
 34     |  The default value for n_clusters is eight.                                       
 35     |  But of course we know that the number of clusters in the algorithm is something  
 36     |  that you need to set on your own based on what you think makes sense.            
 37     |  This might even be a parameter that you play around with.                        
 38     |  So you should always be thinking about whether you actually want to              
 39     |  use this default value, or if you want to change it to something else.           
 40     |  I can guarantee you that you're mostly going to want to change it to             
 41     |  something else.                                                                  
 42     |  The second parameter that I want to call your attention to is max_iter=300.      
 43     |  Remember that when we're running k-means clustering we                           
 44     |  have an iteration that we go through as we're finding the clusters,              
 45     |  where we assign each point to a centroid and then we move the centroid.          
 46     |  Then we assign the points again.                                                 
 47     |  We move the centroids again.                                                     
 48     |  And each one of those assign and move, assign and                                
 49     |  move steps is an iteration of the algorithm.                                     
 50     |  And so max_iter actually says how many iterations of                             
 51     |  the algorithm do you want it to go through.                                      
 52     |  300 will usually be a very reasonable value for you.                             
 53     |  In fact most of the time I would guess that it's going to                        
 54     |  terminate before it gets to this maximum number.                                 
 55     |  But if you want to have a finer level of control over the algorithm and          
 56     |  how many times it goes through that iteration process this is                    
 57     |  the parameter that you want.                                                     
 58     |  And then the last parameter that I'll mention,                                   
 59     |  another one that's very important.                                               
 60     |  Is the number of different initializations that you give it.                     
 61     |  Remember we said that k-means clustering has this challenge,                     
 62     |  that depending on exactly what the initial conditions are,                       
 63     |  you can sometimes end up with different clusterings.                             
 64     |  And so then you want to repeat the algorithm several times so                    
 65     |  that any one of those clusterings might be wrong, but in general,                
 66     |  the ensemble of all the clusterings will give you something that makes sense.    
 67     |  That's what this parameter controls.                                             
 68     |  It's basically how many times does it initialize the algorithm,                  
 69     |  how many times does it come up with clusters.                                    
 70     |  You can see that by default it goes through at ten times.                        
 71     |  If you think for some reason that your clustering might be particularly prone to 
 72     |  bad initializations or                                                           
 73     |  challenging initializations, then this is the parameter that you want to change. 
 74     |  Maybe bump the number of initializations up to a higher number.                  
 75     |  But again, just to reiterate, of all those parameters,                           
 76     |  number of clusters is definitely the one that's most important.                  
 77     |  And that you should be playing around with and                                   
 78     |  thinking really hard about the most.                                             


##  19 - Some challenges of k-means
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Now this wraps up what we're going to talk about in                              
 2      |  terms of the k-means algorithm.                                                  
 3      |  What I'll have you do is practice much more in the coding aspects of             
 4      |  this in the mini project.                                                        
 5      |  But before we do that,                                                           
 6      |  here are few thoughts on things that k-means is very valuable for                
 7      |  and a few places where you need to be careful if you're going to try to use it.  


##  20 - Limitations of K-Means Quiz
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So now we look at the limits of what k-means can or                              
 2      |  cannot do, and you're going to try to break it.                                  
 3      |  And specifically, talk about local minima and to do this, I want to ask you      
 4      |  a question that you can think about and see if you get the answer right.         
 5      |  Suppose you use a fixed number of cluster centers, two or three or four.         
 6      |  Will the output for any fixed training set, always be the same?                  
 7      |  So given a fixed data set, given a fixed number of cluster centers,              
 8      |  when you run k-means will you always arrive at the same result?                  
 9      |  Take your best guess.                                                            


##  21 - Limitations of K-Means Solution
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And the answer is no, as I will illustrate to you.                               
 2      |  K-means is what's called a hill climbing algorithm, and                          
 3      |  as a result it's very dependent on where you put your initial cluster centers.   


##  22 - Counterintuitive Clusters
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So let's make another data set.                                                  
 2      |  In this case, you're going to pick three cluster centers and,                    
 3      |  then, conveniently, we'll draw three clusters onto my diagram.                   
 4      |  Obviously, for three cluster centers, you want a cluster to be here, right here, 
 5      |  and right over here.                                                             
 6      |  So my question is, is it possible that all these data                            
 7      |  points over here are represented by one cluster, and                             
 8      |  these guys over here by two separate clusters.                                   
 9      |  Given what you know about k-means, do you think it can happen                    
 10     |  that all these points here fall into one cluster and those two                   
 11     |  fall into two clusters as one what's called a local minimum for clustering.      


##  23 - Counterintuitive Clusters Solution
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And the answer is positive, and I prove it to you.                               
 2      |  Suppose you put one cluster center right between those two points over here and  
 3      |  the other two somewhere in here.                                                 
 4      |  It doesn't even have an error.                                                   
 5      |  In your assignment step, you will find that pretty much everything left of       
 6      |  this line would be allocated to the left cluster center.                         
 7      |  And as a result,                                                                 
 8      |  this is the point where the total rubber band distance is minimized.             
 9      |  So this cluster is very stable.                                                  
 10     |  These two guys over here,                                                        
 11     |  however, separate between themselves the data on the right.                      
 12     |  And they will fight for the same data points and                                 
 13     |  end up somewhere partitioning the cloud on the right side.                       
 14     |  And that is a stable solution because in the assignment step, nothing changes.   
 15     |  This guy will still correspond to all the guys over here, and                    
 16     |  these guys will correspond to the guys over here.                                
 17     |  That's called a local minimum.                                                   
 18     |  And it really depends on the initialization of the cluster centers.              
 19     |  If you had chosen these three cluster centers as your initial guesses,           
 20     |  you would never move away from it.                                               
 21     |  Thus, make sure it's really important in clustering to be aware of               
 22     |  the fact it's a local here climbing algorithm.                                   
 23     |  And it can give you suboptimal solutions that, if you divide them again,         
 24     |  it gives you a better solution.                                                  
 25     |  Obviously, in this case with three cluster centers,                              
 26     |  you want them over here, over here and just one on the right side over here.     


##  24 - Counterintuitive Clusters
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Let me give another example and ask you a quiz.                                  
 2      |  Suppose we have data just like this over here.                                   
 3      |  Do you think there could be a local minimum if you                               
 4      |  initialize this data set with two cluster centers?                               
 5      |  Is there a stable solution where which the two cluster would not end up          
 6      |  one over here and one over here?                                                 
 7      |  Or put differently, is there, does there exist a bad local minimum?              
 8      |  Yes or no?                                                                       


##  25 - Counterintuitive Clusters
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And I would say the answer's yes.                                                
 2      |  You could make it so that the cluster centers sit right on top of each other,    
 3      |  and the separation line looks like this.                                         
 4      |  And all the top points are associated to the top cluster center,                 
 5      |  and all the bottom points are associated to the bottom cluster center.           
 6      |  Granted, it's unlikely, to have init-,                                           
 7      |  ,initialization like this, but                                                   
 8      |  if it happens, then the algorithm would believe this is one cluster.             
 9      |  And this is another cluster.                                                     
 10     |  If we re-run it and you initialize differently.                                  
 11     |  Say one of the cluster centers sits over here.                                   
 12     |  Then a separation line will fall like that.                                      
 13     |  And the classes would automatically resolve themselves.                          
 14     |  It's unlikely, but there exists a bad local minimum,                             
 15     |  even in the example I showed you over here.                                      
 16     |  Now as a rule of thumb,                                                          
 17     |  the more cluster centers you have, the more local minima you find.               
 18     |  But they exist, as a result, you are forced to run the algorithm multiple times. 


