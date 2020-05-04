def colab_pdf(file_name, saveto_Drive = False ,notebookpath = '/content/drive/My Drive/Colab Notebooks/'):
  import os
  import time
  if(not isinstance(file_name,str)):
    raise TypeError(f"expected a string as file_name, but got {type(file_name)} instead.")
  
  drive_mount_point = '/content/drive/'
  gdrive_home = os.path.join(drive_mount_point, 'My Drive/')
  
  if(not os.path.isdir(gdrive_home)):
    from google.colab import drive
    drive.mount(drive_mount_point)

  if(not os.path.isfile(os.path.join(notebookpath,file_name))):
    raise ValueError(f"file '{file_name}' not found in path '{notebookpath}'.")

  get_ipython().system("apt update && apt install texlive-xetex texlive-fonts-recommended texlive-generic-recommended")
  get_ipython().system("jupyter nbconvert --output-dir='$gdrive_home' '$notebookpath''$file_name' --to pdf")

  time.sleep(3) #Some pdf files take time to appear in the drive
  
  from google.colab import files
  file_name = file_name.split('.')[0] + '.pdf'
  files.download(gdrive_home+file_name)
  
  if(not saveto_Drive):
    os.remove(gdrive_home+file_name)
