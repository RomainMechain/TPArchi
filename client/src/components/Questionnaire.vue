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
            this.$emit('afficheQuest', {url: this.url});
    },
    changeMod : function() {
      this.modEdit = !this.modEdit;
      console.log(this.modEdit);
    },
    editQuestionnaire : function() {
      emit('editQuest', {name: this.questionnaire.name, id: this.questionnaire.id});
    }
   },
   emits: ['afficheQuest', 'editQuest']
 }
</script>

<template>
  <div v-if="!modEdit">
    <h1 @click="afficheQuestions">{{ questionnaire.name }}</h1>
    <input type="button" value="Modifier" @click="changeMod">
  </div>
  <div v-else>
    <input type="text" v-model="questionnaire.name">
    <input type="button" value="Valider" @click="editQuestionnaire">
  </div>
</template>