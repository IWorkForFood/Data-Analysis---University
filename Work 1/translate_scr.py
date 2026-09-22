import sqlite3
import pandas as pd

# Подключение к базе SQLite
conn = sqlite3.connect('resources.db')

# Список таблиц для экспорта
tables = ['product_groups', 'products', 'departments', 'sales']

for table in tables:
    # Чтение данных из SQLite
    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    
    # Заменяем точку на запятую ТОЛЬКО в столбцах типа float (вещественные числа)
    float_cols = df.select_dtypes(include=['float', 'float64']).columns
    for col in float_cols:
        # Преобразуем число в строку с заменой точки на запятую
        df[col] = df[col].apply(lambda x: f"{x}".replace('.', ',') if pd.notnull(x) else '')
    
    # Сохраняем в CSV (кодировка cp1251 / windows-1251 для русской Windows и Excel)
    df.to_csv(f"{table}.csv", index=False, sep=';', encoding='cp1251')

conn.close()

print("Экспорт таблиц в CSV успешно завершён!")