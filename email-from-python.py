#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 21:31:11 2021

@author: jm
"""

# %% required libraries
import os


# %% get email and password from environment variables
EMAIL_SENDER= os.environ.get('EMAIL_SENDER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_RECIPIENT = os.environ.get('EMAIL_RECIPIENT')

print(EMAIL_SENDER)
