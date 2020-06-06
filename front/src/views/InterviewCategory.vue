<template>
  <div class="main-container">
    <div class="info">
      <h2>면접 준비</h2>
      <p><small>이런저런 안내문구를 작성하겠습니다.</small></p>
      <p><small>카테고리, 회사를 선택하세요.</small></p>
    </div>
    <div style="margin-top:-60px" class="flex flex-wrap">
      <div class="card"  v-for="c in questionCategory" :key="c" @click="getInterview(c)">
        {{c}}
      </div>
      <div class="card" style="visibility: hidden;"></div>
    </div>
    <div class="saved-interview-btn" @click="submitData">저장된 문제 보러가기</div>
  </div>
</template>

<script>
import axios from "@/api/api.service.js";

export default {
  name: "InterviewCategory",
  data() {
    return {
      selectedCategory: '',
      questionData: {},
      questionCategory: []
    };
  },
  methods: {
    init() {
      axios.get("/api/problems/prob_cate/").then(({ data }) => {
        data.forEach(({ pc_id, pc_value }) => {
          this.$set(this.questionCategory, pc_id - 1, pc_value);
        });
      });
      axios.get("/api/problems/prob_type/").then(({ data }) => {
        this.$store.dispatch("questionType", data);
      });
    },
    getInterview(c) {
      this.$store.dispatch('setInterviewList', {
        user_id: this.user_id,
        category: c
      })
      .then(() => {
        this.$router.push({
          path:'/interview/list'
        })
      })
    },
    submitData() {
      this.$router.push("/interview/list");
    },
  },
  computed: {
    user_id() {
      return this.$store.getters.getUserInfo.id;
    }
  },
  beforeMount() {
    this.init();
  }
};
</script>

<style scoped lang="scss">
* {
  box-sizing: border-box;
  font-family: MapoPeacefull; 
}
.no_highlights{
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
}
.info {
  height: 200px;
  padding: 20px;
  color: white;
  background-color: #888;
}
.info h2 {
  text-align: center;
}
.flex { display: flex ;}
.flex-center { justify-content: center; align-items: center;}
.flex-column { flex-direction: column;}
.flex-wrap {flex-wrap: wrap;}
.card {
  width: 42%;
  height: 72px;
  line-height: 72px;
  text-align: center;
  margin: 20px auto 0;
  font-size: 20px;
  background-color: white;
  border-radius: 5px;
  cursor: pointer;
  box-shadow: 0 0 2rem 0 rgba(136, 152, 170, 0.15);
}
.saved-interview-btn {
  margin: 20px 20px 0;
  height: 72px;
  line-height: 72px;
  text-align: center;
  color: white;
  font-size: 20px;
  background-color: rgb(29, 29, 31);
  border-radius: 5px;
  cursor: pointer;
  box-shadow: 0 0 2rem 0 rgba(136, 152, 170, 0.15);
}
@font-face {
  font-family: "MapoPeacefull";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/MapoPeacefullA.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
</style>
