<script>
import Questionnaires from './components/Questionnaires.vue';
import Questions from './components/Questions.vue';

let data={
  title:'Voici vos questionnaires',
  questions:false,
  urlQuest:"",
  operations:false,

}


export default{
  data(){
    return data;
  },
  components: {Questionnaires,Questions},
  methods: {
    afficherQuestions($event){
      this.questions=true;
      this.urlQuest=$event.url;
      console.log($event);
    },
  }
  
}
</script>

<template>
  <header>
    <h1>{{ title }}</h1>
  </header>
  <div class="questionnaires">
    <h2>Questionnaires : </h2>
    <Questionnaires @afficheQuest="afficherQuestions"></Questionnaires>
  </div>
  <div class="questions">
    <h2>Questions : </h2>
    <Questions v-if="this.questions" :url="this.urlQuest"></Questions>
  </div>
  <div class="operations">
  </div>
</template>


