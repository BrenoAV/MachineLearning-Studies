import matplotlib.pyplot as plt
import numpy as np
from scipy.special import rel_entr
from scipy.stats import norm

# First Normal Dist
mean_1 = 200
std_1 = 10
# Second Normal Dist
mean_2 = 210
std_2 = 20

x = np.linspace(
    min(mean_1, mean_2) - 3 * min(std_1, std_2),
    max(mean_1, mean_2) + 3 * max(std_1, std_2),
    100,
)
pdf_1 = norm.pdf(x, loc=mean_1, scale=std_1)
pdf_2 = norm.pdf(x, loc=mean_2, scale=std_2)

# %% Plots

plt.plot(x, pdf_1, color="g", label="Dist 1")
plt.plot(x, pdf_2, color="b", label="Dist 2")
plt.legend()
plt.title("Two differents normal distribution with the same std and different means")
plt.show()

# %% Compute the KL divergence

Dkl = rel_entr(pdf_1, pdf_2)
print(f"Kullback-Leibler Divergence = {sum(Dkl)}")
