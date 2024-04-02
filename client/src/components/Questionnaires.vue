<script>
export default {
  data() {
    return {
      questionnaires : []
    };
  },
  methods: {
    affichQuestionnaires : function() {
      fetch('http://localhost:5000/quiz/api/v1.0/quiz')
      .then(response => response.json())
      .then(data => {
        this.questionnaires = [];
        for (let i = 0; i < data.length; i++) {
          this.questionnaires.push({name: data[i].name, url: data[i].url});
        }
      });
    },
    afficheQuestions : function() {
        this.$emit('afficheQuest', {url: this.url});
    }
  },
  emits: ['afficheQuest'],
  components: {Questionnaire}
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