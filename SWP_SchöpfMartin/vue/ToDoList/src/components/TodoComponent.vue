<template>
  <div>
    <h1>Todo List</h1>
    <input v-model="newTodoTitle" placeholder="Title" />
    <input v-model="newTodoText" placeholder="Text" />
    <button @click="addTodo">Add Todo</button>
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <h3>{{ todo.title }}</h3>
        <p>{{ todo.text }}</p>
        <button @click="deleteTodo(todo.id)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, watch } from 'vue'

interface Todo {
  id: number
  title: string
  text: string
}

export default defineComponent({
  name: 'TodoComponent',
  setup() {
    const todos = ref<Todo[]>([])
    const newTodoTitle = ref('')
    const newTodoText = ref('')

    const loadTodos = () => {
      const savedTodos = localStorage.getItem('todos')
      if (savedTodos) {
        todos.value = JSON.parse(savedTodos)
      }
    }

    const saveTodos = () => {
      localStorage.setItem('todos', JSON.stringify(todos.value))
    }

    const addTodo = () => {
      if (newTodoTitle.value && newTodoText.value) {
        const newTodo: Todo = {
          id: Date.now(),
          title: newTodoTitle.value,
          text: newTodoText.value,
        }
        todos.value.push(newTodo)
        newTodoTitle.value = ''
        newTodoText.value = ''
      }
    }

    const deleteTodo = (id: number) => {
      todos.value = todos.value.filter(todo => todo.id !== id)
    }

    onMounted(loadTodos)
    watch(todos, saveTodos, { deep: true })

    return {
      todos,
      newTodoTitle,
      newTodoText,
      addTodo,
      deleteTodo,
    }
  },
})
</script>

<style scoped>
/* Add your styles here */
</style>
