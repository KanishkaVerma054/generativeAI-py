document.addEventListener('DOMContentLoaded', function() {
    const input = document.getElementById('todo-input');
    const addBtn = document.getElementById('add-btn');
    const todoList = document.getElementById('todo-list');

    function addTodo() {
        const value = input.value.trim();
        if (value === '') return;

        const li = document.createElement('li');
        li.textContent = value;
        li.addEventListener('click', () => {
            li.classList.toggle('completed');
        });

        const delBtn = document.createElement('button');
        delBtn.textContent = '✕';
        delBtn.className = 'delete-btn';
        delBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            li.remove();
        });

        li.appendChild(delBtn);
        todoList.appendChild(li);
        input.value = '';
        input.focus();
    }

    addBtn.addEventListener('click', addTodo);
    input.addEventListener('keyup', (e) => {
        if (e.key === 'Enter') addTodo();
    });
});
