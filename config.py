import os
"""
Instructions for use:
1) Set everything under main - recommend making a directory and putting the timeseries file in it, then setting
the directory and target file appropriately.
2) If the data file is processed already, just set the data types to match (dtype and target_dtype), and set strip_gaps
to False.
3) Set other options - some are self-explanatory and others are less. All are poorly documented at the moment.
4) Run main.py
"""
# ========== Main/Most relevant ==========
dataset_to_use = "corot"


version = "1.1"

working_dir = "C:/Users/Erik/main/projects/plaskett_photometry/hd47129_analysis_for_thesis/pdc"
target_file = "HD47129_thresh9_lc.txt"
cols = [0, 1, 2]
dtype = "flux"
delimiter = ' '
time_offset = -7000

n_f = 50  # number of frequencies to extract

peak_selection = "slf" # can be highest, bin, slf
bin_highest_override = 12 # sets the number of frequencies
averaging_bin_radius = 0.25
cutoff_iteration = 50
cutoff_sig = 3

multi_fit_type = "lm"  # "anneal", "lm", "scipy". Sets fitting engine to use.
residual_model_generation = "sf" # can be sf, mf. Controls which model is used to generate residual periodogram
boundary_warnings = 0.05
clean_existing = True

sig_method = "poly" # "poly" or "box_avg"
poly_order = 3

# ========== Preprocessing ==========
target_dtype = "mmag"  # allowed values: mag, mmag, flux (only if data originally in flux)
strip_gaps = True
gap_size = 0.5  # days
strip_gaps_points = 50  # on either side of each gap, and at the start and end
# ========== Logging ==========
log_fname = "log.txt"
save_freq_logs = True
freqlog_folder = "freq_logs"

# ========== Console ==========
quiet = False

# ========== Output targets ==========
preprocessed_lightcurve_fname = "inp_lc.dat"
frequencies_fname = "frequencies.csv"
save_supp_data = True
# ========== Frequency Selection ==========
# TODO: implement LOPOLY fit for freq selection+rejection by significance
freq_selection_method = "highest" # can be highest, or averaged

# ========== Fitting ==========
phase_fit_rejection_criterion = 0.1
# ========== LM ==========
# freq bounds use coefficients
freq_bounds_lower_coef = 0.8
freq_bounds_upper_coef = 1.2
# amp bounds use coefficients
amp_bounds_lower_coef = 0.8
amp_bounds_upper_coef = 1.2
# phase bounds set explicitly
phase_bounds_lower = -100
phase_bounds_upper = 100

# ========== Periodograms ==========
periodograms_lowerbound = "resolution"  # can be set to resolution or explicit value in c/d
periodograms_upperbound = 10

# ========== Plots ==========

figure_subdir = "/figures"
reg_plots = True
iterative_subdir = "/figures_iterative"
plot_iterative = True
runtime_plots = False  # shows stuff as the program is running for debugging purposes

# ========== Periodograms ====
pg_x_axis_label = "Frequency [c/d]"
pg_y_axis_label = f"Amplitude [{target_dtype}]"
pg_xlim = [0, 5]

# ========== Dual Annealing ==========
frequencies_da_filename = "frequencies_da.csv"
