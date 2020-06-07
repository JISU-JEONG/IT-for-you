<template>
  <div>
    <div class="content">
      <div class="info">
        <apexchart
          type="radar"
          height="300"
          :options="chartOptions"
          :series="series"
        ></apexchart>
      </div>
    </div>
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";

export default {
  name: "WeaknessChart",
  components: {
    apexchart: VueApexCharts
  },
  data() {
    return {
      series: [
        {
          name: "Series 1",
          data: [80, 50, 30, 40, 100, 20]
        }
      ],

      chartOptions: {
        chart: {
          height: 350,
          type: "radar"
        },
        title: {
          text: "나의 역량"
        },
        yaxis: {
          show: false
        },
        xaxis: {
          categories: [
            "Database",
            "Javascript",
            "OS",
            "Java",
            "Python",
            "Algorithm"
          ]
        }
      }
    };
  }
};
</script>

<style scoped>
.content {
  width: 100%;
  padding: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
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
</style>
