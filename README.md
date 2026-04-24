# eldenring-sim

A lightweight data pipeline and interactive toolset for Elden Ring — built as a portfolio project demonstrating CSV-to-JSON transformation, static UI deployment and CI/CD automation.

## What it does

Two browser-based tools, served via GitHub Pages:

- **Build Manager v13** — AR calculator with weapon selection, upgrade level, affinity and stat requirements check
- **Efficiency Tracker** — Smithing stone farming route tracker with progress state

## Architecture

~~~
data/        CSV source files (weapons, reinforce tables, affinity rules)
scripts/     Python pipeline: CSV to validated JSON
docs/data/   Generated output: weapons_full.json + weapons_index.json
docs/        Static UI: vanilla JS reads JSON, no build step
.github/     CI: validates Python, runs export, checks JSON integrity
~~~

Key decisions:

- Split output into weapons_index.json and weapons_full.json for performance
- CI fails on dirty diffs so data and code stay in sync
- No frontend framework, vanilla JS keeps the tool dependency-free

## Live

https://guevo8.github.io/eldenring-sim/

## Stack

Python, Vanilla JS, GitHub Actions, GitHub Pages
