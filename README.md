# Natural Language Process by IOP,CAS
## NLP example including creating and train models by IOP

* author: Siyuan Wu(吴思远), Tiannian Zhu(朱天念), Sijia Tu(涂思佳), Ruijuan Xiao(肖睿娟), Jie Yuan(袁洁), Quansheng Wu(吴泉生), Hong Li(李泓) and Hongming Weng(翁红明)
* Email: sywu@iphy.ac.cn
* Ref:  Siyuan Wu, Tiannian Zhu, Sijia Tu, Ruijuan Xiao, Jie Yuan, Quansheng Wu, Hong Li and Hongming Weng. $\textit{xxx}$ xxx xx

* tree:
    ```
    │──iop_NLP.py
    │──README.md
    └─data
        └──data.json
    ```

`data/data.json`: storing the datasets for NLP model

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

* `iop_NLP.py` is the main code

    run <font color=yellow>python iop_NLP.py </font>

    then an NLP model `iop_NLP_model.h5` will be created in `model/` floder with `text.json`.

    the `iop_NLP_model.h5` is an NLP model.

    the `text.json` is the tokenizer file.

For code in `iop_NLP.py`:

* I create a class named <font color=green>iopNLP</font> for it



