# -*- coding: utf-8 -*-
"""
Created on Wed Apr 01 14:18:59 2015

@author: jperkowski
"""

import logging
import itertools

def choose_holdout_and_order(cards):
    """
    Input: list of 5 numbers in range [1, 52]
    Output: (holdout_number, [list of numbers in order specified])
    """   
    pass


def predict_holdout(cards):
    """
    Input: list of 4 numbers in order that will predict a holdout number
    Output: holdout number
    """
    pass


def test_algorithm():
    for cards in itertools.combinations(range(52), 5):
        holdout, choice = choose_holdout_and_order(cards)
        predicted = predict_holdout(choice)
        if holdout != predicted:
            logging.error('failure with combination: ' + str(cards))            
            raise RuntimeError('expected {0} got {1}'.format(holdout, predicted))


test_algorithm()
print('all passed!')             
            
            

        