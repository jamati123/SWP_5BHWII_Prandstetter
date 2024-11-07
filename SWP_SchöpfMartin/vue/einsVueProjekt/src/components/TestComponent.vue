<script setup lang="ts">
import axios from 'axios';
import { computed, onMounted } from 'vue';


const text = 'worldus maximus'

const props = defineProps<{
    property: string 
    counter: number
}>()

const today = new Date()

function returnSomethingInside(){
    return "something Inside"
}

function dangerSepp() {
    if (props.property.includes('Sepp')) {
        return 'danger'
    }
    return ''
}   

defineExpose({
    returnSomethingInside
})

const emit = defineEmits(['fetchSUccess'])

onMounted(async () =>{
   let data = await axios.get("https://api.predic8.de/shop/v2/products")
    emit('fetchSUccess', data)
}
)

const propertyPlusHello = computed(() => {
    return "hallo " + props.property
})

const germanToday = computed(() => {
    return "today is " + today 
})

</script>

<template>
    <h1> Hello it's me</h1>
 
    <h2> {{ text }}</h2>
    <h3> {{ property }}</h3>

    <h3> {{ propertyPlusHello }}</h3>

    <h2 :class="dangerSepp()"> {{ property }} </h2>
    <h3> {{ germanToday }}</h3>
    <h3>{{ counter }}</h3>
</template>

<style>
    .danger {
        background-color: red;
    }
</style>