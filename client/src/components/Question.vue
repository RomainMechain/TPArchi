<script>
 export default {
   props: {
     question: Object,
   },
   data() {
    return {
      detail : false,
    };
  },
  methods: {
    afficheDetail : function() {
      console.log('click');
      this.detail=!this.detail;
    },
    supprimerQuestion : function() {
      this.$emit('supprQuest', {id: this.question.id});
    }
  },
  emits: ['supprQuest'],
}
</script>

<template>
  <div>
    <h4 @click="afficheDetail">{{ question.title }}</h4>
    <p v-if="this.detail">Type de question : {{ question.questionType }}</p>
    <p v-if="question.questionType === 'MultipleQuestion' && this.detail">Options : {{ question.options }}</p>
    <p v-if="this.detail">Réponse : {{ question.reponse }}</p>
    <input type="button" value="Supprimer" @click="supprimerQuestion">
  </div>
</template>