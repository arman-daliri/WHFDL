# World Hyper Fuzzy Deep Learning
## WHFDL: an explainable method based on World Hyper-heuristic and Fuzzy Deep Learning approaches for gastric cancer detection using metabolomics data

## How to
### First run this command to install FWHFDL and CWHFDL packages
-
### https://pypi.org/project/CWHFDL/
-
### https://pypi.org/project/FWHFDL/
-
```shell
$ pip install FWHFDL CWHFDL
```
then run `Example/FWHFDL-example.py` to get selected features data and save it to a csv file like `Data/CGMAIN1.csv`.
and then change the 
```python
df = pd.read_csv('../Data/CGMAIN1.csv')
```
to your own csv in the
```
Experimental/Gastric Cancer Prediction Experimental evaluation.ipynb
```
file and run.
