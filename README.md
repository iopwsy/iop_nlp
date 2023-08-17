# Natural Language Process by IOP,CAS
## NLP example including creating and train models by IOP

* author: Siyuan Wu
* Email: sywu@iphy.ac.cn
* Ref:  

data/data.json: storing the datasets for NLP model

* example:
```json
    {
    "abstract": {
      "0": "abstract0",
      "1": "abstract1",
      "2": "abstract2",
     },
     "label": {
      "0": 1,
      "1": 0,
      "2": 1,
     }
    }
```

labeled as 0 represents it doesn't belong to it while labeled as 1 represents it belongs.

* What's need for it?

    ```
    tensorflow
    pandas
    scikit-learn
    ```

* iop_NLP.py is the main code

    run ```python iop_NLP.py```

    then a NLP model will be created in model/ floder with text.json


