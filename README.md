# QA Automation Practice

Practice project with Python, pytest, Selenium, API tests
and GitHub Actions CI.

## What I test

- SauceDemo login and product sorting with Selenium
- JSONPlaceholder API responses with Python requests
- Positive and negative test scenarios

## Run locally

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run all tests:

```powershell
python -m pytest -v
```

Run API-marked tests:

```powershell
python -m pytest -v -m api
```

## CI and evidence

GitHub Actions runs the tests after a push or pull request.
Selenium screenshots are available as an artifact named
`selenium-screenshots` on the workflow run page.