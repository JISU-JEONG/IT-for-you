<template>
  <div class="main-container">
    <div class="content">
      <div class="card">
        <div class="info">
          <div class="name">오늘 맞춘 문제</div>
          <div class="count">18</div>
        </div>
      </div>
      <div class="card">
        <div class="info">
          <div class="name">오늘 틀린 문제</div>
          <div class="count">2</div>
        </div>
      </div>
    </div>
    <Slider />
    <WeeknessChart
      :labelsProps="wrongLabelsProps"
      :seriesProps="wrongSeriesProps"
      v-if="WeeknessChartFlag"
    />
    <StrengthChart
      :labelsProps="correctLabelsProps"
      :seriesProps="correctSeriesProps"
      v-if="StrengthChartFlag"
    />
  </div>
</template>

<script>
import WeeknessChart from "@/components/Main/WeaknessChart.vue";
import StrengthChart from "@/components/Main/StrengthChart.vue";
import Slider from "@/components/Main/Slider.vue";
import axios from "@/api/api.service.js";

export default {
  name: "IT_For_You",
  components: {
    WeeknessChart,
    StrengthChart,
    Slider
  },
  data() {
    return {
      WeeknessChartFlag: false,
      StrengthChartFlag: false,
      wrongSeriesProps: [],
      wrongLabelsProps: [],
      correctSeriesProps: [],
      correctLabelsProps: []
    };
  },
  methods: {
    async init() {
      const user_id = this.$store.state["auth"]["userInfo"]["id"];
      const token = this.$session.get("jwt");
      await axios
        .get("/api/accounts/userprob/", {
          params: {
            user_id: user_id
          },
          headers: {
            Authorization: `JWT ${token}` // JWT 다음에 공백있음.
          }
        })
        .then(({ data }) => {
          console.log(data);
          let userProb = [];
          let userWrongProb = [];
          let userCorrectProb = [];

          data.forEach(v => {
            userProb.push(v.p_cate.pc_value);
            if (v.correct === true) {
              userCorrectProb.push(v.p_cate.pc_value);
            } else {
              userWrongProb.push(v.p_cate.pc_value);
            }
          });

          let categoryCount = {};
          let categoryWrongCount = {};
          let categoryCorrentCount = {};

          userProb.forEach(v => {
            categoryCount[v] = categoryCount[v] + 1 || 1;
          });
          userWrongProb.forEach(v => {
            categoryWrongCount[v] = categoryWrongCount[v] + 1 || 1;
          });
          userCorrectProb.forEach(v => {
            categoryCorrentCount[v] = categoryCorrentCount[v] + 1 || 1;
          });

          this.wrongSeriesProps = Object.values(categoryWrongCount);
          this.wrongLabelsProps = Object.keys(categoryWrongCount);

          // console.log(userWrongProb);
          // console.log("wrongSeriesProps", this.wrongSeriesProps);
          // console.log("wrongLabelsProps", this.wrongLabelsProps);

          // console.log("userProb : ", userProb);
          // console.log("userWrongProb : ", userWrongProb);
          // console.log("userCorrectProb : ", userCorrectProb);

          // console.log("categoryCount", categoryCount);
          // console.log("categoryWrongCount", categoryWrongCount);
          // console.log("categoryCorrentCount", categoryCorrentCount);

          // console.log(Object.values(categoryWrongCount));
          // console.log(Object.keys(categoryWrongCount));

          const size = userCorrectProb.length;
          Object.values(categoryCorrentCount).forEach(v => {
            this.correctSeriesProps.push((v / size) * 100);
          });

          this.correctLabelsProps = Object.keys(categoryCorrentCount);

          console.log("userCorrectProb", userCorrectProb);
          console.log("categoryCorrentCount", categoryCorrentCount);
          console.log("correctSeriesProps", this.correctSeriesProps);
          console.log("correctLabelsProps", this.correctLabelsProps);

          this.WeeknessChartFlag = true;
          this.StrengthChartFlag = true;
        });
    }
  },

  created() {
    this.init();
  }
};
</script>

<style scoped lang="scss">
* {
  box-sizing: border-box;
  font-family: MapoPeacefull;
}

.main-container {
  width: 100%;
  height: 100%;
  max-width: 500px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.content {
  width: 100%;
  padding: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.card {
  display: inline-block;
  width: 50%;
  height: 120px;
  padding: 10px;
}

.info {
  width: 100%;
  height: 100%;
  border: solid 1px black;
  background: "#fff";
  box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.17);
  border-color: rgba(0, 0, 0, 0.05);
  flex-direction: column;
  display: flex;
  justify-content: center;
  align-items: center;
}

.name,
.count {
  margin: 10px;
}

@font-face {
  font-family: "MapoPeacefull";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/MapoPeacefullA.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
</style>
