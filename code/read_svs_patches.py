import h5py # Importing the h5 library to read the files
import cv2
import pandas as pd
import numpy as np
import os
from tqdm import tqdm

dftr = pd.read_csv("/Users/gufran/Desktop/PfsPredictionLungCancer/data/train_path_clin.csv")
dfte = pd.read_csv("/Users/gufran/Desktop/PfsPredictionLungCancer/data/val_path_clin.csv")

df_clinical = pd.read_csv("/Users/gufran/Desktop/PfsPredictionLungCancer/clinical_data/clinical_data.csv")


train_ids = list(dftr.dmp_pt_id)
val_ids = list(dfte.pdl1_image_id)

train_ids_filtered = []
val_ids_filtered = []
train_pt_ids_to_keep = []

train_pfs = []
val_pfs = []

for id in train_ids:
    slide_id = np.array(df_clinical[df_clinical.dmp_pt_id == id].slide_id)[0]
    pfs = np.array(df_clinical[df_clinical.dmp_pt_id == id].pfs)[0]
    if len(slide_id.split(" ")) == 1 and os.path.exists(f"/Users/gufran/Desktop/PfsPredictionLungCancer/pathology/pathology_patches256x256_hdf5/{slide_id}.svs"): 
        train_ids_filtered.append(slide_id)
        train_pt_ids_to_keep.append(id)
        train_pfs.append(pfs)


filtered_df = dftr[dftr['dmp_pt_id'].isin(train_pt_ids_to_keep)]
filtered_df["id"] = train_ids_filtered
# filtered_df.to_csv("/Users/gufran/Desktop/PfsPredictionLungCancer/data/train_path_clin_filtered.csv", index=False)

df_clinical = df_clinical.fillna(-1)
df_clinical["slide_id"] = pd.to_numeric(df_clinical["slide_id"], errors='coerce').astype(float)

for id in val_ids:
    if os.path.exists(f"/Users/gufran/Desktop/PfsPredictionLungCancer/pathology/pathology_patches256x256_hdf5/{id}.svs"):
        pfs = float(np.array(df_clinical[df_clinical.slide_id == id].pfs))
        val_ids_filtered.append(id)
        val_pfs.append(pfs)

dfte["id"] = val_ids_filtered
# dfte.to_csv("/Users/gufran/Desktop/PfsPredictionLungCancer/data/val_path_clin_filtered.csv", index=False)

# print(len(train_ids_filtered))
# print(train_pfs)
# print(len(val_ids_filtered))
# print(train_pfs)


for i in tqdm(range(len(train_ids_filtered))):
    with h5py.File(f'/Users/gufran/Desktop/PfsPredictionLungCancer/pathology/pathology_patches256x256_hdf5/{train_ids_filtered[i]}.svs/{train_ids_filtered[i]}.svs.h5', 'r') as h5_file:
        keys = h5_file.keys()
        num_patches_to_save = 30

        os.mkdir(f"/Users/gufran/Desktop/PfsPredictionLungCancer/data/pathology_patches/train30/{train_ids_filtered[i]}_{train_pfs[i]}")
        for key in keys:
            try:
                image_array = cv2.resize(h5_file[key][()], (100,100))
                cv2.imwrite(f"/Users/gufran/Desktop/PfsPredictionLungCancer/data/pathology_patches/train30/{train_ids_filtered[i]}_{train_pfs[i]}/patch{num_patches_to_save}.png", image_array)

                num_patches_to_save -= 1
                if num_patches_to_save == 0: break
            except:
                continue

for i in tqdm(range(len(val_ids_filtered))):
    with h5py.File(f'/Users/gufran/Desktop/PfsPredictionLungCancer/pathology/pathology_patches256x256_hdf5/{val_ids_filtered[i]}.svs/{val_ids_filtered[i]}.svs.h5', 'r') as h5_file:
        keys = h5_file.keys()
        num_patches_to_save = 30

        os.mkdir(f"/Users/gufran/Desktop/PfsPredictionLungCancer/data/pathology_patches/val30/{val_ids_filtered[i]}_{val_pfs[i]}")
        for key in keys:
            try:
                image_array = cv2.resize(h5_file[key][()], (100,100))
                cv2.imwrite(f"/Users/gufran/Desktop/PfsPredictionLungCancer/data/pathology_patches/val30/{val_ids_filtered[i]}_{val_pfs[i]}/patch{num_patches_to_save}.png", image_array)

                num_patches_to_save -= 1
                if num_patches_to_save == 0: break
            except:
                continue


