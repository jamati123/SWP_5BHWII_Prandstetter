<script setup lang="ts">
import TestComponent from "@/components/TestComponent.vue";
import { ref } from 'vue';
let count = ref(0)
</script>
<template>
  <main>
    <TheWelcome />
    hier sollte ein Komponent sein
    <test-component property="Das ist alles nur geklaut" :counter="count"/>
    <button @click="count++">add</button>
  </main>
</template>
