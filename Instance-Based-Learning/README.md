#  Instance Based Learning Subtitles
##  01 - Instance Based Learning Before
 |  no     |  subtitle                                                                          | 
 |  -----  |  --------------------------------------------------------------------------------  | 
 |  1      |  Hi Michael!                                                                       | 
 |  2      |  >> Hey Charles! How's it going?                                                   | 
 |  3      |  >> It's going pretty well. How's it going with you?                               | 
 |  4      |  >> It is a beautiful fall day here in Providence Rhode Island.                    | 
 |  5      |  >> Oh that's right it's fall, when you are.                                       | 
 |  6      |  >> [LAUGH] Yeah, I think, that's right.                                           | 
 |  7      |  >> So, what we're going to do today, Michael.                                     | 
 |  8      |  If you will indulge me. Is ,we're going to                                        | 
 |  9      |  talk about a different class of ,uh, learning                                     | 
 |  10     |  algorithms and approaches than we've been talking about before.                   | 
 |  11     |  >> So now the other ones were low class, this is going to                         | 
 |  12     |  be high class?                                                                    | 
 |  13     |  >> Exactly. And we call them instance based learning. Which                       | 
 |  14     |  sounds very hoity toity and high voluting. Don't you agree?                       | 
 |  15     |  >> Yeah, sure, why not?                                                           | 
 |  16     |  >> [LAUGH]                                                                        | 
 |  17     |  >> It sounds like it maybe has good posture.                                      | 
 |  18     |  >> It does, in fact, have good posture.                                           | 
 |  19     |  >> Well let's, let's learn about it. I'm, I'm, I'm intrigued.                     | 
 |  20     |  >> Yeah, so I think that ,uh, what we're going to                                 | 
 |  21     |  end up talking about to day is kind of interesting, I                             | 
 |  22     |  hope. But it's sort of different, and what I'm hoping is                          | 
 |  23     |  through this discussion Is that, we will be able to reveal                        | 
 |  24     |  some of the unspoken assumptions that we've been making so far, okay?             | 
 |  25     |  >> Unspoken assumptions, it sounds, yeah, okay, that sounds                       | 
 |  26     |  like we should get to the bottom of that.                                         | 
 |  27     |  >> Yes, so let's do that. So, just to remind you of what we have                  | 
 |  28     |  been doing in the ,um, past, this is what was going on with all of                | 
 |  29     |  our little supervised learning tasks, right. We                                   | 
 |  30     |  were given a bunch of training data ,labeled                                      | 
 |  31     |  here as you know, x, y One, xy two, xy three, dot, dot, dot, xy zen.              | 
 |  32     |  And ,uh, we would then learn some function.                                       | 
 |  33     |  So, for example, if we have a bunch of                                            | 
 |  34     |  points in a plane, we might learn a                                               | 
 |  35     |  line to represent them, which is what this little                                 | 
 |  36     |  blue line is. And what was happening here is we take all this data. We come up    | 
 |  37     |  with some function that represents the data. And                                  | 
 |  38     |  then we would throw the data away effectively, right?                             | 
 |  39     |  >> Okay. Yeah, so like, black is the input here and then                          | 
 |  40     |  the two blue things are what get derived by the learning algorithm.               | 
 |  41     |  >> Right. And then in                                                             | 
 |  42     |  the future when we get some data point, let's                                     | 
 |  43     |  call it x, we would pass it through this function                                 | 
 |  44     |  whatever it is. In this case, probably line. And                                  | 
 |  45     |  that would, be how we would determine answers going forward.                      | 
 |  46     |  >> Yeah. That's, that's what we've been talking about.                            | 
 |  47     |  >> Right. And in particular without reference                                     | 
 |  48     |  to the original data. So. I want                                                  | 
 |  49     |  to propose an alternative and the alternative is basically going to not do this.  | 
 |  50     |  >> [LAUGH]                                                                        | 
 |  51     |  >> So let me give you a, let me, let me tell u exactly what I mean by that.       | 



##  02 - Instance Based Learning Now
 |  no     |  subtitle                                                                          | 
 |  -----  |  --------------------------------------------------------------------------------  | 
 |  1      |  Okay, so here what I mean concretely by not doing this thing                      | 
 |  2      |  over here any more. So here what I'm proposing we do now. We                      | 
 |  3      |  take all the data, all of the training data we had, the                           | 
 |  4      |  xy1, xy2, dot, dot, dot, xyn and we put it in a database                          | 
 |  5      |  >> Ah-ha.                                                                         | 
 |  6      |  >> And then next time we get some new x to look                                   | 
 |  7      |  at, we just look it up in the database. And we're done.                           | 
 |  8      |  >> None of this fancy shmancy learning, none of this                              | 
 |  9      |  producing an appropriate function like you know, wx+b, or what ever               | 
 |  10     |  the equation of a line is. None of that fancy stuff anymore.                      | 
 |  11     |  We just stick in to the data base. People written data                            | 
 |  12     |  base programs before. We'll look it up when we're done. We're done.Period         | 
 |  13     |  >> I feel like you've changed the paradigm.                                       | 
 |  14     |  >> Yes, I am a paradigm changer. So what do you think?                            | 
 |  15     |  >> It's like, it's like disruptive. It's going to throw off the markets.          | 
 |  16     |  >> Yeah. It's going to change everything. So, what do you think?                  | 
 |  17     |  >> well, I mean, so there's a bunch of                                            | 
 |  18     |  really cool things about this idea. Which is why                                  | 
 |  19     |  I'm excited. So one is it, you know, it                                           | 
 |  20     |  doesn't forget, right? So it actually is very reliable.                           | 
 |  21     |  It's very ,um ,dependable, right, so if you put in an x, y pair you ask for the   | 
 |  22     |  x you're going to get that y back instead of                                      | 
 |  23     |  some kind, you know, crack potty, smooth version of it.                           | 
 |  24     |  >> Right, so we don't, yeah that's a good point. So we look at this little        | 
 |  25     |  blue line over here, you'll notice that say,                                      | 
 |  26     |  for this little x over here, we're not going to                                   | 
 |  27     |  get back what we put in, so, it remembers, it's like an elephant. Good.           | 
 |  28     |  >> So that's kind of cool. Another thing is that                                  | 
 |  29     |  there's none of this wasted time, you know, doing learning [LAUGH].               | 
 |  30     |  It just takes the data and it, and it's, very                                     | 
 |  31     |  rapidly just puts it in the database. So [CROSSTALK] it's fast.                   | 
 |  32     |  >> It's fast. It's like. I like it when you say nice things                       | 
 |  33     |  about my algorithms. Okay. So it's fast. Anything else, you can think of?         | 
 |  34     |  >> Sh, yeah I cant think of                                                       | 
 |  35     |  one more thing at least.                                                          | 
 |  36     |  >> Mm-hm.                                                                         | 
 |  37     |  >> Which is ,that like you, it's simple.                                          | 
 |  38     |  >> [LAUGH] That's true. I am simple. I am simple and                              | 
 |  39     |  straightforward. I just need a few things to make me happy.                       | 
 |  40     |  >> Bacon.                                                                         | 
 |  41     |  >> Bacon, and                                                                     | 
 |  42     |  >> And                                                                            | 
 |  43     |  >> Chocolate.                                                                     | 
 |  44     |  >> Oh nice.                                                                       | 
 |  45     |  >> Have you ever had chocolate covered bacon?                                     | 
 |  46     |  >> That seems wrong.                                                              | 
 |  47     |  >> You know, you would think so, but it turns out it's delicious. It's            | 
 |  48     |  like if you take fat, and sugar, and you put it together somehow you like         | 
 |  49     |  it [LAUGH] I'm not making this up you can buy                                     | 
 |  50     |  chocolate covered bacon, you're unsurprised to here in America. Okay, so          | 
 |  51     |  we've got three good things in remember stuff. So, you                            | 
 |  52     |  know, none of this little noisy throwing away information. It's very              | 
 |  53     |  fast, you just stick it in a database. Using your                                 | 
 |  54     |  favorite data base. And looking up is going to be equally as                      | 
 |  55     |  fast. And it's very simple. There's really no interesting learning                | 
 |  56     |  going on here. So it's the perfect algorithm when we're done.                     | 
 |  57     |  >> Okay. I mean, I, it feels                                                      | 
 |  58     |  like there's more that we need to say though.                                     | 
 |  59     |  >> Like what?                                                                     | 
 |  60     |  >> In particular the way that you wrote this, F of X equals look up of X. If      | 
 |  61     |  I give you one of the other points in                                             | 
 |  62     |  between ,then it will return no such point found.                                 | 
 |  63     |  Which means it's really quite conservative. It's not willing                      | 
 |  64     |  to go out on a limb and say ,well                                                 | 
 |  65     |  I haven't seen this before but. It ought to                                       | 
 |  66     |  be around here, instead it just says, I don't know.                               | 
 |  67     |  >> Mm. So the down side of remembering is, no                                     | 
 |  68     |  generalization.                                                                   | 
 |  69     |  >> [LAUGH] And I guess a similar sort of issue is that when you, when             | 
 |  70     |  you call it memorization, it makes, it reminds me of the issues that we saw with  | 
 |  71     |  regard to overfitting So, it bottles the noise                                    | 
 |  72     |  exactly, it bottles exactly what it was given.                                    | 
 |  73     |  So it's going to be very sensitive to noise. So it's kind of a yes and no.        | 
 |  74     |  >> So that's a little scary and, and it can over fit in a couple of               | 
 |  75     |  ways, I think it can over fit ,um,                                                | 
 |  76     |  by believing the data too much that is literally                                  | 
 |  77     |  believing all of it and what do you do if you                                     | 
 |  78     |  have couple ,uh, speaking in noise, what if you have you know                     | 
 |  79     |  a couple of examples that are all the same. I have got                            | 
 |  80     |  an x, shows up multiple times but each with a different y.                        | 
 |  81     |  >> Oh,the same x,ah, yeah, and so the look up                                     | 
 |  82     |  would return two different things and this algorithm or whatever                  | 
 |  83     |  that you have described so far, wouldn't commit to either                         | 
 |  84     |  of them and it would just say, hey, here is both.                                 | 
 |  85     |  >> Yeah, that seems problematic.                                                  | 
 |  86     |  >> Okay, alright. But I feel like,                                                | 
 |  87     |  you know, you are going to to tell me, how                                        | 
 |  88     |  to fix those things. So I wasn't too worried.                                     | 
 |  89     |  >> Yeah, well, there is gotta be a nice way                                       | 
 |  90     |  of fixing it. I think There's sort of a basic problem                             | 
 |  91     |  here, which is that we're taking this remembering and then                        | 
 |  92     |  looking up a little too literally, right? So I stick in                           | 
 |  93     |  the data, and I can get back exactly the data                                     | 
 |  94     |  that I got, but I can't get back anything that I                                  | 
 |  95     |  don't have, and that seems like something that we might                           | 
 |  96     |  be able to overcome if we're just a little bit clever.                            | 
 |  97     |  >> Mm.                                                                            | 
 |  98     |  >> So let's see if we can be a little bit clever.                                 | 



##  03 - Cost of the House
 |  no     |  subtitle                                                                          | 
 |  -----  |  --------------------------------------------------------------------------------  | 
 |  1      |  Okay Michael, so let's see if we can, work                                        | 
 |  2      |  together to deal with this minor triffle of a problem,                            | 
 |  3      |  that ,ah, you've observed with my cooling algorithm, okay.                        | 
 |  4      |  So, here's some data, it's a graph and you see                                    | 
 |  5      |  here's a y axis and here's an x axis,                                             | 
 |  6      |  and each of these points, represents a house, on this                             | 
 |  7      |  map, which I'm, I'm cleverly, using in the background. [CROSSTALK]                | 
 |  8      |  And, you'll notice, that each of the dots is colored.                             | 
 |  9      |  I'm going to say that red represents, really expensive houses, blue               | 
 |  10     |  represents, moderately expensive houses, and                                      | 
 |  11     |  green represents, really inexpensive houses. Okay?                                | 
 |  12     |  >> Okay, where is this?                                                           | 
 |  13     |  >> Where is this? Oh, this is Georgia Tech,                                       | 
 |  14     |  as you can tell because, it says Georgia Tech.                                    | 
 |  15     |  >> Oh, I see it now.                                                              | 
 |  16     |  >> Okay. So, here's what I want you to do. using machine learning.                | 
 |  17     |  I want you to look at all of this data, and then                                  | 
 |  18     |  I want you to tell me, for these little black dots, whether they                  | 
 |  19     |  are really expensive, moderately expensive or, or inexpensive. But ,I want you    | 
 |  20     |  to do it, using something like the technique that we talked about before.         | 
 |  21     |  >> Okay?                                                                          | 
 |  22     |  >> So, let's look at this little dot, over here. Which,                           | 
 |  23     |  by the way, I want to point out. this little black                                | 
 |  24     |  dot here by the US Post Office, underneath the rightmost ,e                       | 
 |  25     |  ,over here, is not a point in our data base. But                                  | 
 |  26     |  I think by staring at this, you might be able to come up                          | 
 |  27     |  with a reasonable guess, about whether                                            | 
 |  28     |  it is moderately expensive, expensive, or inexpensive.                            | 
 |  29     |  >> Okay, yeah. I think, this is a helpful, example, because, now I see            | 
 |  30     |  that it does kind of make sense, especially, in this context, to think of         | 
 |  31     |  the geometric location, as actually being a                                       | 
 |  32     |  very useful attribute for deciding how to                                         | 
 |  33     |  label the new points. So, that black point that you've pointed out, is in the     | 
 |  34     |  part of the neighborhood, that has a green dot                                    | 
 |  35     |  in it. Like, the nearest dot to it, seems like                                    | 
 |  36     |  a pretty good guess as to what, what the value                                    | 
 |  37     |  of that house might be, so I'm going to guess green.                              | 
 |  38     |  >> Yes, and I think ,you would be right. And I like the word that you             | 
 |  39     |  used there. You talked about, its nearest neighbor,                               | 
 |  40     |  so I like that. I'm going to write that down.                                     | 
 |  41     |  Neighbor, okay. So, I'm going to look at my                                       | 
 |  42     |  nearest neighbor. Well let's see if this works,                                   | 
 |  43     |  for another point. Let's look at another point,                                   | 
 |  44     |  that's near an, e, let's see, the first e                                         | 
 |  45     |  over here. This little black point, over here. What do you think? If I,           | 
 |  46     |  if I looked at my nearest neighbor, what would I, what would I guess?             | 
 |  47     |  >> Yeah, this one seems really clear. It's, it's                                  | 
 |  48     |  surrounded by red. It's in the red part of town.                                  | 
 |  49     |  >> So, you're guessing, the output is then, purple? [LAUGH]                       | 
 |  50     |  >> No, I'm going with red.                                                        | 
 |  51     |  >> Yes, and I think that that makes perfect sense. So, this is pretty             | 
 |  52     |  cool. If I have a point that's not in my database ,but, I still,                  | 
 |  53     |  by looking at my nearest neighbour, can, sort of figure out ,ah,                  | 
 |  54     |  what the actual value should be. So, there we have solved, the problem.           | 
 |  55     |  >> Yes, seems like a pretty good role.                                            | 
 |  56     |  >> Yeah, just look at your nearest neighbour and you are                          | 
 |  57     |  done. There, so, boom. There is nothing else for you to do.                       | 
 |  58     |  >> Yeah, except that you didn't do all of the houses yet.                         | 
 |  59     |  >> Okay, well, what did I miss?                                                   | 
 |  60     |  >> The one in the middle and [CROSSTALK]                                          | 
 |  61     |  I'm wondering, if maybe you did that on purpose,                                  | 
 |  62     |  because, this one has some issues.                                                | 
 |  63     |  >> What are its issues? Besides being too, near 10th Street?                      | 
 |  64     |  >> well, yeah, apart from that it doesn't                                         | 
 |  65     |  really have any very close neighbors ,on the,                                     | 
 |  66     |  on the map. So the closest that you get, is, I don't know, maybe that red one?    | 
 |  67     |  >> Maybe.                                                                         | 
 |  68     |  >> But I would be really, I'd be very wary                                        | 
 |  69     |  of just using that as my guess, because, it's also pretty                         | 
 |  70     |  darn close to a bluepoint.                                                        | 
 |  71     |  >> Yeah.                                                                          | 
 |  72     |  >> And also not so, far from the green point.                                     | 
 |  73     |  >> That's a good point. So, this whole nearest neighbor thing                     | 
 |  74     |  doesn't quite work, in this case when you got a bunch                             | 
 |  75     |  of neighbors that are saying different things. And they are kind                  | 
 |  76     |  of close to you. So, any clever way we might around this?                         | 
 |  77     |  >> I would say, move the black dot, to,                                           | 
 |  78     |  >> No, no, no, no, we are not allowed that before.                                | 
 |  79     |  >> No? Okay, right it                                                             | 
 |  80     |  seems, it seems, like it would be helpful.                                        | 
 |  81     |  >> No, no, they are federal laws ,against interesting.                            | 
 |  82     |  >> I was going to say, yeah, so, alright So, short of                             | 
 |  83     |  that, maybe ,we just need to look at a bigger context?                            | 
 |  84     |  >> Ahh, that makes sense. So, you're saying my little nearest neighbor            | 
 |  85     |  thing, sort of worked ,but the problem was I started out with examples            | 
 |  86     |  ,that were, you know, very clearly in a neighborhood, and now I'm                 | 
 |  87     |  in a place where I'm not so sure about the neighborhood, so I                     | 
 |  88     |  should let I should look at more of my neighbors, than just the closest one.      | 



##  04 - Cost of the House Two
 |  no     |  subtitle                                                                          | 
 |  -----  |  --------------------------------------------------------------------------------  | 
 |  1      |  Okay, so, how man do you want to look at?                                         | 
 |  2      |  >> Well in this case it, you know, I feel like I could draw a, a                  | 
 |  3      |  kind of extended city block zone and capture                                      | 
 |  4      |  maybe, I don't know, five of the points.                                          | 
 |  5      |  >> Okay, let's do it. So let's find our                                           | 
 |  6      |  five, our five nearest neighbors. So let's see. This is                           | 
 |  7      |  clearly close, that's one over here. I'd                                          | 
 |  8      |  say this is close. I'll say this one is close. This one's close.                  | 
 |  9      |  None of the other blue ones are actually that close. And I'd                      | 
 |  10     |  say that's the next closest one, so here are my little five points.               | 
 |  11     |  That all seem relative near. So what does that tell you?                          | 
 |  12     |  >> Well, I mean, it's, it feels like it                                           | 
 |  13     |  suggests that red is not a bad choice here.                                       | 
 |  14     |  >> Mm                                                                             | 
 |  15     |  >> It's in a reddish part of town.                                                | 
 |  16     |  >> Yeah, I get that. So, so you think it's a                                      | 
 |  17     |  pretty, fair thing to bet that this should be red then?                           | 
 |  18     |  >> Yeah I mean I think that if you were really asking me seriously                | 
 |  19     |  I would wonder about that blue point to the right of the highway and whether      | 
 |  20     |  that had any influence.                                                           | 
 |  21     |  >> That's pretty far away.                                                        | 
 |  22     |  >> Yeah, it's not that far away.                                                  | 
 |  23     |  >> Well in Atlanta, once you cross highways                                       | 
 |  24     |  you might as well be an infinite distance away.                                   | 
 |  25     |  >> Well so, okay, but. That's a good point then.                                  | 
 |  26     |  So, I guess I was interpreting your notion of distance as                         | 
 |  27     |  being, you know, like straight line distance on the map. But                      | 
 |  28     |  maybe that doesn't make sense for this kind of neighborhood example.              | 
 |  29     |  >> Hm, no, that's a good point. So,                                               | 
 |  30     |  we've been talking about distance sort of implicitly.                             | 
 |  31     |  But this notion of distance. It's actually quite important. So maybe distance is  | 
 |  32     |  straight-line distance, maybe it's as the crow                                    | 
 |  33     |  flies. Maybe it's driving distance. Maybe it                                      | 
 |  34     |  has to take into account the fact that, when you cross highways in                | 
 |  35     |  Atlanta, you're typically moving into a completely                                | 
 |  36     |  different universe. These sorts of things matter.                                 | 
 |  37     |  >> Yeah. So I could imagine I don't know, like Google Maps distance.              | 
 |  38     |  >> Right. Or how many paths can you get there                                     | 
 |  39     |  and which is the shortest one given the traffic? There's all                      | 
 |  40     |  kinds of things like that you could do. So. So that's                             | 
 |  41     |  fair, that's fair. But that just says that this, this distant, we                 | 
 |  42     |  have to be very careful what we mean by distance and                              | 
 |  43     |  that's okay. But let's just say for the sake of this discussion                   | 
 |  44     |  that these are the closest points by some reasonable measure of                   | 
 |  45     |  distance. So, in that world, would you be happy if you had                        | 
 |  46     |  to pick a single example? a single output, a single label                         | 
 |  47     |  of red ,uh, blue or green. Would you be happy picking red?                        | 
 |  48     |  >> Yeah, I                                                                        | 
 |  49     |  mean you know, not ecstatic, but okay.                                            | 
 |  50     |  >> That's fair. So, I like this. So, we, we                                       | 
 |  51     |  went from just picking our nearest neighbor to picking our nearest                | 
 |  52     |  neighbors. And ,what's a good value you think we should,                          | 
 |  53     |  we should stick to with neighbors? We started with one and                        | 
 |  54     |  that clearly wasn't good. You picked, at least not in                             | 
 |  55     |  all cases and you came up with five. So what do                                   | 
 |  56     |  you think? What, what, if I'm going to call this algorithm something,             | 
 |  57     |  what do you think five nearest neighbors? What do you think?                      | 
 |  58     |  What should I call it?                                                            | 
 |  59     |  >> Five seems good. I mean I feel like that, that's gotta be universal.           | 
 |  60     |  >> The number five?                                                               | 
 |  61     |  >> Yeah.                                                                          | 
 |  62     |  >> Well it is in Atlanta but it might                                             | 
 |  63     |  not be univeral in wherever it is you are.                                        | 
 |  64     |  >> We'll call it the Georgia Tech nearest neighbors.                              | 
 |  65     |  >> That doesn't seem like an algorithm that's going to to be used very much.      | 
 |  66     |  >> Fair enough. All right. So what about,                                         | 
 |  67     |  we could do as many nearest neighbors as                                          | 
 |  68     |  is appropriate. Or maybe we should just make it a free parameter and call it K.   | 
 |  69     |  >> Ok, I like that. K nearest neighbors, so we'll have K                          | 
 |  70     |  nearest neighbors. And we'll pick our K numbers. Oh, and you said                 | 
 |  71     |  something fancy there, by the way. You said free parameter. I like                | 
 |  72     |  that. We should, we should come back to that again. So we                         | 
 |  73     |  have an algorithm, k nearest neighbors. Which takes K nearest neighbors as        | 
 |  74     |  a way of deciding how you're going to label some query point here.                | 
 |  75     |  And we've identified two parameters to the algorithm so far. K Which              | 
 |  76     |  is the number of neighbors we're going to use. And some notion of distance.       | 
 |  77     |  >> Oh, sure.                                                                      | 
 |  78     |  >> Which                                                                          | 
 |  79     |  here we were kind of using in the sort of obvious way,                            | 
 |  80     |  but there might be other ways we might want to use distance here.                 | 
 |  81     |  >> Yeah, like I could imagine if the houses, if,                                  | 
 |  82     |  had additional features like how many Square footages they had.                   | 
 |  83     |  >> Right, stuff like that. That would make perfect sense.                         | 
 |  84     |  So, so really distance, we're using distance here in a kind                       | 
 |  85     |  of in an over loaded sense, because this is something                             | 
 |  86     |  on a map. But really distance is a standard for similarity.                       | 
 |  87     |  >> Similarity, good. It's kind of standard                                        | 
 |  88     |  for the opposite of similarity.                                                   | 
 |  89     |  >> [LAUGH] Well distance is just a kind of similarity, right?                     | 
 |  90     |  But in case of, you know, points on the map. Similarity,                          | 
 |  91     |  it sort of makes sense because as you said when we                                | 
 |  92     |  were talking about real estate, location,                                         | 
 |  93     |  location, location matters. So, there, similarity                                 | 
 |  94     |  really is kind of the inverse of distance. But in other                           | 
 |  95     |  ways, things like the number of veterans you have, whether you're                 | 
 |  96     |  one on side of the highway or the other, the school                               | 
 |  97     |  district you're in, things like that, are other things you might add              | 
 |  98     |  as features or dimensions when you talk about similarity or distance.             | 
 |  99     |  Okay, so I like this. I think we have a general algorithm                         | 
 |  100    |  now and I think it does a pretty good job of                                      | 
 |  101    |  addressing the points you brought up. We no longer have to worry                  | 
 |  102    |  about overfitting as much, at least it seems that way to                          | 
 |  103    |  me. And we have a way of being a little bit more                                  | 
 |  104    |  robust to this, you know, not having an exact data point                          | 
 |  105    |  in the database. So ,maybe we should turn this into an algorithm.                 | 
 |  106    |  >> Yeah,                                                                          | 
 |  107    |  let's go for it.                                                                  | 
 |  108    |  >> Okay, let's do that.                                                           | 



##  05 - K NN
 |  no     |  subtitle                                                                          | 
 |  -----  |  --------------------------------------------------------------------------------  | 
 |  1      |  Okay, so what we have here, again, is pseudocode for                              | 
 |  2      |  our K-NN algorithm. And I'm sort of writing it as                                 | 
 |  3      |  like, a function. So, you're going to be given some                               | 
 |  4      |  training data D, that's the little x, y points, x                                 | 
 |  5      |  y one, x y 2, x y 3, so on                                                        | 
 |  6      |  and so fourth. You're given some kind of distance metric                          | 
 |  7      |  or similarity function. And this is important because this represents             | 
 |  8      |  the domain knowledge as I think we, we've already said.                           | 
 |  9      |  You get some number of neighbors that you care about,                             | 
 |  10     |  k, hence the k and n, which also, by the                                          | 
 |  11     |  way, represents domain knowledge. Tells you something about how many              | 
 |  12     |  neighbors you think you should have. And then are given                           | 
 |  13     |  some particular new query point and I want to output                              | 
 |  14     |  some kind of answer, some label, some value. So the                               | 
 |  15     |  K nn algorithm is remarkably simple given these things you                        | 
 |  16     |  simply find a set of nearest neighbors such that they                             | 
 |  17     |  are the K closest to your query point.                                            | 
 |  18     |  >> Okay. I'm sort of processing this. So the, the data                            | 
 |  19     |  the capital D. Are those pairs and there's a set of pairs?                        | 
 |  20     |  >> Yes.                                                                           | 
 |  21     |  >> Ok. And k smallest distances. So this NN this is a set?                        | 
 |  22     |  >> Yes.                                                                           | 
 |  23     |  >> And it's consistent for all the elements in                                    | 
 |  24     |  the data that are closest to the query point?                                     | 
 |  25     |  >> Yep. And the so the query point is a parameter of that. Okay.                  | 
 |  26     |  Yeah. Alright. I think I. Oh. And then it's, then the so it's just return.        | 
 |  27     |  >> Yeah, so we haven't figured out what                                           | 
 |  28     |  to return. So there's two separate cases we've been                               | 
 |  29     |  talking about so far. One is where, we're doing                                   | 
 |  30     |  classification, and one is where we're doing regression. So,                      | 
 |  31     |  a question for you would be, what do you                                          | 
 |  32     |  think we should when we're doing classification? Sort of,                         | 
 |  33     |  what we were doing before on the map. What                                        | 
 |  34     |  will be a way of returning a proper label?                                        | 
 |  35     |  >> So you want to                                                                 | 
 |  36     |  label, not a, like a weight on a label or something like that?                    | 
 |  37     |  >> No. I want a label. You have to                                                | 
 |  38     |  produce an answer. You have to commit to something Michael.                       | 
 |  39     |  >> Alright. Can I commit to more than one thing?                                  | 
 |  40     |  >> Nope.                                                                          | 
 |  41     |  >> Okay. So I would say that a reasonable thing to do                             | 
 |  42     |  there would be. Did we get Ys associated with the things in NN?                   | 
 |  43     |  >> Yeap.                                                                          | 
 |  44     |  >> So I would go with they should vote.                                           | 
 |  45     |  >> I like that. I think that's a good one,                                        | 
 |  46     |  so we'll simply vote and what does it mean to vote?                               | 
 |  47     |  >> It means, let's see, so feel like there would be a way to represent            | 
 |  48     |  it in terms of NN, the set. Like do you want me to write it formally?             | 
 |  49     |  >> No.                                                                            | 
 |  50     |  >> Oh, then I would just say The closest point.                                   | 
 |  51     |  Whichever yi is most frequent among the closest points wins.                      | 
 |  52     |  >> Yeah. Right. So you want to find a,                                            | 
 |  53     |  a vote of basically a vote of the yi's,                                           | 
 |  54     |  that are apart of the neighborhood set. And you take the plurality.               | 
 |  55     |  >> Plurality I see. So it's whichever one occurs the most.                        | 
 |  56     |  >> Right.                                                                         | 
 |  57     |  >> What if there's ties?                                                          | 
 |  58     |  >> It's the mode. The mode. Right.                                                | 
 |  59     |  >> Right.                                                                         | 
 |  60     |  >> Mmmm. Ala mode.                                                                | 
 |  61     |  >> What if they're ties? That's a good point. Well, if they are                   | 
 |  62     |  ties among the output, then you're just going to have to pick one.                | 
 |  63     |  >> OK.                                                                            | 
 |  64     |  >> And there's lots of ways you might do that.                                    | 
 |  65     |  You might say, well, I'll take the one. That is                                   | 
 |  66     |  say, most commonly represented in the data                                        | 
 |  67     |  period. Or I'll just randomly pick each                                           | 
 |  68     |  time, or any number of ways you might, you c an imagine doing that.               | 
 |  69     |  >> The one that's first alphabetically.                                           | 
 |  70     |  >> The one that's first lexicographically?                                        | 
 |  71     |  >> Hm.                                                                            | 
 |  72     |  >> What about in the regression case?                                             | 
 |  73     |  >> Okay. So in the regression case our y-is are numbers.                          | 
 |  74     |  >> Uh-huh. And we have the closest Yi's, so                                       | 
 |  75     |  we have a bunch of those numbers and it                                           | 
 |  76     |  seems like [LAUGH] if you have a pile of numbers and have to return               | 
 |  77     |  one, a standard thing to do would be to take the average, or the mean.            | 
 |  78     |  >> Yeah. Now let's just simply take the mean                                      | 
 |  79     |  of the Yi's, and at least there, you don't                                        | 
 |  80     |  have to worry about a tie. That's right. Though,                                  | 
 |  81     |  I guess, you know. We didn't really deal with                                     | 
 |  82     |  the question of what happens if there's more than                                 | 
 |  83     |  k small. It's, like, what if they're all exactly                                  | 
 |  84     |  the same distance? All n of them are exactly                                      | 
 |  85     |  the same distance. So which are the k closest?                                    | 
 |  86     |  >> Well, there's lots                                                             | 
 |  87     |  of things you could do there. I guess what I would suggest doing, is,             | 
 |  88     |  take the, If you have more than k that are close, that are closest                | 
 |  89     |  because you have a bunch of ties, in terms of the distance. Just take             | 
 |  90     |  all of them. Get the smallest number greater than or equal to k. Okay.            | 
 |  91     |  >> That seem reasonable?                                                          | 
 |  92     |  >> Yeah, I think that's what college rankings do.                                 | 
 |  93     |  >> Actually, that is what college rankings do, and then they, yeah,               | 
 |  94     |  that's exactly what college rankings do. So, let's do that. We know               | 
 |  95     |  that college rankings make sense. [LAUGH]. Yeah,                                  | 
 |  96     |  those are, they're scientifically proven to be,                                   | 
 |  97     |  >> Youths.                                                                        | 
 |  98     |  >> scary, scary to people in colleges.                                            | 
 |  99     |  >> That's exactly right. So, here's what we've                                    | 
 |  100    |  got, Michael. So, all we do is we take                                            | 
 |  101    |  the training data. We have some notion of                                         | 
 |  102    |  similarity or distance. We have a notion of the                                   | 
 |  103    |  number of neighbors that we care about. We                                        | 
 |  104    |  have a query point, we find the K closest                                         | 
 |  105    |  to one, you know breaking ties accordingly. And then                              | 
 |  106    |  we basically average in some way, in a way                                        | 
 |  107    |  that make sense for classification, in a way they make sense                      | 
 |  108    |  for regression and we are done. It's a very simple algorithm,                     | 
 |  109    |  but some of that's because a lot of decisions are being                           | 
 |  110    |  left up to the designer. The distance metric. The number k,                       | 
 |  111    |  how you're going to break ties. Exactly how you choose to implement               | 
 |  112    |  voting. Exactly how you choose to implement the mean or the                       | 
 |  113    |  average operation that shows how to do here. And you could                        | 
 |  114    |  put a bunch of different things here and you end up in,                           | 
 |  115    |  completely, you could end up with completely different answer. Mm.                | 
 |  116    |  >> By the way, one thing that you might do, just to give                          | 
 |  117    |  you an example of just, how much range there is here. Is rather than              | 
 |  118    |  doing a simple vote by counting, you could do a vote that is say,                 | 
 |  119    |  weighted by how far away you are. So we could have a weighted vote.               | 
 |  120    |  >> Uh-huh.                                                                        | 
 |  121    |  >> That might help us with ties.                                                  | 
 |  122    |  >> That could help with ties. Yeah.                                               | 
 |  123    |  >> You could do a weighted average. Yes, right.                                   | 
 |  124    |  So, you're basically saying that the y values that correspond to x values that    | 
 |  125    |  are closer to the query point have more of an influence on the mean.              | 
 |  126    |  >> Which makes some sense, right?                                                 | 
 |  127    |  >> No, I think it makes a lot of sense!                                           | 
 |  128    |  >> So, how would you weight that? What would you do?                              | 
 |  129    |  >> I would weight it by the similarity.                                           | 
 |  130    |  >> Right, so well in this case, the similarity is we have a distance value        | 
 |  131    |  similarity, so You would have to, you know, weight it by something like one over  | 
 |  132    |  the distance.                                                                     | 
 |  133    |  >> Oh I see. Okay. That seems like a hack.                                        | 
 |  134    |  >> Sure but it's a hack that sort of makes sense.                                 | 
 |  135    |  >> Okay.                                                                          | 
 |  136    |  >> Okay. So anyway. Simple algorithim. Lots                                       | 
 |  137    |  and lots of decisions to make here. All                                           | 
 |  138    |  of which could in principle have a pretty big effect. And so, in order to see     | 
 |  139    |  that, I want to do two quizzes that I hope get to heart of this and               | 
 |  140    |  maybe give us a little bit of insight                                             | 
 |  141    |  into how some of these decisions might matter                                     | 
 |  142    |  on the one hand, and exactly just how simple                                      | 
 |  143    |  or not simple this algorithm turns out to be. Okay?                               | 
 |  144    |  >> Awesome.                                                                       | 



##  06 - Wont You Compute My Neighbors
 |  no     |  subtitle                                                                          | 
 |  -----  |  --------------------------------------------------------------------------------  | 
 |  1      |  Okay Michael, I have two quizzes for you. Okay?                                   | 
 |  2      |  >> Yeah, yeah.                                                                    | 
 |  3      |  >> Here's the first quiz, and here's the way it's set up.                         | 
 |  4      |  I want you to fill in the empty boxes of this table. Okay?                        | 
 |  5      |  >> Ooh.                                                                           | 
 |  6      |  >> Got it.                                                                        | 
 |  7      |  >> There's a lot of empty boxes.                                                  | 
 |  8      |  >> There's a lot of empty boxes.                                                  | 
 |  9      |  >> Okay, but Okay, let me make sure I understand what's going                     | 
 |  10     |  on here. So we're looking at                                                      | 
 |  11     |  three different algorithms that are learning algorithms.                          | 
 |  12     |  >> Yep.                                                                           | 
 |  13     |  >> There's one One neural net                                                     | 
 |  14     |  >> No                                                                             | 
 |  15     |  >> Okay, one nearest neighbor.                                                    | 
 |  16     |  >> Mm-hm                                                                          | 
 |  17     |  >> K nearest neighbor and linear regression.                                      | 
 |  18     |  >> Yep                                                                            | 
 |  19     |  >> And for each one you want to know running time and space.                      | 
 |  20     |  >> Mm-hm.                                                                         | 
 |  21     |  >> And this is on n points I assume, yeah, n                                      | 
 |  22     |  sort, what does it mean for data points to be sorted?                             | 
 |  23     |  >> So let's assume we're living in a world where all                              | 
 |  24     |  of our data points are you know in r one. Okay.                                   | 
 |  25     |  >> Oh okay that well that. That could be sorted.                                  | 
 |  26     |  >> That could be. Yeah that could be                                              | 
 |  27     |  sorted. And that you know where going to be                                       | 
 |  28     |  out putting some real numbers as well. So it points on a. On a number of lines.   | 
 |  29     |  So to make things simple for you. I'm going to                                    | 
 |  30     |  say that the points that your given are already sorted.                           | 
 |  31     |  >> Oh ok alright. And yeah that makes sense. Its just                             | 
 |  32     |  a scaler. So then a query point is going to come in.                              | 
 |  33     |  And then its going to be some value. And were going to have                       | 
 |  34     |  to find the nearest neighbor or do the [UNKNOWN] regression or whatever.          | 
 |  35     |  >> Right.                                                                         | 
 |  36     |  >> Alright now that's for running time. For                                       | 
 |  37     |  now space your talking about the space of what.                                   | 
 |  38     |  >> How much space you are going to have                                           | 
 |  39     |  to do in order to accomplish your task. How much space                            | 
 |  40     |  you going to have to use in order to accomplish your task?                        | 
 |  41     |  >> So this is kind of like the the. The                                           | 
 |  42     |  space that's representing the class enviro. Or the regression. After training.    | 
 |  43     |  >> Yes. So actually that question                                                 | 
 |  44     |  about after training is important. You'll notice                                  | 
 |  45     |  I've divided each of these algorithms                                             | 
 |  46     |  into two phases. There's the learning phase.                                      | 
 |  47     |  How much time it takes to learn. How much space you need to                       | 
 |  48     |  learn. Then there's the query phase. When I give you some new value and           | 
 |  49     |  you have to output and answer. What's the running time for that                   | 
 |  50     |  and what are the space requirements for that? Okay? You got that?                 | 
 |  51     |  >> Yeah                                                                           | 
 |  52     |  >> I want that for each one. Of these three algorithms.                           | 
 |  53     |  >> Except for one nearest neighbor which the, it appears                          | 
 |  54     |  as though you filled in for me to get me started.                                 | 
 |  55     |  >> Right so just to get you started and make it easier for you know               | 
 |  56     |  to know what I'm talking about. I'm talking about big o times here. Right. I'm    | 
 |  57     |  not going to make you write out big o. Big o is implicit. So if we                | 
 |  58     |  look at one nearest neighbor, and we                                              | 
 |  59     |  ask well what's the running time of learning?                                     | 
 |  60     |  Well, it's constant. Right? Because there's no learning.                          | 
 |  61     |  >> I see. You just take that sorted set of data                                   | 
 |  62     |  points and you just pass it along through the query here.                         | 
 |  63     |  >> Right. Now, you could say that" Well, I'm going to                             | 
 |  64     |  take the data points or I'm going to copy them into this                          | 
 |  65     |  database," and so it's linear. But let's assume they already come in              | 
 |  66     |  a data base, or some data structure that you can use, okay?                       | 
 |  67     |  >> Gotcha.                                                                        | 
 |  68     |  >> Okay, so now that actually brings us                                           | 
 |  69     |  to a nice little question about how much space,                                   | 
 |  70     |  learning takes here. And, well because you have to store those points,            | 
 |  71     |  and keep them around. The space requirements are big O of N.                      | 
 |  72     |  >> Yeah, that makes sense.                                                        | 
 |  73     |  >> Okay, good. So given that as an example. Do                                    | 
 |  74     |  you think your one example in your data base. Mm, do                              | 
 |  75     |  you think you can use that to build up labels                                     | 
 |  76     |  for all the rest of the phases of the different algorithms?                       | 
 |  77     |  >> Yeah, I think so.                                                              | 
 |  78     |  >> Okay, cool. Go for it.                                                         | 



##  07 - Wont You Compute My Neighbors
 |  no     |  subtitle                                                                          | 
 |  -----  |  --------------------------------------------------------------------------------  | 
 |  1      |  Okay Michael, are you ready?                                                      | 
 |  2      |  >> I am afraid so.                                                                | 
 |  3      |  >> All right, which one do you want to fill out first?                            | 
 |  4      |  >> Let's just do them in order, so ,one nearest neighbor. You, you explained,     | 
 |  5      |  how the training works. We just take the assorted list, and leave it there.       | 
 |  6      |  >> Mm-hm.                                                                         | 
 |  7      |  >> And we have the classifier, or the aggressor itself ,has linear space,         | 
 |  8      |  and now at query time, we need to find the nearest neighbor, Um-huh.              | 
 |  9      |  >> Which we could do by taking the query                                          | 
 |  10     |  point, and running through the whole list ,and seeing which                       | 
 |  11     |  one it's closest to, but, because, it's sorted I think                            | 
 |  12     |  we, we outta be able to use binary search and,                                    | 
 |  13     |  and in log time, find the closest, point to the query.                            | 
 |  14     |  >> That's exactly right, you should be able to do                                 | 
 |  15     |  that in log base, two time. What if it weren't sorted?                            | 
 |  16     |  >> Yeah then, like I said, I think you could just scan through the whole          | 
 |  17     |  list and that would be linear time and that's not a big deal.                     | 
 |  18     |  >> Right, yeah, we could do linear time, but, because I gave you a                | 
 |  19     |  sorted list, because, I'm so helpful, you                                         | 
 |  20     |  can do it in [INAUDIBLE] time, okay, but.                                         | 
 |  21     |  >> That was, that was very, very thoughtful of you.                               | 
 |  22     |  >> It was I thought, I thought of her, so what about on the, space side?          | 
 |  23     |  >> Alright, so the amount of space that you need to process its query is          | 
 |  24     |  linear. We don't need to take any special,                                        | 
 |  25     |  set aside, space beyond, a couple simple variables.                               | 
 |  26     |  And the data that we're given, which we've already accounted for.                 | 
 |  27     |  >> Right, so then why would it be linear, if we accounted for it?                 | 
 |  28     |  >> Did I say linear? I meant constant.                                            | 
 |  29     |  >> Yes, yes, that's right,                                                        | 
 |  30     |  constant. That's what you meant. That's what you said. That's what happened.      | 
 |  31     |  >> [LAUGH]                                                                        | 
 |  32     |  >> Okay.                                                                          | 
 |  33     |  >> It's a good thing, this wasn't being recorded,                                 | 
 |  34     |  so we could verify one way or the other.                                          | 
 |  35     |  >> [LAUGH] It is a good thing, maybe we'll                                        | 
 |  36     |  look it up on Wikipedia, and it'll say confusingly [LAUGH]                        | 
 |  37     |  >> Linear sometimes use to mean constant.                                         | 
 |  38     |  >> Constant. [LAUGH]. Yeah, that is pretty confusing.                             | 
 |  39     |  >> Okay, what about k and n?                                                      | 
 |  40     |  >> Alright, K and n. So k and n, so the training process,                         | 
 |  41     |  the learning process, is exactly the same, as it is for one year stamper,         | 
 |  42     |  which is to say you do nothing and you pass all the data                          | 
 |  43     |  forward, to the, The query processor. So it's going to be 1 n.                    | 
 |  44     |  >> That is correct, nice.                                                         | 
 |  45     |  >> Now querying, seems like its a little more subtle. So                          | 
 |  46     |  we can find the single nearest neighbor in log and time.                          | 
 |  47     |  >> Mm-mm.                                                                         | 
 |  48     |  >> Where we going to get the other K minus one? So, I'm pretty sure,              | 
 |  49     |  that ,once we find the nearest neighbor we can kind of start doing a little,      | 
 |  50     |  Spread out search, from there, until we found the k nearest neighbors.            | 
 |  51     |  >> Sure. So, you're saying, you know,                                             | 
 |  52     |  you've got these points. They're already in a                                     | 
 |  53     |  line, you find the nearest neighbor. You                                          | 
 |  54     |  know ,the, the next nearest neighbors have to                                     | 
 |  55     |  be within k of the points surrounding it, and so you can just move in             | 
 |  56     |  kind of, either direction and pick them up as you go. Yeah, something like that.  | 
 |  57     |  >> Okay.                                                                          | 
 |  58     |  >> I mean the way that, the way that I                                            | 
 |  59     |  was thinking about it is that, I, I think you                                     | 
 |  60     |  can use the same algorithm that you used for merging lists, in merge sort,        | 
 |  61     |  but here the lists actually corresponds, to being, to the left of the query       | 
 |  62     |  point, and being to the right of the query point and they are both                | 
 |  63     |  sorted ,in terms of their distance from the query point. Sure, yeah, I buy that.  | 
 |  64     |  >> So, so that ought to give us log n, plus k.                                    | 
 |  65     |  >> Okay, so, do we need to write the k?                                           | 
 |  66     |  >> I'm going to say yes, because, if k is                                         | 
 |  67     |  on the order of like, n over 2, then it's going to dominate. If k is on           | 
 |  68     |  the order of log n, then it's not                                                 | 
 |  69     |  going to dominate. Mm, that's a good point. So,                                   | 
 |  70     |  yeah, we'll do k. I will point out that if k is on the order of                   | 
 |  71     |  n over 2, you're right, it will dominate, and then really this is big o of n.     | 
 |  72     |  >> That's right.                                                                  | 
 |  73     |  >> But if it's on the order of log n, then it's                                   | 
 |  74     |  just log n plus n, and so it's a big old long                                     | 
 |  75     |  n, log n. But ,you're right, so we should probably keep the                       | 
 |  76     |  k around because, we don't know its relationship to n. Okay, fair enough.         | 
 |  77     |  Okay, what about the space requirements?                                          | 
 |  78     |  >> We know one bit of relationship, it's smaller than or equal to it.             | 
 |  79     |  >> That's true.                                                                   | 
 |  80     |  >> Because that would be really weird, if I gave you                              | 
 |  81     |  ten data points and asked you for the 20 nearest neighbors.                       | 
 |  82     |  >> That's the sort of thing you would do.                                         | 
 |  83     |  >> It's the sort of thing you would                                               | 
 |  84     |  do, but then ,it would be really confusing.                                       | 
 |  85     |  >> No, no, no, it's the sort of                                                   | 
 |  86     |  thing you would do, again, let's go to Wikipedia.                                 | 
 |  87     |  >> Confusingly, Twinny is sometimes [CROSSTALK]. [LAUGH]                          | 
 |  88     |  >> Okay. So what about space?                                                     | 
 |  89     |  >> Space, so, I don't understand why,                                             | 
 |  90     |  it would ever need more than constant space.                                      | 
 |  91     |  So, so we're going to, zip around in that. I mean, I guess, if                    | 
 |  92     |  do it really badly ,we can use K space. To kind of copy over                      | 
 |  93     |  what those, possible nearest neighbors are. But ,we don't need to keep track      | 
 |  94     |  of them. We can just point to them in place, so it's constant.                    | 
 |  95     |  >> Okay,                                                                          | 
 |  96     |  yea that's true in fact, because, it's sorted all you really need                 | 
 |  97     |  to know is the beginning and the ending. So, that's two things                    | 
 |  98     |  that's constant. Okay, cool, alright, good,                                       | 
 |  99     |  so what about linear regression? Your                                             | 
 |  100    |  favorite little algorithm thing that you did? When we talked about this before.   | 
 |  101    |  >> I do like, linear regression. The learning in                                  | 
 |  102    |  this case, is what we are mapping, real number                                    | 
 |  103    |  input to a real number output. The way we                                         | 
 |  104    |  are doing that is we are taking, its probably                                     | 
 |  105    |  M X plus B sort of form [CROSSTALK]. We                                           | 
 |  106    |  need to find, the multiplier and the additive constant. which,                    | 
 |  107    |  It seems, like, in general doing a regression involves,                           | 
 |  108    |  inverting a matrix. But, in this case,I think the matrix                          | 
 |  109    |  that we're talking about is of constant size. So                                  | 
 |  110    |  inverting, is, constant time. I think, it's as easy ,as                           | 
 |  111    |  basically just scanning through the list ,to populate that,                       | 
 |  112    |  that ,constant size matrix. So, I'm going to say order n.                         | 
 |  113    |  >> Yep.                                                                           | 
 |  114    |  >> To process the data.                                                           | 
 |  115    |  >> That is correct.                                                               | 
 |  116    |  >> There's probably a really nice algorithm for that.                             | 
 |  117    |  >> Yeah, probably some kind of linear regression algorithm.                       | 
 |  118    |  >> Yeah. [LAUGH] No, I mean like the general                                      | 
 |  119    |  linear regression algorithm is, is involves inverting a matrix.                   | 
 |  120    |  >> Right.                                                                         | 
 |  121    |  >> Or something like it, something equivalent to it. But here                     | 
 |  122    |  because, we're, it's all in scaler land, I think it's simpler.                    | 
 |  123    |  >> Yeah, I think that's right. Okay ,so what about space?                         | 
 |  124    |  >> All right, so space interpreted                                                | 
 |  125    |  the data that you passed forward from                                             | 
 |  126    |  the learning algorithm, to the regressor, is just,                                | 
 |  127    |  well MX plus B. It's just M and B, which is constant. There's the two numbers.    | 
 |  128    |  >> Right, that's 2, 2 is like 1,                                                  | 
 |  129    |  [UNKNOWN] large values [LAUGH] of 1, so it's constant.                            | 
 |  130    |  >> Yeah, All right, now at query time, you give me an X.                          | 
 |  131    |  I multiply, it by M and add B, so that's constant time [CROSSTALK]. So,           | 
 |  132    |  before the query, cost was expensive and the learning                             | 
 |  133    |  cost was cheap. And now we've kind of swapped that around.                        | 
 |  134    |  >> Yeah, we have, so space would be.                                              | 
 |  135    |  >> Space, oh, that you're asking me?                                              | 
 |  136    |  >> Yeah.                                                                          | 
 |  137    |  >> Space for the query would be [INAUDIBLE] as well.                              | 
 |  138    |  >> Right, exactly, so yeah, so you made                                           | 
 |  139    |  a good point here. So earlier on, we had                                          | 
 |  140    |  the situation where learning was fast, was constant, and                          | 
 |  141    |  querying was, you know, not as fast. It was,                                      | 
 |  142    |  you know, probably logarithmic. But, in the regression case,                      | 
 |  143    |  learning was expensive and the querying was easy, so                              | 
 |  144    |  we swapped around, that's exactly right. So, why would                            | 
 |  145    |  you care about that, well, let's see, I'll point                                  | 
 |  146    |  out something, which is though, even though we swapped                            | 
 |  147    |  out what was expensive in terms of time and                                       | 
 |  148    |  what wasn't, you'll notice that. It's only logarithmic at                         | 
 |  149    |  query time for these first two but it's linear for                                | 
 |  150    |  the learning time, in, linear regression, so doesn't that                         | 
 |  151    |  mean that linear regression is always slower and worse?                           | 
 |  152    |  >> No really, because we only have to                                             | 
 |  153    |  learn once, but we can query many, many times.                                    | 
 |  154    |  >> Right, right. So I guess if we query more than, you know,                      | 
 |  155    |  n times for example ,it'll certainly be,                                          | 
 |  156    |  worse overall. In terms of running time.                                          | 
 |  157    |  >> That's right.                                                                  | 
 |  158    |  >> Okay.                                                                          | 
 |  159    |  >> Though, it's, though it's interesting, because like when I see numbers         | 
 |  160    |  like this, my, my algorithm, hat tells me that                                    | 
 |  161    |  I should try to balance them a little bit more.                                   | 
 |  162    |  Like, here it's, it's you can make, learning ,essentially                         | 
 |  163    |  free and the other one you can make querying essentially                          | 
 |  164    |  free. Really you want to split those, somewhat evenly. Though                     | 
 |  165    |  it's, not obvious to me how you would do that.                                    | 
 |  166    |  Like, square root of n, learning time and then                                    | 
 |  167    |  square root of n query time or something like that.                               | 
 |  168    |  >> Yeah, but you did say something else that was                                  | 
 |  169    |  important right? Which is that you only have to learn once.                       | 
 |  170    |  >> Yeah, It's true.                                                               | 
 |  171    |  >> So, the balance you know, really depends                                       | 
 |  172    |  on how often you're going to do querying and                                      | 
 |  173    |  exactly, what power it gives you. I mean,                                         | 
 |  174    |  the trade off is really there. Don't you think?                                   | 
 |  175    |  >> Yeah, I guess so. I mean so, so specifically,                                  | 
 |  176    |  in the, in the version where you just query ones.                                 | 
 |  177    |  >> Right.                                                                         | 
 |  178    |  >> Then the balance thing could be more interesting.                              | 
 |  179    |  >> Sure, okay, cool. All right anything else                                      | 
 |  180    |  you want to observe about this. Let's see,                                        | 
 |  181    |  we got the trade off between learning versus                                      | 
 |  182    |  querying. So, either you do all your work upfront,                                | 
 |  183    |  or, you put it ,off ,and do your work only, when you're forced to at query time.  | 
 |  184    |  >> Yeah, I guess, well one thing, is, I want to point out that there's            | 
 |  185    |  a nice Mr. Rodgers, reference in the title. That was, that was very cool.         | 
 |  186    |  >> Thank you very much. And the second thing, is                                  | 
 |  187    |  that it does strike me, in a sense, that what's going                             | 
 |  188    |  on here for the nearest neighbor algorithms, is that you                          | 
 |  189    |  just put off ,doing any work until you absolutely have to.                        | 
 |  190    |  >> Mm-hm.                                                                         | 
 |  191    |  >> Which strikes me as kind of a procrastinatory approach.                        | 
 |  192    |  >> So that's a good word, that you used there, procrastinate.                     | 
 |  193    |  The words that people use, in the literature, are ,uh, lazy.                      | 
 |  194    |  >> Mm.                                                                            | 
 |  195    |  >> They say that these are lazy learners, versus                                  | 
 |  196    |  something like linear regression, which is an eager learner.                      | 
 |  197    |  >> Eager.                                                                         | 
 |  198    |  >> Yes. So, linear regression, is eager, it wants to learn right away, and it     | 
 |  199    |  does, but nearest neighbor algorithms are lazy. They                              | 
 |  200    |  want to put off, learning until they absolutely ,have                             | 
 |  201    |  to, and so we refer to this class ,as lazy and this class as eager.               | 
 |  202    |  >> I See, so I guess its the case, that, if                                       | 
 |  203    |  we never query it, then the lazy learner definitely comes out ahead.              | 
 |  204    |  >> Right, that makes sense.                                                       | 
 |  205    |  >> Yeah.                                                                          | 
 |  206    |  >> It's just in time learning, or JIL. [LAUGH]                                    | 
 |  207    |  Or JITL, I guess, which doesn't roll off the tongue                               | 
 |  208    |  anywhere near as well. Okay, cool. So we've gotten                                | 
 |  209    |  through this quiz. Would you like to do another one?                              | 
 |  210    |  >> Yeah, I just have to get this JITL off my tongue.                              | 
 |  211    |  >> [LAUGH]                                                                        | 



##  08 - Domain K NNowledge
 |  no     |  subtitle                                                                          | 
 |  -----  |  --------------------------------------------------------------------------------  | 
 |  1      |  Okay Michael, so here's our second ,quiz, is                                      | 
 |  2      |  a row. In the last quiz, we talked about                                          | 
 |  3      |  running time and space time, but now we're going to                               | 
 |  4      |  talk about ,how the k-nn algorithm, actually works. And                           | 
 |  5      |  in particular how different choices, between distance metrics, values             | 
 |  6      |  of k, and how you're going to put them together,                                  | 
 |  7      |  can give you different answers, okay? So, what I                                  | 
 |  8      |  have over here on the left is training data.                                      | 
 |  9      |  This is a regression problem and you're training                                  | 
 |  10     |  data is made up of xy pairs. X is                                                 | 
 |  11     |  two dimensional. Okay? So this is a function                                      | 
 |  12     |  from R squared to some value in R1. Okay?                                         | 
 |  13     |  >> Mm-hm.                                                                         | 
 |  14     |  >> So, the first dimension represents, something                                  | 
 |  15     |  and the second dimension, represents something. And then                          | 
 |  16     |  there's some particular, output over here. And what I want you to do, is given a  | 
 |  17     |  query point, 4, 2 produce what the proper y or output                             | 
 |  18     |  ought to be, given all of this training did. You're with me?                      | 
 |  19     |  >> Yeah.                                                                          | 
 |  20     |  >> Okay, so I want you to do it in four different cases, I                        | 
 |  21     |  want you to do it in the case where, your distance matrix is euclidean, Okay.     | 
 |  22     |  >> The distance metric, in R2?                                                    | 
 |  23     |  >> Yes.                                                                           | 
 |  24     |  >> Oh I see because, we're going to measure the distance                          | 
 |  25     |  between the query and the different data points.                                  | 
 |  26     |  >> Right.                                                                         | 
 |  27     |  >> Yeah. Okay. Uh-huh.                                                            | 
 |  28     |  >> Mm-hm. So it's euclidean, for a case of one                                    | 
 |  29     |  nearest neighbor and three nearest neighbor and I want you                        | 
 |  30     |  to take, for example, in the three nearest neighbor case.                         | 
 |  31     |  I want you take their output and average them. Okay?                              | 
 |  32     |  >> Okay.                                                                          | 
 |  33     |  >> Now, in the I also want you to do the same thing. But in the case              | 
 |  34     |  where instead of using Euclidean distance, we use Manhattan                       | 
 |  35     |  distance. But again, for both 1 nearest neighbor and                              | 
 |  36     |  3 nearest neighbor And in any case where                                          | 
 |  37     |  we have ties, like in three nearest neighbor where                                | 
 |  38     |  we absolutely have to have at least three of                                      | 
 |  39     |  these things show up, just let 'em average. Okay?                                 | 
 |  40     |  >> Got you.                                                                       | 
 |  41     |  >> Now we're doing averaging instead of                                           | 
 |  42     |  straight voting, because, this is a regression problem.                           | 
 |  43     |  >> Got it.                                                                        | 
 |  44     |  >> Okay. Any questions?                                                           | 
 |  45     |  >> Maybe. Let's see. Three nearest neighbor. And so if there's ties, we, we       | 
 |  46     |  use the college ranking trick of including                                        | 
 |  47     |  everybody who's at least as good as the                                           | 
 |  48     |  k, largest or k closest.                                                          | 
 |  49     |  >> Yes, exactly.                                                                  | 
 |  50     |  >> Okay, yeah, no I think, I think I can take a stab at this.                     | 
 |  51     |  >> Okay, cool then go.                                                            | 



##  09 - Domain K NNowledge
 |  no     |  subtitle                                                                          | 
 |  -----  |  --------------------------------------------------------------------------------  | 
 |  1      |  Alright Michael, you ready?                                                       | 
 |  2      |  >> Yeah.                                                                          | 
 |  3      |  >> Okay. What's the answer? Walk me through.                                      | 
 |  4      |  >> I will walk you through. Alright. So                                           | 
 |  5      |  let's, let's do this. Let's write the Euclidean distance.                         | 
 |  6      |  Well let's write the Manhattan distance, because I don't,                         | 
 |  7      |  I don't want to take square root to my head.                                      | 
 |  8      |  >> Okay.                                                                          | 
 |  9      |  >> Let's write the Manhattan distances next to the Xs.                            | 
 |  10     |  >> OKay.                                                                          | 
 |  11     |  >> Or the Ys.                                                                     | 
 |  12     |  >> Alright.                                                                       | 
 |  13     |  >> Either way.                                                                    | 
 |  14     |  >> Let's do it next to the Xs. So this is                                         | 
 |  15     |  the Manhattan distance or MD as the cool kids call it.                            | 
 |  16     |  >> [LAUGH]                                                                        | 
 |  17     |  >> Is that true?                                                                  | 
 |  18     |  >> Yea.                                                                           | 
 |  19     |  >> The cool kids called it L one.                                                 | 
 |  20     |  >> No, no, no have you ever heard a cool kid ever say something like L one?       | 
 |  21     |  >> Well, to me the cool kids are the people                                       | 
 |  22     |  at neps who know more math than I do. Yea, do                                     | 
 |  23     |  you think any of them are going to watch this video?                              | 
 |  24     |  Actually I'm afraid all of them are going to watch this video.                    | 
 |  25     |  >> Now I'm really afraid.                                                         | 
 |  26     |  >> Mm-Hm so you better get it right, every ones watching.                         | 
 |  27     |  >> All right, well let me do, let me complete the Manhattan distances.            | 
 |  28     |  So the first one what you do is you take the 1 minus 4.                           | 
 |  29     |  >> Mm-Hm.                                                                         | 
 |  30     |  >> And that's three. And you take the 6 minus 2 and that's 4. And you add the     | 
 |  31     |  two together and you get 7. Which interestingly is                                | 
 |  32     |  the same as y, but I think that's a coincidence.                                  | 
 |  33     |  >> Okay. [CROSSTALK]                                                              | 
 |  34     |  >> And now I'll do all the rest of them                                           | 
 |  35     |  'cause I pre-computed them of Four, six, eight, four, six. Alright,               | 
 |  36     |  so now we've got ti set up so we can do                                           | 
 |  37     |  one and three nearest neighbor relatively quickly. So, the one nearest            | 
 |  38     |  neighbor, the closest distance, is four.                                          | 
 |  39     |  >> Mm--hm.                                                                        | 
 |  40     |  >> But unfortauntely there are two points                                         | 
 |  41     |  that have that two comma four in set                                              | 
 |  42     |  number one. We have outputs of eight and                                          | 
 |  43     |  50 because they. Almost agree with each other.                                    | 
 |  44     |  >> Uh-huh.                                                                        | 
 |  45     |  >> Not. And if we take the average of those two things we get 29.                 | 
 |  46     |  >> Yep. That is correct Michael.                                                  | 
 |  47     |  >> Great now in terms of the three nearest neighbors we have the fours and        | 
 |  48     |  the sixes.                                                                        | 
 |  49     |  >> So the four, three nearest neighbors.                                          | 
 |  50     |  >> Yep.                                                                           | 
 |  51     |  >> Somewhat awkwardly. And the we have the average of those things which is       | 
 |  52     |  what. Eight, fifty and sixteen and sixty                                          | 
 |  53     |  eight which gets us thirty five point five.                                       | 
 |  54     |  >> Right. Obviously. [LAUGH] Okay. Alright,                                       | 
 |  55     |  so that was pretty straightforward. And those                                     | 
 |  56     |  answers aren't too far off from one another. So what about the Euclidean case?    | 
 |  57     |  >> Alright,                                                                       | 
 |  58     |  so one thing to point out. I, I was worried                                       | 
 |  59     |  about computing square roots but it occurs to me that                             | 
 |  60     |  I actually don't have to compute square roots because that's                      | 
 |  61     |  the monotonic transformation, and we only care about the orders.                  | 
 |  62     |  >> Hm, okay.                                                                      | 
 |  63     |  >> So for Euclidean distance, or as I like to call him casually, ED,              | 
 |  64     |  >> Mmhm.                                                                          | 
 |  65     |  >> We can just take the square differences summed up.                             | 
 |  66     |  >> Okay, so this would be ED squared.                                             | 
 |  67     |  >> Yes, it would be ED squared.                                                   | 
 |  68     |  >> Okay, ED.                                                                      | 
 |  69     |  >> Good.                                                                          | 
 |  70     |  So the first one, it'll be the one minus four is three, squared is nine. And the  | 
 |  71     |  6 minus 2 is 4, squared is 16. And 9 plus 16 is 25. So the first one will be 25.  | 
 |  72     |  >> And notice the square of 25 is pretty easy to compute.                         | 
 |  73     |  >> Yeah, but the other ones aren't going to be. It just                           | 
 |  74     |  so happens that we've got a pythagorean triple on our hands.                      | 
 |  75     |  >> Mm. I love those.                                                              | 
 |  76     |  >> Al right so the remaining ones, the x squared are eight,                       | 
 |  77     |  26, 40, ten, and 20.                                                              | 
 |  78     |  >> Hm, none of                                                                    | 
 |  79     |  those are easily square rootable.                                                 | 
 |  80     |  >> Exactly, though 40 feels like it really was trying and failed.                 | 
 |  81     |  >> Yeah. An eight over shot and now it's                                          | 
 |  82     |  a perfect cube. So, eight is the smallest distance.                               | 
 |  83     |  >> Yep.                                                                           | 
 |  84     |  >> And again, seemingly, coincidentally, they                                     | 
 |  85     |  Y value associated with that, is eight.                                           | 
 |  86     |  >> Hm.                                                                            | 
 |  87     |  >> So an eight, eight is our answer.                                              | 
 |  88     |  >> Good and that's correct.                                                       | 
 |  89     |  >> And the three closest are eight, ten and 20.                                   | 
 |  90     |  >> Mm-hmm.                                                                        | 
 |  91     |  >> And if we                                                                      | 
 |  92     |  average the Y values for those that's eight, 50 and 68, which gives us            | 
 |  93     |  an average of 42. The meaning of life, the universe. And pretty much everything?  | 
 |  94     |  >> Yes! And that is absolutely correct. So that's kind of That's kind             | 
 |  95     |  of cool that you get completely different answers depending upon what you do.     | 
 |  96     |  >> Yeah, it does seem very different, doesn't it?                                 | 
 |  97     |  I mean there's like several orders of magnitude spread here.                      | 
 |  98     |  >> Well, that's.                                                                  | 
 |  99     |  >> Maybe not orders of magnitude but orders of doubling.                          | 
 |  100    |  >> Yes, there are orders of doubling spread. Well, you know what                  | 
 |  101    |  Michael, I actually had a specific function in mind when I did this.              | 
 |  102    |  >> Okay! Let's find out which one is the right one!                               | 
 |  103    |  >> Well, the function I had was Y was equal to the                                | 
 |  104    |  first dimension squared plus the second dimension. So, let's call that X1         | 
 |  105    |  and X2, and this was actually the function that I had in                          | 
 |  106    |  place. So, you square the first term and you add the second.                      | 
 |  107    |  >> Okay, and                                                                      | 
 |  108    |  so like looking at the second last one, for example, seven                        | 
 |  109    |  squared is 49 plus one is 50 Oh, [UNKNOWN]. It's very consistent.                 | 
 |  110    |  >> Thank you. So what would be the actual answer for four comma two?              | 
 |  111    |  >> Okay so four squared is 16 plus two is 18. Which is close to none of them.     | 
 |  112    |  >> Right. So there's a lesson here, there's several lessons                       | 
 |  113    |  here. And one lesson I don't want you to take away.                               | 
 |  114    |  So here's the lesson. So I actually had a                                         | 
 |  115    |  real function here. There was no noise. It was fairly                             | 
 |  116    |  well represented. The proper answer was 18 and basically none                     | 
 |  117    |  of these are right. But the first thing I want                                    | 
 |  118    |  you to notice is you get completely different answers, depending                  | 
 |  119    |  upon exactly whether you do one versus three, whether you                         | 
 |  120    |  do Euclidean versus Manhattan. And that's because these things make               | 
 |  121    |  assumptions about your domain that might not be particularly relevant.            | 
 |  122    |  And this sort of suggests, that maybe this thing                                  | 
 |  123    |  doesn't do very well. Uh,Cannon doesn't do very well because                      | 
 |  124    |  none of these are close to 18. That seems                                         | 
 |  125    |  a little sad. But I've good new for you Michael.                                  | 
 |  126    |  >> Okay.                                                                          | 
 |  127    |  >> The good news is that, actually cannon tends to                                | 
 |  128    |  work really, really well. Especially given it's simplicity, it just               | 
 |  129    |  doesn't in this particular case. And there's really a reason                      | 
 |  130    |  for that, and it has to do with this sort of.                                     | 
 |  131    |  Fundamental assumptions in bias of K and N, I happen to pick an example that      | 
 |  132    |  sort of violates some of that bias. So I think it's worth to take a moment        | 
 |  133    |  to think about what the preference bias is for K and N and to see                 | 
 |  134    |  if that can lead us to understanding why                                          | 
 |  135    |  we didn't get anything close to 18 here.                                          | 
 |  136    |  >> Okay that sounds useful.                                                       | 
 |  137    |  >> Okay, so let's do that.                                                        | 



##  10 - K NN Bias
 |  no     |  subtitle                                                                          | 
 |  -----  |  --------------------------------------------------------------------------------  | 
 |  1      |  Ok, Michael, so I'm going to talk a little bit                                    | 
 |  2      |  about bias. In particular, the preference bias for K                              | 
 |  3      |  [INAUDIBLE]. So, let me remind you what preference bias                           | 
 |  4      |  is. Preference bias is kind of our notion of                                      | 
 |  5      |  why we would prefer one hypothesis over another. And                              | 
 |  6      |  they say all things, other things being equal. And                                | 
 |  7      |  what that really means is, it's the thing that                                    | 
 |  8      |  encompasses our belief. About what makes a good hypothesis.                       | 
 |  9      |  So in some of the previous examples that                                          | 
 |  10     |  we used it was things like shorter trees,                                         | 
 |  11     |  smoother functions, simpler functions, [UNKNOWN] those sorts of                   | 
 |  12     |  things were the ways that we expressed our preferences                            | 
 |  13     |  over various hypothesis. And cannon is no exception.                              | 
 |  14     |  It also has preference by its built in                                            | 
 |  15     |  as does every algorithm of any note. So I just wanted to go through three that I  | 
 |  16     |  thought of is as being indicitive of this bias. And they're,                      | 
 |  17     |  kind of all related to one another. So the first one                              | 
 |  18     |  is a notion of locality. Right? There's this idea that near                       | 
 |  19     |  points are similiar to one another. Does that make sense to you?                  | 
 |  20     |  >> Yeah. Yeah. That was really important. It came out                             | 
 |  21     |  nicely in the the real estate example. Right. So the                              | 
 |  22     |  whole idea. The whole thing we are using to generalize                            | 
 |  23     |  from one thing to another is this notion of nearness.                             | 
 |  24     |  >> Right. And exactly                                                             | 
 |  25     |  how this notion of nearness works out.                                            | 
 |  26     |  Is embedded in whatever distance function we happen                               | 
 |  27     |  to be given. And so, there's further                                              | 
 |  28     |  bias that might come out, based upon exactly                                      | 
 |  29     |  the way we implement distances. So, in                                            | 
 |  30     |  the example we just did, euclidian distance is                                    | 
 |  31     |  making a different assumption about what nearness or                              | 
 |  32     |  similarity is, compared to Manhattan distance, for example.                       | 
 |  33     |  >> So is there like, a perfect distance function for a given problem?             | 
 |  34     |  >> There's certainly a perfect distance function for any particular problem.      | 
 |  35     |  >> Yeah, that's what I mean. Not one that works for the                           | 
 |  36     |  universe, but one, like, you know, if I give you a problem and                    | 
 |  37     |  you can work on it all day long. Can you find, is                                 | 
 |  38     |  there a notion that there''s a                                                    | 
 |  39     |  distance function that would capture things perfectly?                            | 
 |  40     |  >> Well, it has to be the case for any given fixed problem. That there            | 
 |  41     |  is some distance function that minimizes, say,                                    | 
 |  42     |  some of squared errors or something like that.                                    | 
 |  43     |  First is some other distance function. Right?                                     | 
 |  44     |  >> Okay.                                                                          | 
 |  45     |  >> That has to be the case. So there, there always to                             | 
 |  46     |  be at least one best distance function given everything else is fixed.            | 
 |  47     |  >> That makes sense.                                                              | 
 |  48     |  >> Right. Now, what that is, who                                                  | 
 |  49     |  knows. Maybe you finding it might be. Arbitrarily                                 | 
 |  50     |  difficult. Because there's at least an infinite, there's                          | 
 |  51     |  at least an infinite number of distance [UNKNOWN]                                 | 
 |  52     |  >> Well yeah, I was thinking that, that for latter to find distance functions     | 
 |  53     |  to be anything we want. What about a distance function that said                  | 
 |  54     |  the distance between all the things that have the same answer, is zero.           | 
 |  55     |  >> Mm-hm.                                                                         | 
 |  56     |  >> And the distance between them and the ones that                                | 
 |  57     |  have different answers is you know, infinity or something big.                    | 
 |  58     |  >> Yeah.                                                                          | 
 |  59     |  >> And then, then the distance function,                                          | 
 |  60     |  like, somehow already has built in the solution                                   | 
 |  61     |  to the problem because it's already put                                           | 
 |  62     |  the things that have the same answers together.                                   | 
 |  63     |  >> Right, you could do that, and of course, doing                                 | 
 |  64     |  that would require again solving the original problem. But yeah, so.              | 
 |  65     |  So, such a function has to exist, or, well, you                                   | 
 |  66     |  know, there's always noise. What if there's noise in your data,                   | 
 |  67     |  you know? But some such function like that has to                                 | 
 |  68     |  exist, the question is finding it. But I think the real                           | 
 |  69     |  point to take there is, there are some good distance                              | 
 |  70     |  functions for our problem and there are some bad distance functions               | 
 |  71     |  for our problem. And how you pick those is really fundamental                     | 
 |  72     |  assumption your making about the domain. That's why it's domain knowledge.        | 
 |  73     |  >> Yeah, that sounds right.                                                       | 
 |  74     |  >> Mm 'Kay. So, locality however it's expressed                                   | 
 |  75     |  to the distance function, that is similarity. Is built                            | 
 |  76     |  in to [UNKNOWN] that we believe that near points                                  | 
 |  77     |  are similar. Kind of by definition. That leads actually                           | 
 |  78     |  to the second preference bias which is this notion of                             | 
 |  79     |  smoothness. Alright. That we are by choosing to average.                          | 
 |  80     |  And by choosing to look at points that are similar                                | 
 |  81     |  to one another. We are expecting functions to behave,                             | 
 |  82     |  smoothly. Alright, so, you know, in the two D case.                               | 
 |  83     |  It's, it's kind of easy to see, right? You, you, you, you have these,             | 
 |  84     |  these sort of points and you're basically                                         | 
 |  85     |  saying, look, these two points should somehow be                                  | 
 |  86     |  related to one another more than this point and this point. And that sort         | 
 |  87     |  of assumes kind of smoothly changing behavior                                     | 
 |  88     |  as you move from one neighborhood to another.                                     | 
 |  89     |  [INAUDIBLE] that make sense?                                                      | 
 |  90     |  >> I mean, it seems like we're defining to be pretty similar to locality.         | 
 |  91     |  >> In this case. So I'm, I'm drawing an example, such that, you know,             | 
 |  92     |  whatever we meant by locality has already been kind of expressed in the graph.    | 
 |  93     |  >> Okay.                                                                          | 
 |  94     |  >> And you know, by picking, you know, this is really for pedagogical             | 
 |  95     |  reasons. You know can imagine, this you know, these are points that live in       | 
 |  96     |  77,000 dimensions, and it's impossible to actually                                | 
 |  97     |  visualize them much less draw them. And                                           | 
 |  98     |  I could try. [LAUGH] But here's, here's                                           | 
 |  99     |  three dimensions and here's the fourth dimension.                                 | 
 |  100    |  I think I'm going to get tired before I hit seven and seven thousand              | 
 |  101    |  but, you know, you kind of, you kind of get the idea, right? That, if. In,        | 
 |  102    |  you know, if you can imagine in your head points that are really                  | 
 |  103    |  near one another in some space, you                                               | 
 |  104    |  kind of hope that they behave similarly. Right.                                   | 
 |  105    |  >> Right. Okay, so locality and smoothness. And I think these make sense. I       | 
 |  106    |  mean, these, this is hardly the only                                              | 
 |  107    |  algorithm that makes these kind of assumptions.                                   | 
 |  108    |  But there is another assumption which is a bit more subtle I think. Which         | 
 |  109    |  is worth spending a second talking about, which is, for at least the distance     | 
 |  110    |  functions we've looked at before. The Euclidian distance and                      | 
 |  111    |  the Manhattan distance. They all kind of looked at each                           | 
 |  112    |  of the dimensions, sort of, and subtracted them, and                              | 
 |  113    |  squared them, or didn't, or took their absolute value and                         | 
 |  114    |  added them all together. What that means is, we                                   | 
 |  115    |  were treating, at least in those cases, that all the                              | 
 |  116    |  features mattered. And not only did they matter, they                             | 
 |  117    |  mattered equally. Right. So think about the the last quiz                         | 
 |  118    |  I gave you. Right. It said y equals x 1 squared plus x 2. And you noticed we      | 
 |  119    |  got answers that were wildly off from what the                                    | 
 |  120    |  actual answer was. Well if I know that the                                        | 
 |  121    |  first dimension. The first feature is going to be squared                         | 
 |  122    |  and the second one is not going to be                                             | 
 |  123    |  squared. Do you think either one of these features                                | 
 |  124    |  is more important or more important to get right?                                 | 
 |  125    |  >> Okay. Right. Trying to think about what that might mean. So,                   | 
 |  126    |  if, yea its definitely the case that when you look                                | 
 |  127    |  for similar examples in the database you want to care                             | 
 |  128    |  more about X1 because a little bit of a difference                                | 
 |  129    |  in X1 gets squared out. Right? It can lead to a                                   | 
 |  130    |  very large difference in the corresponding Y value. Whereas in                    | 
 |  131    |  the x2's, it's not quite as crucial. Th, th, the,                                 | 
 |  132    |  if you're off a little bit more, then you're off                                  | 
 |  133    |  a little bit more, it's just a linear relationship. So yeah,                      | 
 |  134    |  it does seems like that first dimension needs to be a lot                         | 
 |  135    |  more important, I guess, when you're doing the matching. Then the second one.     | 
 |  136    |  >> Right so, we probably would have gotten                                        | 
 |  137    |  different, I'm not going to go through this but,                                  | 
 |  138    |  we probably would have gotten different answers if, in                            | 
 |  139    |  the Euclidian or Manhattan case we had instead of                                 | 
 |  140    |  just taking the difference between the first two The                              | 
 |  141    |  first dimensions, we had taken that difference and squared                        | 
 |  142    |  it. And then in the case, including this and                                      | 
 |  143    |  squaring it again, and then some of those things                                  | 
 |  144    |  that were closer in the first dimension instead                                   | 
 |  145    |  of the second dimension would've looked more similar and                          | 
 |  146    |  we might've gotten better answer. That's probably a good                          | 
 |  147    |  exercise to go back and do for someone else.                                      | 
 |  148    |  >> [LAUGH] Yeah, I was thinking of doing it right                                 | 
 |  149    |  now, but yeah, probably should leave it for other people.                         | 
 |  150    |  >> Well you can do it if you want to. So did you do it Michael?                   | 
 |  151    |  >> I did.                                                                         | 
 |  152    |  >> And?                                                                           | 
 |  153    |  >> So it's a kind of now a mix between the Manhattan distance                     | 
 |  154    |  and the Euclidian distance. So, I'm taking                                        | 
 |  155    |  the first component, take the difference, square                                  | 
 |  156    |  it.                                                                               | 
 |  157    |  >> Mm-hm.                                                                         | 
 |  158    |  >> Take the second component, take the difference,                                | 
 |  159    |  absolute value it. And add those two things together.                             | 
 |  160    |  >> Sure.                                                                          | 
 |  161    |  >> All right. So if I do that, with one nearest neighbor,                         | 
 |  162    |  I still get that tie, but the output answer ends up being 12.                     | 
 |  163    |  >> Hm. Which                                                                      | 
 |  164    |  is better than 24.7.                                                              | 
 |  165    |  >> And that's better than eight, which is what                                    | 
 |  166    |  it was before. So the eight has gone up to                                        | 
 |  167    |  12, which is better than the other one, which I                                   | 
 |  168    |  think was 35.5, comes down to 29.5 Close here again                               | 
 |  169    |  to the correct answer which is eighteen. So in                                    | 
 |  170    |  both cases it kind of pushed in the right direction,                              | 
 |  171    |  it was using more, of the, the answers that were                                  | 
 |  172    |  relevant and fewer of the answers that were not relevant.                         | 
 |  173    |  >> Right. There you go. So the notion of relevance by the way,                    | 
 |  174    |  turns out to be very, very important. And highlights a weakness of                | 
 |  175    |  Knn. So this brings me to a kind of theorem or fundamental                        | 
 |  176    |  results of a machine learning that is particularly relevant to Knn but            | 
 |  177    |  its actually relevant everywhere. Do you think its worth while to mention it?     | 
 |  178    |  >> Sure it sounds [INAUDIBLE] relevant.                                           | 
 |  179    |  >> Alright let's do it.                                                           | 



##  11 - Curse of Dimensionality
 |  no     |  subtitle                                                                          | 
 |  -----  |  --------------------------------------------------------------------------------  | 
 |  1      |  Okay, Michael. So this notion of having different features or different           | 
 |  2      |  dimensions throw us off has a name and it's called the Curse of Dimensionality.   | 
 |  3      |  >> Oh, nice audio effect.                                                         | 
 |  4      |  >> I did like that effect in post-production. And                                 | 
 |  5      |  it refers to well, a very particular thing. So let                                | 
 |  6      |  me just read out what it refers to. As                                            | 
 |  7      |  the number of features or equivalently ,uh, dimensions grows that                 | 
 |  8      |  is as we add more and more features we go x of 1, x of two then                   | 
 |  9      |  we add x of three, add more and                                                   | 
 |  10     |  more of these features. As those features grows or                                | 
 |  11     |  as the number of dimensions grow ,the amount of data ,that we                     | 
 |  12     |  need to generalize accurately also grows exponentially. Now this                  | 
 |  13     |  is a problem of course because Exponentially means, bad in computer science land  | 
 |  14     |  because when things are exponential they're effectively untenable.                | 
 |  15     |  You just, you just, you sort of can't win.                                        | 
 |  16     |  >> I think everybody knows that in the sense that if you look,                    | 
 |  17     |  I've done this experiment actually, if you look in the popular press like,        | 
 |  18     |  you know, Time Magazine Or New York Times, USA Today. People will use             | 
 |  19     |  the word exponentially sometimes to mean                                          | 
 |  20     |  exponentially, and sometimes to mean, a lot.                                      | 
 |  21     |  >> Yeah that's actually a pet peeve of mine.                                      | 
 |  22     |  The whole notion of,                                                              | 
 |  23     |  >> Me too.                                                                        | 
 |  24     |  >> Oh, it's exponentially bigger. No,                                             | 
 |  25     |  that's, that's not meaningful. If you're                                          | 
 |  26     |  saying I have one point. And then I have another point, and I                     | 
 |  27     |  want to say this one point is exponentially bigger than this one. That's          | 
 |  28     |  meaningless! It's also liberally bigger than                                      | 
 |  29     |  that one. Exponentially refers to a trend.                                        | 
 |  30     |  >> Again, their,their,their not talking about the                                 | 
 |  31     |  mathematical relationship. They just mean a lot.                                  | 
 |  32     |  >> Okay, so they're wrong. And it bothers me deeply but                           | 
 |  33     |  I'm willing to accept it for the purposes of this discussion. Okay.               | 
 |  34     |  Exponentially means bad. It means that we need more, and more, and more,          | 
 |  35     |  and more data as we add features and dimensions. Now as a machine                 | 
 |  36     |  learning person this is a real problem right, because What you want to do,        | 
 |  37     |  or like what your instinct tells you to do is, oh ,we've                          | 
 |  38     |  got this problem, we've got a bunch of data, we're not sure what's                | 
 |  39     |  important. So why don't we just keep adding more and more and more                | 
 |  40     |  features. You know, we've got all these sensors and we'll just add this           | 
 |  41     |  little bit and this little bit, and we'll keep                                    | 
 |  42     |  track of GPS location and we'll see the time of                                   | 
 |  43     |  the day and we'll just keep adding stuff and then                                 | 
 |  44     |  we'll figure out which ones are important. But the curse                          | 
 |  45     |  of dimensionality says that every time you add another one                        | 
 |  46     |  of these features. You add another dimension, to your input                       | 
 |  47     |  space, you're going to need exponentially more data, as you add                   | 
 |  48     |  those features, in order to be able to generalize accurately.                     | 
 |  49     |  >> Mm.                                                                            | 
 |  50     |  >> This is a very serious problem, and it sort                                    | 
 |  51     |  of captures, a little bit of what the difficulties are                            | 
 |  52     |  in k and n. If you have a di, if you have distance function                       | 
 |  53     |  or a similarity function, that assumes that                                       | 
 |  54     |  everything is Relevant, or equally relevant, or                                   | 
 |  55     |  important, and some of them aren't. You're going to have to see a lot of          | 
 |  56     |  data before you can figure that out, sort of before it washes itself away.        | 
 |  57     |  >> [CROSSTALK]                                                                    | 
 |  58     |  >> Yeah, that makes a lot of sense.                                               | 
 |  59     |  >> Yeah, it seems a little scary. So, you know, I think you                       | 
 |  60     |  can say these words, and the words sort of make sense, but I think                | 
 |  61     |  it helps to kind of draw a picture,                                               | 
 |  62     |  and so I'm going to draw a little picture. Okay?                                  | 
 |  63     |  >> Yeah.                                                                          | 
 |  64     |  >> All right.                                                                     | 



##  12 - Curse of Dimensionality Two
 |  no     |  subtitle                                                                          | 
 |  -----  |  --------------------------------------------------------------------------------  | 
 |  1      |  Okay, Michael, so let's, let's look at this little line                           | 
 |  2      |  segment, okay? And then say I've got ten little points that                       | 
 |  3      |  I could put down on this line segment, and I want                                 | 
 |  4      |  them all to represent some part of this line, alright? That's                     | 
 |  5      |  kind of [UNKNOWN] -ish. So, I'm going to put a little                             | 
 |  6      |  X here, I'll put one here, I'll put one here, put                                 | 
 |  7      |  one here, put one here, here, here, here, here, here. Is                          | 
 |  8      |  that ten? Three... six. Nine, ten. Ten. Okay. And let's pretend                   | 
 |  9      |  I did the right thing here and I have them                                        | 
 |  10     |  kind of uniformly distributed across the line segment. So that means              | 
 |  11     |  each one of these points is sort of owning, an                                    | 
 |  12     |  equal size sub segment of this segment. Does that make sense?                     | 
 |  13     |  >> Yeah, so, so it's representing it in the sense that, that point. Uh,when       | 
 |  14     |  you're trying to estimate values of other places on the line it's going to        | 
 |  15     |  default as the nearest neighbor to being                                          | 
 |  16     |  that point so there's a very small little                                         | 
 |  17     |  neighborhood of the red line segment that is covered by each of the green X's.    | 
 |  18     |  >> That is exactly right and in fact each one                                     | 
 |  19     |  of these green X's represents. How much of this segment?                          | 
 |  20     |  >> Each of the green X's covers one tenth?                                        | 
 |  21     |  >> That's exactly right. You cover one tenth. Alright                             | 
 |  22     |  Michael, so let's say I move from a line                                          | 
 |  23     |  segment now to a two dimensional space. So                                        | 
 |  24     |  a little square segment. If that's the right                                      | 
 |  25     |  technical term. And I've taken my little ten                                      | 
 |  26     |  x's, and I put them down here before. Well,                                       | 
 |  27     |  here's something you'll notice; you'll notice that each                           | 
 |  28     |  one of these x's is going to still end                                            | 
 |  29     |  up representing one-tenth of all of this space,                                   | 
 |  30     |  but you'll also notice that, that, that it's representing                         | 
 |  31     |  now you know. Really really really really big.                                    | 
 |  32     |  >> I see.                                                                         | 
 |  33     |  >> So one way of putting it is, you know if you think                             | 
 |  34     |  about the farthest point, as opposed to                                           | 
 |  35     |  the furthest point which would be incorrect.                                      | 
 |  36     |  >> [LAUGH]                                                                        | 
 |  37     |  >> The farthest point that this particular first x                                | 
 |  38     |  over here is representing, its got some distance here.                            | 
 |  39     |  Over here, the farthest point from this x, the                                    | 
 |  40     |  distance is very, very far away. So, a question                                   | 
 |  41     |  would be, how can I make it so that each of                                       | 
 |  42     |  the x's I put down represents the same amount of. I                               | 
 |  43     |  don't know diameter or distance as the xs in this line                            | 
 |  44     |  segment over here. So what do you think I have to do?                             | 
 |  45     |  >> I feel like you need to fill up the square with xs.                            | 
 |  46     |  >> Yeah, that's exactly right so let's do that. So                                | 
 |  47     |  filling em up Michael as you suggested. You'll notice that                        | 
 |  48     |  at least if we pretend that I drew this right. Each of                            | 
 |  49     |  these X's is now going to end up being the nearest neighbor for                   | 
 |  50     |  a little square like this, and the diameter of these little squares are           | 
 |  51     |  going to be the same as the diameter of these little line segments.               | 
 |  52     |  >> Yeah, I agree for some definition of the word diameter.                        | 
 |  53     |  >> Yes, and for some definition of our demonstration. Okay, so how                | 
 |  54     |  many of these X's are there, Michael? Can you tell? You want to count?            | 
 |  55     |  >> [LAUGH].                                                                       | 
 |  56     |  I'm going to multiple [CROSSTALK] cause it looks like                             | 
 |  57     |  you did ten by ten so that'll be 100.                                             | 
 |  58     |  >> That'll be 100. So each one now holds a hundredth of the space, and I went     | 
 |  59     |  from needing ten points to, of course, 100 points                                 | 
 |  60     |  in order to cover the same amount of space.                                       | 
 |  61     |  >> Alright, so that definitely seems like the mild rebuke of dimensionality.      | 
 |  62     |  >> Yes.                                                                           | 
 |  63     |  >> But doesn't seem that bad.                                                     | 
 |  64     |  >> Okay well, what happens if I now move into three dimensions?                   | 
 |  65     |  So now, if I want to cover the same amount of, you know,                          | 
 |  66     |  diameter space for, you know, sufficient                                          | 
 |  67     |  definition of diameter. I'm going to have                                         | 
 |  68     |  to do a bunch of copying and pasting that I'm not willing                         | 
 |  69     |  to do so, you know, there would be more x's here and                              | 
 |  70     |  you know, there will be x's there and an x here and                               | 
 |  71     |  it'll just kind of go and fill up some space and you                              | 
 |  72     |  know, I'm not going to do this whatever but [SOUND] and you'll get                | 
 |  73     |  x's everywhere. And you notice, I need a lot more X's than                        | 
 |  74     |  I had before. And by the way, I'm just                                            | 
 |  75     |  showing you the outside of this little cube, there are                            | 
 |  76     |  actually X's on the inside as well, that you                                      | 
 |  77     |  can't see. How many X's do you think I have?                                      | 
 |  78     |  >> I don't think you drew any X's. You're                                         | 
 |  79     |  just like scribbling on the side of the cube.                                     | 
 |  80     |  >> These are X's.                                                                 | 
 |  81     |  >> You, you were doing so well for awhile, and then just lost it entirely.        | 
 |  82     |  >> Well, wouldn't you lose it if you had to write 1000 x's.                       | 
 |  83     |  >> Hm. No                                                                         | 
 |  84     |  because I would use computers to help me but yes, yes it is very                  | 
 |  85     |  frustrating to have to have that many x's. And so but in particular in            | 
 |  86     |  this case we're talking about data points in a nearest neighbor method and that,  | 
 |  87     |  boy that does seem like a big growth from ten to a 100 to 1000.                   | 
 |  88     |  >> In fact the growth is, exponential.                                            | 
 |  89     |  >> Exponential                                                                    | 
 |  90     |  >> >Right. So if we went into four dimensions, which                              | 
 |  91     |  I'm not going to draw, then we would need not                                     | 
 |  92     |  1,000, but 10,000 points. And if five dimensions we would                         | 
 |  93     |  need 100,000 points. And in six dimensions, we would need 1,000,000               | 
 |  94     |  points. And so on and so forth. So something like.                                | 
 |  95     |  Ten to the D, where D is the number of dimensions.                                | 
 |  96     |  >> Wow.                                                                           | 
 |  97     |  >> Right. So this is really problematic right.                                    | 
 |  98     |  In my little nearest neighbor method, wanted to be                                | 
 |  99     |  able to say, well, I want to make                                                 | 
 |  100    |  sure the neighborhood remains small, as I add dimensions,                         | 
 |  101    |  I'm going to need to grow the number of points that                               | 
 |  102    |  I have in my training set exponentially. And that's really bad.                   | 
 |  103    |  And by the way, this isn't just an issue. Of                                      | 
 |  104    |  k-nn. This is true in general, don't think about this now                         | 
 |  105    |  as nearest neighbors in the sense of [INAUDIBLE], but think                       | 
 |  106    |  of it as points that are representing or covering the space.                      | 
 |  107    |  And if you want to represent the same sort of hyper-volume                        | 
 |  108    |  of space as you add dimensions, you're going to have to get                       | 
 |  109    |  exponentially more points in order to do that. And                                | 
 |  110    |  coverage is necessary to do learning. So the curse                                | 
 |  111    |  of dimensionality does not just to K and N.                                       | 
 |  112    |  It is a curse of dimensionality for ML period [SOUND].                            | 
 |  113    |  >> You mean for me?                                                               | 
 |  114    |  >> Yes. Because of [INAUDIBLE]                                                    | 
 |  115    |  >> [LAUGH] Okay. And that seems really problematic because it's very              | 
 |  116    |  natural to just keep throwing dimensions into a machine learning problem.         | 
 |  117    |  Like it's, it's having trouble learning. Let me                                   | 
 |  118    |  give it a few more dimensions so, to give                                         | 
 |  119    |  it hints. But really what you're doing is just                                    | 
 |  120    |  giving it a larger and larger volume to fill.                                     | 
 |  121    |  >> Yeah. And it can't fill it unless you give it more and more                    | 
 |  122    |  data. So you're better off giving more data than you are giving more dimensions.  | 
 |  123    |  >> Zoinks.                                                                        | 
 |  124    |  >> Mm-hm. There's an entire series of lessons that                                | 
 |  125    |  we will get eventually that, that deals with this issue.                          | 
 |  126    |  >> The issue of?                                                                  | 
 |  127    |  >> Dimensionality.                                                                | 
 |  128    |  >> Finding the right dimensionality?                                              | 
 |  129    |  >> Yeah.                                                                          | 
 |  130    |  >> That would be a useful thing.                                                  | 
 |  131    |  >> It would. But it's far off in the future. It's like infinitely                 | 
 |  132    |  far in the future. So we'll worry about that in a few weeks.                      | 
 |  133    |  >> Okay.                                                                          | 
 |  134    |  >> Okay. All right. So there you go, Michael.                                     | 
 |  135    |  Curse of Dimensionality is real and it's a real problem.                          | 
 |  136    |  >> Where did that term come from, it's a cool                                     | 
 |  137    |  term. I think it came from, oh what's his name. Bellman.                          | 
 |  138    |  >> Oh, Bellman, like the dynamic programming guy.                                 | 
 |  139    |  >> Yeah, the dynamic programming guy,                                             | 
 |  140    |  uh,the Bellman of Bellman equation guy.                                           | 
 |  141    |  >> Which we haven't gotten to yet in the course.                                  | 
 |  142    |  >> Which we haven't gotten to in the course but we will get to in the             | 
 |  143    |  course. Because it's central. So it looks like                                    | 
 |  144    |  actually, the element's central to a lot of things.                               | 
 |  145    |  >> Wow.                                                                           | 
 |  146    |  >> Sometimes it gives us equations that                                           | 
 |  147    |  helps us but sometimes it gives us curses.                                        | 
 |  148    |  >> [LAUGH] Curses Betterman. Foiled again.                                        | 
 |  149    |  >> [LAUGH]                                                                        | 



##  13 - Some Other Stuff
 |  no     |  subtitle                                                                          | 
 |  -----  |  --------------------------------------------------------------------------------  | 
 |  1      |  Okay, Michael so we talked a little bit about the curse of dimensionality,        | 
 |  2      |  but I think it's worthwhile to talk about some other stuff that comes             | 
 |  3      |  up. We've been sort of skirting around this and you know bring it                 | 
 |  4      |  up in various ways throughout our discussion so far. But I think it's worthwhile  | 
 |  5      |  kind of writing them all down on a slide and trying to think                      | 
 |  6      |  through them for a little bit. So ,uh, the other stuff that comes                 | 
 |  7      |  up in [UNKNOWN] mainly comes up in these sort of assumptions we make              | 
 |  8      |  about parameters to the algorithm. So the one we talked about ,uh, probably the   | 
 |  9      |  most is our distance measure, you know our                                        | 
 |  10     |  distance between some X and some query point Q                                    | 
 |  11     |  and we've explored a couple. We looked at                                         | 
 |  12     |  Eucudean and we looked at Manhattan. And we even                                  | 
 |  13     |  looked at weighted versions of those. And this                                    | 
 |  14     |  really matters, I've said this before but I really                                | 
 |  15     |  think it bears repeating that your choice of                                      | 
 |  16     |  distance function Really matters. If you pick the wrong                           | 
 |  17     |  kind of distance function, you're just going to get very poor behavior.           | 
 |  18     |  >> So I, so I have a question about these these distance functions.               | 
 |  19     |  So you mentioned Euclidean and Manhattan,                                         | 
 |  20     |  are there other distance functions that the                                       | 
 |  21     |  students should know? Like, things that they, that might come up, or things       | 
 |  22     |  that they should think of first if they have a particular kind of data?           | 
 |  23     |  >> yeah, there's a, there's a ton of them. I think Well, first off,               | 
 |  24     |  it, it's probably worth pointing out that                                         | 
 |  25     |  this, this notion of weighted distance is one                                     | 
 |  26     |  way to deal with the curse of dimensionality. You can weight                      | 
 |  27     |  different dimensions differently. And that would be one, and you might            | 
 |  28     |  come up with sort of automatic ways of doing that. That,                          | 
 |  29     |  that's sort of worth mentioning. But you will notice that both Euclidean          | 
 |  30     |  and Manhattan distance at least as we have talked about them,                     | 
 |  31     |  are really useful for things like regression. Their kind of assuming              | 
 |  32     |  that you have numbers in that subtraction kind of makes sense.                    | 
 |  33     |  But there are other functions, distance functions that you might do if            | 
 |  34     |  you are dealing with cases like, I don't know Discrete                            | 
 |  35     |  data, right? Where instead of it all being numbers, it's colors,                  | 
 |  36     |  or something like that. Alright so, your distance might be mismatches.            | 
 |  37     |  For example, or it might be a mixture of those. In                                | 
 |  38     |  fact, one of the nice things about KNN, is that                                   | 
 |  39     |  we've been talking about it with points, because it's sort of                     | 
 |  40     |  easy to think about it that way. But this distance function                       | 
 |  41     |  is just a black box. You can take Arbitrary things and                            | 
 |  42     |  try to decide how similar they are based on whatever you                          | 
 |  43     |  know about the domain and that could be very useful. So                           | 
 |  44     |  ,you could talk about images right, where you take pictures of                    | 
 |  45     |  people and you know rather than doing something like a pixel                      | 
 |  46     |  by pixel comparison, you try to line up their eyes. And                           | 
 |  47     |  look at their mouths, and try to see if they're the                               | 
 |  48     |  same shape you know things like that, that might be more                          | 
 |  49     |  complicated and and perhaps even arbitrarily                                      | 
 |  50     |  computational to determine notions of similarity                                  | 
 |  51     |  so really this idea of distance in similarity tells                               | 
 |  52     |  you a lot about your domain and what you                                          | 
 |  53     |  believe about it. ,another thing that's worth what what's                         | 
 |  54     |  pushing on a little bit is how you pick k.                                        | 
 |  55     |  Well there's no good was to pick k you                                            | 
 |  56     |  just You just have to know something about it, but                                | 
 |  57     |  I want to think about a particular case. Well,                                    | 
 |  58     |  what if we end up in a world where K=N.                                           | 
 |  59     |  >> Well, that would be silly.                                                     | 
 |  60     |  >> Why would it be silly?                                                         | 
 |  61     |  >> Well, so if K=N, then what you're doing is you're taking, so in the case       | 
 |  62     |  of regression for example, you're taking all                                      | 
 |  63     |  of the data points and averaging the.                                             | 
 |  64     |  Y values together. Basically ignoring the query.                                  | 
 |  65     |  So, you end up with a constant function.                                          | 
 |  66     |  >> But that's only if you do a                                                    | 
 |  67     |  simple average. What if you do a weighted average?                                | 
 |  68     |  >> A weighted average. So the near, the points that are                           | 
 |  69     |  the query are going to get more weight in the average, so                         | 
 |  70     |  that acually will be diffrent. Even though k equals n, it                         | 
 |  71     |  will be different depending on where you actually put your query down.            | 
 |  72     |  >> Exactly. That's exactly right so, for example, if I have                       | 
 |  73     |  a little bunch of points like this say. Where you notice it                       | 
 |  74     |  kind of looks like I have two different lines here and                            | 
 |  75     |  I can pick a query point way over here, all of these                              | 
 |  76     |  points are going to influence me as oppose to these points and                    | 
 |  77     |  so I'm going to end up. Estimating with something that looks more                 | 
 |  78     |  like this because these points over here won't have much to                       | 
 |  79     |  say. But if I have a query point that's way over here                             | 
 |  80     |  somewhere these points are going to matter and I'm going to end up                | 
 |  81     |  looking something looks a little bit more like this than like                     | 
 |  82     |  that. Now I'm drawing these as lines. They won't exactly look                     | 
 |  83     |  like lines because these points will have some influence. They'll be more         | 
 |  84     |  curvy than that. But the point is that near, near                                 | 
 |  85     |  the place we want to do the query it will                                         | 
 |  86     |  look To be more strongly influenced by these points over                          | 
 |  87     |  here or these points over here depending on where you are.                        | 
 |  88     |  >> Well that gives me an idea.                                                    | 
 |  89     |  >> Oh, what kind of idea does it give you?                                        | 
 |  90     |  >> Well, what about instead of just taking                                        | 
 |  91     |  a weighted average, what about using a distance matrix                            | 
 |  92     |  to pick up some of the points? And                                                | 
 |  93     |  then do a different regression on that substantive point.                         | 
 |  94     |  >> Right, I like that.                                                            | 
 |  95     |  So we can replace this whole notion of                                            | 
 |  96     |  average with a more kind of, regression-y thing.                                  | 
 |  97     |  >> So it actually, instead of using the same value for                            | 
 |  98     |  the whole patch. Actually, it still continues to use the input values.            | 
 |  99     |  >> Yeah. So, in fact, average is just                                             | 
 |  100    |  a special case of a kind of regression, right?                                    | 
 |  101    |  >> Mm hm, mm hm.                                                                  | 
 |  102    |  >> Right? So this actually has a name,                                            | 
 |  103    |  believe it or not. It's actually called locally                                   | 
 |  104    |  weighted regression. Yeah, so this actually works pretty                          | 
 |  105    |  well and in place of sort of averaging                                            | 
 |  106    |  function, you can do just about anything you want to.                             | 
 |  107    |  You could throw in a decision tree, you could throw in                            | 
 |  108    |  a neural network, you could throw in lines do linear                              | 
 |  109    |  regression. You can do, almost anything that you can imagine doing.               | 
 |  110    |  >> Neat,                                                                          | 
 |  111    |  >> Yeah. Add that works out very well. And again, it                              | 
 |  112    |  gives you a little bit of power. So here's something I don't                      | 
 |  113    |  think is very obvious until it's pointed out to you. Which is                     | 
 |  114    |  this notion of replacing the average with a more general regression or            | 
 |  115    |  even classification function. It actually allows                                  | 
 |  116    |  you to do something more powerful                                                 | 
 |  117    |  than it seems. So let's imagine that we were going to do locally                  | 
 |  118    |  weighted regression and we were going to do, in fact, linear regression. So,      | 
 |  119    |  what would locally- weighted linear regression look like? Well, if we go          | 
 |  120    |  back to this example over here on the left basically, you take                    | 
 |  121    |  all the points that are nearby and you try to fit a                               | 
 |  122    |  line to it. And, so you would end up with stuff that                              | 
 |  123    |  looked, pretty much, like this. While you're over here, you would get             | 
 |  124    |  the line like this, but while you were over here you'd                            | 
 |  125    |  get a line like this. Then, somewhere in the middle you                           | 
 |  126    |  would get lines that started to look like this and And                            | 
 |  127    |  you would end up with something that kind of ended up looking                     | 
 |  128    |  a lot like a curve. So that's kind of cool because                                | 
 |  129    |  you notice that we start with a hypothesis state of lines                         | 
 |  130    |  and this locally weighted linear regression. But then we end up                   | 
 |  131    |  actually being able to represent a hypothesis space that is strictly bigger.      | 
 |  132    |  Then the set of lines. Hm. So we can                                              | 
 |  133    |  use a very simple kind of hypothesis space but by                                 | 
 |  134    |  using this locally weighted regression we end up with                             | 
 |  135    |  a more complicated space that is complicated, that's made more                    | 
 |  136    |  complicated depending upon the complications that are represented by              | 
 |  137    |  your data points. So this results, this sort of reveals                           | 
 |  138    |  another bit of power with k nn. Which is, it                                      | 
 |  139    |  allows you to take local information and build functions or                       | 
 |  140    |  build concepts around the local things that are similar to                        | 
 |  141    |  you. And that allows you to make arbitrarily complicated functions.               | 
 |  142    |  >> Neat.                                                                          | 
 |  143    |  >> At least in principle. Okay, cool. Alright so you got all that?                | 
 |  144    |  >> I, think so yeah.                                                              | 
 |  145    |  >> Okay, cool. So then, I think we should wrap up.                                | 
 |  146    |  >> Nice.                                                                          | 
 |  147    |  >> Nice.                                                                          | 



##  14 - What Have We Learned
 |  no     |  subtitle                                                                          | 
 |  -----  |  --------------------------------------------------------------------------------  | 
 |  1      |  Okay Michael so I think with that little                                          | 
 |  2      |  bit of discussion, I feel like we're done.                                        | 
 |  3      |  >> Cool! Alright. Well it's been nice talking to you. I hope                      | 
 |  4      |  the course went well and, oh you mean just for this lesson?                       | 
 |  5      |  >> Yeah just for this lesson.                                                     | 
 |  6      |  >> Alright.                                                                       | 
 |  7      |  >> So let's.                                                                      | 
 |  8      |  >> Well let's wrap up this lesson then.                                           | 
 |  9      |  >> Yeah let's see what have we learned?                                           | 
 |  10     |  So remind me Michael what have we learned?                                        | 
 |  11     |  >> Well we were talking about instance based learning.                            | 
 |  12     |  >> That's true. That's the first thing we learned. You will notice                | 
 |  13     |  by the way, I never actually told you why it was called instance                  | 
 |  14     |  based learning.                                                                   | 
 |  15     |  >> Charles, why is it called instance based learning?                             | 
 |  16     |  >> I don't know but I am willing to guess that it has to do with a                | 
 |  17     |  fact that we look at the exact instances that                                     | 
 |  18     |  we have and we base our learning on that.                                         | 
 |  19     |  >> Alright and we brought it in                                                   | 
 |  20     |  by starting off thinking eager and lazy learning.                                 | 
 |  21     |  >> Right. What is the difference, Michael?                                        | 
 |  22     |  >> I will tell you when I need to tell you.                                       | 
 |  23     |  >> [Laugh]                                                                        | 
 |  24     |  That's exactly right.                                                             | 
 |  25     |  >> So lazy learning is about putting off the work                                 | 
 |  26     |  until it's actually needed. Eager is about, as soon as                            | 
 |  27     |  the problem is posed, solve it. And then, you know,                               | 
 |  28     |  if you're lucky, the answer will eventually come in handy.                        | 
 |  29     |  >> Exactly right. Okay what else?                                                 | 
 |  30     |  >> So as a concret example of a lazy                                              | 
 |  31     |  learner we talked about K's nearest neighbor or K-nn.                             | 
 |  32     |  >> K-nn. And                                                                      | 
 |  33     |  this whole notion of nearest neighbor. Is in                                      | 
 |  34     |  fact one way of talking about similarity functions.                               | 
 |  35     |  >> Right and the similarity functions play a really central role in all this.     | 
 |  36     |  >> Right. Similarity. We talk about it as                                         | 
 |  37     |  if they were distance functions. But distance is                                  | 
 |  38     |  just another way of talking about, a similarity.                                  | 
 |  39     |  So, this is actually keeping. K-nn was a specific,                                | 
 |  40     |  algorithm we used, and we talked about various versions of it,                    | 
 |  41     |  and, the nearest neighbor part really got us to think a                           | 
 |  42     |  little bit about similarity and distance and, and what all that                   | 
 |  43     |  means. A really important thing here is, I think, that similarity is              | 
 |  44     |  just another way of capturing the main knowledge. And K, in                       | 
 |  45     |  K-nn is another way of capturing the main knowledge. And that                     | 
 |  46     |  if we saw through the quizes and some of our discussions,                         | 
 |  47     |  that this is actually very, very important. That the main knowledge matters.      | 
 |  48     |  Now, we also talked about KNN in the context of both regression and               | 
 |  49     |  classification. I see what you did there, 'Knnowledge', it's got KNN in it.       | 
 |  50     |  >> >Okay, so yeah, classification and regression are different things. But,       | 
 |  51     |  KNN can handle both of them. And, at the end of the                               | 
 |  52     |  day, that's all stuck in our notion of similarity, and our                        | 
 |  53     |  notion of averaging. Which we kind of took as an overall term,                    | 
 |  54     |  for a bunch of different things you might do, which some people find confusing.   | 
 |  55     |  >> [LAUGH].                                                                       | 
 |  56     |  >> But I think that other people                                                  | 
 |  57     |  would really kind of understand what we mean.                                     | 
 |  58     |  >> I'm very tempted to take that out of                                           | 
 |  59     |  Wikipedia, but that would, that would just be rude.                               | 
 |  60     |  >> It would be rude. Anything else? We learned one big thing.                     | 
 |  61     |  >> We looked at how to compose different learning algorithms                      | 
 |  62     |  together. For example in the context of locally weighted linear regression.       | 
 |  63     |  >> Mm hm.                                                                         | 
 |  64     |  >> We used this instance based idea                                               | 
 |  65     |  along with linear regression to get something                                     | 
 |  66     |  that was both locally smooth but globally bumpy.                                  | 
 |  67     |  >> Right. So, I'm going to just say                                               | 
 |  68     |  locally weighted regression. Where we can do any kind                             | 
 |  69     |  of regression we might want to. I was going to                                    | 
 |  70     |  call that $X. So, stick in your favorite value.                                   | 
 |  71     |  >> Let's see, what else? Oh, oh, a                                                | 
 |  72     |  really big thing was Bellman's curse of dimensionality.                           | 
 |  73     |  >> Yes.                                                                           | 
 |  74     |  >> And                                                                            | 
 |  75     |  the idea there was that the more features that you                                | 
 |  76     |  include The more data you need to fill up that space.                             | 
 |  77     |  >> Yep, It's exponential.                                                         | 
 |  78     |  >> And in fact I even just I decided to go and play with this a little            | 
 |  79     |  bit so that example that you were doing                                           | 
 |  80     |  before where the y equals x1 squared plus x2                                      | 
 |  81     |  >> Mm-hm.                                                                         | 
 |  82     |  >> When I gave it well as we saw in the example we gave it like ten or 12         | 
 |  83     |  examples and it did really badly. So it continued to do somewhat badly until      | 
 |  84     |  I got to about 100,000 and then it was actually doing [LAUGH] really well.        | 
 |  85     |  >> Hmm.                                                                           | 
 |  86     |  >> But that seems like an awful lot of                                            | 
 |  87     |  examples for what is otherwise a very simple problem.                             | 
 |  88     |  >> Right. Well if you think about it, the                                         | 
 |  89     |  amount of data you have to see to determine                                       | 
 |  90     |  the relative. Relevance of the two different dimensions is                        | 
 |  91     |  quite a bit in that particular kind of function.                                  | 
 |  92     |  >> Hm.                                                                            | 
 |  93     |  >> Yeah. That's a lot                                                             | 
 |  94     |  of space to cover. All possible real                                              | 
 |  95     |  values [LAUGH] across a potentially infinite space.                               | 
 |  96     |  >> Yeah, I guess that's true.                                                     | 
 |  97     |  >> Yeah, so the cursor dimensionality is real and we                              | 
 |  98     |  just sort of can't get around it. Although As I mentioned                         | 
 |  99     |  earlier we will see in the second part of the                                     | 
 |  100    |  course ways that people try to get around recursive dimensionality.               | 
 |  101    |  >> Ahah!                                                                          | 
 |  102    |  >> Mm-hm. Okay.                                                                   | 
 |  103    |  >> Or at least                                                                    | 
 |  104    |  blunt it. Right?                                                                  | 
 |  105    |  >> Yeah or at least blunt it because you can't                                    | 
 |  106    |  actually get around recursive dimensionality, you can only deal with it.          | 
 |  107    |  >> There is no free lunch.                                                        | 
 |  108    |  >> There is no free lunch. In fact, that's a theorem.                             | 
 |  109    |  >> [LAUGH]                                                                        | 
 |  110    |  >> [INAUDIBLE] a theorem?                                                         | 
 |  111    |  >> Yeah, I think so.                                                              | 
 |  112    |  >> What's the theorem?                                                            | 
 |  113    |  >> No free lunch. That any learning algorithm that you create                     | 
 |  114    |  is going to have the property; that if you average over all possible instances,   | 
 |  115    |  it's not doing any different than random.                                         | 
 |  116    |  >> Right. And, and another way of thinking about                                  | 
 |  117    |  that, a practical way of thinking about that is;                                  | 
 |  118    |  if I don't know anything about the data that                                      | 
 |  119    |  I'm going to have to learn over. Then, it doesn't                                 | 
 |  120    |  really matter what I do because there's all possible                              | 
 |  121    |  kind of data sets. However, if I have domain                                      | 
 |  122    |  knowledge, I can use that to choose the best                                      | 
 |  123    |  learning algorithm for the problems that I'm going to encounter.                  | 
 |  124    |  >> So does that mean that, that all of machine learning really comes down to,     | 
 |  125    |  you have to already know what you need to solve                                   | 
 |  126    |  the problem to apply these. Techniques to solve the problem?                      | 
 |  127    |  >> No, but you have to know a little bit                                          | 
 |  128    |  about your problem in order to decide what to do.                                 | 
 |  129    |  And in fact, you could make the argument that this                                | 
 |  130    |  entire class is about exposing the students to a wide                             | 
 |  131    |  range of techniques and giving them enough practice so that                       | 
 |  132    |  they can do a pretty good job of telling, given                                   | 
 |  133    |  a problem. Would it be better to use this kind                                    | 
 |  134    |  of technique or this kind of technique? Is K-nn a sort of                         | 
 |  135    |  better way of approaching it? Decision tree a better way                          | 
 |  136    |  of approaching it? Um,It's a lot of what this class is                            | 
 |  137    |  about. Is helping them to get enough domain knowledge or enough                   | 
 |  138    |  knowledge anyways so that they can apply it to particular domains.                | 
 |  139    |  >> Cool, so alright, that seems like a plenty useful lesson.                      | 
 |  140    |  >> Yes, it's a very hopeful note to end on, so let's end on that.                 | 
 |  141    |  >> Alright, see you next time.                                                    | 
 |  142    |  >> Alright, bye Michael.                                                          | 



