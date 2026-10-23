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
| 306 | Medium | Math | Okay problem, just brute force |
| 895 | Hard | Heap | Use a max heap to keep track of the most frequent element, using the number of calls as a secondary index (note its not the length of the stack as the stack length can shrink to uncover something from before, but in reality a newer value was added first just with smaller or equal to length). A max heap works because it gives us the element with the largest frequency and we note that stale values are kept in teh heap because that was the most frequent at that time (i.e. if 5 has a freq of 3 and is popped, then the 5 with freq 2 at calls maybe like 2 will come to the top which is expected) |
| 795 | Medium | Two Pointer | Should do an atMost solution (count the number of subarrays with atmost _ maximum sum), then subtract atMost(right) - atMost(left-1) |
| 2251 | Hard | Intervals | Use a heap to keep track of minimum end time seen, add to the heap when start time is less than current person's visit |
| 1293 | Hard | BFS | Think through teh question first, note that this is most likely going to be BFS (with some variation of dp), because it's not directed so a visited list must exist. This comes in the form of something like "best" array. DP would work, we would just need to keep track of visited with some backtracking |
| 778 | Hard | Dijkstra's | 1. **DP:** Use DP when the problem has reusable states with a natural ordering / DAG structure, so each state can be computed from previously solved states without problematic cycles.<br><br>2. **BFS:** Use BFS for shortest-path problems where every move/edge has the same cost (usually `1`), so the first time you reach a state is optimal.<br><br>3. **Dijkstra:** Use Dijkstra for shortest-path/minimum-cost problems where edges or transitions have different **non-negative costs**, so you prioritize the currently cheapest state. |
| 2096 | Medium | DFS | Watch the memory limits with strings, other than that what we can essentially do is populate an ARRAY with the current path (using backtracking), we get the path to the start and to the destination. Then we see how many of their levels match (i.e they are going the same way), after wards, we move up so that the start value is at the shared level, then continue with the instructions to get to the destination. |
| 2131 | Medium | Hash Table | Break this down into manageable parts. There are three cases essentially: The mirror word appears in the given words. The mirror word is different than current word so we can put it in any order in a valid palindrome, hence max_length += 4 * min(word_set[reverse], word_set[word]). Otherwise, if we have a two-letter, we note it will be unpaired, but we can squeeze it in the middle somewhere (as it's the same as it's mirror) => hence this unpaired gets added later and is another case. The final case is the same as the original one |
| 198 | Medium | DP | Basic Dp |
| 1146 | Medium | Binary Search | Refresh on the binary search algorithm using bisect (bisect_left, bisect_right), this is perfect for finding the index just make sure know how to use. Other than that for this q in specific make sure that for each index that the snapshots don't have multiple entries at the same snap_id |
| 845 | Medium | Two Pointer | One pass solution in O(1) is so annoying to reason about, just need to think it through. For an interview, the better solution is to use left and right arrays to indicate the length of a strictly increasing seq at each i. |
| 900 | Medium | Counting | Just don't unload the entire array and try to process n, just process the encoding one at a time using a while loop and based on index amount |
| 8 | Medium | Brute Force | Tokenization, just think carefully before doing the problem, thats honestly all |
| 438 | Medium | Sliding Window | Make sure not to repeatedly build the anagram's frequency map and instead just add or subtract by one |
| 1928 | Hard | Dijkstras | Use a memoized state of (fee, time), only add if we see either a smaller fee or smaller time. To improve this space complexity what we can do is see if the current time is greater than the minimum time we saw for this node (once a node has been processed, it must mean it has smaller cost, so if it also has smaller time then minTime we can use to knock out anything else. WOrks on the same premise as below, only process nodes where either the cost is smaller or the time is smaller |
| 213 | Medium | DP | Either rob first house or dont rob last |
| 162 | Medium | Binary Search | Adjacent elements can not be equal too each other so this is pretty straightforward |
| 2468 | Hard | Design | Watch the log issues, convert to string instead of log (honestly general advice, lots of mishaps have t round otherwise) |
| 173 | Medium | DFS | In Order Traversal |
| 1641 | Medium | DP | track number of vowels |
| 2785 | Medium | Brute Force | Straightforward solution |
| 1419 | Medium | Counting | Just remember we keep track f which frog is at what stage, but also the total number of frogs we see (corresponds to the number of "C's" that have not reached "K") |
| 2512 | Medium | Sorting | Easy |
| 3727 | Medium | Two Pointer | straightforward |
| 847 | Hard | Bitmask | Standard bitmask problem, rmemeber no dp cuz undirected graph allows for cycles. DP ON DAGS |
| 3659 | Medium | Math | Focus on highest frequency number |
| 23 | Hard | Linked List | pre simple, could alternatively sort, but prolly best to do it using heap yk |
| 124 | Hard | DFS | Just remember kadanes algo + path sum means we cna on;y take from left or right |
| 239 | Hard | Monotonic Queue | Heap sol works, but queue is faster becuase it preserves index order and maximal number |
| 200 | Medium | DFS | Might be easiest dfs ever |
| 295 | Hard | Heap | Split into lower half and upper half and keep balancing |
| 2044 | Medium | DP | Just remember the correct dp state and what to do for treating things outside the bounds (dont be stupid) |
| 84 | Hard | Monotonic Stack | Need to think hard about this question tbh, important to note that we want a monotnically increasing stack, for every height smaller we can basically extend to whatever index the height we popped can extend to (as everything must be less than current height) |
| 1466 | Medium | DFS | Just remember that flipping means we can go from a to b but we wanna go from b to a so we flip then |
| 3815 | Medium | Heap | Lazy deletion |
| 150 | Medium | Stack | Straightfoward when you consider stack |
| 560 | Medium | Hash Table | REMEMBER, no sliding window because invairant does not hold, we have negative numbers so if we move forward by one and sliding window is not true then we might be able to move foreawrd one more and it is true, no invariant that once its false its alwayss false. |
| 2034 | Medium | Heap | Lazy Deletion with heap |
| 996 | Hard | Backtracking | Keep track of frequency as duplicates can cause stack to explode and they're all treated the same, note that preventing. We could use a bitmask and keep track of order when nodes are seen |
| 921 | Medium | Stack | Pop whatever works, append whatever doesnt |
| 287 | Medium | Linked List | Tortoise + hare |
| 765 | Hard | Union Find | We want to find for a particular value, how many couples are involved in that couple needing to sit together (i.e people paried with the couple). We can then find out how many unique couples that is and subtract by 1for the number of swaps to get in the correct order. To do this, we can use union find, find the size of each group //2 (because we need couple count) and usbtract by one |
| 3941 | Medium | Brute Force | Might be the easiest problem on LC |
| 1169 | Medium | Brute Force | Just remember the detials |
| 3551 | Medium | Brute Force | (REVIST) Think hard about the problem, its easy but need to think through swapping problem |
| 2171 | Medium | Prefix Sum | Prefix Sum + Sorting, not a hard problem at all, just think carefully about the problem, Really not sur ehow i didnt one shot so REVISIT |
| 2192 | Medium | Graph Theory | Topological Sort q pre straight forward, just read q description and reqs |
| 2734 | Medium | Brute Force | Simple |
| 3686 | Hard | DP | Just don't forget about the None/0 checks default behaviour and also make sure to add mod before final result |
| 3148 | Medium | DP | Watch the move condition, just use float("-inf") and then kadanes after |
| 1792 | Medium | Heap | Notice we want to keep track of some order of classes, in this case we want to add one to the class with the greatest BENEFIT! |



