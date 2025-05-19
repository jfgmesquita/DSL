def execute(ast):
    for comand, fields in ast:
        print(f"\n--- Executando {comand} ---")
        for key, value in fields.items():
            print(f"{key} = {value}")
