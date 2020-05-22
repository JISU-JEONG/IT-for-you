<template>
  <div class="wrapper" style="overflow: scroll;">
    <table style="width: 100%;">
      <tr>
        <th>카테고리</th>
        <th>문제</th>
        <th>삭제</th>
      </tr>
      <tr v-for="question in questions" :key="question.p_id" >
        <td>{{category[question.pc_id]}}</td>
        <td>{{question.p_question}}</td>
        <td class="btn" @click="deleteQuestion(question.p_id)">삭제</td>
      </tr>
    </table>
  </div>
</template>
<script>
import axios from 'axios'
export default {
    data() {
      return {
        category: ["", "Web", "Server", "Algorithm", "DataBase", "Network", "JAVA", "Python", "OS"],
        questions: []
      }
    },
    methods: {
      loadAllQuestions() {
        axios.get('http://211.213.225.87:8086/api/problems/probs/')
        .then(res => {
          this.questions = res.data
        })
      },
      deleteQuestion(id) {
        if (confirm('문제를 삭제하시겠습니까?')) {
          axios.delete(`http://211.213.225.87:8086/api/problems/delete_prob/${id}/`)
          .then(res => {
            this.questions.splice(this.questions.findIndex(p => p.p_id === id), 1)
          })
        }
      }
      // 수정은 다음에 합니다...
    },
    mounted() {
      this.loadAllQuestions()
    }

}
</script>
<style scoped>
  @font-face { font-family: 'RIDIBatang'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_twelve@1.0/RIDIBatang.woff') format('woff'); font-weight: normal; font-style: normal; }
  * {font-family: 'RIDIBatang';}
  li { list-style: none; cursor: pointer;}
  th {border: 1px solid rgb(107, 107, 107)}
  tr:nth-child(2n) {
      background-color: rgb(230, 230, 230);
    }
  td {text-align: center;}
  .btn {cursor: pointer;}
  .wrapper {width: 100%; height: 100%;}
  .question-container {width: 60%; height: 100%; border: 1px solid black;}
</style>