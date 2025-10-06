# World Hyper Fuzzy Deep Learning
## WHFDL

## Article title:
WHFDL: an explainable method based on World Hyper-heuristic and Fuzzy Deep Learning approaches for gastric cancer detection using metabolomics data
-
## Note:
Note that the values ​​of the interpretability criteria change each time you run and output.
By nature, the values ​​should change, and the model should remain stable and interpretable. So don't be surprised if the graphs change.
-
# Accepted on: 
## BioData Mining
### https://biodatamining.biomedcentral.com

## How to
### First run this command to install FWHFDL and CWHFDL packages
### https://pypi.org/project/CWHFDL/
### https://pypi.org/project/FWHFDL/
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

## Authors
- Mohammad Mahdi Mir [Contact](mailto:standardret@proton.me)
- Arman Daliri [Contact](mailto:daliriwork2@gmail.com)
- Nora Mahdavi [Contact](mailto:noramahdvi@gmail.com)
