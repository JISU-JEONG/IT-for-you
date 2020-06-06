
<template>
  <div class="main">
    <p>문제를 씁니다.</p>
    <audio-recorder
      :upload-url="uploadurl"
      filename="interview" 
      format="wav"
      :attempts="1"
      :time="2"
      :before-recording="callback"
      :pause-recording="callback"
      :after-recording="callback"
      :select-record="callback"
      :before-upload="callback"
      :successful-upload="callback"
      :failed-upload="callback"
      :bit-rate="192"/>
  </div>
</template>

<script>
  import { API_URL } from "@/api/config";
  export default {
    name: 'app',
    data () {
      return {
        uploadurl : API_URL+"/api/interprobs/myinters/1/",
        headers: {
          'X-Custom-Header': 'some data'
        }
      }
    },
    methods: {
      callback (msg) {
        console.debug('Event: ', msg)
      },
    }
  }
</script>
<style scoped>
.main {
  width: 100%;
  max-width: 500px;
  margin:0 auto;
  height: 600px;
}
</style>