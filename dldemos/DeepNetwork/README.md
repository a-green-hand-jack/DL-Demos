1. Install the repository

```shell
python setup.py develop
```

2. Download the dataset from https://www.kaggle.com/datasets/fusicfenta/cat-and-dog?resource=download and organize the directory as follows:

```plain text
└─data
    └─archive
        └─dataset
            ├─single_prediction
            ├─test_set
            │  ├─cats
            │  └─dogs
            └─training_set
                ├─cats
                └─dogs
```

3. Modify the path in `main.py`:

```Python
train_X, train_Y, test_X, test_Y = get_cat_set(
        'dldemos/LogisticRegression/data/archive/dataset', train_size=1500)
```

Replace 'dldemos/LogisticRegression/data/archive/dataset' with your path.

4. Run `main.py`. (You can open and close `save()` and `load()`  using comment)

You can edit the model hyper-parameters and see what will happen.
