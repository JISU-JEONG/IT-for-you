<template>
  <div class="main-container">
    <transition name="move">
      <InterviewDetail
        v-if="showInterview"
        :p_info="p_info"
        @close-interview="closeInterview"
      />
    </transition>
    <div class="card company-container">
      <p>회사 선택</p>
      <input type="radio" name="all" id="all" value="" v-model="selectedCompany" style="display:none" class="tag">
      <label class="badge no_highlights" for="all">전체선택</label>
      <span v-for="tag in interviewTag" :key="tag">
        <input type="radio" :name="tag" :id="tag" :value="tag" v-model="selectedCompany" style="display:none" class="tag">
        <label class="badge no_highlights" :for="tag">{{tag}}</label>
      </span>
    </div>
    <transition-group
      name="staggered-fade"
      :css="false"
      @before-enter="beforeEnter"
      @enter="enter"
      @leave="leave"
    >
      <div
        class="card flex"
        v-for="(interview, index) in computedList"
        :key="interview.p_code + index"
        :data-index="index"
      >
        <div class="info">
          <p>{{ interview.p_question }}</p>
          <div class="badge saved" v-if="interview.myinter_check">
            저장된 문제
          </div>
          <div class="badge" v-if="interview.p_code">{{ interview.p_code }}</div>
        </div>
        <div class="next-btn no_highlights" @click="nextButton(interview)">
          <span
            >연습 <br />
            하기</span
          >
        </div>
      </div>
    </transition-group>
    <!-- <div
      class="card flex"
      v-for="interview in interviewList"
      :key="interview.id"
    >
      <div class="info">
        <p>{{ interview.p_question }}</p>
        <div class="badge saved" v-if="interview.myinter_check">
          저장된 문제
        </div>
        <div class="badge" v-if="interview.p_code">{{ interview.p_code }}</div>
      </div>
      <div class="next-btn no_highlights" @click="nextButton(interview)">
        <span
          >연습 <br />
          하기</span
        >
      </div>
    </div> -->
  </div>
</template>

<script>
import InterviewDetail from "@/components/Interview/InterviewDetail.vue";
import Velocity from 'velocity-animate'

export default {
  data() {
    return {
      p_info: {},
      showInterview: false,
      selectedCompany: '',
    };
  },
  methods: {
    nextButton(interview) {
      this.p_info = interview;
      this.showInterview = true;
    },
    closeInterview() {
      this.showInterview = false;
    },
    beforeEnter(el) {
      el.style.opacity = 0
      el.style.height = 0
    },
    enter(el, done) {
      var delay = el.dataset.index * 150
      setTimeout(function () {
        Velocity(
          el,
          { opacity: 1, height: '100px' },
          { complete: done }
        )
      }, delay)      
    },
    leave(el, done) {
      var delay = el.dataset.index * 150
      setTimeout(function () {
        Velocity(
          el,
          { opacity: 0, height: 0 },
          { complete: done }
        )
      }, delay)      
    }
  },
  components: {
    InterviewDetail
  },
  computed: {
    interviewList() {
      return this.$store.state.question.interviewList;
    },
    computedList() {
      if (!this.selectedCompany) {return this.interviewList}
      else {
        const vm = this
        return this.interviewList.filter(interview => interview.p_code === this.selectedCompany)
      }
    },
    interviewTag() {
      return this.$store.getters.interviewTag
    }
  }
};
</script>
<style scoped>
* {
  box-sizing: border-box;
}
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
  position: relative;
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
  color: #c62828;
  border-color: #c62828;
  margin-right: 8px;
}
.next-btn {
  display: inline-block;
  width: 20%;
  height: 100%;
  padding: 16px;
  display: flex;
  color: white;
  background-color: black;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.tag:checked + label {
  color: white;
  background-color: #009688;
}
.next-btn span {
  font-size: 16px;
}
.move-enter-active,
.move-leave-active {
  transition: all 0.5s;
}
.move-enter, .move-leave-to /* .fade-leave-active below version 2.1.8 */ {
  transform: translateY(100%);
}
</style>
