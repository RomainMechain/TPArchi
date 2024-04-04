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
        this.$emit('afficheQuest', {url: this.questionnaire.url, id: this.questionnaire.id, name: this.questionnaire.name});
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
    <h3 @click="afficheQuestions">{{ questionnaire.name }}</h3>
    <input type="button" value="Modifier" @click="changeMod" class="btn btn-info m-1">
    <input type="button" value="Supprimer" @click="supprimerQuestionnaire" class="btn btn-danger m-1">
  </div>
  <div v-else>
    <input type="text" v-model="questionnaire.name" class="col-form-label border-2 rounded m-1 mt-4">
    <input type="button" value="Valider" @click="editQuestionnaire" class="btn btn-success m-1">
  </div>
</template>