<style lang="scss">
  @import '../scss/icons';
</style>

<template>
  <div class="uploader-wrapper" @click="upload">
    <icon-button name="save" class="ar-icon ar-icon__xs ar-icon--no-border" />
    <span> 녹음파일->대본 </span>
  </div>
</template>

<script>
  import IconButton from './icon-button'
  import UploaderPropsMixin from '@/mixins/uploader-props'
  // import axios from 'axios'
  import axios from '../api/api.service.js'
import router from '../router'
  export default {
    mixins: [UploaderPropsMixin],
    props: {
      record: { type: Object }
    },
    components: {
      IconButton
    },
    methods: {
      upload () {
        console.log('기은이 테스트')
        if (!this.record.url) {
          return
        }
        this.$eventBus.$emit('start-upload')
        this.$session.start()
        const token = this.$session.get('jwt')
        const data = new FormData()
        data.append('audio', this.record.blob, `${this.filename}.mp3`)
        console.log('기은이 테스트2')
        const headers = Object.assign(this.headers, {})
        headers['Content-Type'] = `multipart/form-data; boundary=${data._boundary}`
        headers['Authorization'] = `JWT ${token}`
        console.log(headers)
        axios.post('/api/interprobs/record/', data, { headers: headers }).then(resp => {
          this.$eventBus.$emit('end-upload', { status: 'success', response: resp })
          console.log(resp)
          this.$store.commit('setInterviewResult', resp.data.content)
        }).catch(error => {
          this.$eventBus.$emit('end-upload', { status: 'fail', response: error })
        })
      }
    }
  }
</script>
