

<template>
  <div class="row">
    <audio-recorder
      :upload-url="uploadurl"
      filename="interview" 
      :attempts="3"
      :time="1"
      :show-download-button="false"
    />
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
