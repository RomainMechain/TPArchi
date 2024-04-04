<script>
 export default {
   props: {
     question: Object,
   },
   data() {
    return {
      detail : false,
      editMod: false
    };
  },
  methods: {
    afficheDetail : function() {
      console.log('click');
      this.detail=!this.detail;
    },
    supprimerQuestion : function() {
      this.$emit('supprQuest', {id: this.question.id});
    },
    changeModEdit : function() {
      this.editMod = !this.editMod;
    },
    editQuestion : function() {
      fetch('http://localhost:5000/quiz/api/v1.0/quiz/question/'+this.question.id, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          title: this.question.title,
          questionType: this.question.questionType,
          options: this.question.options,
          reponse: this.question.reponse,
          id: this.question.id
        })
      })
      this.changeModEdit();
    }
  },
  emits: ['supprQuest'],
}
</script>

<template>
  <div>
    <div v-if="!editMod">
      <h4 @click="afficheDetail">{{ question.title }}</h4>
      <p v-if="this.detail">Type de question : {{ question.questionType }}</p>
      <p v-if="question.questionType === 'MultipleQuestion' && this.detail">Options : {{ question.options }}</p>
      <p v-if="this.detail">Réponse : {{ question.reponse }}</p>
      <input type="button" value="Supprimer" @click="supprimerQuestion">
      <input type="button" value="Modifier" @click="changeModEdit">
    </div> 
    <div v-else>
      <input type="text" v-model="question.title">
      <input v-if="question.questionType === 'MultipleQuestion'" type="text" v-model="question.options">
      <input type="text" v-model="question.reponse">
      <input type="button" value="Valider" @click="editQuestion">
    </div>
  </div>
</template>