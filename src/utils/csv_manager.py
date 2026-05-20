import pandas as pd
from pathlib import Path

import io
import pandas as pd
from pathlib import Path

def load_csv(directory: Path):
    csv_file = list(directory.glob("*.csv"))
    if not csv_file:
        raise FileNotFoundError(f"No CSV file found in {directory}")
    
    cleaned_lines = []
    with open(csv_file[0], 'r', encoding='utf-8-sig') as f:
        for line in f:
            stripped = line.strip()
            # Falls die Zeile fälschlicherweise komplett in Anführungszeichen eingepackt ist
            if stripped.startswith('"') and stripped.endswith('"'):
                # Entferne die äußeren Anführungszeichen und mache aus "" wieder "
                stripped = stripped[1:-1].replace('""', '"')
            cleaned_lines.append(stripped + '\n')
            
    # Übergibt die bereinigten Zeilen direkt an Pandas
    return pd.read_csv(io.StringIO(''.join(cleaned_lines)), sep=',')
