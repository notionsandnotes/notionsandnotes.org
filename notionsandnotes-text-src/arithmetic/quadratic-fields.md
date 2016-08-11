Title: Quadratic fields
Date: 2016-05-17
Category: Arithmetic/Number Fields
Tags: Quadratic fields, Discriminant, Algebraic number fields
Slug: quadratic-fields
Status: draft

[TOC]

###Quadratic fields
--------------

<!-- PELICAN_BEGIN_SUMMARY -->
A quadratic field is a field extension of $\mathbb Q$ of degree $2$. These are comparatively easier examples of algebraic number fields. We can show that a quadratic field is determined by its discriminant provide a basis for the ring of integers depending only on the discriminant. 
<!-- PELICAN_END_SUMMARY -->

**Proposition 1.** 
A quadratic extension of $\mathbb Q$ is of the form $\mathbb Q(\sqrt{D})$ where $D \in \mathbb Z$ and square-free.

*[square-free]: no perfect square divides the number.

**Proof:**
Let $K$ be a quadratic field and let $\alpha \in K$ with $\alpha \notin \mathbb Q$. 
Then, $\{1, \alpha \}$ is a basis for $K$ as a vector space over $\mathbb Q$ and $\alpha$ satisfies a quadratic equation $a_2\alpha^2 + a_1\alpha + a_0 = 0$ with coefficients in $\mathbb Q$.
Clearing denominators by their l. c. m., it may be assumed $a_0, a_1, a_2 \in \mathbb Z$.
[Completing the square](https://en.wikipedia.org/wiki/Completing_the_square) in the equation, we get $(2a_2\alpha + a_1)^2 = a_1^2 - 4a_0a_2 = D$ and $K = \mathbb Q(\sqrt{D})$ elsewise. Without loss of generality one may also assume $D$ is square-free.
**Q.E.D.**
--------------
*[l. c. m]: least common multiple 

This proposition can be strengthened to:

**Proposition 2**
Let $K = \mathbb Q(\sqrt{D})$ be a quadratic field with square-free $D \in \mathbb Z$. 
Let $d$ be the discriminant of $K$. 
Then, $K= \mathbb Q(\sqrt{d})$.
The discriminant $d$ of $K$ equals $D$ if $D \equiv 1\ (\mathrm{mod}\ 4)$ and $4D$ if $D \equiv 2\ \mathrm{or}\ 3\ (\mathrm{mod}\ 4)$.
Let $\mathcal O_K$ be the ring of integers of $K$. Then,
The set $\{ 1, \frac{d+\sqrt{d}}{2} \}$ forms a basis of $\mathcal O_K$.

**Proof:**

$K = \mathbb Q(\sqrt{D})$ is called a *real quadratic field* if $\mathbb Q(\sqrt{m}) \subset \mathbb R$ and *imaginary quadratic field* otherwise; i. e., according as $D > 0$ or $D < 0$, respectively.

-------------------


--------------
### Bibliography
--------------

[^Hecke1923]: Hecke, E., Vorlesunger die Theorie der algebraischen Zahlen, Akademische Verlaggesselschaft, Leipzig, 1923; Lectures on the theory of algebraic numbers, Springer-Verlag New York, 1981.

[^Stark1967]: Stark, H., [A complete determination of the complex quadratic fields of class-number one](https://projecteuclid.org/euclid.mmj/1028999653).

[^Heegner1952]: Heegner, K., [Diophantische Analysis und Modulfunktionen](http://gdz.sub.uni-goettingen.de/de/dms/load/img/?PID=GDZPPN002382962).

[^Stark2007]: Stark, H., [The Gauss Class-Number Problems](www.uni-math.gwdg.de/tschinkel/gauss-dirichlet/stark.pdf).

[^Oesterle1984]: Oesterlé, J., [Nombres de classes des corps quadratiques imaginaires](http://numdam.mathdoc.fr/numdam-bin/item?id=SB_1983-1984__26__309_0).

[]([^Narasimhan1966]: Narasimhan, R. et. al., [Algebraic Number Theory](http://www.math.tifr.res.in/~publ/pamphlets/algnum.pdf), TIFR, 1996.)


