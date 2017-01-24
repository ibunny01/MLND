#  Bayesian Learning Subtitles
##  01 - Intro
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  HI Michael.                                                                      
 2      |  >> Hey how's it going?                                                           
 3      |  >> So I want to talk about something today Michael.                              
 4      |  I want to talk about Bayesian Learning, and I've been inspired                   
 5      |  by our last discussion on learning theory to think a                             
 6      |  little bit more about what it is exactly that we're trying                       
 7      |  to do. I'm in the mood beyond specific algorithms to                             
 8      |  just think more generally The sort that learning people want us                  
 9      |  to do, learning theory people want us to do and I                                
 10     |  think Bayesian Learning is a nice place to start. Sound fair?                    
 11     |  >> Yeah, that sounds really cool, I think                                        
 12     |  that might be a nice formal framework for thinking about some of these problems. 
 13     |  >> Good. Good. So, I'm going to start out. By                                    
 14     |  making a few assertions, which I hope you will                                   
 15     |  agree with, and if you agree with this then                                      
 16     |  we'll be able to kind of move forward and ask                                    
 17     |  some pretty cool questions okay? So Bayesian learning, so                        
 18     |  the kind of idea here behind Bayesian learning is                                
 19     |  this sort of fundamental Underlying assumption about what we're                  
 20     |  trying to do with the machine learning. So, I've written                         
 21     |  it down here, here's what I'm going to claim                                     
 22     |  we're trying to do. We are trying to learn                                       
 23     |  the best hypothesis we can given some data and                                   
 24     |  some domain knowledge. Do you buy that as an assertion?                          
 25     |  >> Yeah, it's, and pretty much everything we've talked about so far              
 26     |  has had a form kind of like that. We're searching through a hypothesis           
 27     |  base and As you've pointed out on multiple occasions there's this kind           
 28     |  of extra domain knowledge that comes into play for example when you pick         
 29     |  a like a similarity metric first thing like [INAUDIBLE]                          
 30     |  >> Right and of course we always have the                                        
 31     |  data because we're machine learning people and we always have                    
 32     |  data. So this is what we've been trying to do                                    
 33     |  and I'm going to suggest that we can be a                                        
 34     |  little bit more precise about what we mean by                                    
 35     |  best and I'm going to try to do that and                                         
 36     |  see if you agree with me. Okay, so I'm going                                     
 37     |  to rewrite what I've written already except I'm replacing best                   
 38     |  with most probable. Okay. So what I'm going to claim is that what                
 39     |  we've really been trying to do with all these algorithms we're doing is          
 40     |  we're trying to learn the most likely or the most probable hypothesis            
 41     |  given the data and whatever domain knowledge we bring [UNKNOWN]. You buy that?   
 42     |  >> Interesting. I'm not sure yet. I mean, so is it                               
 43     |  the hypothesis that it's most likely to be returned by the algorithm?            
 44     |  >> No, it's the hypothesis                                                       
 45     |  that we think is most likely, given the data that we've seen.                    
 46     |  Given the training set and given whatever domain knowledge that we bring to      
 47     |  bear on the problem, the best hypothesis is the one that is                      
 48     |  most likely, that is Most probable. Or most l, probably the correct one.         
 49     |  >> Interesting. Well, are we going to be able to connect that to what we         
 50     |  were talking before? Which is generally we were                                  
 51     |  selecting hypotheses based on things like their error.                           
 52     |  >> Yes. Exactly. We are going to be able to connect that.                        
 53     |  We are definitly going to be able to connect that. But.                          
 54     |  >> Okay.                                                                         
 55     |  >> I can;t go forward unless I can convince                                      
 56     |  you that it's reasonable to at least start out thinking                          
 57     |  about best being the same thing as most probable. Yeah,                          
 58     |  I'm willing to go forward with this. It sounds interesting.                      
 59     |  >> So if you're willing to move forward with this, then I want to write          
 60     |  one more thing down and then we can sort of dive into it. So if                  
 61     |  you buy that we're trying to learn the most probable hypothesis, the most likely 
 62     |  one, the one that has the highest chance of being correct given the data, and    
 63     |  our domain knowledge, then we can write that                                     
 64     |  down in math speak pretty simply. It's the                                       
 65     |  probability of, some particular hypothesis h, drawn from                         
 66     |  some hypothesis class. Given some amount of data                                 
 67     |  which I'm just going to refer to as D                                            
 68     |  from now on. Okay? And that's just, exactly                                      
 69     |  what we said just above when we talk                                             
 70     |  about the most probable age, given the data. Okay?                               
 71     |  >> Well wait. Two things. One is so D                                            
 72     |  is not distribution which we've had in the past.                                 
 73     |  >> That's true.                                                                  
        |  00:03:21,910 --> 00:03:25,130                                                    
        |  00:03:25,130 --> 00:03:26,730                                                    
        |  00:03:26,730 --> 00:03:29,280                                                    
        |  00:03:29,280 --> 00:03:31,580                                                    
        |  00:03:31,580 --> 00:03:34,620                                                    
        |  00:03:34,620 --> 00:03:40,010                                                    
        |  00:03:40,010 --> 00:03:40,360                                                    
        |  00:03:40,360 --> 00:03:47,220                                                    
        |  00:03:47,220 --> 00:03:49,260                                                    
        |  00:03:49,260 --> 00:03:52,800                                                    
        |  00:03:52,800 --> 00:03:53,400                                                    
        |  00:03:53,400 --> 00:03:57,250                                                    
        |  00:03:57,250 --> 00:03:59,039                                                    
        |  00:03:59,039 --> 00:04:00,310                                                    
        |  00:04:00,310 --> 00:04:03,480                                                    
        |  00:04:03,480 --> 00:04:06,000                                                    


##  02 - Bayes Rule
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Alright Michael. So like I said, we're going                                     
 2      |  to spend all this time trying to, to                                             
 3      |  unpack this particular equation. And the first thing                             
 4      |  we need to do is we need to come                                                 
 5      |  up with another form of it that we                                               
 6      |  might have some chance of actually understanding of                              
 7      |  actually getting through. So I want to use                                       
 8      |  something called Bayes' rule. Do you remember Bayes' rule?                       
 9      |  >> I do.                                                                         
 10     |  >> Okay, what's Bayes' Rule?                                                     
 11     |  >> The man with the Bayes makes the                                              
 12     |  rule. Oh wait, no, that's the golden rule.                                       
 13     |  >> That's right, no.                                                             
 14     |  >> The Bayes Rule, is, it relates, it, I                                         
 15     |  don't know. I think of it as just letting                                        
 16     |  you switch which thing is on which side of the bar.                              
 17     |  >> Okay, so.                                                                     
 18     |  >> Do you want me to give the whole expression?                                  
 19     |  >> Yeah, give me the whole expression.                                           
 20     |  >> So if we're going to apply Bayes' Rule to the probability of h given D. We    
 21     |  can move, turn it around and make it equal to the probably of D given H. And it  
 22     |  would be great if we could just stop with                                        
 23     |  that, but we can't. We have to now kind                                          
 24     |  of put them in the same space. So, we                                            
 25     |  multiply by the probability of H, and then we                                    
 26     |  divide by the probability of D. And sometimes                                    
 27     |  that's just a normalization and we don't have                                    
 28     |  to worry about it too much. But that's,                                          
 29     |  that's the bay, that's Bayes' rule right there.                                  
 30     |  >> So this is Bayes' rule. And it actually is                                    
 31     |  really easy to derive. It falls it follows directly from                         
 32     |  the chain rule in probability theory. Do you think it's                          
 33     |  worthwhile? Showing people that or just they should just accept it.              
 34     |  >> Well, I mean, you could just, you might be able to just see it. Just,         
 35     |  the, the thing on top of the, the                                                
 36     |  normalization, the probability of D given h times probability                    
 37     |  of h. That's actually the probability of D and                                   
 38     |  h together. Right. So the probability of h times the                             
 39     |  probability of d over h as you say also the                                      
 40     |  chain rule basically the definition of conditional probability in conjunctions   
 41     |  and if you move the probability of d over                                        
 42     |  to the left hand side you can see we're really                                   
 43     |  just saying the same thing two different ways. It's just                         
 44     |  the probability of h and d. So then we're done.                                  
 45     |  >> No, that's right. So I can write down                                         
 46     |  what you just said. And use different letters just                               
 47     |  to make it more confusing, so                                                    
 48     |  >> Oh good.                                                                      
 49     |  >> You can point out that the probability of A and B, by the chain rule, is      
 50     |  just the probability of A given B, times the                                     
 51     |  probability of B. But because order doesn't matter, it's                         
 52     |  also the case that the probability of A and B. Is the probability of b given a   
 53     |  times the probability of a. And that's just the                                  
 54     |  chain rule. And so if these two quantities equal                                 
 55     |  to one another's exactly what you say, I could say                               
 56     |  well, the probability of a given b is just the probability                       
 57     |  of b given a times the probability a divided by the                              
 58     |  probability of b. And that's exactly what we have over here.                     
 59     |  >> Good. So now that we've mastered that                                         
 60     |  all your Bayes are belong to us. [LAUGH]                                         
 61     |  >> How long have you been saying that?                                           
 62     |  >> The...just, only about 3 or 4 minutes.                                        
 63     |  >> [LAUGH] Fair enough. Okay, so we have Bayes's rule. And what's really nice    
 64     |  about Bayes's rule is that while it's a very simple thing, it's                  
 65     |  also true. It follows directly from probability theory. But more importantly for 
 66     |  machine learning, it gives us a handle to talk about. What it                    
 67     |  is we're exactly trying to do when we say we're trying to                        
 68     |  find the most probable hypothesis, given the data. So let's just take            
 69     |  a moment to think about what all these terms mean. We know                       
 70     |  what this term here means. The, it's just the probability of some                
 71     |  hypothesis given the data. But what do all these other terms mean?               
 72     |  I want to start with this term, the probability of                               
 73     |  the data. It's really nothing more than your prior belief of                     
 74     |  seeing some particular set of data. Now, and as you point                        
 75     |  out, Michael, often it just ends up to be a normalizing                          
 76     |  term and typically does not matter, though we'll see a couple                    
 77     |  of cases where it does matter, helps us to, to sort                              
 78     |  of think about a few things. But generally speaking, whatever it                 
 79     |  is Since the only thing that we care about is the                                
 80     |  hypothesis, we're trying to find that, the                                       
 81     |  probability of the data doesn't depend on the                                    
 82     |  hypothesis, so typically we ignore it, but it's nice to just be clear about what 
 83     |  it means. The other terms are a bit more interesting. They matter a little bit   
 84     |  more. This term here, the probability is the                                     
 85     |  probability of the data given the hypothesis right?                              
 86     |  >> Mm. Seems like learning backwards.                                            
 87     |  >> It does seem like learning backwards but                                      
 88     |  what's really nice about this quantity is that unlike                            
 89     |  the other quantity, the probability of the hypothesis given the data, it's       
 90     |  actually, turns out to be pretty easy to think about the likelihood that         
 91     |  we would see some data given that we were in a world                             
 92     |  where some hypothesis, h, is true. So there is a little bit of                   
 93     |  subtlety there and I, let me, let me unpack that subtlety a                      
 94     |  little bit. So we've been talking about the data if its sort of                  
 95     |  a thing that is floating out in air, but we know that the                        
 96     |  data is actually our training data. And it's a set of inputs and                 
 97     |  lets just say for the sake of argument we are                                    
 98     |  going to do classification learning, it's a set of labels that                   
 99     |  are associated with those inputs. So just to drive the                           
 100    |  point home, I'm going to call those d's, little d's. And                         
 101    |  so our data is made up of a bunch of                                             
 102    |  these training examples. And these training examples are whatever input that     
 103    |  we get coming from a teacher, coming from ourselves, coming                      
 104    |  from nature, coming from somewhere and the associated label that goes            
 105    |  along with them. So when you talk about the probability of the data given        
 106    |  the hypothesis, what you're talking about, well,                                 
 107    |  what's the likelihood that. Given that I've                                      
 108    |  got all of these Xis and given that I'm living in a world where                  
 109    |  this particular hypothesis that I would see                                      
 110    |  these particular labels. Does that make sense Michael?                           
 111    |  >> I see. Yeah, so, so I can imagine a                                           
 112    |  more complicated kind of notation where, we're, we're kind of accepting          
 113    |  the Xs as given. But the labels is what we are                                   
 114    |  actually saying is something that we want to assigned probability to.            
 115    |  >> Right so its not really that the x's matter in the sense                      
 116    |  that we are trying to understand those. What really mattes re the labels         
 117    |  that are associated with them. And we will see an example of that                
 118    |  in a moment. But I wanted to make sure that you get this subtled.                
 119    |  >> So in a sense then I guess you're saying that the probability of D given H    
 120    |  component, or, or quantity, is really like running                               
 121    |  the hypothesis. It's like, It's like labeling the data.                          
 122    |  >> Okay Michael, just to make sure we get this. Let's                            
 123    |  imagine we're in a universe, where the following hypothesis is true. It          
 124    |  returns true, in exactly the cases where some input number X, is                 
 125    |  greater than or equal to 10 And it returns false otherwise. Okay?                
 126    |  >> Yup.                                                                          
 127    |  >> Okay. So                                                                      
 128    |  here's a question for you. Let's say that our data was made up of exactly one    
 129    |  point. And that value set x equal to 7. Okay? What is                            
 130    |  the probability that the label associated with 7. Would be true.                 
 131    |  >> Huh. So you're saying we're in a world                                        
 132    |  where h is holding and that the h, h                                             
 133    |  is being used to generate labels. So it wouldn't                                 
 134    |  do that right? So, the probability ought to be zero.                             
 135    |  >> That's                                                                        
 136    |  exactly right and what's the probability that it would                           
 137    |  be false? 1 minus 0 [LAUGH] which we'll call 1.                                  
 138    |  >> Which we'll call 1. That's exactly right.                                     
 139    |  So it's, it's just that simple. That, the                                        
 140    |  probability of the data given the hypothesis, is                                 
 141    |  really about, given a set of x's, what's                                         
 142    |  the probability that I would see some particular                                 
 143    |  label. Now, what's nice about that is, is,                                       
 144    |  as you point out, is that, it's as                                               
 145    |  if we're running the hypothesis. Well, given a hypothesis,                       
 146    |  it's really easy, or at least it's easier usually, to compute                    
 147    |  the probability of us seeing some labels. So, this quantity is                   
 148    |  a lot easier to figure out than the original quantity that                       
 149    |  we're looking for. The probability of the hypothesis, given the data.            
 150    |  >> Yeah, I could see that. It's sort of reminding me a little                    
 151    |  bit of the Version Space, but I can't quite crystallize what the connection is.  
 152    |  >> Well that's, it's good you bring that up. Because I, I think in a             
 153    |  couple of seconds I'll give you an example                                       
 154    |  that might really help you to see that. Okay?                                    
 155    |  >> Okay.                                                                         


##  03 - Bayes Rule p2
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  >> So, let's look at the last quantity that                                      
 2      |  we haven't talked about so far. And that is the                                  
 3      |  probability of the hypothesis. Well, just like the probability of                
 4      |  D is the prior on the data, this is in                                           
 5      |  fact your prior on the hypothesis. So, just like                                 
 6      |  the probability of D is a prior on the data.                                     
 7      |  The probability of H is a prior on a particular                                  
 8      |  hypothesis drawn from the hypothesis space. So in other words,                   
 9      |  in encapsulates our prior belief that one hypothesis is likely                   
 10     |  or unlikely compared to other hypotheses. So in fact what's                      
 11     |  really neat about this from a sort of AI point                                   
 12     |  of view is that the prior As its called is in                                    
 13     |  fact our domain knowledge. So if every angle that we've                          
 14     |  seen so far, everything that we've said there's always some                      
 15     |  place where we stick in out domain knowledge. Are prior                          
 16     |  belief about the way the world works. Whether that's a similarity                
 17     |  metric for Knn It, it's something about which                                    
 18     |  features might be important, so we care about high                               
 19     |  information gain and decision trees, or our belief                               
 20     |  about the, the structure of a neural network. Those                              
 21     |  are prior beliefs, those are, that represents the                                
 22     |  main knowledge. And here in Bayesian Learning, here in                           
 23     |  this notion of, of Bayes' Rule, all of our                                       
 24     |  prior knowledge sits here in the probability or prior                            
 25     |  probability over the hypotheses. Does that all make sense?                       
 26     |  >> Yeah its really interesting I guess. So we talked about things like           
 27     |  kernels and similarity functions as ways                                         
 28     |  of capturing this kind of domain knowledge.                                      
 29     |  And I guess, I guess what its saying is that its maybe tending                   
 30     |  to prefer or assign higher probability to                                        
 31     |  hypothesis that group things a certain way.                                      
 32     |  >> exactly right. So, in fact, when you use something                            
 33     |  like Euclidian distance in K and N, what you're saying is,'Well,                 
 34     |  points that are closer together ought to have, similar labels, and so,           
 35     |  we would believe any hypothesis that puts points that are physically close to    
 36     |  one another to have similar outputs, we would say, are more likely than          
 37     |  ones that put points that are very close together to have different outputs.     
 38     |  >> Neat.                                                                         
 39     |  >> So let me just mention one last thing                                         
 40     |  before I give you a quiz, okay? So, see                                          
 41     |  if this makes sense, I'm a see if you                                            
 42     |  really understand Bayes' rule. So let's imagine that I wanted                    
 43     |  to know under what circumstances the, probability of a hypothesis, given the     
 44     |  data, goes up. What on the right side of the equation would                      
 45     |  you expect to change, go up or go down, or stay the                              
 46     |  same, that would influence whether the probability of a hypothesis goes up.      
 47     |  >> So the probability of the hypothesis given                                    
 48     |  the data, what could make that combined quantity                                 
 49     |  go up, so one is looking at the                                                  
 50     |  right hand side, the probability of the hypothesis,                              
 51     |  so, so if you have a hypothesis that has                                         
 52     |  a higher prior, has, is more likely to be                                        
 53     |  a good one. Before you see the data then                                         
 54     |  that would raise it after you see the data too.                                  
 55     |  >> Right.                                                                        
 56     |  >> And I guess the probability of the data given the hypothesis should           
 57     |  go up. Oh, which is kind of like accuracy. It's kind of like                     
 58     |  saying that if you pick a hypothesis that does a better job of                   
 59     |  labeling the data, then also your probability of the hypothesis will go up.      
 60     |  >> Right. Anything else?                                                         
 61     |  >> I guess the probability of the data going                                     
 62     |  down. But that's not really a change from the hypothesis.                        
 63     |  >> Right. But it is true that if those                                           
 64     |  goes down, then the probability in the hypothesis can and                        
 65     |  the data will go up. But as you point                                            
 66     |  out, it's not connected to the hypothesis directly. And I'll                     
 67     |  write in equation for you in, in just a                                          
 68     |  moment that'll kind of make that, I think, a little                              
 69     |  bit clearer. Okay, but you got all this, right? So                               
 70     |  I think you understand it. So we got Bayes' Rule.                                
 71     |  And, notice what we've done. We've gone from this sort                           
 72     |  of general notion of saying we need to find the best                             
 73     |  hypothesis, to actually coming up with an equation, that sort                    
 74     |  of makes explicit what we mean by that. That what we                             
 75     |  care about is the probability of some hypothesis given the                       
 76     |  data. That's what we mean by best. And that, that can                            
 77     |  be further thought as, the probablity of us seeing, some labels                  
 78     |  on some data, given hypothesis. Times the probability of the hypothesis,         
 79     |  even without any data whatsoever, normalized by the                              
 80     |  probability of the data. So let's play around with                               
 81     |  Bayes' rules a little bit and make certain that                                  
 82     |  we all, we all kind of get it. Okay?                                             
 83     |  >> Sure.                                                                         
 84     |  >> Okay.                                                                         


##  04 - Bayes Rule Quiz
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay Mike, are you ready for a quiz?                                             
 2      |  >> Uh-huh. Okay, so, here, let me, let me set up the, the situation for          
 3      |  you. So a man goes to see his doctor, okay, because his back hurts or something. 
 4      |  >> Aww.                                                                          
 5      |  >> And she gives him a, I know, it's really sad. It's his, the left side         
 6      |  of his lower back, he's been playing too                                         
 7      |  much racquetball. Anyway, so a man goes to                                       
 8      |  see a doctor, and she gives him a lab test. Now this test is pretty good,        
 9      |  okay? It returns a correct positive. That is,                                    
 10     |  if you have the thing that this lab test                                         
 11     |  is testing for, it will say you have it 98 percent of the time, okay? So it only 
 12     |  gives you a false positive two percent of the                                    
 13     |  time. And at the same time, it will return                                       
 14     |  a correct negative, that is if you don't have                                    
 15     |  what the lab test is testing for, it will                                        
 16     |  say you don't have it. 97% of the time,                                          
 17     |  so it has a false negative rate of only 3%.                                      
 18     |  >> Wait, hang on. So, just, what's his problem?                                  
 19     |  >> Oh, that's the question. So, the test                                         
 20     |  looks for a disease. So, give me a disease.                                      
 21     |  >> Spleen?                                                                       
 22     |  >> Okay, I like that. So the test looks for                                      
 23     |  spleentitis. Now spleentitis is such a rare disease that nobody's ever           
 24     |  heard of it, And it turns out that it's so rare that                             
 25     |  only about this fraction of the population has it. Okay?                         
 26     |  >> Mm-hm.                                                                        
 27     |  >> That make sense? So we're looking for spleentitis. It's a                     
 28     |  very rare disease, but this test is really good at determining                   
 29     |  whether you have it or determining whether you don't have it                     
 30     |  >> Can I tell you that, its,                                                     
 31     |  spleentitis appeared zero times in google. [LAUGH] So                            
 32     |  it really is quite rare.                                                         
 33     |  >> It really is quite rare. But what does                                        
 34     |  google know? OK, so you got it all Michael?                                      
 35     |  >> Yeah. So its a really rare disease                                            
 36     |  and we have a very accurate test for it.                                         
 37     |  >> Good. Man goes to see the doctor. She gives him a lab test. Its a             
 38     |  pretty good lab test. Its checking for spleentitis,                              
 39     |  relatively rare disease and the test comes back positive.                        
 40     |  >> Oh.                                                                           
 41     |  >> Yes. So, test is positive. So, here is the quiz question.                     
 42     |  >> Should we be                                                                  
 43     |  net, notifying his next of kin?                                                  
 44     |  >> Yes. Does he have spleentitis?                                                
 45     |  >> You said, just said he had spleentitis.                                       
 46     |  >> No, I said the test says he had spleentitis. Or the                           
 47     |  test looks for spleentitis, and the test came back positive. So, does            
 48     |  he have spleentitis? Yes or no? Alright, before I try to answer                  
 49     |  that can I just, ask for clarification, can I get a clarification?               
 50     |  >> Please.                                                                       
 51     |  >> So the 98 is a percentage and the                                             
 52     |  97 is a percentage, is .008 also a percentage?                                   
 53     |  >> No it's not.                                                                  
 54     |  So if I wanted to convert it to a percentage it would be .8%.                    
 55     |  >> Got it. Alright, now I think I have, what I need.                             
 56     |  >> Okay, alright, so, you think about it. Go.                                    


##  05 - Bayes Rule Quiz
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  >> Okay Michael, what's the answer?                                              
 2      |  >> Does he have spleentitis?                                                     
 3      |  >> Yes, does he have spleentitis?                                                
 4      |  >> I don't think we know, for sure.                                              
 5      |  >> Mm? What do mean by that?                                                     
 6      |  >> Well, I mean. It's a noisy and probabilistic world right. So the              
 7      |  test told us that things look like he has spleentitis and the test               
 8      |  is usually right. But the test is sometimes wrong and it can give                
 9      |  the wrong answer and that's really all we know, so we can't be sure.             
 10     |  >> Okay but if you had to pick one. If you had to yes or                         
 11     |  no, like our students they did when they took                                    
 12     |  the quiz. Which one would you pick? Yes or no.                                   
 13     |  >> So, I guess C the pants. I would just say, yes because the                    
 14     |  test says, yes but if I guess I was trying to be more precise, I                 
 15     |  may go through and work out the probability and I guess if it's more             
 16     |  likely to have than not to have, then I'd say and otherwise I'd say, no.         
 17     |  >> Okay. So how would you go about doing that? Walk me through it.               
 18     |  >> Based on the name of the quiz, I think I'd go with Bayes' Rule.               
 19     |  >> Okay. So [LAUGH]                                                              
 20     |  I like that. So Bayes' Rule, is everyone recall, is                              
 21     |  the probability of the hypothesis given the data is equal to                     
 22     |  the probability of the data given the hypothesis times the probability           
 23     |  of the hypothesis divided by the probability of the data. So,                    
 24     |  >> [LAUGH]                                                                       
 25     |  >> Let's write all that out. So what is the probability of spleentitis,          
 26     |  which I'm just going to write as an s. Given.                                    
 27     |  >> We're making jokes about spleentitis, but we                                  
 28     |  don't want that to be confused with splenitis,                                   
 29     |  which is a real thing and probably not very                                      
 30     |  pleasant. So apologies to anyone out there with splenitis.                       
 31     |  But this is spleentitis, which is really totally different.                      
 32     |  >> Is splenitis a real thing?                                                    
 33     |  >> Yeah.                                                                         
 34     |  >> :Really what is it?                                                           
 35     |  >> Enlargement and inflammation in the spleen and the spleen as                  
 36     |  a result of infection or possibly a parasite infestation or cysts.               
 37     |  >> So what you're saying                                                         
 38     |  is that's gross and we don't want to think about it. OK good so Woo okay, so the 
 39     |  probability of getting splentitis and probably isn't even real.                  
 40     |  >> Totally, its totally different, its definitely not real                       
 41     |  >> Yea definitely not. Given that we gotten a positive result and you say        
 42     |  that we should use Baye's rules so that would be in this case what?              
 43     |  >> So it's the same as                                                           
 44     |  the probability of the positive result given that you have spleentitis.          
 45     |  >> Mm-hm.                                                                        
 46     |  >> Times the probability, the prior probability of having spleentitis.           
 47     |  >> Mm-hm.                                                                        
 48     |  >> And I want to say normalize, but like                                         
 49     |  divided by the probability of a positive test result.                            
 50     |  >> And what would be, the probabili. The other option is that you                
 51     |  don't have spleentitis.                                                          
 52     |  >> Mm-hm.                                                                        
 53     |  >> Even though you got a positive result. And that would be equal to?            
 54     |  >> The probability of a positive result given you don't have spleentitis.        
 55     |  >> Mm-hm.                                                                        
 56     |  >> Times the prior probability of not having spleentitis.                        
 57     |  >> huh.                                                                          
 58     |  >> Divided by the, again the same thing. The probability of the                  
 59     |  test results. So that's, those two things added together, needed to be one.      
 60     |  >> Right.                                                                        
 61     |  But as you point out. If we just want to figure out which                        
 62     |  one is bigger than the other. We don't actually have to know this.               
 63     |  >> Hm, good point.                                                               
 64     |  >> So we can ignore it, okay. Okay, so, let's compute this. So, what             
 65     |  is in fact, the probability of me getting a plus, given that I have spleenitis?  
 66     |  >> Right. So it says in the setup, the                                           
 67     |  test results correct positive 98% of the time. So,                               
 68     |  I, I think that's what it means. It means                                        
 69     |  that if you really do have it, it's going to                                     
 70     |  say that you have it with that probability.                                      
 71     |  >> Okay, so That's just point nine eight. OK? And                                
 72     |  that's times the prior probability of having spleentitis which is?               
 73     |  >> .008.                                                                         
 74     |  >> Right. .008.                                                                  
 75     |  And what's that equal to?                                                        
 76     |  >> It is equal to. 0.0078.                                                       
 77     |  >> 0.00784.                                                                      
 78     |  >> Okay, fine. We can do the same thing over here. So                            
 79     |  what's the probability of getting a positive if you don't have spleentitis       
 80     |  >> So, the probability of a correct negative is 97%.                             
 81     |  That means if you really don't have it, it's going to                            
 82     |  say you don't have it, so probability of positive result                         
 83     |  given that you don't have it, that should be the 3%.                             
 84     |  >> That's exactly right. Times the prior                                         
 85     |  probability of not having spleentitis which is?                                  
 86     |  >> .992. 1- .008.                                                                
 87     |  >> That's right, and that is equal to?                                           
 88     |  >> .02976                                                                        
 89     |  >> So, which number is bigger?                                                   
 90     |  >> The one that has the larger significant digit.                                
 91     |  >> Which one of those two is that?                                               
 92     |  >> I mean, obviously, the one that's bigger is the, you don't have it.           
 93     |  >> That's right.                                                                 
 94     |  So the answer would be no.                                                       
 95     |  >> And in fact the probability is almost 80%.                                    
 96     |  >> Yeah.                                                                         
 97     |  >> Which is crazy. So, it's like, you go into the doctor, you've run a           
 98     |  test, the doctor says congratulations, you don't                                 
 99     |  have speentitis, because the test says you do.                                   
 100    |  >> That's right. [LAUGH]                                                         
 101    |  >> So, what does that tell you?                                                  
 102    |  >> That seems stupid.                                                            
 103    |  >> That does seem stupid, but what does                                          
 104    |  it tell you About Bayes' Rule. What is                                           
 105    |  Bayes' Rule capture. What is thing that make                                     
 106    |  the answer no, despite the fact, you have                                        
 107    |  a high reliability test that says yes.                                           
 108    |  >> I. Okay. So I guess, I guess the way to                                       
 109    |  think about it is, a random person showing up in the                             
 110    |  doctors office, is very unlikely to have this particular disease. And            
 111    |  even the tiny, little, small percentage probability that the test would give     
 112    |  a wrong answer is completely swamped by the fact that you                        
 113    |  probably don't have the disease. But I guess this isn't really factoring         
 114    |  in the idea that, you know, presumably this lab test was                         
 115    |  run for some other reason. There was some other evidence that there              
 116    |  was concern.                                                                     
 117    |  >> Or the doctor just really wanted some                                         
 118    |  more money, because She needs a new boat.                                        
 119    |  >> Yeah, I know a lot of doctors.                                                
 120    |  >> I do too.                                                                     
 121    |  >> And most of them don't work like that.                                        
 122    |  >> Yeah most, well most of them have PhD's not MD's. So, another                 
 123    |  way of summarizing what you just said Michael, I think, is that priors matter.   
 124    |  >> I want to say the thing that I got out of this is tests don't matter.         
 125    |  >> Well, tests matter.                                                           
 126    |  >> Like what's the purpose of running a                                          
 127    |  test if if it's going to come back and say.                                      
 128    |  Well it used to be that I was pretty sure you didn't                             
 129    |  have it and now I am still pretty sure you don't have it.                        
 130    |  >> Well the point of running a test is                                           
 131    |  you run a test when you have a reason to                                         
 132    |  believe that the test might be useful. So what is                                
 133    |  the one thing, if I could only change one thing                                  
 134    |  without getting completely ridiculous, whats the easy well, I                    
 135    |  don't know whats easy, whats the easiest thing for me                            
 136    |  to change about this setup. I have three numbers here.                           
 137    |  This one, this one and this one. What would be                                   
 138    |  the easiest number to change?                                                    
 139    |  >> Well, in some sense none of the seem                                          
 140    |  that easy to change but I guess maybe what                                       
 141    |  you're trying to get me to say is that                                           
 142    |  if we look at a different population of people                                   
 143    |  then we can change that .008 number to something                                 
 144    |  else, like if we only give the test to                                           
 145    |  people who have other signs of spleentitis. Then then                            
 146    |  it, it would probably be a much bigger number.                                   
 147    |  >> Right, so changing the test, making the test better                           
 148    |  might be hard, presumably you know, billion of dollars of                        
 149    |  research have gone into that, but if you don't give the                          
 150    |  test to people who you don't have any reason to believe                          
 151    |  have Spleentitis, just walking off the street, as you put it,                    
 152    |  a random person walking off the street, then you can change                      
 153    |  the priors, so some other evidence. That you might have splentitis               
 154    |  might lead the prior to change, and then the test would                          
 155    |  suddenly be useful. So this, by the way, is an argument                          
 156    |  for why you don't want to just require that everyone take                        
 157    |  tests for certain things. Because if the prior probability is low, then          
 158    |  the test isn't very useful. On the other hand, as soon as                        
 159    |  you have any reason to believe We have strong evidence that someone              
 160    |  might have some condition, then it makes sense to test them for it.              
 161    |  >> So it's like a stop and frisk situation.                                      
 162    |  >> It's exactly like a stop and frisk                                            
 163    |  situation. I'm looking at you [INAUDIBLE]. Okay But in                           
 164    |  some sense, you're use of the word prior                                         
 165    |  is a little confusing there. So it's not that                                    
 166    |  we're changing the prior, it's that we're...we have                              
 167    |  some additional evidence that we can factor in. And                              
 168    |  I guess we can imagine that that's part                                          
 169    |  of the prior, but it seems like it's post-ilia.                                  
 170    |  >> Yeah, it does. And it, but... One way                                         
 171    |  to think about it, you actually, I think you                                     
 172    |  just captured it in what you just said, right?                                   
 173    |  Which is you can think of as a prior. Well,                                      
 174    |  a prior to what? So it's your prior belief                                       
 175    |  over a set of hypotheses, given the world you happen                             
 176    |  to be in. If you're in a world where                                             
 177    |  random people walk in to take a test for splentitis,                             
 178    |  then there's a low prior probability that they have it. If you're in a world     
 179    |  where the only people who come in are people who are from a population where     
 180    |  the prior probability is significantly higher, then                              
 181    |  you would have a different prior. It's really                                    
 182    |  a question about where you are in                                                
 183    |  the process when you actually formulate your question.                           
 184    |  >> So would it be worth asking people how, how likely would it have to be        
 185    |  that you have spleentitis to make this test                                      
 186    |  at all useful? Right, that would change a                                        
 187    |  positive, a positive result would actually change                                
 188    |  your mind about whether someone has it.                                          
 189    |  >> yeah, actually that, I think that's something that I,                         
 190    |  I'll leave for the for the, for the interested reader,                           
 191    |  where would that prior probability have to change so that                        
 192    |  getting a positive result, I would be more likely to believe                     
 193    |  that you actually have it than not. That does bring                              
 194    |  up a philosophical question, though, which is So what, just because              
 195    |  the priors have changed, doesn't mean that suddenly the test                     
 196    |  is useful, or that the test is going to give you an                              
 197    |  answer that somehow distinguishes and is this positive. And from                 
 198    |  a mathematical point of view, the question of whether this                       
 199    |  number is 0.008 or, or 0.8, you know, 8 10ths                                    
 200    |  of a percent, where does it change? Does it change                               
 201    |  at 5%? Or does it change at 50%? Or does                                         
 202    |  it change at 500%? It probably changes at 500%. You                              
 203    |  know, what, where is the place in which suddenly a                               
 204    |  positive result would make you believe they actually had spleentitis or          
 205    |  whatever disease you're looking for. Okay?                                       
 206    |  >> Okay.                                                                         


##  06 - Bayesian Learning
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay, Michael, so we've gotten through that quiz and you see                     
 2      |  that Bayes' rule actually gives you some information. It actually helps          
 3      |  you make a decision. So I'm going to suggest that, that whole                    
 4      |  exercise we went through was actually our way of walking through                 
 5      |  an algorithm. So here's a particular algorithm that follows from what            
 6      |  we just did. And let me just write that down for                                 
 7      |  you. All right, so here's the algorithm, Michael, so it's very                   
 8      |  simple. For each H in H, that is, each candidate hypothesis                      
 9      |  in our in our hypothesis space, simply                                           
 10     |  calculate the probability of that hypothesis given                               
 11     |  the data W which we know is equal to the probability of the data given           
 12     |  that hypothesis times the prior probability of                                   
 13     |  the hypothesis, divided by the probability of                                    
 14     |  the data. And then simply output whichever                                       
 15     |  process has maximum probability. Does that make sense?                           
 16     |  >> Yeah.                                                                         
 17     |  >> Okay, so I do want to point out that since                                    
 18     |  all we care about is computing the argmax, as before,                            
 19     |  we don't actually ever have to compute that little bit                           
 20     |  so, and that's a good thing because we don't always know                         
 21     |  what the prior probability on the data is, so we                                 
 22     |  can ignore it for the purposes of finding the maximal hypothesis.                
 23     |  >> So the place you removed it from, it seems like that's not actually valid,    
 24     |  because it's not the case that the probability of h given d equals, it's the     
 25     |  probability of d given h times the probability of h. It just means that we       
 26     |  don't care what the probability is when                                          
 27     |  we go to compute the argmax. That's right,                                       
 28     |  so, in fact, it's probably better to say that I'm going to approximate           
 29     |  the probability hypothesis given the data                                        
 30     |  by just calculating the probability of the                                       
 31     |  data given the hypothesis times the probability of the hypothesis and just go    
 32     |  ahead and ignore the denominator. Precissely                                     
 33     |  because it doesn't change hte maximal age.                                       
 34     |  >> Yeah, so it's, it's nice that that goes away.                                 
 35     |  >> Right, because it's hard to know, often what                                  
 36     |  the prior, what the prior probability over the data is.                          
 37     |  >> It would                                                                      
 38     |  be nice if we didn't have to worry about the other one, either.                  
 39     |  >> Which other one?                                                              
 40     |  >> The probability of h, where's that coming from?                               
 41     |  >> right, so where does that come from? So that's                                
 42     |  a deep philosophical question. Sometimes it's just something you believe, and    
 43     |  you can write down. And sometimes it's a little harder. And                      
 44     |  that's actually good that you bring that up. When we compute,                    
 45     |  our probabilities this way so it's actually got a name,                          
 46     |  it's the MAP or the maximum a posteriori hypothesis and that                     
 47     |  makes sense, it's the biggest posterior given all of your                        
 48     |  priors. But you're right Michael that often it's just as hard                    
 49     |  to say anything particular about your prior over the hypothesis                  
 50     |  as it is to say something about your prior of the                                
 51     |  data and, so it is very common to drop that. And,                                
 52     |  in dropping that, we're actually computing the argmax over the probability       
 53     |  of the data given the hypothesis. And,                                           
 54     |  that is known as the maximum likelihood hypothesis.                              
 55     |  >> I guess you can't call it the maximum                                         
 56     |  A priori hypothesis, because then it would also be MAP.                          
 57     |  >> Exactly, although I've never thought about that before.                       
 58     |  By the way, just just to be clear, we're                                         
 59     |  not really dropping this, in this case, what we                                  
 60     |  really said, is that, our prior belief is that                                   
 61     |  all hypotheses are equally likely. So we                                         
 62     |  have a uniform prior that is, the probability                                    
 63     |  of any given hypothesis is exactly the same                                      
 64     |  as the probability as any other given hypothesis.                                
 65     |  >> I see, so you're saying if, if we assume                                      
 66     |  that they all are equally likely, then, the choice of                            
 67     |  hypothesis doesn't change that term at all, the p of                             
 68     |  h term, so it really is equivalent to just ignoring it.                          
 69     |  >> Exactly, in some constant, we don't even have                                 
 70     |  to know what the constant is. But whatever it is,                                
 71     |  it's the same everywhere and therefor it doesn't affect                          
 72     |  the other terms or, in particular, affect the argmax computation.                
 73     |  >> So that's actually pretty cool right?                                         
 74     |  Once you think about what we just did.                                           
 75     |  We just took something that was very                                             
 76     |  hard. Computing the probability of a hypothesis given                            
 77     |  the data and turned it into something                                            
 78     |  much easier that is... Computing the probability of                              
 79     |  you seeing the data labels given a particular                                    
 80     |  hypothesis and it turns out that those are                                       
 81     |  effectively the same thing if you don't have                                     
 82     |  a strong prior. So that's really cool, so we're                                  
 83     |  done right? We now know how to find                                              
 84     |  the best hypothesis You're just finding the most likely                          
 85     |  hypothesis or the most probable one and that                                     
 86     |  turns out to be the same thing as just                                           
 87     |  simply finding the hypothesis that best matches the                              
 88     |  data. We're done its all, its easy. Everythings good.                            
 89     |  >> So,the math seems very nice and pretty and easy                               
 90     |  but is isn't it hiding a lot of work to actually                                 
 91     |  do these computations?                                                           
 92     |  >> Well, sure well well look you know                                            
 93     |  how to do multiplication that's pretty easy right?                               
 94     |  >> [LAUGH].                                                                      
 95     |  >> So I guess the only hard part                                                 
 96     |  is we have to look at every single hypothesis.                                   
 97     |  >> Yeah, that's just a slight, little, you know, issue.                          
 98     |  >> So, mathematically meaningful, but computationally questionable.              
 99     |  >> Hm.                                                                           
 100    |  >> So, the big point there, is that it's not practical. Well, unless the         
 101    |  number of hypotheses is really, really small. But as we know, a lot of           
 102    |  the hypotheses spaces that we care about, like, for example, linear separators,  
 103    |  are actually infinite. And so it's going to be very difficult to use             
 104    |  this algorithm directly. But despite all that, I think that there's still        
 105    |  something important that we get out of thinking about it this way                
 106    |  in just the same way that we get something important out of                      
 107    |  thinking about vc dimension. Even if we're not entirely sure how to              
 108    |  compute it in some particular case. This really gives us a gold                  
 109    |  standard, right? We have an algorithm,                                           
 110    |  at least a conceptual algorithm, that tells                                      
 111    |  us what the right thing to do would be if we're                                  
 112    |  capable of computing it directly. So, that's good because we can                 
 113    |  maybe prove things about this and compare results that we get                    
 114    |  from some Real live algorithms to what we might expect to                        
 115    |  get but also it turns out it's pretty cute because it                            
 116    |  helps us to say other things about what it is we                                 
 117    |  actually expect to learn. And I'm going to give you a couple                     
 118    |  examples of those just to sort of prove my point, sound good?                    
 119    |  >> Yeah.                                                                         
 120    |  >> Okay.                                                                         


##  07 - Bayesian Learning in Action
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  >> Okay Michael, so let's see if we can actually use this as a way               
 2      |  of deriving something maybe that we already                                      
 3      |  knew. So I'm going to go through a couple                                        
 4      |  of these because I I actually think,                                             
 5      |  well, frankly I just think it's kind of cool.                                    
 6      |  But, I I'm hoping I can convince you it's sort of cool too and that              
 7      |  we get something out of it. Okay, so let me set up the word, I'm                 
 8      |  going to set up a a problem, and it's going to be a kind of generic problem,     
 9      |  and I'm going to see what we can get out of it, okay? So this is                 
 10     |  machine learning, so we're going to be given a                                   
 11     |  bunch of data, so there are three assumptions                                    
 12     |  that I'm going to make here. The first is                                        
 13     |  that we're going to be given a bunch of labeled                                  
 14     |  training data, which I'm writing here as x sub i and d sub i, so x sub i         
 15     |  is whatever the input space is, and d sub i are these labels. And let's say, it  
 16     |  doesn't actually even matter what the labels are, but                            
 17     |  let's say that the labels are classification labels. Okay?                       
 18     |  >> Hm.                                                                           
 19     |  >> All right. And furthermore, not only we're given                              
 20     |  this data as examples drawn from some underlying concept c,                      
 21     |  but they're, in fact, noise-free. Okay? So they're                               
 22     |  true examples that tell you what c is. Okay?                                     
 23     |  >> Mm-hm.                                                                        
 24     |  >> So I'm going to say, in fact, let me write                                    
 25     |  that down because I think it's important. They're noise-free examples. Okay.     
 26     |  >> Like di equals c of xi.                                                       
 27     |  >> That's right, for all xi. So, the second assumption, is that the true         
 28     |  concept c, is actually in our hypothesis                                         
 29     |  space, whatever that hypothesis space is. And finally,                           
 30     |  we have no reason to believe that                                                
 31     |  any particular hypothesis in our hypothesis space is                             
 32     |  more likely than any other. And so, we have a uniform prior over our hypotheses. 
 33     |  >> So it's like the one thing we know is that we don't know anything.            
 34     |  >> That's right. So, sometimes people called this an uninformative prior         
 35     |  because you don't know anything. Except of course I've always thought that's     
 36     |  a terrible name because its a completely informative prior. In fact              
 37     |  its equally as informative as every other prior in that it tells                 
 38     |  you something that all hypothesis are equally likely. But that's                 
 39     |  >> I thought it was called an uninformed prior.                                  
 40     |  >> Is it? So its just an ignorant prior is what you're telling me. Yeah.         
 41     |  >> Okay. Well, then maybe that's the problem.                                    
 42     |  I just always had a problem with it                                              
 43     |  because people keep calling it uninformative and the                             
 44     |  really mean uninformed. Okay. In any case, so these                              
 45     |  are our, these are our assumptions. We've got                                    
 46     |  a bunch of data, it's noise free, the concept                                    
 47     |  is actually in the hypothesis base we care                                       
 48     |  about and we have a uniform prior. So we                                         
 49     |  need to compute the best hypothesis. So given                                    
 50     |  that we want to somehow compute the probability of                               
 51     |  some hypothesis given the data, right? That's just                               
 52     |  Bay's Rule. So, Michael, you've got the problem right?                           
 53     |  >> Yes.                                                                          
 54     |  >> [LAUGH]                                                                       
 55     |  okay. So in order to compute the probability of a hypothesis                     
 56     |  given the data, we just need to figure out all of these                          
 57     |  other terms. So let me just write down some of the terms                         
 58     |  and you can tell me what a you think the answer. Okay.                           
 59     |  >> Well, what was the question?                                                  
 60     |  >> The question is, while we want to compute some                                
 61     |  kind of expression for the probability of a hypothesis given                     
 62     |  the data. So given some particular hypothesis, I want to know                    
 63     |  what's the probability of that hypothesis given the data, okay?                  
 64     |  >> Yeah.                                                                         
 65     |  >> Okay, you got the setup. So, we're                                            
 66     |  going to compute that by figuring out these three                                
 67     |  terms over here. So, let's just pick, one                                        
 68     |  of them to do. Let's try the prior probability.                                  
 69     |  So Michael, what's the prior probability on H?                                   
 70     |  >> Did we say that it was a finite hypothesis class?                             
 71     |  >> It is a finite hypothesis class.                                              
 72     |  >> Then it's like, one over the                                                  
 73     |  size of that hypothesis class because it's uniform.                              
 74     |  >> Exactly right, uniform means Exactly that. Okay so we've got one of our       
 75     |  terms, good job. Lets pick another term. How about the probability of            
 76     |  data given the hypothesis. What's that?                                          
 77     |  >> The probability, so I guess noise free, and we know that it's                 
 78     |  noise free so it's always, so they're always going to be zeros and ones.         
 79     |  >> Mm-hm.                                                                        
 80     |  >> So, and it's going to be a question of whether or not                         
 81     |  the data is consistent with that hypothesis. Right, if the labels all match.     
 82     |  >> Right.                                                                        
 83     |  >> What we expect them to be if that really were the hypothesis, then            
 84     |  we get a one, otherwise we get a zero. That's exactly right. So let me           
 85     |  see if I can write down what I think you just said. The probability of the data, 
 86     |  given the hypothesis, is, therefor one if it's the case, that the labels         
 87     |  And the hypothesis agree for every single one of the training exercises. Right?  
 88     |  >> Yep                                                                           
 89     |  >> Is that what you said? Good. And if any of                                    
 90     |  them disagree, then the probability is zero. So that's actually very important.  
 91     |  It's important to, to understand exactly what it means for,                      
 92     |  to have the probability to get a hypothesis, as we                               
 93     |  mentioned before. That the English version of this is, what's                    
 94     |  the probability that I would see data with these labels in                       
 95     |  a universe where H is actually true. Which is different                          
 96     |  from saying that H is trure or H is false. It's                                  
 97     |  really a common about the labels that you see on                                 
 98     |  a data. In a universe, where H happens to be true.                               
 99     |  >> Okay, but you know, it's occurring to me now                                  
 100    |  that you wrote that down, that we've talked about this idea before.              
 101    |  >> When?                                                                         
 102    |  >> Well, so, like there's a shorter way of writing that. Which is                
 103    |  D of H equals one if H is in the version space of D.                             
 104    |  >> Huh, that's exactly right, that's exactly right. So, in                       
 105    |  fact, that will help us to compute the final term                                
 106    |  that we need, which is the probability of seeing the                             
 107    |  data labels. So, how do we go about computing that? Well,                        
 108    |  it's exactly going to boil down to the version space                             
 109    |  as you say, let me just write out a couple                                       
 110    |  of steps so that it's pretty Kind of easy to                                     
 111    |  see. It's sometimes easier in these situations to kind of break                  
 112    |  things up. So, the probability of the data sort of                               
 113    |  formally, is equal to just this. So we can write the                             
 114    |  probability of the data as being, basically, a marginalized version              
 115    |  of the probability of the data given each of the hypotheses                      
 116    |  times the probability of the hypotheses. Now, this is only                       
 117    |  true in a world where our hypotheses are mutually exclusive.                     
 118    |  Okay so let's assume we are in that world because                                
 119    |  frankly that's what we always assume and this little trick                       
 120    |  is going to workout for us because we are going to                               
 121    |  get to take advantage of two terms that we already                               
 122    |  computed naming the probability that the data given the hypothesis               
 123    |  and the probability of a particular hypothesis so we know that                   
 124    |  prior probability of a hypothesis is right, its                                  
 125    |  just one over the side of the hypothesis space                                   
 126    |  and how am I going to substitute in this equation                                
 127    |  for the probability of the data given the hypothesis?                            
 128    |  >> So, I don't know. I would                                                     
 129    |  write that differently. I mean, it's basically it's                              
 130    |  like the indicator function on whether or hot HI is in the virtual space of D.   
 131    |  >> Right, that's exactly right. So in fact this is not a good                    
 132    |  way to have written it. Let's see if I can come up with a,                       
 133    |  a good notational way of doing it. Let's                                         
 134    |  say, for every hypothesis that is in the                                         
 135    |  version space of the hypothesis space given the                                  
 136    |  labels that we've got. Okay? How's that count?                                   
 137    |  >> Okay.                                                                         
 138    |  >> So rather than having to come                                                 
 139    |  up with an indicator function, I'm just going to                                 
 140    |  define vs as the subset of all                                                   
 141    |  those hypotheses that are consistent with the data.                              
 142    |  >> Yeah exactly                                                                  
 143    |  >> Okay, and so whats the probability of those?                                  
 144    |  >> One It's one and it's zero otherwise, so then,                                
 145    |  we can simplify the sum and it's simply what? ?                                  
 146    |  >> The sum of the one, ooh! The                                                  
 147    |  one of each doesn't even depend on the hypothesis.                               
 148    |  >> mm-mh!                                                                        
 149    |  >> I see wait I don't see oh yes I do, I do its one over the size                
 150    |  of virgin space. No its the size of the                                          
 151    |  virgin space over the size of the hypothesis space.                              
 152    |  >> That's exactly right.                                                         
 153    |  Basically for every single hypothesis in the virgin space we're                  
 154    |  going to add one and how many of those are?                                      
 155    |  Well the size of the virgin space number of those.                               
 156    |  And multiply all that by one over the size hypothesis space,                     
 157    |  and so the probability the data is that term. So                                 
 158    |  now we can just substitute all of that, into our                                 
 159    |  handy dandy equation up there, and let's just do that.                           
 160    |  So the probability of the hypothesis given the data, is the                      
 161    |  probability of the data given the hypothesis Which we know is one for all those  
 162    |  that are consistent, zero otherwise. The probability                             
 163    |  of the prior probability over the hypothesis is                                  
 164    |  just one over the size of the hypothesis space, and the probability of the data  
 165    |  is the size of the version space Over the size of the hypothesis base which,     
 166    |  when we divide everything out, is simply this. Got it?                           
 167    |  >> Got it.                                                                       
 168    |  >> So, what does that all say? It says that, given a bunch of data, your         
 169    |  probability of a particular hypothesis being correct, or being the best one      
 170    |  or the right one, is simply uniform over all of the hypotheses that are          
 171    |  in the virgin space. That is, are consistent with the data that we see.          
 172    |  >> Nice.                                                                         
 173    |  >> It                                                                            
 174    |  is kind of nice. And by the way, if it's                                         
 175    |  not consistent with it, then it's zero. So, this is                              
 176    |  only true for hypotheses that are still in A                                     
 177    |  version space and zero otherwise. Now notice that all of                         
 178    |  this sort of works out only in a world                                           
 179    |  where you really do have noise free examples, and you                            
 180    |  know that the concept is actually in your hypothesis space                       
 181    |  and, just as crucially that you have a uniform prior                             
 182    |  for all the hypotheses. Now this is exactly the algorithm that                   
 183    |  we talked about before right. We talked about before what would                  
 184    |  we do. To kind of decide whether a hypothesis was good                           
 185    |  enough in this sort of noise-free world. And the answer we came                  
 186    |  up with is you should just pick one of them that's                               
 187    |  in the version space. And what this says is there's no reason                    
 188    |  to pick one over the other from the version space. They're                       
 189    |  all equally as good or rather equally as likely to be correct.                   
 190    |  >> Yeah,                                                                         
 191    |  that follows.                                                                    
 192    |  >> Yeah. So there you go. So it turns out you                                    
 193    |  can actually do something with this. Notice by the way that we                   
 194    |  did not pick a particular hypothesis space, we did not pick                      
 195    |  a particular form of our instance space, we did not actually say                 
 196    |  anything at all about exactly what the labels were other than                    
 197    |  that they were labels of some sort. The strongest assumption that we             
 198    |  made was a uniform prior, so this is always the right thing                      
 199    |  to do. At least in a Bayesen sense in a world where                              
 200    |  you've got noise free data, you have to find that hypothesis space, and          
 201    |  you have uniform priors. Just pick                                               
 202    |  something from the consistent set of hypotheses.                                 


##  08 - Noisy Data
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Alright, Michael, I got a quiz for you, okay?                                    
 2      |  >> Sure.                                                                         
 3      |  >> So, in the last example we had noise free data.                               
 4      |  So I want to think a little bit about what happens if we                         
 5      |  have some noisy data. And so I'm going to come up with                           
 6      |  a really weird, noisy model. But hopefully it illustrates the point. Okay.       
 7      |  >> Sure.                                                                         
 8      |  >> Okay so i got a bunch of training data, its x of i d                          
 9      |  of i and here's how the true underline process sort of works. So give us some    
 10     |  particular x of i, you get a label which is                                      
 11     |  d of i which is equal to k times x of                                            
 12     |  i where k is some number So one of the                                           
 13     |  counting numbers, one, two, three, four, five, six, seven, eight, and            
 14     |  so on and so forth. And the probability that you                                 
 15     |  actually get anyone of those multiples of x of i is                              
 16     |  equal to one over two to the k. Now why did                                      
 17     |  I choose one over two to the k? Because it turns                                 
 18     |  out that the sum of all those two to the k's from one                            
 19     |  through infinity happens to equal to                                             
 20     |  one. So it's a true probability distribution.                                    
 21     |  >> Hmm, okay.                                                                    
 22     |  >> So it's just a neat little geometric                                          
 23     |  distribution. So, you under understand the setup so far?                         
 24     |  >> I think so, so before hypothesis were producing                               
 25     |  answers then we looked for them to be exactly                                    
 26     |  in the data. Now we're saying that the hypothesis                                
 27     |  produces an answer, and it gets kind of smooshed around                          
 28     |  a little bit before it reappears in the table, thats the noisy part.             
 29     |  >> Right, so you, you're not going to be in a case now, that if                  
 30     |  the hypothesis disagrees with the label it sees. That in fact that means no it   
 31     |  can't possibly be the right hypothesis because                                   
 32     |  there's some stochastic process going on that might                              
 33     |  corrupt your output label, if you want to think                                  
 34     |  of it as corruption, since it's noisy. Okay?                                     
 35     |  >> Okay, yeah sure.                                                              
 36     |  >> Alright?                                                                      
 37     |  >> Okay, so here's                                                               
 38     |  a set of data that you got. Here's a bunch of x's that, that make                
 39     |  up our training data one, three, 11, 12,                                         
 40     |  and 20. For some reason they're in ascending                                     
 41     |  order. And the labels that go along with them are five, six, 11, 36, and 100. So 
 42     |  you'll notice that they're all multiples of some sort of the input x. Okay?      
 43     |  >> Alright.                                                                      
 44     |  >> Now I have a candidate hypothesis.                                            
 45     |  H of x which just returns x. That's kind of neat.                                
 46     |  So it's the identity function. So, what I want you to do                         
 47     |  is to compute the probability of seeing this particular data set in              
 48     |  a world where that hypothesis, the identity function, is in fact true.           
 49     |  >> The identity function plus this noise process.                                
 50     |  >> Yes.                                                                          
 51     |  >> And one other question quickly this, this noise                               
 52     |  process is supplied independently to each of these inputs,                       
 53     |  outputs, pairs?                                                                  
 54     |  >> Yes, absolutely.                                                              
 55     |  >> Okay, then, yeah, I think I can do that. Uh-huh.                              
 56     |  >> Okay, go.                                                                     


##  09 - Noisy Data
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay, Michael. You got the answer?                                               
 2      |  >> Yeah, I think, well I can work                                                
 3      |  through it, I don't actually have the number yet.                                
 4      |  >> Okay, let's do that.                                                          
 5      |  >> So, alright, so in a world where.                                             
 6      |  >> In a world where.                                                             
 7      |  >> Where this is the hypothesis that actually matters. We're saying that X       
 8      |  comes in, the hypothesis spits that same X out. And then this noise process      
 9      |  causes it to become a multiple. And the probability of a multiple is this        
 10     |  one over two to the case. So, the probability that that would happen from        
 11     |  this hypothesis. for the very first data item. The one to five, would be         
 12     |  1 32nd. That's the probability that a one would produce a five by this process.  
 13     |  >> Okay. How do you, how'd you figure that out?                                  
 14     |  >> Cause the k that we would need                                                
 15     |  the multiplier would have to be five. And so                                     
 16     |  the probability for that multiplier is exactly one over                          
 17     |  two to the five which is one 30 second.                                          
 18     |  >> Okay.                                                                         
 19     |  >> And so then I would use that same thought                                     
 20     |  process on the next one which says that it is doubled and the way that           
 21     |  this particular process would have produced a doubling                           
 22     |  would be if with, with probability a quarter.                                    
 23     |  >> Uh-hm.                                                                        
 24     |  >> And, the next data element would have                                         
 25     |  been produced by this process with probability at                                
 26     |  half, because it's k will be 1, and 1 over 2 to the k would be half,             
 27     |  >> Okay, I like this.                                                            
 28     |  >> Right? The next one will be an 8th, because its                               
 29     |  tripled,                                                                         
 30     |  >> Uh-hm.                                                                        
 31     |  >> And the last one is also a multiplier of 5, just                              
 32     |  like the first one, so that will be one thirty second as well,                   
 33     |  >> Mm-hm.                                                                        
 34     |  >> Alright but now we need to assign a probability                               
 35     |  to the whole data set, and because you told me it                                
 36     |  was okay to think about these things happening independently, the                
 37     |  probability that all these things would happen is exactly the product.           
 38     |  >> Right.                                                                        
 39     |  >> So I'll multiply a 32nd and a quarter and                                     
 40     |  1/2 and an 8th and a 32nd, so that's like a factor of 5 plus 2                   
 41     |  is 7 plus 1 is 8. Plus another                                                   
 42     |  3 is 11 plus another 5 is 16 and 2^16                                            
 43     |  is 65,536. So it should be 1 over, oh you already wrote it. 65,536. Yea that.    
 44     |  >> Yes that's absolutely correct Michael. Well done. Okay so,                    
 45     |  that's right, but you did it with a bunch of specific numbers. Is                
 46     |  there a more generic Is there a general form that we could write down?           
 47     |  >> Yeah, I think so, we're doing something pretty regular                        
 48     |  once I fell into a pattern. So, I took the D,                                    
 49     |  and divided by X, so D over X tells me                                           
 50     |  that the multiplier that was used, so that's like, the K.                        
 51     |  >> So. D over x gave you the k.                                                  
 52     |  >> And it was one                                                                
 53     |  over 2 to the that.                                                              
 54     |  >> Okay, so one over 2 to the that.                                              
 55     |  >> And it was then the product of, of that quantity for all of                   
 56     |  the data elements, so all the i's. So product over all the i's of that.          
 57     |  >> Okay.                                                                         
 58     |  >> But we have to be careful because If it                                       
 59     |  was the case that for any of our xi's the                                        
 60     |  d wasn't a multiple of it, that can't happen under                               
 61     |  this hypothesis and the whole probability needs to go to zero.                   
 62     |  >> Right.                                                                        
 63     |  >> So they all have to                                                           
 64     |  be divisible otherwise all bets are off.                                         
 65     |  >> Okay, so in other words if d of i mod x of                                    
 66     |  i is equal to zero and this formula holds and it's zero otherwise.               
 67     |  >> Exactly.                                                                      
 68     |  >> Okay. Sounds good. Okay, great Michael. So that's right and that              
 69     |  was exactly the right way of thinking about it. And now, what we're              
 70     |  going to do next, is we're going to take what we've just gone through.           
 71     |  This sort of process of thinking about, how to generate data labels. for,        
 72     |  you know, noisy cases and we're going to apply to it what I                      
 73     |  think you will find will be a pretty cool derivation. Sound good?                
 74     |  >> Awesome!                                                                      
 75     |  >> Excellent.                                                                    


##  10 - Return to Bayesian Learning
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay Michael, so that was pretty good with the quiz. I want to                   
 2      |  do another derivation and I want you to help me with it, okay?                   
 3      |  >> Hm. Cool.                                                                     
 4      |  >> Okay, so Michael, we have a similar                                           
 5      |  setup to what we've had before. We're given a                                    
 6      |  bunch of training data, XI inputs and DI                                         
 7      |  outputs. But this time we're dealing with real valued                            
 8      |  functions. So the way DIs are constructed is                                     
 9      |  there's some Deterministic function f, that we pass the                          
 10     |  fs through. And that gives us some value.                                        
 11     |  And that's really what we're trying to figure out.                               
 12     |  What is the underlying f? But to make our job                                    
 13     |  a little bit harder, we have noisy outputs. So, for every                        
 14     |  single DI that is generated, there's some small error, epsilon                   
 15     |  that is added to it. Now, this particular error term, is                         
 16     |  in fact drawn from a normal distribution with zero mean                          
 17     |  and some variance. We don't know what the variance is. It's                      
 18     |  going to turn out. It doesn't actually matter. There's some variance             
 19     |  going on here. The important thing is that there's zero mean.                    
 20     |  So, you got it?                                                                  
 21     |  >> And it's important that it's probably the same variance for all the data.     
 22     |  >> That's right, in fact, each of these epsilon sub i's are drawn iid.           
 23     |  >> And is that f, are we assuming it's linear?                                   
 24     |  >> Nope, we're not assuming that it's linear.                                    
 25     |  >> Okay.                                                                         
 26     |  >> It's just some function.                                                      
 27     |  >> All right, I'm with you.                                                      
 28     |  >> Okay, so you got it?                                                          
 29     |  >> Yep.                                                                          
 30     |  >> All right. So, here's my question                                             
 31     |  to you. What is The maximum likelihood hypothesis.                               
 32     |  >> Do we know f? Can I just say f?                                               
 33     |  >> No,                                                                           
 34     |  we don't know f. All we see are x sub i's and d sub i's. But we                  
 35     |  know there is some underlying f. And we                                          
 36     |  know that it's noisy, according to some normal distribution.                     
 37     |  >> I don't know how I would find that.                                           
 38     |  >> Well let's try to walk it through. So.                                        
 39     |  We know how to find the maximum likelihood hypothesis, at                        
 40     |  least we know an equation for it. The maximum                                    
 41     |  likelihood hypothesis is simply the one that maximizes this expression.          
 42     |  >> Right. That was when we assumed a uniform                                     
 43     |  prior on the hypotheses.                                                         
 44     |  >> Exactly. And so we, this is sort of the easiest                               
 45     |  case to think about Where it turns out that finding the                          
 46     |  hypothesis that best fits the data is the same as finding                        
 47     |  a hypothesis that describes the data the best. If you make an                    
 48     |  assumption about a uniform distribution, or a uniform prior. Okay, so.           
 49     |  This is all we have to do now is figure out                                      
 50     |  what we're going to do to expand this expression. So what do                     
 51     |  you think we should do first? The probability of the data given                  
 52     |  the hypothesis. Right. So each we assumed IID.                                   
 53     |  >> Mm-hm.                                                                        
 54     |  >> You actually helpfully even wrote that down.                                  
 55     |  So we can expand that into the product                                           
 56     |  over all the data elements of the probablity                                     
 57     |  of that data element given the hypothesis. And x.                                
 58     |  >> Okay, so let's do that, Michael.                                              
 59     |  Let's write that out. So, finding the hypothesis                                 
 60     |  that maximizes the data that we see, as you point out, is just a product         
 61     |  over each of the independent data that we                                        
 62     |  see. Or datums. So that's good. That's one                                       
 63     |  nice step. So we've gone from talking about                                      
 64     |  all of the data together to each of the                                          
 65     |  individual training data that we see. So what                                    
 66     |  do we do next? What is the probability                                           
 67     |  of seeing one particular P sub i, given that we're in a world where H is true.   
 68     |  >> So okay, given that H is true that means whatever the corresponding xi        
 69     |  is, if we push that through the f function, then the di is going to              
 70     |  be F of XI plus some error term soI guess if we took di minus                    
 71     |  F X I, that would tell us what the error term is and the we                      
 72     |  just need an expression for saying how likely it is that we get that much error. 
 73     |  >> Right, so, what is the expression that tells us that?                         
 74     |  >> I'm guessing it's something that uses the                                     
 75     |  normal distribution, it probably has an E in it.                                 
 76     |  >> [LAUGH] I think that' s absolutely right.                                     
 77     |  So, let's be particular about what you said. So, when                            
 78     |  you say that we should push it through F of X,                                   
 79     |  let's be clear that that's basically what H is supposed                          
 80     |  to be. Our goal here is, given all of this training                              
 81     |  data, lets recover what the true f of x is.                                      
 82     |  And that's what our H is. Each of our hypotheses a                               
 83     |  guess about what the true underlying deterministic function F is.                
 84     |  So, if we have some particular labels, some particular value D                   
 85     |  sub I that is at variance with that. What's the probability of us                
 86     |  seeing something that far away from the                                          
 87     |  true underlying F. Well, it's completely determined                              
 88     |  by, the noise model. And the noise is a Gaussian. So, we can                     
 89     |  actually write down Gaussian. Do you remember                                    
 90     |  what the equation for a Gaussian is?                                             
 91     |  >> Yes. It's exactly something that has an E in it.                              
 92     |  >> That's right. So I'll see, I'm going to start writing it                      
 93     |  and you see if you remember any of what I'm writing down.                        
 94     |  >> E to the...                                                                   
 95     |  >> No.                                                                           
 96     |  >> Okay, good.                                                                   
 97     |  >> It's 1 over.                                                                  
 98     |  >> E to the.                                                                     
 99     |  >> No.                                                                           
 100    |  >> Okay.                                                                         
 101    |  >> Square root of, it's, it's coming back to you now. 2 pi sigma squared.        
 102    |  >> Okay.                                                                         
 103    |  >> Times...                                                                      
 104    |  >> I was going to put that in after.                                             
 105    |  >> Oh, okay. So now you get your E, so E to the what?                            
 106    |  >> It's going to be the value, which, in our case, is, like, H of XI             
 107    |  minus DI.                                                                        
 108    |  >> Yeah. And then I feel like, we probably square that?                          
 109    |  >> Yep.                                                                          
 110    |  >> And then we divide by sigma squared?                                          
 111    |  >> right.                                                                        
 112    |  >> Really?                                                                       
 113    |  >> Yeah.                                                                         
 114    |  >> Sweet!                                                                        
 115    |  >> And your missing one tiny thing.                                              
 116    |  >> There needs to be another two.                                                
 117    |  >> Yes. And in fact it's minus one half.                                         
 118    |  >> Got it.                                                                       
 119    |  >> So, this is exactly the form of the Gaussian                                  
 120    |  in the normal distribution. And what it basically says is the                    
 121    |  probability me seeing some particular point, in this case DMI. Given             
 122    |  that the mean is H of X. Which is to say                                         
 123    |  that's the underlying the function. Is exactly this expression. E to             
 124    |  the minus one half, of the distance from the mean, squared,                      
 125    |  divided by the merits. Okay. And that's just, you either remember                
 126    |  that or you don't. But that's just the definition of a                           
 127    |  Gaussian. So that means the probability of us seeing the data                    
 128    |  is the product of the probability of us seeing each of                           
 129    |  the data items. And that's just the product of this expression                   
 130    |  here. Good. Now, we need to simplify this. We could stop here                    
 131    |  because this is true, but we really need to simplify this and                    
 132    |  I think it's pretty... Not to hard to do. It's pretty easy.                      
 133    |  >> Mm..hm.                                                                       
 134    |  >> What kind of trick do you think we would do here to simplify this?            
 135    |  >> So, first thing I would do is, noticed that the 1 over square root 2 pi       
 136    |  sigma square doesn't depend on i at all, and                                     
 137    |  maybe move it outside the pi but then realize,                                   
 138    |  well, actually since we're doing an argmax anyway, it's not going to have        
 139    |  any impact at all. [CROSSTALK] I would just like cross that baby out.            
 140    |  >> I like that. No point in keeping it. All right, now I'm                       
 141    |  hoping that the other sigma squared we can make that go away too.                
 142    |  So I'm tempted to just cross it out, but I'd rather, I'd be                      
 143    |  much more happy if I had a good explanation for why that's okay.                 
 144    |  >> Well, so what's the normal trick,                                             
 145    |  so we're trying to maximize the function,                                        
 146    |  right? What you just said is we can get rid of this particular constant          
 147    |  expression because it doesn't affect the max.                                    
 148    |  What's making it hard for you to get                                             
 149    |  rid of the sigma squared here is that                                            
 150    |  it's being passed through some exponential and you                               
 151    |  can't remember off the top of your head                                          
 152    |  what clever work you can do with constants                                       
 153    |  inside of exponentials. So it would be nice                                      
 154    |  if we could get rid of the exponential.                                          
 155    |  >> Very good. So because log is concave.                                         
 156    |  >> No, because it's monotonic.                                                   
 157    |  >> um-hm. We can take the log of the whole shabang. So this is going to          
 158    |  be equal to the argmax of the sum of the log of that expression, which           
 159    |  is going to move the thing to the outside and the log of E, so that's            
 160    |  going to be good, so it's going to be                                            
 161    |  the sum of the superscript thing, the power.                                     
 162    |  >> Right. So let's write that down. Okay, so just                                
 163    |  to be sure that that was clear to everybody, let's just                          
 164    |  point out that we basically took the log of both, the                            
 165    |  natural log of both sides, and so we said, instead of                            
 166    |  trying to find the maximum hypothesis or the maximum likelihood hypothesis       
 167    |  by evaluating this expression directly, we instead evaluated the log of          
 168    |  that expression. And as you'll recall from intermediate algebra, the log         
 169    |  of a product is the same as the sum of the                                       
 170    |  logs, and the log of E to something is just that thing.                          
 171    |  >> As long as we do natural log.                                                 
 172    |  >> As long as we do natural log when we have E. If we were doing                 
 173    |  something to the, 2 to the power of something, we'd want to do log base 2. Okay. 
 174    |  >> Got it. And you said to do it to both sides but we really didn't need to      
 175    |  do it to both sides we just needed to                                            
 176    |  do it inside the things we taking the argmax.                                    
 177    |  >> That's correct. Okay, so we've got here. So,                                  
 178    |  is there any other simplifying that we can do.                                   
 179    |  >> Yeah, yeah now it seems much clearer                                          
 180    |  so the. The negative one half divided by sigma                                   
 181    |  squared all can move outside the sum cause it doesn't depend on I at all.        
 182    |  >> Right. And then the sigma squared you                                         
 183    |  said that before you said that that wasn't going                                 
 184    |  to turn out to matter. Both sigma squares ended                                  
 185    |  up, you know, getting tossed into the rubbish heap.                              
 186    |  >> That's right.                                                                 
 187    |  >> And I want to be careful with the negative sign. Like I feel like             
 188    |  the half can go and the sigma square can go but the negative has to stay.        
 189    |  >> You're right. The half can go. And the sigma squared                          
 190    |  can go. So that leaves us with this expression. So I've taken,                   
 191    |  gotten rid of the one half, like you                                             
 192    |  suggested. Got rid of the sigma squared like you                                 
 193    |  suggested, and I moved the minus sign outside                                    
 194    |  of the summation. And I'm left with this expression.                             
 195    |  >> I have a thought about getting rid of that minus sign.                        
 196    |  >> Well how would you get rid of a minus sign?                                   
 197    |  >> So the max of a negative is the min. Right, so we can                         
 198    |  get rid of the minus sign by                                                     
 199    |  just simply minimizing instead of maximizing that expression.                    
 200    |  We end up with this expression.                                                  
 201    |  >> Nice. That's much simpler than where we started. The e is gone.               
 202    |  >> It's much simpler. We got rid of a bunch                                      
 203    |  of e's. We got rid of a bunch of turns                                           
 204    |  out extraneous constants. We got rid of multiplication. We did                   
 205    |  a bunch of stuff, and we ended up with this.                                     
 206    |  >> You know, we got rid of two pis. It's kind of sad I would like some pie.      
 207    |  >> Mm, I wonder what kind of pie it was?                                         
 208    |  >> Pecan pie?                                                                    
 209    |  >> [LAUGH]                                                                       
 210    |  >> Okay, so we got this expression, and that's kind of                           
 211    |  nice on your own you say, but actually it's even nicer                           
 212    |  than that.                                                                       
 213    |  >> What?                                                                         
 214    |  >> What does this expression remind you of Michael?                              
 215    |  >> The Sum of Squares.                                                           
 216    |  >> This is exactly it. This is, in                                               
 217    |  fact. The sum of squared error, which is awesome.                                
 218    |  >> Yeah, whoever decided it would be a good idea                                 
 219    |  to model noise as a Gaussian was really on to something.                         
 220    |  >> Mm-hm. Now, think about what this                                             
 221    |  means, Michael. We just took, using Bayesian Learning,                           
 222    |  a very simple idea of maximizing a likelihood.                                   
 223    |  We did nothing but substitution, here and there.                                 
 224    |  With the noise model. We got rid of a bunch of things                            
 225    |  that we didn't have to get rid of. We cleverly used the natural                  
 226    |  log. Notice that the minus sign can be taken away with the                       
 227    |  min. And, we ended up with some of squared error. Which suggests that            
 228    |  all that stuff we were doing with back propagation. And, all these               
 229    |  other kinds of things we're doing with receptrons is the right thing to          
 230    |  do. Minimizing the sum of square error, which we've just been doing              
 231    |  before. Is in fact the right thing to do according to Bayesian learning.         
 232    |  >> Right in this                                                                 
 233    |  case meaning meaning what a Bayesian would say.                                  
 234    |  >> Meaning what a Bayesian would say which I believe                             
 235    |  is sort of right by definition. More importantly here it is.                     
 236    |  >> They certainly believe it.                                                    
 237    |  >> Well, they, they do frequently.                                               
 238    |  >> Oh! I see what you did there.                                                 
 239    |  >> No one will get that but, but us. Anyway,                                     
 240    |  the thing is this is the thing you should minimize if                            
 241    |  you're trying to find the maximum likelihood hypothesis. Now, I just             
 242    |  want to say something. That is beautiful. Absolutely beautiful. That you         
 243    |  do something very simple like finding the maximum [UNKNOWN]                      
 244    |  hypothesis and you end up deriving some of squared errors.                       
 245    |  >> So, just to make sure that                                                    
 246    |  I'm understanding. because I see some beauty here,                               
 247    |  but maybe not all of it. We didn't talk about what the hypothesis class here     
 248    |  was. Right, so, if you don't know                                                
 249    |  what the hypothesis class is... You're, you're kind                              
 250    |  of stalled at this point, but if we                                              
 251    |  say the hypothesis class is say linear functions.                                
 252    |  >> Mm-hm.                                                                        
 253    |  >> Then, what we're saying is we can do linear regression,                       
 254    |  because linear regression is exactly about minimizing the sum                    
 255    |  of the squares, right? So linear regression comes popping out                    
 256    |  of this kind of Bayesian perspective just like that, so                          
 257    |  is, is that part of what makes it so cool?                                       
 258    |  >> That is part of what makes it cool, but I                                     
 259    |  just think more generally about gradient descent right? The way gradient descend 
 260    |  works is you take a derivative by stepping in this, in                           
 261    |  this space of the air function, which is sum of squared error.                   
 262    |  >> I see, so you get gradient descend too.                                       
 263    |  >> Yes, you get all of the stuff that people have been doing.                    
 264    |  Now, there's a piece of beauty there, which is that we derived                   
 265    |  things like gradient descend and linear regression, all of the stuff we          
 266    |  were talking about before and we have an argument. For why it's                  
 267    |  the right thing to do at least in a Bayesian sense. But                          
 268    |  there's an even deeper beauty here, which is tied in with ugliness,              
 269    |  which is the reason this is the right thing to do, is                            
 270    |  because of the specific assumptions that we've made. So what were the            
 271    |  assumptions that we made? We assumed that there was some True deterministic      
 272    |  function that was mapping our x's to our in                                      
 273    |  this case our d's and that they were corrupted                                   
 274    |  say transmission error or line noise or however you                              
 275    |  want to think about it. They are corrupted by some                               
 276    |  noise that has a very particular form. Uncorrelated, independently               
 277    |  drawn, Gaussian noise, with mean zero. So the less pretty                        
 278    |  way of thinking about it is. Whenever you're trying                              
 279    |  to minimize the sum of squared error, you are in                                 
 280    |  fact assuming that the data that you have has been corrupted by                  
 281    |  Gaussian noise. And if it's corrupted by some other noise, or you're             
 282    |  actually not trying to model determinance function, of this sort. And then       
 283    |  you are in fact, possibly, in fact most likely doing the wrong thing.            
 284    |  >> I mean are there other noise models                                           
 285    |  that lead to some other kinds of learning.                                       
 286    |  >> Sure, pick any other model in here that does't look                           
 287    |  Gaussian at all, and you would end up with something else.                       
 288    |  I don't know what you would end up with because. You                             
 289    |  know, you couldn't do all these cute tricks with natural logs but                
 290    |  yes, you would end up with something different. And one question                 
 291    |  you might ask yourself is well, if I try to do minimizing                        
 292    |  the sum of the squared errors, or something for which this                       
 293    |  model was not the right one, what sort of bad things might                       
 294    |  happen? Here let me give you an example, let's imagine that we're                
 295    |  looking at this here, and our X's are, I don't know measurements                 
 296    |  of people. Okay? So height and weight. Something like that.                      
 297    |  >> Mm-hm.                                                                        
 298    |  >> And in fact let's make it, let's make it                                      
 299    |  let's make it even simpler than that. Let's imagine that our                     
 300    |  x is our height. And our outputs, our d's, are                                   
 301    |  say weight. And what we're trying to learn is some kind of                       
 302    |  function from height to weight. Now, this doesn't make a                         
 303    |  lot of sense to have a true [INAUDIBLE], but I'm trying                          
 304    |  to make a point here. So what we're saying here is                               
 305    |  that we, we measure our height and then we measure weight.                       
 306    |  That there's some simple relationship between                                    
 307    |  them that's captured by f. But, when                                             
 308    |  we measure the weight, we get a sort of noisy version of that                    
 309    |  weight. Okay? That seems reasonable. But                                         
 310    |  what's not reasonable is we're saying. Our                                       
 311    |  measurement of the weight is noisy, but our measurement of height is not.        
 312    |  >> Because if the x's are noisy, then this is not a valid assumption.            
 313    |  >> I see.                                                                        
 314    |  >> So, it seems to work                                                          
 315    |  a lot of the time and we have an argument for                                    
 316    |  when it will work, but it's not clear that this particular assumption            
 317    |  actually makes a lot of sense in the real world. Even                            
 318    |  though in practice it seems to do just fine. Okay, got it?                       
 319    |  >> I think so though I feel like if the error if you put                         
 320    |  an error term inside the f along with the x and f is say linear.                 
 321    |  >> Mm-hm.                                                                        
 322    |  >> Then maybe it pops out and it just becomes another                            
 323    |  part of the noise term and, and it all still goes through.                       
 324    |  Like I feel lines are still pretty happy even with that.                         
 325    |  >> No I think you're right. Lines would be happy here because                    
 326    |  linear, I mean linear functions are very nicely behaved in that way.             
 327    |  But of course, they'd have to be the same noise model in                         
 328    |  order for it to work the way you want it to work.                                
 329    |  >> Yeah.                                                                         
 330    |  >> They'd have to both be Gaussian. They have to both have                       
 331    |  zero mean, right? And they'd have to be independent of one another.              
 332    |  So your measuring device that gives you an error for your height                 
 333    |  would also have to give you an independent normal error for the weight.          
 334    |  >>                                                                               
 335    |  Yeah. Though I feel like my scale and my                                         
 336    |  yardstick actually are fairly independent. And they're Gaussian? .               
 337    |  >> Oh mine is clearly Gaussian.                                                  
 338    |  >> Yeah.                                                                         
 339    |  >> Yeah. Well at least they're normal.                                           
 340    |  >> They're normally are.                                                         
 341    |  >> Mm-hm.                                                                        
 342    |  >> Okay good. So let's move on to the next thing Michael. Let's try one          
 343    |  more example of this and, and then I hope that means you got it, okay?           
 344    |  >> Sure.                                                                         
 345    |  >> Beautiful.                                                                    


##  11 - Best hypothesis
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So before we go on to the next example, Michael, I wanted to                     
 2      |  do a quick quiz, just to make certain you really get what's going                
 3      |  on here. The, the sort of power of looking, using Bayesian learning. The,        
 4      |  the main insight, I think, I, I want to drive home here, is something            
 5      |  you said. Which is that, when we were doing regression before, when we           
 6      |  were talking about the perceptrons, we actually had in our head a particular     
 7      |  kind of function, a particular hypothesis class. In here with what been talking  
 8      |  about with Bayesian learning, the answer tto                                     
 9      |  finding to sum of squared errors was                                             
 10     |  independent of the hypothesis class and only dependent upon the                  
 11     |  key assumptions that we were making, mainly that we had                          
 12     |  labeled the data with certain form, and that that data                           
 13     |  was generated by a process that took deterministic function and                  
 14     |  added some Gaussian noise to it. So, here's the quiz.                            
 15     |  Here's your training data. You've got a bunch of Xs                              
 16     |  and a bunch of Ds. These are the values that                                     
 17     |  you have to learn. And I want you to tell                                        
 18     |  me, which of these three functions over here, these three                        
 19     |  hypotheses is the best one under this assumption. Got it?                        
 20     |  >> mod? Are we allowed to do that?                                               
 21     |  >> We are allowed to do that because                                             
 22     |  >> It's just a function.                                                         
 23     |  >> It's just a function, man.                                                    
 24     |  >> Interesting.                                                                  
 25     |  >> It's just a function.                                                         
 26     |  >> So we've got a linea-, a                                                      
 27     |  constant function, a linear function, and we've talked                           
 28     |  about those, but we've also got a mod                                            
 29     |  function. alright, and we've got a uniform prior                                 
 30     |  over these threes hypotheses.                                                    
 31     |  >> Yup.                                                                          
 32     |  >> Okay. Yeah, I think I can do that.                                            
 33     |  >> Okay. Go.                                                                     


##  12 - Best hypothesis
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Alright, we're back, what's the answer Michael?                                  
 2      |  >> So, you want me to work it through?                                           
 3      |  >> Sure.                                                                         
 4      |  >> So what I did first is I made it to, I extended the table that you had.       
 5      |  >> Okay.                                                                         
 6      |  >> To include each of these, the output for each of                              
 7      |  these three functions. What I'm basically, what I like to do is                  
 8      |  compute the squared error for each of these three functions on that              
 9      |  data and then choose the one that has the lowest squared error.                  
 10     |  >> Make total sense to me. Sounds good                                           
 11     |  enough to be an algorithm. Aren't you going                                      
 12     |  to write out the table?                                                          
 13     |  >> Well, I mean, I decided to do that, and then there                            
 14     |  was like one too many steps, and I just threw out my                             
 15     |  hand and just wrote this all down. Okay, so, we'll just say"                     
 16     |  Insert code here", because that's what you did, that was the step.               
 17     |  >> And, what did your code tell you?                                             
 18     |  >> Well, let me start with the constant function, because that's the             
 19     |  easiest piece of code. So, I'm saying what's the difference between each         
 20     |  of the D values and two. Squaring it all and summing it                          
 21     |  up and I get 19. And I can do the same thing,                                    
 22     |  instead of using two I use x over three take the difference of that              
 23     |  to the D values and square that and I get 19 point [INAUDIBLE] four, four,       
 24     |  four, four, four. Then I can do, right, so now at this point I'm                 
 25     |  rock and rolling. I can actually just substitute in my nine, and I get 12?       
 26     |  >> Not, not something-odd 12?                                                    
 27     |  >> No, just 12, so the error's 12. So that has the smallest error.               
 28     |  So even though that's sort of a crazy, like, stripy function                     
 29     |  right. Like, it increases linearly and then it resets at 9.                      
 30     |  >> Mmhmm.                                                                        
 31     |  >> It actually fits the state of the best.                                       
 32     |  >> That is correct. Your code is correct, Michael. Well done. Well actually,     
 33     |  looking at this data that sort of makes sense to me, right. Because              
 34     |  if you look at the first three examples. Of the data, the outputs                
 35     |  are very close. But the outputs of the next three are much bigger, and           
 36     |  by doing a mod nine, what you effectively do is                                  
 37     |  say, this is the identity function above this line. And then                     
 38     |  below the line, it's as if I'm sort of subtracting                               
 39     |  nine from all of them, and that makes them closer together.                      
 40     |  >> Hm.                                                                           
 41     |  >> And so it just happens to work out                                            
 42     |  here. But surely that's just because we came up                                  
 43     |  with a bad constant function and a bad linear                                    
 44     |  function. Do you think there's a better linear function?                         
 45     |  >> So I mean because it's the squared                                            
 46     |  error, we're really just talking about linear regression.                        
 47     |  >> Right.                                                                        
 48     |  >> So I can just run linear regression. So I get                                 
 49     |  an intercept of 0.9588 And a, and a slope of 0.1647.                             
 50     |  >> Okay                                                                          
 51     |  >> So that's, so that's my linear function of choice.                            
 52     |  >> Okay, so that's, what was, what was that again?                               
 53     |  >> So x times, you know, it's like a six, I guess, like 0.165 probably.          
 54     |  >> 0.165x                                                                        
 55     |  >> Plus                                                                          
 56     |  >> Mm hm.                                                                        
 57     |  >> Plus 0.959. So that's                                                         
 58     |  our function, that's our best linear function,                                   
 59     |  the function that minimizes greater. So it better                                
 60     |  end up being, it better end up being less than 19.4, or I'm a liar.              
 61     |  >> Mm-hm.                                                                        
 62     |  >> And now I need to take the difference                                         
 63     |  between that and D square it, and sum. 15.7.                                     
 64     |  >> Hm. So that gives you 15, I'm going to say 15.8. So that is better.           
 65     |  >> Yeah, so it's better than the X over three,                                   
 66     |  but it's also worse than the mod nie.                                            
 67     |  >> Hm.                                                                           
 68     |  >> and the best constant function, has to be worse, because the linear           
 69     |  functions include the constant functions as a subset, so this is, that 15.8 is.  
 70     |  Is better than the best constant function too. Oh its easy to do                 
 71     |  though right? Because the best constant function is just the mean of the data.   
 72     |  >> What is the mean of the data?                                                 
 73     |  >> 2.17.                                                                         
 74     |  >> huh two is pretty close.                                                      
 75     |  >> Yeah that's interesting.                                                      
 76     |  >> Well that's                                                                   
 77     |  >> Kind of in the middle of the pack                                             
 78     |  I guess.                                                                         
 79     |  >> That sort of works right because two the error                                
 80     |  for two was actually lower than the error for x divided                          
 81     |  by three. And for what it's worth the error for                                  
 82     |  2.17 as constant function to 2.2 is 8.8, 18.8, 18.8 sorry.                       
 83     |  >> Yeah, you're not the [INAUDIBLE].                                             
 84     |  >> Yeah, eight would have been less than everything.                             
 85     |  >> Okay. So, what have we learned here?                                          
 86     |  >> That sometimes you want to use mod.                                           
 87     |  >> Yeah.                                                                         
 88     |  >> If your data is weird. [LAUGH]                                                
 89     |  >> You have you                                                                  
 90     |  have definitely modified my box.                                                 
 91     |  >> Well I'm glad you found it mod. Hmm. [LAUGH]                                  
 92     |  PUNS. Okay, good, so I think that was                                            
 93     |  a good, that was, that was a good exercise.                                      
 94     |  So I'm going to give you one more example                                        
 95     |  of deriving something and then we're going to move on.                           
 96     |  >> Cool.                                                                         
 97     |  >> Okay.                                                                         


##  13 - Minimum Description Length
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  >> All right, Michael. So I, all I have written up                               
 2      |  here for you is, are a maximum a posteriori equation, right?                     
 3      |  So the best hypothesis is the one that maximizes this expression.                
 4      |  Nothing new, right? So I want to do a little trick, the                          
 5      |  same trick that you did before. So, you noticed that when                        
 6      |  we had E to the something, that we could use the                                 
 7      |  natural log on E to get rid of everything. So I                                  
 8      |  am going to try to do the same thing here. In the                                
 9      |  nat, why did the natural log work again?                                         
 10     |  >> Well, it's the inverse of the E, but it let us turn products into sums.       
 11     |  >> Right. And the other reason it worked is because it's a.                      
 12     |  >> Oh, it's monotonic.                                                           
 13     |  >> Right, it's a monotonic function and                                          
 14     |  so it doesn't change the argmax. So, I'm                                         
 15     |  going to do the log of both sides here. But this time I'm going to do            
 16     |  log base 2, for no particular reason other                                       
 17     |  than it'll turn out to help later. So,                                           
 18     |  I'm just going to take the log of                                                
 19     |  this entire expression, which, because it turns products                         
 20     |  into sums, gives me this. And by the way for                                     
 21     |  those of you who haven't noticed, I drew in a little                             
 22     |  bit of notation here. When you write just LG, it's just                          
 23     |  log base 2. Okay, so, we agree that the answer to                                
 24     |  this equation and the answer to this equation is the same.                       
 25     |  And now I'm going to do one other little trick, exactly                          
 26     |  the trick that you used before. I'm going to change my                           
 27     |  max into a min, by simply multiplying everything by minus 1.                     
 28     |  >> Okay, I don't quite see where you're going here.                              
 29     |  >> But you agree that                                                            
 30     |  we haven't changed the answer.                                                   
 31     |  >> I agree that we haven't changed the answer.                                   
 32     |  >> Okay. Do a log in there, do a minus                                           
 33     |  sign in there that took us from a max to a                                       
 34     |  min, but I haven't changed the answer. Now, do you recognize anything            
 35     |  about these expressions? I'll give you a hint. Information theory.               
 36     |  >> Okay. So, information theory is usually entropy,                              
 37     |  which is like some of P log P stuff.                                             
 38     |  >> Right.                                                                        
 39     |  >> I'm not seeing that.                                                          
 40     |  >> Well, there you, there's your log and there's your P.                         
 41     |  >> Sure. [LAUGH]                                                                 
 42     |  >> [LAUGH]                                                                       
 43     |  >> It's not P times that though.                                                 
 44     |  >> That's true. But we know from information theory, based exactly on this       
 45     |  notion of entropy, that the optimal code for some event with probability P has   
 46     |  length minus log base 2 of P. So, that just comes straight out of information    
 47     |  theory. That's where all the entropy stuff comes from. Okay. So, if we           
 48     |  have some event that has some particular probability P of happening,             
 49     |  the best code for it has this structure, minus log of P.                         
 50     |  >> Okay.                                                                         
 51     |  >> So, if we take this fact that we know, and                                    
 52     |  we apply it to here, what is this actually saying? This is                       
 53     |  saying that, in order to find the maximum a posteriori hypothesis,               
 54     |  we want to some how minimize two terms that can be described                     
 55     |  as lengths.                                                                      
 56     |  >> Okay. I can see that.                                                         
 57     |  >> So my question to you is, given that this definition over here, that an       
 58     |  event with probability P has some length minus                                   
 59     |  log P, what is this the length of?                                               
 60     |  >> So that would be the length of                                                
 61     |  the probability of the data given the hypothesis.                                
 62     |  >> Mm-hm.                                                                        
 63     |  >> And the length of the hypothesis, or the probability of the hypothesis.       
 64     |  >> Well no, it's just the length of that hypothesis.                             
 65     |  >> Oh, because the event is what has the length.                                 
 66     |  Oh, I see. So it's the length of the data,                                       
 67     |  given the hypothesis, and the length of the hypothesis.                          
 68     |  >> Right. So let's write that out.                                               
 69     |  >> But I was just doing, like, pattern matching                                  
 70     |  there. It's not clear to me what a length                                        
 71     |  of a hypothesis is. Hypotheses are functions. I don't                            
 72     |  know how to take a tape measure to a function.                                   
 73     |  >> That's fair. So this is the length of the hypothesis. Hypothesis. Right?      
 74     |  >> Yep.                                                                          
 75     |  >> So, you said you don't know what that means. But, let's think about           
 76     |  that out loud for a moment. What does it mean to have a length of                
 77     |  a hypothesis? That's really sort of the number of                                
 78     |  bits you need to describe a particular hypothesis, right?                        
 79     |  >> Okay.                                                                         
 80     |  >> Okay. And in fact, that's exactly what it means.                              
 81     |  That's why we use log base 2. So, if we want                                     
 82     |  to minimize the length of a hypothesis, what does that mean,                     
 83     |  the number of bits that we need to represent the hypothesis?                     
 84     |  >> The number of bits that we need to represent the hypothesis is, I guess,      
 85     |  in some representation, or, so in this case                                      
 86     |  I guess it would be some optimal representation.                                 
 87     |  We are taking all the different hypotheses and writing them out. The ones        
 88     |  that are more likely have a higher P of H, because that's the                    
 89     |  prior. And those are going to have smaller lengths than the optimal code.        
 90     |  And the ones that are less common are going to have longer codes.                
 91     |  >> Well, let's make it more concrete.                                            


##  14 - Which Tree
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So here are two decision trees, which one has the smallest link? Go.             


##  15 - Which Tree
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay, Michael. Which of these two decision trees is smaller?                     
 2      |  >> [LAUGH] The one on the right is smaller.                                      
 3      |  >> That's exactly right because it's easier, it's,                               
 4      |  it's easier to represent it in sort of almost                                    
 5      |  any obvious way that you could think of. It                                      
 6      |  has fewer nodes, so smaller decision trees, trees with                           
 7      |  fewer nodes, less depth, whatever you need to                                    
 8      |  make it smaller, have smaller lengths than bigger decision                       
 9      |  trees. So that means that if all we cared                                        
 10     |  about was the second term here. We would prefer                                  
 11     |  smaller decision trees, over bigger decisions trees.                             
 12     |  >> Which we do.                                                                  
 13     |  >> Which we do. Now what about this over here? The, what                         
 14     |  does it mean? So this is pretty straight forward. You got this right?            
 15     |  >> That the length of. Well, I mean guess                                        
 16     |  what's weird that you, you're kind of moving back and                            
 17     |  forth between a notion of a prior, which is                                      
 18     |  where the p of h came from and a notion                                          
 19     |  of Well, you know, if we're going to actually have                               
 20     |  to describe the hypothesis you're going to have to write                         
 21     |  it down in some way, and this gives you                                          
 22     |  a way of measuring how long it takes to write                                    
 23     |  it down. But I guess what this whole derivation                                  
 24     |  is doing is linking those two concepts, so that                                  
 25     |  you can think about our bias for shorter decision                                
 26     |  trees as actually being the prior, right? Actually being the                     
 27     |  thing that says the smaller ones are more likely                                 
 28     |  And vica versa, that when we think about things that                             
 29     |  are priors, that are assigning higher probability to certain                     
 30     |  things, it's kind of like giving them a shorter description.                     
 31     |  >> Right, so infact if you were to take                                          
 32     |  this example literally here, that we prefer smaller trees                        
 33     |  to bigger trees, this kind of a bayesian argument for occam's razor.             
 34     |  >> And pruning.                                                                  
 35     |  >> And pruning. Well, you, often use                                             
 36     |  razors to prune, so it makes perfect sense.                                      
 37     |  >> Ok, so this is kind of straight foreward, that basically smaller              
 38     |  trees are smaller than bigger trees. It sort of makes sense.                     
 39     |  Now, what about this over here? What does it mean to                             
 40     |  talk about the length of the data given a particular hypothesis.                 
 41     |  >> Uh...I could think of one interpretation there. So                            
 42     |  like, if the hypothesis generates the data really well, then                     
 43     |  you don't really need the data at all, right?                                    
 44     |  You just have...you already have the hypothesis. The data is                     
 45     |  free. Right? But if it deviates a lot from                                       
 46     |  the hypothesis, then you're going to have to have a long                         
 47     |  description of where the deviations are. So maybe it's kind of                   
 48     |  capturing this sort of notion of how well it fits.                               
 49     |  >> Right, that's exactly right. So I like that                                   
 50     |  explanation so let me write it down. So here                                     
 51     |  we literally just mean something like size of h.                                 
 52     |  But over here we are talking about, well sort                                    
 53     |  of error right? if the hypo, if just exactly what                                
 54     |  you said if the hypothesis perfectly describes the data,                         
 55     |  then you don't need any of the data. But lets                                    
 56     |  imagine that the hypothesis gets all of the data                                 
 57     |  labels wrong. Then when you send the hypothesis over To                          
 58     |  this person. This, this sort of person we're making up                           
 59     |  who, trying to understand the Daden hypothesis. And you're also                  
 60     |  going to have to send over what all the correct answers                          
 61     |  were. So, what this really is, is a notion of miss-classification                
 62     |  error, or just error in general. If we're thinking about                         
 63     |  regression. So, basically, what we're saying is, if we're trying                 
 64     |  to find the maximum Imposterior Hypothesis. We want to maximize this             
 65     |  expression. We want to find the age that maximizes this expression.              
 66     |  That's the same as finding the age that                                          
 67     |  maximizes the log of that expression, which gives you                            
 68     |  this. Which is the same as minimizing this expression,                           
 69     |  which is just maximizing this expression but throwing a                          
 70     |  minus one in front But these terms actually have meanings in information theory, 
 71     |  the best hypothesis, the hypothesis with the maximum [UNKNOWN] probability is    
 72     |  the one that minimizes error and the size of your hypothesis.                    
 73     |  You want the most simple hypothesis that minimizes                               
 74     |  your error. That is pretty much occums razor.                                    
 75     |  What is important here In reality is that                                        
 76     |  these are often traded off of one another.                                       
 77     |  If I give a more complicated or bigger                                           
 78     |  hypothesis, I can typically drive down my error.                                 
 79     |  Or I can have a little bit of error for a smaller hypothesis. But this is the    
 80     |  sort of fundamental tradeoff here. You want to find The simplest                 
 81     |  hypothesis that still explains your data, that is, minimizes your error.         
 82     |  >> Hm.                                                                           
 83     |  >> So this actually has a name, and                                              
 84     |  that is the minimum description, and there have                                  
 85     |  been many algorithms over the years that have                                    
 86     |  tried to do this directly by simply trading                                      
 87     |  off some notion of error, and some notion                                        
 88     |  of size. And finding the tradeoff between them                                   
 89     |  that actually works. Now, if you think about                                     
 90     |  it for a little whiel Michael you'll realize that                                
 91     |  yea this sort of makes sense at the hand wavy level                              
 92     |  at which I just talked about it. But, you do have some                           
 93     |  real issues here about for example units. So, I don't know if                    
 94     |  the units of the size of the hypothesis are directly comparable to               
 95     |  the counts of errors or you know sum of squared errors                           
 96     |  or something like that and so you have to come up with                           
 97     |  some way of translating between them... And some way of making the               
 98     |  decision whether you would rather minimize this or you'd rather minimize that    
 99     |  if you were forced to make a decision. But the                                   
 100    |  basic idea is still the same here. That the best                                 
 101    |  hypothesis is the one that minimizes error without paying too                    
 102    |  much of a price for the complexity of the hypothesis.                            
 103    |  >> Wow. So I've been sitting here thinking about, so with decision trees,        
 104    |  this notion of length feels... Like you could translate it directly into bits    
 105    |  right like you actually had to write it down and transmit it, it                 
 106    |  makes a lot of sense. But then I was thinking about neural networks.             
 107    |  And, and, and given that a fixed neural network architecture it's always         
 108    |  the same number of weights and they're just numbers. So you just                 
 109    |  transmit those numbers. So I thought, hmmm, this isn't really helping us         
 110    |  understand? ? ? ? ? ? and then it occurred to me                                 
 111    |  that those weights, if they get really you're going to need more                 
 112    |  bits to express those big weights. And in fact that's exactly when               
 113    |  we get over fitting with neural nets if we let the weights                       
 114    |  get too big. So like this gives a really nice story for understanding            
 115    |  neural nets as well.                                                             
 116    |  >> Right. That the complexity is not in the number of parameters                 
 117    |  directly but in what you need to represent the value of the parameters.          
 118    |  >> Wow.                                                                          
 119    |  >> So I could have ten parameters that are all                                   
 120    |  binary, in which case I need ten bits. Or they                                   
 121    |  could be arbitrary real numbers, in which case I might                           
 122    |  need, well, an arbitrary number of bits. That's really weird.                    
 123    |  >> Yeah, but the point here, Michael, I want to wrap this                        
 124    |  up. The point here is we've now used Bayesian learning to derive                 
 125    |  a bunch of different things that we've actually been using                       
 126    |  all along, and so again the beauty of Bayesian learning is                       
 127    |  that it gives you a sort of handle on why                                        
 128    |  you might be making some of the decisions that you're making.                    
 129    |  >> It seems like this raises the theory question                                 
 130    |  that you threw at me in a previous unit. Right.                                  
 131    |  Which is like well so if it doesn't really tell                                  
 132    |  us anything we didn't already know, how important is it?                         
 133    |  >> Well in this case, I think it is important                                    
 134    |  because it told us something that we were thinking and tells                     
 135    |  us in fact we were right. So now we can                                          
 136    |  comfortably go out in the world minimizing some of squared                       
 137    |  error when we're in a world where there is some                                  
 138    |  kind of [UNKNOWN] transmission noise. We can go about trying to                  
 139    |  Believe Occam's Razor because Bayes told us so. [LAUGH] Thanks                   
 140    |  to Shannon. And so on and so forth. We can                                       
 141    |  do these things and know that in some sense, they're                             
 142    |  the right things to do, at least in a Bayesian sense.                            
 143    |  >> Neat.                                                                         
 144    |  >> Okay, good. Now one more thing, Michael, I'm going to show you.               
 145    |  Which is that everything I've told you so far is a lie. [SOUND]                  


##  16 - Bayesian Classification
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay, Michael, so here's a quiz. Now it's a                                      
 2      |  pretty straightforward quiz. I just want you to use everything                   
 3      |  that you've learned so far. Okay, so you have                                    
 4      |  three hypotheses. Let's call them h1, h2, and h3, okay?                          
 5      |  >> Mm-hm.                                                                        
 6      |  >> For the sake of argument. Here's what each of these hypotheses Outputs        
 7      |  or some particular x. h1 says plus. h2 says minus. h3 says minus. Okay?          
 8      |  >> Mm-hm.                                                                        
 9      |  >> Now here we've,                                                               
 10     |  already made it easy for you and we've                                           
 11     |  computed the probability of, a particular hypothesis given some                  
 12     |  set of data. I'm not showing you the data                                        
 13     |  but I'm showing you the answer for it. Okay?                                     
 14     |  So the probability of h1 given the data is 0.4, h2 is 0.3, and h3 is 0.3.        
 15     |  Got it? Wait hang on, so, okay, I see                                            
 16     |  that corresponds here about this given data, what's x?                           
 17     |  >> x is some input, it doesn't matter,                                           
 18     |  just like it doesn't matter what the date is.                                    
 19     |  >> [LAUGH] 'Kay.                                                                 
 20     |  >> Just                                                                          
 21     |  call it so that, that, x is x, okay? It's just some                              
 22     |  object out in the world and each hypothesis labels it. Plus or minus.            
 23     |  >> 'Kay.                                                                         
 24     |  >> Or can label it plus or minus. And H1 decides if for                          
 25     |  that X, it's positive, and the other two hypotheses decide that it is,           
 26     |  in fact, negative and H1 has probability that is the maximum a posterior         
 27     |  probability h1 is .4, h2 is .3 and h3 is .3. So my question                      
 28     |  is, very simple. Using all of the magic we've done, this is just to make sure    
 29     |  you've got it, Michael, I dunno, we've done                                      
 30     |  a lot of derivations, we've walked away from some                                
 31     |  things [LAUGH] we gotta make sure we get back to basics here. What is the best   
 32     |  label for x? Is it plus, or is it minus? I see why this is tricky. Okay.         
 33     |  >> And go.                                                                       


##  17 - Bayesian Classification
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  And we're back. What's the answer, Michael?                                      
 2      |  >> Okay, so it depends.                                                          
 3      |  >> What does it depend on?                                                       
 4      |  I've given you everything. This is straightforward.                              
 5      |  >> Well, so, okay, I guess. The here, so here's what I'm seeing.                 
 6      |  So I'm, what I'm seeing is that hypothesis one is the most likely hypothesis.    
 7      |  >> It's not just the most likely, it's the most a posteriori.                    
 8      |  >> Well, that's what I mean by likely.                                           
 9      |  Right, is the map hypothesis? It's the maximum a                                 
 10     |  posteriori hypothesis. So if we say, what is the                                 
 11     |  label according to the map hypothesis? Boom, it's plus.                          
 12     |  >> Yes.                                                                          
 13     |  >> But, if we're saying what's the                                               
 14     |  most likely label. So the most likely label                                      
 15     |  is, is, we have to actually look over all the hypotheses and in a sense,         
 16     |  let them vote. So the probability that the label is minus is actually 0.6, which 
 17     |  is greater than 0.4, so if I had to pick, I would go with minus.                 
 18     |  >> And you would be correct. So I did a                                          
 19     |  little tricky thing here for you Michael. You've been complaining about          
 20     |  my titles, because everyone said Bayesian learning and                           
 21     |  I changed the title here to Bayesian Classification.                             
 22     |  >> Ohhh.                                                                         
 23     |  >> Because in fact the problem here, we've been talking about all along          
 24     |  is, what's the best hypothesis. But here. I ask you what's the best label?       
 25     |  >> Hm. And exactly as you point out, finding the                                 
 26     |  best hypothesis is a, is a very simple algorithm. Here I'll                      
 27     |  write it for you because we did it before. For                                   
 28     |  every H in hypothesis set, simply compute the probability that it                
 29     |  is the best one, and then simply output max. That's how you find the best        
 30     |  hypothesis, but that's not how you find the best label. The way you find the     
 31     |  best label is you basically do a                                                 
 32     |  weighted vote for every single hypothesis in the                                 
 33     |  hypothesis set, according to the weight being                                    
 34     |  the probability of that hypothesis given the data.                               
 35     |  >> Okay.                                                                         
 36     |  >> So the best, if you can only output hypothesis and use that hypothesis,       
 37     |  in fact, you would say plus. But if you asked everyone                           
 38     |  to vote, just like we did with boosting, just like we                            
 39     |  did effectively with KNN and all these other kind of. Weighted                   
 40     |  regression techniques we've used before, you need to do the voting.              
 41     |  >> And I, and I feel like I could probably derive                                
 42     |  that using rules of probability. Right, because really what we want is           
 43     |  we're trying to maximize the probability of the label, given the                 
 44     |  data, and I think the probability laws would tell us that's equal                
 45     |  to some or all hypotheses of the hypothesis and the                              
 46     |  label given the data, which is, like, the probability of the                     
 47     |  hypothesis given the data, times the probability of the label                    
 48     |  given the hypothesis, and that's what we did, we summed up.                      
 49     |  You know, the probability of the label given the hypothesis                      
 50     |  is either one or zero. That's your left column. And then                         
 51     |  we're summing up the probabilities that corresponding to the pluses. And         
 52     |  we're summing up the probabilities corresponding to the minuses and choosing     
 53     |  the largest one.                                                                 
 54     |  >> So, this is what you just said written down                                   
 55     |  as an equation. basically, the most likely value. Is the                         
 56     |  one that maximizes this expression. And this follows directly from               
 57     |  Bayesian's rule where now instead of trying to maximize the                      
 58     |  hypothesis given the data, you're trying to maximize the value                   
 59     |  given the data. And I think it's pretty straightforward to                       
 60     |  derive that but I'd like to leave it up to                                       
 61     |  the students to do it on their own. Okay, so Michael,                            
 62     |  in some sense everything that I've told you before is a                          
 63     |  lie, in that I've led you down this path that somehow,                           
 64     |  finding the best hypothesis is the right thing to do. But                        
 65     |  the truth is, finding the value is what we actually care about.                  
 66     |  Finding a hypothesis is just a means to an end. And                              
 67     |  if we have a way of actually computing the probabilities for                     
 68     |  all the hypotheses, then we should let them both in order                        
 69     |  to find the best actual label or the best value for it.                          
 70     |  >> Got it.                                                                       
 71     |  >> All right. Good.                                                              


##  18 - Summary
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Okay Michael so this wraps up all this                                           
 2      |  Bayesian Learning stuff. What have we learned today?                             
 3      |  >> We did Bayes rule.                                                            
 4      |  >> We learned Bayes rule. We even learned how to derive Bayes rule.              
 5      |  >> And it was super useful because it                                            
 6      |  lets you swap, kind of, causes and effect.                                       
 7      |  >> So I like the way you put that, Michael that                                  
 8      |  we're swapping causes and effects. Sort of mathematically when we think about    
 9      |  Bayes rule, what that really lets us do is. Instead of                           
 10     |  having to compute the probably of a hypothesis given the data We                 
 11     |  instead view to compute the probability of the                                   
 12     |  data given the hypothesis, which is typically a                                  
 13     |  much easier thing to do. And what makes it of course Bayes rule in general is    
 14     |  that you wait that by the prior probability                                      
 15     |  over the hypothesis. Which in fact is one                                        
 16     |  of the important things that we learned which                                    
 17     |  is that priors matter. So anything else we learned?                              
 18     |  >> Yep, we did the MAP hypothesis, Maximum a posteriori. Right.                  
 19     |  We learned about HMap, and we also learned about HML.                            
 20     |  >> ML, right. The maximum likelihood hypothesis. > Right. And what's the         
 21     |  maximum likelihood hypothesis? How's it relate                                   
 22     |  to the maximum a posteriori hypothesis?                                          
 23     |  >> It's the map that you get when the prior in uniform.                          
 24     |  >> Right. Alright. And we, oh, we                                                
 25     |  connected up maximum uposteriory(?) and lease(?) squares.                        
 26     |  >> Yeah, that was pretty, I really liked that. So, we basically der, we          
 27     |  deroved. We derived a bunch of things we'd                                       
 28     |  been doing before. And short of showed that                                      
 29     |  there's actually a good argument for them. At                                    
 30     |  least if you're Bayesian. There are good arguments for                           
 31     |  doing some doing some squares. There are good                                    
 32     |  arguments for Achem's(?) Razor(?). We'd actually be able                         
 33     |  to give real justification for doing them other                                  
 34     |  than, well sure it makes us one of them.                                         
 35     |  >> Right so that includes the minimum description length story.                  
 36     |  >> Mm-hm.                                                                        
 37     |  >> And then finally,                                                             
 38     |  you told me that was all a lie, and you said that really what you want to do     
 39     |  is this other kind of way of picking that                                        
 40     |  actually factors in the probability of all the different hypotheses              
 41     |  and having them essentially vote. Right. What we really                          
 42     |  care about, is classification. We're learning in the end and                     
 43     |  so we also learned about base classifiers. So in                                 
 44     |  fact, what we described before, which is voting of hypothesis.                   
 45     |  Turns out to be the Bayes optimal classifier. I                                  
 46     |  didn't say that, but it is very important to note.                               
 47     |  In fact, what you should be noting there is                                      
 48     |  not only is it the Bayes optimal classifier, it's the                            
 49     |  Bayes optimal classifier. And what that means is that                            
 50     |  on average you cannot do any better than basically doing                         
 51     |  a weighted vote of all the hypotheses according to                               
 52     |  the probability of the hypothesis given the data. You cannot                     
 53     |  do any better than this on average. So                                           
 54     |  again, what Bayesian learning gives us and what Bayesian                         
 55     |  classification gives us is a way of talking                                      
 56     |  about optimality... In gold standards. What'd you think, Michael?                
 57     |  >> That's really neat.                                                           
 58     |  >> I like it. I mean, I have to tell                                             
 59     |  you, I really think that this stuff is kind of cool.                             
 60     |  It's always nice to be able to take things that actually                         
 61     |  work and explain them according to some framework, some underlying theory.       
 62     |  >> I wonder though, it seems like                                                
 63     |  all these Bayesian equations lead us to the question, of how we actually infere  
 64     |  probabilities from various different quantities and observations.                
 65     |  So is there a way to do that?                                                    
 66     |  >> So I think the answer is yes. And maybe you should                            
 67     |  go figure it out and then tell me about it next time.                            
 68     |  >> Okay. [LAUGH] All right, as you wish.                                         
 69     |  >> As you wish.                                                                  
 70     |  >> Stay tuned.                                                                   
 71     |  >> Anyway, this has been a lot of fun, Michael.                                  
 72     |  I will talk to you later.                                                        
 73     |  >> Thanks.                                                                       
 74     |  >> Bye.                                                                          


