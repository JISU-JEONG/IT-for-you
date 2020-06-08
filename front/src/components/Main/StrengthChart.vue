<template>
  <div>
    <div class="content">
      <div class="info">
        <div class="title">
          나의 강점
        </div>

        <apexchart
          type="radar"
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
      series: [
        {
          name: "Series 1",
          data: this.seriesProps
        }
      ],

      chartOptions: {
        chart: {
          type: "radar",
          toolbar: {
            show: false
          }
        },
        yaxis: {
          show: false
        },
        xaxis: {
          categories: this.labelsProps
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
  box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.17);
  border-color: rgba(0, 0, 0, 0.05);
  flex-direction: column;
  display: flex;
  justify-content: center;
  align-items: center;
}

.title {
  margin-top: 20px;
}
</style>
