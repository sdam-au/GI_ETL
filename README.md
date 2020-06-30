# PHI dataset extraction and preprocessing
* ETL

---

## Purpose
The purpose of this repository is to extract the PHI dataset from numerous `.csv` files into one tabular object in Python (pandas dataframe), clean it, and upload it to sciencedata.dk for further usage.

---
## Authors
* Vojtěch Kaše [![](https://orcid.org/sites/default/files/images/orcid_16x16.png)]([0000-0002-6601-1605](https://www.google.com/url?q=http://orcid.org/0000-0002-6601-1605&sa=D&ust=1588773325679000)), SDAM project, vojtech.kase@gmail.com
* Petra Heřmánková [![](https://orcid.org/sites/default/files/images/orcid_16x16.png)](https://orcid.org/0000-0002-6349-0540), SDAM project, petra@ancientsocialcomplexity.org

## License
CC-BY-SA 4.0, see attached [License](https://github.com/sdam-au/PHI_ETL/blob/master/LICENSE.md)

## DOI
[Here will be DOI or some other identifier once we have it]

### References
[Here will go related articles or other sources we will publish/create]

---
# How to use this repository

## Sources and prerequisites
[Describe the provenance of data used in the scripts contained and clarify how it is harvested and what other prerequisites are required to get the scripts working. In case of pure tool attribute any reused scripts to source, etc., license and specify any prerequisites or technical requirements.]

### Data
Anything else on data metadata and data used. Link to data repository or explanatory article. 


## Data storage: 

`SDAM_root/SDAM_data/PHI` folder on sciencedata.dk

* [1_0_py_PHI_EXTRACTION_FROM_ZIP_RAW.ipynb](https://github.com/sdam-au/PHI_ETL/blob/master/scripts/1_0_py_PHI_EXTRACTION_FROM_ZIP_RAW.ipynb))
  * input: `PHI-raw-csv-2020-06-19.zip`
  * output: `PHI_merged_[timestamp].json`
  
* [1_1_r_PHI_SCRAPING_MISSING_DATA.Rmd](https://github.com/sdam-au/PHI_ETL/blob/master/scripts/1_1_r_PHI_SCRAPING_MISSING_DATA.Rmd)
  * input: `PHI_merged_[timestamp].json`
  * output: `PHI_enriched_[timestamp].json`

* [1_2_r_PHI_CLEANING_TEXT.Rmd](https://github.com/sdam-au/PHI_ETL/blob/master/scripts/1_2_r_PHI_CLEANING_TEXT.Rmd).
  * input1: `PHI_enriched_[timestamp].json`
  * output: `PHI_cleaned_[timestamp].json` (latest verified version: 2020-06-29)
   
* [1_3_EXTRACTING_DATES.ipynb](https://github.com/sdam-au/PHI_ETL/blob/master/scripts/1_3_EXTRACTING_DATES.ipynb)
  * input:  `PHI_cleaned_[timestamp].json`
  * output1: `PHI_cleaned_dated_[timestamp.json`
  * output2: overview data samples in gsheet `PHI_overview`

* [1_4_MODELLING_DATES.ipynb](https://github.com/sdam-au/PHI_ETL/blob/master/scripts/1_4_MODELLING_DATES.ipynb)
  * input: `PHI_cleaned_dated_[timestamp.json`
  * output: `PHI_sim_time_blocks_[timestamp].json 


### Software
1. Google Colab or Jupyter Notebooks
1. R, version 4.0.1

### Registered account
1. Google Colab

### Hardware
1. Multiple-screen
1. Mouse
1. A lot of Coffee

---
## Installation
[Describe the steps necessary to install the tool/package; example: https://gist.github.com/PurpleBooth/109311bb0361f32d87a2]

---
## Instructions 
[Describe first steps, how to use the current repository by a typical user - the digital historian with limited technical skills]
1. First, do ...
1. Second, do ...
1. Third, go to ...


## Screenshots
![Example screenshot](./img/screenshot.png)




