#!/usr/bin/python3
import sys
sys.path.append('/MyRecap/p_pract/anbpro/models/')
import base_model as math

my_model = math.Basemodel()
print(type(my_model))
print(my_model.__dict__)