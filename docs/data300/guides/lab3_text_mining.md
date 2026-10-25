# Lab 3: Text mining

<p class="lead">
Your third graded Python lab. You turn ten short customer reviews of a tablet into numbers: clean and tokenise the text, find the most frequent keywords, draw a word cloud, score each review's sentiment with VADER, chart how many reviews are positive, neutral and negative, answer questions about what you see, and submit one PDF on GAP.
</p>

*Adapted from the DATA 300 GAP course, In-Class Module 1, Lab 3: Text Mining Application. Written in our own words; follow GAP for the official wording.*

---

## 1. What and why

| | |
|---|---|
| **What you do** | Run GAP's setup code, then two blocks of given Python code (key terms, then sentiment) on ten product reviews, and answer five questions in three sections in a Markdown cell at the bottom of the notebook |
| **Why** | Most of what customers tell a business is free text. The lab's scenario is a consultant asked to summarise a batch of tablet reviews for the product's engineering teams without reading thousands of them by hand |
| **CLOs** | CLO 3 (computational methods to find patterns in unstructured data), CLO 1 (the business question descriptive and predictive analytics can answer), CLO 2 (communicating findings with a chart) |
| **Weight** | 3% |
| **Deadline** | **Thursday 12 November, 23:59 China Standard Time**, on GAP (worked on in periods 5 and 6 of Day 3) |
| **Before you start** | The [Text mining](../D3_lecture_text_mining.md) lecture, especially Parts 2–8 |

The data is a small table built inside the notebook: one row per review, with a review number and the review text. There is no rating column; the sentiment comes only from the text.

---

## 2. Route A: Try JupyterLab (as on GAP)

### Part 1: Open and name a notebook

Open Try JupyterLab, start a **Python (Pyodide)** notebook and rename it with the file name GAP gives (your last name, the course code and "AppliedLab3").

### Part 2: Set up NLTK and load the reviews

Paste GAP's first code block into a cell and run it. In outline, it:

1. installs `nltk`, `wordcloud` and `seaborn` into the browser session with `%pip`;
2. imports pandas, matplotlib, seaborn, NLTK's VADER analyser, stop-word list and tokeniser, and `WordCloud`;
3. defines a small helper that downloads NLTK data files from GitHub with `pyfetch` and unzips them, then uses it (with `await`) to fetch the VADER lexicon, the Punkt tokeniser tables (`punkt` and `punkt_tab`) and the stop-word lists;
4. builds a DataFrame of ten reviews and shows the first rows.

The downloads take a few seconds each. Wait until the cell finishes (the `[*]` becomes a number) before going on.

### Part 3: Preprocessing and key terms

Paste and run GAP's second block. It joins all ten reviews into one lower-case string, tokenises it, keeps only alphabetic tokens that are not stop words (NLTK's English list **plus three product words** GAP adds), draws a **word cloud**, and prints the **five most frequent keywords** with their counts.

### Part 4: Sentiment with VADER

Paste and run GAP's third block. It downloads the VADER lexicon again (harmless if you already have it), creates the analyser, rebuilds the same ten-review table, adds each review's **compound score**, labels it Positive (≥ 0.05), Negative (≤ −0.05) or Neutral (in between), shows the table, and draws a **bar chart of how many reviews fall in each label**.

### Part 5: Answer the questions

Add a **Markdown** cell at the bottom and answer GAP's questions in full sentences. They come in three sections: preprocessing and key terms (what a stop word is and why removing it matters for frequency counts; which product feature is discussed most), the sentiment scores (the exact score of one named review and whether it matches a human reading; why another named review is labelled Neutral), and a business recommendation to an engineering team, backed by specific outputs. Read every value from **your own output** and name the table or chart it comes from.

### Part 6: Export and submit

Run everything from the top, then **File → Print → Save as PDF** with *Background graphics* ticked. See *Submission* below.

---

## 3. Route B: offline in Anaconda JupyterLab

Use this route if the NLTK downloads from GitHub fail or hang, or if you prefer your own laptop. It follows the same steps as GAP's code but reads NLTK's data from the course folder (`data/nltk_data`), so nothing is installed or downloaded. Create a notebook **inside the `DATA300_GAP` folder** (next to `data`), named as in Route A. Paste the block into one cell, or split it at the `# ---` lines into cells that match GAP's parts. The ten reviews and the questions are the same as in Route A.

Two small differences from GAP's code, neither of which changes any number: the bar chart uses colour-blind-safe colours in a fixed order, and the word cloud uses a fixed layout so it looks the same on every run.

```{.python .offline}
# Route B for Lab 3: run offline in Anaconda JupyterLab.
# NLTK's data comes from the course folder (data/nltk_data), so nothing is downloaded.

# --- Part 2a: point NLTK at the bundled data (run once per session)
import re
import zipfile
from pathlib import Path

import nltk

NLTK_DIR = Path("data/nltk_data").resolve()
if not (NLTK_DIR / "tokenizers" / "punkt_tab").exists():
    with zipfile.ZipFile(NLTK_DIR / "tokenizers" / "punkt_tab.zip") as z:
        z.extractall(NLTK_DIR / "tokenizers")
nltk.data.path.insert(0, str(NLTK_DIR))

import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud

# The bundle has the newer 'punkt_tab' tables only. NLTK 3.8.2 and later use them.
# Older NLTK looks for 'punkt' instead; this fallback splits sentences with a simple
# rule and gives the same tokens for these reviews.
try:
    word_tokenize("Check. Done.")
    tokenize = word_tokenize
    print("NLTK", nltk.__version__, "- using word_tokenize with punkt_tab")
except LookupError:
    def tokenize(text):
        sentences = re.split(r"(?<=[.!?])\s+", text)
        return [tok for s in sentences for tok in word_tokenize(s, preserve_line=True)]
    print("NLTK", nltk.__version__, "- older version, using the sentence-split fallback")

# --- Part 2b: the ten reviews from GAP
data = {
    "Review_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Review_Text": [
        "Absolutely love the new OmniPad! The battery life is amazing and the screen is beautiful.",
        "Terrible experience. The screen cracked after one week and customer service was completely useless.",
        "It is an okay tablet. Nothing special, but it gets the job done for basic web browsing.",
        "The battery life is incredibly poor. I have to charge it twice a day. Very disappointed.",
        "Fantastic device! Fast processor, great camera, and very lightweight. Highly recommend.",
        "Overpriced garbage. The software is laggy and it crashes constantly.",
        "A solid upgrade from the previous generation. The stylus integration is perfect for my artwork.",
        "I hate the new update. It ruined the user interface and made everything slower.",
        "Decent value for the price. The battery is fine, but the camera could be better.",
        "Best purchase I've made this year. Beautiful display and amazing battery life!",
    ],
}
df = pd.DataFrame(data)
print("--- Raw customer reviews ---")
print(df.to_string(index=False))

# --- Part 3: preprocessing, word cloud and top five keywords
all_text = " ".join(df["Review_Text"]).lower()
stop_words = set(stopwords.words("english"))
stop_words.update(["omnipad", "tablet", "device"])      # the same product words GAP adds

words = tokenize(all_text)
cleaned_words = [w for w in words if w.isalpha() and w not in stop_words]

wordcloud = WordCloud(width=800, height=400, background_color="white",
                      colormap="viridis", random_state=0).generate(" ".join(cleaned_words))
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Key terms in the product reviews (word size = frequency)", fontsize=16)
plt.show()

freq_dist = nltk.FreqDist(cleaned_words)
print("\n--- Top 5 most frequent keywords ---")
for word, count in freq_dist.most_common(5):
    print(f"Keyword: '{word}' | Frequency count: {count}")

# --- Part 4: VADER sentiment scores, labels and chart
analyzer = SentimentIntensityAnalyzer()
df["Compound_Score"] = df["Review_Text"].apply(lambda t: analyzer.polarity_scores(t)["compound"])

def categorize_sentiment(score):
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment_Label"] = df["Compound_Score"].apply(categorize_sentiment)
print("\n--- Sentiment results ---")
print(df[["Review_ID", "Review_Text", "Compound_Score", "Sentiment_Label"]].to_string(index=False))

order = ["Positive", "Neutral", "Negative"]
counts = df["Sentiment_Label"].value_counts().reindex(order, fill_value=0)
colours = ["#0072B2", "#B0B0B0", "#D55E00"]    # blue, grey, orange: readable with colour-blindness
plt.figure(figsize=(8, 5))
plt.bar(counts.index, counts.values, color=colours)
for x, v in enumerate(counts.values):
    plt.text(x, v + 0.05, str(v), ha="center")
plt.title("Distribution of customer sentiment labels", fontsize=16)
plt.xlabel("Sentiment label")
plt.ylabel("Number of reviews")
plt.show()
```

In JupyterLab you may replace the `print(... .to_string(index=False))` lines with `display(df)` for nicer tables; the numbers are the same. Export with **Kernel → Restart Kernel and Run All Cells**, then **File → Print → Save as PDF**.

---

## 4. Checks you can make

These tell you whether your output is right without giving any answers away.

- [ ] The setup cell runs without errors and without any network access (Route B), or every `await download…` line finishes (Route A).
- [ ] The review table has **10 rows**, numbered 1 to 10.
- [ ] The cleaned word list contains only lower-case words made of letters: no punctuation, no "the" or "and", and none of the three product words GAP removes.
- [ ] The word cloud shows words, not punctuation; the top-five list prints **five lines**, each with a whole-number count, in descending order.
- [ ] The sentiment table has **four columns** (ID, text, compound score, label), and every compound score lies between **−1 and +1**.
- [ ] Every label agrees with its score and the thresholds: ≥ 0.05 Positive, ≤ −0.05 Negative, otherwise Neutral.
- [ ] The three bars of the chart **add up to 10**.
- [ ] Each answer quotes the number or word it relies on, names the output it comes from, and, for the "does it match a human reading" and "why neutral" questions, explains the result with how VADER works (which words it knows, and the thresholds), not just with an opinion.

---

## 5. Known pitfalls and fixes

| Problem | Cause | Fix |
|---|---|---|
| The first cell hangs, or ends with a network or `pyfetch` error | GAP's code downloads NLTK data from GitHub, which can be slow or blocked | Wait a minute and run the cell again; if it still fails, switch to Route B, which needs no network |
| `SyntaxError: 'await' outside function`, or the downloads never seem to run | The `await` lines only work at the top level of a notebook cell in the browser kernel. They fail inside a function, in a `.py` script, or when cells are run out of order | Run GAP's blocks as notebook cells, in order, in Try JupyterLab. In Anaconda, use Route B instead |
| `ModuleNotFoundError: No module named 'pyodide'` in Anaconda | GAP's browser-only download code was pasted into Anaconda | Use the Route B code above |
| `ModuleNotFoundError: No module named 'nltk'` (or `wordcloud`) in Try JupyterLab | The `%pip install` line did not run in this session | Run the first cell again; every new Try JupyterLab session needs it |
| `LookupError: Resource punkt not found` (Route B) | Your NLTK is older than 3.8.2 and looks for `punkt`, which the course bundle does not include (it has the newer `punkt_tab`) | Route B's fallback handles this automatically. If you wrote your own code, use the `tokenize` function from Route B. Check your version with `print(nltk.__version__)` |
| `LookupError` for `stopwords`, `vader_lexicon` or `punkt_tab` (Route B) | The notebook is not in the `DATA300_GAP` folder, or the setup lines were skipped | Save the notebook inside `DATA300_GAP`, next to `data`, restart the kernel and run from the top |
| Part 4 downloads the VADER lexicon a second time | GAP's Part 4 is written to work on its own | Harmless; let it run. Route B loads it once |
| The bar chart raises an error mentioning `legend` | `sns.countplot(..., hue=..., legend=False)` needs **seaborn 0.13 or later**; older Anaconda versions have 0.12 | Check with `import seaborn as sns; print(sns.__version__)`. On an older version, remove `hue=` and `legend=False`, or use Route B's matplotlib bar chart |
| Red and green bars are hard to tell apart | GAP's palette uses red for negative and green for positive, which about 1 in 12 men cannot distinguish well | Use blue, grey and orange as Route B does, and keep the text labels on the axis. Your counts do not change |
| The bars appear in a different order from the labels you expect | seaborn orders categories by first appearance in the data | Add `order=["Positive", "Neutral", "Negative"]` to `countplot`, or use Route B's `reindex` |
| The word cloud looks different each time you run it | Word placement is random unless a seed is set | Normal: the word **sizes** (frequencies) do not change. Add `random_state=0` for a fixed layout |
| `NameError: name 'display' is not defined` | `display()` exists only inside Jupyter | Run the code in JupyterLab, or use `print()` as Route B does |
| Your answer quotes a score with a different number of decimals from a classmate's | Formatting only | Quote the score exactly as your table prints it |
| "not" and "very" never appear in the keyword list | They are in NLTK's stop-word list, so the preprocessing removes them | Expected in this lab; GAP's questions are about the output as produced. See *Beyond the lab* for why this matters |
| Charts are grey or missing in the PDF | *Background graphics* was off, or cells were not run before printing | Tick *Background graphics*; restart and run all, then print |

---

## 6. Beyond the lab

Optional, not graded. Try these in the same notebook after you have answered GAP's questions:

1. Look up the words behind a score that surprised you: `analyzer.lexicon.get("someword")` returns the word's rating, or `None` if VADER does not know it. Which words in that review does VADER know?
2. Remove `"not"`, `"no"` and `"very"` from `stop_words` and rebuild the top-ten keyword list. What changes, and when would you want these words kept?
3. List the bigrams of each review separately with `list(nltk.bigrams(tokens))` on that review's cleaned tokens. Are any pairs more informative than the single keywords?
4. Score each **sentence** of the mixed reviews separately (split on `". "`). Which reviews contain both a positive and a negative sentence?
5. Make a copy of the analyser, add one or two technical words that customers use as complaints to its `lexicon` with a negative rating you can justify, and re-score. What changed, and why is tuning a lexicon on the same ten reviews you report on a risky thing to do?
6. Write the business recommendation as the lecture's four parts: finding, evidence, action with an owner, and how you would know it worked.

---

## 7. Submission

| File | Contents |
|---|---|
| **Final file** | The executed notebook as one PDF: review table, word cloud, top-five keywords, sentiment table, bar chart and the Markdown cell with your answers, named `YourLastName_DATA300_AppliedLab3.pdf` |

1. Run **Kernel → Restart Kernel and Run All Cells** (Route B) or run every cell from the top (Route A), and check that every table and chart is visible.
2. Export with **File → Print → Save as PDF**, *Background graphics* ticked. If you wrote answers in a separate document instead, combine the PDFs **offline** as described in [Combining PDFs without internet](../setup.md#combining-pdfs-without-internet).
3. Open the PDF and check every part is present and readable, including the full review text in the table (print in landscape if it is cut off).
4. Upload it to **Applied Lab 3** on **GAP** and submit before **Thursday 12 November, 23:59 China Standard Time** ([how to submit](../setup.md#submitting-on-gap-moodle)).
