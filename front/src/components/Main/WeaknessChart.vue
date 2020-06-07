<template>
  <div>
    <div class="content">
      <div class="info">
        <apexchart
          type="pie"
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
      series: [25, 28, 44, 55, 45],
      chartOptions: {
        chart: {
          width: "100%",
          type: "pie"
        },
        labels: ["Database", "Javascript", "OS", "Java", "Python"],
        theme: {
          monochrome: {
            // enabled: true
          }
        },
        plotOptions: {
          pie: {
            dataLabels: {
              offset: -5
            }
          }
        },
        title: {
          text: "내가 많이 틀리는 문제"
        },
        dataLabels: {
          formatter(val, opts) {
            const name = opts.w.globals.labels[opts.seriesIndex];
            return [name, val.toFixed(1) + "%"];
          }
        },
        legend: {
          show: false
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
