<script>
export default {
  data() {
    return {
      questions : []
    };
  },
  props: {
    url: String,
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
    }
    
  },

  components: {Question}
}

import Question from './Question.vue';
</script>

<template>
    <section>
      <button @click="affichQuestions">Afficher les questions</button>
        <ul>
            <li v-for="quest in questions">
                <Question :question="quest" @supprQuest="supprimerQuestion"></Question>
            </li>
        </ul>
    </section>
</template>