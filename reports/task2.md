# Task 2 report: Interactive Bike Sharing Dashboard Deployment

| Field | Value |
| --- | --- |
| Student | Stefano Nicolo Centurion Antepara |
| Dataset | Bike Sharing — `day.csv` |
| Task | 2 — App deployment |
| Tag / commit | `task2` |
| How to run | `docker compose up --build -d`; check `docker compose ps` and `docker compose logs dashboard`; open the host port configured in `compose.yaml` (8501 or 8502); stop with `docker compose down` |
| Timebox | Elapsed time not recorded |

## 1. Summary

The project turns the Task 1 exploration of daily bicycle rentals into an interactive web dashboard. It uses Python, Pandas and Streamlit to display dataset records, filter by year, and explore monthly rental trends, temperature association and user types. The application is packaged using a Dockerfile and launched with Docker Compose. The daily dataset has 731 records spanning 2011 and 2012. An initial Docker startup encountered a host-port collision on port 8501; the issue was addressed by freeing the port or changing the host mapping. The main limitation is that the deployment has only been tested locally, not in a production environment.

**Evidence:** `app.py`, `datasets/day.csv`, `Dockerfile`, `compose.yaml`;

## 2. Goal and success criteria

**Goal.** Deploy a containerized application that supports interactive exploration of the same Bike Sharing dataset used in Task 1.

| Criterion | How it is measured | Target | Result |
| --- | --- | --- | --- |
| Interactive exploration | Change year selection and inspect metrics and charts | 2011 / 2012 / all | Implemented in `app.py`; browser behavior to confirm |
| Reproducible container build | Run `docker compose up --build -d` | Image builds without errors | User reported the deployment working after resolving the port conflict; preserve logs for evidence |
| Browser access | Open the mapped host port | Dashboard loads | User reported successful recovery; screenshot still needed |
| Data integrity | Compare observations with source CSV | 731 rows with all years selected | Expected from Task 1; verify in the container |

**Evidence:** `app.py`.

## 3. Approach and key decisions

| # | Finding | Decision | Alternative considered | Where in the code |
| --- | --- | --- | --- | --- |
| D1 | The project already uses Python and Pandas | Use Streamlit for a small interactive dashboard | Writing an HTTP server and HTML interface manually | `app.py`, `pyproject.toml` |
| D2 | The input is a small static daily CSV | Read the CSV locally inside the container | Separate database or data API | `app.py`, `datasets/day.csv`, `Dockerfile` |
| D3 | One app is sufficient for the task | Deploy one container using Docker Compose | Kubernetes/minikube | `Dockerfile`, `compose.yaml` |
| D4 | Reproducibility and image size matter | Use Python 3.12 slim and locked dependencies with `uv` | Installing unpinned packages during every build | `Dockerfile`, `uv.lock` |

**Architecture:** Browser → host port → Docker Compose service → Streamlit/Pandas → local `day.csv`.

**Evidence:** `Dockerfile`, `compose.yaml`, `uv.lock`, `app.py`.

## 4. Results

| Result | Value | Baseline or reference |
| --- | --- | --- |
| Daily observations | 731 | Source `day.csv` |
| 2011 observations | 365 | Year filter (`yr == 0`) |
| 2012 observations | 366 | Year filter (`yr == 1`) |
| Overall mean daily rentals | About 4,504 | Task 1 analysis |
| Overall temperature–rentals correlation | About 0.627 | Task 1 analysis; value changes with filtering |
| Application runtime | Docker Compose service `dashboard` | Local Streamlit run |

The dashboard includes year-dependent metrics, monthly averages, a temperature–rentals scatter plot and a comparison of casual versus registered users. The reported numbers above describe the dataset; they are not evidence of a completed container test on their own.

**Evidence:** `app.py`, `datasets/day.csv`, `main.py`; `docker compose ps`.

## 5. Problems and how you handled them

| Problem | Cause | What you did | Status |
| --- | --- | --- | --- |
| Docker could not bind `0.0.0.0:8501` | Host port 8501 was already in use, likely by locally running Streamlit | Stop the local Streamlit process or map host port 8502 to container port 8501, then restart Compose | Reported resolved |
| Different local and container execution paths | The app must bind to all interfaces in the container | Configure Streamlit with `--server.address=0.0.0.0` | Configured in Dockerfile; verify logs |

**Evidence:** Docker daemon port-bind error from the terminal; `compose.yaml`; `Dockerfile`; subsequent `docker compose ps` output to capture.

## 6. Limitations and trade-offs

| Area | Limitation or trade-off | Impact | Mitigation or next step |
| --- | --- | --- | --- |
| Operations | Local Docker Desktop deployment only | No evidence of production readiness | Repeat deployment from a clean clone |
| Architecture | Single-container dashboard | No independent scaling of UI and data services | Appropriate for 731 rows; separate services only if needed |
| Data | CSV is packaged with the image | New data requires a rebuild | Use a mounted volume or external source if the dataset changes |
| Analytics | Correlation is observational, not causal | Risk of overstating weather effects | Describe it as an association and retain clear labels |
| Security | No authentication on the dashboard | Not appropriate for private data on a public host | Limit access and add authentication before public deployment |

**Evidence:** `app.py`, `Dockerfile`, `compose.yaml`, `datasets/day.csv`.

## 7. Next steps

| Priority | Next step | Why | Effort |
| --- | --- | --- | --- |
| 1 | Save browser screenshot and `docker compose ps`/logs | Demonstrate end-to-end deployment | S |
| 2 | Rebuild from a fresh clone | Confirm reproducibility | S |
| 3 | Review repository for secrets and unwanted large files | Meet submission rules | S |
| 4 | Update `AI_LOG.md`, commit, tag `task2` and push | Complete task hand-in | S |

**Evidence:** Git history and remote tag once created.

## 8. Use of AI assistants

| Tool | What you used it for | Where (files or sections) | How you checked the output |
| --- | --- | --- | --- |
| ChatGPT | Proposed and drafted substantial Streamlit code for filters, statistics and charts | `app.py` | Reviewed the displayed dashboard and dataset-derived values; remaining checks listed above |
| ChatGPT | Drafted the Dockerfile and Compose configuration, explained the port collision and troubleshooting | `Dockerfile`, `compose.yaml` | Local Docker startup reported successful after troubleshooting; command output not yet captured |
| ChatGPT | Drafted this report and explained the required template | `reports/task2.md` | Must be reviewed and rewritten in the student's own words before submission |

One AI-assisted choice was initially unnecessary: replacing Streamlit with a manual Python HTTP server, even though the official instructions allow any framework. The project returned to Streamlit because it was simpler for this dashboard. AI also supplied core application and deployment code, beyond the boilerplate assistance described in the exercise ground rules; this must be disclosed accurately and the student must understand and be able to justify the submitted work.

**Evidence:** `AI_LOG.md`.

## Checklist

- [ ] `task2` tag pushed and named in the table at the top
- [ ] Runs from a fresh clone with the commands above
- [ ] No secrets, API keys or unwanted large data files committed
- [ ] Every section has an Evidence line
- [ ] Screenshots and terminal evidence attached or linked as needed
- [x] Template guidance blocks and blank placeholders removed
- [ ] `AI_LOG.md` accurately updated
- [ ] Report reviewed and rewritten in the student's own words
