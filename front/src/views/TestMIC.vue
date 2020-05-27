<template>
  <div>
    <input type="file" accept="audio/*">
    <video  autoplay playsinline ref="video" id="video" width="300" height="200"></video>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        video: {},
        mediaContraint: {
          video: true
        }
      }
    },
    methods: {
      testMic() {
        navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
          console.log(stream)
        }).catch(err => {
          console.log(err)
        })
      }
    },
    mounted() {
      this.testMic()
    }
  }
</script>