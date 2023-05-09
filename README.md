# CS598DL4H
### Explainable Automated Coding of Clinical Notes using Hierarchical Label-wise Attention Networks and Label Embedding
                                    CS598 DL4H - Spring 2023


### Citation to the original paper
Explainable Automated Coding of Clinical Notes using Hierarchical Label-wise Attention Networks and Label Embedding Initialisation https://arxiv.org/abs/2010.15728
<br />
<br />


### Link to the original paper’s repo
This project is using existing 'Explainable-Automated-Medical-Coding' repo from the original paper.<br />
https://github.com/acadTags/Explainable-Automated-Medical-Coding
<br />
<br />


### Dependencies
Original repo makes use of the following 'caml-mimic' repo <br />
https://github.com/dmcguire81/caml-mimic/tree/c10536badc2d69c7a42e69735143fa83d4625e00
<br />
<br />

### Data download instruction
MIMIC-III data is required to reproduce this paper. User has to apply for access to PhysioNet database. 
Instruction to access MIMIC-III data is available in https://eicu-crd.mit.edu/gettingstarted/access/. 
User needs to first finish a CITI training session, and then request access to MIMIC-III.
<br />
<br />

### Preprocessing Instructions
Copy the following files from MIMIC-III to 'caml-mimic' directory.<br />
If the downloaded MIMIC-III data is in \*.csv.gz format, then unzip it to \*.gz and then copy the files.<br />
<br />

```
D_ICD_DIAGNOSES.csv       caml-mimic/mimicdata/D_ICD_DIAGNOSES.csv
D_ICD_PROCEDURES.csv      caml-mimic/mimicdata/D_ICD_PROCEDURES.csv
NOTEEVENTS.csv            caml-mimic/mimicdata/mimic3/NOTEEVENTS.csv
DIAGNOSES_ICD.csv         caml-mimic/mimicdata/mimic3/DIAGNOSES_ICD.csv
PROCEDURES_ICD.csv        caml-mimic/mimicdata/mimic3/PROCEDURES_ICD.csv
```
<br />

The tree structure will look like below. 

```
mimicdata/
|   D_ICD_DIAGNOSES.csv
|   D_ICD_PROCEDURES.csv
└───mimic3/
    |   NOTEEVENTS.csv
    |   DIAGNOSES_ICD.csv
    |   PROCEDURES_ICD.csv

```
<br />
Copy the requirements.txt from root directory to 'caml-mimic' directory. <br />
(Existing requirements.txt in 'caml-mimic' repo is not working for us.)

<br />
Navigate to 'caml-mimic' directory and set the enviroment as follows.

```
pyenv local 3.7.11
python3.7 -m venv env_caml
env/bin/pip install --upgrade pip
env/bin/pip install -r requirements.txt
```


Use `caml-mimic/env_caml/bin/python` as the kernel for [caml-mimic/notebooks/dataproc_mimic_III.ipynb](caml-mimic/notebooks/dataproc_mimic_III.ipynb). <br />
Run the above dataproc_mimic_III.ipynb.
<br />
<br />

## Pretrained model 
Download checkpoints, cache_vocabulary_label_pik, and embeddings from [Onedrive](https://onedrive.live.com/?authkey=%21ACZVuCnEV2zDKow&id=22F95C44F607EC5B%21255141&cid=22F95C44F607EC5B).

Copy the files to corresponding directories in Explainable-Automated-Medical-Coding.

<br />
<br />

## Training Instructions
Navigate to root directory and run 'convert_and_copy_files.py'. This will convert the files generated in 'caml-mimic' and copy it to Explainable-Automated-Medical-Coding'. <br />
Navigate to Explainable-Automated-Medical-Coding' directory and set the enviroment as follows.

```
pyenv local 3.7.11
python3.7 -m venv env_explain
env/bin/pip install --upgrade pip
env/bin/pip install -r requirements.txt
```

### Train HLAN+LE_50
```
# HLAN+LE trained on MIMIC-III-50
HAN_train.py --dataset mimic3-ds-50 --batch_size 32 --per_label_attention=True --per_label_sent_only=False --num_epochs 100 --report_rand_pred=False --running_times 1 --early_stop_lr 0.00002 --remove_ckpts_before_train=False --use_label_embedding=True --ckpt_dir ../checkpoints/checkpoint_HLAN+LE_50/ --use_sent_split_padded_version=False --marking_id 50-hlan
```

### Train HAGRU+LE_50
```

# HAGRU+LE trained on MIMIC-III-50
HAN_train.py --dataset mimic3-ds-50 --batch_size 32 --per_label_attention=True --per_label_sent_only=True --num_epochs 100 --report_rand_pred=False --running_times 1 --early_stop_lr 0.00002 --remove_ckpts_before_train=False --use_label_embedding=True --ckpt_dir ../checkpoints/checkpoint_HAGRU+LE_50/ --use_sent_split_padded_version=False --marking_id 50-hagru
```

### Train HAN+LE_50
```
 HAN_train.py --dataset mimic3-ds-50 --batch_size 32--per_label_attention=False --per_label_sent_only=False --num_epochs 100 --report_rand_pred=False --running_times 1 --early_stop_lr 0.00002 --remove_ckpts_before_train=False --use_label_embedding=True --ckpt_dir ../checkpoints/checkpoint_HAN+LE_50/ --use_sent_split_padded_version=False --marking_id 50-han
```

## Evaluation
Once the models are trained, Copy the demo_HLAN_viz.ipynb from root directory to 'Explainable-Automated-Medical-Coding/HLAN/' directory. <br />
This modified files has the following code. Uncomment each group and run it by setting the following env and path. <br />
Code is added at the end of the file for printing prediction and f1-score.


```
cd HLAN/
source ../env_explain/bin/activate
```

### Result HLAN+LE_50
```
# HLAN+LE trained on MIMIC-III-50
ckpt_dir="../checkpoints/checkpoint_HLAN+LE_50/"
dataset = "mimic3-ds-50"
batch_size = 32
per_label_attention=True
per_label_sent_only=False
sent_split=False
```

### Result HAGRU+LE_50
```

# HAGRU+LE trained on MIMIC-III-50
ckpt_dir="../checkpoints/checkpoint_HAGRU+LE_50/"
dataset = "mimic3-ds-50"
batch_size = 32
per_label_attention=True
per_label_sent_only=True
sent_split=False
```

### Result HAN+LE_50
```
# HAN+LE trained on MIMIC-III-50
ckpt_dir="../checkpoints/checkpoint_HAN+LE_50/"
dataset = "mimic3-ds-50"
batch_size = 32
per_label_attention=False
per_label_sent_only=False
sent_split=False
```

## Table of results

#### Expected result as per paper
![DLH_Expected_Result](https://user-images.githubusercontent.com/110275249/236979834-13235542-16af-4c81-b758-1771814a3040.png)
#### Actual result as recreated
![DLH_Actual_Result](https://user-images.githubusercontent.com/110275249/236980463-991446fd-76c0-4bfd-97af-4b8b0cbaf6ed.png)

#### HLAN Attention Visualization
<img width="802" alt="HLAN-Attention" src="https://user-images.githubusercontent.com/110275249/236980090-5a18c9d3-af72-4a67-97a6-bf8262a3f5b1.png">


