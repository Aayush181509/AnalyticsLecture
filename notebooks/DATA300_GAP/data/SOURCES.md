# Bundled data for the DATA 300 GAP course section

These files let every lecture notebook and every guide's offline route (Route B) run without internet access. GitHub and some other sites are slow or blocked in mainland China, so nothing here is downloaded at run time.

All files were copied on 2026-10-25, byte for byte, from this repository's China classroom bundle (`notebooks/China_Classroom/data/`), which was downloaded on 2026-10-15 from the same public URLs the DATA 300 labs use. The Datasaurus Dozen comes from this repository's preserved copy. **Reuse terms are listed as reported by each upstream source and must be re-checked before any public redistribution outside this course.**

| File | Used for | Upstream source | Terms (verify) | SHA-256 |
|---|---|---|---|---|
| `penguins.csv` | Activity 1; pre-class refresher | seaborn-data (`mwaskom/seaborn-data`), from the Palmer Penguins data (Horst, Hill & Gorman) | Palmer Penguins: CC0 | `e07636bd8af74260099ea2f8678e2eabbf35def579940cc76f67061ee16c06c1` |
| `diamonds.csv` | Lab 1 | seaborn-data, from the ggplot2 `diamonds` dataset | Distributed with ggplot2 (MIT licence) | `9574730b03aba241d899c4a97511c5061b19358fab89510774fb6c24168345c4` |
| `tips.csv` | Assignment 1 | seaborn-data, from Bryant & Smith (1995) *Practical Data Analysis* | Widely redistributed teaching dataset; no explicit licence found | `e54cc4d2ce1bff65d32ca60b3e4b802e06bde1d7e7caf6f796f6bf7370e863b0` |
| `mpg.csv` | Lab 5 | seaborn-data, from the UCI Auto MPG dataset | UCI datasets: CC BY 4.0 | `c14b8b855ea7ee86cb9736bf8caaf281c4685ca08826f3eb2acaccaaf40f0d5a` |
| `datasaurus_dozen.csv` | Day 1 lecture | `data/raw/datasaurus-dozen/` (datasauRus R package) | MIT licence | `472324f6c71b26a92ed4741054850558db829efbf993c7b5d3c4f70d21b69fba` |
| `nltk_data/sentiment/vader_lexicon.zip` | Lab 3, Assignment 2, capstone | `nltk/nltk_data` (VADER lexicon, Hutto & Gilbert 2014) | VADER: MIT licence | `8adba4294eef3964d820bf655e37e61bdc3a341994356af59b74fb3b4a36ce5c` |
| `nltk_data/corpora/stopwords.zip` | Lab 3 | `nltk/nltk_data` | Per nltk_data package terms | `48c0e52d8b52546e827f53761fb30300c0ab94f70660d28bd65ba0a86270946b` |
| `nltk_data/tokenizers/punkt_tab.zip` | Lab 3 | `nltk/nltk_data` (Punkt tokenizer tables) | Per nltk_data package terms | `e57f64187974277726a3417ca6f181ec5403676c717672eef6a748a7b20e0106` |

The CO₂ series for Lab 4 is not bundled: it ships inside `statsmodels` (`sm.datasets.co2`) and loads offline.

Notebooks that need NLTK add `data/nltk_data` to NLTK's search path and unzip `punkt_tab.zip` on first use; NLTK reads the other two directly from their zip files.

To check the files after copying them to another computer, run this in the `data` folder:

```bash
shasum -a 256 *.csv nltk_data/*/*.zip
```

On Windows, use `certutil -hashfile penguins.csv SHA256` for each file.
