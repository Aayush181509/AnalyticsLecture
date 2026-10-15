# Bundled data for the DATA 300 China classroom

These files ship with the notebooks so the course runs without internet access (GitHub and Google are unreliable in mainland China). Downloaded on 2026-10-15 from the same URLs the DATA 300 syllabus labs use, except the Datasaurus Dozen, which comes from this repository's preserved copy. **Reuse terms are listed as reported by each upstream source and must be re-checked before any public redistribution outside this course.**

| File | Used in | Upstream source | Notes on terms (verify) | SHA-256 |
|---|---|---|---|---|
| `penguins.csv` | Activity 1 | seaborn-data (`mwaskom/seaborn-data`), from the Palmer Penguins data (Horst, Hill & Gorman) | Palmer Penguins is released under CC0 | `e07636bd…c06c1` |
| `diamonds.csv` | Lab 1 | seaborn-data, from the ggplot2 `diamonds` dataset | Distributed with ggplot2 (MIT licence) | `9574730b…345c4` |
| `tips.csv` | Assignment 1 | seaborn-data, from Bryant & Smith (1995) *Practical Data Analysis* | Widely redistributed teaching dataset; no explicit licence found | `e54cc4d2…0b8b0` |
| `mpg.csv` | Lab 5 | seaborn-data, from the UCI Auto MPG dataset | UCI datasets: CC BY 4.0 | `c14b8b85…16c94` |
| `datasaurus_dozen.csv` | Day 1 lecture | `data/raw/datasaurus-dozen/` (datasauRus R package) | MIT licence | `472324f6…69fba` |
| `nltk_data/sentiment/vader_lexicon.zip` | Lab 3, Assignment 2, capstone | `nltk/nltk_data` (VADER lexicon, Hutto & Gilbert 2014) | VADER is MIT-licensed | `8adba429…45c4` |
| `nltk_data/corpora/stopwords.zip` | Lab 3 | `nltk/nltk_data` | Per nltk_data package terms | `48c0e52d…946b` |
| `nltk_data/tokenizers/punkt_tab.zip` | Lab 3 | `nltk/nltk_data` (Punkt tokenizer tables) | Per nltk_data package terms | `e57f6418…0106` |

The CO₂ series for Lab 4 is not bundled: it ships inside `statsmodels` (`sm.datasets.co2`) and loads offline.

Notebooks add `data/nltk_data` to NLTK's search path and unzip `punkt_tab.zip` on first use (NLTK reads the other two directly from their zip files). Full SHA-256 values: run `shasum -a 256 *.csv nltk_data/*/*.zip` in this folder.
