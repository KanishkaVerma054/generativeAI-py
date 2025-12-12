let todos = [];
document.getElementById('add-todo').addEventListener('click', function() {
    let todoInput = document.getElementById('todo-input');
    if (todoInput.value) {
        todos.push(todoInput.value);
        todoInput.value = '';
        renderTodos();
    }
});

function renderTodos() {
    let todoList = document.getElementById('todo-list');
    todoList.innerHTML = '';
    todos.forEach((todo, index) => {
        let li = document.createElement('li');
        li.innerText = todo;
        let deleteBtn = document.createElement('button');
        deleteBtn.innerText = 'Delete';
        deleteBtn.onclick = function() {
            todos.splice(index, 1);
            renderTodos();
        };
        li.appendChild(deleteBtn);
        todoList.appendChild(li);
    });
}
