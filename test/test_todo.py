import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app.todo import TodoApp

# Fixture for a fresh TodoApp instance
@pytest.fixture
def sample_app():
    return TodoApp()

# Test adding a task
def test_add_task(sample_app):
    sample_app.add_task('Buy milk')
    assert len(sample_app.tasks) == 1
    assert sample_app.tasks[0]['task'] == 'Buy milk'

# Test deleting a task
def test_delete_task(sample_app):
    sample_app.add_task('Read newspaper')
    sample_app.delete_task(0)
    assert sample_app.tasks == []

# Test marking a task as complete
def test_complete_task(sample_app):
    sample_app.add_task('Writing')
    sample_app.complete_task(0)
    assert sample_app.tasks[0]['completed'] is True

# Test input validation: empty string
def test_emptytask_notallowed(sample_app):
    with pytest.raises(ValueError):
        sample_app.add_task('')

# Parameterized test for multiple task inputs
tasks = ['Go jogging', 'Write notes', 'Read book']
@pytest.mark.parametrize('task', tasks) #pytest parametrize decorator. It tells pytest to run the test multiple times, once for each value
def test_parametrized_tasks(sample_app, task):
    sample_app.add_task(task)
    print(sample_app)
    assert sample_app.tasks[0]['task'] == task


# Test adding multiple tasks consecutively
def test_add_multiple_tasks_consecutively(sample_app):
    task_list = ['drawing', 'playing', 'studying']
    for task in task_list:
        sample_app.add_task(task)


    assert len(sample_app.tasks) == len(task_list)
    for i in range(len(task_list)):
        assert sample_app.tasks[i]['task'] == task_list[i]
        assert sample_app.tasks[i]['completed'] is False # Check that the task is not marked as completed

