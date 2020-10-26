This projects aims at improving the simple track identification algorithms defined in the Bergen pCT project:
* [Proton tracking in a high-granularity Digital Tracking Calorimeter for proton CT purposes](https://www.sciencedirect.com/science/article/pii/S0168900217301882)
* [Design optimization of a pixel-based range telescope for proton computed tomography](https://www.sciencedirect.com/science/article/abs/pii/S1120179719301358)
* [A High-Granularity Digital Tracking Calorimeter Optimized for Proton CT](https://www.frontiersin.org/articles/10.3389/fphy.2020.568243/abstract)
* Helium Radiography with a Digital Tracking Calorimeter—a Monte Carlo Study for Secondary Track Rejection (submitted)

The layout of the input files (made using the code at github.com/HelgeEgil/focal) is the following:

0 -> 44 | 45 | 46 | 47 | 48 | 49
--------|----|----|----|----|---
de/dz track (idx = layer number) | Track contains electron | Track contains proton | Track contains helium | Track contains heavier ions | Track has Bragg peak

Training data with more statistics (6M tracks; 10k is included here) [is available for download](https://bit.ly/3jknxbD); put the two files in the Data/ subfolder.

Examples of helium tracks, sorted by truth vector contents:
![Helium example tracks](/Figures/heliumExamples.jpg)

Example of 400 input vectors for training (excluding MC truth)
![Helium example input vector](/Figures/input.jpg)
