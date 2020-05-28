<template>
  <div>
    <audio-recorder
    upload-url="YOUR_API_URL"
    :attempts="3"
    :time="2"
    :headers="headers"
    :before-recording="callback"
    :pause-recording="callback"
    :after-recording="callback"
    :select-record="callback"
    :before-upload="callback"
    :successful-upload="callback"
    :failed-upload="callback"/>
  </div>
</template>
<script>
  

  export default {
    data() {
      return {  
        headers:{}
      }
    },
    methods: {
      callback (data) {
        console.debug(data)
      }
    },
    mounted() {

    }
  }
</script>