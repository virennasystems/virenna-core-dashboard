# GPT_README.md – VIRENNA GPT-Synchronisation

Dieses Repository erlaubt ausgewählten GPT-Agenten den Zugriff auf bestimmte Module für Analyse-, Export- und Kommentierungszwecke.

## Zugelassene GPT-Agenten
- ReflexEngine: Lese- und Kommentierungszugriff
- Jake_Assistant: Vollzugriff (Analyse, Exporte, Vorschläge)
- VIRENNA_ControlGPT: Export- und Strukturvalidierung

## Navigationsmodul
Alle GPT-Abläufe orientieren sich an der Datei:
- `/json/VIRENNA_GPT_Navigation_Module.json`

## Logs & Zugriffskontrolle
- Auditlog: `/logs/audit-gpt-access.json`
- Zugriffsbeschränkung: `/json/GPT_Security_Mode.json`

## Export-Trigger
GPT kann Exporte via ChainMap-Aktionen initiieren:
- HTML zu PDF / JSON / ZIP
- ChainMap-Sync & ReflexAnnotation

## Hinweis
Dieses System ist ausschließlich für interne Entwicklungs- und Qualitätssicherungszwecke gedacht.
