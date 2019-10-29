#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:28:50 2019

@author: oscarbarbier

"""

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

from keras import backend as K
K.tensorflow_backend._get_available_gpus()
    
import tensorflow as tf
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))


"""
edcba

cbaed
caedb

dbcae
dcaeb

ebdca
edcab

dcabe
dabec

ecdab
edabc
abcde
"""