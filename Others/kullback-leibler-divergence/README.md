# Kullback-Leibler Divergence

**KL Divergence** measure the "distance" between two distributions, i.e. $p(x)$ and $q(x)$ where $p(x) > 0$ and $q(x) > 0$ for every $x \in X$.

- Discrete Case:

$$ D_{KL} = (p(x) || q(x) = \sum_{x \in X} p(x) \ln \frac{p(x)}{q(x)} $$

- Continuous Case:

$$ D_{KL} = \int_{-\infty}^{\infty} p(x) \ln \frac{p(x)}{q(x)}\,dx $$

- The $p(x)$ is the theory or true model and $q(x)$ is the model which we are to testing
- The $D_{KL}$ is not symmetric: $p(x)$ to $q(x)$ is different from $q(x)$ to $q(x)$
- The $D_{KL}$ is non-negative number, and if $D_{KL} = 0$ means that $p(x) = q(x)$
- In general, is used a Smoothly alternative which include a constant $\epsilon = e^{-3}$ to avoid if exists a event "$e$" in $p(e) > 0$ and $q(e) = 0$ for avoiding the zero division.
