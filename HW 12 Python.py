from jira import JIRA

# Создание объекта JIRA без авторизации (только для локального использования или случаев, где авторизация не требуется)
jira = JIRA(server='https://timofeika2099.atlassian.net/jira/software/projects/KAN/boards/1')  # Замените URL на адрес вашего сервера Jira

# Создание задачи
issue_dict = {
    'project': {'key': 'KAN'},  # Замените 'PROJ' на ваш ключ проекта
    'summary': 'New issue from jira-python',
    'description': 'Look into this one',
    'issuetype': {'name': 'Task'},
}
new_issue = jira.create_issue(fields=issue_dict)

# Получение задач из бэклога
backlog_issues = jira.search_issues('project=PROJ and sprint is empty')

# Создание спринта
board_id = 1  # ID вашей доски (board), замените на соответствующий ID
sprint_name = 'Sprint 1'
sprint = jira.create_sprint(name=sprint_name, board_id=board_id)

# Добавление задач в спринт
sprint_id = sprint.id
jira.add_issues_to_sprint(sprint_id, [issue.key for issue in backlog_issues])

# Начало спринта
jira.start_sprint(sprint_id, name=sprint_name, startDate='2023-01-01T00:00:00.000Z', endDate='2023-01-14T00:00:00.000Z')

# Завершение спринта
jira.complete_sprint(sprint_id)

print("Готово!")