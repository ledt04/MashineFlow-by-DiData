def sample_classifier(csv_names, didata_names):

    # 1. Build the lookup map
    lookup = {
        samp['sample_id']: st['state_id'] 
        for st in didata_names['states'] 
        for samp in st['samples']
    }

    # 2. Collect all unique state IDs found for the provided names
    # Using set comprehension for speed and automatic uniqueness
    found_state_ids = {lookup[name] for name in csv_names if name in lookup}

    # 3. Validation Logic
    if len(found_state_ids) == 1:
        # Exactly one state ID was found for all matching samples
        return found_state_ids.pop()
    
    # Returns None if:
    # - No samples were found (len == 0)
    # - Samples are split across different states (len > 1)
    return None

def switch_name_with_id(sample_peaks, didata_data):
    """
    Ersetzt die Namen (Strings) in sample_peaks direkt mit den entsprechenden 
    IDs aus den DiData-States, da die Namen exakt übereinstimmen.
    """
    # 1. Schritt: Erstelle ein flaches Nachschlage-Verzeichnis (Name -> ID) aus der DiData-Struktur
    name_to_id = {}
    
    for state in didata_data.get('states', []):
        for sample in state.get('samples', []):
            sample_name = sample.get('sample_id')
            entity_id = sample.get('id')
            if sample_name and entity_id:
                name_to_id[sample_name] = entity_id

    # 2. Schritt: Neues Dictionary mit IDs statt Namen aufbauen
    switched_sample_peaks = {}
    
    for csv_sample_name, peaks in sample_peaks.items():
        if csv_sample_name in name_to_id:
            target_id = name_to_id[csv_sample_name]
            switched_sample_peaks[target_id] = peaks
        else:
            # BLANK und LADDER landen automatisch hier, wenn sie nicht in DiData existieren
            print(f"[INFO] CSV-Probe '{csv_sample_name}' wurde in DiData nicht gefunden und wird übersprungen.")
            
    return switched_sample_peaks