# CS598DL4H
Explainable Automated Coding of Clinical Notes using
Hierarchical Label-wise Attention Networks and Label Embedding
Initialisation  for CS598 DL4H in Spring 2023


```

Use `caml-mimic/env/bin/python` as the kernel for [caml-mimic/notebooks/dataproc_mimic_III.ipynb](caml-mimic/notebooks/dataproc_mimic_III.ipynb).

#### Explainable-Automated-Medical-Coding

```sh
pyenv local 3.7.11
python3.7 -m venv env
env/bin/pip install --upgrade pip
env/bin/pip install -r requirements.txt
```

Use `Explainable-Automated-Medical-Coding/env/bin/python` as the kernel for [Explainable-Automated-Medical-Coding/HLAN/demo_HLAN_viz.ipynb](Explainable-Automated-Medical-Coding/HLAN/demo_HLAN_viz.ipynb).


### Prerequisites / Demo

[MIMIC_III.ipynb](./MIMIC_III.ipynb)

### Training

Examples detailed in [Explainable-Automated-Medical-Coding/README.md](./Explainable-Automated-Medical-Coding/README.md).

```sh
cd Explainable-Automated-Medical-Coding/HLAN/
source ../env/bin/activate
```

#### MIMIC-III Top 50

Currently working off of `Explainable-Automated-Medical-Coding/datasets/mimiciii_*_50_th0.txt`.

##### Original

```sh
cd Explainable-Automated-Medical-Coding/HLAN/
../env/bin/python HAN_train.py \
    --dataset mimic3-ds-50 \
    --batch_size 32 \
    --per_label_attention=True \
    --per_label_sent_only=False \
    --num_epochs 100 \
    --report_rand_pred=False \
    --running_times 1 \
    --early_stop_lr 0.00002 \
    --remove_ckpts_before_train=False \
    --use_label_embedding=True \
    --ckpt_dir ../checkpoints/checkpoint_HAN_50_per_label_bs32_LE/ \
    --use_sent_split_padded_version=False \
    --marking_id 50-hlan \
    --gpu=True  # Colab only
```

##### Clone

See `scripts` directory for operational parameters for `HLAN`, `HA-GRU` and `HAN` variants with and without label embedding (`LE`):
* `scripts/HLAN+LE.sh`
* `scripts/HA-GRU+LE.sh`
* `scripts/HAN+LE.sh`
* `scripts/HLAN.sh`
* `scripts/HA-GRU.sh`
* `scripts/HAN.sh`



## Code Changes

### Refactoring of HAN Class

* Original source: `Explainable-Automated-Medical-Coding/HLAN/HAN_model_dynamic.py`
* Refactored source: `HLAN/HAN_model_dynamic.py`

