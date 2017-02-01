#  Ensemble B&B Subtitles
##  01 - Ensemble Learning Boosting
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Hey Charles, how's it goin'?                                                     
 2      |  >> It's going pretty well Michael. How's it going with you?                      
 3      |  >> Good, thank you.                                                              
 4      |  >> Good, good, good. Guess what we're going to talk about today?                 
 5      |  >> Well, reading off this screen, it looks                                       
 6      |  like maybe ensemble learning, and boosting, whatever that is.                    
 7      |  >> Yes, that's exactly what we're                                                
 8      |  going to talk about. We're going to talk about                                   
 9      |  a class of algorithms called ensemble learners. And I think you will See         
 10     |  that they're related to some of the stuff that we've been doing already,         
 11     |  and in particular we're going to spend most of our time focusing on, boosting.   
 12     |  because boosting is my favorite of the                                           
 13     |  ensemble learning algorithms. So you ready for that?                             
 14     |  >> Yeah! Let's do it.                                                            
 15     |  >> Okay. So, I want to start this out by,                                        
 16     |  going through a little exercise with you. I want you                             
 17     |  to think about a problem. Okay. And the particular                               
 18     |  problem I want you to think about is, spam email.                                
 19     |  >> Mm, I think about that a lot.                                                 
 20     |  >> So, normally if we were thinking of this a classification                     
 21     |  task, right, where we're going to take some email and we're going to decide      
 22     |  if it's spam or not. Given what we've talked about so                            
 23     |  far we would be thinking about using a decision tree or                          
 24     |  you know neural networks or k and n whatever that means                          
 25     |  with email. We would be coming up with all of these sort                         
 26     |  of complicated things. I want to propose an alternative which is                 
 27     |  going to get us to ensemble learn. OK and here's the alternative.                
 28     |  I don't want you to try to think of some complicated                             
 29     |  Rule that you might come up with that would capture spam email.                  
 30     |  Instead, I want you to come up with some simple rules                            
 31     |  that are indicative of spam email. Okay, so let me be                            
 32     |  specific, Michael. We have this problem with spam email. That is,                
 33     |  you you're going to get some email message and you want some computer            
 34     |  program To figure out automatically for you if something is a                    
 35     |  piece of spam or it isn't. And I want you to help                                
 36     |  write a set of rules that'll help me to figure that                              
 37     |  out. And I want you to think about simple rules, so can                          
 38     |  you think of any simple rules that might indicate that something is spam?        
 39     |  >> Alright I can, yeah I can think of some simple rules. I don't think           
 40     |  they would be very good, but they might better than nothing. Like If for example 
 41     |  it mentions how manly I am, I, I would be, be willing to believe that            
 42     |  was a spam message. So like if the body of the message contains the word manly.  
 43     |  >> Okay, I like that. like that when body                                        
 44     |  contains manly.                                                                  
 45     |  I like that rule, because I often get non-spam messages talking about            
 46     |  manly. So I guess one man's spam is another man's normal email.                  
 47     |  >> [LAUGH] I guess that's true.                                                  
 48     |  >> Probably. Any other rules?                                                    
 49     |  >> Sure if it, you know if it comes from my spouse it's probably not spam.       
 50     |  >> OK, so let's see, from spouse.                                                
 51     |  >> Her name's Lisa. Now we're going to call our spouse. So                       
 52     |  let's say minus, I'm going to go to plus here, so we know                        
 53     |  some rules are indicitive of being spam, and some                                
 54     |  rules are indicitive of not being spam. Okay, anything else?                     
 55     |  >> Possibly the length of the message. I guess. Like what?                       
 56     |  >> I don't know. I don't know that this would be very                            
 57     |  accurate, but I think some of this, some of the spam I                           
 58     |  get sometimes is very, very short just like the, it's like the                   
 59     |  URL. Like hey, check out this site, and then there's a URL.                      
 60     |  >> Hm, I like that. So, we'll just say short.                                    
 61     |  Just contains URLs. Hm, I like those rules. Let's see if we can                  
 62     |  think of anything else. Oh, how about this one. It's just an image.              
 63     |  >> Hm.                                                                           
 64     |  >> I get a lot of those where it's just an image.                                
 65     |  >> I see, like in it's it's and if you                                           
 66     |  look at the picture it's all various pharmaceuticals from Canada.                
 67     |  >> Exactly. Here's one I get a lot.                                              
 68     |  >> Hm,                                                                           
 69     |  >> Lots of misspelled words that you end up reading as being                     
 70     |  a real word.                                                                     
 71     |  >> Hm. But I don't know how I'd write that                                       
 72     |  as a rule. Or you could just list the words.                                     
 73     |  >> Like rules that, words that have already                                      
 74     |  been modified in that way. I guess so.                                           
 75     |  >> Yeah, kind of a, kind of a black list, a black list of words.                 
 76     |  >> Okay so, words like, I would say manly, but you were saying prawn.            
 77     |  >> Or whatever that says. yeah, so they're and they're tons                      
 78     |  of these. Right? I mean, another one that's, that's very popular                 
 79     |  if you're old enough anyway is this one, remember this one?                      
 80     |  >> Oh, sure that was sometimes a virus, right?                                   
 81     |  >> Yes. Our young, our younger viewers will not know this but this was one       
 82     |  of the first big spam messages that would                                        
 83     |  get out there. Make money fast. And there's                                      
 84     |  tons and tons of these. We could come up with a bunch of them. Now, here's       
 85     |  something they all kind of have in common,                                       
 86     |  Michael, and you've touched on this all ready.                                   
 87     |  All of them are sort of right. They're useful but no one of them is going to be  
 88     |  very good at telling us whether a message has                                    
 89     |  spam on its own. Right. So the word manly is                                     
 90     |  evidence but it's not enough to decide whether something                         
 91     |  is spam or not. It's from your spouse, it's evidence                             
 92     |  it's not spam, but sometimes you get messages from                               
 93     |  your spouse that are in fact spam, because in fact,                              
 94     |  she didn't actually send them. You know, and so                                  
 95     |  on and so forth. And sometimes she did email                                     
 96     |  from Princes in Nigeria. I didn't. And they're not                               
 97     |  always spam. I, I actually do, but any case,                                     
 98     |  sometimes people are asking you for money, and maybe                             
 99     |  that's message you want to ignore, but it isn't                                  
 100    |  necessarily spam. And some people are very interested in                         
 101    |  getting like this and don't consider it spam, right?                             
 102    |  >> So, so, okay, so I can see that these would                                   
 103    |  all maybe provide some evidence, but it seems really hard tp figure out the      
 104    |  right way of combining them all together to I don't know, make a decision.       
 105    |  >> Right, this is exactly right. And by the                                      
 106    |  way, if you think about something like decision tree, you                        
 107    |  could. There's really a sort of similar problem going on                         
 108    |  there. We can think of each of the nodes in                                      
 109    |  a decision tree as being a very simple rule and                                  
 110    |  the decision tree tells us how to combine them. Right?                           
 111    |  So, we need to figure out how to do that                                         
 112    |  here and that is the fundamental notion of ensemble learning.                    
 113    |  >> But wait, isn't, couldn't you also do something similar with                  
 114    |  something like neural net. Right? Where each of these now becomes a              
 115    |  feature and we're just trying to learn ways for combining them                   
 116    |  all together. So That would kind of satisfy what you were talking about.         
 117    |  >> True, I mean I think the the difference here in this case and                 
 118    |  and I think you're absolutely right but                                          
 119    |  one difference here is that typically with the                                   
 120    |  new network we've already built the network                                      
 121    |  itself and the nodes and we're trying                                            
 122    |  to learn the weights whereas in something                                        
 123    |  like a decision tree you're building up rules                                    
 124    |  as you go along. And typically with ensemble learning you're building up a       
 125    |  bunch of rules and combining them together until you got something that's good   
 126    |  enough. But you're absolutely right. You                                         
 127    |  could think of [UNKNOWN] networks as being                                       
 128    |  an ensemble of little parts. Sometimes                                           
 129    |  hard to understand, but an ensemble nonetheless.                                 


##  02 - Ensemble Learning Simple Rules
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So, the characteristic of ensemble learning is first this, that                  
 2      |  you take a bunch of simple rules, all of which kind                              
 3      |  of make sense and you can see as sort of helping.                                
 4      |  But on their own, individually, do not give you a good                           
 5      |  answer. And then you magically combine them in some way to                       
 6      |  create a more complex rule, that in fact, works really well.                     
 7      |  And ensemble learning algorithms have a sort of basic form to                    
 8      |  them, that can be described in just one or two lines.                            
 9      |  So let me do that and then we can start wondering a little bit                   
 10     |  how we're going to make that real. So here's the basic form of an ensemble       
 11     |  learning algorithm. Basically you learn over a                                   
 12     |  subset of the data, and that generates                                           
 13     |  some kind of a rule. And then you learn over another subset of the data          
 14     |  and that generates a different rule. And then you learn over another subset of   
 15     |  the data and that generates yet a third rule, and yet a fourth rule, and         
 16     |  yet a fifth rule, and so on and so forth. And then eventually you                
 17     |  take all of those rules and you combine them into one of these complex rules.    
 18     |  So, we might imagine in the email case that I might                              
 19     |  look at a small subset of email that I know is already                           
 20     |  spam and discover that the word manly shows up in all of                         
 21     |  them and therefore pick that up as a rule. That's going to be                    
 22     |  good at that subset of mail, but not necessarily be good                         
 23     |  at the other subset of mail. And do the same thing and                           
 24     |  discover that a lot of the spam mails are in fact short                          
 25     |  or a lot of them are just images or just urls and                                
 26     |  so on and so forth. And that's how I                                             
 27     |  learn these rules by looking at different subsets. Which                         
 28     |  is why you end up with rules that are very good at a small set of the data, but  
 29     |  aren't necessarily good at a large set of the                                    
 30     |  data. And then after you've collected these rules, you combine                   
 31     |  them in some way, and there you go. And                                          
 32     |  that's really the beginning and the end of ensemble learning.                    
 33     |  >> So wait. So, when you say manly was in a lot of the positive                  
 34     |  examples. Do you mean like it distinguishes the                                  
 35     |  positive and the negative example? So it should                                  
 36     |  also not be in the negative examples.                                            
 37     |  >> That's right. That's exactly right. So think of                               
 38     |  this as any other classification learning problem that you                       
 39     |  would have where you're trying to come up with                                   
 40     |  some way to distinguish between the positives and the negatives.                 
 41     |  >> And, and now why does it, why are we are looking at subsets of                
 42     |  the data? I don't understand why we can't just look at all, the whole data.      
 43     |  >> Well, if we look at all of the data,                                          
 44     |  then it's going to be hard to come up with these, these                          
 45     |  simple rules. That's the basic answer. Actually, ask me that                     
 46     |  question a little bit later, when we talk about over fitting,                    
 47     |  and I think I'll have a good answer for you. Okay,                               
 48     |  so here we go Michael. This is Ensemble Learning. You learn                      
 49     |  over a subset of the data over and over again picking                            
 50     |  up new rules and then you combine them and you're done.                          


##  03 - Ensemble Learning Algorithm
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Here's the Ensemble Learning algorithm. We're done,                              
 2      |  Michael, we're done with the entire lesson.                                      
 3      |  We don't have to do anything else anymore. We know that we're supposed to        
 4      |  look over subset of data, pick up rules, and then combine them. So, what         
 5      |  else do you need to know in                                                      
 6      |  order to write your first Ensemble Learning algorithm?                           
 7      |  >> So, I'm already kind of uncomfortable with this notion of"                    
 8      |  combine," right? So, like, I can think of lots of really dumb                    
 9      |  ways to combine things. Like, choose one at random or, you                       
 10     |  know, I don't know, add em all up and divide by p                                
 11     |  ,i I mean so,so presumably there's gotta be                                      
 12     |  some intelligence in how this combination is taking place                        
 13     |  >> Yes, you would think so, but your not                                         
 14     |  at all bothered about how you pick a subset?                                     
 15     |  >> Oh ,I was imaging you meant random subsets.                                   
 16     |  >> Oh ,so you'd automated assumption about how we were going to                  
 17     |  pick a subset. You just [CROSSTALK] werent sure how to combine them. Well        
 18     |  actually lets explore that for a minute. Here's kind of the dumbest              
 19     |  thing you can imagine doing. That turns out to work out pretty well.             
 20     |  We're going to pick subsets, by, I'm going to say uniformly. Just to             
 21     |  be specific about it. So ,we're going to do the dumbest thing                    
 22     |  that we can think of, or one one of the dumbest                                  
 23     |  things you could think of. Or maybe ,we should say simplest and                  
 24     |  not dumbest so as not to, to, to make a value                                    
 25     |  judgment. That you can think of doing which would be to just                     
 26     |  uniformly randomly Choose among some of the data, and say that's                 
 27     |  the data I'm going to look at, and then I'm going to apply some                  
 28     |  learning algorithm to it. Is that what you were thinking of Micheal?             
 29     |  >> Yeah.                                                                         
 30     |  >> Okay, so just pick a subset of the                                            
 31     |  data, apply a learner to it. I'll get some                                       
 32     |  hypothesis out, I'll get some rule out. And now                                  
 33     |  I'm going to combine them, so since were being simple. Why                       
 34     |  don't we try doing something simple for combining. Let's                         
 35     |  imagine, Michael, that we're doing a regression. What's kind of                  
 36     |  the simplest thing you could do if you have                                      
 37     |  ten different rules which tell you, how you should be                            
 38     |  predicting some new data point? What's the                                       
 39     |  simplest thing you could imagine doing with it?                                  
 40     |  >> So, okay, so each of them spits out a number. I guess if we kind              
 41     |  of equally believe in each of them, a                                            
 42     |  reasonable thing to do would be to average.                                      
 43     |  >> Great. So, a very simple way of combining, in the case of                     
 44     |  regression, would be to average them. We'll simply take the mean. And by         
 45     |  the way, why wouldn't we equally believe in each of them. Each one               
 46     |  of them learned over a random subset of the data. You have no reason.            
 47     |  >> Well.                                                                         
 47     |  >> To believe                                                                    
 48     |  one's better than the other.                                                     
 49     |  >> There's a couple of reasons. One ,it could be a                               
 50     |  bad random subset. I don't know how I would measure that.                        
 51     |  >> I could be a good random subset.                                              
 52     |  >> Yeah. Then we'd want, we'd want that to count more in                         
 53     |  the mean. But, but I guess what I was thinking more in terms                     
 54     |  of maybe for some of the subsets you know, it gets more                          
 55     |  error than others or it uses more complex rule than others or something.         
 56     |  >> I could imagine that. Actually maybe we can explore how this sort of idea     
 57     |  might go wrong. Let's, let's do that. Maybe we can do that with the quiz.        
 58     |  You like quizzes, right?                                                         
 59     |  >> They're important.                                                            


##  04 - Ensemble Learning Outputs
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay, so here's a quiz for you Micheal, here's the                               
 2      |  setup, you ready? You've got in data points. The learner                         
 3      |  that you're going to use over your subsets is a                                  
 4      |  zero or a polynomial. The way you're going to combine the                        
 5      |  output of the learners is by averaging them. So, it's                            
 6      |  just what we've been talking about so far, and your                              
 7      |  subsets are going to be constructed in the following way. You                    
 8      |  uniformly randomly picked them and you ended up with N different                 
 9      |  subsets or disjoint, and each one has a single point                             
 10     |  in it, that happens to be one of the data points.                                
 11     |  >> Okay i think i get that                                                       
 12     |  >> Right, so if you look over here on your left                                  
 13     |  you got a graph of some data points and this is                                  
 14     |  one subset This is another subset, that's another subset, that's another         
 15     |  subset, that's another subset, that's another                                    
 16     |  subset, that's another subset, got it.                                           
 17     |  >> Yeah, now what do you want to know about it.                                  
 18     |  >> Now what I want to know is when you do your                                   
 19     |  ensemble learning you learn all these different,                                 
 20     |  you learn all these different rules and then                                     
 21     |  you combine them ,what is the output going to be? What does the ensemble output? 
 22     |  >> And you want a number?                                                        
 23     |  >> I want a description and if the answers a number that's a                     
 24     |  perfectly fine description. But I'll give you a hint, it's a short description.  
 25     |  >> A short description of the answer. Okay, I'll think about it.                 
 26     |  >> Alright.                                                                      


##  05 - Ensemble Learning Outputs
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay Michael have you thought about it? Do you know what the answer is?          
 2      |  >> Yeah. I think, you know, you asked it in a                                    
 3      |  funny way, but I think, what you're asking maybe was pretty                      
 4      |  simple. So let, let me, let me see if I can                                      
 5      |  talk it through. So ,we've got n data points, each learner is                    
 6      |  a zeroth order polynomial. So you, you said the ensemble rule                    
 7      |  is that you learn over a subset, a zeroth order polynomial                       
 8      |  is just (no period) Well, we said that the thing that                            
 9      |  minimizes the average. Sorry, that minimizes the expected error, or the squared  
 10     |  error [INAUDIBLE] it's just the average. So, if                                  
 11     |  the sets are indistinct sets, with one data point                                
 12     |  each, then each, of the individual learners, is                                  
 13     |  just going to learn the average. Then they get, not                              
 14     |  the average sorry. The actual output value of                                    
 15     |  each individual point is the average, and then the                               
 16     |  combining algorithm, to combine all the pieces of                                
 17     |  the ensemble into one answer, combines with the mean.                            
 18     |  So ,it's going to combine the mean of those                                      
 19     |  each of which is the data point, so it's                                         
 20     |  the mean of the data points. So, the ensemble                                    
 21     |  outputs, I don't know, I'd say average or mean?                                  
 22     |  >> Yes.                                                                          
 23     |  >> Or zeroth [INAUDIBLE] polynomial of the data set,                             
 24     |  or, you know, one node decision tree, or ,uh.                                    
 25     |  >> A constant? Which happens to be the                                           
 26     |  mean of the data. Haven't we seen this before?                                   
 27     |  >> It seems to come up a lot,                                                    
 28     |  when we are outputting very simple hypotheses.                                   
 29     |  >> Right. And the last time we did this, if I recall correctly, this is what     
 30     |  happens ,if you do an unweighted average with k and n where k is equal to n.     
 31     |  >> Oh, right. Like, like, right. And N-NN.                                       
 32     |  >> N-NN.                                                                         
 33     |  >> Mm.                                                                           
 34     |  >> Mm, so we should probably do                                                  
 35     |  something a little smarter than this then. And,                                  
 36     |  I thought that we might look at some of the housing data, because, no            
 37     |  one's started looking at the housing data                                        
 38     |  yet. [LAUGH] Okay, so let's look at that                                         
 39     |  right quick and see if we can figure out how this works. And then                
 40     |  see if we can do something a little bit better, even better than that. Okay?     


##  06 - Ensemble Learning An Example
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Alright, Michael, so, here's what you have before you. You have the same         
 2      |  housing data that we've looked at a couple of times before. I've, for the        
 3      |  sake of readability, I've drawn over, some of the data points so that            
 4      |  they're easier to see. This is exactly the data, that we've always had. Okay?    
 5      |  >> Okay.                                                                         
 6      |  >> Now, you'll notice that I marked one of                                       
 7      |  them as green, because here's what we're going to do.                            
 8      |  I'm going to take the housing data you've got, I'm                               
 9      |  going to do some ensemble learning on it. And I'm                                
 10     |  going to hold out the green data point. Okay? So of                              
 11     |  the nine data points, you're only going to learn on 8                            
 12     |  of them. And I'm going to add that green data point                              
 13     |  as my test example and see how it does. Okay?                                    
 14     |  >> Okay. So that sounds like, cross validation.                                  
 15     |  >> It does. This is a cross validation. Or you could just say,                   
 16     |  I just put my training set and my test set on the same slide.                    
 17     |  >> Okay.                                                                         
 18     |  >> Okay, Michael, so the first thing I'm going to do is I'm going to pick        
 19     |  a random subset of these points. And just for the                                
 20     |  sake of the example, I'm going to pick five points                               
 21     |  randomly. And I'm going to do that five times. So                                
 22     |  I'm going to have five subsets of five examples. And by the                      
 23     |  way, I'm going to choose those randomly, and I'm going to choose                 
 24     |  them with replacement. So we're not going to end up in the                       
 25     |  situation we ended up just a couple of minutes ago                               
 26     |  where we never go to see the same data point twice.                              
 27     |  Okay?                                                                            
 28     |  >> Yeah.                                                                         
 29     |  >> Alright. So 5 subsets of 5 examples, and then I'm                             
 30     |  going to learn a third order polynomial. And I'm going to take those             
 31     |  3rd order polynomials. I'm just going to learn on that subset, and then          
 32     |  I'm going to combine them by averaging. Want to see what we get?                 
 33     |  >> Oh, yeah, sure.                                                               
 34     |  >> So here's what you get, Michael. Here I'm showing you a plot over             
 35     |  those same points, with the five different                                       
 36     |  3rd order polynomials. Can you see them?                                         
 37     |  >> Yeah. They're, right. There's like a bunch of wispy hairs.                    
 38     |  >> Just like most third order polynomials. And as                                
 39     |  you can see they're, they're kind of you stare at                                
 40     |  them and you see their kind of similar. But                                      
 41     |  some of them they veer off a little bit because                                  
 42     |  they're looking at different data points. One of them                            
 43     |  actually very hard to see because it's only one like                             
 44     |  this. Actually veers off like this because just, purely                          
 45     |  randomly, it never got to see the two final points.                              
 46     |  >> I see.                                                                        
 47     |  But they all, but they all seem to be pretty much in                             
 48     |  agreement, like between points three and                                         
 49     |  four. There's a lot of consistency there.                                        
 50     |  >> Right. Because just picking five of the                                       
 51     |  subsets you seem to be able to either get                                        
 52     |  things on the end, or you get things in                                          
 53     |  the middle. And maybe one or two things on                                       
 54     |  the end it sort of works out. Even the                                           
 55     |  one that doesn't see the, the last two points                                    
 56     |  still got to see a bunch of first ones                                           
 57     |  and get this part of this space fairly right.                                    
 58     |  >> Cool.                                                                         
 59     |  >> Okay.                                                                         
 60     |  So the question now becomes how good is                                          
 61     |  the average of these compared to something we might                              
 62     |  have learned over the entire data set? And here's                                
 63     |  what we get when do that. So what you're                                         
 64     |  looking at now Michael, is the red line,                                         
 65     |  is the average of all of those five third                                        
 66     |  order polynomials. And the blue line, is the fourth                              
 67     |  order polynomial that we learned when we did this                                
 68     |  with simple regression, a couple of lessons back.                                
 69     |  >> Okay.                                                                         
 70     |  >> And you actually see them pretty close.                                       
 71     |  >> Why is one of them a fourth order, and one a third order?                     
 72     |  >> Well what I wanted to do is try a simpler set of hypothesis,                  
 73     |  than we were doing, than when we were doing full blown regression. So third      
 74     |  order simpler than fourth order. So, I thought we'd combine a bunch of simpler   
 75     |  rules. Then the one we had used before and see how well it does.                 
 76     |  >> You want to know how well it does?                                            
 77     |  >> I would!                                                                      
 78     |  >> Well it turns out that on this data                                           
 79     |  set and I did this many, many, many times                                        
 80     |  just to see what would happen with many different                                
 81     |  random subsets. It typically is the case that the                                
 82     |  blue line always does better on the training set,                                
 83     |  the red points, than the red line does. But                                      
 84     |  the red line almost always does better on the                                    
 85     |  green point on the test set or the validation set.                               
 86     |  >> Interesting.                                                                  
 87     |  >> That is kind of interesting. So wait, so let me get this straight.            
 88     |  It seems sort of magical. So, so it learns an average                            
 89     |  of third degree polynomials, third order polynomials, which is itself a          
 90     |  third order polynomial. But you're saying it does better by doing                
 91     |  this kind of trick than just learning a third order polynomial directly.         
 92     |  >> Yeah, why might you think that might be?                                      
 93     |  I have a guess, you tell me what you think.                                      
 94     |  >> Wow, so well, I mean, you know, the danger is often                           
 95     |  over fitting, over fitting is like the scary possibility. And so maybe           
 96     |  by, by kind of mixing the data up in this way and focusing                       
 97     |  on different subsets of it. I don't know. Somehow manages to find the            
 98     |  important structure as opposed to getting                                        
 99     |  misled by any of the individual datapoints.                                      
 100    |  >> Yeah. That's the basic idea. It's kind of the                                 
 101    |  same thing, at least that's what I, I think that's                               
 102    |  a good answer. It's basically the same kind of argument                          
 103    |  you make for cross validation. Alright. You take a random                        
 104    |  bunch of subsets. You don't get trapped by one or two points that happen to      
 105    |  be wrong because they happen to be wrong                                         
 106    |  because of noise or whatever. And you sort                                       
 107    |  of average out all of the variances and                                          
 108    |  the differences. Hm. And often times it works.                                   
 109    |  And in practice this particular technique. Ensemble learning                     
 110    |  does quite well in getting rid of overfitting.                                   
 111    |  >> And what is this called?                                                      
 112    |  >> So, this particular version, where you take                                   
 113    |  a random subset and you combine by the mean, it's called bagging.                
 114    |  >> And I guess the bags are the random subsets?                                  
 115    |  >> Sure.                                                                         
 116    |  >> [LAUGH]                                                                       
 117    |  That's how I'm going to think of it.                                             
 118    |  >> That's how I'm going to think of it. It also has another name                 
 119    |  which is called bootstrap aggregation. So I                                      
 120    |  guess the different subsets are the boots.                                       
 121    |  >> [LAUGH] No,no, no, no bootstrap usually                                       
 122    |  refers to pulling yourself up by your bootstraps.                                
 123    |  >> Yeah, I                                                                       
 124    |  like my, I like my answer better. So, each of the subsets                        
 125    |  are the boots and the averaging is the strap. And there you go.                  
 126    |  So, regardless of whether you call it bootstrap aggregation or you call it       
 127    |  bagging, you'll notice it's not what I said we were going to talk about          
 128    |  during today's discussion. I said we were going to talk about boosting. So we're 
 129    |  talking about bagging but we're going to                                         
 130    |  talk about boosting. The reason I wanted                                         
 131    |  to talk about bagging is because it's really the simplest thing you can          
 132    |  think of and it actually works remarkably well. But there are a couple           
 133    |  of things that are wrong with it, or a couple                                    
 134    |  of things you might imagine you might do better. That                            
 135    |  might address some of the issues and we're going to see                          
 136    |  all of those when we talk about boosting right now.                              


##  07 - Ensemble Boosting
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay so, let's go back and look at our two                                       
 2      |  questions we were trying to answer. And so far we've                             
 3      |  answer the first one, learn over a subset of data,                               
 4      |  defined a rule by choosing that subset uniformally randomly and                  
 5      |  applying some learning algorithm. And we answered the second question,           
 6      |  which is how do you combine all of those rules                                   
 7      |  of thumbs by saying, you simply average them. And that                           
 8      |  gave us, bagging. So Michael, I'm going to suggest an alternative                
 9      |  to at least the first one. And leave open the                                    
 10     |  second one for a moment. That's going to get us                                  
 11     |  to what we're supposed to be talking about today, which                          
 12     |  is boosting. So let me throw and idea at you and                                 
 13     |  you tell me if you think it's a good one.                                        
 14     |  So rather than choosing uniformly randomly. Over the data, we should             
 15     |  try to take advantage of what we are learning as                                 
 16     |  we go along, and instead of focusing just kind of randomly,                      
 17     |  we should pick the examples that we are not good at.                             
 18     |  So what do i mean by that? What i mean by that                                   
 19     |  is. We should pick a subset based upon whether the examples                      
 20     |  in that subset are hard. So what do you think of that?                           
 21     |  >> Well, I guess it depends on how we think about hard, right                    
 22     |  so it could be that it's hard because some, in some absolute sense right,        
 23     |  or could be that it is hard relative to you know, if we                          
 24     |  were to stop now how well we do Yeah, and I mean the latter.                     
 25     |  >> Oh. Okay. Alright. Well that I feel like                                      
 26     |  that makes a lot of sense. I mean, certainly when                                
 27     |  I'm you know, trying to learn a new skill,                                       
 28     |  I'll spend most of my energy on the stuff that                                   
 29     |  I kind, that I'm kind of on the edge of                                          
 30     |  being able to do, not the stuff that I've already                                
 31     |  mastered. It can be a little dispiriting. But it, but                            
 32     |  it I think it, I make faster progress that way.                                  
 33     |  >> Right and if you, if you go                                                   
 34     |  back to the example that we, we started with, with spam right?                   
 35     |  If you come up with a and you see it does a                                      
 36     |  very good on some of the data, some of the mail examples,                        
 37     |  but doesn't do a good job on the other. Why would you spend                      
 38     |  your time trying to come up with more rules that do well                         
 39     |  on the email messages you already know how to classify? You should               
 40     |  be focusing on the ones you don't know how to classify. And                      
 41     |  that's the basic idea here between, the basic idea hearer behind boosting and    
 42     |  finding the hardest examples.                                                    
 43     |  >> Cool.                                                                         
 44     |  >> Okay. So that answers the first one. We're going to                           
 45     |  look at the hardest examples, and I'm going to define for                        
 46     |  you exactly what that means. I'm going to have to introduce                      
 47     |  at least one technical definition. But ,uh, I want to make                       
 48     |  certain you got that. And the second one, the combining,                         
 49     |  well that's a difficult and sort of complicated thing, but                       
 50     |  at a high level, I can explain it pretty easily                                  
 51     |  by saying we are going to still stick with the mean.                             
 52     |  >> Okay.                                                                         
 53     |  >> We're voting except this time,this time we                                    
 54     |  are going to do weighted mean. Now why do we want to do                          
 55     |  weighted mean? Well I have to tell you exactly how we are going to               
 56     |  weight it but the basic idea is to avoid the certain situations That             
 57     |  we came across when we looked at the data before, when taking an average         
 58     |  over a bunch of points that are spread out, this gives you an                    
 59     |  average or a constant that doesn't give you a lot of information about the       
 60     |  space. So we're going to weight it by something, and it's going to turn          
 61     |  out the way we choose to weight it will be very important. But just              
 62     |  keep in your head for now that we're going to try to                             
 63     |  do some sort of weighted average. Some kind of weighted voting. Okay?            
 64     |  >> Sure. One of the things that's scaring me at the moment though is this,       
 65     |  like I have this fear that by focusing                                           
 66     |  on the hardest questions, and then, and then                                     
 67     |  sort of mastering those, what's to keep the                                      
 68     |  learner from starting to kind of lose track of                                   
 69     |  the ones it has already mastered? Like how,                                      
 70     |  why does it not thrash back and forth?                                           
 71     |  >> So that's going to be the trick. Behind the,                                  
 72     |  the particular way that we do weighting.                                         
 73     |  >> Okay                                                                          
 74     |  >> So I will show you that in a moment, and it's going to require                
 75     |  two slightly technical definitions, that we have                                 
 76     |  been kind of skirting around, this entire conversation. Okay?                    
 77     |  >> Sure.                                                                         


##  08 - Ensemble Boosting Quiz
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Alright so, the, the whole goal of what we're                                    
 2      |  going to add for boosting here is we're going to, we're going to                 
 3      |  expand on this notion of hardest examples and weighted                           
 4      |  mean. But before I can do that, I'm going to have                                
 5      |  to define a couple of terms. Okay. And you                                       
 6      |  let me know Michael if, if these terms make sense.                               
 7      |  So, here's the first one. The first one is                                       
 8      |  error. So how have we been defining error so far?                                
 9      |  >> Usually we take the square difference between the                             
 10     |  correct labels and the, what's produced                                          
 11     |  by our classifier or regression algorithm.                                       
 12     |  >> That's true. That is how we've been using                                     
 13     |  error when we're thinking about regression error. How about, a                   
 14     |  notion of accuracy. About how good we are at,                                    
 15     |  say, classifying examples. So let's, let's stick with classification formulas.   
 16     |  >> Well, that would be the same as                                               
 17     |  squared areas, except that it's not really meeting the                           
 18     |  whole powers [INAUDIBLE] area. That is to say, if                                
 19     |  the outputs are zeroes and ones, the squared area                                
 20     |  is just whether or not there's a mismatch. So                                    
 21     |  it could just be the total number of wrong answers.                              
 22     |  >> Right. So, what we've been doing so                                           
 23     |  far is counting mismatches. I like that word, mismatches.                        
 24     |  And we might call an error raid or                                               
 25     |  an error percentage as the total number of mismatches                            
 26     |  over the total number of examples. And that                                      
 27     |  tells us whether we're at 85% or 92%, or,                                        
 28     |  or whatever, right? So that's what we've been doing                              
 29     |  so far. But implicit in that, Michael, is the                                    
 30     |  idea that every single example is equally as important.                          
 31     |  So, that's not always the case. Now you might remember                           
 32     |  from the first talk that we had. We talked                                       
 33     |  about distributions over examples. We said that, you know, learning              
 34     |  only happens if you're training set has the same                                 
 35     |  distribution as your future testing set. And if it doesn't,                      
 36     |  then all bets are off. And it's very difficult                                   
 37     |  to talk about induction or learning. That notion of distribution                 
 38     |  is implicit in everything that we've been doing so far, and                      
 39     |  we haven't really been taking into account when we've been talking               
 40     |  about error. So here's another definition of error and you tell                  
 41     |  me if you think it makes sense, given what we just                               
 42     |  said. So, this is my definition of error. So the subscript                       
 43     |  D, stands for distribution. So we don't know how new examples                    
 44     |  are being drawn, but however they're being drawn they're being drawn             
 45     |  from some distribution, and I'm just going to call that distribution" D", okay?  
 46     |  >> mhm                                                                           
 47     |  >>                                                                               
 48     |  Right. So H is our old friend the                                                
 49     |  hypothesis. That's the specific hypothesis that our learner                      
 50     |  has output. That's what we think is the                                          
 51     |  true concept, and C is whatever the true underlying                              
 52     |  concept is. So I'm going to define error as                                      
 53     |  the probability, given the underlined distribution that I                        
 54     |  will disagree with the true concept on some                                      
 55     |  particular instance X. Does that make sense for you?                             
 56     |  >> Yeah                                                                          
 57     |  but I'm not seeing why that's different from number of mismatches in the         
 58     |  sense that if we count mismatches on a sample drawn from D, which is             
 59     |  how we would get our testing set anyway. Then I would think that would           
 60     |  be you know if it's large enough a pretty good approximation of this value.      
 61     |  >> So here Michael, let me give you a specific example.                          
 62     |  I'm going to draw four, four possible values of X. And when                      
 63     |  I say I'm going to draw four possible values of X, I                             
 64     |  mean I'm just going to put four dots on the the screen.                          
 65     |  >> Hm.                                                                           
 66     |  >> Okay? And                                                                     
 67     |  then I'm going to tell you this particular learner output a hypothesis.          
 68     |  Output you know, a, a potential function that ends up getting                    
 69     |  the first one and the third one right, but gets the                              
 70     |  second and the fourth one wrong. So what's the error here?                       
 71     |  >> Mm.                                                                           
 72     |  >> So let's just make sure that, that                                            
 73     |  everybody's with us. Let's do this as a quiz.                                    
 74     |  >> Okay, so let's ask the students what they                                     
 75     |  think. So here's the question again. You've output some hypothesis               
 76     |  over the four possible values of x, and it turns                                 
 77     |  out that you get the first and the third one right,                              
 78     |  and you get the second and the fourth one wrong.                                 
 79     |  If I look at it like this, what's the error rate?                                


##  09 - Ensemble Boosting Solution
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay, Michael what's your answer?                                                
 2      |  >> It looks like, half of them are right and half of them are                    
 3      |  wrong. So, the number of mismatches, is, two out of four or a half.              
 4      |  >> Right, that is exactly the right                                              
 5      |  answer ,because ,you got half of them right                                      
 6      |  and half of them wrong. But ,it assumes ,that your likely to see all four of     
 7      |  the examples, equally often. So, what if I told you, that, that's not in fact    
 8      |  the case. So ,here's another example of error for you. What if I told you that   
 9      |  each of the points, is, likely to be seen ,uh,                                   
 10     |  in different proportions and in fact in these particular proportions.            
 11     |  So you're going to see the first one ,half the time.                             
 12     |  You're going to see the second one ,one 20th at                                  
 13     |  a time. You're also going to see the fourth one, one                             
 14     |  20th at a time and you'll see the third one                                      
 15     |  ,four tenths of the time. Alright, so you got it                                 
 16     |  Michael? One half, one 20th, four tenths and one twentieth.                      
 17     |  >> Got it.                                                                       


##  10 - Ensemble Boosting Quiz Two
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay. So, now I have a different question for you. Actually, I have              
 2      |  the same question for you, which is, what is the error rate now. Go.             


##  11 - Ensemble Boosting Solution Two
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay, Michael what's the answer?                                                 
 2      |  >> Well, it's still a half. But I guess we, we really should                     
 3      |  take into consideration those probability. So                                    
 4      |  the number of mismatches they have, but                                          
 5      |  the actual number of errors, the expected number of errors is like well,         
 6      |  a 20th plus 20th, so like a 10th. So it's 90% correct, 10% error.                
 7      |  >> Right. That's exactly right, so, what's important to see here                 
 8      |  is that even though you may get many examples wrong, in some                     
 9      |  sense some examples are more important than others. Because                      
 10     |  some are very rare. And if you think of error,                                   
 11     |  or the sort of mistakes that you're making, not as                               
 12     |  the number of distinct mistakes you can make, but rather                         
 13     |  the amount of time you will be wrong, or the                                     
 14     |  amount of time you'll make a mistake, then you can                               
 15     |  begin to see that it's important to think about the                              
 16     |  underlying distribution of examples that. You see. You buy that?                 
 17     |  >> Yeah.                                                                         
 18     |  >> Okay, so, that notion of error                                                
 19     |  turns out to be very important for boositng because in the                       
 20     |  end, boosting is going to use this trick of distributions in order               
 21     |  to define what hardest is. Since we are going to have learning                   
 22     |  algorithms that do a pretty god job of learning on a bunch                       
 23     |  of examples. We're going to pass along to them a distribution                    
 24     |  over the examples, which is another way of saying, which examples are            
 25     |  important to learn, versus which examples are not as important to                
 26     |  learn. And that's where the hardest notion is going to come in.                  
 27     |  So, every time we see a bunch of examples, we're                                 
 28     |  going to try to make the harder ones more important to get                       
 29     |  right. Than the ones that we already know how to solve.                          
 30     |  And I'll, I'll describe in a minute exactly how that's done.                     
 31     |  >> But isn't it the case that this distribution                                  
 32     |  doesn't really matter? You should just get them all right.                       
 33     |  >> Sure. But now it's a question of                                              
 34     |  how you're going to get them all right. Which                                    
 35     |  brings me to my second definition I want to                                      
 36     |  make. And that second definition is a weak learner.                              
 37     |  So there's this idea of a learning algorithm, which is                           
 38     |  what we mean by a learner here. As being weak. And                               
 39     |  that definition's actually fairly straightforward                                
 40     |  so straightforward in fact that you                                              
 41     |  can sort of forget that it's really important. And all a                         
 42     |  weak learners is, is a learner that no matter what                               
 43     |  the distribution is over your data, will do better than chance                   
 44     |  when it tries to learn labels on that data. So what                              
 45     |  does does better than chance actually mean? Well what it means                   
 46     |  is, that no matter what the distribution over the                                
 47     |  data is, you're always going to have an error rate that's                        
 48     |  less than a half. So that means sort of                                          
 49     |  as a formalism, is written down here below. That for                             
 50     |  all D, that is to say no matter what                                             
 51     |  the distribution is, your learning algorithm We'll have an expected              
 52     |  error. That is the probability that it will disagree with                        
 53     |  it through actual concept if you draw a single sample                            
 54     |  that is less than or equal to one half                                           
 55     |  minus Epsilon. Now epsilon is a term that you end                                
 56     |  up seeing a lot in mathematical proofs and particularly ones                     
 57     |  involving machine learning. And epsilon just means a really, really              
 58     |  small number somewhere between a little bigger than 0 and                        
 59     |  certainly much smaller than 1. So, here what this means                          
 60     |  technically is that you're bounded away from 1 1/2. Which                        
 61     |  another way of thinking about that is you always get                             
 62     |  some information from the learner. The                                           
 63     |  learner's always able to learn something. Chance                                 
 64     |  would be the case where your probability is 1/2 and you actually learn           
 65     |  nothing at all which kind of ties us back into the notion of information         
 66     |  gained way back when with decision trees. So does that all make sense Michael?   
 67     |  >> I'm not sure that I get this right. Let's, maybe we can do                    
 68     |  a quiz and just kind of nail down some of the questions that I've got.           
 69     |  >> Okay, sure. You got an idea for a quiz?                                       
 70     |  >> Sure.                                                                         


##  12 - Weak Learning
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay Michael so you, let's make certain that                                     
 2      |  you really grasp this concept of weak learning okay?                             
 3      |  >> Mm-hm.                                                                        
 4      |  >> So, here's a little quiz that I put together to test your knowledge.          
 5      |  So, here's the, here's the deal. I've got a little matrix here, it's a           
 6      |  little table, and across the top. Are                                            
 7      |  three different hypotheses. So, hypothesis one, hypothesis                       
 8      |  two, and hypothesis three. So your entire                                        
 9      |  hypothesis base consists only of these three hypothesis,                         
 10     |  hypotheses. Got it?                                                              
 11     |  >> Got it.                                                                       
 12     |  >> Okay, your entire instance space consists entirely of                         
 13     |  only four examples; X1, X2, X3, and X4. Got it?                                  
 14     |  >> Got it.                                                                       
 15     |  >> I have an X in a square, if that particular hypothesis does not get the       
 16     |  correct label for that particular instance, and I                                
 17     |  have a green check mark if that particular                                       
 18     |  hypothesis does in fact get the right label for that                             
 19     |  example. So, in this case hypothesis one gets examples 2, 3,                     
 20     |  and 4 correct. But gets example one wrong, while hypothesis                      
 21     |  three gets one in four correct, but two and three incorrect.                     
 22     |  >> I see. So, there's no hypothesis that gets everything right.                  
 23     |  >> Right.                                                                        
 24     |  >> So does that mean that we don't have a weak                                   
 25     |  learner, because then there's some distributions for which any given hypothesis  
 26     |  is going to get things wrong.                                                    
 27     |  >> Maybe. Maybe not. Let's see. Here's what I want you to do. I want             
 28     |  you to come up with the distribution over                                        
 29     |  the 4 different examples, such that a learning                                   
 30     |  algorithm that has to choose between one of                                      
 31     |  those 3 hypotheses will in fact be able                                          
 32     |  to find that does better than chance. That                                       
 33     |  is, has an expected error greater than half.                                     
 34     |  >> Okay. Then if you can do that, I want                                         
 35     |  you to see if you can find a distribution which might not exist,                 
 36     |  such that if you have that distribution                                          
 37     |  over the four examples, a learning algorithm                                     
 38     |  that only looked at age one, age two and age three would not be                  
 39     |  able to return one of them that has an expected error greater than half.         
 40     |  >> So greater than half in this case would mean three out of four, correct?      
 41     |  Oh no, no. Oh, you're using, you want to                                         
 42     |  use that definition that you, that actually took                                 
 43     |  into consideration the distribution.                                             
 44     |  >> Exactly. That's the whole point. If you, if you always need to                
 45     |  have some distribution over your examples to                                     
 46     |  really know what your expected error is.                                         
 47     |  >> Alright. And if there is no such evil distribution, should I just fill in     
 48     |  zeroes in all those boxes? Yes, all zeros means no such distribution. You can do 
 49     |  it in either case. So if you put in all zeros you're saying no such              
 50     |  distribution exists. But otherwise it should add                                 
 51     |  up to one down each of the columns.                                              
 52     |  >> It had better add up to one.                                                  
 53     |  >> Alright, I think I                                                            
 54     |  can give that a shot. Okay, go.                                                  


##  13 - Weak Learning
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay Michael, you got answers for me?                                            
 2      |  >> Yeah, I think so. The first thing I notice is that if I put                   
 3      |  equal weights on all four examples, like                                         
 4      |  I, I decided that instead of solving this                                        
 5      |  problem by thinking, I would just try a couple examples, and see if I found      
 6      |  things in both boxes. So, if I put equal weight on X1, X2, X3, X4.               
 7      |  >> Mm-hm.                                                                        
 8      |  >> Then hypothesis one, H1 gets three                                            
 9      |  out of four correct, that's three quarters.                                      
 10     |  That's better than a half. So.                                                   
 11     |  >> Well done.                                                                    
 12     |  >> Then I fill that in, in the good boxes, quarters all the way down.            
 13     |  >> That's a turtle, 'because it's turtles all the way down [LAUGH].              
 14     |  >> No, no, it's not though, it should be quarters all                            
 15     |  the way down. I thought you'd may be draw a quarter.                             
 16     |  >> I, I can't draw a quarter, also I can't draw a turtle obviously but still.    
 17     |  >> [LAUGH] Agreed. Alright, good.                                                
 18     |  >> You'd think, anyone, do you think anyone listening to                         
 19     |  this is old enough to get turtles all the way down.                              
 20     |  >> Yeah, that's a great joke. Everybody knows that joke.                         
 21     |  >> And                                                                           
 22     |  if people don't know the joke, then we should pause this thing right now, and    
 23     |  you should go look up turtles all the way down. And then come back. Okay.        
 24     |  >> It's a, it's a really great joke if you're computer scientist.                
 25     |  >> Yes, and if you don't think it's a good                                       
 26     |  joke then you should probably be in a different field. Okay.                     
 27     |  >> [LAUGH]                                                                       
 28     |  >> What about the evil distribution?                                             
 29     |  >> So then I started to generate. Okay, well what                                
 30     |  if, the, the, the issue here is that, because we spread                          
 31     |  all the, the, the, the probability out in the first hypothesis                   
 32     |  really good. So I said okay, well let me put all                                 
 33     |  the weight on the first example. The x1.                                         
 34     |  >> Okay. So what did that look like.                                             
 35     |  >> Now h1 did very badly. It gets, it's 100 percent error. And                   
 36     |  h2 is 100 percent error. But h3 is 0 percent errors. So so.                      
 37     |  >> yes.                                                                          
 38     |  >> So, so putting it all putting all the weight on x1 is no                      
 39     |  good. And if you look x2, x3, x4, they all have the property that there's        
 40     |  always a hypothesis that gets them right.                                        
 41     |  So I started to think, well maybe there                                          
 42     |  isn't an evil distribution. And I kind of lucked into putting a half on both     
 43     |  the first and the second one. because i figured that, that                       
 44     |  ought to work, but then i realized, oh wait a second that's                      
 45     |  an evil distribution, because if you choose h1, h2, or h3,                       
 46     |  they all have exactly 50% error on the half a half distribution.                 
 47     |  >> Very good. So 1/2, 1/2, zero, zero, is a correct answer.                      
 48     |  >> Now I don't know if there's others. You know, certainly X, putting all        
 49     |  the weight on X2 and X3 is no good, because H2 and H1                            
 50     |  both get those. Putting all the weight on X3 and X4 are no                       
 51     |  good, because H1 gets all of those correct. In fact we have to                   
 52     |  have some weight on X1, right. Otherwise H1 is the way to go.                    
 53     |  >> Right. So, yeah. No, that's interesting.                                      
 54     |  So what does that mean in this case?                                             
 55     |  >> What do you mean, what does that mean?                                        
 56     |  >> So what does this tell us about, how                                          
 57     |  do we build a weak learner for this example?                                     
 58     |  >> So what it                                                                    
 59     |  tells us is that since there is a                                                
 60     |  distribution for which none of these hypotheses will                             
 61     |  be better than chance, there is no weak                                          
 62     |  learner for this hypothesis space, on this instant set.                          
 63     |  >> Interesting. Now is there a way that                                          
 64     |  we can, like, okay, so this example has no                                       
 65     |  weak learner. Is there a way to change                                           
 66     |  this example so it would have a weak learner?                                    
 67     |  >> Um...I'm sure there is.                                                       
 68     |  >> Like if we change that x2, x, h3, if that was a check instead of an X.        
 69     |  >> Which one?                                                                    
 70     |  X2 H3.                                                                           
 71     |  >> So if we made that a green one, here I'll,                                    
 72     |  I'll make it a green one. By using the power of computers.                       
 73     |  >> Woah, special effect.                                                         
 74     |  >> Yes.                                                                          
 75     |  >> So now there's no way to put weight                                           
 76     |  on any two things and have it fail. I don't                                      
 77     |  know, my intuition now is that this, this should have                            
 78     |  a weak learner. Okay, well, how would we prove that?                             
 79     |  >> I don't know, but may be we should end this quiz.                             
 80     |  >> Yeah, I think, we should end this quiz. And leave it as an exercise           
 81     |  to the listener. I'm pretty sure I can figure this out.                          
 82     |  By the way, we should point a couple of things here                              
 83     |  though, Michael. That one is that, the if it weren't the                         
 84     |  case, if we had more hypotheses and more examples. Perhaps an odd                
 85     |  number of them and we have the x's and the y's                                   
 86     |  in the right places then there'd be lots of ways to                              
 87     |  get weak learners for all the distributions just because you'd have              
 88     |  more choices to choose from. What made this one particularly hard is             
 89     |  that you only had three hypotheses and none of                                   
 90     |  them was, not all of them were particularly good.                                
 91     |  >> Sure, yeah. I mean if you have a bun-, you can have many,                     
 92     |  many hypotheses and they're all pretty bad                                       
 93     |  then you're not going to do very well.                                           
 94     |  >> Well, it would depend upon if                                                 
 95     |  they're bad on very different things. But you're                                 
 96     |  right, if you have a whole lot of hypotheses that are bad at everything, you're  
 97     |  going to have a very hard time with a weak learner. And if you have a            
 98     |  whole bunch of hypotheses that are good at                                       
 99     |  almost everything, then it's pretty easy to have                                 
 100    |  a weak learner.                                                                  
 101    |  >> Interesting. Okay, this is more subtle                                        
 102    |  than I thought. So that's, that's interesting.                                   
 103    |  >> Right. So what the lesson you should take away                                
 104    |  from this is. If you were just, to think about it                                
 105    |  for 2 seconds you might think okay weak learner. That                            
 106    |  seems easy. And often it is, but if you think about                              
 107    |  for 4 seconds you realize that's actually a pretty strong                        
 108    |  condition. You're going to have to have a lot of hypotheses that                 
 109    |  are, many of which are going to have to do good on                               
 110    |  lots of different examples, or otherwise, you're not always going to be          
 111    |  able to find one that does well no matter what the                               
 112    |  distribution is. So it's actually a fairly strong, and important condition.      


##  14 - Boosting In Code
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  All right Michael, so here's boosting in pseudo code. Okay,                      
 2      |  let me read it out to you then you can tell                                      
 3      |  me if it makes sense. So we're given a training set.                             
 4      |  It's made up of a bunch of xi, yr pairs. You                                     
 5      |  know, x is your input and y is your output.                                      
 6      |  And for reasons that'll be clear in a moment All of                              
 7      |  your labels are either minus one or plus one. Where minus                        
 8      |  one means not in class or plus one means you're in                               
 9      |  a class. So this is a binary classification task. That make sense?               
 10     |  >> So far.                                                                       
 11     |  >> Okay. And then what you're going to do is,                                    
 12     |  you're going to loop at every time step, let's call it                           
 13     |  lower-case t. From the first time step one, to some big                          
 14     |  time in the future. We'll just call it capital T and                             
 15     |  not worry about where it comes from right now. The                               
 16     |  first thing you're going to do is you're going to construct a distribution.      
 17     |  And I'll tell you how in a minute, Michael. Okay, so,                            
 18     |  so, don't worry about it. And we'll just call that D                             
 19     |  of T. So, this is your distribution over your                                    
 20     |  examples at some particular time T. Given that distribution, I                   
 21     |  want you to find a weak classifier. I want your                                  
 22     |  weak learner to output some hypothesis. Let's call that eight                    
 23     |  sub T. The hypothesis that gets produced to that                                 
 24     |  time step. And that hypothesis should have some small error.                     
 25     |  Let's call that error Epsilon sub T, because it's a                              
 26     |  small number. Such that it does well on the training                             
 27     |  set, given the particular distribution. So, I'm just rewriting                   
 28     |  my notion of error From, the other side of the                                   
 29     |  screen. So there are times we want you to find                                   
 30     |  a weak classifier. That is, we want you to call                                  
 31     |  some weak learner that returns some hypothesis. Lets call                        
 32     |  it h of t that has a small error. Lets                                           
 33     |  call that epsilons of t. Which is to say ,that                                   
 34     |  the probability of it being wrong that is disagreeing with                       
 35     |  the training label is small, with respect to the underlying distribution.        
 36     |  >> So just to be clear there, the epsilon could                                  
 37     |  be as big as slightly less than a half. Right? It                                
 38     |  doesn't have to be teeny, tiny. It could actually be,                            
 39     |  almost a half. But it can't be bigger than a half.                               
 40     |  >> That's right. And, and no matter what happens.                                
 41     |  Or even equal to a half. but, you know,                                          
 42     |  we can assume, although it doesn't matter for the                                
 43     |  algorithm that the learner is going to return the best one                       
 44     |  that it can. With some error. But regardless, it's                               
 45     |  going to have, it's going to satisfy the requirements                            
 46     |  of a weak learner, and all I've done is                                          
 47     |  copy this notion of error over to here. Ok?                                      
 48     |  >> Awesome!                                                                      
 49     |  >> Ok. So, you're going to do that and you'll do that a whole bunch of times     
 50     |  steps, constantly finding hypothesis at each time step                           
 51     |  [INAUDIBLE] with small error [INAUDIBLE] constantly making new. Distributions,   
 52     |  and then eventually, you're going to output some                                 
 53     |  final hypothesis. Which, I haven't told you yet how                              
 54     |  you're going to to get the final hypothesis. But that's                          
 55     |  the high level bit. Look at your training data,                                  
 56     |  construct distributions, find a week classifier with low error.                  
 57     |  Keep doing that you have a bunch of them                                         
 58     |  and then combine them somehow into some final hypothesis.                        
 59     |  And that's high level of algorithm for boosting, okay?                           
 60     |  >> Okay, but you've left out the two, two really                                 
 61     |  important things, even the part from how you find we,                            
 62     |  weak classifier, which is where do we get this                                   
 63     |  distribution and where do we get this, this final hypothesis?                    
 64     |  >> Right, so let me do that for you right now.                                   


##  15 - The Most Important Parts
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay Michael, you've called my bluff. You, you said                              
 2      |  I've left out the most important parts, and you                                  
 3      |  are right. So, I'm going to tell you ,how to                                     
 4      |  construct the most important parts. Let's start, with the distribution.          
 5      |  So, let's start with the base case, and that                                     
 6      |  is the distribution, at the beginning of time, D                                 
 7      |  sub one. So, this distribution, is going to be                                   
 8      |  over each of the examples and those examples, are ,indexed,                      
 9      |  so, over i. And I'm simply going to                                              
 10     |  set that distribution, to be uniform. So, how                                    
 11     |  many examples do we have, Michael? Let's pick,                                   
 12     |  let's pick a letter. Let's call it n.                                            
 13     |  >> Okay.                                                                         
 14     |  >> Why not, cause we do that for everything else and I'm                         
 15     |  going to say that for every single one of the examples they happen one           
 16     |  over int times, that is uniform distribution. Now, why do I do that,             
 17     |  because, I have no reason to believe, for the purposes of this algorithm,        
 18     |  that any given example, is better ,than any other example,                       
 19     |  more important than any other example, harder than other example                 
 20     |  or anything else. I know nothing. So, see if you                                 
 21     |  can learn over all of the examples. You with me?                                 
 22     |  >> Yeah, cause I feel like if it                                                 
 23     |  actually solves that problem, we're just done. So [CROSSTALK]                    
 24     |  >> [CROSSTALK] Yes and, and that's what you always want. But that's              
 25     |  the easy case. So I start out with uniform distribution, that's what you         
 26     |  usually do ,when you don't know anything. But, what are you going to             
 27     |  do ,while your in the middle? So, here's what I am going to                      
 28     |  do Michael. At every time step T, I'm                                            
 29     |  going to construct, a new distribution, Dis of                                   
 30     |  T plus 1. Okay so, here's how we're                                              
 31     |  going to construct the distribution at every time step. Okay?                    
 32     |  I'm going to create the new distribution, T plus 1 to be E for each example, I.  
 33     |  - to be the old distribution, and times T, times E to the minus alpha T, times Y 
 34     |  suvai, times H of sub-T, of X of I, all divided                                  
 35     |  by Z sub T. [LAUGH] So that's pretty obvious right? [LAUGH]                      
 36     |  So what do each of those terms mean? I mean ,I                                   
 37     |  know it's intuitively obvious ,even to the most casual observer, but ,let        
 38     |  me just try to explain what each of the parts mean.                              
 39     |  So, we know that the D is our distribution and it's some                         
 40     |  number, where, over all the examples, it adds up to one.                         
 41     |  And it's a stand-in, we know, because I said this at the                         
 42     |  beginning, for how important a particular ,example is, how                       
 43     |  often we expect to see it. And that's the                                        
 44     |  trick that we're using with distributions. So, I'm going to                      
 45     |  take the old distribution for an example, of, for                                
 46     |  a particular example. And I'm going to either make                               
 47     |  it bigger or smaller, based upon, how well, the                                  
 48     |  current hypothesis, does, on that particular example. So, there's                
 49     |  a cute little trick here, we know that h                                         
 50     |  of t always returns, a value ,of either minus one or                             
 51     |  plus one, because ,that's how we define our training set, you                    
 52     |  always have a label of minus one or plus one. So,                                
 53     |  ht is going to return minus one or plus one for a                                
 54     |  particular x of i. Y of i which is the label                                     
 55     |  with respect to that, example ,is also always going to be plus                   
 56     |  one or minus one. And alpha t is a constant, which                               
 57     |  I will get into a little bit later just right now think                          
 58     |  of it as a number. And so what                                                   
 59     |  happens ,Michael, if the hypothesis ,at time t for                               
 60     |  a particular example x of i agrees ,with the                                     
 61     |  label ,that is associated with that x of i?                                      
 62     |  >> Well, hang on, you say the alpha's a                                          
 63     |  number. Is it a positive number? A between 0                                     
 64     |  and 1 number? A negative number? What kind of                                    
 65     |  number? Does, does it not matter. I think it matters.                            
 66     |  >> That's a good question. It, it                                                
 67     |  matters eventually. But right now, that number is                                
 68     |  always, positive.                                                                
 69     |  >> Positive, alright. So, like, a [UNKNOWN]. Almost                              
 70     |  like a learning rating kind of thing, maybe.                                     
 71     |  >> It's a learning rating kind of thing, sort of.                                
 72     |  >> Alright, so, good. So the y, okay, I see, I see. So, the y                    
 73     |  times the h is going to be. 1 if they agree, and minus 1 if they disagree.       
 74     |  >> Exactly, so if they both say positive 1, positive 1 times positive 1 is 1.    
 75     |  If they both say negative 1, negative 1 times negative 1 is 1. So, it's exactly  
 76     |  what you say when they agree, that number is 1. And                              
 77     |  when they disagree, that number is minus 1. Alpha Sub T,                         
 78     |  which i define below, is always a positive number. You can                       
 79     |  trust me on this. The error is always between 0 and                              
 80     |  1. And it just turns out that the natural log of                                 
 81     |  1 minus a number between 0 and 1 over that number,                               
 82     |  always gives you a positive number. And if you don't believe                     
 83     |  me, you should play around with the numbers till you convince yourself.          
 84     |  So, that's going to be some positive number.                                     
 85     |  So, that means when they agree, that whole product                               
 86     |  will be positive. Which means ,you'll be raising                                 
 87     |  e to minus some number when they disagree that                                   
 88     |  product will be negative which means you'll be                                   
 89     |  raising e to some positive number. So, let's imagine                             
 90     |  they agree. So you're going to be re                                             
 91     |  raising, e ,to minus some number, what's going to                                
 92     |  happen to the relative weight of d sub t of i?                                   


##  16 - When D agrees
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So, Michael wants us to do a quiz.                                               
 2      |  Because Michael likes quizzes cause he thinks you like                           
 3      |  quizzes. And so, I want you to answer                                            
 4      |  this question before Michael gets a chance to. So                                
 5      |  just to be clear here's the question again. What happens to the distribution     
 6      |  over a particular example i when the hypothesis ht that was output by the        
 7      |  example. Agrees with the particular label, Y-sub-i.                              
 8      |  Okay, so we have four possibilities when they agree.                             
 9      |  One is the probability of you seeing that particular                             
 10     |  example increases. That is, you increase the value of                            
 11     |  D-sub-t on i. Or the probability of you seeing that                              
 12     |  example decreases. That is, the number d of t                                    
 13     |  of i goes down, or it stays the same                                             
 14     |  when they agree or well it depends on exactly                                    
 15     |  what's going on with the old value of d and                                      
 16     |  alpha and all these other things. So ,you can't                                  
 17     |  really give just one of those other three answers.                               
 18     |  So those are your possibilites. The other radio buttons                          
 19     |  [LAUGH] only one of them is right. And go.                                       


##  17 - When D agrees
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay Michael what's the answer.                                                  
 2      |  >> Alright, so you kind of were walking us through                               
 3      |  it, but basically if Yi and Ht agree, that means                                 
 4      |  they're both negative or they're both positive. They're equal                    
 5      |  to each other. So when we multiply them together we                              
 6      |  get one. One times whatever our alpha thing is,                                  
 7      |  some positive number is going to be positive. We're negating                     
 8      |  that, so it's negative E to the negative something is                            
 9      |  something between zero and one. Less than, less than one.                        
 10     |  So, that's going to scale it down. So, it looks                                  
 11     |  like. And you know assuming that everything else goes ok                         
 12     |  with, with the way that ,uh, the normalization happens right?                    
 13     |  It seems like it could be depends on the normalization.                          
 14     |  >> So by the way. That's a good point. The the x sub t. Is in fact, what ever    
 15     |  normalization constant you need at time T, in order                              
 16     |  to make it all work out to be a distribution.                                    
 17     |  >> Correct. Then not going to, not going to change.                              
 18     |  >> True.                                                                         
 19     |  >> But is some of them are correct and some of them incorrect, the ones          
 20     |  that are correct are going to decrease. And the                                  
 21     |  ones that are incorrect are going to increase.                                   
 22     |  >> That's right, so what's the answer to the quiz.                               
 23     |  >> Depends.                                                                      
 24     |  >> That's true, it does. That's exactly the right answer.                        
 25     |  It depends ,on what else is going on, you're correct. Now.                       
 26     |  >> But I feel like it should                                                     
 27     |  be decreases, like that's really, mainly what happens.                           
 28     |  >> That's also fair. The answer is, if this one is correct,                      
 29     |  that is they agree, and you disagree on at least some of                         
 30     |  them, at least one, one other example, it will in fact decrease.                 
 31     |  So I could ask a similar question, which is, well what happens                   
 32     |  when they disagree? And at least one other example agrees. Then what happens?    
 33     |  >> Yeah, then they, then that should increase. Oh.                               
 34     |  >> Right.                                                                        
 35     |  >> Oh. It's going to put more weight on the ones that it's getting wrong.        
 36     |  >> Exactly. And the ones that it's getting                                       
 37     |  wrong must be the ones that are harder. Or at least that's the underlying        
 38     |  idea. All right, Michael, so you got                                             
 39     |  it? So you understand what the equation's for?                                   
 40     |  >> Yeah, it look. It seemed really scary at first but it seems you know          
 41     |  marginally less scary now because all that it's                                  
 42     |  doing, it's doing it in a particular way.                                        
 43     |  I don't know why it's doing it in this particular way. But all it seems to       
 44     |  be doing is. The answers that it, it had, it was getting wrong... It puts more   
 45     |  weight on those and the ones that its                                            
 46     |  getting right, it puts less weight on those                                      
 47     |  and then you know, the loop goes around                                          
 48     |  again and it tries to make a new classifier.                                     
 49     |  >> Right, and since the ones that its getting wrong are getting more and         
 50     |  more weight but we are guaranteed or atleast we've assumed that we have a weak   
 51     |  learner that will always do better than                                          
 52     |  chance. On ,ah, any distribution, it means that                                  
 53     |  you'll always be able to output some learner that can get some of the ones       
 54     |  that you were getting wrong, right.                                              


##  18 - Final Hypothesis
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So that ties together this, what constructed E does                              
 2      |  for you, and connecting it to the hardest examples.                              
 3      |  So now, that gets us to a nice little                                            
 4      |  trick where we can talk about how we actually output                             
 5      |  our final example. So, the way you construct your                                
 6      |  final example, they way you do that combination in the                           
 7      |  step is basically by doing a weighted average. And                               
 8      |  the weight Is going to be based upon this alpha                                  
 9      |  sub T. So the final hypothesis is just the s g n function of the weighted sum of 
 10     |  all of the rules of thumb, all of the weak classifiers that you've been picking  
 11     |  up over all of these time steps Where                                            
 12     |  they're weighted by the alpha sub T's. And remember,                             
 13     |  the alpha sub T is one half of the natural log of one minus epsilon T over       
 14     |  epsilon T. That is to say, it's a measure of how                                 
 15     |  well you're doing with respect to underlining error. So, you get more            
 16     |  weight if you do well Then if you do less well or                                
 17     |  you get less weight. So what does this look like to you?                         
 18     |  Well its a weighted average based on how well you're doing or                    
 19     |  how well each of the individual hypotheses are doing and then you                
 20     |  pass it through a thresh holding function where if its below zero                
 21     |  you say you know what? Negative and if its above zero you                        
 22     |  say you know what? Positive and if its zero you just throw                       
 23     |  up your hands and And return zero. In other words, you return literally          
 24     |  the sign of the number. So you are throwing away information there, and          
 25     |  I'm not going to tell you what it is now, but when we go                         
 26     |  to the next lesson it;s going to turn out that that little bit of                
 27     |  information you throw away is actually                                           
 28     |  pretty important. But that's just a little                                       
 29     |  bit of a teaser. We'll get back to that there. Okay so, this                     
 30     |  is boosting, Michael. There's really nothing else to it. You have a very         
 31     |  simple algorithm, which can be written down in a couple                          
 32     |  of lines. The hardest parts are constructing the distribution, which I           
 33     |  show you how to do over here, and then simply bringing                           
 34     |  everything together, which I show you how to do over here.                       
 35     |  >> Alright yeah, I think it doesn't seem so bad                                  
 36     |  and I feel like I could code this up, but I                                      
 37     |  would be a little happier if I had a handle                                      
 38     |  on what the, why alpha is the way that it is.                                    
 39     |  >> Well there's two answers. The first answer                                    
 40     |  is. You use natural logs because you're using                                    
 41     |  exponentials and that's always a cute thing to                                   
 42     |  do. And of course, you're using the error term                                   
 43     |  as a way of measuring how good the hypothesis                                    
 44     |  is. And the second answer is, it's in the                                        
 45     |  reading you were supposed to have done. [LAUGH] So,                              
 46     |  go back and read the paper now that you've                                       
 47     |  listened to this and you will have a much                                        
 48     |  better understanding of what it's trying to tell you.                            
 49     |  >> Thanks                                                                        
 50     |  >> You're welcome. I'm about helping others Michael you know that.               


##  19 - Three Little Boxes
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So, Michael, I want to try to convince                                           
 2      |  you other than the fact that it's an algorithm                                   
 3      |  with symbols that, it sort of works, at, at                                      
 4      |  least informally. And then, I'm going to do what I                               
 5      |  always do and refer you to actually read                                         
 6      |  the, the, the text to get the, the details.                                      
 7      |  But before I do that, I wanted to go                                             
 8      |  through an example if you think that would help.                                 
 9      |  >> I would like an example.                                                      
 10     |  >> Okay. So, let's go through an example. So, here's a very simple               
 11     |  example. So, I got three little boxes on the screen. Can you see them?           
 12     |  >> Yeah.                                                                         
 13     |  >> Now,                                                                          
 14     |  they're the same boxes. I've drawn them up here beforehand                       
 15     |  because I'm going to solve this problem in only three steps.                     
 16     |  >> Hey those boxes are really nice, did                                          
 17     |  you get help from our trusty course developer?                                   
 18     |  >> I did in fact did get help from our trusty                                    
 19     |  course developer. And when I say help, I mean he did this.                       
 20     |  >> Oh thanks Push Car.                                                           
 21     |  >> Yes Push Car is wonderful. Now what's                                         
 22     |  really cool about this is that Push Car is                                       
 23     |  already let you know that we're going to be                                      
 24     |  able to do this in 3 simple steps. And                                           
 25     |  I'm going to be able to animate it. Or at least hopefully                        
 26     |  it'll look animated by the time, [LAUGH] we're done with all                     
 27     |  the editing. So just pay attention to the first box for                          
 28     |  now, you have a bunch of data points; red pluses and                             
 29     |  green minuses, which is the opposite of what we usually do                       
 30     |  Push Car. But either way it's red pluses and green minuses.                      
 31     |  [LAUGH] With the appropriate labels and they all live in this,                   
 32     |  this part of the plane. By the way, what do you call                             
 33     |  a part of the plane? I know you have                                             
 34     |  line segments, what's like, a sub part of a plane?                               
 35     |  >> Looks like a square to me.                                                    
 36     |  >> Yes it is, but I mean, what do you call them? You,                            
 37     |  you don't call it a plane segment, do you? What do you call it?                  
 38     |  >> A region.                                                                     
 39     |  >> A square region, fine. So it's a square region on a plane. And we             
 40     |  want to figure out how to be able to correctly classify these examples. Okay, so 
 41     |  that is nothing new there. We just want to be able to come up with               
 42     |  something. So now we have to do what we did like in the quiz is that             
 43     |  we have to specify what our hypothesis space is. So                              
 44     |  here's our hypothesis space. So the hypothesis space is the set                  
 45     |  Of axis aligned semi-planes. You know what that means?                           
 46     |  >> Mm, no.                                                                       
 47     |  >> Well for the purpose of this example it means,                                
 48     |  I'm going to draw a line, either horizontal or vertical and say                  
 49     |  that everything on one side of that line is positive                             
 50     |  and everything on the other side of that line is negative.                       
 51     |  >> I see. Okay, good.                                                            
 52     |  >> Right. And their axes align because it's only                                 
 53     |  horizontal and vertical, and they're semi-planes because the positive part       
 54     |  of it is only in part of the plane. Okay, so I'm                                 
 55     |  going to just walk through what boosting would end up doing with this particular 
 56     |  example or what a boosting might do with this particular example given that      
 57     |  you have a learner. That always chooses between axis aligned semi planes. Okay?  
 58     |  >> Yeah.                                                                         
 59     |  >> So let's imagine we ran our boosting algorithm                                
 60     |  now in the beginning it's step 1 all of the                                      
 61     |  examples look the same because we have no particular reason                      
 62     |  to say any are more important than the other, any                                
 63     |  are easier or harder than the other. And that's just                             
 64     |  the algorithm we had before We run through and we ask                            
 65     |  our learner to return some hypotheses that does well in                          
 66     |  classifying the examples. It turns out that though there are many,               
 67     |  and in fact there are an infinite number of possible                             
 68     |  hypotheses you could return. One that works really well is one                   
 69     |  that looks like a vertical line that separates                                   
 70     |  the first two data points from the rest.                                         
 71     |  >> That is what I was guessing.                                                  
 72     |  >> Of course it was. And what I'm saying here is that everythign to              
 73     |  the left of this line is going to be positive and everything to the right        
 74     |  is going to be negative. So if you look at this what does this hypothesis do? So 
 75     |  it gets correct, correctly labeled positive. The two pluses to the left. Right?  
 76     |  >> Correct.                                                                      
 77     |  >> And it gets correct all of the minuses as well.                               
 78     |  >> Correct.                                                                      
 79     |  >> Right? But it gets wrong the three pluses on the                              
 80     |  right side. So it gets, this wrong, this wrong, and this wrong.                  
 81     |  >> Right, the Three Plusketeers.                                                 
 82     |  >> Exactly. [LAUGH] The Three Plusketeers. That's                                
 83     |  actually pretty good. So I'm just you know                                       
 84     |  I'm just going to ask you to trust me here but it turns out that the specific    
 85     |  error here is 0.3 and if you stick that into our little alpha you end up,        
 86     |  our little, our little formula for alpha, you end up with alpha equal to 4.2.    
 87     |  >> That's not obvious to me but.                                                 
 88     |  >> Is is See, see, see it's not always obvious.                                  
 89     |  >> [LAUGH]                                                                       
 90     |  >> Okay. Good. So there you go and that's                                        
 91     |  just what happens when you stick this particular set in                          
 92     |  there. So now we're going to construct the next distribution.                    
 93     |  Right? And what's going to happen in the next distribution?                      
 94     |  >> So the one's that it got right should get less weight and the one's that      
 95     |  it got wrong should get more weight so                                           
 96     |  those three plusketeers should become more prominent somehow.                    
 97     |  >> That's exactly what happens. They become, I'm just going to draw them         
 98     |  as much thicker and bigger to kind of emphasise that they're getting             
 99     |  bigger, and it's going to turn out that everything else is going                 
 100    |  to get smaller which is a lot harder to draw here. So i'm                        
 101    |  just going to kind of leave them their                                           
 102    |  size, so they sort of get normalized away. Okay?                                 
 103    |  >> I would guess as to what the next plane should be. I think that we should     
 104    |  cut it. Underneath those pluses but above the green                              
 105    |  minuses. And that should get us three errors. The                                
 106    |  two pluses on the left and the minus on                                          
 107    |  the top will be wrong. But they have less                                        
 108    |  weight than the three pluses we got right, so                                    
 109    |  this going to be better than the previous one.                                   
 110    |  >> So,                                                                           
 111    |  that's possibly true. But it's not what the learner output.                      
 112    |  >> Oh!                                                                           
 113    |  >> Let me tell you what the learner did output though. This learner              
 114    |  output by putting a line to the right of the three pluses, because               
 115    |  he's gotta get those right in saying that everything to the left is              
 116    |  in fact, positive. So, does that seem like a reasonable one to you?              
 117    |  >> Well, it does better than half. I guess that's really all what we're          
 118    |  trying to do, but it does seem to do worse than what I suggested.                
 119    |  >> Well, let's see, it gets the three                                            
 120    |  that mattered that you were really, really doing poorly                          
 121    |  right but then so did yours. And it only,                                        
 122    |  and it picks up still the other two which                                        
 123    |  it was getting right. And it gets wrong these                                    
 124    |  three minus' which aren't worth so much. So is                                   
 125    |  that worse than what you suggested? No, it gets                                  
 126    |  wrong, oh, the three minuses. Oh, it gets correct                                
 127    |  those two red pluses on the left. So it gets three things                        
 128    |  wrong. So that's just as good as what I suggested. Okay, I agree.                
 129    |  >> Okay good. So the area of this step by the way, turns out                     
 130    |  to be 0.21 and the alpha at this [INAUDIBLE] step turns out to be 0.65.          
 131    |  So that's pretty interesting, so we got a bunch of these right and a bunch of    
 132    |  these wrong. So what's going to happen to the distribution over these examples.  
 133    |  >> Alright, the ones that it, again, the                                         
 134    |  ones that it got wrong should get pushed up                                      
 135    |  in weight and which ones are those, those are                                    
 136    |  the, the three green minuses in the middle patch                                 
 137    |  >> Right.                                                                        
 138    |  >> They should become more prominent. The pluses, the three, the three           
 139    |  plusketeers should become less prominent than they were but it still might be    
 140    |  more prominent than they were in the beginning. And maybe because in fact        
 141    |  the alpha, let's see the alpha is bigger so, it will have actually               
 142    |  a bigger effect on bringing it down.                                             
 143    |  >> Yeah I guess so, but it, there'll still be                                    
 144    |  more prominent than the other ones that haven't been bumped.                     
 145    |  >> Yeah the ones that you, the, the two, the two                                 
 146    |  red pluses on the left have, you've never gotten them wrong.                     
 147    |  >> Hm.                                                                           
 148    |  >> So they're really going to disappear. So, if we do, If I                      
 149    |  do my best to, If I do my best to kind of draw                                   
 150    |  that you're still, you're going to have. These pluses are going to be a          
 151    |  little bit bigger than the other pluses, but they're going to be smaller than    
 152    |  they were before. The two, the three greens in the middle are                    
 153    |  going to be bigger than they were before. But those two pluses                   
 154    |  are going to be even smaller, and these two minuses are going to                 
 155    |  be smaller. So, what do you think the third hypothesis should be.                
 156    |  >> Quiz.                                                                         
 157    |  >> Oh, I like that.                                                              


##  20 - Which Hypothesis
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay, so Michael wanted to have a quiz here,                                     
 2      |  'because Michael again, likes those sort of things and, and                      
 3      |  I like to please Michael. So, we came up                                         
 4      |  with three possibilities, one of which we hope is right.                         
 5      |  >> [LAUGH]                                                                       
 6      |  >> And I've labeled them here in orange, A, B,                                   
 7      |  and C and put little radio boxes next to 'em, so                                 
 8      |  you could select 'em. So which of those three hypotheses                         
 9      |  are, is a good one to pick next? So, A is                                        
 10     |  a horizontal line that says everything above it should be a plus. B is a,        
 11     |  another horizontal line that says everything above it should be a plus. And C is 
 12     |  a vertical line, like the last two                                               
 13     |  hypotheses that we found, that says everything to                                
 14     |  the left should be a plus. So, which do you think is the right one? Go.          


##  21 - Which Hypothesis
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  >> Alright Michael, what's the answer?                                           
 2      |  >> Alright so of those others, well C                                            
 3      |  is pretty good, because it does separate the                                     
 4      |  pluses from the minuses. We, we even liked it so much we used it in round two.   
 5      |  >> Mh-hm.                                                                        
 6      |  >> But it doesn't as good to me as A, because A actually does a good             
 7      |  job of separating the very, the more heavily                                     
 8      |  weighted points. So I would, I would say A.                                      
 9      |  >> So in fact that is what our little learning system shows.                     
 10     |  It shows A. Now, through the trick of animation, I                               
 11     |  leave you with A. And that is exactly the right                                  
 12     |  answer. By the way, Michael, if you look at these                                
 13     |  three hypothesis and their weights, you end up with something kind               
 14     |  of interesting. So if you look at this third hypothesis                          
 15     |  that's chosen here, turns out they have a very low                               
 16     |  error, you'll notice that the errors are going down over                         
 17     |  time, by the way, of 0.14. And it has a much                                     
 18     |  higher alpha of 0.92. Now if you look at these weights and you add them up, you  
 19     |  end up with a cute little combination. So,                                       
 20     |  let me draw that for you. Okay Michael, so                                       
 21     |  I cleaned up a little bit so that you could see it. If you take each of          
 22     |  the three hypothesis that we produced, and you weight                            
 23     |  them accordingly, you end up with the bottom figure.                             
 24     |  >> No way.                                                                       
 25     |  >> Absolutely.                                                                   
 26     |  >> That's. Kind of awesome. So what you're saying                                
 27     |  is that, even though we were only using half planes,                             
 28     |  or, or axis-aligned semi planes, for all the weak learners, that                 
 29     |  at the end of the day it actually kind of bent                                   
 30     |  the line around and captured the positive and negative examples perfectly.       
 31     |  >> Right. Does that remind you of                                                
 32     |  anything else we've talked about in the past?                                    
 33     |  >> Sh. Everything. Nothing. No, I dunno, I mean so with,                         
 34     |  with decision trees you can make the shapes like that, and                       
 35     |  >> That's true.                                                                  
 36     |  >> And the fact that we're doing a weighted                                      
 37     |  combination of things reminds me of the neural net.                              
 38     |  >> Yeah. And it should remind you of one other thing.                            
 39     |  >> I'm imagining that you want me to say                                         
 40     |  nearest neighbors, but I can't quite make the connection.                        
 41     |  >> Well, you recall in our discussion with nearest neighbors,                    
 42     |  when we did weighted nearest neighbor. In particular we did weighted             
 43     |  linear regression, we were able to take a simple hypothesis,                     
 44     |  add it together in order to get a more complicated hypothesis.                   
 45     |  >> That's true, because it's local.                                              
 46     |  >> Right, exactly because it's local, and                                        
 47     |  this is a general feature of Ensemble methods that if you try to look            
 48     |  at just some particular hypothesis class. Let's                                  
 49     |  just call it H, because you're doing weighted                                    
 50     |  averages over hypotheses drawn from that hypothesis                              
 51     |  class. This hypothesis class is almost all                                       
 52     |  low, is at least as complicated as                                               
 53     |  this hypothesis class and often is more complicated.                             
 54     |  So you're able to be more expressive, even though you're                         
 55     |  using simple hypotheses, because you're combining them in some way.              
 56     |  >> I'm not surprised that you can combine simple things to get                   
 57     |  complicated things. But I am surprised that you can combine them just            
 58     |  with sums. And get complicated things because sums often act very, you           
 59     |  know, sort of, friendly. Right it's                                              
 60     |  a linear combination not a nonlinear combination.                                
 61     |  >> Actually, Michael part of the reason you get something                        
 62     |  nonlinear here is because you're passing it through a non-linearity              
 63     |  at the end.                                                                      
 64     |  >> The sine.                                                                     
 65     |  >> Yea, that's a good thing, we should, we should ponder that.                   


##  22 - Good Answers
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  >> Okay Michael, so we've done our little                                        
 2      |  example. I want to ask you a quick question                                      
 3      |  and try to talk something through with you                                       
 4      |  and then we can start to wrap up. Okay.                                          
 5      |  >> Awesome.                                                                      
 6      |  >> Alright, so, here is my quick question. Now, in the reading, which I know     
 7      |  you've read, there's a proof. That shows that boosting not                       
 8      |  only, you know, does pretty things with axis of line semi-planes, but also       
 9      |  that it will converge to good answers and that it will                           
 10     |  find good combined hypotheses. You know, we could go look at                     
 11     |  the reading and write down a proof that shows that boosting                      
 12     |  does well. Umm. And there's one in the reading. Or we                            
 13     |  could talk about an intuition. So if someone were to come                        
 14     |  up to you. If a student were to find you somewhere                               
 15     |  and said, I read the proof, I'm kind of getting it,                              
 16     |  but do you have a good sort of intuition about why                               
 17     |  boosting pins will do well? What do you think you would tell them?               
 18     |  Could you think of something simple? I've been struggling with this for a while. 
 19     |  >> No. [LAUGH].                                                                  
 20     |  >> Okay, well, then let me try something on you and you can tell                 
 21     |  me if it sort of makes sense. So this is just an intuition for why,              
 22     |  for why boosting pins will do well. Okay, so what does boosting do? Okay.        
 23     |  Boosting basically says, if I have some                                          
 24     |  examples that I haven't been able to classify                                    
 25     |  well, I'm going to re-rate all my examples. So that the ones                     
 26     |  I don't do well become increasingly                                              
 27     |  important. Right, that's what boosting does. Yes?                                
 28     |  >> Yes.                                                                          
 29     |  >> Right, that's what this whole, whole bit of D is all about. It's all about    
 30     |  re-weighting based on difficulty and hardest. And we know that                   
 31     |  we have the notion of a weak learner. That no matter what happens for            
 32     |  whatever distribution, we're always going to be able to find                     
 33     |  some hypothesis that does well. So, if I'm trying to                             
 34     |  understand why boosting in the end, why the final hypothesis                     
 35     |  that I get at the end, is going to do well.                                      
 36     |  I can try to get a feeling for that by                                           
 37     |  asking, well. Under what circumstances would it not do well? So,                 
 38     |  if it doesn't do well, then that means there has                                 
 39     |  to be a bunch of examples that it's getting wrong, right?                        
 40     |  >> Mm hm.                                                                        
 41     |  >> That's what it would mean not to do well, agreed?                             
 42     |  >> Yeah.                                                                         
 43     |  >> Okay. So how many things could it not get right? How many things could it     
 44     |  misclassify? How many things could it get incorrect?                             
 45     |  Well, I'm going to argue Michael, that, that                                     
 46     |  number has to be small. There cannot be a lot of examples that it gets wrong.    
 47     |  So do you want to know why? Do you want to know my reasoning for why?            
 48     |  >> Yeah.                                                                         
 49     |  >> So, here's my reasoning, let's imagine I had a                                
 50     |  number of examples at the end of this whole process.                             
 51     |  I've done it T times. I've gone through this many times                          
 52     |  and I have some number of examples that I'm getting                              
 53     |  wrong. If I were getting those examples wrong, then I was                        
 54     |  getting them wrong in the last time step, right? And,                            
 55     |  since I have a distribution and I re-normalize, and it has                       
 56     |  to be the case that at least half of the time,                                   
 57     |  more than half of the time I am correct, that number                             
 58     |  of things I'm getting wrong has to be getting smaller over                       
 59     |  time. Because let's imagine that was at a stage where I                          
 60     |  had a whole bunch of them wrong. Well, then I would                              
 61     |  naturally renormalize them with a distribution so that all of those things       
 62     |  are important. But if they were all important, the ones that                     
 63     |  I was getting wrong, the next time I run a learner, I                            
 64     |  am going to have to get at least half of them                                    
 65     |  right, more than half of them are right. Is that make sense?                     
 66     |  >> It does, but it, but what scares me is, okay, why can't                       
 67     |  it just be the case that the previous ones which were getting right              
 68     |  start to get more wrong as we shift our energy towards the errors.               
 69     |  >> Yeah, why is that?                                                            
 70     |  >> I don't know. But did you wanna,are we, we working up to some kind of you     
 71     |  know, log any kind of thing where each time                                      
 72     |  you are knocking off half of them and therefore.                                 
 73     |  >> I don't know. Do you remember the proof.                                      
 74     |  >> The proof.                                                                    
 75     |  >> I mean what goes on is that                                                   
 76     |  you get, sort of, this exponentially aggressive weighting over                   
 77     |  examples, right?                                                                 
 78     |  >> Yeah.                                                                         
 79     |  >> And you're driving down the number of things you get wrong. Sort of           
 80     |  exponentially quickly, over time. That's why boosting                            
 81     |  works so well and works so fast.                                                 
 82     |  >> I get that we're, the we're quickly ramping up the weights on the hard        
 83     |  ones. I don't get why that's causing us to get fewer things wrong over time.     
 84     |  So like, when you should, in your, in your example that you worked through, that 
 85     |  had the error in the alphas and the errors kept going down and the alphas        
 86     |  kept going up.                                                                   
 87     |  >> Right.                                                                        
 88     |  >> Like, is that necessarily the case?                                           
 89     |  >> Well, what would be the circumstances under                                   
 90     |  which it isn't the case? How would you                                           
 91     |  ever go back and forth between examples? Well,                                   
 92     |  certainly it's the case that if you keep getting                                 
 93     |  something, right, you will, get them. Well, so                                   
 94     |  here's what happens over time, right. Is that over                               
 95     |  time, every new hypothesis, it gets to get                                       
 96     |  a vote, based upon how well it does on                                           
 97     |  the last, difficult let's say, distribution. So the                              
 98     |  ones that are even if the ones that                                              
 99     |  you were getting right you start to get                                          
 100    |  wrong, they are going to, if you get them                                        
 101    |  increasingly wrong, that error's going to go down and                            
 102    |  you're going to get less of a vote, right.                                       
 103    |  Because e sub T is over the current                                              
 104    |  distribution. And it's not over the sum of the                                   
 105    |  voted, over all the examples you've ever seen.                                   
 106    |  >> Understand.                                                                   
 107    |  >> So does that make sense? Is that right?                                       
 108    |  >> I don't know. I don't have the intuition, it seems like                       
 109    |  it could be, you know, could we keep shifting the distribution. It               
 110    |  could be that the error is going up. Like if the air                             
 111    |  could be low, why can't we just make it low from the beginning.                  
 112    |  >> Right.                                                                        
 113    |  >> Like, I feel like the arrow should be going up,                               
 114    |  because we're, we're asking it harder and harder questions as we go.             
 115    |  >> No, no, no, because we're asking it harder and                                
 116    |  harder questions, but even though we're                                          
 117    |  asking it harder and harder questions, it's                                      
 118    |  forced to be able to do well on those hard questions. It's forced                
 119    |  to, because it's a weak learner. I mean that's why having, being able            
 120    |  to always, that's why having a weak learner is such a powerful thing.            
 121    |  >> But why couldn't we like on, on                                               
 122    |  iteration 17, have something where the weak learner works                        
 123    |  right at the edge of it's abilities, and                                         
 124    |  it just comes back with something that's a half                                  
 125    |  minus epsilon.                                                                   
 126    |  >> That's fine. But it has to always be able to do that. If it's                 
 127    |  a half minus epsilon, the things it's getting                                    
 128    |  wrong will have to go back down again.                                           
 129    |  >> No, no I understand that. What I'm saying                                     
 130    |  is that, why would the error go down each iteration.                             
 131    |  >> Well, it doesn't have to, but it shouldn't be getting bigger.                 
 132    |  >> Why shouldn't it be getting bigger?                                           
 133    |  >> So, imagine, imagine, imagine the case that you're                            
 134    |  getting, right. You, you are working at the edge of                              
 135    |  your abilities. You get half of them right. Roughly and                          
 136    |  half of them wrong, the ones you got wrong would                                 
 137    |  become more important, so the next time round you're going                       
 138    |  to get those right, versus the other ones. So you could                          
 139    |  cycle back and forth I suppose, in the worst case,                               
 140    |  but then you're just going to be sitting around, always having                   
 141    |  a little bit more information. So your error will not                            
 142    |  get worse, you'll just have different ones that are able to                      
 143    |  vote on that do well on different parts of the space.                            
 144    |  Right? Because you're always forced to do better than chance. So.                
 145    |  >> Yeah but that, that's not the same as saying                                  
 146    |  that we're forced to get better and better each iteration.                       
 147    |  >> That's right, it's not.                                                       
 148    |  >> So it's, yeah again, I don't see that, that property just falling out.        
 149    |  >> Well, I don't see it falling out either, but then                             
 150    |  I haven't read the proof in like seven, eight, nine years.                       
 151    |  >> Well, I feel like it should be, it should be something like, look we          
 152    |  had, look at what the, so okay, so we generate a new distribution, what is       
 153    |  the previous, what's the previous classified error                               
 154    |  on this distribution, it better be the case.                                     
 155    |  I mean if it were the case that we always return the best classifier that        
 156    |  I could imagine trying to use that but.                                          
 157    |  >> Well we, well we don't, we don't require that.                                
 158    |  >> Yeah, I mean, it's just finding one                                           
 159    |  that's epsilon minus, or a half minus epsilon.                                   
 160    |  >> Right, so let's, let's see if we can take the simple case,                    
 161    |  we got three examples, right, and you're bouncing back and forth and you want    
 162    |  to construct something so that you always do well on two of them.                
 163    |  And then poorly on one, kind of a thing, and that you keep bouncing              
 164    |  back and forth. So let's imagine that you have one-third, one-third, one-third,  
 165    |  and your first thing gets the first two right and the last one                   
 166    |  wrong. So you have an error of a third. And you make that                        
 167    |  last one more likely and the other two less likely. Suitably normalized, right?  
 168    |  >> Yep.                                                                          
 169    |  >> So now, your next one, you want to somehow                                    
 170    |  bounce back and have it decide that it can miss,                                 
 171    |  so lets say you missed the third one. So you,                                    
 172    |  you get the third one right. You get the second                                  
 173    |  one right but you get the first one wrong. What's going                          
 174    |  to happen? Well, three is going to go down. You're still going to,               
 175    |  well you won't have a third error actually. You'll have less than                
 176    |  a third error because you had to get one of the ones                             
 177    |  you were getting right wrong, you had to get the one                             
 178    |  you were getting wrong right. So your error is going to be                       
 179    |  at least an example I just gave. Less than a third. So,                          
 180    |  if your error is less and a third, then the weighting goes                       
 181    |  up more. And so, the one that you just got wrong                                 
 182    |  goes up, doesn't go back to where it was before. It                              
 183    |  becomes even more important than it was when you had a                           
 184    |  uniform distribution. So the next time around, you have to get                   
 185    |  that one right, but it's not enough to break a half.                             
 186    |  So you're going to have to get something else right as well,                     
 187    |  and the one in the middle that you were getting right                            
 188    |  isn't enough. So you'll have to get number three right as well.                  
 189    |  >> Interesting.                                                                  
 190    |  >> Right? And so, it's really hard to cycle                                      
 191    |  back and forth between different examples, because you're exponentially          
 192    |  weighting how important they are. Which means, you're always                     
 193    |  going to have to pick up something along the way.                                
 194    |  Because the ones that you, coicidentally, got right two                          
 195    |  times in a row. Become so unimportant. It doesn't                                
 196    |  help you to get those right. Whereas, the ones                                   
 197    |  that you've gotten wrong, in the past. You've got to,                            
 198    |  on these cycles. Pick up some of them in order to get you over a half.           
 199    |  >> Mmm                                                                           
 200    |  >> And so, it is very difficult for you to cycle back and forth.                 
 201    |  >> Interesting.                                                                  
 202    |  >> And that kind of makes sense, right? If                                       
 203    |  you think about it in kind of an information gain                                
 204    |  sense, because what's going on there is you're, you're                           
 205    |  basically saying you must pick up information all the time.                      
 206    |  >> Hm. And then your non uni. Well uniform is                                    
 207    |  the wrong word but you are kind of. You know,                                    
 208    |  non-linearly using that information in some way. So that kind of                 
 209    |  works. It makes some sense to me, but I think that                               
 210    |  in the end what has to happen is you. You, there                                 
 211    |  must be just a few examples in a kind of weighted sense                          
 212    |  that you're getting wrong. And so if I'm right, that as                          
 213    |  you, as you move through each of these cycles, you're weighting                  
 214    |  in such a way that you have to be picking up                                     
 215    |  things you've gotten wrong in the past. So in other words,                       
 216    |  it's not enough to say, only the things that are                                 
 217    |  hard in the last set, are the ones that I                                        
 218    |  have to do better. You must also be picking up                                   
 219    |  some of the things that you've gotten wrong earlier more                         
 220    |  than you were getting right. Because there's just not enough                     
 221    |  information in the one's that you're getting right all the                       
 222    |  time, because by the time you get that far along,                                
 223    |  the weight on them is near zero and they don't matter.                           
 224    |  >> Interesting.                                                                  
 225    |  >> And then if you say, well, Charles,                                           
 226    |  I could cycle back by always getting those wrong,                                
 227    |  yes, but then if you're getting those wrong, they're going to                    
 228    |  pull up and you're going to have to start getting                                
 229    |  those right too. And so, over time, you've gotta not                             
 230    |  just pick out things that do better than a                                       
 231    |  half. But things that do well on a lot of                                        
 232    |  the data. Because there's no way for all of the                                  
 233    |  possible distributions for you to do better than chance otherwise.               
 234    |  >> Cool.                                                                         


##  23 - Back to Boosting
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  >> Alright, so back to boosting, Michael. So as                                  
 2      |  you recall the little teaser I left you with last                                
 3      |  time, is that it appears that boosting does not                                  
 4      |  always over-fit. And a little graph. That's true, but it                         
 5      |  doesn't seem to over-fit in the ways that we                                     
 6      |  would normally expect it to over-fit. And in particular we'd                     
 7      |  see a, you know, an error line on training And                                   
 8      |  what we expect to see is a testing line that                                     
 9      |  would, you know, hue pretty closely and then start to                            
 10     |  get bad. But what actually happens is that instead, this                         
 11     |  little bit at the end where you get over fitting                                 
 12     |  seems to instead. Just keep doing well. In fact, getting better                  
 13     |  and better and better. And I promised you an explanation                         
 14     |  for why that was. So, given what we talked about                                 
 15     |  with support vector machines, and what we spent most of                          
 16     |  our time thinking about, what do you think the answer is?                        
 17     |  >>                                                                               
 18     |  Well I, I don't think I would have asked again if I, had                         
 19     |  a thought about it. But you mean You want me to connect it                       
 20     |  to support vector machines, somehow. Well the, the thing that was fighting over  
 21     |  fitting in support vector machines, was                                          
 22     |  trying to focus on maximum margin classifiers.                                   
 23     |  >> Here, let me, let me try to explain to you                                    
 24     |  why it is that you don't have this problem with With                             
 25     |  overfitting at least not in the, in the typical way as                           
 26     |  you keep applying it over and over again like you do                             
 27     |  with something like neural networks. And it really boils down                    
 28     |  to noticing that we've been ignoring some information. So, what we               
 29     |  normally keep track of is error. So error on say                                 
 30     |  a training set is just, you know, the The probability that                       
 31     |  you're going to come up with an incorrect answer or                              
 32     |  come up with an answer that disagrees with your training set.                    
 33     |  and that's a very natural thing to think about and it                            
 34     |  makes a lot of sense. But there's also something else that                       
 35     |  is actually captured inside of boosting and captured by a lot of learning        
 36     |  algorithms we haven't been taking advantage                                      
 37     |  of, and that's the notion of confidence.                                         
 38     |  So confidence is not just whether you got it right or wrong. It's                
 39     |  how strongly you believe in a particular answer that you given. Make sense?      
 40     |  >> Yes, a lot of the algorithms we talked                                        
 41     |  indirectly have something like that. So, like in a nearest                       
 42     |  neibhbor method, if you are doing five nearest neighbor                          
 43     |  and all five of the neighbor agree, that seems different                         
 44     |  than the case with vote one way and two vote the other.                          
 45     |  >> Right. And in fact, that's a really good example. If you think of that in     
 46     |  terms of regression Then you could say something                                 
 47     |  like the variance, between them is sort of                                       
 48     |  a stand in for confidence. Low variance means                                    
 49     |  everyone agrees, high variance means, there's some major                         
 50     |  disagreement. Okay. So what does that mean in                                    
 51     |  the boosting case? Well as you recall, the final                                 
 52     |  output of the boosted classifier is given by a very simple formula.              
 53     |  And here's the equation here that h of x is equal to the sine of                 
 54     |  the sum over all of the weak hypothesis that you've gotten of alpha              
 55     |  times h. So the weighted average of all of the hypothesis, right? And            
 56     |  you just simply, if it's positive you produce a plus                             
 57     |  one. And if it's it negative you produce a minus and                             
 58     |  if it's exactly zero you don't know what to do                                   
 59     |  so you just. Produces zero. Just throw up your hands. So                         
 60     |  I'm going to make a tiny change to this formula, Michael. Just, just for         
 61     |  the purpose of sort of, explanation, that                                        
 62     |  doesn't change the fundamental answer. And I'm                                   
 63     |  just going to take exactly this equation as it is. And I'm going to divide       
 64     |  it, by the weights that we use. Now what does that end up doing?                 
 65     |  >> Okay, so the weights. I'm getting a.                                          
 66     |  There's Alphas in the SVM's too, so I'm                                          
 67     |  getting a little confused. So that I'm. I                                        
 68     |  think these Alphas all have to be non-negative.                                  
 69     |  >> Right.                                                                        
 70     |  >> But they kind of like this support vector values, in that                     
 71     |  there could be zero, if, if that hypothesis isn't come into play?                
 72     |  >> Well, but they want in that case, the, the                                    
 73     |  alpha is always set to be the natural log of something.                          
 74     |  >> Oh, oh, oh, and also these alphas are applied to hypothesis whereas           
 75     |  the alphas in the, in the SVM settings were being applied to data points.        
 76     |  >> That's right. So, unfortunately in machine                                    
 77     |  learning, people in, invent things separately and                                
 78     |  re-use notation. Alpha's an easy Greek character to draw, so people use          
 79     |  it all the time. But here, remember, alpha's the measure of how good             
 80     |  a particular weak hypothesis was, and since it has to do better                  
 81     |  than chance, it works out that it will always be greater than zero.              
 82     |  >> Gotcha, okay. So this, this normalization factor,                             
 83     |  this denominator doesn't, it's just a constant with respect                      
 84     |  to x, the input. So it won't actually change                                     
 85     |  the answer. So it really is the same answer                                      
 86     |  as we had before, just a different way of writing it.                            
 87     |  >> Right. And what it ends up doing like                                         
 88     |  often is the case in these situations, is it                                     
 89     |  normalizes the output. So it turns out that this                                 
 90     |  value. Inside here is always going to be between minus                           
 91     |  one and plus one. Okay? But otherwise it doesn't                                 
 92     |  change anything about what we've been doing for boosting. So                     
 93     |  you might ask why did I go through the                                           
 94     |  trouble of normalizing it between minus one and plus one?                        
 95     |  >> Why indeed?                                                                   
 96     |  >> Well it's makes it easier for me to draw                                      
 97     |  what I want to draw next. So, we know that the                                   
 98     |  output of this little bit inside the sign function is                            
 99     |  always going to be between minus one and plus one. Let's                         
 100    |  imagine that I take some particular data point x and                             
 101    |  I pass it through this function, I'm going to get some                           
 102    |  value between minus one and plus one. And let's just                             
 103    |  say for the sake of the argument, it ends up here.                               
 104    |  Okay?                                                                            
 105    |  >> Is that an x or a plus?                                                       
 106    |  >> That's a plus.                                                                
 107    |  >> Okay. So it's a positive example and it's near plus one.                      
 108    |  >> Right.                                                                        
 109    |  >> So this would be something that the algorithm is getting correct.             
 110    |  >> Yes, and it's not just getting it correct,                                    
 111    |  but it is very confident. In its correctness. because it                         
 112    |  gave it a very high value. By contrast there                                     
 113    |  could have been another positive that ends up around here.                       
 114    |  >> Hmm.                                                                          
 115    |  >> So it gets it correct but it doesn't have a lot                               
 116    |  of confidence so to speak in its correct answer because it's very                
 117    |  near to zero. So that's the difference between error and confidence. Because     
 118    |  for example I could also have a plus value way over here.                        
 119    |  So I am very, very confident in my very, very incorrect answer.                  
 120    |  >> Mm.                                                                           
 121    |  >> So this is my daughter, for example.                                          
 122    |  [LAUGH] She's very confident whether she's right or                              
 123    |  wrong. [LAUGH] Okay. And so now imagine there's                                  
 124    |  lots of little points like this. And if                                          
 125    |  you're doing well, you would expect that, you                                    
 126    |  know, very, very often you're going to be                                        
 127    |  correct. And so you end up shoving all                                           
 128    |  the positives over here to the right, and all                                    
 129    |  the negatives over here to the left. And it would be really nice if you were     
 130    |  sort of confident in all of them. Okay,                                          
 131    |  so does this make sense, Michael as a picture,                                   
 132    |  >> Oh yeah.                                                                      
 133    |  >> What, what might be going on? Absolutely.                                     
 134    |  >> Okay, good. So now I want you to imagine that we've                           
 135    |  been going through these, these training                                         
 136    |  examples, and we've gotten very, very good                                       
 137    |  training error. In fact, let's imagine that                                      
 138    |  we have negative training error. I'm [LAUGH]                                     
 139    |  >> Wow.                                                                          
 140    |  >> In fact, let's imagine that we have no                                        
 141    |  training error at all. So we, we label everything correctly.                     
 142    |  So then the picture would look just a little                                     
 143    |  bit different We're going to have all the pluses on one                          
 144    |  side, and all the minuses on the other. But                                      
 145    |  we keep on training, we keep adding more and more                                
 146    |  weak learners into the mix. So here's what ends up                               
 147    |  happening in practice, right? What ends up happening in practice                 
 148    |  is, you have to do some kind of distribution                                     
 149    |  on the hard examples. And the hard examples are                                  
 150    |  going to be the one that are very near the                                       
 151    |  boundary. So as you add more and more of these                                   
 152    |  weak learners what seems to happen in practice is                                
 153    |  that these pluses that are near the boundary and these                           
 154    |  minuses that are near the boundary just start moving                             
 155    |  farther and farther away from the boundary. So, this minus                       
 156    |  starts drifting and drifting and drifting until it's all the way over            
 157    |  here, this minus starts drifting and drifting and drifting untili it's all the   
 158    |  way over here. And the same happens for the pluses. And as                       
 159    |  you keep going and you keep going, what ends up happening is that                
 160    |  your error stays the same. It doesn't change at all, however your                
 161    |  confidence keeps going up and up and up and up and up. Which                     
 162    |  has the effect, if you'll look at this little drawing over here of               
 163    |  moving the pluses all around over here, so they're all in a bunch,               
 164    |  and the minuses are on the other side.                                           
 165    |  So what does that look like to you, Michael?                                     
 166    |  >> This picture?                                                                 
 167    |  >> Yeah.                                                                         
 168    |  >> I mean that there's a, there's a                                              
 169    |  big gap between the left most plus and the                                       
 170    |  right most minus. Which, you know, in the                                        
 171    |  context of this lecture reminds me of a margin.                                  
 172    |  >> That's exactly right. Basically what ends up                                  
 173    |  happening is that as you add more and more                                       
 174    |  weak learners here the boosting out rhythm ends                                  
 175    |  up becoming more and more confident in its answers                               
 176    |  which it's getting correct. And therefore effectively ends up creating a         
 177    |  bigger and bigger margin. And what do we know about large margins?               
 178    |  >> Large margins tend to minimize over fitting.                                  
 179    |  >> That's exactly right. So it, counter intuitively, as we create                
 180    |  more and more of these hypotheses, which you would think would                   
 181    |  make something more and more complicated, it turns out that you                  
 182    |  end up with something smoother, less likely to overfit and ultimately,           
 183    |  less complicated. So the reason boosting tends to do well and tends to avoid     
 184    |  over fitting even as you add more and more learners is that you're increasing    
 185    |  the margin. And there you go. And if you look in the reading that                
 186    |  we gave the students there's actually a                                          
 187    |  detailed descritpion about this in a proof.                                      
 188    |  >> Cool.                                                                         
 189    |  >> Okay. So, there you go, Michael.                                              
 190    |  Do you think, then, that boosting never overfits?                                
 191    |  >> [SOUND] Never seems like such a strong word.                                  
 192    |  I mean, the story that you told says that it's going to try                      
 193    |  to separate those things out, but I guess I guess it doesn't have                
 194    |  to be able to do that. I mean, it could be that                                  
 195    |  for example all the weak learners                                                
 196    |  are I dunno very unconfident very inconsistent.                                  
 197    |  >> Hm. Okay, well you know, maybe, maybe it's worthwhile to                      
 198    |  take a little diversion here to take a five second quiz.                         
 199    |  >> I think it's worth the time.                                                  
 200    |  >> Done!                                                                         


##  24 - Boosting Tends to Overfit
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay Michael. So here's a quick quiz. So we just tried                           
 2      |  to argue that boosting has this annoying habbit of not always                    
 3      |  over fitting, but of course something can always over fit. Because               
 4      |  otherwise we just do boosting and we're done, then neither of us                 
 5      |  would have jobs. And we don't want that to happen. So                            
 6      |  here's a little quiz to see if we can figure out the                             
 7      |  circumstances under which boosting might over fit, or tends to over              
 8      |  fit. So here are five possiblities. Let me read them to you.                     
 9      |  Tell me if they actually make sense. So                                          
 10     |  here's possiblity number one, boosting will tend to over                         
 11     |  fit if The weak learner that it's boosting                                       
 12     |  over, always chooses the weakest output that is, it,                             
 13     |  among all the hypothesis that it finds that                                      
 14     |  do better than chance over the training with whatever                            
 15     |  given distribution. It always pick the one that is                               
 16     |  still nonetheless closest to chance, while still being better.                   
 17     |  >> Well, why would it do that?                                                   
 18     |  >> Just to be difficult.                                                         
 19     |  >> Alright, and so you want to know, whether that makes                          
 20     |  it over, would [INAUDIBLE] make it over fit? [UNKNOWN] boosting overfit.         
 21     |  >> Okay. Alright.                                                                
 22     |  >> The second one is weak learner actually ends up using...or                    
 23     |  the weak leaner itself that boosting is using is in fact                         
 24     |  a neural network learner. And just for a little specificity, let's               
 25     |  say this is a neural network that has many many layers and                       
 26     |  many many nodes. So, you know, it's a big                                        
 27     |  powerful neural network, alright? the other option is... Boosting has            
 28     |  a lot of data. So you're trying to learn, your                                   
 29     |  training data is actually very, very, very large. You have                       
 30     |  lots and lots of examples. The fourth case, is that,                             
 31     |  the true underlying hypothesis,the true underlying concept, is in fact           
 32     |  non linear. So you can't just draw a line. And                                   
 33     |  then the fifth case is that we let boosting train                                
 34     |  much too long. Whatever that means. Let's just say we let it                     
 35     |  train a lot. Not just a thousand iterations but a hundred billion iterations.    
 36     |  >> Okay.                                                                         
 37     |  >> Okay. Billions and billions of itterations. Okay. You got it?                 
 38     |  >> Yeah.                                                                         
 39     |  >> Alright. Go.                                                                  


##  25 - Boosting Tends to Overfit
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  >> All right, Michael. What's the answer?                                        
 2      |  >> All right. Well, let me start off with what I think the                       
 3      |  answer isn't. So, the last one, boosting tends to overfit, if boosting trains    
 4      |  too long. You just told me a story about that not being true.                    
 5      |  So I'm going to eliminate that                                                   
 6      |  one from consideration. Boosting training too long.                              
 7      |  >> Oh, nice to know you were listening.                                          
 8      |  >> [LAUGH] Boosting training too long, seems like                                
 9      |  not a good reason for it to overfit.                                             
 10     |  >> You're correct.                                                               
 11     |  >> All right. Boosting tends to overfit if it's                                  
 12     |  a nonlinear problem. So, that doesn't seem right. I                              
 13     |  mean I guess, no, this one just doesn't seem right                               
 14     |  at all. Like I don't see why, why the problem                                    
 15     |  being linear or nonlinear, has anything to do with overfitting.,                 
 16     |  >> Okay.                                                                         
 17     |  >> A whole lot of data is the opposite of what tends                             
 18     |  to cause overfitting. If there's lots of data then you'd think that it           
 19     |  would actually do a pretty reasonable job of, you know, there's a                
 20     |  lot to fit. There's a lot going on there. It's unlikely to overfit.              
 21     |  >> Right, and                                                                    
 22     |  in fact if a whole lot of data included all of the data, and you actually        
 23     |  could get zero training error over it, then                                      
 24     |  you know you have zero training zero generalization error.                       
 25     |  >> because it'll work on the testing data as well, because it's in there.        
 26     |  >> Right.                                                                        
 27     |  >> All right. Weak learner uses artificial neural network with                   
 28     |  many layers and nodes. So I'm guessing that you wanted                           
 29     |  me to think about that being something that, on its                              
 30     |  own, is prone to overfitting, because it's got a lot                             
 31     |  of parameters.                                                                   
 32     |  >> Sure.                                                                         
 33     |  >> So, if, and now we're doing boosting                                          
 34     |  over that. So we fit a neural net, and                                           
 35     |  then we fit another neural net, and we                                           
 36     |  fit another neural net. And we're combining all the                              
 37     |  outputs together in the correct, weighted way. It's                              
 38     |  not obvious to me that that should be a                                          
 39     |  good thing to do. I'm not sure it would overfit, but it seem like it sure could. 
 40     |  >> OK, so you're, you're, so for now let's                                       
 41     |  put a little question mark to it. You think that                                 
 42     |  might be the right answer, but you want to think about it some more?             
 43     |  >> Yeah let me, let me look at the first                                         
 44     |  one. Weak learner chooses the weakest output. Well, I mean                       
 45     |  boosting is supposed to work as long as we have                                  
 46     |  a weak learner. . And it doesn't matter if it                                    
 47     |  chooses the weakest or the strongest. All that matters is                        
 48     |  it does significantly better than a half. So, like I                             
 49     |  feel like the only one, the only one of these                                    
 50     |  choices that is likely to be true is the second one.                             
 51     |  >> And that is, in fact, correct. So let me give you an example                  
 52     |  of when that would be correct. So let's imagine                                  
 53     |  I have a big powerful new network that could represent                           
 54     |  any arbitrary functions. Okay, got lots of layers and lots                       
 55     |  of nodes. So, boosting calls it, and it perfectly fits                           
 56     |  the training data, but of course overfits. So then it                            
 57     |  returns, and it's got no error, which means all of                               
 58     |  the examples will have equal weight. And when you go                             
 59     |  through the loop again, you will just call the same                              
 60     |  learner, which will use the same neural                                          
 61     |  network, and will return the same neural network.                                
 62     |  So every time you call the learner, you'll get zero training error, but you will 
 63     |  just get the same neural network over and over and over again. And a weighted    
 64     |  sum of the same function is just that                                            
 65     |  function. So if it overfit, boosting will overfit.                               
 66     |  >> Interesting. And not only will it overfit, but it'll                          
 67     |  just, it'll be stuck in a horrible loop of error.                                
 68     |  >> Right. So that's why this                                                     
 69     |  is the sort of situation where you can imagine                                   
 70     |  boosting a lower fit. If the underlying learners all                             
 71     |  overfit and you can never get them to stop                                       
 72     |  overfitting, then there's really not much you can do.                            
 73     |  >> Interesting.                                                                  
 74     |  >> Now, I do want to have a little semantic argument                             
 75     |  with you for a moment, Michael. You used the word strongest at                   
 76     |  some point, when you were talking about using the weakest output. And            
 77     |  I just want to point out that, that doesn't really mean anything.                
 78     |  >> What do you mean, it doesn't mean anything?                                   
 79     |  >> Well, so what's a strong, what would you call                                 
 80     |  a strong learner?                                                                
 81     |  >> One that is far away from it. If a                                            
 82     |  weak learner just has to do a little bit better                                  
 83     |  than a half, it seems like a strong learner would                                
 84     |  be something that would be very close to being accurate.                         
 85     |  >> Right. Of course, on the other hand, if                                       
 86     |  by that definition all strong learners are also weak learners.                   
 87     |  >> Sure.                                                                         
 88     |  >> Because anything that does better than a half is still doing better           
 89     |  than a half, which is all it requires to be a weak learner.                      
 90     |  >> Yeah, but that's kind of true of people                                       
 91     |  too. Like a strong person is also a weak person.                                 
 92     |  >> No.                                                                           
 93     |  >> Well it depends how you define it. So,                                        
 94     |  if you say a weak person is someone who can                                      
 95     |  at least lift their own arms, then strong people are                             
 96     |  also weak people in that they can lift their arms.                               
 97     |  >> Yes if you define it that way and if I define                                 
 98     |  blue to be purple, then I can say blue is purple. But that's                     
 99     |  not how people define weak people. They define weak people, by saying they       
 100    |  can't lift more than, not that they can lift at least as much.                   
 101    |  >> I see. So it's this piece of terminology that boosting uses that is in        
 102    |  error, not me.                                                                   
 103    |  >> That's one interpretation. It's not the one that I would use, but             
 104    |  it's one interpretation. When you say something like a strong learner, I mean,   
 105    |  it makes sense to use that kind of term, and sort of throw                       
 106    |  it around, and say, well, by a strong learner I mean someone who's,              
 107    |  or a learner that's going to overfit, or is going to always do                   
 108    |  really well on the training data. But in kind of a technical definition          
 109    |  it's very difficult to sort of pin down. So don't get too caught                 
 110    |  up what a strong learner means if you want to write a proof.                     
 111    |  Seems fair?                                                                      
 112    |  >> Good point yeah, also, also that this whole notion that strong                
 113    |  is sometimes defined as not weak. And it is not the case that                    
 114    |  if you have something that's not a weak learner that it's, then                  
 115    |  it's a strong learner. In fact, it's no lear, no learner at all.                 
 116    |  >> Exactly. So, a weak learner's just defined in a way that                      
 117    |  basically says, it gives me at least some information. Good. Let me              
 118    |  just throw one more thing in here and then we can stop                           
 119    |  talking about this. There's another, a couple of other cases where boosting      
 120    |  tends to overfit. The one that matters the most, or                              
 121    |  comes up the most, is in the case of pink noise.                                 
 122    |  >> Did you say, peak noise?                                                      
 123    |  >> I said, pink noise. I even wrote it in red, which                             
 124    |  looks like pink. It's a strong pink as opposed to a weak pink.                   
 125    |  >> [LAUGH]                                                                       
 126    |  >> I'm sorry. There's no way for that to be obvious from what we've              
 127    |  talked about, but as a practical matter,                                         
 128    |  pink noise tends to, cause boosting overfit.                                     
 129    |  >> Okay, but this is not a term I'm familiar with                                
 130    |  unless you're critiquing the musical stylings of a particular performer.         
 131    |  >> [LAUGH] No. Although I did recently see, see them in concert. But             
 132    |  that's a whole other conversation. Okay, so pink noise just means uniform noise. 
 133    |  >> I thought white noise was uniform noise.                                      
 134    |  >> No, white noise is Gaussian noise. Okay, so pink noise is uniform             
 135    |  noise and white noise is Gaussian noise. This is why, Michael, by the way,       
 136    |  if you ever try to set up a studio or a cool stereo system in your house, you    
 137    |  want a pink noise generator. So that it covers                                   
 138    |  all the frequencies equally, not just the white noise. generated.                
 139    |  >> Hm.                                                                           
 140    |  >> But boosting tends to overfit in those sorts of circumstances. And you        
 141    |  can read more about it in the notes if you want to. But                          
 142    |  the one that I want I really want people to get is, that                         
 143    |  if you have an underlying weak learner that overfits, then it is difficult       
 144    |  for boosting to overcome that. Because fundamentally you've already done all of  
 145    |  your overfitting and it's, there's really not much for those things to do.       
 146    |  >> Okay. Got it?                                                                 
 147    |  >> Got it.                                                                       
 148    |  >> Excellent. It all ties back into margins, and it's all one                    
 149    |  big story, which I think is the lesson of all of machine learning.               


##  26 - Summary
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay, Michael, so that was a great conversation, what have we learned?           
 2      |  >> Alright, well we talked about ensemble learning                               
 3      |  which was the idea of instead of just                                            
 4      |  learning one thing, if it's good to learn                                        
 5      |  once, it's even better to learn multiple times,                                  
 6      |  >> In multiple ways.                                                             
 7      |  >> The simple version that we concentrated on first was                          
 8      |  this notion of bagging. Where what we did is instead                             
 9      |  of just learning on the whole data set, we would                                 
 10     |  sub-sample bunch of examples from the training set, different ways,              
 11     |  and train up different classifiers or different learners on each                 
 12     |  of those and then merge them together with the average.                          
 13     |  >> Okay, so if I can summarize                                                   
 14     |  that, we learned that ensembles are good. [LAUGH]                                
 15     |  >> We learned that even simple ensembles like bagging are good.                  
 16     |  >> We talked about the fact that by using this kind                              
 17     |  of ensemble approach, you can take simple learners or simple classifiers and     
 18     |  merge them together and get more complicated classifiers.                        
 19     |  >> Mm, yeah, so we can take. We                                                  
 20     |  can. Combining simple gives you complex. Anything else?                          
 21     |  >> And we talked about the idea of boosting where you                            
 22     |  can Oh, maybe this is why it's called boosting. You can take                     
 23     |  something that has possibly very high error but always less than                 
 24     |  a half, and turn it into something that has very low error.                      
 25     |  >> So we learned that boosting is really good.                                   
 26     |  And, we talked a little bit about why, that's                                    
 27     |  good. By the way, there's a whole bunch of                                       
 28     |  other details here too, right? Boosting also has the                             
 29     |  advan, as does bagging Not only has these little                                 
 30     |  properties you've talked about before, but it tends to be                        
 31     |  very fast. It's agnostic to the learner. As you                                  
 32     |  noticed, that in no time, did we say, try                                        
 33     |  to take advantage of what the actual learner was                                 
 34     |  doing. Just that it was, in fact, a weak learner.                                
 35     |  >> Hm.                                                                           
 36     |  >> So I think that's important. It's agnostic.                                   
 37     |  >> Meaning you can plug in any learner you want?                                 
 38     |  >> Yeah. So long as it's a weak learner. So there's something                    
 39     |  we learned about. We learned about weak learners that we defined with that       
 40     |  meant. And, we also talked about ,um, what error really, really means.           
 41     |  With respect to some kind of underlying distribution. What do you think Michael? 
 42     |  >> That seems like useful stuff.                                                 
 43     |  >> These are useful stuff to me. I'm going to throw one more                     
 44     |  thing at you, Michael, before I let you go. Okay, you ready?                     
 45     |  >> Yep.                                                                          
 46     |  >> Here's a simple fact. About boosting that                                     
 47     |  turns out in practice. You know our                                              
 48     |  favorite little over-fitting example. Do you know                                
 49     |  how over-fitting works? You have a training                                      
 50     |  line that tends to get better, and better,                                       
 51     |  and better. Maybe even going down to zero error. But then you have test          
 52     |  error Which gets better and better and at some point it starts to get worse.     
 53     |  >> Mm.                                                                           
 54     |  >> And at that point you have over fitting and I think,                          
 55     |  Michael, you asserted it at some point or maybe I asserted that                  
 56     |  ,you always have to worry about over fitting. Over fitting is                    
 57     |  just the kind of fact of life. You got to come                                   
 58     |  up with ways to deal with it or sort of over                                     
 59     |  believing your data. Well, what if I told you that in practice                   
 60     |  When you run boosting, even as you run it over time                              
 61     |  so that your training error keeps getting better and better and                  
 62     |  better and better, it also turns out that your testing error                     
 63     |  keeps getting better and better and better and better and better and             
 64     |  better and better.                                                               
 65     |  >> That seems too good to be true.                                               
 66     |  >> It does seem too good to be true. It turns out it's                           
 67     |  not too good to be true. And I have an explanation for it.                       
 68     |  >> Tell me.                                                                      
 69     |  >> Not until next time.                                                          
 70     |  >> alright, see you then.                                                        
 71     |  >> See you then. Bye.                                                            


