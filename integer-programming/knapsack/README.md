# Knapsack Problem

Knapsack problem can take different forms depending on if the variables
are binary or integer. The binary version means that there is only one
item of each item type that can be taken. This is typically illustrated
as a backpack (knapsack) and some items to put into it (see ), but has
applications in many contexts.
\(a,c \in \mathbb{Q}^n_+\), \(b \in \mathbb{Q}\), then the Binary
Knapsack probem is
Given an non-negative weight vector $$a \in \mathbb{Q}^n_+$$, a capacity
$b \in \mathbb{Q}_+$, and objective coefficients $c \in \mathbb{Q}^n$,
$$\begin{split}
\max \ \ & c^\top x\\
\text{s.t.}\ \ & a^\top x \leq b\\
& x \in \{0,1\}^n
\end{split}$$


Given an non-negative weight vector \(a \in \mathbb{Q}^n_+\), a capacity
\(b \in \mathbb{Q}_+\), and objective coefficients
\(c \in \mathbb{Q}^n\), \[\begin{split}
\max \ \ & c^\top x\\
\text{s.t.}\ \ & a^\top x \leq b\\
& x \in \{0,1\}^n
\end{split}\]

The knapsack problem can take different forms depending on if the variables are binary or integer.  The binary version means that there is only one item of each item type that can be taken.  This is typically illustrated as a backpack (knapsack) and some items to put into it (see  \autoref{fig:wiki/File/knapsack}), but has applications in many contexts.    This problem can be phrased as the following mathematical optimization problem:

Given an non-negative weight vector $$a \in Q^n_+$$, a capacity $$b \in Q_+$$, and objective coefficients $$c \in Q^n$$, 

$$ \max     c^\top x$$
s.t.  $$ a^\top x \leq b$$
$$ x \in \{0,1\}^n$$


For example, consider the image:

Which items should we choose take in the knapsack that maximizes the value while respecting the 15kg weight limit?


This can be modeled in the following way:



 You have a knapsack (bag) that can only hold W = 15 kgs.  There are 5 items that you could possibly put into your knapsack.  The items (weight, value) are given as:
(12 kg, $\$$4), (2 kg, $\$$2), (1kg, $\$$2), (1kg, $\$$1), (4kg, $\$$10).  Which items should you take to maximize your value in the knapsack? See \autoref{fig:wiki/File/knapsack}.\\

\noindent \textbf{Variables:}
\begin{itemize}
\item let $x_i = 0$ if item $i$ is in the bag
\item let $x_i = 1$ if item $i$ is not in the bag
\end{itemize}
\textbf{Model:}
\begin{equation}
\begin{split}
\max  \  \ &4 x_1 + 2 x_2 + 2 x_3 + 1 x_4 + 10 x_5\\
\text{ s.t. }\ \ &  12 x_1 + 2 x_2 + 1 x_3 + 1 x_4 + 4 x_5 \leq 15\\
& x_i \in \{0,1\} \text{ for } i=1, \dots, 5
\end{split}
\end{equation}
\end{examplewithcode}
In the integer case, we typically require the variables to be non-negative integers, hence we use the notation $x \in \Z^n_+$.  This setting reflects the fact that instead of single individual items, you have item types of which you can take as many of each type as you like that meets the constraint.
\begin{general}{Integer Knapsack Problem}{\npcomplete}
Given an non-negative weight vector $a \in \Q^n_+$, a capacity $b \in \Q_+$, and objective coefficients $c \in \Q^n$, 
\begin{equation
