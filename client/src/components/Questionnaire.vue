<script>
 export default {
   props: {
     name: String,
     url: String,
   },
   methodes: {
    afficheQuestions : function() {
            this.$emit('afficheQuest', {url: this.url});
        }
   },
   emits: ['afficheQuest']
 }
</script>

<template>
  <div>
    <h1 @click="afficheQuestions">{{ name }}</h1>
  </div>
</template>