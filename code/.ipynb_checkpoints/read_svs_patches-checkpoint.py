import h5py # Importing the h5 library to read the files

# Reading the h5 file
with h5py.File('filename.h5', 'r') as h5_file:
    # getting the keys from the h5_file, where each key represents a patch
    keys = h5_file.keys()

    # getting the first patch (the first key) in the file
    patch = h5_file[str(key[0])][:] # this returns the patch as a numpy array
                                    # with shape (256,256,3)
