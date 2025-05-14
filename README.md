# InsecureCodeLab

Laboratorios prácticos para realizar Secure Code Review en Python. Este proyecto explora no solo vulnerabilidades comunes del OWASP Top Ten, sino también muchas otras que no se incluyen en este TOP. Todo esto, mediante aplicaciones diseñadas intencionalmente inseguras. Cada código vulnerable incluye una solución propuesta, pero se recomienda que primero intentes desarrollar tu propia remediación antes de revisar las soluciones proporcionadas. Recuerda, no hay un único camino para mitigar estas vulnerabilidades; existen múltiples enfoques para resolver cada problema.

---

## Requisitos:

- Python 3.10 o superior
- Virtualenv (opcional, pero recomendado)
- Flask

---

## Instalación:

```bash
git clone https://github.com/medicenr4z0r/InsecureCodeLab.git

cd InsecureCodeLab

python3 -m venv venv

source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

pip install -r requirements.txt
```
---
## Cómo ejecutar los laboratorios:
Cada laboratorio está desarrollado en un archivo independiente. Para ejecutar un laboratorio específico, simplemente corre el archivo correspondiente. Por ejemplo:

```bash
python3 sqli.py
```
---
## Objetivo

- Identificar vulnerabilidades en aplicaciones.
- Comprender cómo funcionan las vulnerabilidades.
- Aprender a mitigar y corregir cada vulnerabilidad.
---

## Advertencia

Este proyecto es únicamente para fines educativos y no debe ser utilizado en entornos de producción o sistemas no autorizados.

---

### Aporta o aparta

Tu apoyo sería un gran favor a la comunidad, estamos acá para dejar un mundo mejor, acuérdate de tu yo de hace 5 años, siempre podemos ayudar a los demás, stay hack.

Con amor ~ R4z0r.
