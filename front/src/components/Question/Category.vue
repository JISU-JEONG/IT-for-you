<template>
  <div class="main-container">
    <div class="categoty-container">
      <h3>카테고리 선택</h3>
      <hr>
      <div v-for="c in questionCategory" :key="c" class="category">
        <span>{{c}}</span>
      </div>      
    </div>
  </div>
  <!-- <div class="main-content">
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
      <input type="number" placeholder="1~50" v-model="p_number" />
    </div>
    <div class="send-button">
      <span @click="selectedData()">문제 풀러가기</span>
    </div>
  </div> -->
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
        ".question-content .category span"
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

.main-container {
  width: 100%;
  margin: 0 auto;
  padding: 12px;
}
.categoty-container {
  width:100%;
  padding: 12px;
  border: 1px solid black;
  border-radius: 5px;
}




.question-content,
.question-content-count {
  width: 100%;
}

.question-content-count,
.send-button {
  display: flex;
  justify-content: center;
}

.category,
.level-contaienr {
  display: inline-block;
  width: 50%;
  padding: 10px;
}

.category > span,
.level-contaienr > span {
  display: inline-block;
  width: 100%;
  text-align: center;
  border: 1px black solid;
  border-radius: 10px;
  padding: 10px;
}

.active,
.send-button:hover {
  background-color: black;
  color: white;
}

input {
  height: 50px;
  text-align: center;
}

h1 {
  margin-top: 30px;
  text-align: center;
}

h1,
input,
.question-content span {
  font-family: "Recipekorea";
}

.send-button {
  font-family: "Openas";
  border: 5px black solid;
  border-radius: 50px;
  font-size: 2rem;
  padding: 15px;
  margin: 50px;
}

@font-face {
  font-family: "Recipekorea";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/Recipekorea.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: "CookieRunOTF-Black";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_twelve@1.0/CookieRunOTF-Black00.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: "Openas";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_nine_@1.1/Openas.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
</style>