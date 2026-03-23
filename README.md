# gestor_eventos
# 📅 gestor_eventos

## 🧾 Descripción

`gestor_eventos` es una aplicación de escritorio desarrollada en Python con Tkinter que permite registrar, visualizar y eliminar eventos o tareas programadas.

---

## 🎯 Objetivo del proyecto

Desarrollar una aplicación funcional aplicando:

* Programación Orientada a Objetos (POO)
* Interfaces gráficas con Tkinter
* Manejo de eventos
* Organización modular del código

---

## 🛠️ Tecnologías utilizadas

* Python 3.x
* Tkinter
* ttk (Treeview)
---

## 📂 Estructura del proyecto

```bash id="dljtpy"
gestor_eventos/
│
├── main.py              # Archivo principal
├── modelo/              # Clases de datos
│   └── evento.py
├── vista/               # Interfaz gráfica
│   └── interfaz.py
├── controlador/         # Lógica del sistema
│   └── controlador.py
└── utils/               # (Opcional) validaciones
```

---

## ⚙️ Funcionalidades

### ✅ Gestión de eventos

* Agregar eventos con:

  * Fecha (YYYY-MM-DD)
  * Hora (HH:MM)
  * Descripción
* Visualizar eventos en tabla (Treeview)
* Eliminar eventos seleccionados

### ⚠️ Validaciones

* Campos obligatorios
* Formato correcto de hora

---

## 🖥️ Interfaz gráfica

La interfaz está organizada mediante **Frames**:

* 📋 Lista de eventos (Treeview)
* 📝 Entrada de datos (Entry)
* 🎮 Botones de acción

---

## 🧠 Arquitectura (POO)

Se implementa una estructura basada en **MVC (Modelo - Vista - Controlador)**:

* **Modelo (`Evento`)**

  * Representa los datos de cada evento

* **Vista (`Interfaz`)**

  * Maneja la interfaz gráfica

* **Controlador**

  * Gestiona la lógica y la interacción

---

## ▶️ Ejecución

1. Abrir PowerShell o terminal
2. Ir a la carpeta del proyecto:

```bash id="t2u3r8"
cd gestor_eventos
```

3. Ejecutar:

```bash id="3zhf4n"
python main.py
```

---

## 🧪 Ejemplo de uso

1. Ingresar:

   * Fecha: 2026-03-22
   * Hora: 15:00
   * Descripción: Estudiar


## 🚀 Mejoras futuras

* Guardado en Excel o base de datos
* Edición de eventos
* Interfaz moderna (CustomTkinter)
* Notificaciones más avanzadas
* Versión ejecutable (.exe)

---

## 👩‍💻 Autor

MICHELLE TORO
Proyecto académico desarrollado para aplicar conceptos de programación en Python, interfaces gráficas y POO.

---

## 📄 Licencia

Uso educativo
