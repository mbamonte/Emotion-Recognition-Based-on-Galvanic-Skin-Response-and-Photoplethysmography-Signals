#%%--------------------------------------------------------------------
import numpy as np

data = [
    [0.24828373, 0.62497919, 0.62569231, 0.61722688, 0.62000162, 0.29776146, 0.64458333, 0.67338462, 0.62189527, 0.64383607],
    [0.48148992, 0.73272727, 0.75738462, 0.71797039, 0.73773882, 0.32082258, 0.6599359, 0.662, 0.62737021, 0.64566307],
    [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    [0.16379734, 0.57822511, 0.614, 0.53119747, 0.5698649, 0.05110741, 0.52564103, 0.52538462, 0.51721683, 0.52119558],
    [0.42066902, 0.69787582, 0.76523077, 0.64824957, 0.69948185, 0.40726498, 0.70331169, 0.71753846, 0.68672159, 0.69913823],
    [0.30555716, 0.63809524, 0.72907692, 0.57463455, 0.64492433, 0.13911228, 0.56269841, 0.67723077, 0.44349209, 0.55647774],
    [0.2657655, 0.63301282, 0.63384615, 0.61774279, 0.6258259, 0.11064261, 0.55547369, 0.55815385, 0.54213809, 0.5494202],
    [-0.06983436, 0.46840278, 0.49830769, 0.42254676, 0.45794565, 0.37071974, 0.67991342, 0.70953846, 0.64791171, 0.67684749],
    [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    [0.15884152, 0.56909722, 0.66969231, 0.47224932, 0.56343944, 0.06999128, 0.53333333, 0.57784615, 0.46556212, 0.52486324],
    [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    [0.05288678, 0.51856061, 0.82076923, 0.14755949, 0.50419182, 0.25933284, 0.63006494, 0.64492308, 0.6165585, 0.62654963],
    [0.32887331, 0.65508578, 0.70923077, 0.62001492, 0.65868268, 0.20245609, 0.5965482, 0.64876923, 0.56289997, 0.59796229],
    [-0.04243694, 0.48342105, 0.70507692, 0.1545791, 0.45390158, -0.04117461, 0.47948718, 0.48184615, 0.46095372, 0.4714543],
    [0.20215099, 0.60096154, 0.60107692, 0.59846854, 0.59965478, 0.25562924, 0.62301879, 0.67769231, 0.57632794, 0.61903344],
    [-0.06714885, 0.46774892, 0.48184615, 0.44293579, 0.46111237, 0.19284954, 0.58258145, 0.72876923, 0.46923062, 0.57982783],
    [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    [0.09448461, 0.54725691, 0.55430769, 0.53291468, 0.54257722, 0.12478057, 0.56340743, 0.56553846, 0.55167143, 0.55745413],
    [0.37829164, 0.6751634, 0.75692308, 0.61562451, 0.67815938, 0.44740745, 0.72307692, 0.72507692, 0.71243673, 0.71954724],
    [0.40776723, 0.69673611, 0.73323077, 0.67973455, 0.70110991, 0.16434268, 0.57708333, 0.62476923, 0.52919653, 0.57359212],
    [0.10633364, 0.55159722, 0.59323077, 0.51007373, 0.54632515, 0.19723723, 0.59632035, 0.61030769, 0.57082462, 0.59034763],
    [0.32160581, 0.65923611, 0.67769231, 0.64919862, 0.65855826, 0.22428795, 0.61076389, 0.65738462, 0.58236337, 0.60849233]
]

numpy_array = np.array(data)
print(numpy_array)


    #%% ----------------------------------------
    # Print results from simulations files (.csv)

    # from functions import print_results_from_file 

    # print_results_from_file(print_results=True, show_plot=False)


#%%----------------------------------------------------------------
# Calculate the standard deviation of each column
np.set_printoptions(linewidth=np.inf)
mean = np.round(np.nanmean(numpy_array, axis=0), decimals=3)
print("Mean of each column:")
print("  v_c   v_u   v_a   v_g   v_f1  a_c   a_u   a_a   a_g   a_f1")
print(mean)


std_dev = np.round(np.nanstd(numpy_array, axis=0), decimals=3)
print("  v_c   v_u   v_a   v_g   v_f1  a_c   a_u   a_a   a_g   a_f1")
print("Standard Deviation of each column:")
print(std_dev)


# Print the result after handling division by zero
with np.errstate(divide='ignore', invalid='ignore'):
    result = np.round(np.where(mean == 0, 0, std_dev * 100 / mean), decimals=2)
    print("std_dev*100/mean:")
    print("  v_c   v_u   v_a   v_g   v_f1  a_c   a_u   a_a   a_g   a_f1")
    print(result)
