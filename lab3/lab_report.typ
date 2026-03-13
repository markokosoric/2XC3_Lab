#set page(
  paper: "a4",
  margin: (x: 1.25in, y: 1.25in),
)

#set text(
  font: "New Computer Modern",
  size: 11pt,
)



#align(center)[
  #text(size: 2em, weight: "bold")[Lab Report: Sorting Algorithms Analysis]

  #v(1em)

  #text(size: 1.5em)[2XC3 Lab 1]

  #v(1em)

  #text(size: 1.2em)[Marko Kosoric, Patrick]

  #v(1em)

  #text(size: 1em)[February 1, 2026]
]

#pagebreak()

#outline()

#outline(title: "Figures", target: figure.where(kind: image))
#outline(title: "Tables", target: figure.where(kind: table))

#pagebreak()

= Executive Summary


#show figure.where(
  kind: image,
): set figure.caption(position: top)
#show figure.where(
  kind: table,
): set figure.caption(position: top)



#pagebreak()

= Part 1


== Expirement 1

Random lists of length 10,000 were generated. Each list was used to make a Binary Search Tree and a Red-Black Tree using the same insertion order. After building both trees, the difference

$ "BST height" - "RBT height" $

was calculated. This process was repeated 10,000, and the average difference

$ ("BST height" - "RBT height") / n $

was measured.

For lists of length 10,000, the average difference was 15.196. This shows that binary search trees are consistently taller then red-black trees when inserting a lot values in random order.

These results were expected since red-black trees are self-balancing, while binary search trees depend on the insertion order which can cause them to be very unbalanced.

However, there are cases where a binary search trees are better. BSTs are simpler to implement and do not need rotations and recoloring operations. This means when the number of inputs are smaller, BST insertions are slightly faster and can still be relatively balanced compared to the red-black tree version. This can be seen in Figure 1

#figure(
  image("experiment_0_graph.png"),
  caption: [
    Plot of Average height of BSTs and RBTs on Varying Node Sizes
  ],
)

== Expiremnt 2

Random lists of length 50 were generated 10,000 times per run. Each run the list would become more unsorted by performing an increasing number of random swaps (swaps = [0,1,2,3,4,5,10,25,50,100]). The modified list was then inserted into both a BST and RBT and the height difference

$ ("BST height" - "RBT height") / n $

was measured. The resulting graph plots number of swaps on the x-axis and average difference on the y-axis.

#figure(
  image("experiment_2_graph.png"),
  caption: [
    Plot of Average Difference in height between BSTs and RBTs on Varying Amounts of Random Swaps
  ],
)

When the list was perfectly sorted (0 swaps), the BST became very unbalanced and produced the largest height difference compared to the red-black tree. As the list became less sorted (\# swaps increased), the difference in height decreased closer to 1.

The results were expected because BSTs performance highly depends on input order. With a sorted list, the BST becomes similar to a linked list causing a big height. In contrast, the RBT's performance stays similar regardless of input order. As the list becomes less sorted, the BST structure becomes more balanced because the order of values are more random.

#pagebreak()
= Part 2
== Experiment 3
A X3Tree was generated for all degrees $i in NN_0$ where $0 <= i <= 25$. The
height of the tree was recorded. Since X3Tree generation is deterministic, only
one tree was generated for each degree.

#figure(
  grid(
    columns: 2, gutter: 4em,
    table(
      columns: 2,
      stroke: none, column-gutter: 1em, row-gutter: -0.1em,
      [*Degree*], [*Height*],
      table.hline(),
      [0], [1],
      [1], [2],
      [2], [2],
      [3], [3],
      [4], [3],
      [5], [4],
      [6], [4],
      [7], [5],
      [8], [5],
      [9], [6],
      [10], [6],
      [11], [7],
      [12], [7],
    ),
    table(
      columns: 2,
      stroke: none, column-gutter: 1em, row-gutter: -0.1em,
      [*Degree*], [*Nodes*],
      table.hline(),
      [13], [8],
      [14], [8],
      [15], [9],
      [16], [9],
      [17], [10],
      [18], [10],
      [19], [11],
      [20], [11],
      [21], [12],
      [22], [12],
      [23], [13],
      [24], [13],
      [25], [14],
    )
  ), caption: [
    Height of XC3 vs Degree
  ]
)

For every increase of two to a X3Tree's degree, the height increases by one.
This is because the height of a X3Tree of degree $i$ is one plus the maximum
height of the children, and the child with the maximum height is the $(i-2)$.

Therefore, we have the recurrence relation
$
  h(i) = 1 + h(i-2)
$
Since the degree 0 X3Tree has height 1 and the degree 1 X3Tree has height 2, the
recurrence relation has solution
$
  h(i) = ceil(i/2) + 1
$
== Experiment 4
A X3Tree was generated for all degrees $i in NN_0$ where $0 <= i <= 25$. The
number of nodes in the tree was recorded. Since X3Tree generation is
deterministic, only one tree was generated for each degree.

#figure(
  grid(
    columns: 2, gutter: 4em,
    table(
      columns: 2,
      stroke: none, column-gutter: 1em, row-gutter: -0.1em,
      [*Degree*], [*Nodes*],
      table.hline(),
      [0], [1],
      [1], [2],
      [2], [3],
      [3], [5],
      [4], [8],
      [5], [13],
      [6], [21],
      [7], [34],
      [8], [55],
      [9], [89],
      [10], [144],
      [11], [233],
      [12], [377],
    ),
    table(
      columns: 2,
      stroke: none, column-gutter: 1em, row-gutter: -0.1em,
      [*Degree*], [*Nodes*],
      table.hline(),
      [13], [610],
      [14], [987],
      [15], [1597],
      [16], [2584],
      [17], [4181],
      [18], [6765],
      [19], [10946],
      [20], [17711],
      [21], [28657],
      [22], [46368],
      [23], [75025],
      [24], [121393],
      [25], [196418],
    )
  ), caption: [
    Number of nodes in a XC3 vs Degree
  ]
)

The results show that the number of nodes for a tree of degree $i$ is the
Fibonacci number $F_(i+2)$. This is because the child with degree $i-4$ has
$F_(i)$ nodes and the sum of other nodes is equal to $F_(i-3) - 1$, therefore the
sum of all nodes is $F_(i-2)$

It is known that the sum of all Fibonacci numbers up to $n$ is equal to one less
than the $(n+2)$th Fibonacci number.
$
  sum_(i=1)^n F_i = F_(n+2) - 1
$

Since the sum of all nodes is
$
  "Nodes"(n) & = 1 + sum_(i = -1)^(n-2) "Nodes"(c) \
             & = 1 + sum_(i=1)^n F_i               & "Inductive hypothesis" \
             & = 1 + F_(i+2) - 1                   &   "Fibonacci Identity" \
             & = F_(i+2)
$
Since the base case is also fulfilled, the number of nodes in a degree $n$
X3Tree is $F_(n+2)$


=== Complexity bound on height
Since the height increases linearly with respect to degree and the number of
nodes increases exponentially with respect to degree (since Fibonacci numbers
grow at a rate of $phi^n$), height effectively has the
same complexity of degree. Therefore the complexity of number of nodes with
respect to height is exponential. Inverting this relation gives that complexity
of height with respect to number of nodes is base-$phi$-logarithmic. Since all logarithmic
complexities are the same, $h(n)$ can be said to be in $O(log(n))$.

For a more rigorous argument, Let $n$ denote the number of nodes, $d$ denote the
degree, and $h$ denote the height. From the previous analysis,
$
  n(d) &= "Fib"(d) \
  h(d) &= ceil(d/2) + 1
$
The height of a tree with respect to the number of nodes is given by the
composition
$
  n(d) &= F(d) \
  d(n) &= F^(-1)(n) \
  h(d) &= G(d) \
  h(n) &= G thick circle.small thick F^(-1) \
  &=   (ceil(("Fib"^(-1)(n))/2) + 1)
$
Using the closed form for $"Fib"(n)$
$
  "Fib"(n) &= (phi^n + psi^n)/sqrt(5) \
  &approx phi^n/sqrt(5) &wide "for large" n
$
Therefore
$
  "Fib"^(-1)(n) = sqrt(5) log_phi (n) wide "for large" n
$
Thus
$
  h(n) 
  &= ceil(("Fib"^(-1)(n))/2) + 1 \
  &= ceil((sqrt(5) log_phi (n))/2) + 1 \
  &approx (sqrt(5))/2 log_phi (n) + 1
$
Therefore $h(n) in O(log_phi (n)) tilde.equiv O(log (n))$

#pagebreak()

= Appendix: Code Navigation


