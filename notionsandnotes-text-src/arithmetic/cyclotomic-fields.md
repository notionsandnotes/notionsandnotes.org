Title: Cyclotomic fields
Date: 2016-05-17
Category: Arithmetic/Number Fields
Tags: Cyclotomy, Cyclotomic fields, Cyclotomic polynomial, Kummer's proof of FLT, Algebraic number fields
Slug: cyclotomic-fields
Status: draft


[TOC]

### Roots of unity
---------------

<!-- PELICAN_BEGIN_SUMMARY -->
Cyclotomy entails investigations of arithmetical properties of roots of unity.
Its etymology is from Greek [κύκλος](https://en.wiktionary.org/wiki/%CE%BA%CF%8D%CE%BA%CE%BB%CE%BF%CF%82) (cyclos, circle)
and [τόμος](https://en.wiktionary.org/wiki/%CF%84%CF%8C%CE%BC%CE%BF%CF%82) (tomos, cutting).

Let $n \geq 1$ be a fixed integer.
C. F. Gauss in his seminal work *Disquisitiones Arithmeticae*[^Gauss1801] embedded the $n^{\mathrm{th}}$ roots of unity into the unit circle in the complex plane with primitive $n^{\mathrm{th}}$ root of unity as $\zeta = \zeta_n = e^{2\pi i/n}$.
Then the set $\mu_n$ of all $n^{\mathrm{th}}$ roots of unity may be realized as the points $\zeta^k = e^{2\pi ik/n}$, where $1 \leq k \leq n$, forming a regular $n$-gon inside the unit circle, and also a cyclic group of order $n$ under multiplication.

In the theory of algebraic numbers, the $n^{\mathrm{th}}$ cyclotomic field is the extension of $\mathbb Q$ by $\mu_n$ or by the single primitive element $\zeta = \zeta_n$ generating $\mu_n$. It may be denoted $\mathbb Q(\zeta)$ or $\mathbb Q(\zeta_n)$.
Cyclotomic field extensions can likewise be defined for any field $K$, but in such a case a convenient transcendental function such as $e^{ix}$ may not always be available to generate primitive $n^{\mathrm{th}}$ roots of unity.

This article introduces the ring of integers of the number field $\mathbb Q(\zeta_n)$, its Galois group, the cyclotomic polynomials, etc., and partially reconstruct how E. Kummer attempted to prove the Fermat's Last Theorem (FLT) using arithmetic of cyclotomic fields.
<!-- PELICAN_END_SUMMARY -->

The group homomorphism $\mu_n \to \mu_n$ defined by $\zeta \mapsto \zeta^s$ for a fixed $s \in \mathbb Z$ is an automorphism if $(n,s) =1$.
This establishes a canonical ismorphism from the multiplicative group $\left( \mathbb Z /n\mathbb Z \right)^\times$ to the automorphism group $\mathrm{Aut}(\mu_n)$, by which the latter has cardinality $\phi(n)$, where $\phi$ is the Euler's totient function. [^Chandrasekharan1968].
This group can be shown to be the Galois group of $\mathbb Q(\zeta_n)$, which will be proved using the device of cyclotomic polynomials:
*[Euler's totient function]: the arithmetic function that counts the positive integers less than or equal to n that are relatively prime to n.

### Cyclotomic polynomials

The $n^{\mathrm{th}}$  cyclotomic polynomial may be defined as the monic, minimal polynomial in $\mathbb{Z}[x]$ for a primitive $n^{\mathrm{th}}$ root of unity.
As it must divide $(x^n -1)$, a constructive determination may be made by examining factorization of $(x^n-1)$ which for example is done in Kronecker (1901)[^Kronecker1901].
One may also consider the factorization
$$(x^n - 1) = \prod_{1 \leq k \leq n} \left( x - e^{2\pi ik/n} \right)$$
and directly define 
$$\Phi_n(x) = \prod_{1 \leq k \leq n;\ (k,n)=1} \left( x - e^{2\pi ik/n} \right)$$
as, when $d | n$, it follows $\Phi_d(x) | (x^n - 1)$.
$\Phi_n(x)$ is seen to have cardinality $\phi(n)$, where $\phi$ is Euler's totient.
Grouping the $n^{\mathrm{th}}$ roots of unity as primitive $d^{\mathrm{th}}$ roots for $d|n$ it follows:
$$(x^n-1) = \prod_{d | n} \Phi_d(x).$$

**Lemma**: $\Phi_n(x)$ is a monic polynomial in $\mathbb Z[x].$ 
[ ](Proof below follows Thangadurai (1999)[^Thangadurai1999].)

**Proof**:

Result is true for $n = 1$ with $\Phi_1(x) = x-1$.
For general case, assume by induction that result is true for all $d < n.$ 
That is to say, for all proper divisors $d|n,$ it is given $\Phi_d(x)$ is monic and in $\mathbb Z[x].$
Recall:
$$\Phi_n(x) = \frac{x^n -1}{\prod_{d | n,\ d \neq n} \Phi_d(x)}$$
and using the division algorithm, quotient of a monic polynomial in $\mathbb Z[x]$ by another is again monic in $\mathbb Z[x].$ **Q.E.D.**

The irreducibility is proved first for the easier case of primes and later extended.

### Irreducibility of the cyclotomic polynomials (prime case)
---------------------

The $n^{\mathrm{th}}$ cyclotomic polynomial is the monic polynomial in $\mathbb{Z}[x]$ that is a minimal polynomial for $\zeta_n$ over $\mathbb Q$.
Then the cylcotomic field $\mathbb{Q} (\zeta_n)$ turns out to be the splitting field of the cyclotomic polynomial $\Phi_n(x)$.
Its construction is simpler in the case where $n=p$, a prime number, and may be done as follows.

The cyclotomic polynomial is

$$\Phi_p(x) = \frac{x^p -1}{x -1} = x^{p-1} + \cdots + x + 1. $$

Substituting $x + 1$ for $x$,

$$\frac{(x+1)^p - 1}{x} = x^{p - 1} + \binom{p}{p-1}x^{p - 2} + \cdots + \binom{p}2 x + \binom{p}1,$$

where $\binom{n}{m}$ denotes the binomial coefficient. Applying Eisenstein's criterion, this polynomial is irreducible. 
Therefore so is the original polynomial $\Phi_p(x)$, as $x \mapsto x+1$ is an automorphism of the polynomial ring $\mathbb Q[x]$. 
Therefore $\Phi_p(x)$ is an irreducible polynomial whose roots are $p^{\mathrm{th}}$ roots of unity save $1$ itself. 
Therefore it factorizes to

$$\Phi_p(x) = (x- \zeta)(x- \zeta^2) \cdots (x-\zeta^{p-1}),$$

where $\zeta = \zeta_p$, and thus $\mathbb Q(\mu_p)$ is the splitting field of $\Phi_p(x)$.

### Ring of integers (prime case)

Let $\zeta = \zeta_p$ be primitive $p^{\mathrm{th}}$ root of unity, where $p$ is a prime.
Ring of integers of $\mathbb Q(\zeta)$ turns out to be $\mathbb{Z}[\zeta]$ which we prove as follows.

Clearly, $\mathbb Z[\zeta]$ is contained in the ring of integers $\mathcal O_K$ of $K=\mathbb Q(\zeta)$.

Suppose $r$ and $s$ are integers with $(p, rs) = 1$. Then, $r \equiv st\ (\mathrm{mod}\ p)$ for some $t$, which gives
$$\frac{\zeta^{r}-1}{\zeta^s-1} = \frac{\zeta^{st}-1}{\zeta^s-1} = 1 + \zeta^s + \zeta^{2s} + \cdots + \zeta^{(n-1)s} \in \mathbb Z[\zeta].$$

Similarly, $\frac{\zeta^{s}-1}{\zeta^t-1}$ also belongs to $\mathbb Z[\zeta]$. Therefore both are units of $\mathcal O_K$. 


*[FLT]: Fermat's Last Theorem

### Kummer's "proof" of FLT
------------------

For more details on Kummer's effort, please refer to chapter 1 of Washington[^Washington1997].

Let $p \geq 5$ be a prime and let $\zeta$ be primitive $p^{\mathrm{th}}$ root of unity. 
Then, $\Phi_p(x) = x^{p-1} + \cdots + x + 1$ and $x^p- 1 = (x-1)(x-\zeta )(x- \zeta^2) . \cdots . (x - \zeta^{p-1}).$
Replacing $x$ by $-x/y$, 

$$(x^p + y^p) = (x+y)(x + \zeta y)(x + \zeta^2 y) . \cdots . (x + \zeta^{p-1}y).$$

$\Phi_p(x)$ is of degree $p-1$ and irreducible with root $\zeta$; so $\zeta^{p-1} = -(1+ +\zeta + \cdots + \zeta^{p-2})$.
The set $\{ 1, \zeta , \zeta^2 , \ldots , \zeta^{p-2} \}$ forms a basis for $\mathbb Q(\zeta)$ considered as a vector space over $\mathbb Q$.
It also forms a basis for the ring $\mathbb Z [\zeta]$ considered as a module over $\mathbb Z$.

The Fermat equation factorizes in $\mathbb Z[\zeta]$ as:

$$z^p = (x+y)(x + \zeta y)(x + \zeta^2 y) . \cdots . (x + \zeta^{p-1}y) $$

### Irreducibility of cyclotomic polynomial (general case)

Generally, the $n^{\mathrm{th}}$ cyclotomic polynomial is defined as the monic, minimal polynomial in $\mathbb{Z}[x]$ for a primitive $n^{\mathrm{th}}$ root of unity.
In the case $n = p$, this agrees with $\Phi_p(x)$ defined earlier because any $n^{\mathrm{th}}$ root of $1$ satisfies the polynomial $x^n -1$  and $x^p-1$ factorizes as $(x-1)\Phi_p(x)$ into irreducibles.


### Galois group

This is a Galois extension with Galois group the multiplicative group 
$\left(\mathbb{Z}/n\mathbb{Z} \right)^\times$ of the ring $\left(\mathbb{Z}/n\mathbb{Z} \right)$. 

--------------
### Bibliography
--------------

[^Gauss1801]: Gauss, Carl Friedrich, [Disquisitiones Arithmeticae](http://gdz.sub.uni-goettingen.de/dms/load/img/?PID=PPN235993352), 1801.

[^Washington1997]: Washington, Lawrence C., Introduction to Cyclotomic Fields, Graduate Texts in Mathematics 83, Springer-Verlag, New York, 1997.

[^Lang1990]: Lang, S., Cyclotomic Fields I and II, Graduate Texts in Mathematics, 121. Springer-Verlag, New York, 1990. 

[^Kronecker1901]: Kronecker, L., [Vorlesungen über Zahlentheorie](https://archive.org/details/vorlesungenberz00krongoog), Springer, 1901.

[^vanderWaerden1930]: van der Waerden, B. L., Moderne Algebra, 1930; Algebra I & II, Springer, 1991.

[^Prosolov2001]: Prosolov, V. V., Polynomials, Springer, 2001.

[^Chandrasekharan1968]: Chandrasekharan, K., Introduction to Analytic Number Theory, Springer, 1968.

[ ]([^Thangadurai1999]: Thangadurai, R., [On the Coefficients of Cyclotomic Polynomials](http://bprim.org/cyclotomicfieldbook/th.pdf).)


