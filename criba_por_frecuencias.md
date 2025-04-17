## Criba por Frecuencias: Modelo de Análisis de Primalidad

### Introducción

Este documento presenta una propuesta de modelo alternativo para el análisis de primalidad, basado en la cancelación de compuestos mediante "frecuencias" generadas a partir de números primos base. El modelo evita la factorización directa y se fundamenta en patrones cíclicos asociados a números de la forma \( 6N \pm 1 \), los únicos candidatos a primos mayores que 3.

Este modelo fue desarrollado por observación empírica y validación con herramientas computacionales. Se pretende que esta formulación tenga un lenguaje formal y técnico, de utilidad para su futura evaluación académica.

---

### I. Fundamento Teórico

#### 1. Números candidatos a primos

Todo número primo mayor que 3 se puede expresar como \( 6N \pm 1 \). A estos les llamaremos **números base** o **potenciales primos**.

\[ \text{Base general: } p = 6N - 1 \quad \text{o} \quad p = 6N + 1 \]

Estos números se disponen en una lista de forma creciente, y se les asocia una posición relativa en la sucesión (por ejemplo, la posición 1, 2, 3... según su aparición como número de la forma \( 6N \pm 1 \)).

#### 2. Frecuencias

Para cada número primo conocido, se generan dos columnas de frecuencias, denominadas aquí **frecuencia 1** y **frecuencia 2**. Estas representan valores que, al ser sumados iterativamente con múltiplos de un ciclo, generan un patrón periódico que elimina compuestos.

**Frecuencia 1**:
Se genera sumando el ciclo \( C \) a un valor inicial asociado al primo base. Por ejemplo:

\[ f_1 = a + kC \]

**Frecuencia 2**:
De forma complementaria, se generan dos valores cercanos al primo base mediante:

\[ f_2^- = C - 1, \quad f_2^+ = C + 1 \]

Luego se aplica:

\[ f_2 = f_2^-, f_2^+ + mC \]

En la práctica, se usan los múltiplos de 4 para generar estos pares. El patrón se repite con cada nuevo número base.

#### 3. Cancelación por frecuencias

Cada frecuencia actúa como un "rastro" que pisa y elimina posiciones de la lista. Si una frecuencia incide sobre un número candidato a primo, se considera **compuesto**. Basta una colisión para invalidar la primalidad.

Esta idea se deriva de una observación visual en la que se evidencian patrones que se reinician cíclicamente al alcanzar productos como \( 5 \times 7 \times 11 \times \ldots \).

#### 4. Rango de aplicación

Las frecuencias generadas para cada primo base \( p \) solo se aplican desde \( p+1 \) hasta \( p^2 \). Este rango asegura que no haya interferencia entre patrones futuros ni cancelaciones prematuras.

---

### II. Método de Evaluación

Para determinar si un número \( n \) es primo, se aplica el siguiente procedimiento:

1. Verificar si \( n \) es de la forma \( 6N \pm 1 \).
2. Generar todas las frecuencias correspondientes a los primos menores que \( \sqrt{n} \).
3. Aplicar las frecuencias como pasos iterativos y observar si alguna colisiona con \( n \).
4. Si existe al menos una colisión, el número es **compuesto**. Si ninguna frecuencia pisa \( n \), se considera **primo**.

Esta técnica puede expresarse computacionalmente como un sistema de predicción mediante **offsets**. Un offset determina cuántas veces una frecuencia determinada alcanzaría un número objetivo:

\[ \text{offset} = \frac{n - f}{C} \]

Si el resultado es entero, implica que la frecuencia pisa el número y, por tanto, es compuesto.

---

### III. Conclusión

La criba por frecuencias permite un análisis de primalidad alternativo, sin recurrir a divisiones ni factorizaciones. Aunque su origen fue experimental, los resultados empíricos coinciden con la criba de Eratóstenes. La predicción por offsets ofrece una ventaja computacional y puede automatizarse de forma eficiente.

Este documento excluye referencias al desarrollo histórico en hojas de cálculo y se enfoca en la formulación matemática y teórica del modelo.

---

### Futuro trabajo

- Formalización matemática rigurosa.
- Comparación de eficiencia con métodos clásicos.
- Exploración de propiedades emergentes en patrones de frecuencias.

---

**Autor**: Héctor Cárdenas Campos

**Licencia**: Creative Commons Attribution-NonCommercial (CC BY-NC)
