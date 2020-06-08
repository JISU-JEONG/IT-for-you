<template>
  <div>
    <div class="content">
      <div class="info">
        <div class="title">
          내가 많이 틀리는 문제
        </div>
        <apexchart
          type="pie"
          height="230px"
          :options="chartOptions"
          :series="series"
        ></apexchart>
      </div>
    </div>
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";
import axios from "@/api/api.service.js";

export default {
  name: "WeaknessChart",
  components: {
    apexchart: VueApexCharts
  },
  props: {
    seriesProps: {
      type: Array
    },
    labelsProps: {
      type: Array
    }
  },

  data() {
    return {
      series: this.seriesProps,
      chartOptions: {
        chart: {
          width: "100%",
          type: "pie"
        },
        labels: this.labelsProps,
        plotOptions: {
          pie: {
            dataLabels: {
              offset: -5
            }
          }
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
* {
  font-family: MapoPeacefull;
}

.content {
  width: 100%;
  padding: 20px;
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

.title {
  margin-top: 20px;
  margin-bottom: 10px;
}

@font-face {
  font-family: "MapoPeacefull";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/MapoPeacefullA.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
</style>
