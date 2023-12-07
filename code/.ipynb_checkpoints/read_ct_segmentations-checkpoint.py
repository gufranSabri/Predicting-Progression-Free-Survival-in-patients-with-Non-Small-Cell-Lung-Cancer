import SimpleITK as sitk # importing the simpleitk library

ct_segmentation = sitk.ReadImage('filename.mha') # reading mha file
ct_segmentation_as_array = sitk.GetArrayFromImage(ct_segmentation) # getting segmentation as a numpy array
