Title: Symmetric polynomials and symmetric function theorem
Date: 2016-05-17
Category: Algebra/Commutative Rings
Tags: Symmetric polynomial, Elementary symmetric polynomials, Fundamental theorem on symmetric polynomials, Resultant, Discriminant, Determinant, Commutative rings
Slug: fundamental-theorem-of-symmetric-functions
Status: draft

[TOC]

###Symmetric polynomials
-------------

<!-- PELICAN_BEGIN_SUMMARY -->
Let $R$ be a commutative ring and $R[x_1, x_2 , \ldots , x_n]$ the polynomial ring in $n$ indeterminates over $R$.
A polynomial $f(x)$ in it is said to be a symmetric polynomial (or symmetric function) of $x_1, \ldots , x_n$ if it is unchanged by any permutation of the indeterminates.
Introduce one more indeterminate $X$ and consider the polynomial 

\begin{eqnarray*} f(t ,x_1, \ldots, x_n) & = & (t - x_1)(t-x_2). \dotsm .(t-x_n)\\
        & = & t^n -e_1(x_1, \ldots , x_n)t^{n-1} + \cdots + (-1)^n e_n(x_1, \ldots , x_n)t 
\end{eqnarray*}

where

\begin{eqnarray*} e_1(x_1, \ldots , x_n) & = & x_1 + x_2 + \cdots + x_n \\ 
e_2(x_1, \ldots , x_n) & = & x_1x_2 + x_1x_3 + \cdots + x_1x_n + x_2x_3 + \cdots + x_{n-1}x_n \\
& \vdots & \\
e_i(x_1, \ldots , x_n) & = & \sum_{1\leq  j_1 < j_2 < \cdots < j_i \leq n} x_{j_1} \dotsm x_{j_i} \\
& \vdots & \\
e_n(x_1, \ldots , x_n) & = & x_1x_2 \dotsm x_n
\end{eqnarray*}

All of $f(t ,x_1, \ldots, x_n)$ and $e_i(x_1, \ldots , x_n)$ are symmetric functions of $x_1, \ldots , x_n$. 
The $e_i$'s are called elementary symmetric polynomials of $x_1, \ldots , x_n,$ with:

$$f(t ,x_1, \ldots, x_n) =  \sum_{i=0}^n t^{n-i} e_i(x_1, \ldots , x_n).$$
A polynomial $g(e_1, \ldots , e_n)$ of $e_1, \ldots , e_n$ becomes a symmetric polynomial $g(x_1, \ldots x_n)$ when $e_i$'s are written in terms of $x_i$'s. 
The fundamental theorem on symmetric functions is the converse of this statement, which presently will be more precisely stated and proved.

<!-- PELICAN_END_SUMMARY -->

Sums, products and scalar multiples of symmetric polynomials are again symmetric polynomials. 

Note that symmetric polynomials give general expressions for coefficients of a polynomial in terms of its roots.
The fundamental theorem (once proved) can then be thought of as being able to express any symmetric function of the roots of a polynomial, in terms of the coefficients without needing to explicitly compute the roots.

Note that the discussion so far is valid for any ring $R$ by e.g., first doing in the ring $\mathbb Z[t, x_1, \ldots , x_n]$ and tensoring with $R$. 
A more sophisticated way to state context is to construct the ring of symmetric functions as a "power series ring" constructed as the inverse limit as $n$ varies, of the ring of symmetric polynomials in $n$ variables over $R$.
Details of such a construction is available eg in MacDonald (1979)[^MacDonald1979].
The exposition here is of van der Waerden (1930)[^vanderWaerden1930] and Lang (1993)[^Lang1993].

Every polynomial $e_i$ is a homogeneous polynomial of degree $i$ in $x_1, \ldots x_n$.

Consider the homomorphism from $R[x_1, \ldots , x_n]$ to itself sending $x_1 \mapsto e_1, \ldots ,x_n \mapsto e_n$.
Given a polynomial $g(x_1, \ldots , x_n)$, one gets the symmetric polymonial $g(e_1, \ldots , e_n)$ considered as a polynomial in $x_1, \ldots , x_n$.
The term $a.e_1^{\mu_1}.\cdots .e_n^{\mu_n}$ of $g(e_1, \ldots , e_n)$ where $a$ is a scalar, becomes a homogeneous polynomial of degree $\mu_1 + 2\mu_2 + \ldots + n\mu_n$ in $x_1, \ldots, x_k.$

--------------
###Bibliography
----------

[^vanderWaerden1930]: van der Waerden, B. L., Moderne Algebra, 1930; Algebra I & II, Springer, 1991.
[^Lang1993]: Lang, S., Algebra, Springer, 2002.
[^Prosolov2001]: Prosolov, V. V., Polynomials, Springer, 2001.
[^MacDonald1979]: MacDonald, I. G., Symmetric Polynomials and Hall functions, Oxford Mathematical Monographs, 1979.
