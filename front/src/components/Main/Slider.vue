<template>
  <div class="slider-content"></div>
</template>

<script>
import axios from "@/api/api.service.js";

export default {
  name: "Slider",
  data() {
    return {};
  },
  methods: {}
};
</script>

<style scoped lang="scss">
* {
  max-width: 500px;
}

.slider-content {
  width: 100%;
  height: 150px;
}
.chart1 {
  height: 100px;
  width: 100px;
  background-color: blue;
}
.chart2 {
  height: 100px;
  width: 100px;
  background-color: red;
}

.arrow-left {
  left: 20px;
  border-bottom: 6px solid #ffffff;
  border-left: 6px solid #ffffff;
  transform: rotate(45deg);
  transition: left 0.5s;
  &:hover {
    left: 15px;
  }
}
.arrow-right {
  right: 20px;
  border-bottom: 6px solid #ffffff;
  border-right: 6px solid #ffffff;
  transform: rotate(-45deg);
  transition: right 0.5s;
  &:hover {
    right: 15px;
  }
}
</style>
