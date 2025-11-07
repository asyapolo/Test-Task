def average_rating_report(rows):

# отчет по рейтингу моделей телефонов
    sums = {}
    counts = {}

    for row in rows:
        brand = row["brand"]
        rating = float(row["rating"])
        sums[brand] = sums.get(brand, 0.0) + rating
        counts[brand] = counts.get(brand, 0) + 1

    stats = []
    for brand, total in sums.items():
        avg = total / counts[brand]
        stats.append((brand, avg))

    stats.sort(key=lambda x: x[1], reverse=True)

    headers = ["brand", "rating"]
    table_rows = [[brand, round(avg, 2)] for brand, avg in stats]

    return headers, table_rows


REPORTS = {
    "average-rating": average_rating_report,
}