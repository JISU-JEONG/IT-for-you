<template>
  <div class="main-content">
    <div class="question-content" @click="select()">
      <h1>카테고리</h1>
      <div v-for="c in questionCategory" :key="c" class="category-contaienr">
        <span>{{c}}</span>
      </div>
      <h1>레벨</h1>
      <div v-for="l in 5" :key="l" class="level-contaienr">
        <span>{{l}}</span>
      </div>
    </div>
    <h1>문제갯수</h1>
    <div class="question-content-count">
      <input type="text" placeholder="1~50" v-model="p_number" />
    </div>
    <div class="send-button">
      <span @click="selectedData()">Send</span>
    </div>
  </div>
</template>

<script>
import axios from "@/api/api.service.js";

export default {
  name: "Category",
  data() {
    return {
      questionData: {},
      questionCategory: [],
      p_number: null
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
    selectedData() {
      const category = document.querySelectorAll(
        ".question-content .category-contaienr span"
      );
      const level = document.querySelectorAll(
        ".question-content .level-contaienr span"
      );

      this.questionData.pc_value = [...category].reduce((arr, v) => {
        if (v.classList.value === "active") {
          arr.push(v.innerText);
        }
        return arr;
      }, []);

      this.questionData.pd_id = [...level].reduce((arr, v) => {
        if (v.classList.value === "active") {
          arr.push(Number(v.innerText));
        }
        return arr;
      }, []);

      this.questionData["p_number"] =
        this.p_number === null ? 10 : Number(this.p_number);

      //   console.log(this.questionData);

      axios
        .post("/api/problems/search/", this.questionData)
        .then(({ data }) => {
          console.log(data);
          this.$store.dispatch("questionList", data);
          this.$router.push("/detail");
        });
    }
  },
  beforeMount() {
    this.init();
  }
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}
.main-content {
  width: 100vw;
  height: 100vh;
  margin: 0 auto;
}

.question-content {
  width: 100%;
}

.send-button {
  margin: 50px;
}

.send-button {
  margin-top: 70px;
}

.category-contaienr,
.level-contaienr {
  display: inline-block;
  width: 50%;
  padding: 10px;
}

.category-contaienr > span,
.level-contaienr > span {
  display: inline-block;
  width: 100%;
  text-align: center;
  border: 1px black solid;
  border-radius: 10px;
  padding: 10px;
}

input {
  text-align: center;

  height: 50px;
}
.active {
  background-color: gold;
}
</style>