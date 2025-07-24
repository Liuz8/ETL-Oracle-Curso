# 📊 Análisis de Evasión de Clientes (Churn Analysis)

Este proyecto tiene como objetivo analizar los factores que influyen en la **evasión de clientes** de una empresa de servicios. A través del análisis de datos, se busca identificar patrones y variables que estén relacionadas con la cancelación del servicio por parte de los clientes, para proponer estrategias que ayuden a reducir la pérdida de usuarios.

---

## 🧠 Objetivo del Proyecto

- Identificar variables numéricas clave que influyen en la evasión de clientes.
- Analizar diferencias de comportamiento entre clientes que cancelaron el servicio y los que permanecen activos.
- Generar visualizaciones que respalden los hallazgos.
- Proponer recomendaciones basadas en datos para mejorar la retención de clientes.

---

## 📁 Estructura del Proyecto

- `notebook.ipynb`: Contiene todo el análisis paso a paso, desde la carga de datos hasta las conclusiones.
- `churn_data.csv`: Dataset utilizado en el análisis (no incluido aquí por privacidad).
- `README.md`: Descripción general del proyecto.

---

## 🧼 Limpieza y Tratamiento de Datos

- Se cargaron los datos y se revisaron los tipos de variables.
- No se detectaron valores nulos en las variables numéricas analizadas.
- Se transformó la variable `Churn` (Sí/No) en una versión binaria para facilitar análisis estadísticos.

---

## 📊 Variables Analizadas

Se enfocó el análisis en las siguientes variables numéricas:

- `customer_tenure`: Tiempo que el cliente ha estado con la empresa.
- `account_Charges_Monthly`: Cargo mensual por el servicio.
- `account_Charges_Total`: Cargo total acumulado.
- `estimated_daily_charge`: Estimación del cargo diario promedio.

---

## 📈 Análisis Exploratorio de Datos

Se realizaron análisis comparativos mediante **boxplots** y estadísticas agrupadas para observar cómo se distribuyen las variables numéricas según si el cliente canceló o no.

Se observó, por ejemplo:

- Los clientes que evaden tienden a tener menor tiempo de contrato.
- Ciertos cargos mensuales más altos están más asociados a cancelación.
- El cargo diario promedio tiende a ser más bajo entre clientes que se van.

---

## 🧩 Conclusiones

- La variable más fuertemente relacionada con la evasión es `customer_tenure`.
- Los clientes con menor antigüedad presentan mayor probabilidad de cancelar.
- No hay una relación directa entre mayor gasto y menor evasión: algunos clientes con cargos elevados también cancelan.

---

## 💡 Recomendaciones

- Implementar estrategias de retención para nuevos clientes (primeros meses).
- Ofrecer beneficios o descuentos progresivos con el tiempo.
- Analizar más a fondo a los clientes con cargos bajos, ya que podrían sentirse menos comprometidos o satisfechos.

---

## 🚀 Herramientas Utilizadas

- Python
- Pandas
- Seaborn
- Matplotlib
- Jupyter Notebook

---

## ✅ Autor

Luis Ángel Martínez Franco  
Estudiante/Data Analyst  

---

## 📬 Contacto

Para consultas o sugerencias, no dudes en escribirme.

