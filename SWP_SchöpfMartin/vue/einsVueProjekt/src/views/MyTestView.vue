<script setup lang="ts">
import TestComponent from "@/components/TestComponent.vue";
import { ref, useTemplateRef } from 'vue';
let count = ref(0)
let inputValue = ref()

const TestComponentRef = useTemplateRef('tc')

const myData = [
  {prop: "1"},
  {prop: "2"},
  {prop: "3"},
  {prop: "4"},
  {prop: "5"},
]

function printSomething(){
  
  console.log(TestComponentRef.value?.returnSomethingInside())
  console.log(inputValue)
}

</script>
<template>
  <main>
    <TheWelcome />
    hier sollte ein Komponent sein
    <input v-model="inputValue">gib was ein
    <p>
    <button @click="count++">add</button>
    <button @click="printSomething">print</button>
    </p>
    <test-component ref="tc" :property="inputValue" :counter="count"/>
    <div v-for="d in myData" v-bind:key="d.prop">
      <test-component :property="d.prop" :counter="count"/>
    </div>
    <h1 v-if="count > 5"> Count ist </h1>
    <h1 v-else>Not there yet </h1>
  </main>
</template>
