# Debugging Diary

## Issue 1 — ModuleNotFoundError: No module named 'src.data'

**When:** Running `scripts/check_preprocess.py` for the first time.

**Error:**
## ModuleNotFoundError: No module named 'src.data'

**Investigation:**
Python could not find the `src` package because the project root
was not on the Python path. Running scripts directly does not
automatically add the project root to `sys.path`.

**Fix:**
Created a `setup.py` file and installed the project in editable
mode using `pip install -e .`. This registers the project root
as a package, making `from src.data.preprocess import ...` work
correctly from anywhere in the project.

**Lesson:**
Always install the project as an editable package when using
a `src/` layout. This avoids path hacks and mirrors how the
package would be installed in production.

---

## Issue 2 — ModuleNotFoundError: No module named 'pkg_resources'

**When:** Importing MLflow with Python 3.12.

**Error:**

## ModuleNotFoundError: No module named 'pkg_resources'


**Investigation:**
Python 3.12 removed `pkg_resources` from the standard library.
The installed version of MLflow (2.13.0) still depended on it.

**Fix:**
Upgraded MLflow to the latest version using:

The newer version no longer depends on `pkg_resources`.

**Lesson:**
Always verify library compatibility with the Python version before
starting. Python 3.12 has several breaking changes from 3.10/3.11.

---

## Issue 3 — Model F1 Score near 0 for readmission class

**When:** First training run with Random Forest.

**Observation:**

# F1 Score: 0.0045
# Recall for class 1: 0.00


**Investigation:**
The preprocessing was one-hot encoding `diag_1`, `diag_2`, `diag_3`
columns which contain thousands of unique ICD diagnosis codes.
This created 2,371 features, most of which were extremely sparse.
The Random Forest could not learn meaningful patterns from this
high-dimensional sparse space.

**Fix:**
Dropped `diag_1`, `diag_2`, `diag_3` from the feature set entirely.
This reduced features from 2,371 to 126 and improved model recall.

**Lesson:**
Always inspect feature cardinality before encoding. High-cardinality
categorical columns need special treatment (grouping, embeddings, or
target encoding) rather than naive one-hot encoding.

---

## Issue 4 — Random Forest still not predicting readmissions

**When:** Second training run after fixing features.

**Observation:**


# F1 Score: 0.02
# Recall for class 1: 0.01


**Investigation:**
Even with `class_weight="balanced"`, the Random Forest was still
predicting almost all records as negative (class 0). The model was
optimizing for accuracy rather than recall on the minority class.

**Fix:**
Switched from Random Forest to Logistic Regression with a
StandardScaler pipeline. Logistic Regression with balanced class
weights improved recall for class 1 from 0.01 to 0.54.

**Lesson:**
For imbalanced classification problems, Logistic Regression often
outperforms tree-based methods because it directly optimizes the
decision boundary rather than fitting individual trees.

---

## Issue 5 — api/main.py missing from Docker container

**When:** Running `uvicorn api.main:app` — got import error.

**Investigation:**
The file `api/main.py` was never saved properly in VS Code.
The `api/` folder only contained `schemas.py` and `predictor.py`.

**Fix:**
Created and saved `api/main.py` correctly. Verified with `ls api/`
before running uvicorn again.

**Lesson:**
Always verify files exist with `ls` before running commands that
depend on them.




