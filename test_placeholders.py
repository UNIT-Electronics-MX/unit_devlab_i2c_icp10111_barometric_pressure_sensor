#!/usr/bin/env python3
"""
Test script para verificar el sistema de placeholders
"""
import os
import sys
import tempfile

# Agregar el directorio de documentación al path
sys.path.insert(0, 'software/documentation')

from generate_professional_pdf import ProfessionalDatasheetGenerator

def test_placeholder_system():
    print("🧪 Iniciando test del sistema de placeholders")
    
    # Crear contenido de test con placeholder
    test_content = """# Test Hardware README

## Schematics
<a href="{{SCHEMATIC_PDF}}">Ver esquemático</a>

## Description
Este es un test del sistema de placeholders.
"""
    
    # Crear archivo temporal
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as temp_file:
        temp_file.write(test_content)
        temp_path = temp_file.name
    
    try:
        # Crear instancia del generador
        generator = ProfessionalDatasheetGenerator()
        
        # Procesar placeholders
        processed_content = generator.process_hardware_readme_placeholders(temp_path)
        
        print("\n📝 Contenido original:")
        print(test_content)
        
        print("\n🔄 Contenido procesado:")
        print(processed_content)
        
        # Verificar que el placeholder fue reemplazado
        if "{{SCHEMATIC_PDF}}" not in processed_content:
            print("\n✅ Placeholder reemplazado correctamente")
            return True
        else:
            print("\n❌ Placeholder no fue reemplazado")
            return False
            
    finally:
        # Limpiar archivo temporal
        os.unlink(temp_path)

def test_schematic_detection():
    print("\n🔍 Test de detección de esquemáticos")
    
    generator = PDFGenerator()
    
    # Test con la ruta real del hardware README
    hardware_readme = "hardware/README.md"
    
    if os.path.exists(hardware_readme):
        schematic = generator.find_schematic_pdf(hardware_readme)
        print(f"📄 Esquemático detectado: {schematic}")
        
        if schematic and schematic.startswith('unit_sch') and schematic.endswith('.pdf'):
            print("✅ Detección de esquemático funciona correctamente")
            return True
        else:
            print("❌ No se detectó correctamente el esquemático")
            return False
    else:
        print("⚠️ No se encontró hardware README para el test")
        return False

if __name__ == "__main__":
    print("🚀 Sistema de Test de Placeholders")
    print("=" * 50)
    
    test1 = test_placeholder_system()
    test2 = test_schematic_detection()
    
    print("\n" + "=" * 50)
    if test1 and test2:
        print("✅ Todos los tests pasaron correctamente")
        print("🎯 El sistema de placeholders está funcionando")
    else:
        print("❌ Algunos tests fallaron")
        
    print("\n📊 Resumen:")
    print(f"   📝 Procesamiento de placeholders: {'✅' if test1 else '❌'}")
    print(f"   🔍 Detección de esquemáticos: {'✅' if test2 else '❌'}")
