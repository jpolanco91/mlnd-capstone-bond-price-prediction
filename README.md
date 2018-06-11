# Machine Learning Engineer Capstone project - U.S. corporate bond price prediction.

##### Project Description.

This project is based on the “Benchmark Bond Trade Price Challenge” Kaggle competition (Benchmark Solutions, 2012). The main goal is to predict the next price a US corporate bond might trade at based on its last 10 transactions. 

##### Datasets.

Original datasets were cleaned for this project, since most of them had datapoints with missing features values or invalid values. These are the datasets used in this project:

- Training set: train_clean.csv (a cleaned version from the original training set in Benchmark solutions competition).
- Test set: test_clean.csv (a cleaned version from the original test set in the Benchmark solutions kaggle competition).

##### Install

This project requires **Python 3.0** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

##### Running the project.

```sh
$ jupyter notebook finding_donors.ipynb
```
##### Data and features.

These are the dataset's features. This data comes from a time-series dataset. However, for the particular problem I'm solving, I won't use any time-series related feature/data, because it doesn't depend on it.

- `bond_id:` The unique id of a bond. This is used to aid in the reconstruction of a time-series.
- `weight:` The weight of the row for evaluation purposes. This is calculated as the square
root of the time since the last trade and then scaled so the mean is 1.
- `current _coupon:` the coupon of the bond at the time of the trade.
- `time_to_maturity:` The number of years until the bond matures at the time of the trade.
- `is_callable:` A binary value indicating whether or not the bond is callable by the issuer.
- `reporting_delay:` The number of seconds after the trade occurred that it was reported.
- `trade_size:` the notional amount of the trade.
- `trade_type:` 2=customer sell, 3=customer buy, 4=trade between dealers. We would expect
customers to get worse prices on average than dealers.
- `curve_based_price:` A fair price estimate based on implied hazard and funding curves of
the issuer of the bond.
- `received_time_diff_last{1-10}:` The time difference between the trade and that of the
previous {1-10}.
- `trade_price_last{1-10}:` The trade price of the last {1-10} trades.
- `trade_size_last{1-10}:` The notional amount of the last {1-10} trades.
- `trade_type_last{1-10}:` The trade type of the last {1-10} trades.
- `curve_based_price_last{1-10}:` The curve based price of the last {1-10} trades.

##### Target variable.
- `trade_price:` This is the price of what the trade occurred.

##### Important notes.

- visuals.py: This library is based on the visuals.py used in previous ML projects in the Nanodegree. Also most of the visuals code is on the notebook, which is also based on the previous visuals code used in the Nanodegree. Since this visualization code belongs to Udacity, it is cited using the following code citing notation:

```
Title: Title that briefly describes what the code does.
Author: The original author of the code.
Date: The date it was last modified. Also available on the code’s repo.
Code version: Code version if available. Otherwise, will use the name of the branch where I found it.
Availability: Url where the code is located.
```
