## UnionFind

UnionFind is a set of two operations that are a part of a well known and general problem. Namely, the problem of *Dynamic-Connectivity*. Simply stated, this problem is: given a set of N objects and the two commands (Find and Union) maintain an undirected graph G so that edges may be inserted and deleted and connectivity queries may be answered efficiently. 

There are a number of methods for solving this problem: 

### Quickfind

Store an array of size N where the indices store some arbitrary integer id that represents a connected component (group) i.e. if nodes 1 and 2 are connected then they both might have the integer 7 to show they are in the same connected component.  To perform a Find, we can then simply compare the values at two indices to see if they are in the same connected component. However, to perform a Union we must change all the nodes in one connected component to the id of another. 



### Quickunion

Store the root of node N at index N in an array of size N. Hence, we can perform a Union by simply setting the root of one connected component to another.  However to do a find we must trace all the routes to see if they are in the same connected component, which gives much worse properties for Find. 



