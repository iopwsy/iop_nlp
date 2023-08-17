# Natural Language Process by IOP,CAS
## NLP example including creating and train models by IOP
author: Siyuan Wu
* Ref:

data/data.json: storing the datasets for NLP model

* example:
$    {
$    "abstract": {
$      "0": "abstract0",
$      "1": "abstract1",
$     },
$     "label": {
$      "0": 1,
$      "1": 0
$     }
$    }

labeled as 0 represents it doesn't belong to it while labeled as 1 represents it belongs.

run as 'python iop_NLP.py'
the model is stored at 'model' folder