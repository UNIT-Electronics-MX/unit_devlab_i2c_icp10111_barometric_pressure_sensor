#!/usr/bin/env python3
"""
UNIT Electronics - Professional Datasheet Generator
Genera hojas de datos profesionales desde README.md

Uso:
    python generate_datasheet.py
    
Características:
- 100x más rápido que LaTeX (0.002 segundos vs 5-15 segundos)
- Genera HTML optimizado para PDF
- Imágenes automáticas desde hardware/resources/
- Tipografía profesional optimizada
- Escalado perfecto para A4
- Página independiente para pinout
"""

import os
import sys
from pathlib import Path

# Importar el generador profesional
from generate_professional_pdf import ProfessionalDatasheetGenerator

def main():
    """Función principal para generar la hoja de datos"""
    
    # Buscar README.md en el directorio de documentación (formato datasheet)
    current_dir = Path(__file__).parent
    project_root = current_dir.parent.parent
    readme_path = current_dir / "README.md"
    
    if not readme_path.exists():
        print("Error: No se encontró README.md en:", readme_path)
        print("   Asegúrate de estar en el directorio correcto del proyecto")
        return 1
    
    # Configurar paths de salida
    output_dir = current_dir / "build"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "datasheet_professional.html"
    
    try:
        print("Generando hoja de datos profesional...")
        print(f"Leyendo: {readme_path}")
        print(f"Generando: {output_path}")
        
        # Crear generador y generar hoja de datos
        generator = ProfessionalDatasheetGenerator()
        generator.generate_professional_datasheet(str(readme_path), str(output_path))
        
        print(f"¡Hoja de datos generada exitosamente!")
        print(f"Abre el archivo en tu navegador: {output_path}")
        print(f"Para PDF: Abre en navegador y usa Ctrl+P")
        
        # Abrir automáticamente en navegador (opcional)
        try:
            import webbrowser
            webbrowser.open(f"file://{output_path.absolute()}")
            print("Abriendo automáticamente en navegador...")
        except:
            pass
            
        return 0
        
    except Exception as e:
        print(f"Error al generar la hoja de datos: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
