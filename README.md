# btechtards-awards
A point system being developed by the mods of r/btechtards.
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

Ever heard of [Zeno's Dichotomy Paradox](https://en.wikipedia.org/wiki/Zeno's_paradoxes#Dichotomy_paradox)? I (u/lonelyroom-eklaghor) am planning to keep something like diminishing returns, much like that Dichotomy paradox. This particular idea of mine is unknowingly influenced by a bit of a psychology too.

First of all, what is that paradox? Say, from Point A to B (1 unit length, you travel half the distance. From that half, you travel half the distance (1/4 + 1/2 = 3/4 or 0.75). From there, 1/8 added, we get 7/8. But we never reach 1.

How has this been used here? We assume that once the system hits 0.99 points, it directly goes to 1, thereby breaking the asymptotic flow altogether. When it goes to 1, limit reached and the automod 'moves on' with the post. No more increments for that post, sorry. But if only 1 award has been given, half of the barrier has passed, because the first achievement is always the hardest. From then, it just goes to "the ocean is thirsty" mode, so we just put a stop altogether when it reaches .99-something points: we just increase it to 1.

From the perspective of psychology (not physics/kinematics), it is in my personal opinion that Zeno's Dichotomy Paradox isn't a paradox, it's a reality. Increasing 1 lion among 99 lions DOESN'T INCREASE the problematic factor much, whereas adding one lion to another lion INCREASES the problematic factor much more THAN BEFORE. 

In case of achievements, as said before, getting the first award is the hardest. That's why I literally claim, "You've done half of the work already." This will give incentives to people for even giving less amount of posts.