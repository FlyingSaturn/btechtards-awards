# zeno-awards
A point system being developed by FlyingSaturn for Reddit.
(Name not given yet)


# Parameters

0. Eligibility of the post (post flairs like "Showcase your project", or maybe we can make new post flairs for guides and technical stuff)
1. Eligibilty of the user giving the award
2. The one writing the comment/post should just have the normal requirements (so, nothing new needed)
3. How many awards given to this post? If more, then automod says, "Nah I'd win, you won't be giving more awards to this asymptotic* piece of quality comment."
4. Awarded before? Then nuh-uh!
5. Points exceeded? Limit reached bro.


The whole thing is intentionally kept within an infinite loop. For now, it's just a simulation but is a very good metaphor for every case the PRAW integration might have.

# *System of the increments

Ever heard of [Zeno's Dichotomy Paradox](https://en.wikipedia.org/wiki/Zeno's_paradoxes#Dichotomy_paradox)? I (FlyingSaturn) am planning to keep something like diminishing returns, much like that Dichotomy paradox. [This particular idea of mine is unknowingly influenced by a VSauce video.](https://youtu.be/Pxb5lSPLy9c)

First of all, what is that paradox? Say, from Point A to B (1 unit length, you travel half the distance. From that half, you travel half the distance (1/4 + 1/2 = 3/4 or 0.75). From there, 1/8 added, we get 7/8. But we never reach 1.

How has this been used here? We assume that once the system hits 0.99 points, it directly goes to 1, thereby breaking the asymptotic flow altogether. When it goes to 1, limit reached and the automod 'moves on' with the post. No more increments for that post, sorry. But if only 1 award has been given, half of the barrier has passed, because the first achievement is always the hardest. From then, it just goes to "the ocean is thirsty" mode, so we just put a stop altogether when it reaches .99-something points: we just increase it to 1.

From the perspective of psychology (not physics/kinematics), it is in my personal opinion that Zeno's Dichotomy Paradox isn't a paradox, it's a reality. I heard from somewhere that if there is/are lions chasing you, then increasing 1 lion among 99 lions DOESN'T INCREASE the problematic factor much, whereas adding one lion to another lion INCREASES the problematic factor much more THAN BEFORE. 

In case of achievements, as said before, getting the first award is the hardest. That's why I literally claim, "You've done half of the work already." This will give incentives to people for even giving less amount of posts.

# Constants used

Deserves a separate section of its own.

CAP is the limit value. When the points equal or exceed CAP, then points = 1 and the limit is reached. CAP shouldn't be increased more than 1. Even then, increasing CAP to something more than .95 isn't recommended. CAP more, delay to get to 1 more.

FACTOR is the variable which governs what part of the remaining distance should be covered. Increase the factor, more delays.


Adjust the values and check for yourself which feels more of a healthy progression. I'll check with FACTOR = e.

(It didn't work. Golden ratio didn't either. (1+1/e) suffered the same)

# Mathematical Perspective

We were using 1/(FACTOR^n) for our needs. Basically, we were adding (FACTOR^(-n)). Notice that the initial value wasn't 1, it was .5. Otherwise, the infinite geometric series would have converged to 2. But converges to 1. (Man, humans INDEED think in terms of multiplication, not addition)

Therefore, in the GP, a = 1*(1/r). While calculating the series, we get

(1 * (1/r)) / (1 - 1/r)

which results in 

1 / (r - 1)

Putting y = 1/(x-1) on a graph, we notice that for 2, it's 1, for e, it's 0.58..., we need something which will work. I don't think that changing the FACTOR will work, or it will... if done carefully.
We can make the factor less than 2, but just by a bit. We can also change the CAP to a smaller value, from example, from .99 to .96

# Points for the future (Self)

- Before pitching the idea, try to integrate Devvit or CRON in the mix. You need to know Redis man.
- Tracking needed: we just need to track the post and who awarded the awards (maybe same IP addresses can't award the same person ig?), then we'll save the TOTAL points of the post and the posters who contributed. All of these saved stuff will actually be attached to the post, and the post will be attached to the user. Now, for addition, we'll add the name of that specific poster and will update the field like this: `points = points - prev + zeno()`, where we literally won't need to care what the next value will be based on the previous value. This will give us some independence to experiment with `zeno()`.
- zeno() should actually recalculate the no. of points, like, reinventing the wheel.  (wait, do we really need all this `prev`? can't we just use points = `zeno()`)
- Well, atleast it won't let us shoot on the foot, we can literally calculate by seeing the number of posters...
