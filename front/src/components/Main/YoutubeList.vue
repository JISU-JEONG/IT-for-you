<template>
  <div class="content">
    <div class="youtube-content">
      <div clsss="title" style="text-align:center;">
        오늘의 추천영상
      </div>
      <div class="youtube-wrapper">
        <div class="youtube" v-for="(p, i) in path" :key="i">
          <iframe
            :src="p"
            frameborder="0"
            allowfullscreen
            v-if="i === index"
          ></iframe>
        </div>
      </div>
      <div class="button" style="text-align:center;">
        <span v-for="(list, i) in ListFlag" :key="i">
          <i
            class="silde-button active fas fa-circle"
            v-if="list"
            @click="click(i)"
          ></i>
          <i class="silde-button far fa-circle" v-else @click="click(i)"></i>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "YoutubeList",
  data() {
    return {
      path: [
        "https://www.youtube.com/embed/lJES5TQTTWE",
        "https://www.youtube.com/embed/q3_WXP9pPUQ",
        "https://www.youtube.com/embed/iyFHfzCRHA8",
        "https://www.youtube.com/embed/hhd8uUPO3-0",
        "https://www.youtube.com/embed/eprXmC_j9A4"
      ],
      ListFlag: new Array(5).fill(false),
      index: 0
    };
  },
  beforeMount() {
    this.ListFlag[0] = true;
  },
  methods: {
    click(i) {
      this.ListFlag[this.index] = false;
      this.ListFlag[i] = true;

      const active = document.querySelector(".active");
      active.classList.remove("active");
      active.classList.remove("fas");
      active.classList.remove("z-index");
      active.classList.add("far");

      const now = event.target;
      now.classList.remove("far");
      now.classList.add("active");
      now.classList.add("fas");
      now.classList.add("z-index");
      this.index = i;

      console.log(this.ListFlag);
    }
  }
};
</script>

<style scoped>
.content {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.youtube-content {
  position: relative;
  height: 230px;
  width: 100%;
}

@media (min-width: 400px) {
  .youtube-content {
    height: 250px;
  }
}

@media (min-width: 450px) {
  .youtube-content {
    height: 300px;
  }
}

.youtube-wrapper {
  display: inline-block;
  position: relative;
  width: 100%;
  height: 100%;
}

.youtube {
  position: absolute;
  width: 100%;
  padding-top: 10px;
  padding-bottom: 56.25%;
  margin: 10px 0px;
}

.youtube iframe {
  position: absolute;
  width: 100%;
  height: 100%;
  z-index: 1;
}

.silde-button {
  margin: 10px;
  cursor: pointer;
}
.z-index {
  z-index: 1;
}
</style>
