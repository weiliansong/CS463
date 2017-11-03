age(aaron, 40).
age(captain, 30).
age(eagle, 32).
age(goodman, 34).
age(ian, 20).
age(konan, 23).
age(munich, 25).
age(norway, 10).
age(austin, 22).
age(andrew, 11).
age(zach, 1).

age(becky, 41).
age(diana, 31).
age(french, 33).
age(helen, 35).
age(jane, 21).
age(lynn, 24).
age(pam, 12).
age(tiffany, 13).

/* First row */
child(diana, aaron).
child(diana, becky).
child(eagle, aaron).
child(eagle, becky).
child(goodman, aaron).
child(goodman, becky).

/* Second row */
child(jane, captain).
child(jane, diana).
child(austin, captain).
child(austin, diana).
child(konan, eagle).
child(konan, french).
child(munich, goodman).
child(munich, helen).

/* Third row */
child(norway, ian).
child(norway, jane).
child(pam, konan).
child(pam, lynn).
child(andrew, konan).
child(andrew, lynn).

/* Fourth row */
child(zach, norway).
child(zach, tiffany).
