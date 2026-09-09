# LC-Sols
| Problem Number | Difficulty | Type         | Notes                                                                 |
|----------------|------------|--------------|-----------------------------------------------------------------------|
| 236            | Medium     | DFS          | Watch out for global variable mutation                                |
| 212            | Hard       | Backtracking | Consider case where multiple words appear from same suffix, no premature returns |
| 3169           | Medium (contest)       | DFS | Pretty easy problem, make sure you sort meeting dates correctly |
| 229            | Medium     | Hash | Easy |
| 2375           | Medium     | Backtracking | Backtrack through, keeping a set of possible integers |
| 1079           | Medium     | Backtracking | Backtrack permutations
| 1291           | Medium     | Tree, Design | Remember tree unique indexing (calculating distance between nodes, odd and even indexing) |
| 22             | Medium     | DP, backtrack | encode valid paranthesis into backtrack |
| 62             | Medium     | DP | Remember base cases and edge cases|
| 63             | Medium     | DP| Think about edge cases and bases cases (some stupid ones like if the obstacle is on the first square return 0) also remember summing 2d arr |
| 64             | Medium     | DP| Think about edge cases and bases cases (some stupid ones like if the obstacle is on the first square return 0) also remember summing 2d arr |
|55              | Medium     | DP| Decievingly Greedy problem, simple O(n) solution exists, DP sol to slow|
|2222             | Medium     | Greedy| Keep track of 0,1,01,10,101,010 --> greedy solution is devious 
|983             |Medium| DP| Make sure you understand the problem, logic is not difficult, make sure you start at right day and index correctly|
|2140           |Medium| DP| (Revisit) Bag pull -- went deep in my bag for this, always remember that DP can also reverse the list and use those indices to maintain bottom up|
|1035           |Medium| DP| (Revisit) Longest common subsequence, but with uncrossed lines. If both numbers at the end are equal then continue, else take one letter off and repeat...|
|712           |Medium| DP| (Revisit) REMEMBER INDICES FOR TWO SEQUENCE QUESTIONS, longer string must have enough array buckets to store answer, otherwise intuitive|
|931           |Medium| DP| Grid DP|
| 9 | Easy | Brute Force | Testing |
| 4 | Hard | Binary Search | Binary Searching based on halfway splits of arrays (logcially O(log(m+n)). Remember arrays are sorted, and an arbitrary index should split one of the arrays (whichever is smaller than combined indexes). Remmber the search index should shrink if we remove the top half of an array). |
| 2240 | Medium | Math | Not as challenging as it appears, remember that there are only two costs (like that CCC problem), so as we increment one we can do O(1) ops to get the other. |
| 3876 | Medium | Math | Consider the minimum of the array, given it can't be changed, then determine a pattern based on that |
| 1329 | Medium | Brute Force | Read question properly, sorting on a diagonal will require a new array. Look at heap solutions |
| 3159 | Medium | Hash Table | Straightforward Problem, Keep Track of X's appearances in the array. |
| 304 | Medium | Math | Not Intuitive, O(mn) one time pass works uisng column, but make sure to watch edge cases for the sum. Core idea is to construct prefix sum with the (0,0) corner and calculate based on that. |
| 2581 | Hard | DFS | No need for DP, one-pass is enough to compute the number of roots at 0. From there, we can make a super quick idstinction for the neighbours (+1 if (neighbour, root) in guess set, -1 if (root, neighbour) was in guess set) |
| 2761 | Medium | Math | Sieve Modified, solve in One-pass |
| 3618 | Medium | Math | Simple, just use Sieve |
| 1642 | Medium | Heap | Not so intuitive heap solution, important to break down the problem here. A ladder essentially means how many array entries can I skip before I need to count bricks (or diff between curr and next).  The important distinction, the entries wwe want to skip are the largest ones so we need a heao wich basically tells us which to use ladders on -- the k (or loadders) largest elements |
| 3761 | Medium | Hash Table | Keep track of previously seen reversed, just make sure that reversing the num is done properly |
| 1761 | Hard | DFS | Compute trios, the important distinction is to consider the direction of the nodes. We should orient the graph such that we only consider the direction where we go from lower nodes to greater nodes. This avoids recomputation (given we only need ot process one direction), and minimizes the amount fo times we need to loop (i.e. we are always processing the node with the least amount of degree first, for any edge) |
| 3904 | Medium | Two Pointer | Simple Problem, just keep track of mins and maxes on left,right sides |
| 1048 | Medium | DP | Read the question, nothing difficult, lenient time complexity |
| 402 | Medium | Monotonic Stack | The monotonic stack works here (similar to how a  heap works essentially), basically we want to remove the largest elements from the start, hence a monotonic stack implies the order is always ascending and if optimally removed, the smallest number will be ascedning order. |
| 2707 | Medium | DP | Super Simple DP state (blaming it on being tired), basically we note that the extra characters from substring[i:] should hold  since we processes smaller words earlier |
| 3918 | Medium | Math | Simple math problem, nothing too complicated |
| 2641 | Medium | BFS | Level-Order Traversal of the tree, keeping track of parent sum and then updating values in two passes. Used a two-pass solution, but a one-pass solution is possible by processing the NEXT LEVELs SUM first and updating the child nodes in the next level to their siblings sum. |
| 1743 | Medium | DFS | Important distinction to remember the roots of adjacent pairs must only appear once + any number can only appear at most twice. Hence, for any neighbour, we must have already proceessed one of its edges (to get to the current node), hence we just need to add the other to a stack. its basically a line. |
| 1563 | Hard | DP | PRUNE FOR MINMAX! Solution probably works in C++ with no pruning, but remember to PRUNE WHEN DOING MINMAX TREES. In this case, we know that when the answer we found is already bigger than what we are maximally trying to calculate, then we can skip (or break if we are doing it from the right) |
| 3693 | Medium | DP | Simple, just remember that costs is 1-indexed, not zero-indexed (i.e no cost at the starting step, to go from i to step n, it costs cost[n-1]) |
| 1288 | Medium | Intervals | Must sort by starting time (pretty intiutive why), but because we are looking for fully covered times, we want the largest intervals first (i.e ascending start time, and descing ending time). This is because these are the largest intervals. After that just stack |
| 2645 | Medium | Greedy | Essentially, we can go by every substring ("abc", "ab", "bc", "ca") and count how many characters needed to be added to those strings (with some intersection math). For example, if we have one occurance of a bc (seperate not inside an abc), we need to add a character to make it into the entire string. This keeps character additions down to a minimum as the string must be ordered and seperate, so everything is on its own |
| 1209 | Medium | Stack | use a stack to keep track of letters seen, pop when k duplicate letters are seen (this basically collapses the stack to always have the duplciaation check up to date). |
| 1519 | Medium | DFS | Two-pass solution (store freq and then use that freq map to get the label frequency works). A one-pass solution is more clean though (simply propogating the frequency map up and using it to store answer then, given thats the subtree count). Akin to a dp pproblem |
| 3746 | Medium | Stack | Stack Problem, pre basic because they concatenate after being removed |
| 3112 | Medium | Dijkstras | Straightforward Dijkstras, just refresh on syntax and process disappearances in alg |
| 4039 | Medium | Math | Make sure to keep total_sum bounded by not only calculating the power bounded (pow(x, y, MOD)), but also making sure to bound the addition (i.e the final result) |
| 940 | Hard | DP | (REVISIT) Top down solution is mainly intiutive, similar to what we see in that we don't want to reprocess subsequences that start with a character we will see. There's also a good amount of math in here, just remember the +1 accounts for the current character in the subseq |
| 3871 | Medium | Math | Bounded Problem (lower bound and upper bound for number of commas) |
| 3649 | Medium | Two Pointer | Simplify the identity, from which we then use a two pointer approach. We note that if some [a,b] in the abs value sorted array doesn't work, then [a, b+1] can never work,  because b - a > a. so (b+1)-a > a. We only care about the lower bound as upper bound always true |
