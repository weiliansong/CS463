# Prolog Family Assignment #

## What's here ##
Within this directory are 5 files.
1. `database.pl` : geneological database, where only child relations and ages
   are defined.
2. `rules.pl` : predicates to determine various family relations.
3. `main.pl` : sanity script that outputs knowledge base in a neat format.
4. `family_tree.png` : the family tree visualized.
5. `output.txt` : output of `main.pl` just in case if it can't run.

## How To Run ##
Simply type `swipl -l main.pl` to print out knowledge base.

## Learning Outcome ##
So this assignment is interesting mostly because of the new programming
language I have to use. Heck it ain't even a full programming language, as its
functionality is primitive compared to other more familiar ones like C, Java,
Python, etc. But with less functionalities mean that we have to find clever
ways to accomplish what we want, and it is very surprising how concise my code
is after I thought through the basic rules of satisfiability. I most likely
won't be using Prolog anytime again, but it is certainly an interesting
language and I have a special respect for those who have mastered it.

Having used Prolog, I think I can program prettier code by limiting myself
with the number of external libraries I am allowed to use. This way I am less
relied on outside sources and can fully utilize the power of the programming
language I'm using.

## Acknowledgements ##
I would like to thank Thomas Deeter for providing a template script for us to
test our custom predicates.

I would like to thank Edwin Gogzheyang for discussing with me about family
relations in general, like what does it mean to be nth cousin k time removed.

Lastly I would like to thank user3633383 on Stack Overflow for giving me hints
on how to implement the cousin() predicate. Full link to post is: https://stackoverflow.com/questions/30497704/prolog-general-rule-for-finding-cousins-etc. I did not borrow the concept of nth cousin from the post, as I didn't understand it.
