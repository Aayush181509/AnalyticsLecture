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
| `ecovate_focus_group.csv` | Assignment 4 (capstone) | The five fictional EcoVate focus-group comments printed in the DATA 300 syllabus, Assignment 4; typed into a CSV (columns `Review_ID`, `Review_Text`) on 2026-10-15 | Fictional case text from the course syllabus; course use only | `38f46e2e…a2ea` |
| `ecovate_base_demand.csv` | Assignment 4 (capstone) | The five-year EcoVate base demand plan (years 1–5) given in the DATA 300 syllabus, Assignment 4; typed into a CSV (columns `Year`, `Base_Demand`) on 2026-10-15 | Fictional case figures from the course syllabus; course use only | `ed990952…efba4` |

The CO₂ series for Lab 4 is not bundled: it ships inside `statsmodels` (`sm.datasets.co2`) and loads offline.

Notebooks add `data/nltk_data` to NLTK's search path and unzip `punkt_tab.zip` on first use (NLTK reads the other two directly from their zip files). Full SHA-256 values: run `shasum -a 256 *.csv nltk_data/*/*.zip` in this folder.

## Added for Days 4–5 (2026-10-16)

| File | Used in | Origin | Terms | SHA-256 |
|---|---|---|---|---|
| `leafline_simulation_practice.xlsx` | Day 5 lecture (financial modelling and simulation) | Made for this course with openpyxl: a **synthetic** LeafLine Tea branch model (Read me, Model and Simulation sheets; 1,000 trials of `RAND()` / `NORM.INV()` formulas, no stored values; Excel calculates on opening). Built deterministically (fixed document dates and zip timestamps) by a private generator script | Course material; synthetic, no third-party data | `b9ab22c8…f6bc` |

Generated in the notebooks, not bundled: the Assignment 2 home sales (500 rows, `np.random.seed(101)`, the syllabus's own generator) and the Day 4 bicycle listings (600 rows, `default_rng(2026)`), both synthetic. The Day 4 regression lecture reuses `diamonds.csv`.

## Added for Day 6 (2026-10-16)

| File | Used in | Origin | Terms | SHA-256 |
|---|---|---|---|---|
| `ecodrive_battery_costs.xlsx` | Day 6 lecture; Lab 7 (BI case study) | The 11 quarterly battery costs per vehicle (Q1-2023 to Q3-2025) of the **fictional** EcoDrive Motors, as printed in the DATA 300 syllabus, Applied Lab 7. One sheet, *Historical Data*: `Period` (1–11, the numeric timeline Excel's Forecast Sheet needs), `Battery Cost per EV ($)`, `Quarter` (label). Built with openpyxl deterministically (fixed document dates and zip timestamps) by a private generator script | Fictional case figures from the course syllabus; course use only | `4f168461…3bbb` |

Generated in the notebooks, not bundled: the Day 6 lecture's synthetic stores, job applicants and bank accounts (`default_rng` seeds 6, 11 and 3), the Lab 6 demand draws (seeds 2026 and 7) and the Assignment 3 reference simulation (seed 322). The Day 6 lecture also reuses `tips.csv`.
