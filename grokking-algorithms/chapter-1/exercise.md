# Chapter-1 Exercises

1.1 Suppose you have a sorted list of 128 names, and you’re searching through it using binary search. What’s the maximum number of steps it would take?
    let's calculate logx = 128, and 2^7 = 128, so the maximum number of steps is 7.

1.2 Suppose you double the size of the list. What’s the maximum number of steps now?
    let's calculate logx = 256, and 2^8 = 256, so the maximum number of steps is 8.

Give the run time for each of these scenarios in terms of Big O.
1.3 You have a name, and you want to find the person’s phone number in the phone book.
    if the phone book is sorted, then the run time is O(log n), otherwise it is O(n).

1.4 You have a phone number, and you want to find the person’s name in the phone book. (Hint: You’ll have to search through the whole book!)
    O(n)

1.5 You want to read the numbers of every person in the phone book.
    O(n)

1.6 You want to read the numbers of just the As. (This is a tricky one! It involves concepts that are covered more in chapter 4. Read the answer—you may be surprised!)
    If we assume that the phone book is sorted by last name, then we can use binary search to find the first entry with last name starting with "A". Then, we can iterate through the entries until we reach the first entry whose last name does not start with "A".
    The time complexity for binary search is O(log n), where n is the number of entries in the phone book. The worst case scenario is that all the entries have last names starting with "A", so we need to iterate through all n entries, which takes O(n) time. Therefore, the overall time complexity is O(log n + n) = O(n).

