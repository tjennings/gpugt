# GPUGT

GPU-accelerated counterfactual regret minimization for imperfect-information games.

## Setup

```bash
uv sync          # install all dependencies (including dev)
```

Requires an NVIDIA GPU with CUDA 13.x driver support. CUDA runtime libraries are provided via pip nvidia packages and pre-loaded in `gpugt/__init__.py`.

## Running

Game files are gitignored and must be generated from OpenSpiel before solving:

```bash
uv run python scripts/open-spiel-game.py kuhn_poker | uv run python scripts/compress.py > games/kuhn-poker.json
```

Then solve:

```bash
uv run python scripts/solve.py games/kuhn-poker.json gpugt.games.TwoPlayerZeroSumExtensiveFormGame gpugt.regret_minimizers.CounterfactualRegretMinimization 1024 -a -e figures/gpugt/exploitabilities/kuhn-poker.pdf -v figures/gpugt/values/kuhn-poker.pdf -n "Kuhn poker" > data/gpugt/kuhn-poker.json
```

## Validation

All checks must pass before submitting changes:

```bash
uv run flake8 gpugt                                                    # PEP 8 style
uv run mypy --strict gpugt                                             # strict type checking
uv run interrogate -f 100 -i -m -n -p -s -r '^\w+TestCase' gpugt      # 100% docstring coverage
uv run python -m unittest                                              # unit tests
uv run python -m doctest gpugt/*.py                                    # doctests
```

## Code Standards

- PEP 8 compliance (enforced by flake8)
- `mypy --strict` must pass -- all code must be fully typed
- 100% docstring coverage (enforced by interrogate)
- All unit tests and doctests must pass

## Project Structure

- `gpugt/` -- main package (games, regret_minimizers, utilities)
- `scripts/` -- CLI scripts for game conversion, solving, plotting, summarization
- `games/` -- game JSON files (gitignored, generated from OpenSpiel)
- `data/` -- solver output JSON
- `figures/` -- generated PDF plots
