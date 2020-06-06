<style lang="scss">
  @import '../scss/icons';
</style>

<template>
  <div class="downloader-wrapper" @click="download">
    <icon-button
      id="download"
      class="ar-icon ar-icon__xs ar-icon--no-border"
      name="download"/>
      <span> 녹음파일 저장 </span>
  </div>
</template>

<script>
  import IconButton from './icon-button'

  export default {
    props: {
      record    : { type: Object },
      filename  : { type: String }
    },
    components: {
      IconButton
    },
    methods: {
      download () {
        console.log('다운로드')
        if (!this.record.url) {
          return
        }
        const type = this.record.blob.type.split('/')[1]
        const link = document.createElement('a')
        link.href = this.record.url
        link.download = `${this.filename}.${type}`
        link.click()
      }
    }
  }
</script>
