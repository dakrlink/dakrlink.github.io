# dakrlink.github.io

![GitHub last commit](https://img.shields.io/github/last-commit/dakrlink/dakrlink.github.io?logo=github)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/dakrlink/dakrlink.github.io/Build%20and%20Deploy?logo=github) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/dakrlink/dakrlink.github.io?logo=github)

[dakr.link](http://dakr.link) / [dakrlink.github.io](https://dakrlink.github.io) - static page with my shortened urls and their QR codes.

## How to

1. Redirections defined with my hosting provider.
2. List of links and their's descriptions created using AsciiDoc (see my list in [dakr.link.adoc](https://github.com/dakrlink/dakrlink.github.io/blob/master/dakr.link.adoc)).
3. List of links created in csv file (see my list in [links.csv](https://github.com/dakrlink/dakrlink.github.io/blob/master/links.csv)).
4. QR codes generated from [links.csv](https://github.com/dakrlink/dakrlink.github.io/blob/master/links.csv) using [qrgen.py](https://github.com/dakrlink/dakrlink.github.io/blob/master/qrgen.py).
5. GitHub Page deployed using GitHub Action [Deploy to GitHub Pages](https://github.com/marketplace/actions/deploy-to-github-pages) (see Workflow file definition [.github/workflows/deploy.yml](https://github.com/dakrlink/dakrlink.github.io/blob/master/.github/workflows/deploy.yml)).
## QR codes

1. `mkvirtualenv qrgen`
2. `pip install -r requirements.txt`
### generate QR codes automatically

1. `workon qrgen`
2. `python qrgen.py`
3. `open links.csv`
4. `open build/qr/dakr-link.png`

### generate QR codes manually
1. `workon qrgen`
2. `qr dakr.link --output=dakr-link.png`
3. `open dakr-link.png`