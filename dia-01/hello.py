#!/usr/bin/env python3.7
"""
Hello Word Mult Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:
    export LANG=pt_BR essa é do SO nativo
    ou 
    export LANGS_DEMO=pt_BR essa é criada com export

Execução:
    python3 hello.py
    ou
    ./hello.py
"""

__version__ = "0.0.1"
__author__ = "Raphael Ferreira"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANGS_DEMO", "en_US")[:5]

msg = "Hello, World!!!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!!" 
elif current_language == "it_IT":
    msg = "Ciao, Mondo"
elif current_language == "es_SP":
    msg = "Hola, Mondo"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde"

print(msg)