# Format data as detailed in Explainable-Automated-Medical-Coding/datasets/README.md
from csv_to_txt import main

main("caml-mimic/mimicdata/mimic3/dev_50.csv", "Explainable-Automated-Medical-Coding/datasets/mimiciii_dev_50_th0.txt")
main("caml-mimic/mimicdata/mimic3/test_50.csv", "Explainable-Automated-Medical-Coding/datasets/mimiciii_test_50_th0.txt")
main("caml-mimic/mimicdata/mimic3/train_50.csv", "Explainable-Automated-Medical-Coding/datasets/mimiciii_train_50_th0.txt")

# put additional data in place per Explainable-Automated-Medical-Coding/README.md
!cp caml-mimic/mimicdata/D_ICD_DIAGNOSES.csv Explainable-Automated-Medical-Coding/knowledge_bases/
!cp caml-mimic/mimicdata/D_ICD_PROCEDURES.csv Explainable-Automated-Medical-Coding/knowledge_bases/
