#  Bayesian Inference Subtitles
##  01 - Intro
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Hey Charles.                                                                     
 2      |  >> Hey Michael.                                                                  
 3      |  >> So like I get to lecture near you today.                                      
 4      |  >> Yes you do. I can even see you.                                               
 5      |  >> This is, this is crazy. I sort of don't                                       
 6      |  have my regular pad. This makes me a little uncomfortable.                       
 7      |  >> But you look very dashing in your nice blue suit.                             
 8      |  >> Thanks. We're going to record some live action stuff today.                   
 9      |  >> Mm.                                                                           
 10     |  >> [LAUGH] All right so. Do you remember                                         
 11     |  last time we were talking about Bayesian learning?                               
 12     |  >> I do, because I led that.                                                     
 13     |  >> Right. Good point.                                                            
 14     |  And so one of the questions that I asked as a follow-up was, these               
 15     |  quantities, these probabilistic quantities that we're working                    
 16     |  with. Is there's anything that we need to                                        
 17     |  know about how to represent and reason with them. And you said that I should     
 18     |  look into it. Yeah, because I, I just, I yeah you should look into it.           
 19     |  >> So I did. So, and it's cool. And so                                           
 20     |  I figured it would be fun to tell you about it.                                  
 21     |  >> Okay, well I look forward to it.                                              
 22     |  >> Thanks! And also I want to point out, we're                                   
 23     |  using a different color scheme today. Isn't that a nice blue?                    
 24     |  >> It is a nice blue, its sort                                                   
 25     |  of a relaxing blue. As opposed to that blue blue that we used before.            
 26     |  >> It's like Cerulean... Is it?                                                  
 27     |  >> No.                                                                           
 28     |  >> It's more like periwinkle.                                                    
 29     |  >> No, it's definitely not periwinkle.                                           
 30     |  >> Oh you're right, it's not periwinkle. Periwinkle's a                          
 31     |  >> Navy.                                                                         
 32     |  >> No, it's too light to be navy.                                                
 33     |  >> All right, so so good, so right. It turns out that there's this concept       
 34     |  called Bayesian Networks, which is this wonderful                                
 35     |  representation for representing and manipulating probabilistic quantities over   
 36     |  complex spaces. And so it fits in really well                                    
 37     |  with the stuff you were talking about last time.                                 


##  02 - Joint Distribution
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Alright, so to make this work, we're going to need to build on this              
 2      |  idea of a joint distribution. It's not going to be obvious right away what       
 3      |  this has to do with machine learning, at all. But, I, it's going to              
 4      |  connect. So, just bear with me for a little bit. Alright, so to talk             
 5      |  about this concept, what we're going to do is look at an example. And            
 6      |  the example that I think might work, that would be nice and simple, is           
 7      |  the notion of storm and lightning. So, here's a little picture of storm          
 8      |  and lightning. And what we're going to do is say, let's say, on a random         
 9      |  day, at 2 PM. You look outside. And, what I want you to do                       
 10     |  is say, what fraction of the time,                                               
 11     |  is, is each of these different possible combination                              
 12     |  of things happening? So, for example, what's                                     
 13     |  the probability that you look out and                                            
 14     |  there's a storm and there's lightning at the same time? So, what do you think?   
 15     |  >> On a random day?                                                              
 16     |  >> Yeah, random day at 2 PM. And we                                              
 17     |  can be in Atlanta since that's what you're familiar with.                        
 18     |  >> Is it summer? Because that happens more often in the summer.                  
 19     |  >> Sure, let's say summer.                                                       
 20     |  >> It's fairly high at 2 PM. Let's say it happens a quarter of the time.         
 21     |  >> Wow, that's a rainy summer.                                                   
 22     |  >> Mm-hm.                                                                        
 23     |  >> Alright. Now, that's not the only possibility though. It                      
 24     |  could also be that there's a storm but no lightning.                             
 25     |  >> Right. That happens more often at 2 PM                                        
 26     |  in the summer in Atlanta. Let's say it's mm, .4.                                 
 27     |  >> Wow. Alright. Now what's the probability that you look                        
 28     |  at the window and there's no storm but there is lightning.                       
 29     |  >> Maybe 5%.                                                                     
 30     |  >> And what's the probability that you look out and                              
 31     |  there's, you know, it's nice clear there's no storm no lightning.                
 32     |  >> Coincidentally I picked numbers that made it easier                           
 33     |  for me to subtract from one. So, it's 0.3.                                       
 34     |  >> [LAUGH] Right and so these, there's only, these are the only four             
 35     |  possibilities. We're saying. And they, so they have to add up to 100%. And       
 36     |  so I, yeah it had to be 30 at this point. So, it's                               
 37     |  actually more likely that there's a storm than not, according to what you said.  
 38     |  >> It's Atlanta                                                                  
 39     |  in the summer at 2 PM.                                                           
 40     |  >> There you go. Alright. So, this is a                                          
 41     |  joint distribution. And now we can actually ask various                          
 42     |  kinds of questions about this. Oh, you know what                                 
 43     |  would be a good form for asking a question.                                      
 44     |  >> I don't know. I'm looking at you quizzically.                                 
 45     |  >> Nice. Using the fact that we are in                                           
 46     |  the same place. We are going to do a quiz.                                       


##  03 - Joint Distribution Quiz
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  >> You ready for a quiz?                                                         
 2      |  >> Yes, I am.                                                                    
 3      |  >> Okay. Here's what I'd like you to do. I'd like                                
 4      |  you to use these probabilities that we have written down here,                   
 5      |  that, that constitute the joint distribution of, when you look out               
 6      |  do you see a storm, do you see lightning? And use these                          
 7      |  numbers to answer some other questions that aren't directly in here              
 8      |  but you can figure it out. So, the first one is to                               
 9      |  say, what's the probability when you look out the window at                      
 10     |  2 PM in the summer, in Atlanta, that there's no storm, okay?                     
 11     |  >> Okay. And, then the question is to say,                                       
 12     |  what's the probability that if there is                                          
 13     |  a storm, there is also lightning, okay? So                                       
 14     |  the probability of lightning given that there                                    
 15     |  is a storm. And we've done some stuff                                            
 16     |  with conditional probability. So these concepts should                           
 17     |  be familiar with you, but you should be                                          
 18     |  able to connect it up with, you know, the numbers in the table. You ready?       
 19     |  >> I am ready.                                                                   
 20     |  >> Go.                                                                           


##  04 - Joint Distribution Solution
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  All right. Let's here it.                                                        
 2      |  >> Okay. So here's the process that I went through.                              
 3      |  I'm just going to talk this out. I haven't actually worked it                    
 4      |  out in my head yet. So what's the probability that there                         
 5      |  isn't a storm? Well the way you have this drawn it                               
 6      |  actually makes it pretty easy to see. I can just look                            
 7      |  at the cases where storm is false, and it turns out                              
 8      |  there's two of them. And I can just add those probabilities                      
 9      |  over there, and I get .05 plus .30, and that gives                               
 10     |  me .35.                                                                          
 11     |  >> That's great. Yes, so that's exactly what                                     
 12     |  you did. So you went through, and now all                                        
 13     |  that matters in the universe are the cases where                                 
 14     |  they're not a storm and that ended up being                                      
 15     |  these two numbers. And you said, well Those are                                  
 16     |  two different cases that can happen. We'll just add                              
 17     |  their probabilities because they're not overlapping and you've got               
 18     |  .35. Great. All right what about the second question?                            
 19     |  >> Okay, so that's probability that there's                                      
 20     |  lightning in a world where there's a storm                                       
 21     |  so I'm going to do a very similar trick. I'm going                               
 22     |  to look at the cases where storm happens to be true.                             
 23     |  And conveniently they're the first two rows and I have                           
 24     |  two cases, so we know the probability of there being a                           
 25     |  storm is 0.65 which is good, because 0.65 and 0.35                               
 26     |  add up to one. But that's not the probability of there                           
 27     |  being lightening, given there is a storm. So, of those two                       
 28     |  cases, there's only one where lightening is happening, windstorm is happening,   
 29     |  and that's 0.25. But 0.25 isn't enough because it's only 0.25 out of 0.65.       
 30     |  >> Hm.                                                                           
 31     |  >> So the correct answer would be 0.25                                           
 32     |  divided by 0.65. Which is, some number. 5 13th's?                                
 33     |  >> Yeah. It's 5 13th's. And, though I'd                                          
 34     |  rather that people fill it in as a fraction.                                     
 35     |  >> As a, wait. That is a 5 13ths is a fraction.                                  
 36     |  >> Good point. As a point something something. A decimel.                        
 37     |  >> So, 5 13ths is obviously 0.4615. And there you go. Is that right?             
 38     |  >> Yes. That was perfect. Yeah so its usually when there's a                     
 39     |  storm, its not lightningy. It's less than half the time. That makes sense.       
 40     |  >> It does because otherwise lightning would be happening all the time.          
 41     |  >> Well when its storming. It could                                              
 42     |  be that its very likely when its storming.                                       
 43     |  >> It is likely when it's storming, but it wouldn't be happening                 
 44     |  every time its storming because otherwise it would be lightning all the time     
 45     |  when its storming.                                                               
 46     |  >> RIght.                                                                        
 47     |  >> And often there's breaks between lighting. In fact, most of the time          
 48     |  there's not lightning, at least outside my window. At 2pm. In the summer.        


##  05 - Adding Attributes
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  >> Alright, so that wasn't so bad. You are able                                  
 2      |  to compute some probabilities from this joint distribution. So let's             
 3      |  see what happens when we start talking about more variables.                     
 4      |  More propositions that could be true or false. What I did                        
 5      |  is I filled in thunder as another variable and thunder                           
 6      |  can be true or false in each of these cases. And                                 
 7      |  I wrote down what the probabilities could be from my                             
 8      |  experience in Atlanta in the summer. I was, I was around                         
 9      |  over last summer, and in 2004, so let's, so I'm an expert obviously, so          
 10     |  I'm able to estimate these probabilities to                                      
 11     |  the nearest percent. Anyway the point is, that                                   
 12     |  one of the things you should notice here is that each time we add                
 13     |  one variable what happens to the number                                          
 14     |  of probabilities that we have to write down?                                     
 15     |  >> Well in a world where it's binary it goes up by two.                          
 16     |  >> A factor of two, right?                                                       
 17     |  >> A factor of two.                                                              
 18     |  >> Not just, not just two more, but like, twice as many. And so                  
 19     |  if we have a complicated scenario that we want to be able to reason about,       
 20     |  and it's got, I don't know, a hundred variables, that's going to be a lot.       
 21     |  >> That's, that's, I can't even, I can't even think about that.                  
 22     |  >> Yeah, it's like two to the hundred is.                                        
 23     |  >> That's, that's not even a real number.                                        
 24     |  >> It's technically a real number, but                                           
 25     |  it's an, it's an unimaginably large number.                                      
 26     |  >> There's only like four numbers, one, two, three, many, and too many.          
 27     |  >> So it's going to be really inconvenient as we start adding more               
 28     |  of these and especially if we add                                                
 29     |  variables like, you know, remember the restaurant                                
 30     |  example that we worked on when we were doing decision trees.                     
 31     |  >> Oh yeah those were the days.                                                  
 32     |  >> Then there was variables like food type,                                      
 33     |  and what was the deal with food type?                                            
 34     |  >> It had lots of values that it could take on.                                  
 35     |  >> Yeah, yeah like five or something like that.                                  
 36     |  >> Thai an, American and Italian.                                                
 37     |  >> Right and so if we had, add variable like that it's going                     
 38     |  to multiply the number of probabilities that we need by five. So this is         
 39     |  going to get really big really fast. So would it be nice if                      
 40     |  we had an more convenient way of writing it out in this distribution?            
 41     |  >> Yeah, it would be nice.                                                       
 42     |  >> So it turns out that we can factor it.                                        
 43     |  >> But I thought we already had a factor of two?                                 
 44     |  >> Well that was a joke but it actually is pretty close to                       
 45     |  being the truth, which is the idea that instead of representing all, so,         
 46     |  so, in this case, there's eight numbers. Instead of representing them as eight   
 47     |  numbers, we're going to represent it by you know, 2 times 2 time 2.              
 48     |  So we really are going to essentially factor it. putting,                        
 49     |  putting things into pieces that we can recombine, smaller pieces                 
 50     |  that we can recombine into, into larger pieces. And it,                          
 51     |  yeah, it turns out that actually works out really well.                          


##  06 - Conditional Independence
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Alright, I'm going to hit you with a definition first.                           
 2      |  >> Hit me.                                                                       
 3      |  >> So, conditional independence is this idea that goes                           
 4      |  like this. We're going to say that some variable that                            
 5      |  makes up the joint distribution is conditionally independent of                  
 6      |  some other variable, Y, given Z, if it's the                                     
 7      |  case of the probability distribution governing X, so the                         
 8      |  probabilities associated with the values in this variable X                      
 9      |  Is independent of the value of y given the value of z. So if I tell you what     
 10     |  z is, then you can figure out what the probability of x                          
 11     |  is without having to look at y. So that is, if it's                              
 12     |  the case that for all possible values, little x, little y and                    
 13     |  little z for the variables big x, big y, and big z, If                           
 14     |  it's the case that the probability that big X, the random variable               
 15     |  big X, equals, takes on the value of little x, given that                        
 16     |  big Y takes on the value of little y and big Z                                   
 17     |  takes on the value of little z, equals the probability that big X                
 18     |  takes on the value of x given big Z takes                                        
 19     |  on the value of z. If those are equal for all                                    
 20     |  possible ways of filling in the values of the variables,                         
 21     |  then we say that x is conditionally independent of y given                       
 22     |  z. Right, so you see we dropped Y from the                                       
 23     |  right-hand side of the probability expression. Okay, so it's sort of             
 24     |  less things we have to worry about, if it's the                                  
 25     |  case that we really didn't need it in the first place.                           
 26     |  >> Fewer.                                                                        
 27     |  >> Fair enough.                                                                  
 28     |  >> So that's pretty similar                                                      
 29     |  to normal independence. Okay, so what's normal independence?                     
 30     |  >> So normal independence, we say the probability of x and y                     
 31     |  is equal to the probability of x times the probability of y.                     
 32     |  >> That's right.                                                                 
 33     |  >> Which means if we think about the chain rule, we                              
 34     |  also know that the probability of x and y is equal                               
 35     |  to the probability of x given y times the probability of                         
 36     |  y. So that means that the probability of x given y is                            
 37     |  equal to the probability of x, for all values of x and y.                        
 38     |  >> So this is actually implying. So [INAUDIBLE] if it                            
 39     |  equals that. Oh, that means that px times py equals                              
 40     |  px given y times py. If we cancel those, we                                      
 41     |  get px equals. Okay. That's what you wanted to say.                              
 42     |  >> Right. So, since, What independence means,                                    
 43     |  right, is that the joint distribution between two                                
 44     |  variables is equal to the product of their                                       
 45     |  marginals. That's just. You know comes from basic                                
 46     |  probability theory and so if you think about what that means                     
 47     |  from the chainable point of view it's like saying the probability of             
 48     |  x given y is equal to the probability of x. So,                                  
 49     |  it looks just like the equation you wrote down for conditional independence.     
 50     |  >> Right, the only thing that we added is this notion that it might              
 51     |  be the case that we don't have such a strong property as this where              
 52     |  it's always the case that you can write the probabiltiy of x given y             
 53     |  just with the probabilty of x. But in the context of some, of knowikng           
 54     |  some value z, it might be true. And that's what conditional                      
 55     |  independence gives us. As long as there is some z that we                        
 56     |  stick in here, that gives us that property, that's great, we can                 
 57     |  essentially ignore why, when we are talking about the probability of x.          
 58     |  >> Okay, that's pretty cool. Thatmeans more powerful or something.               
 59     |  >> Yeah, and in fact if you remember you mentioned the                           
 60     |  word factoring. You can see here that we are down a                              
 61     |  probability as the product of two other things. We are factoring                 
 62     |  that probability distribution. That's what                                       
 63     |  independence lets us do. And conditional                                         
 64     |  independence let's us do that in, in more general circumstances. So              
 65     |  let's apply this content back to what we were talking about before.              
 66     |  >> Okay.                                                                         


##  07 - Conditional Quiz
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  >> So, here's a quiz using this notion of conditional                            
 2      |  independence. So, bear with me for a second, because this is                     
 3      |  a little bit weird the way that I wrote it. But,                                 
 4      |  what I'd like you to do is find a truth setting                                  
 5      |  for thunder and lightning. So like, true/true or true/false or false/true        
 6      |  or false/false. Such that, the following thing holds true. That the              
 7      |  probability that thunder takes on that value, given that lightning takes         
 8      |  on the value that you give, and the storm is true,                               
 9      |  ends up equaling the probability that thunder takes on                           
 10     |  that value given lightning takes on the value that you                           
 11     |  gave and storm is false. Right, so a setting                                     
 12     |  here so that basically the value of storm doesn't matter.                        
 13     |  >> So, whatever I put in the upper left box                                      
 14     |  has to be what I put in the lower left                                           
 15     |  box. What I put in the upper right box has                                       
 16     |  to be what I put in the lower right box.                                         
 17     |  >> Right and in fact we're just not going to give you boxes for the              
 18     |  other ones. We'll just give you the two top boxes and automatically fill in the  
 19     |  bottom box.                                                                      
 20     |  >> Okay, that seems reasonable.                                                  


##  08 - Conditional Solution
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Alright, so how are we going to figure this out?                                 
 2      |  >> By you letting them figure it out while I figure it out.                      
 3      |  >> [LAUGH]                                                                       
 4      |  I think you should figure this out.                                              
 5      |  >> Okay let's figure it out.                                                     
 6      |  >> It might not be obvious just looking at it blankly so why don't               
 7      |  we just throw in some values here. So, for example we can do this.               
 8      |  >> Mm-hm                                                                         
 9      |  >> Which is, it gets filled in                                                   
 10     |  in both places. So the probability that thunder                                  
 11     |  is true given that lightning is false and storm is true, what is that number?    
 12     |  >> Well,                                                                         
 13     |  so we just have to find the place in our                                         
 14     |  little eight-row table where lightning is false and storm is true.               
 15     |  >> Lightning is false and storm is true, uh-huh.                                 
 16     |  >> Which is there.                                                               
 17     |  >> Uh-huh.                                                                       
 18     |  >> And the probability that thunder is true is 0.04 divided by                   
 19     |  0.4. Oh cause we're asking about thunder right. Was what's the probability that  
 20     |  thunder is true given that the other two things lightning is false and           
 21     |  storm is true so that's going to be divided by the point 4.                      
 22     |  That's the setting that we're in.                                                
 23     |  >> Right and Point 04 divided by point 4 is point 1                              
 24     |  >> Right so maybe we'll get lucky and it will work out the same                  
 25     |  with the other one. So where do we have to look for that one?                    
 26     |  >> Well now we have to look in the                                               
 27     |  row where lightning has false and storm is false.                                
 28     |  >> Okay. Down here.                                                              
 29     |  >> And look at the case where thunder is true,                                   
 30     |  and that's .03. .03 divided by .3 which is also .1.                              
 31     |  >> Woo hoo! So that works as an answer. It turns out that, in fact,              
 32     |  no matter what you type into these two boxes, it                                 
 33     |  does, in fact, work. And what does that tell us?                                 
 34     |  >> Well, it tells us that it doesn't                                             
 35     |  matter what the value of storm is. We can                                        
 36     |  figure out the value of thunder by only looking                                  
 37     |  at the value of lightening. So, that is to                                       
 38     |  say, that the probability of thunder given lightning                             
 39     |  and storm is equal to the probability of thunder                                 
 40     |  given lightening or that we have conditionally independent variables.            
 41     |  Yes, that's right. Storm is conditionally independent of thunder,                
 42     |  given lightning.                                                                 
 43     |  >> Right. So, the probability of thunder giving                                  
 44     |  li-, given lightning and storm, is equal to                                      
 45     |  the probability of thunder, given lightning. That means                          
 46     |  that thunder and storm. Are conditionally independent, given lightning.          
 47     |  >> Or thunders conditionally independent of storm, given lightning.              
 48     |  >> Sure.                                                                         
 49     |  >> Very good. Alright. So now what we're going to                                
 50     |  do next is say, Okay well given that we                                          
 51     |  have this nice property. And yeah, I, I worked                                   
 52     |  a little bit to make sure that the numbers,                                      
 53     |  worked out. It doesn't always happen this way,                                   
 54     |  but here we had some nice conditional independence and                           
 55     |  what, we're going to do next is look                                             
 56     |  at a nice representation of that, kind of information.                           


##  09 - Belief Networks
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So the concept of a belief network, sometimes also known                         
 2      |  as Bayes Net. Sometimes also known as Bayesian Network. Sometimes                
 3      |  also known as a graphical model. And there's other names,                        
 4      |  but it's the same idea over and over again. And                                  
 5      |  the, and the idea is that what we're going to do                                 
 6      |  is we're going to represent the                                                  
 7      |  conditional independence relationships between all                               
 8      |  the variables in the joint distribution graphically. In terms of                 
 9      |  of a little picture like this, where there's nodes corresponding                 
 10     |  to all the variables. And, edges corresponding to dependencies that              
 11     |  need to be explicitly represented. So, the way that this                         
 12     |  works is, what we can do is we can fill                                          
 13     |  in the prior probability of storm, which we can get by                           
 14     |  just marginalizing out. So we've, we've already done an exercise                 
 15     |  like this. So this is a number you should be able                                
 16     |  to figure out. Then because of vary well, this is                                
 17     |  also true that that you can figure out what the probability                      
 18     |  of lightning is, given storm and also given not storm.                           
 19     |  And these are numbers that you can just get by marginalizing                     
 20     |  out. Finally, the probability of thunder, normally you'd have to                 
 21     |  condition that on both storm and lightning. But as we already                    
 22     |  talked about, it's actually conditionally independent of storm given lightning.  
 23     |  So, all we need to figure out is the probability of                              
 24     |  thunder given lightning, and the probability of thunder given not                
 25     |  lightning. And once we have these, in this case five numbers,                    
 26     |  that's enough to work out any probability we want                                
 27     |  in the joint, just by multiplying corresponding components together.             
 28     |  So, what I'd like you to do is actually fill in these boxes as a quiz. And to    
 29     |  help you out we copied the numbers over from                                     
 30     |  the previous slides so that you actually have the                                
 31     |  [LAUGH] values that you need to fill in this                                     
 32     |  table. because otherwise that would have been kind of mean.                      


##  10 - Belief Networks
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  >> Hey Charles can you work out these numbers?                                   
 2      |  >> I can. So the first one is pretty easy because                                
 3      |  we did that once when we were talking a couple slides back.                      
 4      |  >> We did.                                                                       
 5      |  >> We just look at the case where a storm is set to                              
 6      |  be true. Those are, those two mega rows there and those are .25 and              
 7      |  .4. We add that up and we get .65. We're pointing out that                       
 8      |  since we know that S is .65, we know that not S is .35.                          
 9      |  >> Good.                                                                         
 10     |  >> Okay. Although that table really has two numbers in it, we only need one      
 11     |  of them.                                                                         
 12     |  >> Right. Yes. Very good point.                                                  
 13     |  >> because it's constrained by needing to add                                    
 14     |  up to one. Then we do something similar                                          
 15     |  with lightning. We look at the cases where                                       
 16     |  lightning is true. And s is also true.                                           
 17     |  >> Yep. There's just one case like that. Huh?                                    
 18     |  >> Huh, there is only one case like that.                                        
 19     |  >> Right, but what we really want to know is                                     
 20     |  what's the probability that lightning is true given that storm                   
 21     |  is true. So we need to think about both cases where storm is                     
 22     |  true and say of these, what's                                                    
 23     |  the probability that storm...that lightning is true.                             
 24     |  >> And it's .25 over .65.                                                        
 25     |  >> Right.                                                                        
 26     |  >> Which is .385 rounded up.                                                     
 27     |  >> because you're a cowboy.                                                      
 28     |  >> Which means that... The probability of it, of                                 
 29     |  not L given S is one minus that or .615.                                         
 30     |  >> That's right.                                                                 
 31     |  >> Okay. So we do the same                                                       
 32     |  trick with probability of L given not S and we find the case where lightning     
 33     |  is true but storm is false and that's .05, or we have to do it out of            
 34     |  both cases where S is false and so it's .05. Divided by,                         
 35     |  point .05 divided by .35 which is, 1 7th. And 1 7th is                           
 36     |  approximately .143, rounded up. And so not L given                               
 37     |  not S is .857.                                                                   
 38     |  >> [LAUGH] Nicely done.                                                          
 39     |  >> I use subtraction in my head.                                                 
 40     |  >> In your head yeah, but it was like with carries and stuff                     
 41     |  that was nice. And right, so let's see. And, does these sorts of things          
 42     |  make sense. Of not a storm, it's kind of unlikely that we'll see                 
 43     |  lightening. Or, if there is a storm,                                             
 44     |  it's moderately common that we'll see lightening.                                
 45     |  >> Okay, that makes sense. Okay, good. So, now we                                
 46     |  do the same trick again with thunder. Except now, instead of                     
 47     |  looking at l n s, we look at > Thunder and, and                                  
 48     |  lighting, so we need to look a case where thunder is true                        
 49     |  and lightning is true, so that would be, point, that's all the                   
 50     |  cases where lightning is true, so it would be .2 divided by .25                  
 51     |  >> Alright and why are we looking at the case where storm is true?               
 52     |  >> Why are we doing it? Because it's conditionally independent of storm.         
 53     |  >> It doesn't matter.                                                            
 54     |  >> [CROSSTALK] Information, so it doesn't matter which rows we look at.          
 55     |  What matters is we look at a case where thunder and                              
 56     |  lightening are both true, and we compare that to thunder is false                
 57     |  and lightening is true. So that's this number. Those add up to                   
 58     |  the 0.25, we get 0.2, over the 0.25, which is 0.8. Right.                        
 59     |  >> So it's very likely to hear thunder if you see lightning.                     
 60     |  >> That makes sense. And there's only a 20%                                      
 61     |  chance that you don't hear thunder when you hear lightning.                      
 62     |  >> It's lightning not thunder, yup. Mmhmm.                                       
 63     |  >> And so we do the same thing in the case                                       
 64     |  where we have thunder and there's not lightning. So we find that row.            
 65     |  >> Okay. Not lightning and there is thunder. There's one.                        
 66     |  >> Right and we do the same trick we did before and we get,                      
 67     |  .04 over .4. Which I think we did last time, actually, and we get .1.            
 68     |  >> We did. So, if it's, if there's not                                           
 69     |  lightening out, it's very unlikely to hear thunder. Alright.                     
 70     |  >> Alright and just to drive this point home.                                    
 71     |  That was great. Just to drive this point home.                                   
 72     |  What if it was the case that it mattered what's                                  
 73     |  value storm had, how would we fill in this table.                                
 74     |  >> Well we'd have to look at a lot more rows.                                    
 75     |  >> Well in particular we couldn't draw this kind                                 
 76     |  of leaf network if that were the case, right?                                    
 77     |  >> Right.                                                                        
 78     |  >> Because it wouldn't be conditionally independent. So we'd have to draw        
 79     |  basically another edge. Here, and what that represents is that thunder, to work  
 80     |  out to what the proper? of thunder is, you have to look at                       
 81     |  storm and lightning, all the joint combinations of those to make it work.        
 82     |  << And that grows exponentially as you add more and more data. <<                
 83     |  And that's right, and that's something that threw me when I started to look      
 84     |  at this, because the picture looks a lot like a neural net. Right? In            
 85     |  a neural net, you've got these nodes, you've got arrows going into the nodes,    
 86     |  and when you have a bunch of arrows going into the same node,                    
 87     |  you just end up like adding all                                                  
 88     |  those different influences together, weighted by what's,                         
 89     |  what it has on the weight. This                                                  
 90     |  belief network representation is an entirely different                           
 91     |  animal. In particular, now, what we're really saying is, to work out the value   
 92     |  of this node, you need to know what's going on                                   
 93     |  in all combinations of what the inputs are. And so,                              
 94     |  as you pointed out, so astutely, that grows exponentially as                     
 95     |  you have more variables coming into the node. Higher in degree.                  
 96     |  >> Hm. So this is not just a network. It's                                       
 97     |  a graph. And so we can talk about parents and children                           
 98     |  right? So, basically, the number of numbers you have to                          
 99     |  keep track of is exponential in your number in your parents.                     
 100    |  >> I mean it's a, yes.                                                           
 101    |  Though it's not exactly a tree. Doesn't have to be a tree so the parents         
 102    |  relationships are kind of weird. Like in particular,                             
 103    |  if you use parent terminology in this graph,                                     
 104    |  what you're saying is that lightning has                                         
 105    |  one parent which is storm and thunder has                                        
 106    |  two parents which are storm and lightning. So                                    
 107    |  it's, storm is it's own grandfather and parent.                                  
 108    |  >> So let me ask you a quick question, Michael. So earlier on when               
 109    |  you were describing this, this graph, I                                          
 110    |  noticed you used the word dependencies. You said                                 
 111    |  we're going to capture the dependencies.                                         
 112    |  >> Hm.                                                                           
 113    |  >> So if you erase the red line between storm and thunder,                       
 114    |  >> I'd be happy to.                                                              
 115    |  >> So you erased that, should I read                                             
 116    |  this as storms cause lightning, and lightning causes thunder.                    
 117    |  >> You can do that, but you would be wrong.                                      
 118    |  >> Oh okay.                                                                      
 119    |  >> You can not infer that there is a cause of relationship                       
 120    |  just because there is an arrow between them. These arrows are just telling       
 121    |  us about the relationship between the probabilities and                          
 122    |  not anything about the physically processes that underlie them.                  
 123    |  >> Okay so let me make sure I understand, what you are saying is, it             
 124    |  would be very natural to look at a belief network or a [UNKNOWN] net or a        
 125    |  Bayes Nets or graphical model. And read                                          
 126    |  the arrows as causes, and therefore read them                                    
 127    |  as talking about dependencies. But actually what's happening                     
 128    |  here is that these things represent conditional independencies.                  
 129    |  So, it is not true that lightening is                                            
 130    |  dependent on storm and thunder is dependent on                                   
 131    |  lightening. So much as is the case that                                          
 132    |  storm and thunder are conditionally independent given lightning.                 
 133    |  >> That's, that is a good point. I guess I never really realized                 
 134    |  that dependence. You use the word dependence.                                    
 135    |  Sometimes it means a physical dependence. Like,                                  
 136    |  in the real world it's dependent.                                                
 137    |  Here I'm just talking about statistical dependence.                              
 138    |  It's really just talking about the fact that we can derive numbers from other    
 139    |  numbers, and not that You know things cause other things. So yeah, that's a      
 140    |  really good point. It seems like that was an easy place to get slipped up.       
 141    |  >> Okay. Cool.                                                                   


##  11 - Sampling From The Joint Distribution
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Alright, so now that we have a handle on this                                    
 2      |  kind of representation, let's look at some things we can do                      
 3      |  with it. So, here's an example of a Bayesian network                             
 4      |  with five variables. A, B, C, D, E. And let's pretend                            
 5      |  that each one has some set of possible values. Could                             
 6      |  be true/false. Could be red, green, blue. Whatever it happens to                 
 7      |  be. And these arrows again tell us about our conditional dependence              
 8      |  relationships. So how would we go about actually well, say sampling              
 9      |  from this distribution? So let's say that we wanted to just                      
 10     |  as an example see what A, B, C, D, and E, might                                  
 11     |  look like in a, in a randomly selected example from the                          
 12     |  distribution that this network represents. So turns out what we can do           
 13     |  is that if we sample from A. Now A is specified                                  
 14     |  has no incoming arrows so it's not conditioned on anything in particular         
 15     |  so we can sample directly from A's distribution. We can do                       
 16     |  the same for B and now C. If we want to sample                                   
 17     |  from C, we need to, make use of what values have already                         
 18     |  been selected for A and B. Because C is conditioned on A                         
 19     |  and B. But we can sample from that distribution. Each, each value                
 20     |  of A and B, each joint value of A and B gives                                    
 21     |  a distribution over C. And we do the same thing for D                            
 22     |  and the same thing for E. And we're done. What we've sampled                     
 23     |  from is actually the probability distribution,                                   
 24     |  the joint probability distribution. So does                                      
 25     |  that seem like a useful thing to be able to do Charles?                          
 26     |  >> It does seem like a useful thing to be able to do.                            
 27     |  >> Yeah, so here's just a quickie quiz. So just write                            
 28     |  a one word description that says, well in this sampling you'll notice            
 29     |  I went a, b, c, d, and e. What ordering do                                       
 30     |  I need to do if I have a belief net like this                                    
 31     |  specified by this graphical structure with the arrows? If I want                 
 32     |  to be able to sample it, I need to do it in                                      
 33     |  a particular order. Some orders are, are going to be problematic because         
 34     |  we haven't actually, you know, sampled the variables that it depends on.         
 35     |  So, what ordering should we select for A, B, C, D, E? In general, what, what is  
 36     |  the name for that. So that we can                                                
 37     |  actually do this kind of sampling trick this way.                                
 38     |  >> Okay.                                                                         


##  12 - Sampling From The Joint Distribution
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  >> All right Charles, so, so, what do you think the answer is here?              
 2      |  >> Actually I don't know what you're looking for here.                           
 3      |  >> Oh, okay. Well, so one thing that's true. We                                  
 4      |  had to sample the, the variables from A to E.                                    
 5      |  >> Mm-hm.                                                                        
 6      |  >> And that's alphabetical order. So do                                          
 7      |  you think that's what I was looking for?                                         
 8      |  >> Maybe in this case but I would think that that wouldn't be generally true.    
 9      |  >> True. Right. So, yeah, alphabetical is not what I                             
 10     |  was looking for. So, there's it's a graph theoretic property                     
 11     |  that says we want to basically put the nodes                                     
 12     |  in order, so that you always put the things                                      
 13     |  that have incoming links that haven't been visited yet                           
 14     |  after the ones where you, they have been visited.                                
 15     |  >> Oh, so it is a lot like alphabetical                                          
 16     |  or a lot like lexo-, lexicographic, but it's topological.                        
 17     |  >> There we go. Yeah, that's what I was looking for. So, topological sort.       
 18     |  >> Which makes perfect sense.                                                    
 19     |  >> Right, and so this a standard thing that you can do with a graph, and it's    
 20     |  very quick to, to actually compute one of                                        
 21     |  these. It does depend on a particular property, though.                          
 22     |  >> Let's see. Topological only makes sense if you really can                     
 23     |  go from no parents to parents. So, it cannot be cyclical. You                    
 24     |  can't have arrows that take you back. So, E can't be a                           
 25     |  parent of A and also have A be one of its parents.                               
 26     |  >> That's right.                                                                 
 27     |  >> So it must be acyclic.                                                        
 28     |  >> Must be acyclic, right. And that's going to                                   
 29     |  be true in these cases, because we're always going                               
 30     |  to set it up so that in a, in a Bayes net, the variable that we're each          
 31     |  variable depends on other variables. But they all, it ultimately has to bottom   
 32     |  out. There can't by cyclic dependencies. So, it is a directed acyclic graph.     
 33     |  >> So, what would it mean if there were cycles?                                  
 34     |  >> I don't know. I don't know what to do with such a graph.                      
 35     |  >> It just doesn't mean anything at all, I guess.                                
 36     |  >> Yeah, I mean, there, there is a family of undirected models.                  
 37     |  >> Mm-hm.                                                                        
 38     |  >> But we're talking only about the directed ones here. So, the directed         
 39     |  ones yeah, it'd have to be acyclic for the, for the probability distribution     
 40     |  to be meaningful.                                                                
 41     |  >> Well, that makes sense.                                                       
 42     |  >> I'm sure we could make something up, but this is, typically                   
 43     |  this is how it's done. It's, it's, we constrain ourselves to acyclic graphs.     
 44     |  >> Well, if a Bayesian network is                                                
 45     |  supposed to capture conditional independencies, then if you                      
 46     |  add cycles, that's like saying there are none,                                   
 47     |  right? I'm not even sure what that means.                                        
 48     |  >> I could make it mean something. So here,                                      
 49     |  we, we want the probability of A, conditioned on probability                     
 50     |  of A. Well, maybe that's like probability of what, what A was one time step      
 51     |  ago. Or it could mean that it, you                                               
 52     |  know, that, that we've actually putting constraints on                           
 53     |  the joint assignment to all the variables.                                       
 54     |  But, yeah, it's not really, it doesn't really,                                   
 55     |  it makes things more complicated and that's not                                  
 56     |  he model that, that is the typical one                                           
 57     |  >> Okay, fair enough.                                                            


##  13 - Recovering the Joint Distribution
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So another important thing that you can do with this representation              
 2      |  is recover the joint distribution. Remember a couple, a couple slides ago        
 3      |  we looked at the issue of how can we go from                                     
 4      |  the distrib, joint distribution to specifying                                    
 5      |  what the probabilities are, the conditional                                      
 6      |  probability tables, they're called, at each of these nodes. But we               
 7      |  can actually go the other direction as well. We can go from,                     
 8      |  from the values in these conditional probabilities tables in each of             
 9      |  the nodes, to computing the probability                                          
 10     |  of any combination, any joint combination                                        
 11     |  of variables that we want. So, it turns out it's really, really                  
 12     |  simple. We can just go and use these same ideas and say                          
 13     |  the joint probability for some assignment to the variables, is equal to          
 14     |  just the product of all the individual values. So the probability that that      
 15     |  value of A would be taken times the probability that that value                  
 16     |  of B would be taken times the probability that that value of                     
 17     |  C would be taken, conditioned on those are the values that were                  
 18     |  chosen for A and B. So it's just like in the sampling case.                      
 19     |  >> Right, and                                                                    
 20     |  that's much more compact a representation.                                       
 21     |  >> That's a good observation, yeah. So how, if                                   
 22     |  these were Boolean variables, how many values would we                           
 23     |  need to specify for the joint distribution in the                                
 24     |  standard representation, where you just assign probability to everything.        
 25     |  >> Well if I ignore the fact that there are some constraints that we might be    
 26     |  able to take advantage of, it would be                                           
 27     |  2 to the 5th, because there are five variables.                                  
 28     |  >> Right, but here we've broken it down                                          
 29     |  into smaller chunks so, the probability of A,                                    
 30     |  it's just specified by single number. Probability of B is                        
 31     |  specified by a single number. Probability of C is specified                      
 32     |  for a single number for each combination of A and                                
 33     |  B. That's four of them. This also requires four values and                       
 34     |  this requires four values. So this is really, what, it's                         
 35     |  like 2 to the 5th minus 1 I guess. Because, if                                   
 36     |  I tell you the first 31 values, the last, the                                    
 37     |  32th value, it's just 1 minus the sum of the other.                              
 38     |  This is 14 numbers versus 31. You are right, it is more compact, 31 is bigger.   
 39     |  >> Right but let's imagine that all of the                                       
 40     |  variables were in fact completely independent of one another,                    
 41     |  then you would have 5, you would only need                                       
 42     |  5 numbers. It would be the product of the unconditionals.                        
 43     |  >> Yeah, which is what we'd get if we had kind of like just a                    
 44     |  set of weighted coins. If they're unrelated to                                   
 45     |  each other, but each one has some probability                                    
 46     |  of coming up heads, the probability of getting some, some particular             
 47     |  combination like, A is heads and B is tails and C                                
 48     |  is heads and D is heads and E is heads. We                                       
 49     |  could just break that down to the probability of the individual events.          
 50     |  >> So then all of the, just like with the joint distribution where               
 51     |  you have this exponential growth, because you need to know everything. Here you  
 52     |  have the exponential growth that only depends upon the number of parents you     
 53     |  have. If you have no parents, then it is constant, if you have parents,          
 54     |  then is grows exponentially with the number of parents.                          
 55     |  >> Right, so the fewer number of parents,                                        
 56     |  the more compact the distribution ends up being.                                 


##  14 - Sampling
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  >> Earlier I mentioned sampling and I asked you whether that                     
 2      |  sounded useful, and you said it was. So, let's do a                              
 3      |  little exercise. Why? Why [LAUGH] is that a useful thing? Why                    
 4      |  is it good idea to be able to sample from a distribution?                        
 5      |  >> Well, because it's one of the two things that distributions are for.          
 6      |  >> What does that mean?                                                          
 7      |  >> Well so why do you have a                                                     
 8      |  distribution? A distribution is so that given some                               
 9      |  value, you can, you can tell me what's                                           
 10     |  the probability of me seeing that value which                                    
 11     |  is kind of what it looks like when you have the probability function, but        
 12     |  also if you have a nice distribution                                             
 13     |  you can generate values according to that distribution.                          
 14     |  >> Okay. That's a little bit circular in the sense that it didn't tell me why    
 15     |  it was useful to generate them other than it's one of the things you can do.     
 16     |  >> Well, you didn't ask me to actually make sense. But I mean, this is           
 17     |  the, the thing that you use distributions for.                                   
 18     |  Now why would you want to do that?                                               
 19     |  >> Yeah.                                                                         
 20     |  >> So,                                                                           
 21     |  if a distribution represents kind of a process, it would                         
 22     |  be nice if I could duplicate that process, right? So, I                          
 23     |  would have to be able to generate values in the                                  
 24     |  right way, consistent with the distribution in order to generate that            
 25     |  process. So it's like flipping a coin, or I want                                 
 26     |  to flip a coin and find out whether I'm going to                                 
 27     |  get heads or tails. It would be nice if I can                                    
 28     |  do that in a way that's consistent with whatever the underlying                  
 29     |  bias of the coin is.                                                             
 30     |  >> Okay, so yeah, if this distribution                                           
 31     |  represented something complex, we might, you know, for                           
 32     |  whatever reason need to simulate that world                                      
 33     |  and, and act according to those probabilities. So,                               
 34     |  yeah, that, that's a reasonable one. What else, what if, what if I showed you    
 35     |  this, if i took this distribution that                                           
 36     |  we used for the lightning and thunder example.                                   
 37     |  >> Mm-hm.                                                                        
 38     |  >> What if you wanted to get a handle on it? How can we                          
 39     |  use sampling for the distribution to give                                        
 40     |  you some insight into how the storms work?                                       
 41     |  >> Okay                                                                          
 42     |  so let's see, I've, I've, I've got this representation                           
 43     |  of the joint distribution, but it's just a representation of                     
 44     |  the joint distribution. If I want to asked a                                     
 45     |  question like, well what's the chance that it's, oh let's                        
 46     |  say, storming outside if I've heard thunder, I could                             
 47     |  go through and, and, you know, back compute the reverse                          
 48     |  of the conditional probability tables. And I could do things                     
 49     |  like, or I could just generate a bunch of samples                                
 50     |  where I had thunder and I can just see how                                       
 51     |  often the storm was also true. Does that make sense?                             
 52     |  >> It does, though I'm not going to use                                          
 53     |  the words that you just used to write that down.                                 
 54     |  >> Okay.                                                                         
 55     |  >> I'm going to call that approximate inference. So the basic idea is that       
 56     |  you would like to do some inference, you'd like to figure out what might         
 57     |  be true of the world in different                                                
 58     |  situations. Instead of doing some complex probability                            
 59     |  calculation, you're just going to imagine a                                      
 60     |  bunch of possible worlds and see how often                                       
 61     |  is it the case that whatever it is you                                           
 62     |  want to figure out is true. So yeah, that, that                                  
 63     |  turns out to be a really good way to                                             
 64     |  do it. In fact, sometimes I think that's a lot                                   
 65     |  of what people are doing when we're, when we're                                  
 66     |  making judgments in the world. We're just really, really good                    
 67     |  at this kind of sampling from past realities that                                
 68     |  are relevant, and we can make judgments based on that.                           
 69     |  >> Hm. So, how would you do that?                                                
 70     |  >> How would I do what?                                                          
 71     |  >> How would you do this approximate inference?                                  
 72     |  >> We're going to get to that but I wanted to.                                   
 73     |  >> Oh, okay, cool.                                                               
 74     |  >> But                                                                           
 75     |  there, but there's one or two other                                              
 76     |  things about sampling that I wanted to mention.                                  
 77     |  >> Okay.                                                                         
 78     |  >> Another thing that I could imagine using this for                             
 79     |  is this notion of visualization. Which may be, I mean this                       
 80     |  in a, in a broader way than it sounds, not                                       
 81     |  necessarily to actually see what the distribution is like, but to                
 82     |  kind of get a feel for it. So, I bet if I was to run that if I was to draw       
 83     |  a bunch of samples from the lightening thundering set, you                       
 84     |  would have a better feel for how likely different things are.                    
 85     |  Just you as a person might get a sense of how these                              
 86     |  things work. So, you can imagine in, in a medical domain a doctor                
 87     |  who's, who's thinking about prescri, prescribing a particular kind of drug for a 
 88     |  particular kind of person, if the                                                
 89     |  information about drug interactions and so forth                                 
 90     |  was, was represented as a big belief net, it might be hard to                    
 91     |  look at it and know anything. But if it ge, if you use                           
 92     |  that to generate a bunch of artificial patients you might start to get           
 93     |  to feel for oh, you know what, these kinds of people tend to                     
 94     |  react badly in these kinds of circumstances.                                     
 95     |  >> That's still a kind of approximate inference, right?                          
 96     |  >> That's right. So this is, this is a kind of an                                
 97     |  in the machine sense, and this is kind of in the human sense.                    
 98     |  >> Okay, I like that. So let's see, let's see                                    
 99     |  if I, if I understand this. So the, the nice thing                               
 100    |  about the storm, the thunder, and the lightning example is that                  
 101    |  it has pedagogical value. Because it's easy for a student to                     
 102    |  look at that and go okay, I understand what's                                    
 103    |  going on here. One because there's only three nodes                              
 104    |  and two arrows, and the other is because, we                                     
 105    |  think we understand how storms, thunder and lightning work. Right.               
 106    |  >> Yup.                                                                          
 107    |  >> Or most people do. So that makes a lot of sense. Of course                    
 108    |  the downside of it is, we think we understand it. And so it's hard to            
 109    |  see why you would need to do samples, I mean, there's just a couple of           
 110    |  probability distributions and we kind of know                                    
 111    |  what it means. But in the real world,                                            
 112    |  there are perhaps hundreds and hundreds of variables                             
 113    |  with complicated relationships and conditional independencies that, that aren't  
 114    |  necessary intuitive just by looking at the graph. And                            
 115    |  so picking one conditional probability table and looking at                      
 116    |  it isn't going to tell you much. But by                                          
 117    |  sampling I get real examples that are concrete that,                             
 118    |  as a human being, I can understand without having                                
 119    |  to, you know, really glock all the 25 different                                  
 120    |  conditional probability tables. Does that sound right? Is that. [CROSSTALK]      
 121    |  >> Yeah, yeah.                                                                   
 122    |  >> What you're trying to say?                                                    
 123    |  >> That's exactly right. Thanks.                                                 
 124    |  >> Okay.                                                                         
 125    |  >> I want to draw your attention to this, this                                   
 126    |  word here for a moment. This notion of approximate inference. Now                
 127    |  generally we don't like approximations when we can do things, things             
 128    |  exactly. So why are, why are we not doing things exactly?                        
 129    |  >> because it's hard.                                                            
 130    |  >> It's hard, that's exactly right. So or,                                       
 131    |  or, even if it weren't hard, it may,                                             
 132    |  it may be in some cases faster. So I would be,                                   
 133    |  I'm not going to do it now, but I'd be happy                                     
 134    |  if I guess if there's ground swell of support among the                          
 135    |  students. To I can go through the argument as to why                             
 136    |  this inference is hard. There's a nice little reduction to problems,             
 137    |  N, NP complete problems like satisfiability. But it turns out roughly            
 138    |  that if you could do inference exactly on any belief net                         
 139    |  that you want, then you could solve very, very hard problems efficiently         
 140    |  using that idea. So it's, it's cute, but it's kind of takes us                   
 141    |  a little bit off our path, so I'm not going to get into that.                    
 142    |  >> Okay, so sampling is useful, Michael, which I always suspected in my          
 143    |  heart, and now we've got some good arguments for why it actually is.             


##  15 - Inferencing Rules
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So, okay so let's, let's actually do some inferencing just to, to                
 2      |  kind of get a feel for it. For certain kinds of networks we                      
 3      |  can do things exactly. And we're going to look at one of                         
 4      |  those examples in just a moment. But, it turns out, helpful to                   
 5      |  remind ourselves of some rules of probability in inference that will help        
 6      |  us do that. So, here's just kind of a little cheat sheet.                        
 7      |  For you, so, marginalization is this idea that we can represent the              
 8      |  probability of, of a value, at, by summing over some other variable and          
 9      |  looking at the joint probabilities of those. And if, if                          
 10     |  you've trouble remembering this one, this, this's how I like to                  
 11     |  think about it, if we're trying to figure out the probablitiy                    
 12     |  of x, then one way, one thing we can do is                                       
 13     |  break it up in. Break the world up into, well                                    
 14     |  the cases where x and, not y. Plus, places where x                               
 15     |  and y. So, the probability of x is it can be                                     
 16     |  broken down into the probability of x when y is false                            
 17     |  plus the probability of x when y is true. So                                     
 18     |  it's really simple in that sense, but it actually turns out                      
 19     |  to be a useful thing to be able to do.                                           
 20     |  To marginalize out. The chain rule, we've used this a bunch                      
 21     |  of times. The probability of x and y can be                                      
 22     |  written as the probability of x times the probability of y                       
 23     |  given x. And that's important that we've the given X. If                         
 24     |  we drop that then what is that implying? Just go ahead.                          
 25     |  >> Well, if you drop that then it                                                
 26     |  implies that they are completly independent of one another.                      
 27     |  >> Right, in the case where the variables                                        
 28     |  are independent, you can just look at their product.                             
 29     |  In the general case you actually have to                                         
 30     |  look at the second one given the first one.                                      
 31     |  >> And as I recall, the order on the                                             
 32     |  left doesn't matter, so, you've the probability of X times                       
 33     |  the probability of Y, but you could have written the                             
 34     |  probability of Y times the probability of, X given Y.                            
 35     |  >> Yes. And, actually, let's do a quick quiz.                                    
 36     |  >> Okay.                                                                         


##  16 - Inferencing Rules Quiz
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  All right. So, person who's adept at manipulating Bayes Nets                     
 2      |  would know that this chain rule idea, this probability of X                      
 3      |  and Y can be written either as a probability of                                  
 4      |  X times the probability of Y given X. Or as the                                  
 5      |  probability of Y times the probability of X given Y,                             
 6      |  actually correspond to two different networks. So which of these two             
 7      |  networks corresponds to the fact that the probability of x and                   
 8      |  y, the joint probability of X and can be written as                              
 9      |  the probability of Y times the probability of X given Y.                         
 10     |  >> Go.                                                                           


##  17 - Inferencing Rules Solution
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Did you get it?                                                                  
 2      |  >> Yeah I did actually. so, so this one                                          
 3      |  I think I understand completely. So we know that from                            
 4      |  the last discussion we had about how you would recover                           
 5      |  the joint, that what you're saying on the right of                               
 6      |  this equation probability y times probability n y means that                     
 7      |  the probability of y, the variable y doesn't depend on                           
 8      |  anything. So, between those two graphs the one on the                            
 9      |  right is the one where you're saying that. You don't                             
 10     |  need to know the value of any other                                              
 11     |  variable in order to determine the probability of y.                             
 12     |  >> Good.                                                                         
 13     |  >> So it has to be the one on the sec, the second and just to make sure          
 14     |  if you look at the second product the probability                                
 15     |  of x given y the second multican? Is it multican?                                
 16     |  >> Hm, factor.                                                                   
 17     |  >> Factor? Let's say factor. The second factor,                                  
 18     |  this says that while you determine the probability                               
 19     |  of x given the value of y and there is an arrow from y to x                      
 20     |  so, the second one is in fact correct.                                           
 21     |  >> Yeah. So this is actually just one way you could just read this               
 22     |  network is to say what is this node x with an arrow coming into it?              
 23     |  That is the probability of x. But, the, the things pointing into it are what's   
 24     |  exactly being given. What it's being conditioned                                 
 25     |  on. So that's exactly right, the second one.                                     
 26     |  >> Right. So this, this, so this makes sense to me. This is why when             
 27     |  you look at a network, network, it's very                                        
 28     |  hard not to think of them as dependencies.                                       
 29     |  Even though they're not dependencies, they're conditional independencies.        
 30     |  >> Well the arrows are a form of dependence but it's not a causal                
 31     |  dependence necessarily, it's it's again it's just                                
 32     |  the way the probabilities are being decomposed.                                  
 33     |  >> Hm.                                                                           
 34     |  >> And the last of these three equations just Bage's rule,                       
 35     |  this time written correctly where the denominator has to be the probability      
 36     |  of x, and we've gone over this a couple of times. I                              
 37     |  don't, I don't need to, to describe it again, but what Would                     
 38     |  like to, just, bring to your attention to                                        
 39     |  this three together turn out to be kind                                          
 40     |  of our, you know, three musketeers in working                                    
 41     |  out the probability of various kinds of events.                                  
 42     |  >> Excellent.                                                                    


##  18 - Inference By Hand
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  All right. So let's put some of these rules into play                            
 2      |  by actually doing some inference by hand. Ultimately, we're going to derive      
 3      |  some algorithms that can do this so you don't have to                            
 4      |  think about it so hard. But understanding those algorithms, it's helpful to      
 5      |  have gone through an exercise where you actually use these ideas.                
 6      |  So here's a setup. Let's imagine that we've got two boxes. Onee                  
 7      |  has 4 balls in it and one has 5 balls in it.                                     
 8      |  And we're going to choose one of those boxes uniformly at random.                
 9      |  Either the box that we choose is equal to box 1,                                 
 10     |  or the box that we choose is equal to box 2.                                     
 11     |  And after that, we're going to draw at random, uniformly at                      
 12     |  random, from what's inside the box, one of the balls, and                        
 13     |  let's say it turns out to be green. All right. So                                
 14     |  the draw that we make, we have a green ball. We                                  
 15     |  reach into that same box a second time, and the question                         
 16     |  is, what's the probability that that second ball will be blue,                   
 17     |  given that the first one we drew was green? So                                   
 18     |  let's, to make, maybe to help point out how this                                 
 19     |  is connected with Bayes net inference, Charles, why don't you                    
 20     |  help me draw the Bayes net that corresponds to this problem.                     
 21     |  >> Okay. So, if I think about it as                                              
 22     |  a process, which now means I'm, I'm thinking about this                          
 23     |  as things causing the other, the first thing that                                
 24     |  you did in the process is you picked the box.                                    
 25     |  >> Good. All right. So let's say, so the first variable in                       
 26     |  the net is going to be the box variable.,                                        
 27     |  >> Right, and then once I had the box variable                                   
 28     |  over there, I can then pick, the second thing in                                 
 29     |  the process is I pick a ball. So, in this                                        
 30     |  case you're calling it 1. So I make the first pick.                              
 31     |  >> And is it, do we need an arrow there?                                         
 32     |  >> Yeah, because the, you pick the box and                                       
 33     |  then that let's you pick which ball that you have.                               
 34     |  So, which ball you pick, the color of the                                        
 35     |  ball you pick, depends upon the box so to speak.                                 
 36     |  >> Good. And so, the probabilities here are                                      
 37     |  going to be, it's going to look like this.                                       
 38     |  All right. So the second variable here is what, what                             
 39     |  color ball you get when you do the first draw                                    
 40     |  from the box. Ad we can represent this as a                                      
 41     |  conditional probability table. So for box 1, it's three quarters                 
 42     |  green, one quarter yellow or orange, zero for blue. And                          
 43     |  for box 2, it's two fifths, zero, and three fifths.                              
 44     |  And so that captures what happens on the first draw.                             
 45     |  >> So for the second draw,                                                       
 46     |  well, clearly, that sort of depends upon what you drew                           
 47     |  the first time. Because you said we were drawing without                         
 48     |  replacement. So it definitely depends upon what you, what you                    
 49     |  drew the first time. But also, it still depends upon                             
 50     |  the box. Okay, so now we've got tables for a                                     
 51     |  box, we've got tables for ball 1, and we need                                    
 52     |  to know what ball 2 is going to be. Well,                                        
 53     |  the value that ball 2 takes definitely depends upon whatever                     
 54     |  value ball 1 takes.                                                              
 55     |  >> Sure.                                                                         
 56     |  >> But it also depends upon which box you're                                     
 57     |  in. So you need an arrow from there as well.                                     
 58     |  And what would be really nice is if we                                           
 59     |  were in the storm, lightening and thunder case where, if                         
 60     |  I knew that it was, what ball 1 was,                                             
 61     |  I would know what ball 2 was, but that's not                                     
 62     |  true. Because in a case, for example, when ball                                  
 63     |  1 is green, it doesn't tell me what ball 2                                       
 64     |  is unless I also know which box I'm in. So,                                      
 65     |  we have to draw the arrow from box to ball 2.                                    
 66     |  >> Indeed. Right. And so there's a lot                                           
 67     |  of, a lot of probabilities that we have                                          
 68     |  to write down. But lets, let's just write down a piece of that table. Let's say  
 69     |  that the value of ball 2 depends on which box. And it depends on what            
 70     |  ball 1 is. But let's just look at the piece of that table where ball 1 is green. 
 71     |  >> hm.                                                                           
 72     |  >> because that's what we're                                                     
 73     |  ultimately going to need here. So now ball 2, in                                 
 74     |  the case where we were drawing from box 1, that                                  
 75     |  probably that's green. In the case were the first ball                           
 76     |  had been green, it leaves just 2 out of 3, right.                                
 77     |  >> hmm.                                                                          
 78     |  >> And 1 out of 3 yellow and no blue. But on the other hand, had we drawn        
 79     |  from box 2 first, and again, we had gotten green, now it's green one fourth,     
 80     |  zero yellow, and blue three quarters.                                            
 81     |  >> RIght.                                                                        
 82     |  >> And there's yeah, we need this same                                           
 83     |  thing where the other case, where ball 1 is                                      
 84     |  yellow and ball 1 is blue. But we are                                            
 85     |  not going to need those numbers for this problem.                                
 86     |  >> Right.                                                                        
 87     |  >> All right. So now that we have written it as                                  
 88     |  a Bayes net, is that, is that helpful at all? So what                            
 89     |  we're, we haven't asked the question yet. So maybe it's time                     
 90     |  to ask the question and then we could work on the answer.                        
 91     |  >> Okay.                                                                         
 92     |  >> All right. The question                                                       
 93     |  is, what's the probability that the second draw is                               
 94     |  blue, given that the first draw had been green? Go.                              


##  19 - Inference By Hand
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  All right, so can you use this Bayes net to help work things out?                
 2      |  >> Yeah, actually it make it a lot easier. I                                     
 3      |  was, I was thinking about how I would do this and,                               
 4      |  and wouldn't involve writing a whole lot of equations and doing                  
 5      |  a whole lot of stuff but actually, just by writing out                           
 6      |  the Bayes net we ended up, and filling out these tables                          
 7      |  we ended up doing that. So, the, the bottom table is,                            
 8      |  basically tells me the probability of, ball two being some color.                
 9      |  In a world where ball one is known to be green.                                  
 10     |  Because we just broke down that part of the table, so                            
 11     |  we don't have to do it for every other one. And,                                 
 12     |  you know, if I knew that I were in box one,                                      
 13     |  then the probability of it being blue in a world where                           
 14     |  ball one was green is in fact zero. And if I                                     
 15     |  knew I were in box two. Then the probability of it                               
 16     |  being blue in, where ball one is green, and where box                            
 17     |  two is three quarters. So I only care about that last column.                    
 18     |  >> All right.                                                                    
 19     |  >> And now I just                                                                
 20     |  have to choose the row or choose how to                                          
 21     |  distribute the likelihood over the row. So all I                                 
 22     |  really need to know is, what's the probability of                                
 23     |  me being in box one and being in box two.                                        
 24     |  >> All right, which we have in the table as well, as a half.                     
 25     |  >> Right. So that means the probability of                                       
 26     |  it being ball two. Being, ball two being                                         
 27     |  blue in a world where ball one is green, is just the probability of ball two     
 28     |  being blue, given that ball one is green. And we want to                         
 29     |  know the probability two is blue given that one is green                         
 30     |  but when you look at the table and all we care                                   
 31     |  about is that last column, all we really want to know is, well,                  
 32     |  we know the answer when box one, when we're in box                               
 33     |  one, when box equals one, it's zero, and we know the                             
 34     |  answer when box equals two, it's 3 4s. So if we                                  
 35     |  were going to do a sample, for example, which we talked about earlier,           
 36     |  we would just sample a bunch of times, and we would get                          
 37     |  0 sometimes and we would get 3 4s sometimes. And that would                      
 38     |  be great, except of course, we want to compute this exactly. And                 
 39     |  we know how to compute it exactly, because we actually know the distribution     
 40     |  over, how many times box would be equal to 1 and how                             
 41     |  many times box would be equal to 2. It would be half                             
 42     |  in each case. So, I really like, I think you've made this                        
 43     |  easier by giving us the table. So, actually writing out the Bayes net.           
 44     |  So we want to know the probability that the second ball                          
 45     |  is blue given that the first ball is green. And that's                           
 46     |  just equal to the probability that the second ball is blue.                      
 47     |  Given that the first ball is green and we were in                                
 48     |  box one. Because if we knew that, we knew we were                                
 49     |  in box one and the first ball we drew was green,                                 
 50     |  it'd be really easy to compute the probability of the second                     
 51     |  ball being blue. It's right there in the table at zero.                          
 52     |  >> Is this, is this the                                                          
 53     |  way that you think it should be written?                                         
 54     |  >> Almost, but not quite. That would be the easy thing to do because we know     
 55     |  that answer. We know the probably that box is equal to 1. It's just a half. But  
 56     |  it's not just the probability that box is                                        
 57     |  equal to one, it's the probability that box                                      
 58     |  is equal to one in a world where we knew the first thing we drew was green.      
 59     |  >> Gotcha.                                                                       
 60     |  >> And if we had that then it would be easy to figure out the, the products      
 61     |  there to figure out two is blue in a                                             
 62     |  world where the box one is green. Boxes equal                                    
 63     |  to 1 and the first ball that we pulled was equal to, was green. And then we will 
 64     |  just add that to the probability that the second                                 
 65     |  ball we drew was blue. Given that the first                                      
 66     |  ball that we drew was green. And we were                                         
 67     |  in box two. We were drawing from box two.                                        
 68     |  And that would have to be weighted by the prober-, probability that box was      
 69     |  two in a world where the first ball that we grew, drew was green.                
 70     |  >> Good. Very good. And in fact, this                                            
 71     |  rule that you kind of worked through follows                                     
 72     |  just algebraically from two of the rules that                                    
 73     |  we just talked about. It's the combination of                                    
 74     |  the marginalization rule, which lets us introduce this                           
 75     |  box variable. But the way that we wrote                                          
 76     |  it before, it was, you have to and it in. But then we actually then applied      
 77     |  the chain rule to split that into a conditional probability. So, so this is      
 78     |  all valid at the moment. And are these quantities that we, that we know?         
 79     |  >> Well, we certainly know the very first term in each                           
 80     |  of the two summands. Can it be summands? Let's say they're                       
 81     |  summands. If they're not, we'll get nasty emails from people. The                
 82     |  first part's probability. Second ball is blue given that the first               
 83     |  one is green in red box one. And                                                 
 84     |  the probablity that the second ball is blue given                                
 85     |  that the first one is green in red                                               
 86     |  box two. That's easy, that's actually in the table.                              
 87     |  >> That's easy, that's in the table. And it's                                    
 88     |  zero in this case, and three quarters in this case.                              
 89     |  >> Right, so it's zero in the first case and                                     
 90     |  it's three quarters in the second case, straight outta the table.                
 91     |  Now all we have to do is figure out how                                          
 92     |  often we're in box one and how often we're in box                                
 93     |  two and if you didn't think it through you would just have                       
 94     |  the probability of box equals one and the probability of box equals two.         
 95     |  But we have to remember we're in a world where the first ball                    
 96     |  we picked was green. So now we just have to compute each of                      
 97     |  those terms. So how do we do that? So we want to                                 
 98     |  know what the probability is that boxes, we're in box 1 given that               
 99     |  we picked a green ball first. Well that one's actually much easier to            
 100    |  think about because Bayes' rule will give us, will allows us to express          
 101    |  this in quantities where we do know the answer. Because we have the tables. So   
 102    |  that would be the probability that the first ball was green given that we were   
 103    |  in box 1 times the probability                                                   
 104    |  that we're in box 1 divided by the probability that the first thing we picked    
 105    |  is green. So, the probability that we get a green ball if                        
 106    |  we pick box one, is just well, it's three quarters.                              
 107    |  >> Yep. It's.                                                                    
 108    |  >> A different three quarters than the other one though.                         
 109    |  >> Yeah. Those, those two three                                                  
 110    |  quarters aren't the same three quarters. This,                                   
 111    |  this way. Because sometimes, two three quarters                                  
 112    |  are not the same two three quarters.                                             
 113    |  >> In this case, there are three green balls and one, what                       
 114    |  we're pretending to call yellow because it's easier to write than orange, ball.  
 115    |  And so three of the four of them are green, so if we                             
 116    |  were in box one, we close our eyes, we'd get three of those.                     
 117    |  So what the probability that we're in box one? Well, it's                        
 118    |  right there in the table, to Bayes' net, it's one half. Now                      
 119    |  we just have to figure out well, what's the probability that                     
 120    |  I would get a green ball the first time I picked one?                            
 121    |  >> Right. And so one easy way to do                                              
 122    |  that is, we actually do this, this whole process again                           
 123    |  on box two, and then just normalize. Or we                                       
 124    |  could break this apart using the, using the marginalization rule.                
 125    |  >> Yeah,                                                                         
 126    |  which one do you want to do?                                                     
 127    |  >> The first one I think.                                                        
 128    |  >> Okay. So figuring out the probability the first                               
 129    |  one is green isn't, isn't as easy as it                                          
 130    |  looks. You can't just say, well there are five                                   
 131    |  green balls, but there's a total of nine balls,                                  
 132    |  and so it's 5 9th, because those nine balls                                      
 133    |  aren't distributed equally on both sides of the boxes.                           
 134    |  So you really have to, you still have to                                         
 135    |  know which box that you're in, in some sense.                                    
 136    |  >> Right.                                                                        
 137    |  >> But we can kind of skip that step. Okay,                                      
 138    |  so I like this, so what's the probability that the first ball                    
 139    |  is green given that we're in box two, well it's just 2                           
 140    |  5ths. Prove by looking at the screen. And what's the prior probability           
 141    |  that we're in box two? Well, it's just a half because that                       
 142    |  was given to us on the table. And so, we still don't                             
 143    |  know the prior probability of, of the first ball being green, but                
 144    |  it turns out we don't have to because there are only two                         
 145    |  boxes and so we can just normalize and the right thing will happen.              
 146    |  So, three quarters times one half is equal to three eighths. And 2/5 times       
 147    |  1/2 is equal to 2/10 or 1/5. And                                                 
 148    |  that's right. So 3/8 is also 15 over 40. 1/5 is 8 over 40. Why do                
 149    |  we do that? Because we want to be able                                           
 150    |  to add them up and normalize and so that means                                   
 151    |  if you added those two together and put them                                     
 152    |  in the denominator, that would give you 23 over 40.                              
 153    |  And, so how much is 15 40ths of 23 over 40ths well, it's 15 out of 23.           
 154    |  And so, without ever directly computing the probability that                     
 155    |  1 equals green. We know that the probability of                                  
 156    |  us being in box 1, given that the first                                          
 157    |  ball pulled was green is 15 over 23. Which                                       
 158    |  was a lot of work to do considering that                                         
 159    |  we knew we were going to multiply it by zero.                                    
 160    |  >> [LAUGH]                                                                       
 161    |  >> Which meant none of this work mattered.                                       
 162    |  >> Okay.                                                                         
 163    |  >> Or we did it because we love probability.                                     
 164    |  >> No it was, it was kind of helpful because                                     
 165    |  we needed to know how to normalize these two numbers.                            
 166    |  >> Right, so it was useful but, I                                                
 167    |  mean, just the whole thing we already kind of knew.                              
 168    |  >> Yeah.                                                                         
 169    |  >> That [LAUGH] that was going to be zero.                                       
 170    |  >> But this one we didn't know.                                                  
 171    |  >> Right, this one we didn't know, and so now we know that the, the              
 172    |  other case is 8 23rds, and we're done. So 0 times 15, divided by 23 is           
 173    |  0, and three quarters times 8 23rds is 24 over 92.                               
 174    |  >> Right, and we can, there's a factor of                                        
 175    |  4 in both of those. So it's actually 6 23rds.                                    
 176    |  >> That's what I said.                                                           
 177    |  >> Woohoo!                                                                       
 178    |  >> Wow.                                                                          
 179    |  >> [LAUGH]                                                                       
 180    |  Boy it would be nice if we had an algorithm to do this for us.                   
 181    |  >> Man, and the algorithm shou, shou, should not involve me. [LAUGH]             


##  20 - Naive Bayes
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  Alright, so what we'd like to do is work up to an algorithm that can             
 2      |  actually do some of these inference steps instead                                
 3      |  of having to think it through each time                                          
 4      |  de novo. So what I'm going to do is, let's hearken back to an example that we    
 5      |  looked at before which is about spam detection.                                  
 6      |  Do you, do you remember the spam example?                                        
 7      |  >> I do remember the spam example. That                                          
 8      |  was way back in the boosting lecture, right?                                     
 9      |  >> Yes, I think you did that one. I did, it was an excellent example.            
 10     |  >> There you go. So,                                                             
 11     |  we didn't think about it in a Bays net setting,                                  
 12     |  it was in a classification setting we were trying to                             
 13     |  come up with the rule, but let's think of this                                   
 14     |  as a Bays Net where there's a bunch of different variables                       
 15     |  that can be true or false about any given email                                  
 16     |  message. It can either be spam or not. It can contain                            
 17     |  the word Viagra or not. It can contain the word                                  
 18     |  prince or not. It maybe contains the word udacity, or not.                       
 19     |  >> Mm.                                                                           
 20     |  >> Right? And, so, just as we think about these as these random variables.       
 21     |  If we're trying to build a belief net or a base net                              
 22     |  with these variables. We have to say. kind of, what's dependent on what. In      
 23     |  terms of representing the probibilities. So how would you, how do you            
 24     |  think we should draw arrows to,to relate these to quantities to each other.      
 25     |  >> I think that the arrows should go down from spam to                           
 26     |  the other features of spam mail and I'll tell you why. Because if,               
 27     |  I like this notion of generation that you talked about a                         
 28     |  little bit earlier. It seems to me if you know. Spam                             
 29     |  mail or not. It sort of generates certain words. And as                          
 30     |  written as these are like words I mean I know the, the                           
 31     |  spam example these are you know, kind of stand ins for                           
 32     |  features. But they're sort of features of spam mail. Yeah I                      
 33     |  think that's a really good way to think about it. So,                            
 34     |  in some sense what we're saying if we draw the bayes net                         
 35     |  in this way, then any given email                                                
 36     |  message has some probability of being spam. And                                  
 37     |  given that it's spam, it has some                                                
 38     |  probability of containing different sets of possible words.                      
 39     |  >> Right.                                                                        
 40     |  >> So, I would say that, well what, so what do you, oh                           
 41     |  let's see if we can actually fill in some of these values. So                    
 42     |  given that we have a spam message, how likely do you think it                    
 43     |  would be to contain a word like, well let's say the word viagra.                 
 44     |  >> Fairly high.                                                                  
 45     |  >> It might                                                                      
 46     |  be 0.3, but a non-spam message might be, I don't know, like 0.001.               
 47     |  >> Right.                                                                        
 48     |  >> Something like that. So how about a word like prince?                         
 49     |  >> Well I get a lot of email about Prince because I'm a Prince fan.              
 50     |  >> Yeah, I was thinking that. That's                                             
 51     |  why I thought it would an interesting example.                                   
 52     |  So, if in your spam messages, how likely is it for Prince to come up?            
 53     |  >> Fairly low.                                                                   
 54     |  >> Maybe like 0.2                                                                
 55     |  because you're talking about the Nigerian princes                                
 56     |  and whatnot. On the other hand among your                                        
 57     |  non spam messages how likely is it for prince to come up, do you think?          
 58     |  >> Well I get a lot of non spam, so,                                             
 59     |  its still relatively low, but not as low as .001.                                
 60     |  >> Alright, so, let's say .1.                                                    
 61     |  >> Okay.                                                                         
 62     |  >> That's a lot of prince spam.                                                  
 63     |  >> You can never have enough prince spam.                                        
 64     |  >> Alright, so in the messages                                                   
 65     |  that you have that are spam, how often does the word Udacity come up?            
 66     |  >> I guess, it's pretty low.                                                     
 67     |  >> I don't think I've ever seen a spam                                           
 68     |  that mentions Udacity. Alright, what about your non-spam email?                  
 69     |  >> Again, increasingly, it's getting higher and higher.                          
 70     |  >> [LAUGH]                                                                       
 71     |  >> Almost as much as I get prince mail.                                          
 72     |  All right, so we'll call that .1 as well then.                                   
 73     |  >> Okay.                                                                         
 74     |  >> All right, so now we have, oh an,                                             
 75     |  an what's the probability of spam versus not spam?                               
 76     |  >> [INAUDIBLE] Probability to have spam is pretty low,                           
 77     |  I'm going to say, at this point, actually; it's not                              
 78     |  that low. At this point, it's probably half my mail.                             
 79     |  >> Wow. All right, I'm going to say .4                                           
 80     |  Alright, so this is now, Bayesian network structure                              
 81     |  that actually is, it's not exactly generating spam,                              
 82     |  but it is kind of capturing features of email                                    
 83     |  messages as they come in. So, we should                                          
 84     |  be able to answer questions like what's the                                      
 85     |  probability that a given message is spam, given                                  
 86     |  that the message has Viagra in it but not                                        
 87     |  prince or udacity. So, how would we work this out?                               
 88     |  >> Well, Since it says Naive Bays I think I would use Bayes rule.                
 89     |  >> That would be nieve of you. Now we have applied                               
 90     |  Bayes rule, we have flipped things around, why is this giving                    
 91     |  us an advantage? For this kind of network structure it actually                  
 92     |  has a huge advantage because we can break this first quantity up.                
 93     |  >> Oh I do see that, so this is where those conditional independences            
 94     |  come into play If I'm reading this network right, each one of those attribute    
 95     |  values is conditionally independent of each other,                               
 96     |  given that you know the value of SPAM.                                           
 97     |  >> Excellent.                                                                    
 98     |  >> So then that means that the first quantity there                              
 99     |  is actually a product of each of those conditional probabilities.                
 100    |  >> Yeah, so this is a really convenient strucutre.                               
 101    |  Because it really just decomposes into all these separate                        
 102    |  helpful quantities. So in particular, we can actually derive                     
 103    |  this by applying the chain rule. But what we end                                 
 104    |  up with is that this joint probability over these                                
 105    |  three variables decomposes into a product of three independent joint             
 106    |  probabilities. The probability that's, Contains viagra given that it's           
 107    |  spam, which we have. That number is 0.3. That probability                        
 108    |  that prince doesn't appear in it, given that it's                                
 109    |  spam and that is that it doesn't contain prince given                            
 110    |  that it is spam. So that should 0.8, cause 1 minus the                           
 111    |  0.2. And that it's not udacity given that it's spam. Is                          
 112    |  going to be 1 minus this 0.0001, should be 0.9999. All right.                    
 113    |  So this is the case when things, when it is spam, and if it's not spam, we       
 114    |  can do this same thing and get a product,                                        
 115    |  and that we can normalize, to get what the,                                      
 116    |  the relative probabilities between it being spam and not spam. So then I'm a     
 117    |  big fan of normalization, but of course this makes me think about, since it's    
 118    |  sort of a classification problem, we only                                        
 119    |  really care about knowing which one's more                                       
 120    |  likely. We don't really care about the                                           
 121    |  probability, right? Do we have to normalize?                                     
 122    |  >> Yeah, yeah because we do care about the probability.                          
 123    |  >> Oh we do?                                                                     
 124    |  >> Yeah because we're... I asked" What is the                                    
 125    |  probability of spam given these other quantities. Oh, I see.                     
 126    |  >> But you're right. So the observation                                          
 127    |  that you're making is a really good one. Which is that we                        
 128    |  can do probability calculations in this                                          
 129    |  setting, and that's actually going to give                                       
 130    |  us answers to classification problems. And we're going to connect this back to   
 131    |  machine learning. But but first let's write a general form of this formula.      
 132    |  >> Okay.                                                                         
 133    |  >> Because this this seems a little bit specific. Alright so                     
 134    |  the general form for this, is that if we're trying to figure                     
 135    |  out the probability of, of some kind of a a root node                            
 136    |  like this, when you have all these little bristly things coming down.            
 137    |  You can think of it as a probability of a                                        
 138    |  value given a bunch of attributes. And that's going to be equal                  
 139    |  to the product of the probability that each of those                             
 140    |  attributes would be generated by that. Underlying this v. This, this             
 141    |  the label or the or the underlying class. Times the                              
 142    |  prior probability that v and then we just normalize by all                       
 143    |  the different possible values of, of v. This, this quantity across               
 144    |  all the possible types of v. So so this is one                                   
 145    |  way of actually getting a very general kind of. Inference [UNKNOWN],             
 146    |  and there's, as you were pointing out, Charles, there's a. There's               
 147    |  a really nice reason to think about things in this form,                         
 148    |  because it does let you do a kind of classification. So                          
 149    |  essentially if you think of, of this top node as being                           
 150    |  the class, this is what was playing the role of V                                
 151    |  here, and these are all a bunch of attributes, then even                         
 152    |  if, if we have a way of generating attribute values from classes.                
 153    |  What this lets us do is to go the other way.                                     
 154    |  That we observe the attribute values and we can infer the class.                 
 155    |  >> Nice, so what's the equation for that?                                        
 156    |  >> Right, so the, the maximum oposterior                                         
 157    |  class if you're just trying to find whats                                        
 158    |  the most likely class given the, the data that you've seen. You can just take    
 159    |  an arg max over all the different possible values of that, that root node of     
 160    |  the prob, its probability times the product                                      
 161    |  of all the attribute values given that class.                                    
 162    |  So this would actually let us if you're, if you're been paying attention,        
 163    |  we could, in this particular case, compute map spam. Which is a palindrome.      
 164    |  >> Wow. That is spectacular.                                                     
 165    |  >> You did not see that coming did you?                                          
 166    |  >> No I did not.                                                                 


##  21 - Why Naive Bayes Is Cool
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So this idea of Naive Bayes, where you have                                      
 2      |  a network that has a label producing or, or                                      
 3      |  conditionally producing a bunch of attribute values, is just                     
 4      |  a really cool and powerful idea. So one of the,                                  
 5      |  one of the issues is that, even though inference                                 
 6      |  in general is, is is a very difficult problem it's                               
 7      |  NP hard. To work out what these probabilities are,                               
 8      |  when you have a naive Bayes structure, it's cheap. It's,                         
 9      |  it's the formula that we had on the previous slide. The                          
 10     |  number of parameters that you need to write down, again even if                  
 11     |  you have a very large number of variables, it's not exponential                  
 12     |  in the number of variables, it's just linear. There's, two probabilities for     
 13     |  each of the attributes and one probability for the class. We                     
 14     |  can actually estimate these probabilities. So so far, we've only been talking    
 15     |  about Bayes Nets in, in not in a learning setting, but in                        
 16     |  a setting where we just write down what all the numbers are.                     
 17     |  We can actually very easily estimate these parameters. How would we              
 18     |  do that? Well the odd, the easy way to do it, is                                 
 19     |  you count. When you're trying to estimate the probability of a particular        
 20     |  attribute value given a class, it's really just in your, in your                 
 21     |  labeled data. How often do you have an example that has an                       
 22     |  attribute value in that class, and then divide by the number of                  
 23     |  times you had that class at all, and that gives you the                          
 24     |  conditional probability. So this is, you know in, in the case of                 
 25     |  infinite data this is actually going to give you exactly the right               
 26     |  number. It also connects this notion of inference that we've been                
 27     |  talking about with classification. Which is mostly what this, this mini          
 28     |  course has been about. So, that's really great to have a connection,             
 29     |  it actually allows us to do all kinds of interesting things                      
 30     |  like instead of only generating what the labels are, we can actually             
 31     |  generate what attributes are. We can do inference on, in, in                     
 32     |  any of these directions. And it turns out it's wildly successful empirically.    
 33     |  So, my understanding is that Google uses a tremendous amount of Naive Bayes      
 34     |  classification in what they do. If you have enough data you can estimate         
 35     |  these values really well, and Naive Bayes is just remarkably good. So yeah       
 36     |  so it's like unclear why we'd even have any other algorithms, right Charles?     
 37     |  >> Well, there's no free lunch. But I, I gotta say I, I you know                 
 38     |  there's this as a famous man once said it works in practice but doesn't work     
 39     |  in theory. And I'm trying to figure out how this can possibly work.              
 40     |  So I noticed it's called Naive Bayes. And, I think I know why now.               
 41     |  >> Alright.                                                                      
 42     |  >> One is that it's well it's naive and                                          
 43     |  in fact painfully ridiculous to believe that the bayesian                        
 44     |  net that you wrote up there in the upper                                         
 45     |  right-hand corner represents the real world most of the time.                    
 46     |  >> Hm, I see, and why is that?                                                   
 47     |  >> Well because                                                                  
 48     |  what the, what the network says is that all                                      
 49     |  of the attributes are conditionally independent giving that you know             
 50     |  the label, that just can't be true. We talked                                    
 51     |  about this before where we were using evasion inference to,                      
 52     |  to derive the sum of squared errors that it                                      
 53     |  makes a very strong assumption about where your errors come                      
 54     |  from and an even stronger assumption about where your errors                     
 55     |  don't come from. So you're not modeling any of the                               
 56     |  interrelationships, between, the different attributes and                        
 57     |  that just doesn't seem right. So, one                                            
 58     |  question I have. I have two, we'll save the second one though. One question      
 59     |  I have is, how in the world can it possibly be the case                          
 60     |  that this works in practice? Hm, that's a good question. It does. Moving on.     
 61     |  >> [LAUGH] No, that's not satisfying.                                            
 62     |  >> No?                                                                           
 63     |  >> How about, how about I give it a guess? Okay?                                 
 64     |  >> Alright.                                                                      
 65     |  >> Now,                                                                          
 66     |  now that I yelled at you, why don't I, why don't I give it a guess.              
 67     |  >> [LAUGH]                                                                       
 68     |  >> I think it comes back to one of                                               
 69     |  the conversation we had in the previous slide. When                              
 70     |  I was saying well we don't have to care.                                         
 71     |  We don't care about probabilities. And you said we                               
 72     |  do care about probabilities because of the question your                         
 73     |  asking and that was fair. But once were down                                     
 74     |  to classification. The probabilities really don't matter. Right all              
 75     |  that matters is that you get the right answers.                                  
 76     |  So its okay I guess if the probabilities you                                     
 77     |  get are long. So long as they're sort, sort                                      
 78     |  of in the right direction right. That you end                                    
 79     |  up getting the, the right label as a result.                                     
 80     |  >> Yeah, that's a good point. That in fact                                       
 81     |  we're introducing this idea in the context of, of                                
 82     |  Bayesian Inference it might actually not be so good                              
 83     |  at that even if it is particularly good at classification.                       
 84     |  >> Oh, oh actually I think I have a good example so,                             
 85     |  so here, here write this down. So let's imagine there are four                   
 86     |  actually you can use the network that you have up there okay                     
 87     |  >> Good.                                                                         
 88     |  >> So let's say that the first attribute, I'm just going to call it A            
 89     |  and the second attribute I'm going to call B, and let's say we're really, we're  
 90     |  really lucky and our naïve assumption is                                        
 91     |  right and they really are conditionally independent. But                         
 92     |  let's say the third attribute, is actually                                       
 93     |  just another way of writing down A, and                                          
 94     |  the fourth attribute is just another way of writing down                         
 95     |  B. So, clearly there are interrelationships between the attributes, right?       
 96     |  >> The third attiribute is the first one, the fourth attribute is                
 97     |  the second one. There's not way around that. And so you'd think                  
 98     |  Naive Bayes would fail. But, actually, looking at your equation right below      
 99     |  there where you're doing counting, I actually think, it'll work just fine.       
 100    |  >> Why?                                                                          
 101    |  >> Because all you're really doing                                               
 102    |  is double counting the sort of weight of                                         
 103    |  attribute A, but you're also double counting the                                 
 104    |  weight of attribute B and they'll cancel each                                    
 105    |  other out. And you'll get the right answer.                                      
 106    |  >> When you do the arg max, but these                                            
 107    |  >> When you do the arg max                                                       
 108    |  >> You get bad probabilities. The probabilities                                  
 109    |  end up being kind of squared of what                                             
 110    |  they should, what they're supposed to be.                                        
 111    |  But that's okay because the ordering is preserved.                               
 112    |  >> Right, exactly. And so, even if you're unlucky and                            
 113    |  the fourth attribute wasn't B but it was something else, C.                      
 114    |  It doesn't matter if you double count A as                                       
 115    |  long as it still gives you the right label.                                      
 116    |  And you can imagine that if you have weak                                        
 117    |  inner relationships or, you know, you have enough attributes and,                
 118    |  and so on that you would still get the                                           
 119    |  right, you know, yes this is the correct label, even                             
 120    |  if you've got the probabilities wildly wrong. Okay, so                           
 121    |  I'm willing to believe that that could happen in practice.                       
 122    |  >> Okay.                                                                         
 123    |  >> So in fact, my guess is that Naive Bayes believes                             
 124    |  it's answer too much. But it doesn't matter if it happens to be right.           
 125    |  >> All right and did you have other issues with it?                              
 126    |  >> So the second problem I have actually boils down to that                      
 127    |  equation you wrote there. So it's really nice and neat that you                  
 128    |  can compute the probabilities of seeing an attribute, given a value by           
 129    |  just doing counting. But, I don't have an infinite amount of data, right?        
 130    |  >> Not on a bad day, no.                                                         
 131    |  >> No. Or even on a good day I usually                                           
 132    |  don't have an infinite amount of data. So what if                                
 133    |  I'm unlucky enough that for some particular attribute value,                     
 134    |  I have never seen it paired with that label, V.                                  
 135    |  >> Right. So then, that means this numerator will be zero                        
 136    |  >> Right.                                                                        
 137    |  >> So.                                                                           
 138    |  >> Well that numerator is zero, but since                                        
 139    |  the computation involves a product by just having                                
 140    |  one attribute value that I've never seen before.                                 
 141    |  I'm going to end up saying well the probability                                  
 142    |  of that entire product of seeing that value given                                
 143    |  a set of attributes is also going to be zero. So                                 
 144    |  one unseen attribute, basically says it doesn't matter what else                 
 145    |  is going on. Which seems a little weird, right? You,                             
 146    |  you, you'd think that you, if all the other                                      
 147    |  attributes are screaming yes, yes, yes, yes, it should be                        
 148    |  positive. But just because you haven't happened to have seen                     
 149    |  any examples of some other one single attribute, that shouldn't                  
 150    |  be enough to do veto.                                                            
 151    |  >> Good point, so in fact that's not what                                        
 152    |  people often do. People will often, what they call smooth                        
 153    |  the probabilities, by essentially initializing the count, so that                
 154    |  nothing is zero, everything has a tiny little non-zero value                     
 155    |  in it. And there's, there's smarter and less smart                               
 156    |  ways of doing that, but no, you're absolutely right. That,                       
 157    |  that is, that zeroing out problem is a real                                      
 158    |  thing and you have to be a little bit careful.                                   
 159    |  >> Hey, hey I just had a thought. So,                                            
 160    |  if you, you have to do that, because if you don't do                             
 161    |  that, then you're believing your data too much. You're kind of over fitting.     
 162    |  >> Ooh. Over fitting comes up again.                                             
 163    |  >> Oh, oh, it's okay, okay so, so, so, so, so bear with                          
 164    |  me on this Michael. So if you're over fitting by believing the data,             
 165    |  and you're fixing it by smooth, I usually spell it with a V,                     
 166    |  but whatever. If you, you'd think that by being smooth, then you're making       
 167    |  an assumption. There's a kind of inductive                                       
 168    |  bias, right? Your'e, you're saying that I go                                     
 169    |  in with the assumption that they're sort                                         
 170    |  of all things are at least mildly possible.                                      
 171    |  >> Good.                                                                         
 172    |  >> Huh.                                                                          
 173    |  >> Yea, that's, that's right.                                                    
 174    |  >> Okay, Naive Bayes is cool, you've convinced me.                               
 175    |  >> Nice.                                                                         


##  22 - Wrapping Up
 no     |  subtitle                                                                         
 -----  |  -------------------------------------------------------------------------------- 
 1      |  So I was thinking of talking to you more                                         
 2      |  about sampling, but it seems like it might work out                              
 3      |  best to just have some hands on experience with it                               
 4      |  so we're going to put those things on the homework. So                           
 5      |  given that we're actually in a position now to, to                               
 6      |  kind of wrap up the whole Bayes net inference piece                              
 7      |  that we were talking about. So do you want to help                               
 8      |  remind me, Charles, what were the things that we covered?                        
 9      |  >> Sure, I can help you with that. We covered Bayesian [LAUGH]                   
 10     |  I'm sorry.                                                                       
 11     |  I'm punch drunk.                                                                 
 12     |  >> I'm going to choose not to pay attention to that. Instead, write              
 13     |  Bayesian Networks. We talked about the                                           
 14     |  Bayesian Network representation of joint probability distributions.              
 15     |  >> Right. We did a lot of examples of how to do inference with networks.         
 16     |  You know, exactly how do we, do we                                               
 17     |  compute probabilities of particular values. We mentioned sampling.               
 18     |  >> That's right.                                                                 
 19     |  >> And then we did a night phase.                                                
 20     |  >> Well first we did say that, that in general it's hard                         
 21     |  to do exact imprints. It's actually hard to do even approximate imprints.        
 22     |  >> Mm-hm.                                                                        
 23     |  >> But we talked about a special                                                 
 24     |  case of bayesian networks, that was called naive                                 
 25     |  bayes with the naive part being, that we're                                      
 26     |  assuming that attributes are independent of one another.                         
 27     |  >> Condition on the label.                                                       
 28     |  >> Right. And this was actually helping us make a                                
 29     |  link between all this bayesian stuff. The bayesian rabbit hole we                
 30     |  went down. And classification, which is the core machine learning                
 31     |  topic that we've been spending a lot of time on.                                 
 32     |  >> So the other thing that I really                                              
 33     |  liked about this notion, this link to classification, Michael,                   
 34     |  is that when I was talking about Bayesian                                        
 35     |  learning, what we ended up with at the end                                       
 36     |  is this nice idea that we had a gold standard, right? We had a sort of way       
 37     |  of talking about what the right hypothesis was                                   
 38     |  and, ultimately, what the right classification was by computing                  
 39     |  these probabilities. And sometimes, we couldn't do it because, typically,        
 40     |  you can actually do the for loop that requires you compute                       
 41     |  conditional probabilities of hypothesis given data. Over say an infinite number  
 42     |  of hypothesis, but at least we kind of knew what the                             
 43     |  right thing was and we made right assumptions we could do                        
 44     |  things like derive, oh I don't know, a sum of squared                            
 45     |  errors or various other things that you might do and that                        
 46     |  was all very cool. But what you've done here when you                            
 47     |  do inference. Is at least with a base case,                                      
 48     |  you've shown us a way that we can do classification                              
 49     |  using these things, that actually is tractable, and is the                       
 50     |  right thing to do under certain assumptions. I really like                       
 51     |  that. And the other thing that I think is worth                                  
 52     |  mentioning is that not only does it link this Baysean                            
 53     |  learning to classification. But it connects classification back to this          
 54     |  general notion of invasion learning, invasion inference where, you don't         
 55     |  have to worry about just figuring out the most likely label                      
 56     |  given a bunch of attributes. But because it's a Bayes network and                
 57     |  you can compute anything from it, you could try to ask                           
 58     |  well what's the likelihood that I see some particular attribute or set           
 59     |  of attributes, given a label or given a subset of attributes                     
 60     |  on all those kind of things that you could do. With the                          
 61     |  Bayesian learning. So inference gives us this power to not just                  
 62     |  do classification, but to do a larger set of things beyond classification.       
 63     |  I think that's kind of cool.                                                     
 64     |  >> Cool. Yeah, well said. The, the For, and another thing,                       
 65     |  kind of in that same space is that it handles missing attributes                 
 66     |  really well. So whereas things like, oh. You know, decision trees                
 67     |  and so forth, if you give me an example that doesn't have                        
 68     |  one of the attribute values and you've hit that part of                          
 69     |  the decision tree where you need to know that attribute value you're             
 70     |  stuck. Whereas in this naive base setting, you can still do the                  
 71     |  probabalistic inference over the missing attributes                              
 72     |  because all the things are linked                                                
 73     |  by probabilities.                                                                
 74     |  >> Nice.                                                                         
 75     |  >> All right. So I think, you know, you'll, you'll get                           
 76     |  a much stronger handle of this when you go through the,                          
 77     |  the homework problems. But I think that's enough for Bayesian inference.         
 78     |  And I think that actually wraps up classification and regression more generally. 
 79     |  >> Right. So we're done with supervised learning. Well, one's never done with    
 80     |  supervised learning. But we're at least done with this part of the course.       
 81     |  >> Because there's always more to supervise learn.                               
 82     |  >> That's right. And in particular you'll get                                    
 83     |  a nice example of this, because you'll be taking an exam.                        
 84     |  >> [LAUGH]                                                                       
 85     |  >> And your input will be the exam, and then we'll give you a label back.        
 86     |  >> [LAUGH] I guess that's one way to think about it.                             
 87     |  >> Well and then they'll get to generalize beyond                                
 88     |  that for the next time they take the exam.                                       
 89     |  >> Very good! All right. Well, well thanks                                       
 90     |  very much, this has been fun. Thanks Charles.                                    
 91     |  >> This has been fun. I will see you in the second mini course.                  
 92     |  >> All right.                                                                    
 93     |  >> Bye.                                                                          


