import SimpleITK as sitk # Importing the simpleitk library

image = sitk.ReadImage('CT.nii') # Reading the nifti file
image = sitk.GetArrayFromImage(image) # getting a numpy array of it
image_int16 = np.int16(image) # converting it to int16 (since it is saved as int8)

