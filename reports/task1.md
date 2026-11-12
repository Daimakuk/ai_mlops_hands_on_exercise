# Task 1 report: Exploratory data analysis

| Field | Value |
| --- | --- |
| Student | Stefano Nicolo Centurion Antepara |
| Dataset | Bike Sharing — "day.csv" (2011–2012) |
| Task | 1 |
| Tag / commit | `task1` — verify tag and commit hash before submitting |
| How to run | From the project root: "uv sync" then "uv run python main.py" |
| Timebox | Record actual time used and completion status before submitting |

## 1. Summary

I explored daily bike rental demand using the Bike Sharing dataset (731 observations, 16 columns). Initial checks found no missing values, duplicate rows, duplicated dates, negative rental counts, or discrepancies between `cnt` and `casual + registered`. Average daily rentals were **4,504.35** (median **4,548**). The highest average by calendar month was in June (**5,772.37**), and the lowest in January (**2,176.34**). Normalized temperature was positively associated with daily rentals (Pearson **r = 0.627**). These are historical associations, not proof that temperature causes demand changes.

**Evidence:** `main.py`; terminal outputs for data checks, descriptive statistics, grouped averages and correlation.

## 2. Goal and success criteria

**Goal.** Assess the dataset's quality and identify interpretable rental-demand patterns that can inform a later interactive dashboard.

| Criterion | How it is measured | Target | Result |
| --- | --- | --- | --- |
| Understand the dataset | Shape, column types and date range | Identify dataset structure | 731 rows, 16 columns; 2011–2012 |
| Check data quality | Missing, duplicate, negative and inconsistent records | Identify and report issues | 0 in each tested check |
| Describe demand | Summary statistics and monthly averages | Report interpretable numerical findings | Mean 4,504.35; June highest, January lowest |
| Explore a relationship | Pearson correlation with `temp` | Report association and caveat | r = 0.627; causality not established |

**Evidence:** `main.py`; console outputs shared during the exercise.

## 3. Approach and key decisions

| # | Finding | Decision | Alternative considered | Where in the code |
| --- | --- | --- | --- | --- |
| D1 | The file contains one observation per day. | Analyze daily total rentals (`cnt`). | Analyze only `casual` or `registered`. | `main.py` |
| D2 | No nulls or exact duplicate rows were found. | Keep observations and perform domain-specific consistency checks. | Drop rows without evidence of an error. | `main.py` |
| D3 | The analysis question concerns seasonal demand. | Calculate **average daily rentals** by calendar month. | Use monthly totals, which are influenced by month length. | `main.py` |
| D4 | Temperature might relate to demand. | Inspect the relationship and calculate Pearson correlation. | Infer a relationship from the plot alone. | `main.py` |

**Evidence:** `main.py` (`isna`, `duplicated`, `groupby`, `corr`, and rental-total checks).

## 4. Results

| Result | Value | Baseline or reference |
| --- | --- | --- |
| Observations / columns | 731 / 16 | Original `day.csv` |
| Missing values / duplicate rows / duplicate dates | 0 / 0 / 0 | Data-quality checks |
| Negative rentals / inconsistent totals | 0 / 0 | `cnt >= 0`; `cnt = casual + registered` |
| Mean / median daily rentals | 4,504.35 / 4,548 | `cnt` descriptive statistics |
| Minimum / maximum daily rentals | 22 / 8,714 | `cnt` descriptive statistics |
| Standard deviation | 1,937.21 | `cnt` descriptive statistics |
| Highest / lowest monthly daily mean | June: 5,772.37 / January: 2,176.34 | Calendar-month grouping, 2011–2012 combined |
| Temperature–rentals Pearson correlation | +0.627 | `temp` vs `cnt` |

**Figure 1 — monthly demand:** `figures/monthly_rentals.png`. *Average daily rentals by calendar month; June averaged 5,772.37 and January 2,176.34.*

**Figure 2 — temperature:** `figures/temperature_vs_rentals.png`. *Normalized temperature and daily rental counts showed a Pearson correlation of +0.627.*

**Evidence:** `main.py`; analysis output. Two image files in `figures/` .

## 5. Problems and how you handled them

| Problem | Cause | What you did | Status |
| --- | --- | --- | --- |
| `ModuleNotFoundError: pandas` | Pandas was not available in the Python environment used to run the script. | Set up dependencies with `uv` and ran the project using `uv run`. | Solved |
| `uv` not recognized in PowerShell | `uv` was not yet available on the command path. | Installed/configured `uv`; confirmed Python 3.12.16. | Solved |
| `pyproject.toml` missing `[project]` | Invalid/incomplete project metadata for `uv add`. | Updated project metadata and installed dependencies. | Solved |


**Evidence:** `pyproject.toml`, `uv.lock`; PowerShell outputs

## 6. Limitations and trade-offs

| Area | Limitation or trade-off | Impact | Mitigation or next step |
| --- | --- | --- | --- |
| Data | Only 2011–2012 observations. | Results may not generalize to current usage. | Compare against recent data if available. |
| Analysis | Monthly results pool two years. | Year-specific changes may be hidden. | Compare monthly patterns separately for 2011 and 2012. |
| Interpretation | Pearson correlation measures linear association, not causation. | Cannot claim warmer weather directly causes more rentals. | Examine season, weather and other potential confounders. |
| Data quality | Passing null and duplicate checks does not exclude all anomalies. | Unusual low-rental days may need explanation. | Review extreme observations and business context. |

**Evidence:** `main.py`; dataset coverage; monthly summary; temperature correlation.

## 7. Next steps

| Priority | Next step | Why | Effort |
| --- | --- | --- | --- |
| 1 | Compare 2011 and 2012 trends. | Separate yearly growth from seasonality. | S |
| 2 | Review very low-rental days. | Investigate possible anomalies or exceptional conditions. | S |
| 3 | Build a Streamlit dashboard with year filters. | Make the findings explorable. | M |
| 4 | Containerize and launch the app with Docker Compose. | Complete Task 2 deployment. | M |

**Evidence:** `main.py`.

## 8. Use of AI assistants

| Tool | What you used it for | Where (files or sections) | How you checked the output |
| --- | --- | --- | --- |
| ChatGPT | Explanations of Pandas, statistics and exploratory-analysis commands; example code. | `main.py`| Executed code and compared outputs with the dataset. |
| ChatGPT | Troubleshooting `uv`, Python environment. | Project configuration and repository | Checked command outputs, Python version. |
| ChatGPT | Explanation of correlation and assistance drafting this report. | this document | Must review wording and ensure every conclusion is supported by actual output. |

During the simulation, the assistant sometimes proposed implementation steps before the preceding steps had been completed. I identified the mismatch when `app.py` had not yet been created and returned to the correct sequence. AI also provided substantial code and report wording; these contributions must be represented faithfully in `AI_LOG.md` rather than described only as syntax help.

**Evidence:** ChatGPT conversation; `AI_LOG.md`.

## Checklist

- [ ] Task tag pushed and named in the table at the top
- [ ] Runs from a fresh clone with the commands above
- [ ] No secrets, API keys or large data files committed
- [x] Every section has an Evidence line
- [x] Every referenced figure has a caption with a number
- [x] Guidance blocks and generic placeholders removed
- [ ] `AI_LOG.md` up to date
