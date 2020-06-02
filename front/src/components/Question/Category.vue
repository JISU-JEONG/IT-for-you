<template>
  <div class="main-container">
    <div class="info">
      <h2>문제 풀기</h2>
      이런저런 안내문구를 작성하겠습니다.
      카테고리, 난이도, 개수를 선택하세요.
    </div>
    <div style="margin-top:-60px">
      <div class="card">
        <div class="selected category flex-center" @click="onClickShow">
          <p v-if="selectedCategory.length === 0">카테고리을 선택해주세요</p>
          <p v-else v-for="c in selectedCategory" :key="c+1">{{c}}</p>
        </div>
        <!-- <div class="setting">
          <button @click="onClickShow" class="btn">열려라</button>
        </div> -->
      </div>
      <div class="card">
        <div class="selected difficulty">
          <p>난이도</p>
        </div>
        <div class="setting">
          <button @click="onClickShow">열려라</button>
        </div>
      </div>
      <div class="card">
        <div class="selected difficulty">
          <p>난이도</p>
        </div>
        <input type="number" placeholder="1~50" v-model="p_number" />
      </div>
      <div class="select-container">
        <div class="select-nav">
          <span>카테고리 선택</span>
          <span>X</span>
        </div>
        <div class="select-content" @click="onClickCategory">
          <div v-for="c in questionCategory" :key="c" class="category-option ">
            <input type="checkbox" name="category" :value="c" :id="c" v-model="selectedCategory">
            <label :for="c">{{c}}</label>
          </div>
        </div>
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
      selectedCategory: [],
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
    },
    onClickCategory() {
      console.log(this.selectedCategory)
    },
    onClickShow() {
      document.querySelector('.select-container').classList.toggle('show')
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
  font-family: MapoPeacefull;
  
}
p {
  font-size: 20px;
}
.main-container {
  width: 100%;
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
.card {
  min-height: 150px;
  margin: 20px;
  position: relative;
  display: flex;
  background-color: white;
  box-shadow: 0 0 2rem 0 rgba(136, 152, 170, 0.15);
  border-radius: 5px;
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
.select-container { /*밑에서 오가는거*/
  height: 450px;
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(var(--b3f,250,250,250),1);
  transform: translateY(450px);
  transition: all 0.3s ease;
  border-top: 1px solid #888;
}
.select-nav {
  padding: 16px;
  display: flex;
  justify-content: space-between;
  border-bottom: 1px solid #888;
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
.category-option > input {
  display: none;
}
.category-option > input:checked+label {
  background-color: rgb(29, 29, 31);
  color: white;
}
.category-option > label{
  width: 100%;
  height: 60px;
  margin-bottom: 12px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  box-shadow: 4px 4px 8px #cbced1,
                  -4px -4px 8px #ffffff;
  color: rgb(29, 29, 31);
  background-color: white;
  font-weight: bold;
  transition: all 0.2s;
}
.flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}
.btn {
  
}
.show {
  transform: translateY(0);
}
/* .categoty-container {
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
} */

@font-face { font-family: 'MapoPeacefull'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/MapoPeacefullA.woff') format('woff'); font-weight: normal; font-style: normal; }
</style>