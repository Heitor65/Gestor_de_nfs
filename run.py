import subprocess
import os
import sys
import webbrowser
import time

# ─── Caminhos ────────────────────────────────────────────────────────────────

requirements = os.path.join(
    "requirements.txt"
)

# ─── Início ──────────────────────────────────────────────────────────────────
print("=" * 50)
print("Iniciando...")
print("=" * 50)

# ─── Instala dependências ────────────────────────────────────────────────────
print("\n[1/4] Instalando dependências Python...")

subprocess.run(
    [
        sys.executable,
        "-m",
        "pip",
        "install",
        "-r",
        requirements
    ],
    check=True
)

# ─── Migrations ──────────────────────────────────────────────────────────────
print("\n[2/4] Verificando alterações nos models...")

subprocess.run(
    [
        sys.executable,
        "manage.py",
        "makemigrations"
    ],
    check=True
)

print("\n[3/4] Aplicando migrations...")

subprocess.run(
    [
        sys.executable,
        "manage.py",
        "migrate"
    ],
    check=True
)

# ─── Inicia servidor ─────────────────────────────────────────────────────────
print("\n[4/4] Iniciando servidor Django...")

servidor = subprocess.Popen(
    [
        sys.executable,
        "manage.py",
        "runserver"
    ],
)

# Espera servidor subir
time.sleep(2)

# ─── Abre navegador ──────────────────────────────────────────────────────────
webbrowser.open(
    "http://127.0.0.1:8000/admin/"
)

print("\nAdmin:")
print("http://127.0.0.1:8000/admin/")