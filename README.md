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
