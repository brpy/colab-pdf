def colab_pdf(file_name, notebookpath="/content/drive/My Drive/Colab Notebooks/"):
    import os

    # Checking if file_name passed is a sring.
    if not isinstance(file_name, str):
        raise TypeError(
            f"expected a string as file_name, but got {type(file_name)} instead."
        )

    # Using the defaults used by google.colab
    drive_mount_point = "/content/drive/"
    gdrive_home = os.path.join(drive_mount_point, "My Drive/")

    # If the drive is not already mounted, attempt to mount it.
    if not os.path.isdir(gdrive_home):
        from google.colab import drive

        drive.mount(drive_mount_point)

    # Check if the notebook exists in the Drive.
    if not os.path.isfile(os.path.join(notebookpath, file_name)):
        raise ValueError(f"file '{file_name}' not found in path '{notebookpath}'.")

    # Installing all the recommended packages.
    get_ipython().system(
        "apt update >> /dev/null && apt install texlive-xetex texlive-fonts-recommended texlive-generic-recommended >> /dev/null"
    )

    # If pdf with the same name exists, remove it.
    pdf_file = os.path.join(gdrive_home, file_name.split(".")[0] + ".pdf")
    
    if os.path.isfile(pdf_file):
        os.remove(pdf_file)

    # Attempt to convert to pdf and save it in Gdrive home dir using jupyter nbconvert command.
    try:
        get_ipython().system(
            "jupyter nbconvert --output-dir='$gdrive_home' '$notebookpath''$file_name' --to pdf"
        )
    except:
        return "nbconvert error"

    # Attempt to download the file to system.
    try:
        from google.colab import files

        file_name = file_name.split(".")[0] + ".pdf"
        files.download(gdrive_home + file_name)
    except:
        return "File Download Unsuccessful. Saved in Google Drive"

    return "File ready to be Downloaded and Saved to Drive"
