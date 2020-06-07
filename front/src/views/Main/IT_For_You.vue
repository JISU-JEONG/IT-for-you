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
  background-color: #f0f2f5;
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
  height: 50%;
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

.circle-content {
  width: 100px;
  height: 100px;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

.circle {
  opacity: 0;
  border: solid 1px black;
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  border-radius: 50%;
  animation: pulse 2.7s;
  animation-iteration-count: infinite;
}

.circle:nth-child(2) {
  animation-delay: 0.9s;
}

.circle:nth-child(3) {
  animation-delay: 1.8s;
}

@keyframes pulse {
  0% {
    transform: scale(1);
    opacity: 0.2;
    transform-origin: center;
  }
  100% {
    opacity: 0;
    transform: scale(1.5);
    transform-origin: center;
  }
}

@font-face {
  font-family: "MapoPeacefull";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/MapoPeacefullA.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
</style>
