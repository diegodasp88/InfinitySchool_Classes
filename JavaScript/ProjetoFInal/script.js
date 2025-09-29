function openForm() {
  document.querySelector("#modalAddTask").style.display = "flex";
}

function closeForm() {
  document.querySelector("#modalAddTask").style.display = "none";
}

window.onclick = function (evento) {
  if (evento.target == document.querySelector("#modalAddTask")) {
    closeForm();
  }
};

async function listTasks() {
  const url = "https://68d4a5c4214be68f8c69e247.mockapi.io/tasks";
  const response = await fetch(url);
  const taskList = await response.json();

  const listContent = document.querySelector("#listContent");
  const taskStatus = document.querySelector("#statusTask");
  listContent.innerHTML = "";

  taskList.forEach(task => {
      const listContentStructure = `
          <div id="taskContent">
              <p id="idTask">${task.id}</p>
              <p id="textTask">${task.text}</p>
              <p id="statusTask">${task.status}</p>
              <button 
                type="button" 
                class="doneBtn" 
                onclick="updateTask(${task.id}, '${task.status}')">
                  ${task.status === "Pending" ? "Mark as Done" : "Mark as Pending"}
              </button>
              <button 
                type="button" 
                class="deleteBtn" 
                onclick="deleteTask(${task.id})">
                  Delete
              </button>
          </div>
      `;

      listContent.innerHTML += listContentStructure;
      const textTask = document.querySelector("#newTask");
      textTask.value = ""
  });
}

listTasks();


async function addTask() {
  const textTask = document.querySelector("#newTask").value;

  const task = {
      text: textTask,
      status: "Pending"
  };

  const url = "https://68d4a5c4214be68f8c69e247.mockapi.io/tasks";
  const response = await fetch(url, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(task)
  });
  closeForm();
  listTasks();
}


async function deleteTask(id) {
  const url = `https://68d4a5c4214be68f8c69e247.mockapi.io/tasks/${id}`;
  const response = await fetch (url, { method: "DELETE" });

  if (response.status === 200) {
    alert("Task removed successfully!")
  } else {
    alert("Task removal failed.")
  }

  listTasks();
}


async function updateTask(id, currentStatus) {
  const url = `https://68d4a5c4214be68f8c69e247.mockapi.io/tasks/${id}`;
  const newStatus = currentStatus === "Pending" ? "Done" : "Pending";
  const response = await fetch (url, { 
    method: "PUT",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ status: newStatus })
  });

  if (response.ok) {
    alert("Task status updated!")
    listTasks();
  } else {
    alert("Task status update failed.")
  }
}
