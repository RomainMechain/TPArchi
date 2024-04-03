<script>
 export default {
   props: {
     questionnaire : Object
   },
   data() {
     return {
       modEdit: false
     };
   },
   methods: {
    afficheQuestions : function() {
        console.log(this.questionnaire.url);    
        this.$emit('afficheQuest', {url: this.questionnaire.url});
    },
    changeMod : function() {
      this.modEdit = !this.modEdit;
    },
    editQuestionnaire : function() {
      this.$emit('editQuest', {name: this.questionnaire.name, id: this.questionnaire.id});
      this.changeMod();
    },
    supprimerQuestionnaire : function() {
      this.$emit('supprQuest', {id: this.questionnaire.id});
    }
   },
   emits: ['afficheQuest', 'editQuest', 'supprQuest']
 }
</script>

<template>
  <div v-if="!modEdit">
    <h1 @click="afficheQuestions">{{ questionnaire.name }}</h1>
    <input type="button" value="Modifier" @click="changeMod">
    <input type="button" value="Supprimer" @click="supprimerQuestionnaire">
  </div>
  <div v-else>
    <input type="text" v-model="questionnaire.name">
    <input type="button" value="Valider" @click="editQuestionnaire">
  </div>
</template>