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
    afficheQuestions : function($event) {
      console.log(this.url);
      this.$emit('afficheQuest', {url: $event.url, id: $event.id});
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
    },
    editQuestionnaire : function($event) {
      fetch('http://localhost:5000/quiz/api/v1.0/quiz/'+$event.id, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({name: $event.name})
      })
    },
    supprimerQuestionnaire : function($event) {
      fetch('http://localhost:5000/quiz/api/v1.0/quiz/'+$event.id, {
        method: 'DELETE'
      })
      .then(response => response.json())
      .then(data => {
        this.questionnaires = this.questionnaires.filter(questionnaire => questionnaire.id !== $event.id);
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
        <button @click="affichQuestionnaires" class="btn btn-primary m-1">Afficher les questionnaires</button>
        <ul style="list-style-type: none;">
            <li v-for="quest in questionnaires">
                <Questionnaire :questionnaire="quest" @afficheQuest="afficheQuestions" @editQuest="editQuestionnaire" @supprQuest="supprimerQuestionnaire"></Questionnaire>
            </li>
        </ul>
        <input type="text" v-model="newQuestionnaire" placeholder="Ajouter un nouveau questionnaire" @keyup.enter="ajouterQuestionnaire" class="col-form-label border-2 rounded mt-4">
    </section>
</template>