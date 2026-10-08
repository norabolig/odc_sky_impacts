# Orbital Data Centre Sky Impacts

Scripts for making figures of sky impacts of satellite systems.

This particular shows scripts used for making figures in Boley, Lawler, and Rein 2026 (DOI to be added).
Arxiv version of paper: https://arxiv.org/abs/2608.02757

By Aaron Boley

License: MIT (see LICENSE file)

Repo: https://github.com/norabolig/odc_sky_impacts

## Scripts

ODC_timeofday.py: creates the time of day plots for different times of year, showing the number of potentially visible satellites in the sky for a given time of day. A cut is used to show only numbers for when the obesrver is between civil twilight.

sats-in-sky.py: creates a series of plots for a given time of day and year. It includes a local sky plot, Mollweide projection, alt-az plot, and a globe projection to give a 3D view of the satellite design. 

Sunrise, SpaceX ODC, and Stampede are all available.

## Figures

In the figs directory, figures used in the Boley, Lalwer, and Rein paper can be found, as well as additional plots produced by thesats-in-sky.py script.


