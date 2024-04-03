<script>
export default {
  data() {
    return {
      questions : [],
      modAjout : false,
      nomNewQuest : '',
      typeNewQuest : 'SimpleQuestion',
      optionsNewQuest : '',
      reponseNewQuest : ''
    };
  },
  props: {
    url: String,
    idQuestionnaire: Number
  },
  methods: {
    affichQuestions : function() {
      this.questions=[];
      console.log(this.url);
      fetch(this.url)
      .then(response => response.json())
      .then(data => {
        console.log(data);
        
        for (let i = 0; i < data.length; i++) {
          
          fetch(data[i])
          .then(response2 => response2.json())
          .then(data2 => {
            if (data2.questionType === 'MultipleQuestion') {
              this.questions.push({id: data2.id, url: data2.url,questionType: data2.questionType,reponse: data2.reponse,title: data2.title, options: data2.options});
            }
            else {
              this.questions.push({id: data2.id, url: data2.url,questionType: data2.questionType,reponse: data2.reponse,title: data2.title});
            }
          }
      )}
      });
    },
    supprimerQuestion : function($event) {
      fetch('http://localhost:5000/quiz/api/v1.0/quiz/question/'+$event.id, {
        method: 'DELETE'
      })
      .then(response => response.json())
      .then(data => {
        this.questions = this.questions.filter(question => question.id !== $event.id);
      });
    },
    changeModAjout : function() {
      this.modAjout = !this.modAjout;
    },
    ajouterQuestion : function() {
      fetch('http://localhost:5000/quiz/api/v1.0/quiz/'+this.idQuestionnaire, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          title: this.nomNewQuest,
          questionType: this.typeNewQuest,
          options: this.optionsNewQuest,
          reponse: this.reponseNewQuest
        })
      })
      if (this.typeNewQuest === 'MultipleQuestion') {
        this.questions.push({title: this.nomNewQuest, questionType: this.typeNewQuest, options: this.optionsNewQuest, reponse: this.reponseNewQuest});
      }
      else {
        this.questions.push({title: this.nomNewQuest, questionType: this.typeNewQuest, reponse: this.reponseNewQuest});
      }
      this.nomNewQuest = '';
      this.typeNewQuest = 'SimpleQuestion';
      this.optionsNewQuest = '';
      this.reponseNewQuest = '';
      this.changeModAjout();
    }
    
  },

  components: {Question}
}

import Question from './Question.vue';
</script>

<template>
    <section>
      <button @click="affichQuestions">Afficher les questions</button>
      <input type="button" value="Ajouter une Question" @click="changeModAjout">
      <div v-if="modAjout">
        <input type="text" placeholder="Nom de la question" v-model="nomNewQuest">
        <select v-model="typeNewQuest">
          <option value="SimpleQuestion">SimpleQuestion</option>
          <option value="MultipleQuestion">MultipleQuestion</option>
        </select>
        <input v-if="typeNewQuest === 'MultipleQuestion'" type="text" placeholder="Options" v-model="optionsNewQuest">
        <input type="text" placeholder="Réponse" v-model="reponseNewQuest">
        <input type="button" value="Valider" @click="ajouterQuestion">
      </div>
        <ul>
            <li v-for="quest in questions">
                <Question :question="quest" @supprQuest="supprimerQuestion"></Question>
            </li>
        </ul>
    </section>
</template>