Title: Algebraic numbers, number fields, algebraic integers and rings of integers
Date: 2016-06-30
Category: Arithmetic/Number Fields
Tags: Algebraic number,  Algebraic integer, Number field, Primitive element theorem, Ring of integers, Conjugate, Norm, Trace, Dedekind domain, Unique factorization
Slug: algebraic-numbers-integers
status: draft

[TOC]

### Algebraic number fields
---------------

<!-- PELICAN_BEGIN_SUMMARY -->
An algebraic number $\alpha$ satisfies a polynomial of the form $a_0 + a_1 x + \cdots + a_{n-1} x^{n-1} + x^n$ where $a_i \in \mathbb Q$ or by clearing denominators, $a_i \in \mathbb Z$. We may consider $\alpha \in \mathbb C$ or $\alpha \in \bar{\mathbb Q}$, the algebraic closure, per convenience. Attention of algebraic number theory is on the field generated by such an algebraic number than individual algebraic numbers. 

Let $K$ be an algebraic number field over $\mathbb Q$, i. e., a finite extension of $\mathbb Q$. This is always generated by a single element $\alpha \in K$ according to the primitive element theorem.

The degree of the extension, denoted $[K:\mathbb Q]$ is defined as the dimension of $K$ as a vector space over $\mathbb Q$. 
This is same as the degree of the minimal polynomial for a primitive element $\alpha$ generating $K/\mathbb Q$. 

Then the set $\mathfrak{O}_K$ of algebraic integers in $K$, i. e., all elements in $K$ that satisfy a polynomial equation $a_0 + a_1 x + \cdots + a_{n-1} x^{n-1} + x^n$ where $a_0, a_1, \ldots \in \mathbb Z$, form an integral domain whose field of quotients is $K$. 

The ring $\mathbb Z [ \sqrt{-5}]$, which may in fact be verified to be the ring of integers of a [quadratic field]({filename}quadratic-fields.md), has e. g. the ambiguous factorization $6 = 2.3 = (1+\sqrt{-5})(1-\sqrt{-5})$ into irreducibles; therefore unique factorization need not hold in such rings. 
Nevertheless, a unique factorization theorem does hold for ideals of rings of integers of number fields; they split into product of powers of prime ideals. This agrees with the usual unique factorization when the rings are principal ideal domains.

This article will prove the unique factorization theorem for ideals of number rings and develop what is necessary along the way.
<!-- PELICAN_END_SUMMARY -->

We generally follow the approach of Hecke (1923)[^Hecke1923], van der Waerden (1930)[^vanderWaerden1930], Koch (1992)[^Koch1992] and Koch (1997)[^Koch1997].

An algebraic number may be considered to satisfy an irreducible polynomial. This can be extended to algebraic integers too -- in the definition, if $\alpha \in C$ satisfies a monic polynomial with integer coefficients, then it satisfies such an irreducible polynomial, by the Gauss lemma.

It may be shown that sums, differences and products of two algebraic numbers are algebraic, as follows. Let $\alpha$ be an algebraic number satisfying the monic polynomial $f(x) = x^n + a_{n-1}x^{n-1} + \cdots + a_0$ and $\alpha_1, \ldots , \alpha_n$ its conjugates; i. e., all roots of this polynomial; thus, $f(x) = (x - \alpha_1). \cdots . (x - \alpha_n)$.
Let  $\beta$ be another algebraic number, satisfying a monic polynomial $g(x) = x^n + b_{n-1}x^{n-1} + \cdots + b_0$ and $\beta_1, \ldots, \beta_m$ its conjugates.
Then, consider
$$h(x) = \prod_{i=1}^{m} \prod_{j=1}^{m} (x-(\alpha_i+\beta_j))$$
which is a symmetric polynomial in the $\alpha_i$'s and $\beta_j$'s.
By a double application of the [fundamental theorem on symmetric functions]({filename}../algebra/commutative/symmetric-polynomials.md), coefficients of the polynomial $F$ may be obtained from those of $f$ and $g$ has coefficients by addition, subtraction and multiplication; thus, the roots of $h(x)$ are themselves algebraic numbers. Argument proceeds similarly for subtraction and multiplication of algebraic numbers.

The above proof actually proved the same regarding algebraic integers too: sums, differences and products of two algebraic integers are again algebraic integers.

Quotient of two algebraic numbers is also an algebraic number, when the latter is nonzero.
For this it is enough to show that the reciprocal of a nonzero algebraic number is algebraic.
Let $\alpha \in \mathbb C$ satisfy $f(x) = x^n + a_{n-1}x^{n-1} + \cdots + a_0$, where one may require that $a_0 neq 0$ if $\alpha =0$.
Then $1/\alpha$ will satisfy $x^{-n} + a_{n-1}x^{-(n-1)} + \cdots + a_0$; i. e., it will satisfy $g(x) =  a_0 x^n + \cdots + a_{n-1}x + 1$ and dividing by $a_0$ we may obtain a monic polynomial.

Let $\alpha$ be an algebraic number. 
Then it may be shown that there exists an integer $m \neq 0$ such that $m\alpha$ is an algebraic integer, which may be shown as follows. 
Let $\alpha$ satisfy the polynomial $a_n x^n+ \cdots + a_0$ where $a_i \in \mathbb Z$.
Then $a_n\alpha$ satisfies $a_n^{-n-1}(a_n\alpha)^n + a_{n-1}a_n^{-(n-1)}(a_n\alpha)^{n-1} + \cdots + a_1 a_n^{-1}(a_n\alpha) a_0$; i. e., $a_n\alpha_n$ satisfies the polynomial $ x^n + a_{n-1}a_n x^{n-1} + \cdots + a_1 a_n^{n-2} + a_0 a_n^{n-1}$. Therefore $m = a_n$ will do. This also means that an algebraic number field $K$ is the field of fractions of its ring of integers $\mathfrak O_K$.

Algebraic integers satisfy the following “transitivity” property: Let $\omega$ be a root of the polynomial $\varphi(x) = x^n + \alpha x^{n-1 } + \beta x^{n-2} + \cdots $, ending in a degree $0$ term, where $\alpha, \beta, \ldots$ are all algebraic integers. 
Then $\omega$ is also an algebraic integer. This can be shown as follows: let $\alpha_i$ run through the conjugates of $\alpha$, $\beta_j$ through those of $\beta$, etc., and apply the fundamental theorem on symmetric functions successively on the polynomial: $\Phi(x) = \prod_{i, k, \ldots} (x^n + \alpha x^{n-1 } + \beta x^{n-2} + \cdots)$. The coefficients of $\Phi$ may be obtained from the coefficients of $\varphi$, and any root of $\varphi$ is also a root of $\Phi$; so $\omega$ is also an algebraic number.


### Primitive element theorem
-----------------

Suppose  $K/F$ is an algebraic extension. 
Let $\alpha \in K$ be algebraic over $F$, satisfying a minimal polynomial $f(\alpha) = 0$ where $f(x) \in F[x]$ of degree $n$.
This polynomial is (upto a scalar multiple) unique.

The **primitive element theorem** states that a finite separable field extension $K/F$ is generated by a primitive element, i. e., there exists $\alpha \in L$ such that $K = F(\alpha)$, which we prove as follows.

The statement is true for finite fields because the multiplicative groups of finite fields are cyclic; thus a generator of $F^\times$ may be expressed as a power of a generator of $K^\times$ and for the rest of the argument it may be assumed that $F$ is infinite.

Let $\alpha \in K$ with $\alpha \notin F$ be a root of $f(x) \in F[x]$ with distinct conjugates $\alpha_1, \ldots , \alpha_n$ and $\alpha = \alpha_1$.
Let $\beta \in K$ with $\beta \notin F$ be a root of $g(x) \in F[x]$ with distinct conjugates $\beta_1, \ldots , \beta_n$ and $\beta = \beta_1$.
It suffices to prove that when $\alpha \neq \beta$, there exits a $\theta \in K$ such that $F(\alpha, \beta) = F(\theta)$; rest follows by induction.
For each $i > 1$ and each $j >1$, there is exactly one solution $\gamma_{i j} \in K$ for the equation $\alpha_i + \gamma\alpha_1 = \beta_j + \gamma\beta_1$.
Fix a $\delta \in K$ different from all the $\gamma_{i k}$'s.
Let $\theta = \alpha + \delta \beta$; as $\theta \in F(\alpha, \beta)$ already, theorem will be proved by showing that $\alpha, \beta \in F(\theta)$.
In the field $F(\theta)$, it is seen that $\beta$ satisfies the equations $g(\beta) = 0$ and $f(\theta - \delta\beta) = f(\alpha) =0$.
Thus $\beta$ is a root of g. c. d. of the polynomials $g(x)$ and $f(\theta-\delta x)$.
However, for the already fixed choice of $\delta$, no root $\beta_j$ of $g(x)$ except $\beta$ will satisfy any $\alpha_i = \theta - \delta \beta_k$, for, if it does for some $i$ and $k$, subtracting the equation $\alpha = \theta - \delta \beta$, we are led to an equation which the choice of violates.
Thus the g. c. d. is a linear term $(x -\beta)$. As the g. c. d. is a polynomial over $F(\theta)$, so does the coefficient $\beta$ in it belong to the same field, g. c. d. being a result of the Euclidean algorithm and thus independent of the base field.
As $\alpha = \theta -\delta \beta$, so does $\alpha$ too.
Thus, the theorem is proved.


### Conjugates, Norm and Trace
----------

Let $K/F$ be a finite separable field extension of degree $n$ with that $K = F(\theta)$ for some $\theta \in K$, so that $\theta$ is a root of some minimal polynomial $f(x)$ of degree $n$ over $F$ and $K = F[x]/(f(x))$. Then, the set $\{1, \theta, \theta^2, \ldots , \theta^{n-1} \}$ forms a basis of $K/L$ as a vector space; that is to say, every element $\alpha$ of $K = F(\theta)$ is obtained exactly once in the form $\alpha = a_0 + a_1 \theta + \cdots + a_{n-1}\theta^{n-1}$, where $a_0, a_1, \ldots , a_{n-1}$ runs through all elements of $F$. 
This may be shown as follows. 
Given $\alpha \in K$, let $\alpha = P(\theta)/Q(\theta)$, with $Q(\theta) \neq 0$. 
Then, $Q(x)$ and $f(x)$ are relatively prime.
Thus there exists $g(x), h(x) \in F[x]$ such that $1 = f(x)g(x) + Q(x)h(x)$.
This gives $1 = Q(\theta)h(\theta)$.
As $\theta^n$ and higher powers are expressible as $F$-linear combinations of $1, \theta, \theta^2, \ldots , \theta^{n-1}$, all $\alpha \in K$ can be expressed in the required form.
To see the uniqueness of this representation, let $a_0 + a_1 \theta + \cdots + a_{n-1}\theta^{n-1} = a_0^\prime + a_1^\prime \theta + \cdots + a_{n-1}\theta_{n-1}^\prime$, where $a_i$'s and $a^\prime_i$'s belong to $F$. 
Then, we have the polynomial equation $(a_0-a^\prime_0) + (a_1 - a^\prime_1) \theta + \cdots + (a_n - a^\prime_n) \theta^{n-1} = 0$ of degree less than $n$ which is impossible unless all coefficients are $0$, due to the minimality of $f$.

 Given as above for $\alpha = g(\theta) \in F(\theta)$ for some polynomial $g$ over $F$, with conjugates $\theta_1, \ldots , \theta_n$ for $\theta$, the relative conjugates of $\alpha$ are defined as the values $\alpha_i = g(\theta_i)$ as $1 \leq i \leq n$. 
This is related to the conjugates of $\alpha$ as follows. 
Let $\phi(x)$ be a minimal polynomial over $F$ such that $\varphi(\alpha_i) =0$ for some $i$.
This means the polynomial $\varphi(f(\theta_i)) = 0$; i. e., $\theta_i$ is a zero of $\varphi (f(x))$.
As $f(x)$ is an irreducible polynomial with zero $\theta_i$, this means all $\theta_j$ for $1 \leq j \leq n$ are zeros of $\varphi (f(x))$; thus, all $\alpha_j$'s are zeros of $\varphi(x)$.
Therefore, relative conjugates of $\alpha$ for $F(\theta)/F$ are also conjugates of $\alpha$.

Moreover, conjugates of $\alpha$ appear equally often among the relative conjugates of $\alpha$, as can be seen as follows.
Consider the polynomial $\phi(x) = \prod_{i=1}{n} (x - g(\theta_i))$ of which the relative conjugates $\alpha_j$'s are the roots.
Let $\varphi(x)$ be a a minimal polynomial for $\alpha$ over $F$.
Then, $\varphi(x)$ divides $\phi(x)$. 
Let $\varphi(x)^q$ with $q \geq 1$ be the highest power of $\varphi(x)$ that divides $\phi(x)$.
It follows that $\phi(x)/\varphi^q(x)$ is constant, for, otherwise, it would be divisible by $(x-\alpha_i)$ for some $i$; but $\alpha_i$ is a root of the irreducible polynomial $\varphi(x)$ and therefore $\varphi(x)$ must divide $\phi(x)/\varphi^q(x)$, violating maximality of $q$.
That is, $\phi(x) = \varphi^q(x)$; therefore, the relative conjugates of $\alpha$ in $F(\theta)$ are precisely the conjugates of $\alpha$ each repeated $q$ times. This also shows that the degree of $\alpha$ over $F$ is $n/q$.

Thus, for an extension $K/F$ with $K=F(\theta)$ of degree $n$, the conjugates of each $\alpha$ with respect to $F$ are independent of the choice $\theta$ of generator of $K$. 

Fix a generator $\theta$ for $K/F$ of degree $n$ and fix an ordering of conjugates $\theta_1, \ldots, \theta_n$.
Each $\alpha \in K$ may be uniquely expressed as $a_0 + a_1 \theta + \cdots + a_{n-1}\theta^{n-1}$.
Define mappings $\sigma_i$ for $1 \leq i \leq n$ from $K$ to the algebraic closure $\bar K$ as: $(a_0 + a_1 \theta + \cdots + a_{n-1}\theta^{n-1} \mapsto a_0 + a_1 \theta_i + \cdots + a_{n-1}\theta_i^{n-1}$.
This in particular takes each $alpha$ to its conjugate $\alpha_i$.
Each $\sigma_i$ is a field isomorphism on to the image.
In fact, what this isomorphism is clear by first identifying $K$ with $F[x]/(f(x))$ via the isomorphism map $F[x]/(f(x)) \rightarrow K$, with $x \mapsto \theta$, and then considering for each $i$ the field embedding $F[x]/(f(x)) \rightarrow \bar K$ into the algebraic closure sending $x \rightarrow \theta_i$. 
Moreover, these are all the possible embeddings of $K$ into $\bar K$, as any image of $\theta$ must be a conjugate of it.
Thus the conjugates $\alpha_i$ may be also be thought of as the images $\sigma_i(\alpha)$ under embeddings $\sigma_i : K \rightarrow \bar K$.

Norm and Trace of an element $\alpha$ in a finite extension $K$ of degree $n$ over a field $F$ are defined as follows. 
$K$ forms a vector space of degree $n$ over $F$ and $\alpha$ acts as an endomorphism on it by multiplication.
The norm $N_{K/F}(\alpha)$ and trace $\mathrm{Tr}_{K/F}(\alpha)$ are defined to be respectively the determinant and trace of this linear transformation.
Let $\theta$ be a primitive element for $K/F$, with minimal polynomial $f(x) = a_0 + \ldots + a_{n-1}x^{n-1} + x^n \in F[x]$.
We compute the norm and trace of $\theta$ for $K/F$ as follows.
Then $1, \theta, \ldots, \theta_{n-1}$ forms a basis for $K/F$.
The matrix of the linear transformation corresponding to $\theta$ has all lower diagonal terms $1$, final row $(-a_{n-1}, \ldots , -a_0)$ and $0$ everywhere else.
Thus $\mathrm{Tr}_{F(\theta)/F}(\theta) = -a_{n-1}$.
The norm $N_{F(\theta)/F}(\theta)$ is the determinant of the vector: $\det(t, t^2, \ldots , t^n)$.
It follows that:
$$\begin{align}
\det(t, t^2, \ldots , t^n)  & =  (-1)^n \det( -(a_0 + \cdots + a_{n-1}\theta^{n-1}), t, \ldots , t^{n-1}) && \text{(interchanging columns)} \\
&=  (-1)^{n-1} \det( -a_0, t, \ldots , t^{n-1}) && \text{(canceling equal columns)}\\
&=  (-1)^{n-1} \det( -(a_0 + \cdots + a_{n-1}\theta^{n-1}), t, \ldots , t^{n-1}) && \text{(interchanging columns)} \\
&=  (-1)^n a_0. && \text{(determinant of basis is } 1)  \end{align}$$

In the algebraic closure $\bar K$ of $K$, the polynomial $f(x)$ splits into $(x-\theta_1). \cdots . (x-\theta_n)$ with $ -a_{n-1} = \theta_1 + \cdots + \theta_n$ and $a_0 = \theta_1 . \cdots . \theta_n$, where $\theta_1, \ldots, \theta_n$ are the conjugates.
Therefore, $N_{K/F}(\theta) = \theta_1 . \cdots \theta_n $ and $\mathrm{Tr}_{K/F}(\theta)= \theta_1 + \cdots + \theta_n $.
In the case that $\alpha \in K$ is not a generator of $K/F$, let $t_1, \ldots , t_q$ be a basis of $K$ over $F(\alpha)$.
As before, $1, \alpha, \ldots, \alpha^{n-1}$ forms a basis for $F(\alpha)/F$.
Then, $1.t_1,, \alpha . t_1 \ldots, \alpha^{n-1}.t_1, \ldots, 1.t_1,, \alpha . t_2,, \ldots, \alpha^{n-1}.t_2, \ldots, \ldots , 1.t_q, \alpha . t_q,, \ldots, \alpha^{n-1}.t_q$ is a basis for $K/L$.
Multiplication by $\alpha$ may be understood as $(1.t_i, \alpha . t_i,, \ldots, \alpha^{n-1}.t_i) \mapsto ( t_i, \alpha . t_i^2,, \ldots, \alpha^{n-1}.t_i^n)$ and the corresponding matrix may be understood as a block matrix with each block similar to the above case.
We get, $N_{K/F}(\alpha) = (N_{F(\alpha)/F)}(\alpha))^q$ and $\mathrm{Tr}_{K/F}(\alpha) = q.\mathrm{Tr}_{F(\alpha)/F}(\alpha)$.
Here too, norm and trace are respectively the product and sum of all the conjugates with respect to $K$.

### Dedekind domains
---------------

The proofs so far were more direct and concrete. Now more of the machinery of abstract algebra will be used and some of the facts are re-proven.

It was shown already that the set $\mathfrak O_K$ of all algebraic integers in an algebraic number field $K$, forms a ring. A different proof is given in the following two paragraphs using a reformulation of the definition.

Note that the condition $\alpha \in \mathbb C$ is an algebraic integer is equivalent to the statement that the ring $\mathbb Z[\alpha]$ is finitely generated as a $\mathbb Z$-module.
To see this implication, if $\alpha^n + a_{n-1}\alpha^{n-1} + \cdots + a_0 =0$ with $a_i \in \mathbb Z$ and $n >1$, then it means $\alpha^n$, and thus all higher powers, may be expressible as integral linear combination of $1, \alpha, \ldots, \alpha^{n-1}$; thus, $\mathbb Z[\alpha]$ is a finitely generated $\mathbb Z$-module.
Conversely, if $\mathbb Z[\alpha]$ is finitely generated, each generator is a polynomial expression in $\alpha$ with integer coefficients, i. e., there exists finitely many polynomial expressions $\alpha_1, \ldots , \alpha_m$ on $\alpha$ with integer coefficients, such that all positive powers of $\alpha$ are integral linear combinations of the $\alpha_i$'s. 
Let $l$ be an integer greater than the maximum of the degrees of these polynomial expressions; then $\alpha^l$ is expressible as an integral linear combination of lower powers of $\alpha$; thus, $\alpha$ is an algebraic integer. 

Now, if $\alpha, \beta \in \mathfrak O_K$, then let $\mathbb Z[\alpha]$ be generated as $\mathbb Z$-modules by by $\alpha_1, \ldots, \alpha_m$ and $\mathbb Z[\beta]$ by $\beta_1, \ldots , \beta_n$; that is to say, all positive powers of $\alpha$ can be expressed as linear combinations of the $\alpha_i$'s and similarly for $\beta$. 
Then, all powers of $\alpha+ \beta$, $\alpha - \beta$ and $\alpha \beta$ can be expressed as linear combinations of the set $S$ of all $\alpha_1, \ldots, \alpha_m$ and all $\beta_1, \ldots, \beta_n$ and all their multiples $\alpha_1\beta_1, \ldots , \alpha_1\beta_n, \ldots \ldots , \alpha_m\beta_1, \ldots , \alpha_m\beta_n$.
Therefore  $\mathbb[\alpha+ \beta]$, $\mathbb Z[\alpha - \beta]$ and $\mathbb Z[\alpha \beta]$ are finitely generated, as submodules of the finitely generated $\mathbb Z$-module on $S$ are themselves finitely generated. Thus, sums and products of algebraic integers are again algebraic integers, and therefore $\mathfrak O_K$ is a ring.

In this proof, use of the  fact that submodules of a finitely generated $\mathbb Z$-modules are themselves finitely generated, is a consequence of the Nötherian property of the ring $\mathbb Z$. Finitely generated modules over it are Nötherian and vice versa, and submodules of a Nötherian module are themselves Nötherian; see e. g., Atiyah and Macdonald (1969)[^AtiyahMacDonald1969]. More generally, the definition may be made of:

Let $R$ be an integral domain $1$. Then it is called a Dedekind domain (or Dedekind ring) if the following three conditions are satisfied:

1. $R$ is Nötherian.
2. Every prime ideal in $R$ is also a maximal ideal.
3. $R$ is integrally closed in its field of fractions; i. e., let $K$ be the field of fractions of $R$ and let $x \in K$ be integral over $R$; then $x$ also belongs to $K$.

## Bibliography

[^Hecke1923]: Hecke, E., Vorlesungen uber die Theorie der algebraischen Zahlen, Akademische Verlaggesselschaft, Leipzig, 1923; Lectures on the theory of algebraic numbers, Springer-Verlag New York, 1981.

[^vanderWaerden1930]: van der Waerden, B. L., Moderne Algebra, 1930; Algebra I & II, Springer, 1991.

[^Koch1992]: Koch, H., Algebraic Number Theory, Encyclopaedia of Mathematical Sciences Vol. 62, Ed: A. N. Parshin and I. R. Shafarevich, Springer-Verlag 1992.

[^Koch1997]: Koch, H., Zahlentheorie. Algebraische Zahlen und Funktionen, Vieweg, 1997; Number Theory: Algebraic Numbers and Functions, AMS, 2000.

[^AtiyahMacDonald1969]: Atiyah, M. F. and I. G. MacDonald, Introduction to Commutative Algebra, Addison Wesley 1969.

===============
