#  Laboratorio Pytest — Sesión 1

> **Módulo II:** Actividades de Descubrimiento de Pruebas y Patrón Arrange-Act-Assert (AAA)  
> **Estudiante / Autora:** Yeimy Alejandra Padilla Gutiérrez  
> **Proyecto:** `laboratorio-descubrimiento`

---

##  Descripción General

Este proyecto contiene la estructura base para desarrollar las actividades prácticas correspondientes a la **Sesión 1 (Módulo II)**. El objetivo principal es comprender cómo **Pytest** descubre de forma automática las pruebas unitarias y cómo aplicar el patrón **Arrange-Act-Assert (AAA)** en funciones de facturación.

---

##  1. Preparación del Entorno

Abre una terminal en la raíz del proyecto (`laboratorio-descubrimiento/`) y sigue estos pasos:

### 1.1 Crear y activar el entorno virtual

* **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
macOS / Linux:

Bash
python -m venv venv
source venv/bin/activate
1.2 Instalar dependencias
Bash
pip install -r requirements.txt
2. Actividad 1.1 — Descubrimiento de Pruebas (Test Discovery)
Al iniciar, el directorio contiene archivos creados tal como los solicita la guía (sin corregir):

tests/test_operations.py

tests/operations_test.py

tests/pruebas_matematicas.py (Nombre y función que Pytest no reconoce inicialmente)

Pasos a ejecutar:
Primera recolección:

Bash
python -m pytest -v
Observación: Notarás que solo se recolectan 2 pruebas.

Renombrar archivos y funciones (Paso 4 del procedimiento):

Renombra: tests/pruebas_matematicas.py ➔ tests/test_matematicas.py

Renombra la función interna: comprobar_multiplicacion() ➔ test_multiply_two_numbers()

Verificación:

Bash
python -m pytest -v
Resultado esperado: Ahora Pytest recolectará 3 pruebas.

Ejecuciones selectivas:

Por ruta específica:

Bash
python -m pytest tests/test_operations.py::test_add_two_positive_numbers -v
Por coincidencia de nombre (-k):

Bash
python -m pytest -k "multiply" -v
 3. Actividad 1.2 — Patrón Arrange-Act-Assert (AAA)
Código fuente: app/invoice.py (Funciones de facturación)

Pruebas: tests/test_invoice.py (Contiene las 3 pruebas resueltas bajo el patrón AAA)
 Sugerencia de práctica:

Si deseas resolver el ejercicio desde cero, borra el contenido de tests/test_invoice.py y escríbelo tú misma siguiendo la guía. Utiliza la versión original únicamente como referencia final.

Simulación de Fallo Controlado (Paso 6):
Modifica temporalmente un valor esperado en tests/test_invoice.py.

Ejemplo: En test_calculate_tax_returns_percentage_of_subtotal, cambia 19000 por 19500.

Ejecuta la prueba:

Bash
python -m pytest tests/test_invoice.py -v
Observa la salida FAILED, analiza la diferencia mostrada por assert ... == ... y restaura el valor correcto.

 Estructura del Proyecto
Plaintext
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