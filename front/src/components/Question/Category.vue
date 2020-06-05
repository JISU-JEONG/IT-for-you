<template>
  <div class="main-container">
    <div class="info">
      <h2>문제 풀기</h2>
      <p><small>이런저런 안내문구를 작성하겠습니다.</small></p>
      <p><small>카테고리, 난이도, 개수를 선택하세요.</small></p>
      <p><small>틀린문제는 자동으로 오답노트에 저장됩니다.</small></p>
    </div>
    <div style="margin-top:-60px">
      <div class="card">
        <div class="selected category flex flex-center flex-wrap no_highlights" style="cursor: pointer;" @click="onClickShow">
          <p v-if="selectedCategory.length === 0">카테고리를 선택해주세요</p>
          <transition-group name="badge" class="flex flex-center flex-wrap">
            <p v-for="c in selectedCategory" :key="c+1" class="badge" >{{c}}</p>
          </transition-group>
        </div>
      </div>
      <div class="card">
        <div class="selected difficulty">
          <p style="text-align: center; margin-bottom: 10px">난이도</p>
          <div class="flex flex-wrap number-box">
            <div class="difficulty-option" v-for="i in 5" :key="i">
              <input type="checkbox" name="difficulty" :value="i" :id="i" v-model="selectedDifficulty" >
              <label class="difficulty-btn flex flex-center flex-wrap no_highlights" :for="i"><span>{{i}}</span></label>
            </div>
          </div>
        </div>
      </div>
      <div class="card last-card">
        <input type="number" placeholder="문제 개수 입력(1~20)"  min="0" max="20" v-model="p_number" />
        <div class="submit-btn flex flex-center" @click="submitData">
          <span>문제풀러가자</span>
        </div>
      </div>
      <div class="default-info">
        <p>기본값</p>
        <p>카테고리 - 전체 선택</p>
        <p>난이도 - 전체 선택</p>
        <p>문제 개수 - 10개</p>
      </div>
      <div class="select-container">
        <div class="select-nav">
          <span>카테고리 선택</span>
          <div class="close-btn no_highlights" @click="onClickShow"></div>
        </div>
        <div class="select-content">
          <div class="category-option" v-for="c in questionCategory" :key="c" >
            <input type="checkbox" name="category" :value="c" :id="c" v-model="selectedCategory">
            <label class="flex flex-center flex-wrap no_highlights" style="cursor: pointer;" :for="c">{{c}}</label>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "@/api/api.service.js";

export default {
  name: "Category",
  data() {
    return {
      selectedCategory: [],
      selectedDifficulty: [],
      p_number: null,
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
    select() {
      if (event.target.nodeName === "SPAN") {
        event.target.classList.toggle("active");
      }
    },
    submitData() {
      this.questionData.pc_value = this.selectedCategory;
      this.questionData.pd_id = this.selectedDifficulty;
      this.questionData["p_number"] =
        (this.p_number === null || this.p_number < 1) ? 10 : this.p_number > 20 ? 20 : this.p_number*1;
      this.questionData.user_id = this.user_id
      axios
        .post("/api/problems/search/", this.questionData)
        .then(({ data }) => {
          console.log(data);
          this.$store.dispatch("questionList", data);
          this.$router.push("/detail");
        });
    },
    onClickShow() {
      document.querySelector(".select-container").classList.toggle("show");
    }
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
p {
  font-size: 20px;
}

.main-container {
  width: 100%;
  max-width: 500px;
  height: 100%;
  margin: 0 auto;
  position: relative;
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
.card {
  height: 150px;
  margin: 20px;
  position: relative;
  display: flex;
  background-color: white;
  box-shadow: 0 0 2rem 0 rgba(136, 152, 170, 0.15);
  border-radius: 5px;
}
.last-card {
  height: 100px;
}
.default-info {
  margin: 10px 30px;
}
.default-info p {
  font-size: 14px;
  color: #888;
}
.last-card input {
  outline: none;
  text-align: right;
  width: 70%;
  padding: 10px;
  font-size: 20px;
  border: 2px solid #3e4149;
  transition: border 1s linear;
}
.last-card input:placeholder-shown {
  border: 2px inset;
}
.submit-btn {
  width: 30%;
  color: white;
  cursor: pointer;
  background-color: #3e4149;
}
.selected {
  width: 100%;
  padding: 8px;
}
.setting {
  width: 20%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.select-container {
  /*밑에서 오가는거*/
  height: 450px;
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  border-radius: 20px 20px 0 0;
  background-color: rgba(var(--b3f, 250, 250, 250), 1);
  box-shadow: 0px -2px 4px lightgray;
  transform: translateY(450px);
  transition: all 0.3s ease;
  z-index: 1;
}
.select-nav {
  padding: 16px 20px;
  display: flex;
  justify-content: space-between;
  border-bottom: 2px solid rgb(209, 209, 209);
}
.select-content {
  padding: 12px;
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}
.category-option {
  width: 30%;
  margin: 3px;
}
.difficulty-option > input,
.category-option > input {
  display: none;
}
.difficulty-option > label {
  width: 50px;
  height: 50px;
  position: relative;
  border: 1.5px #333030 solid;
  border-radius: 100%;
  font-size: 20px;
  cursor: pointer;
  overflow: hidden;
}
.difficulty-option > label > span {
  transition: color 0.25s linear;
}
.difficulty-option > label::before {
  content: "";
  width: 100%;
  height: 0;
  position: absolute;
  left: 0;
  bottom: 0;
  transition: height 0.25s linear;
}
.difficulty-option:nth-child(1) > label {
  border-color: #5CAB7D;
}
.difficulty-option:nth-child(1) > label::before {
  background-color: #5cab7d;
}
.difficulty-option:nth-child(2) > label{
  border-color: #5A9367;
}
.difficulty-option:nth-child(2) > label::before {
  background-color: #5a9367;
}
.difficulty-option:nth-child(3) > label {
  border-color: #44633F;
}
.difficulty-option:nth-child(3) > label::before {
  background-color: #44633f;
}
.difficulty-option:nth-child(4) > label {
  border-color: #3F4B3B;
}
.difficulty-option:nth-child(4) > label::before {
  background-color: #3f4b3b;
}
.difficulty-option:nth-child(5) > label {
  border-color: rgb(43, 48, 42);
}
.difficulty-option:nth-child(5) > label::before {
  background-color: rgb(43, 48, 42);
}
.difficulty-option > input:checked + label > span {
  color: white;
  z-index: 1;
}
.difficulty-option > input:checked + label::before {
  height: 100%;
}
.category-option > input:checked + label {
  background-color: rgb(29, 29, 31);
  color: white;
}
.category-option > label {
  width: 100%;
  height: 60px;
  margin-bottom: 12px;
  border-radius: 10px;
  box-shadow: 4px 4px 8px #cbced1, -4px -4px 8px #ffffff;
  color: rgb(29, 29, 31);
  background-color: white;
  font-weight: bold;
  transition: all 0.2s;
}
.flex {
  display: flex;
}
.flex-center {
  justify-content: center;
  align-items: center;
}
.flex-wrap {
  flex-wrap: wrap;
}
.badge {
  padding: 4px;
  margin: 4px;
  color: white;
  background-color: #274c5e;
  border-radius: 5px;
}
.badge:nth-child(2n) {
  background-color: #7f9eb2;
}
.badge-enter-active,
.badge-leave-active {
  transition: all 0.3s;
}
.badge-enter,
.badge-leave-to {
  opacity: 0;
  transform: scale(0);
}
.number-box {
  justify-content: space-between;
  align-items: center;
  height: 70px;
}
.close-btn {
  display: inline-block;
  cursor: pointer;
  width: 21px;
  height: 21px;
  border-radius: 5px;
  background-image: url("../../assets/icons/close.png");
  background-color: rgb(29, 29, 31);
  background-repeat: no-repeat;
  background-size: cover;
}
.show {
  transform: translateY(0);
}
@font-face {
  font-family: "MapoPeacefull";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/MapoPeacefullA.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
</style>
