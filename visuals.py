###########################################
# Suppress matplotlib user warnings
# Necessary for newer version of matplotlib
import warnings
warnings.filterwarnings("ignore", category = UserWarning, module = "matplotlib")
#
# Display inline matplotlib plots with IPython
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
from collections import deque
###########################################

import matplotlib.pyplot as pl
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
from time import time
from sklearn.model_selection import train_test_split, learning_curve, ShuffleSplit, validation_curve


def distribution(data, features_to_watch, transformed = False):
    """
    Title: Visualization code for displaying skewed distributions of features
    Author: Udacity.
    Date: Nov 17, 2017.
    Code version: master (using branch since they don't have tag version in their github repo)
    Availability: https://github.com/udacity/machine-learning/blob/master/projects/finding_donors/visuals.py
    """

    plot_title = ("Skewed Distributions of Continuous bonds Data Features", "Log-transformed Distributions of Continuous Census Data Features")[transformed]
    plot_xlabel = "Value"
    plot_ylabel = "Number of records"

    #Creating queue of features
    f_queue = deque(features_to_watch)

    hist = hist_plots_grid(data, f_queue, plot_title, plot_xlabel, plot_ylabel, 1, 3)

    return hist


def hist_plots_grid(data, features_to_watch, title, xlabel, ylabel, max_num_rows = 2, max_num_cols = 2, fig_size=(11,7)):
    # Create figure
    grid = {"wspace":0.50, "hspace":0.8}
    fig, axs = pl.subplots(max_num_rows, max_num_cols, figsize=fig_size, gridspec_kw=grid)

    # Skewed feature plotting
    for i in range(0,max_num_rows):
        for j in range(0, max_num_cols):
            if features_to_watch:
                feature = features_to_watch.popleft()
                axs[j].hist(data[feature], bins = 25, color = '#00A0A0')
                axs[j].set_title("'%s'"%(feature), fontsize = 10)
                axs[j].set_xlabel(xlabel)
                axs[j].set_ylabel(ylabel)
                axs[j].set_ylim((0, 2000))
                axs[j].set_yticks([0, 500, 1000, 1500, 2000])
                axs[j].set_yticklabels([0, 500, 1000, 1500, ">2000"])

    # Plot aesthetics
    fig.suptitle(title, fontsize = 16, y = 1.03)

    return fig