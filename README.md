# Proyecto Python - Puesta en Producción Segura

## Descripción General

Este proyecto corresponde a la práctica de Puesta en Producción Segura (PPS), orientada a la implantación de mecanismos de seguridad dentro del ciclo de vida del software siguiendo principios DevSecOps.

El objetivo principal es aplicar controles de seguridad sobre un proyecto Python utilizando herramientas de control de versiones, automatización y validación de integridad antes del despliegue a producción.

---

## Tecnologías Utilizadas

| Tecnología | Versión | Descripción |
|---|---|---|
| Python | 3.x | Lenguaje principal del proyecto |
| Git | 2.x | Control de versiones distribuido |
| GitHub | Cloud | Repositorio remoto y CI/CD |
| Gitleaks | Última estable | Detección de secretos expuestos |
| Git Hooks | Nativo Git | Automatización de controles locales |
| GitHub Actions | CI/CD | Automatización de análisis de seguridad |

---

## Guía de Despliegue

### 1. Clonar repositorio

```bash
git clone https://github.com/USUARIO/REPOSITORIO.git
```

### 2. Acceder al directorio

```bash
cd ProyectoPython
```

### 3. Crear entorno virtual

```bash
python3 -m venv .venv
```

### 4. Activar entorno virtual

Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 6. Ejecutar aplicación

```bash
python3 main.py
```

---

## Tabla de Trazabilidad

| Versión | Fecha | Descripción |
|---|---|---|
| v1.0 | 13/05/2026 | Inicialización del repositorio Git |
| v1.1 | 13/05/2026 | Creación de rama desarrollo-seguro |
| v1.2 | 13/05/2026 | Configuración inicial de seguridad |
| v1.3 | 13/05/2026 | Integración mediante merge Fast-forward |

---

## Checklist de Seguridad

### Archivos y directorios protegidos mediante `.gitignore`

| Elemento | Motivo de protección |
|---|---|
| `*.log` | Evitar exposición de logs y datos de depuración |
| `.venv/` | Impedir subida del entorno virtual local |
| `__pycache__/` | Evitar archivos temporales compilados |
| `*.sqlite3` | Proteger bases de datos locales |
| `secrets.env` | Evitar fuga de credenciales o secretos |
| `.env` | Proteger variables sensibles de entorno |

---

## Medidas DevSecOps Implementadas

- Uso de ramas separadas para desarrollo seguro.
- Integración controlada mediante merge.
- Configuración de Git Hooks.
- Escaneo automático de secretos con Gitleaks.
- Automatización CI/CD mediante GitHub Actions.
- Aplicación del principio de menor privilegio.

---

## Autor: Antonio José Fernández López

Proyecto desarrollado para Alan Turing con fines académicos (PPS).
