import os
import time
from datetime import datetime

# Pobierz nazwę testu z argumentu lub ustaw domyślną
test_file = "testy/test_zaawansowane_interakcje.py"  # Domyślny plik
if len(os.sys.argv) > 1:
    test_file = os.sys.argv[1]

# Wygeneruj nazwę raportu z datą i nazwą testu
report_name = f"raport_{os.path.basename(test_file).replace('.py', '')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
os.system(f"pytest {test_file} --headed --slowmo 500 --html={report_name} --self-contained-html")
print(f"Raport wygenerowany: {report_name}")