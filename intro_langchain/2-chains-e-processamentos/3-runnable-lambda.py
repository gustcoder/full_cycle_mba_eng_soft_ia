from langchain_core.runnables import RunnableLambda

def select_winspector_hero(color:str) -> dict:
    hero = ""
    match color:
        case "red": hero = "Fire"
        case "yellow": hero = "Biker"
        case "green": hero = "Highter"
        case _:
            hero = "Junko"
    return {"hero": hero}

# a partir de agora esta função pode ser chamada dentro de um chain
# mesmo sem ter o decorator @chain (bom para funções legado)
parse_runnable = RunnableLambda(select_winspector_hero)    