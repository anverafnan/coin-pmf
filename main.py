import scipy.stats as stats

prob_1=stats.binom.pmf(3,10,0.5)
print("probablity of getting 3 heads :",prob_1)

prob_2=1-stats.binom.pmf(0,10,0.5) - stats.binom.pmf(1,10,0.5) - stats.binom.pmf(2,10,0.5)
print("probablity of 2 heads :")
print(prob_2)