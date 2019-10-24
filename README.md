# Evaluation of binary classifiers under high class imbalance

## Data - Credit Card Fraud Detection

Anonymized credit card transactions labeled as fraudulent or genuine

> The datasets contains transactions made by credit cards in September 2013 by european cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions. It contains only numerical input variables which are the result of a PCA transformatios [...]

please see the original [kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud/data) page for details and author info

## Getting Started

clone this repository
```
git clone https://github.com/mbonart/class-imbalance.git
```

download the dataset into the `data` folder

```
python src/download_data.py
```


## Website Deployment

The website and presentation of this project is hosted on github pages. The `reveal.js` presentation can be generated with the following command:

```shell
pandoc --mathjax -t revealjs -s -o docs/index.html docs/presentation.md \
--css=www/custom.css \
--slide-level=3 \
--highlight-style=breezeDark \
-V revealjs-url=https://revealjs.com \
-V theme=night \
-V progress=true \
-V slideNumber=true \
-V hash=true \
-V navigationMode=linear \
-V transition='slide'
```

## Built With

- [reveal.js](https://github.com/hakimel/reveal.js)
- [pandas](https://github.com/pandas-dev/pandas)
- [pandoc](https://pandoc.org/)
- [scikit-learn](https://github.com/scikit-learn/scikit-learn)
- [plotly](https://github.com/plotly/plotly.py)
- [kaggle's credit card fraud detection dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)

## License

The content of the presentation and the content of the website for this project are licensed under the [Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/). The underlying source code is licensed under the MIT license.
