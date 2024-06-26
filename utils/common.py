import polars as pl


def product_info() -> pl.DataFrame:
    data = [
        {"Code": "F01", "Name": "500g Nut Muesli"},
        {"Code": "F02", "Name": "500g Blueberry Muesli"},
        {"Code": "F03", "Name": "500g Strawberry Muesli"},
        {"Code": "F04", "Name": "500g Raisin Muesli"},
        {"Code": "F05", "Name": "500g Original Muesli"},
        {"Code": "F06", "Name": "500g Mixed Fruit Muesli"},
        {"Code": "F11", "Name": "1kg Nut Muesli"},
        {"Code": "F12", "Name": "1kg Blueberry Muesli"},
        {"Code": "F13", "Name": "1kg Strawberry Muesli"},
        {"Code": "F14", "Name": "1kg Raisin Muesli"},
        {"Code": "F15", "Name": "1kg Original Muesli"},
        {"Code": "F16", "Name": "1kg Mixed Fruit Muesli"},
    ]

    return pl.DataFrame(data)


tables = [
    "BOM_Changes",
    "Carbon_Emissions",
    "Company_Valuation",
    "Financial_Postings",
    "Goods_Movements",
    "Independent_Requirements",
    "Purchase_Orders",
    "Production_Orders",
    "Inventory",
    "Current_Inventory",
    "Current_Inventory_KPI",
    "Current_Suppliers_Prices",
    "Market",
    "Marketing_Expenses",
    "Pricing_Conditions",
    "Production",
    "Current_Game_Rules",
    "Sales",
    "Suppliers_Prices",
    "Stock_Transfers",
]
