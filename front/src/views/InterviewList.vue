<template>
  <div class="main-container">
    <InterviewDetail v-if="showInterview" :p_info="p_info" @close-interview="closeInterview" />
    <div class="company-list">
      <div class="badge">네이버</div>
      <div class="badge">네이버</div>
      <div class="badge">네이버</div>
      <div class="badge">네이버</div>
      <div class="badge">네이버</div>
    </div>
    <div class="card" v-for="interview in interviewList" :key="interview.id">
      <div class="info">
        <p>{{interview.p_question}}</p>
        <div class="badge">{{interview.p_code}}</div>
      </div>
      <div class="btn" @click="nextButton(interview)"><span>go next</span></div>
    </div>
  </div>
</template>
<script>
import InterviewDetail from '@/components/InterviewDetail.vue'

  export default {
    data() {
      return {
        p_info: {},
        showInterview: false
      }
    },
    methods: {
      nextButton(interview) {
        this.p_info = interview
        this.showInterview = true
      },
      closeInterview() {
        this.showInterview = false
      }
    },
    components: {
      InterviewDetail
    },
    computed: {
      interviewList() {
        return this.$store.state.question.interviewList
      }
    }
  }
</script>
<style scoped>
  * { box-sizing: border-box;}
.main-container {
  width: 100%;
  max-width: 500px;
  height: 100%;
  margin: 0 auto;
  position:relative;
}
.card {
  width: 90%;
  height: 100px; /* 필요한가?*/
  display: flex;
  margin: 20px auto 0;
  font-size: 20px;
  background-color: white;
  border-radius: 5px;
  box-shadow: 0 0 2rem 0 rgba(136, 152, 170, 0.15);
}
.company-list {
  margin: 0 20px 20px;
}
.info {
  display: inline-block;
  width: 70%;
  height: 100%;
  padding: 8px;
}
.info p {
  font-size: 16px;
}
.badge {
  display: inline-block;
  font-size: 14px;
  padding: 3px 6px;
  color: white;
  border-radius: 5px;
  background-color: #009688;
}
.btn {
  display: inline-block;
  width: 30%;
  height: 100%;
  padding: 16px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
.btn span {
  font-size: 16px;
}
</style>