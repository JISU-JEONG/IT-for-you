<template>
  <div class="main-container">
    <transition name="move">
      <InterviewDetail v-if="showInterview" :p_info="p_info" @close-interview="closeInterview" />
    </transition>
    <div class="card company-container">
      <p>회사 선택</p>
      <div class="badge no_highlights">네이버</div>
      <div class="badge no_highlights">네이버</div>
      <div class="badge no_highlights">네이버</div>
      <div class="badge no_highlights">네이버</div>
      <div class="badge no_highlights">네이버</div>
      <div class="badge no_highlights">네이버</div>
    </div>
    <div class="card flex" v-for="interview in interviewList" :key="interview.id">
      <div class="info">
        <p>{{interview.p_question}}</p>
        <div class="badge saved" v-if="interview.myinter_check">저장된 문제</div>
        <div class="badge">{{interview.p_code}}</div>
      </div>
      <div class="next-btn no_highlights" @click="nextButton(interview)"><span>연습하기</span></div>
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
      },
      
    }
  }
</script>
<style scoped>
  * { box-sizing: border-box;}
.no_highlights {
  -webkit-tap-highlight-color: transparent;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.main-container {
  width: 100%;
  max-width: 500px;
  height: 100%;
  margin: 0 auto;
  position:relative;
}
.card {
  width: 90%;
  height: 100px;
  margin: 20px auto 0;
  font-size: 20px;
  background-color: white;
  border-radius: 5px;
  box-shadow: 0 0 2rem 0 rgba(136, 152, 170, 0.15);
}
.flex {
  display: flex;
}
.company-container {
  height: initial;
  padding: 12px;
  margin: 0 auto;
}
.company-container p {
  font-size: 16px;
  margin-bottom: 4px;
}
.company-container .badge {
  margin: 2px 4px;
}

.info {
  display: inline-block;
  width: 80%;
  height: 100%;
  padding: 8px;
}
.info p {
  font-size: 16px;
  margin-bottom: 4px;
}
.badge {
  cursor: pointer;
  display: inline-block;
  font-size: 14px;
  font-weight: 600;
  padding: 3px 6px;
  border-radius: 5px;
  /* background-color: #009688; */
  color: #009688;
  border: 1.5px solid #009688;
}
.saved {
  color: #C62828;
  border-color: #C62828;
  margin-right: 8px;
}
.next-btn {
  display: inline-block;
  width: 20%;
  height: 100%;
  padding: 16px;
  display: flex;
  color: white;
  background-color:black;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
.next-btn span {
  font-size: 16px;
}
.move-enter-active, .move-leave-active {
  transition: all .5s;
}
.move-enter, .move-leave-to /* .fade-leave-active below version 2.1.8 */ {
  transform: translateY(100%)
}
</style>