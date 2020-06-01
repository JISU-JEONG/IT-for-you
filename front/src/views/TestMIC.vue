

<template>
  <div class="row">
    <audio-recorder
      :upload-url="uploadurl"
      filename="interview" 
      format="wav"
      :attempts="3"
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
        mp3: '/demo/example.mp3',
        uploadurl : API_URL+"/api/accounts/voice/",
        showRecorder: true,
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
