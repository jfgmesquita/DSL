memory = {}
definitions = {}

def execute(ast):
    for entry in ast:
        if entry[0] == 'assign':
            _, varname, value = entry
            memory[varname] = value
            print(f"[assign] {varname} = {value}")

        elif entry[0] == 'call':
            _, funcname = entry
            if funcname in definitions:
                print(f"[call] {funcname}()")
                for key, value in definitions[funcname].items():
                    print(f"{key} = {value}")
            else:
                print(f"[call] Erro: funcao '{funcname}' nao definida")

        elif entry[0] == 'def':
            _, name, body = entry
            definitions[name] = body
            print(f"[def] Funcao '{name}' registada")

        elif entry[0] == 'if':
            _, expr, then_block, else_block = entry
            result = eval_expression(expr)
            branch = then_block if result else else_block
            print(f"[if] Condicao {'verdadeira' if result else 'falsa'} → executa bloco")
            execute(branch)

        else:
            comand, fields = entry
            print(f"\n--- Executando {comand} ---")
            if isinstance(fields, dict):
                for key, value in fields.items():
                    print(f"{key} = {value}")
            elif isinstance(fields, list):
                for subcomand, subfields in fields:
                    print(f"\n[batch] Executando {subcomand}:")
                    for key, value in subfields.items():
                        print(f"{key} = {value}")
            else:
                print(f"[Erro] Formato inesperado: {type(fields)}")

def eval_expression(expr):
    if isinstance(expr, tuple):
        op = expr[0]
        if op in ('==', '!=', '<', '>'):
            a = resolve(expr[1])
            b = resolve(expr[2])
            if op == '==': return a == b
            if op == '!=': return a != b
            if op == '<':  return a < b
            if op == '>':  return a > b
        elif op == 'and':
            return eval_expression(expr[1]) and eval_expression(expr[2])
        elif op == 'or':
            return eval_expression(expr[1]) or eval_expression(expr[2])
        elif op == 'not':
            return not eval_expression(expr[1])
    return resolve(expr)

def resolve(val):
    if isinstance(val, str) and val in memory:
        return memory[val]
    return val
