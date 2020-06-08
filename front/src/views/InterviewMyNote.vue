<template>
  <div class="main-container">
    <span v-for="interview in interviewList" :key="interview.id" @click="showDetail(interview.id)">
      <button class="accordion" @click="showPanel">Section 1 {{interview.p_question}}</button>
      <div class="panel">
        <div class="my-interview">{{interview.p_answer}}</div>
        <div class="best-interview">{{interview.myanswer}}</div>
        <audio-player :src="interview.audio_data"/>
      </div>
    </span>

    
  </div>
</template>
<script>
  import AudioPlayer from '@/components/player'
  import axios from '@/api/api.service.js'
  export default {
    data() {
      return {
        interviewList: [],
      }
    },
    components: {
      AudioPlayer
    },
    methods: {
      getMyInterview() {
        const token = this.$session.get("jwt");
        const headers =  {
          Authorization: `JWT ${token}`
        }        
        axios.get(`/api/interprobs/myinters/${this.user_id}/`, { headers: headers })
          .then(res => {
            console.log(res.data)
            this.interviewList = res.data
          })
          .catch(err => {
            console.error(err)
          })
      },
  
      showDetail(p_id) {
        const token = this.$session.get("jwt");
        const headers =  {
          Authorization: `JWT ${token}`
        }        
        axios.get(`/api/interprobs/myinters/${this.user_id}/${p_id}/`, { headers: headers })
          .then(res => {
            this.select = res.data.audio_data
            
          })
          .catch(err => {
            console.error(err)
          })
      },
      showPanel() {
        console.log(event.target)
      }
    },
    computed: {
      user_id() {
        return this.$store.getters.user
      }
    },
    mounted() {
      this.getMyInterview()
    }
  }
</script>
<style scoped>
.main-container {
  width: 100%;
  max-width: 500px;
  margin: 0 auto;
}
.accordion {
  width: 100%;
  height: 52px;
  border: none;
  outline: none;
  cursor: pointer;
  background-color: lightseagreen;
}
.panel {
  width: 100%;
  background-color: white;
}
</style>