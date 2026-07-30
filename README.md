# Laboratorio Pytest — Sesión 1

Proyecto listo para abrir en VS Code y trabajar la guía "Actividades Sesión 1 - Módulo II".
Yeimy Alejandra padilla gutierrez 

## 1. Preparar el entorno

Abre una terminal en la carpeta raíz del proyecto (`laboratorio-descubrimiento/`) y ejecuta:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

## 2. Actividad 1.1 — Descubrimiento de pruebas

Los archivos ya están creados tal como los pide la guía (sin corregir):

- `tests/test_operations.py`
- `tests/operations_test.py`
- `tests/pruebas_matematicas.py`  ← nombre y función que Pytest NO reconoce

Ejecuta:

```bash
python -m pytest -v
```

Verás que solo se recolectan 2 pruebas. Cuando la guía lo indique, renombra tú mismo (siguiendo el
paso 4 del procedimiento):

- `tests/pruebas_matematicas.py` → `tests/test_matematicas.py`
- función `comprobar_multiplicacion()` → `test_multiply_two_numbers()`

Vuelve a ejecutar `python -m pytest -v` y compara el resultado (deberían collectarse 3 pruebas).

Ejecuciones selectivas:

```bash
python -m pytest tests/test_operations.py::test_add_two_positive_numbers -v
python -m pytest -k "multiply" -v
```

## 3. Actividad 1.2 — Arrange-Act-Assert

`app/invoice.py` contiene las funciones de facturación.
`tests/test_invoice.py` ya trae las 3 pruebas resueltas con Arrange-Act-Assert, como referencia.

Si quieres practicar el ejercicio desde cero, borra el contenido de `test_invoice.py` y escríbelo
tú mismo siguiendo el "Procedimiento orientado" de la guía; usa este archivo solo para comparar al final.

Para el fallo controlado (paso 6): cambia temporalmente un valor esperado (por ejemplo, en
`test_calculate_tax_returns_percentage_of_subtotal` cambia `19000` por `19500`), ejecuta:

```bash
python -m pytest tests/test_invoice.py -v
```

observa el `FAILED` y el mensaje `assert ... == ...`, y luego restaura el valor correcto.

## Estructura

```
laboratorio-descubrimiento/
├── app/
│   ├── __init__.py
│   ├── operations.py
│   └── invoice.py
├── tests/
│   ├── test_operations.py
│   ├── operations_test.py
│   ├── pruebas_matematicas.py
│   └── test_invoice.py
├── pytest.ini
├── requirements.txt
└── README.md
```
