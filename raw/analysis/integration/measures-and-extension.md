Title: Lebesgue measure 
Date: 2015-02-05 
Category: Analysis/Integration
Tags: Real Analysis, Measure theory, Caratheodory extension, Sigma algebras, Measure spaces, Lebesgue measure, Complete measures
Slug: measures-extension
Series: Lebesgue Theory

[TOC]

**Table of contents**

[TOC]


-----------------------------

### Introduction and examples

--------------------------------------

 A positive measure on a measurable space $X$ is a device to "measure" sets belonging to a class $\Sigma$ of subsets of $X$. We define this as a 
function $l : \Sigma \to [0, \infty]$ satisfying the following axioms:

 1.  $l (A) \in [0, \infty]$ for all $A$.
 2.  $l (A \cup B) = l(A) + l(B)$ whenever $A \cap B = \emptyset$.
 3.  Let $A_n$ be a monotone class, i. e., let $A_1 \subset A_2 \subset \cdots$, and $A = \bigcup\limits_{n=1}^\infty A_n$, then 
     we have $l(A) = \lim\limits_{n \to \infty} l(A_n)$.

 Our first example is the [`counting measure`](http://en.wikipedia.org/wiki/Counting_measure): Here $\Sigma$ is the power 
set of $X$ and for any $A \subset X$, $l(A)$ = $|A|$ where $|A|$ denotes the cardinality of $A$, a finite number or infinity.

 One more easy example is the [`Dirac measure`](http://en.wikipedia.org/wiki/Dirac_measure). Here we choose a point $x \in X$, and, for 
any subset $A \subset X$, we define $\delta_x(A) = 1$ if $x \in A$ and $0$ otherwise. This measure is related to the [`Dirac Delta 
function`](http://en.wikipedia.org/wiki/Dirac_delta_function).

 Next we consider [`Lebesgue measures`](http://en.wikipedia.org/wiki/Lebesgue_measure). An important model for abstract measures is 
the notion of `length` of subsets of $X = \mathbb R$, first defined for intervals and then extended to a larger class of subsets or 
$\mathbb R$, satisfying the three properties above. Here we need to prove that such an extension can be done. Other similar models 
are the notions of `area` and `volume` defined when $X = \mathbb R^2$ and $X = \mathbb R^3$ respectively. In these cases also it is 
to be proved that such an extended mapping satisfying the three properties as above can be constructed, meaning that each of these 
constitute a measure, and this is the Lebesgue measure on $\mathbb R$ or on $\mathbb R^n$. 

 The goal of this article is to prove that Lebesgue measure exists for the one-dimensional case, i.e., on $\mathbb R$. First, we will 
prove the slightly more general Caratheodory extension theorem, and then show that *length* satisfies the conditions necessary for 
its applications; thus we will have shown the existence of Lebesgue measure.

The following two additional properties are satisfied for Lebesgue measures:

 -  For any $x \in X$, we have $l(x + A) = l(A)$.
 -  $l(A) = 1$ for the unit interval, unit square and unit cube in dimensions $1$, $2$ and $3$ respectively. 

The first property means that Lebesgue measure is [`translation invariant`](http://en.wikipedia.org/wiki/Invariant_measure). The second 
property, in conjunction with all others, can be used to [uniquely describe](http://en.wikipedia.org/wiki/Haar_measure) the Lebesgue measure.


Note that we only claimed that the Lebesgue measures on the Euclidean spaces can be extended to a large class of subsets of the space,
and not to the class of all subsets of the space. This is because it is possible to construct non-measurable sets[^1] in $\mathbb R$ 
assuming the axiom of choice[^2]. 

[^1]: A *Hamel Basis* means a basis of $\mathbb R$ as a vector space over the field $\mathbb Q$. There exist examples by Vitali and Levy 
of nonmeasurable sets constructed using a Hamel basis. Cit: [M. G. Nadkarni and V. S. Sunder](https://www.imsc.res.in/~sunder/mgnvss.pdf).

[^2]: If the axiom of choice is not assumed, then it is not possible to do much meaningful measure theory. For more into this topic,
consult books on descriptive set theory, for example Mansfield-Weitkamp, Recursive Aspects of Descriptive Set Theory, 
Oxford University Press, Oxford (1985). 

Now we pass on to the definitions:

---------------------------------------------------

### Definition of Measurable spaces and Measures

--------------------------------------------

**Definition**. An `algebra of sets` consists of a class $\cal A$ of subsets of a set $X$ such that:
 
 1.  $\emptyset \in \cal A$ and $X \in \cal A$.
 2.  $A \in \cal A$ imples $A^c \in \cal A$, where $A^c$ denotes the complement of $A$ in $X$, and,
 3.  If $A_1$ and $A_2$ belong to $\cal A$, then $A_1 \cup A_2$ belongs to $\cal A$.

**Definition**. A `set function` on an algebra $\cal A$ is a function $\ell$ mapping $\cal A$ to a suitable
range for the function, for example, $[0, \infty]$ or to $\mathbb C$.

**Definition** A set function $\ell$ on an algebra $\cal A$ is said to be `finitely additive` if it satisfies the condition that, 
when $A_1, A_2 \in \cal A$ such that $A \cap B =\emptyset$, then $\ell(A \cup B) = \ell(A) + \ell(B)$.

**Definition**. A `measurable space` consists of a pair $(X, \Sigma )$ where $X$ is a set and $\Sigma$ is a collection of subsets of $X$
such that:

 1.  $\emptyset \in \Sigma$ and $X \in \Sigma$.
 2.  $A \in \Sigma$ imples $A^c \in \Sigma$, where $A^c$ denotes the complement of $A$ in $X$, and,
 3.  If $A_1, A_2, \ldots, A_n , \ldots$ all belong to $\Sigma$, then $\bigcup\limits_{n=1}^\infty A_n$ belongs to $\Sigma$.

When $\Sigma$ satisfies the above three conditions, it is called a $\sigma$-algebra, or `sigma-algebra`  of subsets of $X$. 
A set $A$ in $\Sigma$ is said to be a measurable set.

**Remark**. If $X$ has a topology $\cal T$ on it, then there is a natural $\sigma$-algebra $\cal B$ on $X$, which is the smallest
$\sigma$-algebra containing $\cal T$, or equivalently, the intersection of all $\sigma$-algebras containing $\cal T$. This is
called the Borel $\sigma$-algebra.

**Definition**. A `measure space` consists of a triple $(X, \Sigma, \ell)$ where $(X, \Sigma )$ form a measurable space and $\ell$ is 
a set function, called the measure, on $\Sigma$ satisfying the following conditions:

 1.  $\ell (A \cup B) = \ell(A) + \ell(B)$ whenever $A \cap B = \emptyset$.
 2.  Let $A_n$ be a sequence of sets in $\Sigma$ which are pairwise disjoint. Then we have, 
     $$\ell \left( \coprod_{n=1}^\infty A_n \right)  = \sum_{n=1}^\infty \ell(A_n).$$

For a set $A \in \Sigma$, we cann $\ell(A)$ the measure of $A$. 

If  $\ell(A) \in [0, \infty]$ for all $A$, then  $\ell$ is a `positive measure` and if  $\ell(A) \in \mathbb C$ for all $A$, then
$\ell$ is a `complex measure`. We restrict ourselves to positive measures in this page.

The measure on $X$ is called $\sigma$`-finite` if there exists a sequence $A_n$ of measurable sets each of finite measure, such that 
$\cup_{n=1}^\infty A_n = X$.

Let $X$ be a space. A function $\mu : @^X \to [0, \infty]$ 

When $\Sigma$ is replaced by an algebra $\cal A$ of sets, and if there is a set function on it satisfying the above two conditions
whenever it makes sense, we still call it a measure on the algebra. In this case, we can extend the measure to the $\sigma$-algebra
generated by $\cal A$, provided the measure on $\cal A$ is $\sigma$-finite in the above sense. This is the process of Caratheodory 
extension, described below.

-------------------------------

### Caratheodory extension of measures
----------------------------------------

Caratheodory extension gives a `complete measure`, i.e., one in which all subsets of a set of measure
$0$ are measurable. Note that the $\sigma$-algebra obtained via the theorem is not is not the maximal class of subsets to which 
the measure can be extended.[^3]

[^3]: It can be shown for example that a measure on $\sigma$-algebra $\Sigma$ that is properly contained
in the power set of $X$ can always be extended to a bigger $\sigma$-algebra. For a proof, see V. I. Bogachev,
Measure Theory, 

-----------------------------
### Bibliography
-----------------------------

The following are some books on measure theory:

1.  K. B. Athreya and S. N. Lahiri, Measure Theory and Probability.
1.  S. R. Athreya and V. S. Sunder, Measure and Probability.
1.  V. I. Bogachev, Measure Theory. Vols. 1, 2.
1.  J. L. Doob, Measure Theory.
1.  H. Federer, Geometric Measure Theory.
1.  D. H. Fremlin, Measure Theory, Vols, 1-5.
1.  P. R. Halmos, Measure Theory.
1.  O. Kallenberg, Foundations of Modern Probability.
1.  P. Mattila, Geometry of Sets and Measures in Euclidean Spaces
1.  L. Nachbin, The Haar Integral.
1.  H. Royden, Real Analysis.
1.  W. Rudin, Real and Complex Analysis.

