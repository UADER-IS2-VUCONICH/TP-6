import json, sys
def print_help():
    help_message = """
    Extractor de token para acceso API Servicios Banco XXX (versión 1.0)
    
    Uso:
        getJason.py <path archivo JSON> [clave]
    
    Ejemplo:
        python getJason.py ./sitedata.json token1
    
    Si no se especifica una clave, se usará "token1" por defecto.
    """
    print(help_message)

def get_token_from_json(json_path, key='token1'):
    try:
        with open(json_path, 'r') as file:
            data = json.load(file)
            if key in data:
                print(f"{data[key]}")
            else:
                print(f"Error: La clave ingresada no fue encontrada en el archivo JSON.")
    except FileNotFoundError:
        print(f"Error: El archivo no se encuentra.")
    except json.JSONDecodeError:
        print(f"Error: El archivo no es un JSON válido.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
    elif sys.argv[1] == '-h':
        print_help()
    else:
        json_path = sys.argv[1]
        key = sys.argv[2] if len(sys.argv) > 2 else 'token1'
        get_token_from_json(json_path, key)
