# Bot Consulta RUNT

Bot desarrollado en **Python** para automatizar la consulta de información de vehículos en el portal público del **RUNT** y procesar los resultados.

El sistema realiza consultas automáticas por **placa y documento**, resuelve **captcha**, extrae la información del portal y envía los datos a:

* **SQL Server**
* **API externa**

---

# Funcionalidades

* Consulta automática de vehículos en el portal del RUNT
* Resolución automática de captcha mediante **AntiCaptcha**
* Extracción de:

  * Información general del vehículo
  * SOAT
  * Revisión Técnico Mecánica (RTM)
* Registro de resultados en **SQL Server**
* Envío de resultados a **API externa**
* Sistema de logs de ejecución
* Compilación a **ejecutable (.exe)**

---

# Tecnologías utilizadas

* Python 3.11
* Selenium
* Pandas
* PyODBC
* WebDriver Manager
* PyInstaller

---

# Estructura del proyecto

```
ScrapingRunt
│
│   main.py                # Script principal que ejecuta todo el flujo
│   config.json            # Archivo de configuración del sistema
│
├── captcha
│   resolver_captcha.py    # Resolución del captcha usando AntiCaptcha
│
├── config
│   settings.py            # Carga de configuración desde config.json
│
├── db
│   obtener_consultas_db.py    # Obtiene las placas a consultar
│   guardar_resultado_db.py    # Guarda resultados en SQL Server
│   obtener_codigo_vehiculo.py
│
├── driver
│   crear_driver.py        # Inicialización del navegador Selenium
│
├── extract
│   extraer_info_general.py
│   extraer_soat.py
│   extraer_rtm.py
│   extraer_tabla_mat.py
│   _normalizar_rtm.py
│
├── helpers
│   click.py
│   escribir.py
│   seleccionar_mat_option.py
│
├── panels
│   expandir_todos_los_paneles.py
│
├── request
│   criterio_api.py        # Envío de información a API
│   entidad_api.py
│
├── services
│   consultar.py           # Flujo completo de consulta en el portal
│
└── funtions
    log_resultado.py       # Registro de logs del proceso
    convertir_fecha.py
```

---

# Flujo del proceso

1. Se obtienen las consultas pendientes desde **SQL Server**
2. Se abre el portal del RUNT con **Selenium**
3. Se diligencian:

   * placa
   * tipo de documento
   * número de documento
4. Se resuelve el **captcha**
5. Se envía la consulta
6. Se extrae la información:

   * Información general
   * SOAT
   * RTM
7. Se guardan los resultados en:

   * Base de datos
   * API externa
8. Se registra el resultado en logs

---

# Archivo de configuración

El sistema utiliza un archivo **config.json** que permite cambiar configuraciones sin recompilar el ejecutable.

Ejemplo:

```
{
  "ANTICAPTCHA_KEY": "API_KEY_AQUI",

  "TIPO_DOC": "Cédula Ciudadanía",
  "INTERFACE": 1530,

  "URL": "https://portalpublico.runt.gov.co/#/consulta-vehiculo/consulta/consulta-ciudadana",
  "URL2": "http://api.crmgrupoge.com/v3/conectoresimportar",

  "DB_CONFIG": {
    "DRIVER": "{ODBC Driver 17 for SQL Server}",
    "SERVER": "ZEUS",
    "DATABASE": "Integraciones",
    "UID": "usuario",
    "PWD": "password"
  },

  "HEADERS": {
    "conniKey": "API_KEY",
    "conniToken": "TOKEN",
    "Content-Type": "application/json"
  }
}
```

---

# Instalación

Clonar el repositorio:

```
git clone https://github.com/usuario/bot-runt.git
cd bot-runt
```

Instalar dependencias:

```
pip install -r requirements.txt
```

---

# Compilar ejecutable

Para generar el ejecutable:

```
pyinstaller --onefile --clean --collect-all selenium --collect-all webdriver_manager --collect-all pandas main.py
```

El ejecutable se generará en:

```
dist/main.exe
```

---

# Ejecutar el bot

```
main.exe
```

El bot:

* consultará las placas pendientes
* extraerá la información
* guardará los resultados en base de datos
* enviará los datos a la API

---

# Uso en otros equipos

Para ejecutar en otro computador solo se necesita:

```
main.exe
config.json
```

Opcional:

```
logs/
```

---

# Logs

El sistema genera logs de ejecución para cada proceso.

Ejemplo:

```
logs/runt_log_YYYYMMDD.txt
```

---

# Requisitos del sistema

* Windows
* Google Chrome instalado
* ODBC Driver 17 for SQL Server
* Conexión a internet

---

# Autor

Proyecto desarrollado por **Santiago Alzate**.
