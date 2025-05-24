
import json
import sys

def validate_chainmap(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if not isinstance(data, list):
            print("Fehler: Die Datei muss ein Array von Objekten enthalten.")
            return 1

        module_names = set()
        errors = 0

        for i, module in enumerate(data):
            if 'id' not in module or 'name' not in module:
                print(f"Fehlendes Feld in Modul {i}: id oder name fehlt")
                errors += 1
                continue

            if module['name'] in module_names:
                print(f"Doppelter Modulname gefunden: {module['name']}")
                errors += 1
            else:
                module_names.add(module['name'])

        print(f"Validierung abgeschlossen: {len(data)} Module geprüft, {errors} Fehler gefunden.")
        return 0 if errors == 0 else 1

    except json.JSONDecodeError as e:
        print(f"JSON-Fehler: {str(e)}")
        return 1
    except Exception as e:
        print(f"Unerwarteter Fehler: {str(e)}")
        return 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Verwendung: python validate_chainmap.py <pfad_zur_json_datei>")
        sys.exit(1)

    sys.exit(validate_chainmap(sys.argv[1]))
