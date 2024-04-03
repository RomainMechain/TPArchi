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
  method: {
    afficheDetail : function() {
      this.detail= true;
    }
  },
}
</script>

<template>
  <div>
    <h4 @click="afficheDetail">{{ question.title }}</h4>
    <p v-if="this.detail">{{ question.questionType }}</p>
    <p v-if="this.detail">{{ question.reponse }}</p>
  </div>
</template>