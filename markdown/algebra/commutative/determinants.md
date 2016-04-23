Title: Determinants of Matrices over Commutative Rings
Date: 2015-05-16
Category: Algebra/Commutative Rings
Tags: Matrices, Determinants, Leibniz Expansion, Laplace Expansion, Cramer's Rule, Multiplication Theorem, Cofactors, Adjugate, Inverse Matrix, Solution of Linear Equations
Slug: determinants-over-commutative-rings

[TOC]

###Introduction
---------------

<!-- PELICAN_BEGIN_SUMMARY -->
Let $R$ be a commutative ring. Fix an integer $n \geq 1$. Let $\mathbf{A} = (a_{ij})$ be the $n \times n$ square matrix

$$\begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{pmatrix}$$

with entry $a_{ij}\in R$ and $1 \leq i,j \leq n$ is at the intersection of the $i^\mathrm{th}$ row and $j^\mathrm{th}$ column. 
We will define a function $\det(\mathbf{A}) =\det (a_{ij})$ of this matrix $\mathbf{A}$, which will also
be denoted by 

$$\begin{vmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{vmatrix}$$

We will also state and prove the various familiar properties of the determinant in this setting.
<!-- PELICAN_END_SUMMARY -->

The approach we follow is Emil Artin's, based on his book *Galois Theory*. He bases everything over fields. A rewriting of the
arguments to the setting of commutative rings was already done for example by S. Lang in his *Algebra*; but we follow Artin's 
original more closely. Gian Carlo Rota [criticizes](http://www.princeton.edu/~mudd/finding_aids/mathoral/pmcxrota.htm) 
Artin's proofs that they are *perfect but not enlightening*, and so the reader is urged to make sure that he really absorbs 
the proof if required in repeated readings.

--------
### Axiomatic Definition
--------

First, a note. 
We write a matrix $\mathbf{A}$ also as $(\mathbf{a}_1, \mathbf{a}_2, \ldots , \mathbf{a}_n)$, where $$\mathbf{a}_j = \begin{pmatrix} a_{1j} \\ a_{2j} \\ \vdots \\ a_{ij} \\ \vdots \\ a_{nj}\end{pmatrix}$$ is a column vector, in this case the $j^\mathrm{th}$ column of $\mathbf{A}$.

Thus the determinant $\det(\mathbf{A})$ also written as $\det(\mathbf{a}_1, \mathbf{a}_2, \ldots , \mathbf{a}_n)$,

For further development, we first take an axiomatic approach first and prove the existence later.

**Definition**. A function $\det$ of the column vectors is called a determinant if it satisfies the following conditions.

1. $\det$ is linear when viewed as a function $D_j$ of a particular column $\mathbf{a}_j$, i. e., $$\begin{equation}D_j(r\mathbf{a}_j + \mathbf{a}^\prime_j) = r.D_j(\mathbf{a}_j) + D_j(\mathbf{a}^\prime_j)\label{eq:detlinear} \end{equation}$$ where $r \in R$ is a scalar.
2. If adjacent columns $\mathbf{a}_j = \mathbf{a}_{j+1}$, then $\det(\mathbf{A}) = 0$.
3. Let $\mathbf{a}_j$ be given by the Kronecker delta, i. e., $a_{ij} = 1$ if $i =j$ and $0$ if $i \neq j$. Then, $\det(\mathbf{A})=1$.

We now derive consequences of these axioms, and as part, uniqueness of the determinant(if it exists).

-------------
###Properties of determinants
-------------

1. Determinant is zero if a column is zero. 
  
    * To see this, put $\mathbf{a}^\prime_j = 0$ and $r = 0$ in equation \eqref{eq:detlinear}.

2. Determinant does not change if a scalar multiple of one column is added to an adjacent one. 
  
    * From linearity, $D_j(\mathbf{a}_j + r\mathbf{a}_{j+1}) = D(\mathbf{a}_j) + rD(\mathbf{a}_{j+1})$ and from axiom 2, we have $D_j(\mathbf{a}_{j+1}) = 0$.

3. Determinant changes sign if two adjacent columns are exchanged. 

    * Let columns $j, j+1$ be $\mathbf{a}_j$ and $\mathbf{a}_{j+1}$ respectively. Add column $j$ to column $j+1$. 
    * Now subtract column $j+1$ from column $j$. Then add column $j$ to column $j+1$.
    * The $j^\mathrm{th}$ and $(j+1)^\mathrm{th}$ columns are now $-\mathbf{a}_{j+1}$ and $\mathbf{a}_j$ respectively. The $-$ sign
    can be taken outside determinant by linearity.

4. Determinant vanishes if any two columns are equal.

    * Make the columns adjacent via repeated exchange of adjacent matrices, in which only the sign of determinant changes.
    * Subtract one column from the other. By axiom 2., the determinant vanishes.

5. Determinant is invariant when a scalar multiple of a column is added to any other column.

    * Make the columns adjacent via repeated exchange of adjacent matrices, in which only the sign of determinant changes.
    * By property **2**, adding does not change determinant.
    * Now perform in reverse order all the previous exchanges of adjacent columns. Any sign change is cancelled out.

6. Determinant changes sign if any two columns are exhanged.

    * Similar to the above argument, use property **3**.

7. Let $\sigma$ be a permutation of $\{ 1, 2, \ldots , n \}$. Let $\mathrm{sgn}(\sigma)$ denote the sign of the permutation $\sigma$. Then, 
$$\begin{equation}\det(\mathbf{a}_{\sigma(1)}, \mathbf{a}_{\sigma(2)}, \ldots , \mathbf{a}_{\sigma(n)} = \mathrm{sgn}(\sigma) \det(\mathbf{a}_1, \mathbf{a}_2, \ldots , \mathbf{a}_n).\end{equation}$$ 

    * This is clear from property **3** along with a $2$-cycle decomposition of the permutation $\sigma$.

-----------
###Leibniz Expansion and Multiplication Theorem
-----------

Replace $\mathbf{a}_j$ with the column vector 
$$\begin{equation}\mathbf{a}^\prime_j = b_{1j}\mathbf{a}_1 + b_{2j}\mathbf{a}_2 + \cdots + b_{kj}\mathbf{a}_k + \cdots + b_{nj}\mathbf{a}_n\label{eq:colsubn} \end{equation}$$
where $b_{ij}$ are scalars. 

Note, here the $j$ in $\mathbf{a}_j$ denotes the column of $\mathbf{A}$ and its $i^\mathrm{th}$ row
is $a_{ij}$.  Consider the $i^\mathrm{th}$ of the above expression for $\mathbf{a}^\prime_j$. We get,

$$a^\prime_{ij} = b_{1j}a_{i1} + b_{2j}a_{i2} + \cdots + b_{kj}a_{ik} + \cdots + b_{nj}a_{in}$$. 

Therefore the matrix $\mathbf{A}^\prime$ is nothing other than the matrix product $\mathbf{A}\mathbf{B}$.

Now we compute the determinant $\det(\mathbf{a}^\prime_1, \mathbf{a}^\prime_2 , \ldots , \mathbf{a}^\prime_n)$. Using axiom 1., 

$$\begin{align} \det(\mathbf{a}^\prime_1, \ldots , \mathbf{a}^\prime_n) &=  \sum_{i=1}^{n} b_{i1}\det(\mathbf{a}_i, \mathbf{a}^\prime_2 , \ldots , \mathbf{a}^\prime_n) && \text{(expanding}\ \mathbf{a}^\prime_1 \label{eq:detexp1} )\\
& = \sum_{i_1, i_2, \ldots , i_n} b_{i_1 1}b_{i_2 2}\cdots b_{i_n n} \det(\mathbf{a}_{i_1}, \mathbf{a}_{i_2} , \ldots , \mathbf{a}_{i_n}) && \text{(expanding all}\ \mathbf{a}^\prime_j \label{eq:detexp2} )\\
& = \det(\mathbf{a}_1, \mathbf{a}_2, \ldots , \mathbf{a}_n) \sum_{\sigma \in S_n} \mathrm{sgn}(\sigma) b_{\sigma(1) 1}b_{\sigma(2) 2}\cdots b_{\sigma(n) n} &&\text{(by properties 3 and 7)} \label{eq:colexp} \end{align}$$

Here $S_n$ is the group of all permutations on $n$ symbols. Commutativity of the ring $R$ was 
used in moving from equation \ref{eq:detexp1} to \ref{eq:detexp2}.

----------------------

!!! note "Verify that"
    For the statements proved so far, only the axioms (1) of linearity and (2) of vanishing determinant of matrices with equal adjacent rows, were used.

----------------------

Now, let $\mathbf{A}$ be given by the Kronecker delta and $\mathbf{a}_j$ be the corresponding unit column vectors. Therefore 
$\mathbf{a}^\prime_j = \mathbf{b}_j$, the column vector of the matrix $\mathbf{B} = (b_{ij})$. Now by equation \eqref{eq:colexp}
and by axiom (3) for determinants,

$$\begin{equation}\det(\mathbf{B}) = \sum_{\sigma \in S_n} \mathrm{sgn}(\sigma) b_{\sigma(1) 1}b_{\sigma(2) 2}\cdots b_{\sigma(n) n} \label{eq:leibexp} \end{equation}.$$

This is the Leibnitz expansion of the determinant of the matrix $\mathbf{B} = (b_{ij})$.

Plugging this back into \eqref{eq:colexp}, we get, 

$$\begin{equation}det(\mathbf{AB}) = det(\mathbf{A})\det(\mathbf{B}).\label{eq:detproduct}\end{equation}$$

This is called the multiplication theorem for the determinant.

-------------
###Uniqueness of Determinant
-------------

The Leibniz expansion shows that determinants are unique if they exist, since they must equal the right side of equation $\eqref{eq:leibexp}$.

Moreover, let $F$ be any function of the determinant satisfying the axioms (1) and (2), but not necessarily (3). 
Then, using equation \eqref{eq:colexp} which is still valid for $F$, and substituing the Leibniz expansion for $D$, 
we get:

$$F(\mathbf{a}^\prime_1, \mathbf{a}^\prime_2, \ldots , \mathbf{a}^\prime_n ) = F(\mathbf{a}_1, \mathbf{a}_2, \ldots , \mathbf{a}_n ) D(\mathbf{b}_1, \mathbf{b}_2, \ldots , \mathbf{b}_n ).$$

Letting $\mathbf{a}_j$ be equal to $\mathbf{u}_j$, the unit vectors corresponding to the Kronecker delta $\mathbf{U}$, 
this becomes:

$$\begin{equation}F(\mathbf{b}_1, \mathbf{b}_2, \ldots , \mathbf{b}_n ) = f . D(\mathbf{b}_1, \mathbf{b}_2, \ldots , \mathbf{b}_n )\label{eq:detuniq}\end{equation},$$

where $f = F(\mathbf{u}_1, \mathbf{u}_2, \ldots , \mathbf{u}_n )$ is the determinant of the Kronecker delta.

Thus, when axiom (3) is not satisfied, there will only be a possible change of a scalar factor. Therefore axiom (3) 
normalizes the determinant function.

-------------
###Determinant of Transpose
-------------

Fix two adjacent indices $i$ and $i+1$, with $0 \leq i \leq n-1$.
Now let $\mathbf{A}$ be the matrix of a row transformation defined in the following way.
Let $\mathbf{u}_j$ denote the $j^\mathrm{th}$ row of the matrix given by the Kronecker delta.

Then, let $\mathbf{a}_j = \mathbf{u}_j$ when $j \neq i, i+1$, let $ \mathbf{a}_i = \mathbf{u}_i + \mathbf{u}_{i+1}$ 
and let $\mathbf{a}_{i+1} = 0$. 

Left multiplication by $A$ replaces row $i+1$ with row $i$, not changing the other rows, and $\det(\mathbf{A}) = 0$.

Using this in the multiplication theorem \eqref{eq:detproduct}, we see that:

&nbsp; **8.** Determinant vanishes if two adjacent rows are identical. 

Each term on the right side of the Leibniz expansion \eqref{eq:leibexp} is a product with exactly one term from each 
row. Thus, as a function of each row, the determinant is linear and homogenous. Moreover, the determinant of
the matrix where the rows are given by the unit row vectors specified by the Kronecker delta, is $1$, as the 
Kronecker delta is symmetric.

Therefore, the determinant considered as a function of the row vectors satisfies all three axioms. This is equivalent
to taking the transpose, and, therefore, by uniqueness, 

&nbsp; **9.** Determinant is unchanged under transpose operation.

It follows that:

&nbsp; **10.** Determinant is zero if any two rows are identical. Determinant changes sign if any two rows are switched. 
Determinant is invariant when a scalar multiple of a row is added to another. 

Similarly, property 7 can be restated in terms of row permutations, and Leibniz expansion can be rewritten where in the
products the second index is being permuted instead of the first.


-------------
###Cofactor expansion and Existence of Determinant
-------------

We now prove the existence of determinants by induction, and using cofactor expansion.

For $n=1$, the matrix $a_{11}$ has determinant $a_{11}$.

Suppose determinants exist for $(n-1 )\times (n-1)$ matrices over $R$. Let $\mathbf{A}=(a_{ij})$
be an $n \times n$ matrix. To each element $a_{ij}$, we associate an $(n-1 )\times (n-1)$ matrix
by cancelling out the $i^\mathrm{th}$ row and $j^\mathrm{th}$ column of $\mathbf{A}$, and its
determinant is called the minor $M_{ij}$.

From the minor, the cofactor $A_{ij}$ is defined as $(-1)^{i+j}M_{ij}$.

Now fix a row $i$ and define a function $D$ as the sum of the products of row and cofactors:

$$\begin{equation}D = a_{i1} A{i1} + a_{i2}A{i2} + \cdots + a_{in}A{in}.\label{eq:cofexp}\end{equation}$$

Now fix a column $k$ and consider $D$ as a function of the $k^\mathrm{th}$ column $\mathbf{a}_k$. In the sum
in equation \eqref{eq:cofexp}, for $j \neq k$, we have the product $ a_{ij}A{ij}$ with $a_{ij}$ not
depending at all on $\mathbf{a}_k$ and the cofactor $A_{ij}$ linearly depending on each of the columns of the
$(n-1) \times (n-1)$-matrix obtained by removing the $i^\mathrm{th}$ row and $j^\mathrm{th}$ column
from $\mathbf{A}$; i. e., it depends linearly on $\mathbf{a}_k$. Similarly, when $k = j$, in the product 
$ a_{ij}A{ij}$, the first term $a_{ij}$ depends linearly on $\mathbf{a}_k$ and the second term $A{ij}$
does not depend at all on $\mathbf{a}_k$, the $k^\mathrm{th}$ row having been removed. Therefore $D$ satisfies
axiom 1 for determinants.

Now suppose two adjacent columns $k$ and $k+1$ are equal for a matrix $\mathbf{A}$. Then, $a_{i\ k} = a_{i\ k+1}$
and the minors $M_{i\ k} =  M_{i\ k+1}$, but the cofactor $A_{i\ k} = - A_{i\ k+1}$, so we obtain $D = 0$ in 
equation \eqref{eq:cofexp}. Therefore $D$ satisfies axiom 2 for determinants.

Setting $\mathbf{A}$ equal to a unit matrix and explicitly computing, we see that $\det (\mathbf{A}) =1$,
so $D$ satisfies axiom 3 also, and thus we have shown the existence of the $n \times n$ determinant and 
of formula \eqref{eq:cofexp}, which is also called the row expansion, or Laplace expansion of the determinant

-------------
###Linear equations and Cramer's Rule
-------------

Now instead of the right side of equation \eqref{eq:cofexp}, consider the sum:

$$a_{j1} A_{i1} + a_{j2} A_{i2} + \cdots + a_{jn} A_{in} $$

where $j \neq i$. As before, this sum satisfies axioms $1$ and $2$. Letting $\mathbf{A} =\mathbf{1}$,
the unit matrix, the only nonzero term in this sum is $a_{jj} A{ij}$. With $i \neq j$, when removing the
$i^\mathrm{th}$ row and $j^\mathrm{th}$ column from an $n \times n$ unit matrix, we remove both
$a_{ii}=a_{jj}=1$ and have to find the determinant of an $(n-1) \times (n-1)$ matrix with only $n-2$ 
nonzero terms. But each product in the Leibniz expansion for an $n\times n$ matrix has $n$ terms, 
and so this determinant is $0$. Therefore, 

$$\begin{equation}a_{j1} A_{i1} + a_{j2} A_{i2} + \cdots + a_{jn} A_{in} =0\ \mathrm{if}\ i \neq j.\label{eq:cofinj}\end{equation}$$

So far in equations \eqref{eq:cofexp} and \eqref{eq:cofinj}, we might as well have expanded by the columns
instead of by the rows, by the symmetry of determinant under transpose. Doing so, we get:

$$\begin{equation} a_{1j} A_{1i} + a_{2j} A_{2i} + \cdots + a_{nj} A_{ni} = \begin{cases} \det(\mathbf{A}) & \mathrm{if}\ i=j \\ 0 & \mathrm{if}\ i \neq j.\end{cases} \label{eq:cofcol} \end{equation}$$

Define the adjugate matrix $\mathrm{adj}(\mathbf{A})$ of a matrix $\mathbf{A}$ as follows:

$$\begin{equation}\left(\mathrm{adj}(\mathbf{A})\right)_{ij} = A_{ji}\label{eq:adjdef}\end{equation}$$

That is, write the cofactor matrix and take the transpose.

Then the equations \eqref{eq:cofexp}, \eqref{eq:cofinj} and \eqref{eq:cofcol} mean:

$$\begin{equation}\mathbf{A}.\mathrm{adj}(\mathbf{A})  = \mathrm{adj}(\mathbf{A}).\mathbf{A}  = \det(\mathbf{A}). \mathbf{1} \label{eq:adjdet}\end{equation}$$

where $\mathbf{1}$ is the unit matrix.

This leads to the following lemmas.

**Lemma** A matrix $\mathbf{A}$ over a ring $R$ is invertible if and only if $\det(\mathbf{A})$ is.

**Proof** Suppose $\mathbf{A}$ is invertible with inverse $\mathbf{A}^{-1}$. Then by the multiplication theorem, 
$\det(\mathbf{A}).\det(\mathbf{A}^{-1}) = 1$. Now suppose $\det(\mathbf{A})$ is invertible. Then, by equation 
\eqref{eq:adjdet}, 

$$\begin{equation} \mathbf{A}^{-1} =\frac{1}{\det(\mathbf{A})} \mathrm{adj}(\mathbf{A}) \end{equation}$$

 `Q. E. D.`

**Lemma** If the $n$ column vectors $\mathbf{a}_1, \mathbf{a}_2, \ldots , \mathbf{a}_n$ can generate any 
column vector $\mathbf{b} \in R^n$ via linear combinations, then $\det(\mathbf{A})$ is invertible.

**Proof** 
The assumption of the lemma means that in equation \eqref{eq:colsubn}, we can choose $\mathbf{a}^\prime_j = \mathbf{u_j}$,
the unit vector. So, we have $\mathbf{1} = \mathbf{A} \mathbf{B}$ for some $\mathbf{B}$, and by the multiplication
formula, $\det(\mathbf{A})$ is invertible.
 `Q. E. D.`

**Theorem: Cramer's rule** 

Suppose $\det(\mathbf{A})$ is invertible. Then the set of linear equations
$$\begin{equation}a_{i1}x_1 + \cdots + a_{in}x_n  = y_i,\ \text{where}\ 1 \leq i \leq n \end{equation}$$
where $b_i$ are arbitary scalars, has a unique solution, which can be computed via determinants involving $a_{ij}$
and $y_i$.

**Proof**
For a given $j$, multiply the equation for $y_i$ with $A_{ij}$ and add, and apply equation \eqref{eq:cofcol},
and examine the coeffients of $x_j$:
$$\begin{equation}\det(\mathbf{A}) . x_j = y_1 A_{1k} + \cdots + y_n A_{nk} \label{eq:cramer}\end{equation}$$
The right side is also the determinant of the matrix where the $j^\mathrm{th}$ column of $\mathbf{A}$ is replaced 
by the column vector $\mathbf{y} = (y_1, \ldots , y_n)$.
 `Q. E. D.`


