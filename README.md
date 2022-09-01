# AV-comfort-assessment-tool-

# Those scripts were developed as a part of the comfort assessment project.

AV_assessTool.py- assess the comfort. Program uses the AV datasets from the NuScenes.

Plotting scripts:
Barry_mapping.py – Comfort assessment on map & Comfort Score versus Time
Plot.py – Plots lateral/longitudinal acceleration versus time, acceleration classification for the berryIMU data and AV, plots comfort score versus time for AV data
AV_otherplots.py- other plots such as velocity, steering, and yaw rate with the respect of time
Berry_otherplots.py- plots speed/altitude versus time
AV_mapping.py- can plot drive route on map by use of free map providers
AV_Map_assess.py- plots the comfort assessment with respect to the NuScenes position data.

Other:
Filter.py- presents attempt to the data filtering
AV_GPSimport.py-  converts the NuScenes position data to lateral/longitudinal format. Obtains data from JSON file and outputs in text file.

Real-time assessment by use of DAU:

Some instructions:
BerryIMU script assess the comfort and collects all necessary data in TXT format.
Then data can be visualised by use of plotting scripts. 
AV data should be imported, then assessed and then plotted by use of scripts.
