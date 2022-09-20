# what-to-eat-next-week
Ever failed to come up with a reasonable grocery list in a reasonable time, because you failed to think of something good to eat? Here's your solution (I hope)

# Idea

Create a list of all dishes you like, maybe with some cool CLI support. Then all dishes will be fetched internally and brought in some random order. This order will now be iterated to offer N dishes, with no repeat of major dish parts (such as _mashed potatoes_) inside of K days. This can be further improved by a) remembering the dishes of the previous time span and b) providing wishes to incorporate in the plan.
The _algorithm_ will be designed like this:

- Fetch all known dishes
- Shuffle order
  - Fetch next dish
  - Repeat of major part occurs?
  - If not add to plan otherwise discard
  - Is number of N dishes reached?
  - If not go to _Fetch_ step otherwise go to finish
- Finish by listing dishes and additionally list all ingredients

