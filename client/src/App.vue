<script>
import Questionnaires from './components/Questionnaires.vue';
import Questions from './components/Questions.vue';

let data={
  title:'Voici vos questionnaires',
  questions:false,
  urlQuest:"",
  idQuest:"",
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
      this.idQuest=$event.id;
      console.log($event);
    },
  }
  
}
</script>

<template>
  <header>
    <h1>{{ title }}</h1>
  </header>
  <div class="row">
  <div class="col lg-6">
    <h2>Questionnaires : </h2>
    <Questionnaires @afficheQuest="afficherQuestions"></Questionnaires>
  </div>
  <div class="col lg-6">
    <h2>Questions : </h2>
    <Questions v-if="this.questions" :url="this.urlQuest" :idQuestionnaire="this.idQuest"></Questions>
  </div>
</div>
  
</template>


