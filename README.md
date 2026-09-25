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


## Automated test coverage

| Area | Tool | What is checked |
| --- | --- | --- |
| Login, cart, checkout and sorting | Selenium + pytest | User flows and expected page results |
| Posts API | Python requests + pytest | Status codes, response data and negative cases |
| Posts API collection | Postman + Newman | Existing and missing posts |

## CI results

[![Python and Postman tests](https://github.com/Nevena90serbiangirl/qa-automation-practice/actions/workflows/tests.yml/badge.svg)](https://github.com/Nevena90serbiangirl/qa-automation-practice/actions/workflows/tests.yml)

GitHub Actions runs the Python and Postman tests on each push and pull request.
Open the [workflow runs](https://github.com/Nevena90serbiangirl/qa-automation-practice/actions) to see the latest result and download the JUnit, Postman and Selenium screenshot artifacts.

## Postman collection

The exported collection is in `Postman/qa-api-collection.json`.

On Windows PowerShell, run it with:

```powershell
newman.cmd run .\Postman\qa-api-collection.json