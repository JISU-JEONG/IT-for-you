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
    <WeeknessChart />
    <StrengthChart />
  </div>
</template>

<script>
import WeeknessChart from "@/components/Main/WeaknessChart.vue";
import StrengthChart from "@/components/Main/StrengthChart.vue";

export default {
  name: "IT_For_You",
  components: {
    WeeknessChart,
    StrengthChart
  },
  data() {
    return {};
  }
};

// 추가
/*
문제번호
문제타입
문제카테고리
문제맞춤여부
날짜
*/

// 조회
/*
날짜
*/
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
