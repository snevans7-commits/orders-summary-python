# Orders Summary (Python)

This project implements a function that generates a summary of orders grouped by either day or customer.

## Goal

Return aggregated order metrics including:

- number of orders
- total order amount
- average order amount

Results can be grouped by:

- day
- customer

## Function

```python
get_orders_summary(data, from_, to, group_by, min_amount=None)
```

### Parameters

- **data**: list of orders
- **from_**: start date (YYYY-MM-DD, inclusive)
- **to**: end date (YYYY-MM-DD, inclusive)
- **group_by**: `"day"` or `"customer"`
- **min_amount** *(optional)*: minimum computed order amount

### Domain Rules

- Date filtering applies to `orderDate` (inclusive).
- Computed order amount = `sum(quantity * unitPrice)` across all line items.
- If `min_amount` is provided, only include orders with `computedAmount >= min_amount`.
- Group key:
  - **day** → YYYY-MM-DD from `orderDate`
  - **customer** → `customerId`
- Aggregations per group:
  - `count`
  - `totalAmount`
  - `avgAmount = totalAmount / count`
- Results must be sorted by key ascending.

## Project Structure

```
orders-summary-python
│
├── report.py
├── requirements.txt
├── README.md
│
└── tests
    ├── fixtures.json
    └── test_report.py
```

## Setup

Create a virtual environment:

```
python -m venv venv
```

Activate it:

Mac/Linux

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

## Run Tests

```
pytest
```

## Data

Test data is located in:

```
tests/fixtures.json
```
