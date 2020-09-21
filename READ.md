# Deribit Data Pulling

## Deribit Rate Limits


Clients can check their actual limits on https://www.deribit.com/main#/account?scrollTo=api page, or can query the system using the /private/get_account_summary method.

Deribit has two different Rate Limits, one for Matching Engine Requests and another for all other requests (Non Matching Engine).

### 1 Matching engine requests

Each sub-account has a rate limit that is updated in line with the table below every hour and this approach is the same for WS, REST and FIX. 

The rate limit is measured as an aggregate of all books and currencies.

When the counter is exhausted the user will get the following error message "too_many_requests" 10028. When you get a 10028 error and you want to cancel your orders, the best approach would be to wait the request refill time (see table) and send a mass cancel.

|Tier   |Volume  |Rate                    |Limits   |Burst |Explanation                                 |
|-------|--------|------------------------|---------|------|--------------------------------------------|
|Tier 1   |7 Day |7 Day volume > USD 25m  |30 p/s   |150   |150 in a burst or for example 30 per second |
|Tier 2   |7 Day |7 Day volume > USD 5m   |20 p/s   |100   |100 in a burst or for example 20 per second |
|Tier 3   |7 Day |7 Day volume > USD 1m   |10 p/s   |40    |40 in a burst or for example 10 per second  |
|Tier 4   |7 Day |7 Day volume > USD 0    |5 p/s    |20    |20 in a burst or for example 5 per second   |


### 2. Non-matching engine requests


**Each sub-account has a rate limit of 30 requests per second with a burst of 200. This setup is the same for WS, REST and FIX.**

These limits include session-level messages like a heartbeat, test request etc.




## Overview of Matching Engine requests

All requests not in the list below are treated as Non-Matching Engine Requests


* API V2 

/api/v2/private/buy

/api/v2/private/sell

/api/v2/private/edit

/api/v2/private/cancel

/api/v2/private/cancel_all

/api/v2/private/cancel_all_by_instrument

/api/v2/private/cancel_all_by_currency

/api/v2/private/close_position

/api/v2/private/verify_block_trade

/api/v2/private/execute_block_trade

 /api/v2/private/cancel_by_label 


* API V1

/api/v1/private/buy

/api/v1/private/sell

/api/v1/private/edit

/api/v1/private/cancel

/api/v1/private/cancelall


* FIX

new_order_single

order_cancel_request

order_mass_cancel_request

order_cancel_replace_request

