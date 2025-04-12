import os
import pytest
from pycc.compiler import preprocess, compile, assemble, link, delete_files

@pytest.fixture
def setup_test_environment(tmp_path):
    # Erstelle eine temporäre C-Datei
    source_file = tmp_path / "test.c"
    source_file.write_text("int main() { return 0; }")
    output_file = tmp_path / "test"
    return source_file, output_file

def test_preprocess(setup_test_environment):
    source_file, _ = setup_test_environment
    preprocessed_file = preprocess(str(source_file))
    assert os.path.exists(preprocessed_file)
    assert preprocessed_file.endswith(".i")
    os.remove(preprocessed_file)

def test_compile(setup_test_environment):
    source_file, _ = setup_test_environment
    preprocessed_file = preprocess(str(source_file))
    compiled_file = compile(preprocessed_file)
    assert os.path.exists(compiled_file)
    assert compiled_file.endswith(".s")
    os.remove(preprocessed_file)
    os.remove(compiled_file)

def test_assemble(setup_test_environment):
    source_file, _ = setup_test_environment
    preprocessed_file = preprocess(str(source_file))
    compiled_file = compile(preprocessed_file)
    assembled_file = assemble(compiled_file)
    assert os.path.exists(assembled_file)
    assert assembled_file.endswith(".o")
    delete_files(preprocessed_file, compiled_file, assembled_file)

def test_link(setup_test_environment):
    source_file, output_file = setup_test_environment
    preprocessed_file = preprocess(str(source_file))
    compiled_file = compile(preprocessed_file)
    assembled_file = assemble(compiled_file)
    link(assembled_file, str(output_file))
    assert os.path.exists(output_file)
    delete_files(preprocessed_file, compiled_file, assembled_file, output_file)

def test_delete_files(setup_test_environment):
    source_file, _ = setup_test_environment
    preprocessed_file = preprocess(str(source_file))
    compiled_file = compile(preprocessed_file)
    assembled_file = assemble(compiled_file)
    delete_files(preprocessed_file, compiled_file, assembled_file)
    assert not os.path.exists(preprocessed_file)
    assert not os.path.exists(compiled_file)
    assert not os.path.exists(assembled_file)
