### Helpful commands to build and run the application

**Create Virtual Environment:**

```
uv venv
```

**Activate the Virtual Environment:**

```
.venv\Scripts\activate
```

**Deactivate when done**

```
deactivate
```

**Add `requirements.txt` file with required packages** Example:

```
numpy
pandas
scikit-learn
matplotlib
statsmodels
scipy
seaborn
requests
fastapi
uvicorn
jupyterlab
```

**Install the packages from the `requirements.txt` file**

```
uv pip install -r requirements.txt
```

**Run `Jupyter Lab`**

```
uv run jupyter lab
```
