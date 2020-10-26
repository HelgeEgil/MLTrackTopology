import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.collections import LineCollection
import seaborn as sns

data = pd.read_csv("Data/input_helium_resampled.csv", sep=";", nrows=400000, skiprows=range(1, 0 * 400000))

data = data.sample(frac=1)

with_bp = data[data["has bragg peak"] == 1].reset_index()
without_bp = data[data["has bragg peak"] == 0].reset_index()

good_filter = (data["has bragg peak"] == 1) & (data["has electron"] == 0) & (data["has helium"] == 1) & (data["has heavier ion"] == 0) & (data["has proton"] == 0)
good_tracks = data[good_filter].reset_index()

with_electron = data[data["has electron"] == 1].reset_index()
with_proton = data[data["has proton"] == 1].reset_index()
with_helium = data[data["has helium"] == 1].reset_index()
with_heavy = data[data["has heavier ion"] == 1].reset_index()

fig, axs = plt.subplots(2, 3, figsize=(12, 6))
plt.subplots_adjust(hspace=0.4, wspace=0.25, left=0.08, right=0.92)

axs = axs.flatten()

n_tracks = 6
width = 1.2
alpha = 0.6

#colors = ['blue', 'green', 'black', 'red', 'yellow', 'darkgreen', 'darkblue', 'salmon']
#colors = ["midnightblue", "mediumblue", "blue", "slateblue", "royalblue", "cornflowerblue"]
colors = ["aqua", "deepskyblue", "dodgerblue", "blue", "darkblue", "midnightblue"]

datasets = {"All tracks": data, "Good tracks": good_tracks, "Without Bragg peak": without_bp,
            "With electrons": with_electron, "With proton": with_proton, "With heavier ions": with_heavy}

for k, v in datasets.items():
    print(f"len {k} = {len(v)}")

idx = 0
for name, dataset in datasets.items():
    maxY = 0
    for k in range(n_tracks):
        X = range(45)
        Y = np.zeros(45)

        final_index = 44
        for layer in X:
            Y[layer] = float(dataset.at[k, f"Layer {layer}"])
            if Y[layer] == 0:
                final_index = layer
                break

        maxY = max(maxY, max(Y))

        X = np.array(X)[:final_index]
        Y = Y[:final_index]

        widths = (2 * X / final_index) ** 3 + 0.8
        new_x = np.linspace(X[0], X[-1], 100 * len(X))  # new_x has 100x more points than X
        new_y = np.interp(new_x, X, Y)
        new_w = np.interp(new_x, X, widths)

        points = np.array([new_x, new_y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        lc = LineCollection(segments, linewidths=new_w, alpha=alpha, color=colors[k])
        axs[idx].add_collection(lc)

    axs[idx].set_xlim((0, 45))
    axs[idx].set_ylim((0, max(12, maxY * 1.2)))
    axs[idx].set_xlabel("Layer number")
    axs[idx].set_ylabel("Energy deposition [keV/µm]")
    axs[idx].set_title(name, y=1, pad=-15)
    idx += 1

fig, axs = plt.subplots(3, 1, sharex=True, sharey=True)
plt.subplots_adjust(wspace=0, hspace=0, left=0.03, right=1, bottom=0.14, top=0.94)
small_dict = {"All tracks": data, "Good tracks": good_tracks, "Without Bragg peak": without_bp}

ntracks = 400

idx = 0
for name, dataset in small_dict.items():
    array = np.zeros((45, ntracks))
    for k in range(ntracks):
        for l in range(45):
            array[l, k] = dataset.at[k, f"Layer {l}"] ** 0.6

    axs[idx].imshow(array, cmap="bone_r", origin="lower", interpolation="nearest", vmin=0, vmax=22)
    if idx == 2:
        axs[idx].set_xlabel("Track vector number")
    if idx == 1:
        axs[idx].set_ylabel("Track length (number of layers)")
    if idx in [0, 2]:
        axs[idx].tick_params(axis="y", which="both", labelbottom=False)
    axs[idx].set_title(f"{name}", y=1, pad=-15)
    axs[idx].set_ylim((0, 55))
    idx += 1

#plt.tick_params(axis="x", which="both", labelbottom=False)

plt.show()
