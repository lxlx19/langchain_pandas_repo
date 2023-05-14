import numpy as np
import pandas as pd

# Criar um dataframe com 10000 linhas
data = pd.DataFrame(
    {
        "icecream_flavor": np.random.choice(
            [
                "chocolate",
                "vanilla",
                "strawberry",
                "pistachio",
                "cookies and cream",
                "mint chocolate chips",
            ], 10000,
        ),
        "icecream_price": np.random.randint(100, 1000, 10000) / 100,
        "icecream_rating": np.random.randint(1, 5, 10000),
        "customer_id": np.random.choice(
            [f"A{str(np.random.randint(1000, 9999))}" for _ in range(10)]
            + [f"B{str(np.random.randint(1000, 9999))}" for _ in range(10)]
            + [f"C{str(np.random.randint(1000, 9999))}" for _ in range(10)]
            + [f"D{str(np.random.randint(1000, 9999))}" for _ in range(10)],
            10000,
        ),
        "shop_city": np.random.choice(
            [
                "São Paulo",
                "Campinas",
                "Barueri",
                "Ribeirão Pires"
            ], 10000,
        ),
    }
)

data.to_csv("icecream.csv", index=False)

