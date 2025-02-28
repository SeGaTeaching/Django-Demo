// scripts.js

document.getElementById('task-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Verhindert das normale Abschicken des Formulars

    const titleInput = document.getElementById('id_title');  // ID vom Form-Widget
    const title = titleInput.value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch("/tasks/add_task/", {
        method: "POST",
        headers: {
            "X-CSRFToken": csrfToken,
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
            "title": title
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            const taskList = document.getElementById('task-list');
            const newTask = document.createElement('li');
            newTask.textContent = `${data.title} - ${data.created_at}`;
            taskList.prepend(newTask);  // Aufgabe oben hinzufügen
            titleInput.value = '';  // Formular leeren
        }
    })
    .catch(error => console.error('Error:', error));
});