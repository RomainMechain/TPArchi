<script>
 export default {
   props: {
     questionnaire: Object
   },
   methods: {
    afficheQuestions : function() {
        console.log(this.questionnaire.url);    
        this.$emit('afficheQuest', {url: this.questionnaire.url});

        }
   },
   emits: ['afficheQuest']
 }
</script>

<template>
  <div>
    <h1 @click="afficheQuestions">{{ questionnaire.name }}</h1>
    
  </div>
</template>