## Usage 

Paste and run this in your colab notebook in the last cell.
```
!wget https://raw.githubusercontent.com/brpy/colab-pdf/master/colab_pdf.py
from colab_pdf import colab_pdf
colab_pdf('pandas-assignment.ipynb')
```
Enter the the full file name as shown above, within quotes. A file download dialog will show up in your browser, 

Press ***download***.

___
#### Save to Drive
If you also want to save the pdf in Google Drive, you can set flag ```saveto_Drive = True``` as shown below:

```colab_pdf('pandas-assignment.ipynb',True)```  will download pdf to My Drive folder on your Google Drive.

#### Defaults
```python
def colab_pdf(file_name, saveto_Drive = False ,notebookpath = '/content/drive/My Drive/Colab Notebooks/'):
```
Do **not** change the defaults unless required to. A simple ```colab_pdf('notebook_name.ipynb')``` will work in most cases.

#### Google Drive Access
This requires that you have already mounted your google drive in your notebook. If not, this will attempt to Mount your drive, which may ask for your auhtentication.

#### Printing from browser works for me, why use this?
If you are satisfied from browser's pdf, this might not be for you. This uses jupyter's `nbconvert` which is the recommended way to convert `.ipynb` to `.pdf` and may produce better results.

#### Error in nbcovert or xelatex
nbconvert and xelatex are not perfect and might fail to convert your file to pdf. In such case try to debug using output logs or use browser's  File -> Print  method.
___
Thanks to Google Colab for helping the community.
Google Colaboratory is a product of Google.
