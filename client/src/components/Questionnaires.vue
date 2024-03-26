<script>
export default {
  data: {
    questionnaires : []
  },
  methods: {
    affichQuestionnaires : function() {
      fetch('http://localhost:5000/quiz/api/v1.0/quiz')
      .then(response => response.json())
      .then(data => {
        this.questionnaires = data;
      });
    },
    afficheQuestions : function() {
        this.$emit('afficheQuest', {url: this.url});
    }
  },
  emits: ['afficheQuest']
}

import Questionnaire from './Questionnaire.vue';
</script>

<template>
    <section>
        <button @click="affichQuestionnaires">Afficher les questionnaires</button>
        <ul>
            <li v-for="quest in questionnaires">
                <Questionnaire :name="quest.name" :url="quest.url" @afficheQuest="afficheQuestions"></Questionnaire>
            </li>
        </ul>
    </section>
</template>