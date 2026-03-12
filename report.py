def get_orders_summary(*, data, from_, to, group_by, min_amount=None):
    groups = {}

    for order in data:
        order_date = order["orderDate"]

        if order_date < from_ or order_date > to:
            continue

        computed_amount = sum(
            item["quantity"] * item["unitPrice"]
            for item in order["lineItems"]
        )

        if min_amount is not None and computed_amount < min_amount:
            continue

        key = order_date if group_by == "day" else order["customerId"]

        if key not in groups:
            groups[key] = {"key": key, "count": 0, "totalAmount": 0}

        groups[key]["count"] += 1
        groups[key]["totalAmount"] += computed_amount

    results = []

    for key in sorted(groups):
        count = groups[key]["count"]
        total = groups[key]["totalAmount"]

        results.append({
            "key": key,
            "count": count,
            "totalAmount": total,
            "avgAmount": total / count
        })

    return {
        "groupBy": group_by,
        "results": results
    }
