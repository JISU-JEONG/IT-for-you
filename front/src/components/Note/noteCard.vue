<template>
  <div>
    <transition-group class="content__list">
      <div
        class="card-content"
        v-for="(question, i) in myNoteList"
        :key="question.problems.p_id"
      >
        <div class="card">
          <!-- 카드 헤더 -->
          <div class="card-header">
            <span class="info-badge">{{
              questionType[question.problems.pt_id]
            }}</span>
            <span class="info-badge">{{
              questionCategory[question.problems.pc_id]
            }}</span>
            <span class="info-badge">{{ level[question.problems.pd_id] }}</span>

            <span @click="deleteMynote(question.id)" class="close">&#215;</span>
          </div>

          <hr />
          <!--  카드 바디 -->
          <div class="card-body">
            <!-- 질문 -->
            <div class="card-body-header">
              {{ question.problems.p_question }}
            </div>

            <!-- 코드 -->
            <div
              class="card-body-header-code"
              v-if="question.problems.p_code !== null"
            >
              {{ question.problems.p_code }}
            </div>

            <!-- 문제 -->
            <div class="card-body-problem">
              <div v-if="question.problems.pt_id === 2">
                <div v-for="a in question.answers" :key="a.a_id">
                  <label class="label">
                    {{ a.a_value }}
                  </label>
                </div>
              </div>

              <div v-if="question.problems.pt_id === 3">
                <div class="ox-container">
                  <label
                    class="label"
                    v-for="a in question.answers"
                    :key="a.a_id"
                    >{{ a.a_value }}</label
                  >
                </div>
              </div>
            </div>

            <!-- 정답 / 해설 버튼 -->
            <div class="card-trigger">
              <span>
                <figure @click="getAnswer(i)">
                  <img src="../../assets/icons/current.png" />
                  <figcaption>정답</figcaption>
                </figure>
              </span>
              <span>
                <figure @click="getTip(i)">
                  <img src="../../assets/icons/tip.png" />
                  <figcaption>해설</figcaption>
                </figure>
              </span>
            </div>

            <!-- 정답 / 해설 내용 -->
            <div class="question-content">
              <div class="card-body-body-right" v-if="answerFlag[i]">
                {{ question.answer_list[0] }}
              </div>

              <div class="card-body-body-tip" v-if="tipFlag[i]">
                {{ question.problems.p_commentary }}
              </div>
              <div class="tip">{{ question.problems.p_commentary }}</div>
              <div class="answer">{{ question.answer_list }}</div>
            </div>
          </div>
        </div>
      </div>
    </transition-group>
  </div>
</template>

<script>
import axios from "@/api/api.service.js";

export default {
  name: "noteCard",
  data() {
    return {
      tipFlag: null,
      answerFlag: null,
      tmpheight: null,
      myNoteList: null
    };
  },
  created() {
    this.myNoteList = this.list;
  },
  props: {
    list: {
      type: Array
    },
    questionType: {
      type: Array
    },
    questionCategory: {
      type: Array
    },
    level: {
      type: Array
    }
  },
  watch: {
    list() {
      this.myNoteList = this.list;
      this.tipFlag = [...this.list].fill(false);
      this.answerFlag = [...this.list].fill(false);
      this.tmpheight = [...this.list].fill(false);

      const div = document.querySelectorAll(".question-content");
      div.forEach(v => {
        v.style.height = 0;
      });
    }
  },
  methods: {
    deleteMynote(p_id) {
      const del = confirm("정말 삭제하시겠습니까?");
      if (del) {
        const user_id = this.$store.state["auth"]["userInfo"]["id"];
        axios
          .delete(`/api/myprobs/myprob/${user_id}/${p_id}`)
          .then(res => {
            this.myNoteList.splice(
              this.myNoteList.findIndex(q => q.id === p_id * 1),
              1
            );
            this.$emit("deleteMynote", this.myNoteList);
          })
          .catch(err => console.error(err));
      }
    },

    getStyle(name, num, i) {
      const div3 = document.querySelector(name);
      div3.style.opacity = num;
    },

    getTip(i) {
      this.$set(this.tipFlag, i, !this.tipFlag[i]);
      const div = document.querySelectorAll(".question-content")[i];
      const div2 = document.querySelectorAll(".tip")[i];
      if (this.tipFlag[i] === true) {
        this.tmpheight[i] += div2.clientHeight;
        div.style.height = `${this.tmpheight[i]}px`;
        this.$nextTick(() => {
          this.getStyle(".card-body-body-tip", 1, i);
        });
      } else {
        this.tmpheight[i] -= div2.clientHeight;
        div.style.height = `${this.tmpheight[i]}px`;
      }
    },
    getAnswer(i) {
      this.$set(this.answerFlag, i, !this.answerFlag[i]);
      const div = document.querySelectorAll(".question-content")[i];
      const div2 = document.querySelectorAll(".answer")[i];
      if (this.answerFlag[i] === true) {
        this.tmpheight[i] += div2.clientHeight;
        div.style.height = `${this.tmpheight[i]}px`;
        this.$nextTick(() => {
          this.getStyle(".card-body-body-right", 1, i);
        });
      } else {
        this.tmpheight[i] -= div2.clientHeight;
        div.style.height = `${this.tmpheight[i]}px`;
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.card-content {
  width: 100%;
  padding: 30px;
}

@media (min-width: 612px) {
  .card-content {
    width: 100%;
    padding: 30px 50px;
  }
}

.card {
  width: 100%;
  height: 100%;
  padding: 10px;
  border-radius: 15px;
  display: inline-block;
  position: relative;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  overflow: hidden;
}

.card-header {
  width: 100%;
  height: 40px;
}

.card-body-header {
  font-weight: bold;
  line-height: 25px;
  font-size: 15px;
  padding: 10px;
}

.card-body-header-code {
  border: 2px solid black;
  padding: 12px;
  border-radius: 5px;
  background-color: rgb(235, 235, 235);
}

.card-body-body-right,
.card-body-body-tip {
  line-height: 20px;
  font-size: 17px;
  padding: 10px;
  opacity: 0;
  transition: all 2s;
  font-weight: bold;
}

.question-content {
  height: 0px;
  transition: all 0.5s;
}

.card-trigger {
  font-weight: bold;
  display: flex;
  justify-content: space-between;
  margin: 10px;
  padding: 15px;
  border-radius: 15px;
}

.tip,
.answer,
.userAnswer {
  line-height: 20px;
  font-size: 17px;
  padding: 10px;
  position: absolute;
  visibility: hidden;
}

.info-badge {
  padding: 6px;
  font-size: 15px;
  border-radius: 5px;
  color: white;
  font-family: Openas;
  margin-right: 6px;
  background-color: #17a2b8;
  float: left;
}

.close {
  float: right;
  padding-right: 10px;
  font-size: 28px;
  content: "\00d7";
}

.label {
  width: 100%;
  padding: 12px 8px;
  margin: 16px 0px;
  display: inline-block;
  position: relative;
  border-radius: 5px;
  box-shadow: 0 0 8px lightgray;
  cursor: pointer;
  overflow: hidden;
  user-select: none;
}
.label::before {
  width: 0;
  height: 100%;
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  background-color: rgba(33, 149, 243, 0.25);
  transform: translate(-50%, -50%);
  transition: all 0.5s;
}

.ox-container {
  display: flex;
  justify-content: space-around;
}

.ox-container .label {
  width: 120px;
  height: 120px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 40px;
  font-weight: bold;
  color: #888;
  user-select: none;
}

img {
  width: 50px;
  height: 50px;
}

figure {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
figcaption {
  margin-top: 15px;
}

@font-face {
  font-family: "Openas";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_nine_@1.1/Openas.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
</style>
