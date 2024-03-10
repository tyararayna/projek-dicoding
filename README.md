# E-Commerce Public Dataset

**Final Project Data Analysis**

for fast access, click : https://projek-dicoding-7f7ip7kd5zecqztp35f7wk.streamlit.app/
## Setup Environment

```
conda create --name myenv python=3.9.18
conda activate myenv
pip install numpy pandas matplotlib seaborn streamlit
```

## Run Streamlit App

```
streamlit run dashboard/dashboard.py
```

## Dataset Overview

### Introduction

This is a Brazilian ecommerce public dataset of orders made at Olist Store. The dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and finally reviews written by customers. We also released a geolocation dataset that relates Brazilian zip codes to lat/lng coordinates.

This is real commercial data, it has been anonymised, and references to the companies and partners in the review text have been replaced with the names of Game of Thrones great houses.

## Data Structure

The Brazilian E-Commerce dataset from Kaggle consists of several CSV files that cover various aspects of the e-commerce system in Brazil. 
This dataset provides broad insights into e-commerce transactions, customers, products, and sellers in Brazil. By combining data from various tables, comprehensive analysis can be conducted to understand trends and patterns in e-commerce activities.

## Merging Dataframes

In this project, there are two main dataframes that will be used, namely `df_order_items` and `orders`.

- `df_order_items`: A combination of the order_items, products_translation, and seller tables, providing details about item-orders, product translations, and seller information.

- `orders`: A combination of the orders, payments, and customer tables, offering a holistic overview of orders, payments, and customer data.

The integration of these two dataframes will enable a more comprehensive analysis of the entire project's processes and transactions.
