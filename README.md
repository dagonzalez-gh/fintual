# Postulación a Fintual
A continuación se presenta una breve explicación del código creado para la postulación al cargo de Desarrollador en Fintual.

## Requerimientos
1. Construct a simple `Portfolio class` that has a `collection of Stocks` and a `"Profit" method` that receives 2 dates and returns the profit of the Portfolio between those dates. 
2. Assume each `Stock` has a `"Price" method` that receives a date and returns its price.
3. Bonus Track: make the Profit method return the "annualized return" of the portfolio between the given dates.

## Solución
Se implementa la clase `Portfolio`, utilizando el lenguaje `Python`, con los siguientes métodos: 

### \_\_init\_\_
Este método es el constructor de la clase, el cual recibe la colección de stocks y los almacena en una lista.

```python
class Portfolio:
    def __init__(self, stocks):
        self.stocks = list(stocks)
    ...
```

### \_\_str\_\_
- El método `__str__` se utilizará para entregar un mensaje más amigable al programador en caso de que este desee conocer el contenido del objeto.

```python
class Portfolio:
    ...
    def __str__(self):
        return f"Portfolio({self.stocks})"
```

### profit
El método `profit`, es el que contiene la lógica principal. Este recibe dos parámetros: `init_date` (fecha de inicio) y `end_date` (fecha de fin), ambas de tipo `string` y en formato `%Y-%m-%d`.

```python
class Portfolio:
    ...
    def profit(self, init_date, end_date):
        ...
    ...
```

Para obtener el profit del portafolio se debe validar que exista, al menos, un objeto stock en la lista.

```python
if len(self.stocks) > 0:
    ...
else:
    raise ValueError("There are no stocks in the portfolio.")
```

A fin de obtener el profit a través del tiempo, se valida que la fecha de fin (`end_date`) sea mayor que la fecha de inicio (`init_date`).

```python
from datetime import datetime
...
date_format = "%Y-%m-%d"
d1 = datetime.strptime(init_date, date_format)
d2 = datetime.strptime(end_date, date_format)

if d1 < d2:
    ...
else:
    raise ValueError("init_date must be minor than end_date.")
```

Se crea un ciclo `for` que recorre la lista de stocks. Por cada iteración se consulta el precio del stock para la fecha de inicio y la fecha de fin, y se van acumulando los datos obtenidos en variables separadas.

La consulta del precio del stock se realiza asumiendo que cada elemento de la lista `self.stocks` corresponde a una instancia de la clase `Stock`, la cual contiene un método `price`, el cual devuelve el precio de dicho stock en base a una fecha.

```python
init_price, end_price = 0, 0

for i in range(len(self.stocks)):
    init_price += self.stocks[i].price(init_date)
    end_price += self.stocks[i].price(end_date)
```

Al fin, el método `profit` retorna la diferencia entre los acumuladores generados previamente.

```python
...
return end_price - init_price
```