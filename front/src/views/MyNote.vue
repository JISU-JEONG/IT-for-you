<template>  
  <div>
    <ul @click="deleteMynote">
      <li v-for="c in questionList" :key="c.id" :data-id="c.id">{{c.problems.p_question}}</li>
    </ul>
  </div>
</template>
<script>
import axios from "@/api/api.service.js";

export default {
  data() {
    return {
      questionList: []
    }
  },
  methods: {
    getMyNote() {
      axios.get(`/api/myprobs/myprob/${this.user_id}`)
        .then(res => {
          this.questionList = res.data
        })
    },
    deleteMynote() {
      const p_id = event.target.dataset.id
      axios.delete(`/api/myprobs/myprob/${this.user_id}/${p_id}`)
        .then(res => {
          this.questionList.splice(this.questionList.findIndex(q => q.id === p_id*1), 1)
        })
        .catch(err => console.error(err))
    }
  },
  computed: {
    user_id() {
      return this.$store.getters.getUserInfo.id
    }
  },
  mounted() {
    this.getMyNote()
  },
}
</script>