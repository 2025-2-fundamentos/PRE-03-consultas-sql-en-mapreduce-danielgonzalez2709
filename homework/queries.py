"""Taller evaluable"""

# pylint: disable=broad-exception-raised
# pylint: disable=import-error

import os
import pandas as pd

def run():
    """Orquestador"""
    # Leer el dataset
    df = pd.read_csv('files/input/tips.csv')
    
    # Crear directorios de salida
    for i in range(1, 6):
        query_dir = f'files/query_{i}/'
        os.makedirs(query_dir, exist_ok=True)
        
        # TODO: Implementar cada query específica
        result = f"Query {i} result placeholder"
        
        # Escribir archivos de salida
        with open(f'{query_dir}_SUCCESS', 'w') as f:
            f.write('')
        
        with open(f'{query_dir}part-00000', 'w') as f:
            f.write(result)

if __name__ == "__main__":

    run()
