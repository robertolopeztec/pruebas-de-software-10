#!/usr/bin/python3
"""
This script takes two files as parameters.
* The first one contains information in a JSON format about
  a catalogue of prices of products.
* The second one contains a record for all sales in a company.

The output is the computation of total cost for all sales.
"""

import json
import sys
import time


def read_json_file(file: str) -> dict:
    """
    Takes a file path that contains a .JSON file, reads it
    and returns a dict object.
    """
    with open(file, 'r', encoding='utf8') as f:
        json_object = json.load(f)
        f.close()

    return json_object


def compute_sales_product_count(sales_file: str) -> dict:
    """
    Given the file that contains sales of products, get
    the count of the sold items per item.
    """

    sales_file = read_json_file(sales_file)

    # Generate a dictionary that gets the product and the quantity
    # and sums the quantity
    sales_product_count = {}

    for sale in sales_file:
        product = sale['Product']
        quantity = sale['Quantity']

        if product in sales_product_count:
            sales_product_count[product] += quantity
        else:
            sales_product_count[product] = quantity

    return sales_product_count


def get_price_product_catalogue(price_catalogue_file: str) -> dict:
    """
    Given the file containing the catalogue, return a dictionary
    with the product as key, and price as value.
    """
    price_catalogue = read_json_file(price_catalogue_file)

    price_product_catalogue = {}
    for price_product in price_catalogue:
        product = price_product['title']
        price = price_product['price']
        price_product_catalogue[product] = price

    return price_product_catalogue


def compute_total_cost(sales_file: str, price_catalogue_file: str) -> None:
    """
    Given the sales file and a price catalogue per item, then compute the
    total cost.
    """
    total_cost = 0

    # Import the product count of all products
    sales_product_count = compute_sales_product_count(sales_file)

    price_product_catalogue = get_price_product_catalogue(price_catalogue_file)

    # Now, for each product count get its price and add it to the total
    for product, quantity in sales_product_count.items():
        try:
            product_price = price_product_catalogue[product]
            total_cost += quantity * product_price
        except TypeError as e:
            print(e)

    return total_cost


def write_result(result: str) -> None:
    """
    Given a string with the results of the program, then write it.
    """
    with open('./SalesResults.txt', 'w', encoding='utf8') as f:
        f.write(result)
        f.close()


if __name__ == '__main__':

    # Set the start time to compute the elapsing runtime
    start_time = time.perf_counter()

    # Define and save the variables for the input files
    price_catalogue_file_ = sys.argv[1]
    sales_file_ = sys.argv[2]

    total_cost_ = compute_total_cost(sales_file_, price_catalogue_file_)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    result_ = f'TOTAL COST: ${total_cost_:,.2f} | '
    result_ += f'ELAPSED TIME: {elapsed_time:.4f} SECONDS'

    print(result_)
    write_result(result_)
