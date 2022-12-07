import json

def roster (tasks):
    print()
    if not tasks:
        print('no tasks to list')
        return

    print('Task')
    for task in tasks:
        print(f'\t{task}')

###################################
def undo (tasks, task_redo):
    print()
    if not tasks:
        print('no tasks to undo')
        return

    tasks = tasks.pop()
    task_redo.append(tasks)

###################################
def redo (tasks, task_redo):
    print()
    if not task_redo:
        print('no tasks to redo')
        return

    task = task_redo.pop()
    tasks.append(task)

###################################
def update (task, tasks):
    print()
    task = task.strip()
    if not task :
        print('you have not typed any tasks')
        return
    tasks.append(task)
###################################

def read(task, file_pah):
    dados = []
    try:
        with open (file_pah, 'r', encoding='utf8') as file:
            dados = json.load(file)
    except FileNotFoundError:
        print('file not found')
        save(task, file_pah)
    return dados
def save(tasks, caminho_arquivos):
    dados = tasks
    with open (caminho_arquivos, 'w', encoding='utf8') as file:
        dados = json.dump(tasks,file, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'execise27.json'
tasks = read([], CAMINHO_ARQUIVO)
task_redo = []


while True : 
    print('commands: list ,undo and redo')
    assignment = input('enter a task or command: ')
    save(tasks, CAMINHO_ARQUIVO)
    
    if assignment == 'list':
        roster(tasks)
        print()
        continue
    elif assignment == 'undo':
        undo(tasks , task_redo)
        print()
        continue
    elif assignment == 'redo':
        redo(tasks , task_redo)
        print()
        continue
    else:
        update(assignment, tasks)
        print()
        continue
