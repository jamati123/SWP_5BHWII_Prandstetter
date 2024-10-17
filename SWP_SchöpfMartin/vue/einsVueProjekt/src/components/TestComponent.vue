<script setup lang="ts">
const text = 'worldus maximus'

defineProps<{
    property: string
    counter: number
}>()

function returnSomethingInside(){
    return "something Inside"
}

defineExpose({
    returnSomethingInside
})


</script>

<template>
    <h1> Hello it's me</h1>
    <h2> {{ text }}</h2>
    <h3> {{ property }}</h3>
    <h3>{{ counter }}</h3>
</template>