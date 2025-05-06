# Prueba para Desarrollador Python Junior

Repositorio con los ejercicios de la prueba. Sigue las instrucciones de la descripción de la prueba.

## Estructura
- `src/`: código de los ejercicios.
- `project/`: mini-proyecto para revisión.
- `requirements.txt`: dependencias generales.
- `README.md`: este archivo.

## Instrucciones generales

1. **Duración total**: 70 min.
2. **Entorno**: Python > 3.10, pip; acceso a internet **solo** para instalar dependencias.
3. **Prohibido**: ten cuidado con usar IA generativas ya que vas a tener que explicar que has hecho en la prueba.
4. **Entrega**: haz fork del repositorio y cuando lo tengas completado envia el link de github a tech@devera.ai

---

## Distribución de tiempo

| Ejercicio                                                         | Tiempo aprox. |
| :---------------------------------------------------------------- | :-----------: |
| **1. Integración con la API de OpenAI**                           |     25 min    |
| **2. Depuración: encontrar 5 bugs en un código**                  |     25 min    |
| **3. Revisión de proyecto: proponer mejoras en el proyecto**      |     20 min    |

---


### 1. Integración con la API de OpenAI (25 min)

* **Objetivo**: consumir un endpoint de OpenAI desde código Python.
* **Tarea**:
  En `src/paraphrase.py`, crea un script que:

  1. Reciba como argumento la ruta a un fichero `input.txt` con texto en español.
  2. Use la libreria de openai usando `gpt-4o-mini` para que rescriba el texto con otras palabras.
  3. Gestione errores.
  4. Imprima la versión parafraseada por consola.
* **Requisitos**:

  * Uso de la librería oficial `openai`: https://pypi.org/project/openai/
  * Documentar en el README cómo ejecutar:

    ```bash
    python src/paraphrase.py input.txt
    ```

---

### 2. Depuración: encontrar 5 bugs en un código (25 min)

* **Objetivo**: evaluar tu capacidad de lectura crítica y corrección.
* **Tarea**:
  En `src/debug5.py` hay este código (no modifiques nombres de funciones):

  1. **Identifica** y **documenta** los 5 bugs o malas prácticas.
  2. Proporciona una versión corregida de `debug5.py`, con comentarios en línea explicando cada corrección.

---

### 3. Revisión de proyecto: proponer mejoras (20 min)

* **Objetivo**: valorar tu criterio de arquitectura, calidad y buenas prácticas.
* **Tarea**:
  En `project/` tienes este mini-proyecto:

  ```
  project/
  ├─ src/
  │  ├ main.py
  │  ├ utils.py
  │  └ api_client.py
  ├─ requirements.txt
  └─ README.md
  ```

  * **`main.py`**: orquesta la lectura de un CSV y envía los datos a un endpoint REST usando `api_client.py`.
  * **`utils.py`**: funciones de limpieza y validación de datos.
  * **`api_client.py`**: clase `ApiClient` con métodos `get_data()` y `post_data(payload)`.
* **Pregunta**:
  Describe **al menos 3 áreas de mejora** (arquitectura, testing, error handling, estilo, rendimiento, etc.) y **cómo** las implementarías paso a paso.

---

## Pauta de corrección (peso global)

| Ejercicio                                      | Peso |
| :--------------------------------------------- | :--: |
| 1. API de OpenAI                               | 40 % |
| 2. Depuración (5 bugs)                         | 30 % |
| 3. Revisión de proyecto y propuestas de mejora | 30 % |

**Criterios generales**:

* Correctitud y robustez.
* Legibilidad y estilo (PEP 8, tipado, docstrings).
* Gestión de errores y casos límite.
* Claridad en la documentación y README.

---