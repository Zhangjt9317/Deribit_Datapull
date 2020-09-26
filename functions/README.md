## Smoothing 

pseudocode as the following:

```
# initialize time step 0 using state priors and observation dist p(y | x = s)
for si in states:
    alpha[t = 0, state = si] = pi[si] * p(y[0] | x = si)

# determine alpha for t = 1 .. n
for t in1 .. n:
    for sj in states:
        alpha[t,sj] = max([alpha[t-1,si] * M[si,sj] for si in states]) * p(y[t] | x = sj)

# determine current state at time t
return argmax(alpha[t,si] over si)
```