# srategies for dealing with imbalanced data


## Getting Started

clone this repository
```
git clone https://github.com/mbonart/class-imbalance.git
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
