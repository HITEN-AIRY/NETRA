# netra/passive/sources.py

PASSIVE_SOURCES = {
    "crtsh": {
        "description": "Certificate Transparency logs",
        "enabled": True
    },
    "search_engine": {
        "description": "Search engine indexed subdomains",
        "enabled": True
    }
}

'''
This keeps sources:

Centralized

Toggleable

Extensible later (VirusTotal, etc.)

'''