import pandas as pd

df = pd.DataFrame({
   'Animal': ['Perro', 'Gato', 'Elefante', 'Perro', 'Gato', 'Elefante'],
   'Color': ['Negro', 'Blanco', 'Gris', 'Marrón', 'Negro', 'Marrón'],
   'Cantidad': [2, 3, 1, 4, 2, 2]
})
df

print(df.groupby('Animal').sum(numeric_only=True))

print(df)