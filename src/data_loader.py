import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

def load_all_data(data_dir=None):
    if data_dir is None:
        data_dir = PROJECT_ROOT / 'data' / 'raw'
    else:
        data_dir = Path(data_dir)

    customers = pd.read_csv(data_dir / 'customers.csv')
    orders = pd.read_csv(data_dir / 'orders.csv')
    order_items = pd.read_csv(data_dir / 'order_items.csv')
    products = pd.read_csv(data_dir / 'products.csv')
    return customers, orders, order_items, products