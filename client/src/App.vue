<script>
import Questionnaires from './components/Questionnaires.vue';
// import Questions from './components/Questions.vue';

let data={
  title:'Voici vos questionnaires',
  questions:false,
  operations:false,

}


export default{
  data(){
    return data;
  },
  components: {Questionnaires},
  
}
</script>

<template>
  <header>
    <h1>{{ title }}</h1>
  </header>
  <div class="questionnaires">
    <h2>Questionnaires : </h2>
    <Questionnaires></Questionnaires>
  </div>
  <div class="questions">
    <h2>Questions : </h2>
  </div>
  <div class="operations">
  </div>
</template>


