<template>
  <div class="main-container">
    <div class="content">
      <div class="card">
        <div class="info">
          <div class="name">오늘 맞춘 문제</div>
          <div class="count">{{ nowCorrectProb }}</div>
        </div>
      </div>
      <div class="card">
        <div class="info">
          <div class="name">오늘 틀린 문제</div>
          <div class="count">{{ nowWrongProb }}</div>
        </div>
      </div>
    </div>
    <div class="chart">
      <WeeknessChart
        class="WeeknessChart"
        :labelsProps="wrongLabelsProps"
        :seriesProps="wrongSeriesProps"
        v-if="WeeknessChartFlag && WeeknessCarousel"
      />
      <StrengthChart
        class="StrengthChart"
        :labelsProps="correctLabelsProps"
        :seriesProps="correctSeriesProps"
        v-if="StrengthChartFlag && StrengthCarousel"
      />
      <span class="prev" @click="prev()">
        &#60;
      </span>
      <span class="next" @click="next()">
        &#62;
      </span>
    </div>

    <YoutubeList
      :YoutubeList="YoutubeList"
      :ListFlag="ListFlag"
      v-if="youtubeListFlag"
    />
  </div>
</template>

<script>
import WeeknessChart from "@/components/Main/WeaknessChart.vue";
import StrengthChart from "@/components/Main/StrengthChart.vue";
import YoutubeList from "@/components/Main/YoutubeList.vue";

import axios from "@/api/api.service.js";

export default {
  name: "IT_For_You",
  components: {
    WeeknessChart,
    StrengthChart,
    YoutubeList
  },
  data() {
    return {
      WeeknessChartFlag: false,
      StrengthChartFlag: false,
      WeeknessCarousel: true,
      StrengthCarousel: false,

      wrongSeriesProps: [],
      wrongLabelsProps: [],
      correctSeriesProps: [],
      correctLabelsProps: [],

      nowCorrectProb: 0,
      nowWrongProb: 0,

      YoutubeList: [],
      youtubeListFlag: false,
      ListFlag: new Array(5).fill(false),
      path: [
        "https://www.youtube.com/embed/lJES5TQTTWE",
        "https://www.youtube.com/embed/q3_WXP9pPUQ",
        "https://www.youtube.com/embed/iyFHfzCRHA8",
        "https://www.youtube.com/embed/hhd8uUPO3-0",
        "https://www.youtube.com/embed/eprXmC_j9A4",
        "https://www.youtube.com/embed/srQR0Qb7Joo",
        "https://www.youtube.com/embed/NMdnzvPsGu8",
        "https://www.youtube.com/embed/HsJ4oy_jBx0",
        "https://www.youtube.com/embed/EkWI6Ru8lFQ",
        "https://www.youtube.com/embed/iOueE9AXDQQ",
        "https://www.youtube.com/embed/jVG5jvOzu9Y",
        "https://www.youtube.com/embed/tPjpcsgxgWc",
        "https://www.youtube.com/embed/u65F4ECaKaY",
        "https://www.youtube.com/embed/IH7mUwunzlo",
        "https://www.youtube.com/embed/OpoVuwxGRDI",
        "https://www.youtube.com/embed/R0YJ-r-qLNE",
        "https://www.youtube.com/embed/iks_Xb9DtTM",
        "https://www.youtube.com/embed/m0icCqHY39U",
        "https://www.youtube.com/embed/CaXQNfYAdHs",
        "https://www.youtube.com/embed/AERY1ZGoYc8",
        "https://www.youtube.com/embed/iks_Xb9DtTM",
        "https://www.youtube.com/embed/3hxT4cSm03s",
        "https://www.youtube.com/embed/ODa9mY2bEEc"
      ]
    };
  },
  methods: {
    async init() {
      const date = new Date();
      const year = date.getFullYear();
      let month = new String(date.getMonth() + 1);
      let day = new String(date.getDate());

      // 한자리수일 경우 0을 채워준다.
      if (month.length == 1) {
        month = "0" + month;
      }
      if (day.length == 1) {
        day = "0" + day;
      }

      const now = year + "-" + month + "-" + day;

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
          let userWrongProb = [];
          let userCorrectProb = [];

          data.forEach(v => {
            if (v.correct === true) {
              userCorrectProb.push(v.p_cate.pc_value);
              if (v.date === now) {
                this.nowCorrectProb += 1;
              }
            } else {
              if (v.date === now) {
                this.nowWrongProb += 1;
              }

              userWrongProb.push(v.p_cate.pc_value);
            }
          });

          let categoryWrongCount = {};
          let categoryCorrentCount = {};

          userWrongProb.forEach(v => {
            categoryWrongCount[v] = categoryWrongCount[v] + 1 || 1;
          });
          userCorrectProb.forEach(v => {
            categoryCorrentCount[v] = categoryCorrentCount[v] + 1 || 1;
          });

          this.wrongSeriesProps = Object.values(categoryWrongCount);
          this.wrongLabelsProps = Object.keys(categoryWrongCount);

          const size = userCorrectProb.length;
          Object.values(categoryCorrentCount).forEach(v => {
            this.correctSeriesProps.push((v / size) * 100);
          });

          this.correctLabelsProps = Object.keys(categoryCorrentCount);
          this.WeeknessChartFlag = true;
          this.StrengthChartFlag = true;
        });
    },

    next() {
      if (event.target.style.color === "gray") {
        return;
      }

      this.WeeknessCarousel = !this.WeeknessCarousel;
      this.StrengthCarousel = !this.StrengthCarousel;
      if (this.WeeknessCarousel) {
        const span1 = document.querySelector(".prev");
        const span2 = document.querySelector(".next");

        span1.style.color = "gray";
        span2.style.color = "black";
      } else {
        const span1 = document.querySelector(".next");
        const span2 = document.querySelector(".prev");

        span1.style.color = "gray";
        span2.style.color = "black";
      }
    },

    prev() {
      if (event.target.style.color === "gray") {
        return;
      }

      this.WeeknessCarousel = !this.WeeknessCarousel;
      this.StrengthCarousel = !this.StrengthCarousel;
      if (this.WeeknessCarousel) {
        const span1 = document.querySelector(".prev");
        const span2 = document.querySelector(".next");

        span1.style.color = "gray";
        span2.style.color = "black";
      } else {
        const span1 = document.querySelector(".perv");
        const span2 = document.querySelector(".next");

        span1.style.color = "black";
        span2.style.color = "gray";
      }
    },

    random(i) {},

    flag() {},

    getYoutubeList() {
      this.ListFlag[0] = true;

      for (let i = 0; i < 6; i++) {
        if (i === 5) {
          this.youtubeListFlag = true;
        } else {
          let item = this.path[[Math.floor(Math.random() * this.path.length)]];
          if (this.YoutubeList[i] === undefined) {
            this.YoutubeList[i] = item;
          } else {
            i--;
          }
        }
      }
    }
  },

  created() {
    this.getYoutubeList();
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

.chart {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 320px;
  position: relative;
}

.WeeknessChart,
.StrengthChart,
.next,
.prev {
  position: absolute;
}

.prev {
  left: 0;
  color: gray;
  margin-left: 25px;
  font-size: 30px;
  cursor: pointer;
}

.next {
  right: 0;
  margin-right: 25px;
  font-size: 30px;
  cursor: pointer;
}

@font-face {
  font-family: "MapoPeacefull";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/MapoPeacefullA.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
</style>
