# PatchWizardsPython
A repo to demonstrate PatchWizard on Python dependecies.

# How to use
```bash
# Create two virtual envs: one for pre-upgrade dependecies, one for post-.
python -m venv .venv-before
python -m venv .venv-after

# Install deps for each venvs:
source .venv-before/bin/activate
pip install -r requirements.before.txt
deactivate

source .venv-after/bin/activate
pip install -r requirements.after.txt
deactivate

# Then test if the project works in the pre-venv and breaks in the post-venv.
```

# Dependecies
1. `Matplotlib`
