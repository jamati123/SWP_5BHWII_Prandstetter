<template>
  <div>
    <h1>Todo List</h1>
    <input v-model="newTodoTask" placeholder="Task" />
    <input v-model="newTodoDue" type="datetime-local" placeholder="Due Date" />
    <button @click="addTodo">Add Todo</button>
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <input type="checkbox" v-model="todo.done" @change="updateTodo(todo)" />
        <h3>{{ todo.task }}</h3>
        <p>Due: {{ todo.due || 'No due date' }}</p>
        <button @click="deleteTodo(todo.id)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import axios from 'axios';

interface Todo {
  id: number;
  task: string;
  done: boolean;
  due?: string; // Optionales Fälligkeitsdatum
}

export default defineComponent({
  name: 'TodoComponent',
  setup() {
    const todos = ref<Todo[]>([]);
    const newTodoTask = ref('');
    const newTodoDue = ref('');

    // Todos vom Server laden
    const loadTodos = async () => {
      try {
        const response = await axios.get('http://localhost:3000/todos');
        todos.value = response.data;
      } catch (error) {
        console.error('Error loading todos:', error);
      }
    };

    // Neues Todo hinzufügen
    const addTodo = async () => {
      if (newTodoTask.value) {

        const newTodo: Omit<Todo, 'id'> = {
          task: newTodoTask.value,
          done: false,
          due: newTodoDue.value ? new Date(newTodoDue.value).toISOString() : null,
        };
      try {
          const response = await axios.post('http://localhost:3000/todos', newTodo);
          todos.value.push(response.data); // Add the returned todo to the list
          newTodoTask.value = '';
          newTodoDue.value = '';
      } catch (error) {
          console.error('Error adding todo:', error);
        }
      }
    };


    // Todo-Status aktualisieren
    const updateTodo = async (todo: Todo) => {
      try {
        await axios.put(`http://localhost:3000/todos?id=eq.${todo.id}`, {
          done: todo.done,
          task: todo.task,
          due: todo.due,
        });
      } catch (error) {
        console.error('Error updating todo:', error);
      }
    };

    // Todo löschen
    const deleteTodo = async (id: number) => {
      try {
        await axios.delete(`http://localhost:3000/todos/${id}`);
        todos.value = todos.value.filter(todo => todo.id !== id);
      } catch (error) {
        console.error('Error deleting todo:', error);
      }
    };

    onMounted(loadTodos);

    return {
      todos,
      newTodoTask,
      newTodoDue,
      addTodo,
      updateTodo,
      deleteTodo,
    };
  },
});
</script>

<style scoped>
/* Add your styles here */
</style>
