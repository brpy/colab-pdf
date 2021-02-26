## Usage 


Paste and run this in your colab notebook in the last cell.
```ipython
!wget -nc https://raw.githubusercontent.com/brpy/colab-pdf/master/colab_pdf.py
from colab_pdf import colab_pdf
colab_pdf('pandas-assignment.ipynb')
```
Enter the the full file name as shown above, within quotes. The pdf will be saved on your Google Drive.

For better quality plots use:
```python
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf', 'svg')
```
in the first cell of the notebook.
___


#### I want to hide output
The outputs can be long as a lot of commands are run in the background. You can use `%%capture` magic to hide the cell output.
```
%%capture
!wget -nc https://raw.githubusercontent.com/brpy/colab-pdf/master/colab_pdf.py
from colab_pdf import colab_pdf
colab_pdf('pandas-assignment.ipynb')
```
 *Note:* This will also hide pdf creation, pdf save logs. So check your Google Drive for the pdf.

#### Google Drive Access
This requires that you have already mounted your google drive in your notebook. If not, this will attempt to Mount your drive, which may ask for your auhtentication.


#### Printing from browser works for me, why use this?
If you are satisfied with browser's pdf, this might not be for you. This uses jupyter's `nbconvert` which is the recommended way to convert `.ipynb` to `.pdf` and may produce better results.


#### Too slow
Ubuntu repos are updated and xelatex packages are downloaded in the background. This takes upto 90% of the time as these packages are large and can consume time.


#### Browser download works ony half the time
Due to some reason or the way google.colab.files is implemented, browser download fails for the first time. This has been mitigated by putting it in a try block. If you run it second time the file can be downloaded from the browser itself.


#### Error in nbcovert or xelatex
nbconvert and xelatex are not perfect and might fail to convert your file to pdf. In such case try to debug using output logs or use browser's  File -> Print  method.
___


Thanks to Google Colab for helping the community.
Google Colaboratory is a product of Google.
