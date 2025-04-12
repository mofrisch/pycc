import subprocess
import os
import time

def gcc_step(command, description):
    subprocess.run(command, check=True)
    print(f"{description}")

def preprocess(source_file):
    preprocessed_file = source_file.replace(".c",".i")
    gcc_step(["gcc", "-E", source_file, "-o", preprocessed_file], f"Preprocessed file: {preprocessed_file}")
    return preprocessed_file

def compile(preprocessed_file):
    compiled_file = preprocessed_file.replace(".i", ".s")
    gcc_step(["gcc", "-S", preprocessed_file, "-o", compiled_file], f"Compiled file: {compiled_file}")
    return compiled_file

def assemble(compiled_file):
    assembled_file = compiled_file.replace(".s", ".o")
    gcc_step(["gcc", "-c", compiled_file, "-o", assembled_file], f"Assembled file: {assembled_file}")
    return assembled_file

def link(assembled_file, output_file):
    gcc_step(["gcc", assembled_file, "-o", output_file], f"Executable file: {output_file}")

def delete_files(*files):
    for file in files:
        if os.path.exists(file):
            os.remove(file)
            print(f"Deleted file: {file}")

def run_gcc_steps(source_file, output_file):
    # Wechsel in das Unterverzeichnis 'c_examples'
    original_dir = os.getcwd()
    try:
        os.chdir("c_examples")
        if os.getcwd() != os.path.join(original_dir, "c_examples"):
            print("Error: Failed to change directory to 'c_examples'.")
            return
        
        # Schritte ausführen
        preprocessed_file = preprocess(source_file)
        compiled_file = compile(preprocessed_file)
        assembled_file = assemble(compiled_file)
        link(assembled_file, output_file)
        
        # Überprüfen, ob das Ergebnis neuer als die Quelle ist
        if os.path.getmtime(output_file) <= os.path.getmtime(source_file):
            print("Error: The output file is not newer than the source file.")
            return
        
        # Temporäre Dateien löschen
        delete_files(preprocessed_file, compiled_file, assembled_file)
    finally:
        os.chdir(original_dir)

def run_gcc_no_remove(source_file, output_file):
    # Wechsel in das Unterverzeichnis 'c_examples'
    original_dir = os.getcwd()
    try:
        os.chdir("c_examples")
        if os.getcwd() != os.path.join(original_dir, "c_examples"):
            print("Error: Failed to change directory to 'c_examples'.")
            return
        
        # Schritte ausführen
        preprocessed_file = preprocess(source_file)
        compiled_file = compile(preprocessed_file)
        assembled_file = assemble(compiled_file)
        link(assembled_file, output_file)
        
        # Überprüfen, ob das Ergebnis neuer als die Quelle ist
        if os.path.getmtime(output_file) <= os.path.getmtime(source_file):
            print("Error: The output file is not newer than the source file.")
            return
    finally:
        os.chdir(original_dir)

# Beispielaufruf
run_gcc_no_remove("example.c", "example")
# run_gcc_steps("example.c", "example")
