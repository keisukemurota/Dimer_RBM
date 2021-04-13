import numpy as np

import argparse
import os
import sys
import json 
import logging

from scripts import Dimer_RBM

from conf import * # import parameters from config file.

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--h", help = "h",type=float)
    parser.add_argument("--q", help = "q",type=float)
    args = parser.parse_args()

    # n_iter = int(3e3)
    # length = [4,4]
    # alpha = 2

    h = 1 if (not args.h) and (args.h != 0) else round(args.h,2)
    q = 1 if (not args.q) and (args.q != 0) else round(args.q,2)



    V = h * q
    # h = 0
    # V = 1

    Dimer_RBM(h = h, V = V, length = length, alpha = alpha, n_iter = n_iter, 
        n_samples = n_samples_RBM, n_chains = n_chains, n_discard = n_discard, sweep_size = sweep_size)

