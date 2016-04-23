Title: Modules over a PID -- Invariant Factor Decomposition -- Structure Theorem and Applications
Date: 2015-05-09
Modified: 2015-05-09
Category: Algebra/Commutative Rings
Tags: Modules over PIDs, Principal Ideal Domains, Invariant Factor Decomposition, Finitely generated Abelian Groups, Rational Canonical Form, Companion Matrix
Slug: structure-theorem-for-modules-over-a-pid
Status: draft

[TOC]

-----------------------------

### Summary

--------------------------------------

All rings are assumed to be commutative with identity, and ring homomorphisms must take $1$ to $1$.

<!-- PELICAN_BEGIN_SUMMARY -->

The structure theorem for modules over PIDs is as follows.

Let $R$ be a principal ideal domain, i. e., a domain in which every ideal $I$ is a principal ideal of the form $(r)$ for some $r \in R$.
Let $M$ be a finitely generated module over $R$. Then, there exists a unique decreasing sequence of ideals 
$(d_1)\supseteq(d_2)\supseteq\cdots\supseteq(d_n)$ such that {{math|''M''}} isomorphic to the sum of cyclic modules:

$$M\cong\bigoplus_i R/(d_i) = R/(d_1)\oplus R/(d_2)\oplus\cdots\oplus R/(d_n).$$

This article goes through a proof of this theorem. Two particular cases are also given, viz., structure theorem for finitely
generated abelian groups and rational canonical form from linear algebra.

<!-- PELICAN_END_SUMMARY -->


-----------------
### Modules over a PID
-----------------

**Lemma 1**
Let $M$ be a free module of rank $m$ over a PID $R$. Let $N$ be a submodule. Then $N$ is also free. Moreover, let $n$ be 
the rank of $N$. Then, $n \leq m$.

**Proof**
By assumption, $M \cong R^n$, and we proceed by induction on $N$. For $n=1$, a submodule of $R$ is a principal ideal 
of the form $(r)$, which, as an $R$-module, is free because $R$ is a domain. Now let us suppose the claim is proved for 
$R^n$ and suppose $N \subset R^{n-1}$ is a submodule.

----------------
### Finitely generated Abelian Groups
----------------

When $R = \mathbb Z$, modules over $R$ are nothing but abelian groups, and the structure theorem becomes:

**Structure Theorem for Finitely Generated Abelian Groups**
Let $B$ be a finitely abelian group. Then, there are uniquely determined non-negative integers 
$d_1, d_2, \ldots , d_n$ such that, $d_1 | d_2 | \cdots | d_n$, and,
$$ G \cong \mathbb Z/(d_1) \oplus \mathbb Z/(d_2) \oplus \cdots \oplus \mathbb Z/(d_n).$$

It is possible that $d_i = 0$. Such $d_i$ form the *free part* and
the rest the *torsion part*.


