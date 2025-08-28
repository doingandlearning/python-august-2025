# Windows + VS Code + Python venv: Troubleshooting Guide (PowerShell policy errors)

## TL;DR (quick fix)

1. Open **PowerShell** (not as admin) and run:

```powershell
Get-ExecutionPolicy -List
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

2. Close/reopen VS Code.
3. In the project folder:

```powershell
py -m venv .venv
. .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

If you **cannot** change policy (managed laptop), switch the VS Code terminal to **Command Prompt** and activate with:

```cmd
.\.venv\Scripts\activate.bat
```

---

## Why this happens

PowerShell blocks running local scripts by default. A venv’s activator is a script (`Activate.ps1`), so you see errors like:

- “**… cannot be loaded because running scripts is disabled on this system**”
- “**File …\Activate.ps1 is not digitally signed**”

Changing the **CurrentUser** policy to `RemoteSigned` allows local scripts to run.

---

## Recommended setup (VS Code)

1. **Install Python** (from python.org or Store). Verify:

   ```powershell
   py --version
   python --version
   ```

2. In VS Code, **Command Palette → Python: Select Interpreter** → pick the one inside your project’s `.venv` once created.
3. Set the default terminal if needed:

   - **PowerShell** (default) → uses `Activate.ps1`.
   - **Command Prompt** → uses `activate.bat`.
   - **Git Bash** → uses `activate`.
     _(Settings → “Terminal: Integrated Default Profile (Windows)”.)_

---

## Clean venv creation & activation

From your **project root**:

```powershell
# create
py -m venv .venv

# activate (PowerShell)
. .\.venv\Scripts\Activate.ps1

# upgrade pip
python -m pip install --upgrade pip
```

**Other shells:**

```cmd
REM Command Prompt (cmd)
.\.venv\Scripts\activate.bat
```

```bash
# Git Bash
source .venv/Scripts/activate
```

---

## If you still get PowerShell policy errors

### A) Scripts disabled

**Error:** “… running scripts is disabled …”
**Fix (per-user, safe):**

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Close/reopen VS Code afterwards.

### B) Blocked file (downloaded or copied)

**Error:** “The file … is not digitally signed” (even after RemoteSigned)
**Fix:**

```powershell
Unblock-File -Path .\.venv\Scripts\Activate.ps1
```

### C) Corporate/locked-down device

If `Set-ExecutionPolicy` fails or Group Policy resets it:

- Use **cmd** terminal in VS Code and run:

  ```cmd
  .\.venv\Scripts\activate.bat
  ```

- Or use **WSL** (Ubuntu) and create a venv there:

  ```bash
  python3 -m venv .venv && source .venv/bin/activate
  ```

- Or run PowerShell with a one-off bypass:

  ```powershell
  powershell -ExecutionPolicy Bypass
  ```

### D) Wrong interpreter selected in VS Code

**Symptom:** `pip` installs but `import` fails, or Python shows a different version.
**Fix:** Command Palette → **Python: Select Interpreter** → pick `.\.venv\Scripts\python.exe`.

### E) `py` not found / multiple Pythons

**Fixes:**

- Verify launcher: `py --list`.
- If missing, try `python` directly: `python -m venv .venv`.
- Ensure PATH includes your chosen Python, or reinstall Python **for current user** and include the **launcher**.

### F) Long path or weird folder names

Avoid spaces and very deep paths for projects (Windows path length can still bite in tools).

---

## Sanity check (does venv work?)

With venv **activated**:

```powershell
where python
python -c "import sys; print(sys.prefix); print(sys.executable)"
python -m pip list
```

Expect paths inside your project’s `.venv`.

---

## Reset / inspect policies

```powershell
Get-ExecutionPolicy -List
# If you want to revert the per-user change:
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Undefined
```

_(If another scope like MachinePolicy is set by IT, that will still win.)_

---

## Minimal “it just works” checklist for students

- ✅ Installed Python (verify with `py --version`).
- ✅ Project folder has **no** weird characters and is not too deep.
- ✅ Created `.venv` in the project root.
- ✅ VS Code terminal matches your chosen shell (PowerShell or cmd).
- ✅ Policy fixed (`RemoteSigned`) **or** using cmd’s `activate.bat`.
- ✅ VS Code interpreter set to `.\.venv\Scripts\python.exe`.

---

## Template commands to paste into a fresh project

```powershell
# PowerShell path
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
py -m venv .venv
. .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install {{ PACKAGE_1 }} {{ PACKAGE_2 }}
```

```cmd
REM Command Prompt path
py -m venv .venv
.\.venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install {{ PACKAGE_1 }} {{ PACKAGE_2 }}
```
