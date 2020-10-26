This projects aims at improving the simple track identification algorithms defined in the Bergen pCT project:
* https://www.sciencedirect.com/science/article/pii/S0168900217301882
* https://www.sciencedirect.com/science/article/abs/pii/S1120179719301358
* https://www.frontiersin.org/articles/10.3389/fphy.2020.568243/abstract

Training data with more statistics (made using the code at github.com/HelgeEgil/focal) is available for download at https://bit.ly/3jknxbD; put the two files in the Data subfolder. The layout of the files is the following

0 -> 44 | 45 | 46 | 47 | 48 | 49
--------|----|----|----|----|---
de/dz track (idx = layer number) | Track contains electron | Track contains proton | Track contains helium | Track contains heavier ions | Track has Bragg peak


Examples of helium tracks, sorted by truth vector contents:
![Helium example tracks](/Figures/heliumExamples.jpg)

Example of 400 input vectors for training (excluding MC truth)
![Helium example input vector](/Figures/input.jpg)
