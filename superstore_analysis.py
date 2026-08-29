import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "data" / "superstore.db"

def run_query(title, query):
    print(f"\n{'=' * 60}")
    print(title)
    print('=' * 60)
    with sqlite3.connect(DB_PATH) as conn:
        for row in conn.execute(query):
            print(row)

queries = {
    "1. Total Sales + Profit": """
        SELECT ROUND(SUM(Sales), 2) AS Total_Sales,
               ROUND(SUM(Profit), 2) AS Total_Profit
        FROM orders;
    """,

    "2. Total Orders": """
        SELECT COUNT(DISTINCT `Order ID`) AS Total_Orders
        FROM orders;
    """,

    "3. Total Quantity Sold": """
        SELECT SUM(Quantity) AS Total_Quantity
        FROM orders;
    """,

    "4. Sales by Category": """
        SELECT Category,
               ROUND(SUM(Sales), 2) AS Sales
        FROM orders
        GROUP BY Category
        ORDER BY Sales DESC;
    """,

    "5. Profit by Category": """
        SELECT Category,
               ROUND(SUM(Profit), 2) AS Profit
        FROM orders
        GROUP BY Category
        ORDER BY Profit DESC;
    """,

    "6. Sales by Region": """
        SELECT Region,
               ROUND(SUM(Sales), 2) AS Sales
        FROM orders
        GROUP BY Region
        ORDER BY Sales DESC;
    """,

    "7. Profit by Region": """
        SELECT Region,
               ROUND(SUM(Profit), 2) AS Profit
        FROM orders
        GROUP BY Region
        ORDER BY Profit DESC;
    """,

    "8. Top 10 Products by Sales": """
        SELECT `Product Name`,
               ROUND(SUM(Sales), 2) AS Sales
        FROM orders
        GROUP BY `Product Name`
        ORDER BY Sales DESC
        LIMIT 10;
    """,

    "9. Top 10 Products by Profit": """
        SELECT `Product Name`,
               ROUND(SUM(Profit), 2) AS Profit
        FROM orders
        GROUP BY `Product Name`
        ORDER BY Profit DESC
        LIMIT 10;
    """,

    "10. Loss-making Products": """
        SELECT `Product Name`,
               ROUND(SUM(Profit), 2) AS Profit
        FROM orders
        GROUP BY `Product Name`
        HAVING Profit < 0
        ORDER BY Profit ASC
        LIMIT 10;
    """,

    "11. Sales by Segment": """
        SELECT Segment,
               ROUND(SUM(Sales), 2) AS Sales,
               ROUND(SUM(Profit), 2) AS Profit
        FROM orders
        GROUP BY Segment
        ORDER BY Sales DESC;
    """,

    "12. Sales by Ship Mode": """
        SELECT `Ship Mode`,
               COUNT(DISTINCT `Order ID`) AS Orders,
               ROUND(SUM(Sales), 2) AS Sales
        FROM orders
        GROUP BY `Ship Mode`
        ORDER BY Sales DESC;
    """,

    "13. Sales by Sub-Category": """
        SELECT `Sub-Category`,
               ROUND(SUM(Sales), 2) AS Sales,
               ROUND(SUM(Profit), 2) AS Profit
        FROM orders
        GROUP BY `Sub-Category`
        ORDER BY Sales DESC;
    """,

    "14. Top 10 Customers by Sales": """
        SELECT `Customer Name`,
               ROUND(SUM(Sales), 2) AS Sales,
               ROUND(SUM(Profit), 2) AS Profit
        FROM orders
        GROUP BY `Customer Name`
        ORDER BY Sales DESC
        LIMIT 10;
    """,

    "15. Discount vs Profit": """
        SELECT Discount,
               ROUND(SUM(Sales), 2) AS Sales,
               ROUND(SUM(Profit), 2) AS Profit
        FROM orders
        GROUP BY Discount
        ORDER BY Discount;
    """,

    "16. Year-wise Sales & Profit": """
        SELECT strftime('%Y', `Order Date`) AS Year,
               ROUND(SUM(Sales), 2) AS Sales,
               ROUND(SUM(Profit), 2) AS Profit
        FROM orders
        GROUP BY Year
        ORDER BY Year;
    """,

    "17. Monthly Sales": """
        SELECT strftime('%Y-%m', `Order Date`) AS Month,
               ROUND(SUM(Sales), 2) AS Sales
        FROM orders
        GROUP BY Month
        ORDER BY Month;
    """,

    "18. Highest Sales City": """
        SELECT City,
               ROUND(SUM(Sales), 2) AS Sales
        FROM orders
        GROUP BY City
        ORDER BY Sales DESC
        LIMIT 10;
    """,

    "19. Highest Profit City": """
        SELECT City,
               ROUND(SUM(Profit), 2) AS Profit
        FROM orders
        GROUP BY City
        ORDER BY Profit DESC
        LIMIT 10;
    """,

    "20. Final Overall KPI": """
        SELECT COUNT(*) AS Rows,
               COUNT(DISTINCT `Order ID`) AS Orders,
               COUNT(DISTINCT `Customer ID`) AS Customers,
               ROUND(SUM(Sales), 2) AS Sales,
               SUM(Quantity) AS Quantity,
               ROUND(SUM(Profit), 2) AS Profit
        FROM orders;
    """
}

if __name__ == "__main__":
    print("Superstore Sales Analysis")
    print(f"Database: {DB_PATH}")

    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"Database not found: {DB_PATH}\n"
            "Make sure superstore.db is inside the project's data folder."
        )

    for title, query in queries.items():
        run_query(title, query)
