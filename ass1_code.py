#### ASSIGNMENT 1 
#### BY- RUSHAT CHOPRA (20854690)

from email import header
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import statistics
import scipy
import statsmodels.tsa.stattools 
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf
import random

### QUESTION 3
## PART 1
#### The stocks picked are as follows:
#### Amazon, Blackstone, Berkshire Hathaway , NVIDIA and volkswagen.
warnings.filterwarnings("ignore")
amazon = pd.read_csv("/Users/rushatchopra/Desktop/3B term/ECON 423/data/AMZN.csv")
blackstone = pd.read_csv("/Users/rushatchopra/Desktop/3B term/ECON 423/data/BX.csv")
bhathtaway = pd.read_csv("/Users/rushatchopra/Desktop/3B term/ECON 423/data/BRK-B.csv")
NVIDIA = pd.read_csv("/Users/rushatchopra/Desktop/3B term/ECON 423/data/NVDA.csv")
volkswagen = pd.read_csv("/Users/rushatchopra/Desktop/3B term/ECON 423/data/VWAGY.csv")


##------------------------------------------------------------------------------------------------------------------


## PART 2
## creating a histogram ::

# amazon:
fig1_amazon = plt.figure(figsize=(15,5))
ax = plt.gca()
amazon["Adj Close"].plot(ax=ax, figsize=(15,5))
plt.title("Amazon Price")
plt.ylabel("Adjusted close price")
acf_a= statsmodels.tsa.stattools.acf(amazon["Adj Close"])
plot_acf(acf_a)  ### plotting acf with acf result
sm.graphics.tsa.plot_acf(blackstone["Adj Close"], lags=50) ### acf of closing price with 50 lags
mean_amazon = statistics.mean(amazon["Adj Close"])
var_amazon = statistics.variance(amazon["Adj Close"])
skew_amazon = scipy.stats.skew(amazon["Adj Close"])
kurt_amazon = scipy.stats.kurtosis(amazon["Adj Close"])
 
# blackstone : 
fig1_blackstone = plt.figure(figsize=(15,5))
ax = plt.gca()
blackstone["Adj Close"].plot(ax=ax, figsize=(15,5))
plt.title("Blackstone Price")
plt.ylabel("Adjusted close price")
acf_a= statsmodels.tsa.stattools.acf(blackstone["Adj Close"])
plot_acf(acf_a) ### plotting acf with acf result
sm.graphics.tsa.plot_acf(blackstone["Adj Close"], lags=50) ### acf of closing price with 50 lags
mean_blackstone = statistics.mean(blackstone["Adj Close"])
var_blackstone = statistics.variance(blackstone["Adj Close"])
skew_blackstone = scipy.stats.skew(blackstone["Adj Close"])
kurt_blackstone = scipy.stats.kurtosis(blackstone["Adj Close"])

# bhathtaway : 
fig1_bhathtaway = plt.figure(figsize=(15,5))
ax = plt.gca()
bhathtaway["Adj Close"].plot(ax=ax, figsize=(15,5))
plt.title("fig1_bhathtaway Price")
plt.ylabel("Adjusted close price")
acf_a= statsmodels.tsa.stattools.acf(bhathtaway["Adj Close"])
plot_acf(acf_a)### plotting acf with acf result
sm.graphics.tsa.plot_acf(bhathtaway["Adj Close"], lags=50) ### acf of closing price with 50 lags
mean_bhathtaway = statistics.mean(bhathtaway["Adj Close"])
var_bhathtaway = statistics.variance(bhathtaway["Adj Close"])
skew_bhathtaway = scipy.stats.skew(bhathtaway["Adj Close"])
kurt_bhathtaway = scipy.stats.kurtosis(bhathtaway["Adj Close"])


# NVIDIA: 
fig1_NVIDIA = plt.figure(figsize=(15,5))
ax = plt.gca()
NVIDIA["Adj Close"].plot(ax=ax, figsize=(15,5))
plt.title("NVIDIA Price")
plt.ylabel("Adjusted close price")
acf_a= statsmodels.tsa.stattools.acf(NVIDIA["Adj Close"])
plot_acf(acf_a)### plotting acf with acf result
sm.graphics.tsa.plot_acf(NVIDIA["Adj Close"], lags=50) ### acf of closing price with 50 lags
mean_NVIDIA = statistics.mean(NVIDIA["Adj Close"])
var_NVIDIA = statistics.variance(NVIDIA["Adj Close"])
skew_NVIDIA = scipy.stats.skew(NVIDIA["Adj Close"])
kurt_NVIDIA = scipy.stats.kurtosis(NVIDIA["Adj Close"])


# volkswagen:
fig1_volkswagen = plt.figure(figsize=(15,5))
ax = plt.gca()
volkswagen["Adj Close"].plot(ax=ax, figsize=(15,5))
plt.title("volkswagen Price")
plt.ylabel("Adjusted close price")
acf_a= statsmodels.tsa.stattools.acf(volkswagen["Adj Close"])
sm.graphics.tsa.plot_acf(volkswagen["Adj Close"], lags=50)  ### acf of closing price with 50 lags
plot_acf(acf_a)### plotting acf with acf result
mean_volkswagen = statistics.mean(volkswagen["Adj Close"])
var_volkswagen = statistics.variance(volkswagen["Adj Close"])
skew_volkswagen = scipy.stats.skew(volkswagen["Adj Close"])
kurt_volkswagen = scipy.stats.kurtosis(volkswagen["Adj Close"])


#------------------------------------------------------------------------------------------------------------------

 ##### PART 3 :
### Daily percentage change : 

### AMAZON : 
returns_amazon = 100*(np.log(amazon["Adj Close"].shift(1))-np.log(amazon["Adj Close"]))
returns_amazon[0]= 0
mean_amazon_rt = np.nanmean(returns_amazon) 
var_amazon_rt = np.nanvar(returns_amazon) 
skew_amazon_rt = scipy.stats.skew(returns_amazon,nan_policy='omit')
kurt_amazon_rt = scipy.stats.kurtosis(returns_amazon,nan_policy='omit')
### daily amazon returns histogram : 
returns_amazon.plot(figsize=(15,5), title = "Amazon Daily Returns")
acf_rt = statsmodels.tsa.stattools.acf(returns_amazon) 
### actual ACF plot:
sm.graphics.tsa.plot_acf(returns_amazon, lags=50)

## blackstone :
returns_blackstone = 100*(np.log(blackstone["Adj Close"].shift(1))-np.log(blackstone["Adj Close"]))
returns_blackstone[0]= 0
mean_rt = np.nanmean(returns_blackstone) 
var_rt = np.nanvar(returns_blackstone) 
skew_rt = scipy.stats.skew(returns_blackstone,nan_policy='omit')
kurt_rt = scipy.stats.kurtosis(returns_blackstone,nan_policy='omit')
### daily blackstone returns histogram : 
returns_blackstone.plot(figsize=(15,5), title = "Blackstone Daily Returns")
acf_rt = statsmodels.tsa.stattools.acf(returns_blackstone) 
### actual ACF plot:
sm.graphics.tsa.plot_acf(returns_blackstone, lags=50)

### bhathtaway: 
returns_bhathtaway = 100*(np.log(bhathtaway["Adj Close"].shift(1))-np.log(bhathtaway["Adj Close"]))
returns_bhathtaway[0]= 0
mean_rt = np.nanmean(returns_bhathtaway) 
var_rt = np.nanvar(returns_bhathtaway) 
skew_rt = scipy.stats.skew(returns_bhathtaway,nan_policy='omit')
kurt_rt = scipy.stats.kurtosis(returns_bhathtaway,nan_policy='omit')
### Berkshire Hathaway returns histogram : 
returns_bhathtaway.plot(figsize=(15,5), title = "Berkshire Hathaway Daily Returns")
acf_rt = statsmodels.tsa.stattools.acf(returns_bhathtaway) 
### actual ACF plot:
sm.graphics.tsa.plot_acf(returns_bhathtaway, lags=50)


# NVIDIA: 
returns_NVIDIA = 100*(np.log(amazon["Adj Close"].shift(1))-np.log(amazon["Adj Close"]))
returns_NVIDIA[0]= 0
mean_rt = np.nanmean(returns_NVIDIA) 
var_rt = np.nanvar(returns_NVIDIA) 
skew_rt = scipy.stats.skew(returns_NVIDIA,nan_policy='omit')
kurt_rt = scipy.stats.kurtosis(returns_NVIDIA,nan_policy='omit')
### daily NVIDIA returns histogram : 
returns_NVIDIA.plot(figsize=(15,5), title = "NVIDIA Daily Returns")
acf_rt = statsmodels.tsa.stattools.acf(returns_NVIDIA) 
### actual ACF plot:
sm.graphics.tsa.plot_acf(returns_NVIDIA, lags=50)


# volkswagen:
returns_volkswagen = 100*(np.log(amazon["Adj Close"].shift(1))-np.log(amazon["Adj Close"]))
returns_volkswagen[0]= 0
mean_rt = np.nanmean(returns_volkswagen) 
var_rt = np.nanvar(returns_volkswagen) 
skew_rt = scipy.stats.skew(returns_volkswagen,nan_policy='omit')
kurt_rt = scipy.stats.kurtosis(returns_volkswagen,nan_policy='omit')
### daily Volkswagen returns histogram : 
returns_volkswagen.plot(figsize=(15,5), title = "Volkswagen Daily Returns")
acf_rt = statsmodels.tsa.stattools.acf(returns_volkswagen) 
### actual ACF plot:
sm.graphics.tsa.plot_acf(returns_volkswagen, lags=50)

#------------------------------------------------------------------------------------------------------------------
# PART 4:
## For the Squared returns, we can just take the varinace as done in previous part.
amazon["squared-return"] = returns_amazon.pow(2)
acf_sqrt_amz = plot_acf(amazon["squared-return"]) # statsmodels.tsa.stattools.acf(amazon["squared-return"]) 
blackstone["squared-return"]= returns_blackstone.pow(2)
acf_sqrt_bls = plot_acf(blackstone["squared-return"])
bhathtaway["squared-return"] = returns_bhathtaway.pow(2)
acf_sqrt_bht = plot_acf(bhathtaway["squared-return"])
NVIDIA["squared-return"] = returns_NVIDIA.pow(2)
acf_sqrt_NVD = plot_acf(NVIDIA["squared-return"])
volkswagen["squared-return"] = returns_volkswagen.pow(2)
acf_sqrt_vlk = plot_acf(volkswagen["squared-return"])


# fig = px.histogram(probability, nbins=100)
plt.title("part 4 hist")
plt.hist(var_rt, bins=100)
plt.xlim(left = 1, right = 5)
plt.xticks(rotation = 90)


#------------------------------------------------------------------------------------------------------------------


#PART 5:

## amazon : 
dframe = pd.DataFrame(amazon['Volume'])
###  correlation between the return and trading volume for each : 
correlation_amazon = np.corrcoef(returns_amazon,amazon["Volume"] )
### also running a linear regression between the 2 to get more information : 
linear_regression_amazon  = scipy.stats.linregress(returns_amazon, amazon["Volume"]) 


## blackstone : 
dframe = pd.DataFrame(blackstone['Volume'])
###  correlation between the return and trading volume for each : 
correlation_blackstone = np.corrcoef(returns_blackstone,blackstone["Volume"] )
### also running a linear regression between the 2 to get more information : 
linear_regression_blackstone  = scipy.stats.linregress(returns_blackstone, blackstone["Volume"]) 


## bhathtaway : 
dframe = pd.DataFrame(bhathtaway['Volume'])
###  correlation between the return and trading volume for each : 
correlation_bhathtaway = np.corrcoef(returns_bhathtaway,bhathtaway["Volume"] )
### also running a linear regression between the 2 to get more information : 
linear_regression_bhathtaway  = scipy.stats.linregress(returns_bhathtaway, bhathtaway["Volume"]) 



## NVIDIA : 
dframe = pd.DataFrame(NVIDIA['Volume'])
###  correlation between the return and trading volume for each : 
correlation_NVIDIA = np.corrcoef(returns_NVIDIA,NVIDIA["Volume"] )
### also running a linear regression between the 2 to get more information : 
linear_regression_NVIDIA  = scipy.stats.linregress(returns_NVIDIA, NVIDIA["Volume"]) 



## volkswagen : 
dframe = pd.DataFrame(volkswagen['Volume'])
###  correlation between the return and trading volume for each : 
correlation_volkswagen = np.corrcoef(returns_volkswagen,volkswagen["Volume"] )
### also running a linear regression between the 2 to get more information : 
linear_regression_volkswagen  = scipy.stats.linregress(returns_volkswagen, volkswagen["Volume"]) 


#------------------------------------------------------------------------------------------------------------------

### PART 6 :
## Taking the returns to figure if there has been an icnrease or decrease
## if an increase, we take 1 and if there is a decease, we take 0.

### AMAZON : 
amazon["P(t)"] = ""
amz_count_inc_t = 0   ### count of times that the price has increased in time t
amz_count_dec_t = 0   ### count of times that the price has decreased in time t
for i in range(len(returns_amazon.shift(1))): ## Taking a lag of 1 for P(t)
    if returns_amazon[i]>=0:
        amazon["P(t)"][i+1] = 1
        amz_count_inc_t +=1
    else:
        amazon["P(t)"][i+1] = 0
        amz_count_dec_t +=1

amazon["P(t-1)"] = ""
amz_count_inc_t1 = 0 ### count of times that the price has increased in time t-1
amz_count_dec_t1 = 0 ### count of times that the price has decreased in time t-1
for i in range(len(returns_amazon)):
    if returns_amazon[i]>=0:
        amazon["P(t-1)"][i] = 1
        amz_count_inc_t1 += 1
    else:
        amazon["P(t-1)"][i] = 0
        amz_count_dec_t1 += 1

# print(amazon)
# print(count_inc_t1, count_inc_t1)

amz_t_t1_increase = 0  ### count of times that t and t-1 have increased
amz_t_t1_decrease = 0  ### count of times that t and t-1 have decreased
amz_t_inc_t1_dec = 0    ### count of times that t has increased and t-1 has decreased
amz_t_dec_t1_inc = 0   ### count of times that t has decreased and t-1 has increased
for j in range(len(returns_amazon)-1):
    if amazon["P(t-1)"][j+1]== amazon["P(t)"][j]: ### for case 1 and 4
        if amazon["P(t)"][j] == 1:
            amz_t_t1_increase += 1
        else: 
            amz_t_t1_decrease +=1
    else : 
            if amazon["P(t)"][j] == 1:
                amz_t_inc_t1_dec +=1
            else: 
                amz_t_dec_t1_inc  +=1

### Thus, the probability will be as follows: 
### probabilities will be as follows: 
## i) Prob (stock price increases at t | stock price increases at t − 1):
amz_prob_1a = amz_t_t1_increase/amz_count_inc_t1

# ii) Prob (stock price increases at t | stock price decreases at t − 1):
amz_prob_1b =  amz_t_inc_t1_dec/amz_count_dec_t1

# iii) Prob (stock price decreases at t | stock price increases at t − 1):
amz_prob_1c = amz_t_dec_t1_inc/amz_count_inc_t1

# iv) Prob (stock price decreases at t | stock price decreases at t − 1)
amz_prob_1d = amz_t_t1_decrease/ amz_count_dec_t1

print(amz_prob_1a,amz_prob_1b,amz_prob_1c,amz_prob_1d)


###   Blackstone :
 
blackstone["P(t)"] = ""
bls_count_inc_t = 0   ### count of times that the price has increased in time t
bls_count_dec_t = 0   ### count of times that the price has decreased in time t
for i in range(len(returns_blackstone.shift(1))): ## Taking a lag of 1 for P(t)
    if returns_blackstone[i]>=0:
        blackstone["P(t)"][i+1] = 1
        bls_count_inc_t +=1
    else:
        blackstone["P(t)"][i+1] = 0
        bls_count_dec_t +=1

blackstone["P(t-1)"] = ""
bls_count_inc_t1 = 0 ### count of times that the price has increased in time t-1
bls_count_dec_t1 = 0 ### count of times that the price has decreased in time t-1
for i in range(len(returns_blackstone)):
    if returns_blackstone[i]>=0:
        blackstone["P(t-1)"][i] = 1
        bls_count_inc_t1 += 1
    else:
        blackstone["P(t-1)"][i] = 0
        bls_count_dec_t1 += 1


bls_t_t1_increase = 0  ### count of times that t and t-1 have increased
bls_t_t1_decrease = 0  ### count of times that t and t-1 have decreased
bls_t_inc_t1_dec = 0    ### count of times that t has increased and t-1 has decreased
bls_t_dec_t1_inc = 0   ### count of times that t has decreased and t-1 has increased
for j in range(len(returns_blackstone)-1):
    if blackstone["P(t-1)"][j+1]== blackstone["P(t)"][j]: ### for case 1 and 4
        if blackstone["P(t)"][j] == 1:
            bls_t_t1_increase += 1
        else: 
            bls_t_t1_decrease +=1
    else : 
            if blackstone["P(t)"][j] == 1:
                bls_t_inc_t1_dec +=1
            else: 
                bls_t_dec_t1_inc  +=1

### Thus, the probability will be as follows: 
### probabilities will be as follows: 
## i) Prob (stock price increases at t | stock price increases at t − 1):
bls_prob_1a = bls_t_t1_increase/bls_count_inc_t1

# ii) Prob (stock price increases at t | stock price decreases at t − 1):
bls_prob_1b =  bls_t_inc_t1_dec/bls_count_dec_t1

# iii) Prob (stock price decreases at t | stock price increases at t − 1):
bls_prob_1c = bls_t_dec_t1_inc/bls_count_inc_t1

# iv) Prob (stock price decreases at t | stock price decreases at t − 1)
bls_prob_1d = bls_t_t1_decrease/ bls_count_dec_t1


print(bls_prob_1a,bls_prob_1b,bls_prob_1c,bls_prob_1d)



##   BERKSHIRE HATHAWAY :
 
bhathtaway["P(t)"] = ""
bht_count_inc_t = 0   ### count of times that the price has increased in time t
bht_count_dec_t = 0   ### count of times that the price has decreased in time t
for i in range(len(returns_bhathtaway.shift(1))): ## Taking a lag of 1 for P(t)
    if returns_bhathtaway[i]>=0:
        bhathtaway["P(t)"][i+1] = 1
        bht_count_inc_t +=1
    else:
        bhathtaway["P(t)"][i+1] = 0
        bht_count_dec_t +=1

bhathtaway["P(t-1)"] = ""
bht_count_inc_t1 = 0 ### count of times that the price has increased in time t-1
bht_count_dec_t1 = 0 ### count of times that the price has decreased in time t-1
for i in range(len(returns_bhathtaway)):
    if returns_bhathtaway[i]>=0:
        bhathtaway["P(t-1)"][i] = 1
        bht_count_inc_t1 += 1
    else:
        bhathtaway["P(t-1)"][i] = 0
        bht_count_dec_t1 += 1


bht_t_t1_increase = 0  ### count of times that t and t-1 have increased
bht_t_t1_decrease = 0  ### count of times that t and t-1 have decreased
bht_t_inc_t1_dec = 0    ### count of times that t has increased and t-1 has decreased
bht_t_dec_t1_inc = 0   ### count of times that t has decreased and t-1 has increased
for j in range(len(returns_bhathtaway)-1):
    if bhathtaway["P(t-1)"][j+1]== bhathtaway["P(t)"][j]: ### for case 1 and 4
        if bhathtaway["P(t)"][j] == 1:
            bht_t_t1_increase += 1
        else: 
            bht_t_t1_decrease +=1
    else : 
            if bhathtaway["P(t)"][j] == 1:
                bht_t_inc_t1_dec +=1
            else: 
                bht_t_dec_t1_inc  +=1

### Thus, the probability will be as follows: 
### probabilities will be as follows: 
## i) Prob (stock price increases at t | stock price increases at t − 1):
bht_prob_1a = bht_t_t1_increase/bht_count_inc_t1

# ii) Prob (stock price increases at t | stock price decreases at t − 1):
bht_prob_1b =  bht_t_inc_t1_dec/bht_count_dec_t1

# iii) Prob (stock price decreases at t | stock price increases at t − 1):
bht_prob_1c = bht_t_dec_t1_inc/bht_count_inc_t1

# iv) Prob (stock price decreases at t | stock price decreases at t − 1)
bht_prob_1d = bht_t_t1_decrease/ bht_count_dec_t1


print(bht_prob_1a,bht_prob_1b,bht_prob_1c,bht_prob_1d)


# # # NVIDIA: 
NVIDIA["P(t)"] = ""
NVD_count_inc_t = 0   ### count of times that the price has increased in time t
NVD_count_dec_t = 0   ### count of times that the price has decreased in time t
for i in range(len(returns_NVIDIA.shift(1))): ## Taking a lag of 1 for P(t)
    if returns_NVIDIA[i]>=0:
        NVIDIA["P(t)"][i+1] = 1
        NVD_count_inc_t +=1
    else:
        NVIDIA["P(t)"][i+1] = 0
        NVD_count_inc_t +=1

NVIDIA["P(t-1)"] = ""
NVD_count_inc_t1 = 0 ### count of times that the price has increased in time t-1
NVD_count_dec_t1 = 0 ### count of times that the price has decreased in time t-1
for i in range(len(returns_NVIDIA)):
    if returns_NVIDIA[i]>=0:
        NVIDIA["P(t-1)"][i] = 1
        NVD_count_inc_t1 += 1
    else:
        NVIDIA["P(t-1)"][i] = 0
        NVD_count_dec_t1 += 1


NVD_t_t1_increase = 0  ### count of times that t and t-1 have increased
NVD_t_t1_decrease = 0  ### count of times that t and t-1 have decreased
NVD_t_inc_t1_dec = 0    ### count of times that t has increased and t-1 has decreased
NVD_t_dec_t1_inc = 0   ### count of times that t has decreased and t-1 has increased
for j in range(len(returns_NVIDIA)-1):
    if NVIDIA["P(t-1)"][j+1]== NVIDIA["P(t)"][j]: ### for case 1 and 4
        if NVIDIA["P(t)"][j] == 1:
            NVD_t_t1_increase += 1
        else: 
            NVD_t_t1_decrease +=1
    else : 
            if NVIDIA["P(t)"][j] == 1:
                NVD_t_inc_t1_dec +=1
            else: 
                NVD_t_dec_t1_inc  +=1

### Thus, the probability will be as follows: 
### probabilities will be as follows: 
## i) Prob (stock price increases at t | stock price increases at t − 1):
NVD_prob_1a = NVD_t_t1_increase/NVD_count_inc_t1

# ii) Prob (stock price increases at t | stock price decreases at t − 1):
NVD_prob_1b =  NVD_t_inc_t1_dec/NVD_count_dec_t1

# iii) Prob (stock price decreases at t | stock price increases at t − 1):
NVD_prob_1c = NVD_t_dec_t1_inc/NVD_count_inc_t1

# iv) Prob (stock price decreases at t | stock price decreases at t − 1)
NVD_prob_1d = NVD_t_t1_decrease/ NVD_count_dec_t1


print(NVD_prob_1a,NVD_prob_1b,NVD_prob_1c,NVD_prob_1d)



# # # VOLKSWAGEN: 
volkswagen["P(t)"] = ""
VLKS_count_inc_t = 0   ### count of times that the price has increased in time t
VLKS_count_dec_t = 0   ### count of times that the price has decreased in time t
for i in range(len(returns_volkswagen.shift(1))): ## Taking a lag of 1 for P(t)
    if returns_volkswagen[i]>=0:
        volkswagen["P(t)"][i+1] = 1
        VLKS_count_inc_t +=1
    else:
        volkswagen["P(t)"][i+1] = 0
        VLKS_count_dec_t +=1

volkswagen["P(t-1)"] = ""
VLKS_count_inc_t1 = 0 ### count of times that the price has increased in time t-1
VLKS_count_dec_t1 = 0 ### count of times that the price has decreased in time t-1
for i in range(len(returns_volkswagen)):
    if returns_volkswagen[i]>=0:
        volkswagen["P(t-1)"][i] = 1
        VLKS_count_inc_t1 += 1
    else:
        volkswagen["P(t-1)"][i] = 0
        VLKS_count_dec_t1 += 1


VLKS_t_t1_increase = 0  ### count of times that t and t-1 have increased
VLKS_t_t1_decrease = 0  ### count of times that t and t-1 have decreased
VLKS_t_inc_t1_dec = 0    ### count of times that t has increased and t-1 has decreased
VLKS_t_dec_t1_inc = 0   ### count of times that t has decreased and t-1 has increased
for j in range(len(returns_volkswagen)-1):
    if volkswagen["P(t-1)"][j+1]== volkswagen["P(t)"][j]: ### for case 1 and 4
        if volkswagen["P(t)"][j] == 1:
            VLKS_t_t1_increase += 1
        else: 
            VLKS_t_t1_decrease +=1
    else : 
            if volkswagen["P(t)"][j] == 1:
                VLKS_t_inc_t1_dec +=1
            else: 
                VLKS_t_dec_t1_inc  +=1

### Thus, the probability will be as follows: 
### probabilities will be as follows: 
## i) Prob (stock price increases at t | stock price increases at t − 1):
VLKS_prob_1a = VLKS_t_t1_increase/VLKS_count_inc_t1

# ii) Prob (stock price increases at t | stock price decreases at t − 1):
VLKS_prob_1b =  VLKS_t_inc_t1_dec/VLKS_count_dec_t1

# iii) Prob (stock price decreases at t | stock price increases at t − 1):
VLKS_prob_1c = VLKS_t_dec_t1_inc/VLKS_count_inc_t1

# iv) Prob (stock price decreases at t | stock price decreases at t − 1)
VLKS_prob_1d = VLKS_t_t1_decrease/ VLKS_count_dec_t1


print(VLKS_prob_1a,VLKS_prob_1b,VLKS_prob_1c,VLKS_prob_1d)


#------------------------------------------------------------------------------------------------------------------

##### PART 7:


### For amazon:

## trading volume change between t and t-1
amazon["Trading Change"] = ""
for t in range(len(amazon["Volume"])):
    if t+1 != len(amazon["Volume"]):
        amazon["Trading Change"][t] = amazon["Volume"][t+1] - amazon["Volume"][t]
    else: 
        amazon["Trading Change"][t] = 0 - amazon["Volume"][t]

## creating new column for time t
amazon["Trading(t)"] = ""
amz_count_inc_trading_t = 0  ### count of times that the volume has increased in time t
amz_ount_dec_trading_t = 0   ### count of times that the volume has decreased in time t
for i in range(len(amazon["Trading Change"].shift(1))):
    if amazon["Trading Change"][i]>=0:
        amazon["Trading(t)"][i+1] = 1
        amz_count_inc_trading_t +=1
    else:
        amazon["Trading(t)"][i+1] = 0
        amz_ount_dec_trading_t +=1

## creating new column for time t-1
amazon["Trading(t-1)"] = ""
amz_count_inc_trading_t1 = 0   ### count of times that the volume has increased in time t -1
amz_count_dec_trading_t1 = 0   ### count of times that the volume has decreased in time t -1
for i in range(len(returns_amazon)):
    if returns_amazon[i]>=0:
        amazon["Trading(t-1)"][i] = 1
        amz_count_inc_trading_t1 += 1
    else:
        amazon["Trading(t-1)"][i] = 0
        amz_count_dec_trading_t1 += 1

# print(amazon)
amz_trading_t_t1_increase = 0   ### count of times that the volume has increased in time t and t-1
amz_trading_t_t1_decrease = 0   ### count of times that the volume has decreased in time t and t-1
amz_trading_t_inc_t1_dec = 0    ### count of times that the volume has increased in time t and decreased in t-1
amz_trading_t_dec_t1_inc = 0    ### count of times that the volume has decreased in time t and increased in t-1
for j in range(len(amazon["Trading Change"])-1):
    if amazon["Trading(t-1)"][j+1]== amazon["Trading(t)"][j]: ### for case 1 and 4
        if amazon["Trading(t)"][j] == 1:
            amz_trading_t_t1_increase += 1
        else: 
            amz_trading_t_t1_decrease +=1
    else : 
            if amazon["Trading(t)"][j] == 1:
                amz_trading_t_inc_t1_dec +=1
            else: 
                amz_trading_t_dec_t1_inc  +=1

### Thus, the probability will be as follows: 
### probabilities will be as follows: 
## i) Prob (stock price increases at t | stock price increases at t − 1):
amz_prob_2a = amz_trading_t_t1_increase/amz_count_inc_trading_t1

# ii) Prob (stock price increases at t | stock price decreases at t − 1):
amz_prob_2b =  amz_trading_t_inc_t1_dec/amz_count_dec_trading_t1

# iii) Prob (stock price decreases at t | stock price increases at t − 1):
amz_prob_2c = amz_trading_t_dec_t1_inc/amz_count_inc_trading_t1

# iv) Prob (stock price decreases at t | stock price decreases at t − 1)
amz_prob_2d = amz_trading_t_t1_decrease/ amz_count_dec_trading_t1

print(amz_prob_2a,amz_prob_2b,amz_prob_2c,amz_prob_2d)

### BLACKSTONE :

## trading volume change between t and t-1
blackstone["Trading Change"] = ""
for t in range(len(blackstone["Volume"])):
    if t+1 != len(blackstone["Volume"]):
        blackstone["Trading Change"][t] = blackstone["Volume"][t+1] - blackstone["Volume"][t]
    else: 
        blackstone["Trading Change"][t] = 0 - blackstone["Volume"][t]

## creating new column for time t
blackstone["Trading(t)"] = ""
blk_count_inc_trading_t = 0  ### count of times that the volume has increased in time t
blk_count_dec_trading_t = 0   ### count of times that the volume has decreased in time t
for i in range(len(blackstone["Trading Change"].shift(1))):
    if blackstone["Trading Change"][i]>=0:
        blackstone["Trading(t)"][i+1] = 1
        blk_count_inc_trading_t +=1
    else:
        blackstone["Trading(t)"][i+1] = 0
        blk_count_dec_trading_t +=1

## creating new column for time t-1
blackstone["Trading(t-1)"] = ""
blk_count_inc_trading_t1 = 0   ### count of times that the volume has increased in time t -1
blk_count_dec_trading_t1 = 0   ### count of times that the volume has decreased in time t -1
for i in range(len(returns_amazon)):
    if returns_amazon[i]>=0:
        blackstone["Trading(t-1)"][i] = 1
        blk_count_inc_trading_t1 += 1
    else:
        blackstone["Trading(t-1)"][i] = 0
        blk_count_dec_trading_t1 += 1

# print(amazon)
blk_trading_t_t1_increase = 0   ### count of times that the volume has increased in time t and t-1
blk_trading_t_t1_decrease = 0   ### count of times that the volume has decreased in time t and t-1
blk_trading_t_inc_t1_dec = 0    ### count of times that the volume has increased in time t and decreased in t-1
blk_trading_t_dec_t1_inc = 0    ### count of times that the volume has decreased in time t and increased in t-1
for j in range(len(blackstone["Trading Change"])-1):
    if blackstone["Trading(t-1)"][j+1]== blackstone["Trading(t)"][j]: ### for case 1 and 4
        if blackstone["Trading(t)"][j] == 1:
            blk_trading_t_t1_increase += 1
        else: 
            blk_trading_t_t1_decrease +=1
    else : 
            if blackstone["Trading(t)"][j] == 1:
                blk_trading_t_inc_t1_dec +=1
            else: 
                blk_trading_t_dec_t1_inc  +=1

### Thus, the probability will be as follows: 
### probabilities will be as follows: 
## i) Prob (stock price increases at t | stock price increases at t − 1):
blk_prob_2a = bls_t_t1_increase/blk_count_inc_trading_t1

# ii) Prob (stock price increases at t | stock price decreases at t − 1):
blk_prob_2b =  bls_t_inc_t1_dec/blk_count_dec_trading_t1

# iii) Prob (stock price decreases at t | stock price increases at t − 1):
blk_prob_2c = bls_t_dec_t1_inc/blk_count_inc_trading_t1

# iv) Prob (stock price decreases at t | stock price decreases at t − 1)
blk_prob_2d = bls_t_t1_decrease/ blk_count_dec_trading_t1

print(blk_prob_2a,blk_prob_2b,blk_prob_2c,blk_prob_2d)


### BERKSHIRE HATHAWAY :

## trading volume change between t and t-1
bhathtaway["Trading Change"] = ""
for t in range(len(bhathtaway["Volume"])):
    if t+1 != len(bhathtaway["Volume"]):
        bhathtaway["Trading Change"][t] = bhathtaway["Volume"][t+1] - bhathtaway["Volume"][t]
    else: 
        bhathtaway["Trading Change"][t] = 0 - bhathtaway["Volume"][t]

## creating new column for time t
bhathtaway["Trading(t)"] = ""
bth_count_inc_trading_t = 0  ### count of times that the volume has increased in time t
bth_count_dec_trading_t = 0   ### count of times that the volume has decreased in time t
for i in range(len(bhathtaway["Trading Change"].shift(1))):
    if bhathtaway["Trading Change"][i]>=0:
        bhathtaway["Trading(t)"][i+1] = 1
        bth_count_inc_trading_t +=1
    else:
        bhathtaway["Trading(t)"][i+1] = 0
        bth_count_dec_trading_t +=1

## creating new column for time t-1
bhathtaway["Trading(t-1)"] = ""
bth_count_inc_trading_t1 = 0   ### count of times that the volume has increased in time t -1
bth_count_dec_trading_t1 = 0   ### count of times that the volume has decreased in time t -1
for i in range(len(returns_amazon)):
    if returns_amazon[i]>=0:
        bhathtaway["Trading(t-1)"][i] = 1
        bth_count_inc_trading_t1 += 1
    else:
        bhathtaway["Trading(t-1)"][i] = 0
        bth_count_dec_trading_t1 += 1

# print(amazon)
bth_trading_t_t1_increase = 0   ### count of times that the volume has increased in time t and t-1
bth_trading_t_t1_decrease = 0   ### count of times that the volume has decreased in time t and t-1
bth_trading_t_inc_t1_dec = 0    ### count of times that the volume has increased in time t and decreased in t-1
bth_trading_t_dec_t1_inc = 0    ### count of times that the volume has decreased in time t and increased in t-1
for j in range(len(bhathtaway["Trading Change"])-1):
    if bhathtaway["Trading(t-1)"][j+1]== bhathtaway["Trading(t)"][j]: ### for case 1 and 4
        if bhathtaway["Trading(t)"][j] == 1:
            bth_trading_t_t1_increase += 1
        else: 
            bth_trading_t_t1_decrease +=1
    else : 
            if bhathtaway["Trading(t)"][j] == 1:
                bth_trading_t_inc_t1_dec +=1
            else: 
                bth_trading_t_dec_t1_inc  +=1

### Thus, the probability will be as follows: 
### probabilities will be as follows: 
## i) Prob (stock price increases at t | stock price increases at t − 1):
bth_prob_2a = bht_t_t1_increase/bth_count_inc_trading_t1

# ii) Prob (stock price increases at t | stock price decreases at t − 1):
bth_prob_2b =  bht_t_inc_t1_dec/bth_count_dec_trading_t1

# iii) Prob (stock price decreases at t | stock price increases at t − 1):
bth_prob_2c = bht_t_dec_t1_inc/bth_count_inc_trading_t1

# iv) Prob (stock price decreases at t | stock price decreases at t − 1)
bth_prob_2d = bht_t_t1_decrease/ bth_count_dec_trading_t1

print(bth_prob_2a,bth_prob_2b,bth_prob_2c,bth_prob_2d)

### NVIDIA :

## trading volume change between t and t-1
NVIDIA["Trading Change"] = ""
for t in range(len(NVIDIA["Volume"])):
    if t+1 != len(NVIDIA["Volume"]):
        NVIDIA["Trading Change"][t] = NVIDIA["Volume"][t+1] - NVIDIA["Volume"][t]
    else: 
        NVIDIA["Trading Change"][t] = 0 - NVIDIA["Volume"][t]

## creating new column for time t
NVIDIA["Trading(t)"] = ""
NVD_count_inc_trading_t = 0  ### count of times that the volume has increased in time t
NVD_count_dec_trading_t = 0   ### count of times that the volume has decreased in time t
for i in range(len(NVIDIA["Trading Change"].shift(1))):
    if NVIDIA["Trading Change"][i]>=0:
        NVIDIA["Trading(t)"][i+1] = 1
        NVD_count_inc_trading_t +=1
    else:
        NVIDIA["Trading(t)"][i+1] = 0
        NVD_count_dec_trading_t +=1

## creating new column for time t-1
NVIDIA["Trading(t-1)"] = ""
NVD_count_inc_trading_t1 = 0   ### count of times that the volume has increased in time t -1
NVD_count_dec_trading_t1 = 0   ### count of times that the volume has decreased in time t -1
for i in range(len(returns_amazon)):
    if returns_amazon[i]>=0:
        NVIDIA["Trading(t-1)"][i] = 1
        NVD_count_inc_trading_t1 += 1
    else:
        NVIDIA["Trading(t-1)"][i] = 0
        NVD_count_dec_trading_t1 += 1


NVD_trading_t_t1_increase = 0   ### count of times that the volume has increased in time t and t-1
NVD_trading_t_t1_decrease = 0   ### count of times that the volume has decreased in time t and t-1
NVD_trading_t_inc_t1_dec = 0    ### count of times that the volume has increased in time t and decreased in t-1
NVD_trading_t_dec_t1_inc = 0    ### count of times that the volume has decreased in time t and increased in t-1
for j in range(len(NVIDIA["Trading Change"])-1):
    if NVIDIA["Trading(t-1)"][j+1]== NVIDIA["Trading(t)"][j]: ### for case 1 and 4
        if NVIDIA["Trading(t)"][j] == 1:
            NVD_trading_t_t1_increase += 1
        else: 
            NVD_trading_t_t1_decrease +=1
    else : 
            if NVIDIA["Trading(t)"][j] == 1:
                NVD_trading_t_inc_t1_dec +=1
            else: 
                NVD_trading_t_dec_t1_inc  +=1

### Thus, the probability will be as follows: 
### probabilities will be as follows: 
## i) Prob (stock price increases at t | stock price increases at t − 1):
NVD_prob_2a = NVD_t_t1_increase/NVD_count_inc_trading_t1

# ii) Prob (stock price increases at t | stock price decreases at t − 1):
NVD_prob_2b =  NVD_t_inc_t1_dec/NVD_count_dec_trading_t1

# iii) Prob (stock price decreases at t | stock price increases at t − 1):
NVD_prob_2c = NVD_t_dec_t1_inc/NVD_count_inc_trading_t1

# iv) Prob (stock price decreases at t | stock price decreases at t − 1)
NVD_prob_2d = NVD_t_t1_decrease/ NVD_count_dec_trading_t1

print(NVD_prob_2a,NVD_prob_2b,NVD_prob_2c,NVD_prob_2d)


### VOLKSWAGEN :

## trading volume change between t and t-1
volkswagen["Trading Change"] = ""
for t in range(len(volkswagen["Volume"])):
    if t+1 != len(volkswagen["Volume"]):
        volkswagen["Trading Change"][t] = volkswagen["Volume"][t+1] - volkswagen["Volume"][t]
    else: 
        volkswagen["Trading Change"][t] = 0 - volkswagen["Volume"][t]

## creating new column for time t
volkswagen["Trading(t)"] = ""
VLKS_count_inc_trading_t = 0  ### count of times that the volume has increased in time t
VLKS_count_dec_trading_t = 0   ### count of times that the volume has decreased in time t
for i in range(len(volkswagen["Trading Change"].shift(1))):
    if volkswagen["Trading Change"][i]>=0:
        volkswagen["Trading(t)"][i+1] = 1
        VLKS_count_inc_trading_t +=1
    else:
        volkswagen["Trading(t)"][i+1] = 0
        VLKS_count_dec_trading_t +=1

## creating new column for time t-1
volkswagen["Trading(t-1)"] = ""
VLKS_count_inc_trading_t1 = 0   ### count of times that the volume has increased in time t -1
VLKS_count_dec_trading_t1 = 0   ### count of times that the volume has decreased in time t -1
for i in range(len(returns_amazon)):
    if returns_amazon[i]>=0:
        volkswagen["Trading(t-1)"][i] = 1
        VLKS_count_inc_trading_t1 += 1
    else:
        volkswagen["Trading(t-1)"][i] = 0
        VLKS_count_dec_trading_t1 += 1

# print(amazon)
VLKS_trading_t_t1_increase = 0   ### count of times that the volume has increased in time t and t-1
VLKS_trading_t_t1_decrease = 0   ### count of times that the volume has decreased in time t and t-1
VLKS_trading_t_inc_t1_dec = 0    ### count of times that the volume has increased in time t and decreased in t-1
VLKS_trading_t_dec_t1_inc = 0    ### count of times that the volume has decreased in time t and increased in t-1
for j in range(len(volkswagen["Trading Change"])-1):
    if volkswagen["Trading(t-1)"][j+1]== volkswagen["Trading(t)"][j]: ### for case 1 and 4
        if volkswagen["Trading(t)"][j] == 1:
            VLKS_trading_t_t1_increase += 1
        else: 
            VLKS_trading_t_t1_decrease +=1
    else : 
            if volkswagen["Trading(t)"][j] == 1:
                VLKS_trading_t_inc_t1_dec +=1
            else: 
                VLKS_trading_t_dec_t1_inc  +=1

### Thus, the probability will be as follows: 
### probabilities will be as follows: 
## i) Prob (stock price increases at t | stock price increases at t − 1):
VLKS_prob_2a = VLKS_trading_t_t1_increase/VLKS_count_inc_trading_t1

# ii) Prob (stock price increases at t | stock price decreases at t − 1):
VLKS_prob_2b =  VLKS_trading_t_inc_t1_dec/VLKS_count_dec_trading_t1

# iii) Prob (stock price decreases at t | stock price increases at t − 1):
VLKS_prob_2c = VLKS_trading_t_dec_t1_inc/VLKS_count_inc_trading_t1

# iv) Prob (stock price decreases at t | stock price decreases at t − 1)
VLKS_prob_2d = VLKS_trading_t_t1_decrease/ VLKS_count_dec_trading_t1

print(VLKS_prob_2a,VLKS_prob_2b,VLKS_prob_2c,VLKS_prob_2d)



#------------------------------------------------------------------------------------------------------------------
#### QUESTION 4:
## part 1)
### student ID = 20854690 , thus, miu = 2 and varinace = 9
random.seed(20854690)
normal_Dist = np.random.normal(loc=2, scale=9, size=3020)


## part 2)
returns_amazon = 100*(np.log(amazon["Adj Close"].shift(1))-np.log(amazon["Adj Close"])) ### used above

## part 3)
### regression between 2 and data generated in 1
mask = ~np.isnan(returns_amazon) & ~np.isnan(normal_Dist)  #### masking and removing any NaNs in the data
linear_regress =scipy.stats.linregress(returns_amazon[mask], normal_Dist[mask])

### part 4)

for i in range(1000):
    random.seed(20854690)
    normal_Dist = np.random.normal(loc=2, scale=9, size=3020) 
    mask = ~np.isnan(returns_amazon) & ~np.isnan(normal_Dist)  
    linear_regress_1000 =scipy.stats.linregress(returns_amazon[mask], normal_Dist[mask])


plt.show()