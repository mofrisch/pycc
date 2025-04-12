import os
import pytest
from pycc import preprocess  # Importiere die preprocess-Funktion

@pytest.fixture
def setup_test_environment(tmp_path):
    # Erstelle eine temporäre C-Datei
    source_file = tmp_path / "test.c"
    source_file.write_text("int main() { return 0; }")
    output_file = tmp_path / "test"
    return source_file, output_file

def test_preprocess_output_matches_example():
    # Pfad zur example.i Datei
    example_file_path = os.path.join(os.path.dirname(__file__), "../../example.i")
    
    # Lese den Inhalt der example.i Datei
    with open(example_file_path, 'r') as file:
        expected_content = file.read()
    
    # Rufe preprocess() auf und vergleiche die Ergebnisse
    result = preprocess()
    assert result == expected_content, "Das Ergebnis von preprocess() stimmt nicht mit example.i überein."
