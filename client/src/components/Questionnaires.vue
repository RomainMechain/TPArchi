<script>
export default {
  data() {
    return {
      questionnaires : [],
      newQuestionnaire : ""
    };
  },
  methods: {
    affichQuestionnaires : function() {
      fetch('http://localhost:5000/quiz/api/v1.0/quiz')
      .then(response => response.json())
      .then(data => {
        this.questionnaires = [];
        for (let i = 0; i < data.length; i++) {
          this.questionnaires.push({name: data[i].name, url: data[i].url, id: data[i].id});
        }
      });
    },
    afficheQuestions : function() {
        this.$emit('afficheQuest', {url: this.url});
    },
    ajouterQuestionnaire : function() {
      fetch('http://localhost:5000/quiz/api/v1.0/quiz', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({name: this.newQuestionnaire})
      })
      .then(response => response.json())
      .then(data => {
        this.newQuestionnaire = "";
        this.affichQuestionnaires();
      });
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
                <Questionnaire :questionnaire="quest" @afficheQuest="afficheQuestions"></Questionnaire>
            </li>
        </ul>
        <input type="text" v-model="newQuestionnaire" placeholder="Ajouter un nouveau questionnaire" @keyup.enter="ajouterQuestionnaire">
    </section>
</template>