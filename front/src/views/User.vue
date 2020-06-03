<template>
  <div class="main-container">
    <div class="card" v-for="user in userList" :key="user.id">
      <span class="delete-user" @click="deleteUSer(user.id)">탈퇴</span>
      <hr style="clear:both">
      <div class="user-info">
        <p>아이디</p>
        <p>{{user.username}}</p>
        <p>이메일</p>
        <p>{{user.email}}s</p>
      </div>
    </div>
  </div>
</template>
<script>
import axios from '@/api/api.service.js'

export default {
  data() {
    return {
      userList: [],
    }
  },
  methods: {
    getUserInfo() {
      axios.get('/api/accounts/users/')
        .then(res => {
          this.userList = res.data
        })
    },
    deleteUser(user_id) {
      console.log(user_id)
    }
  },
  mounted() {
    this.getUserInfo()
  }
}
</script>
<style scoped>
  .main-container {
    width: 100%;
    height: 100%;
    display: flex;
    flex-wrap: wrap;
    overflow: scroll;
  }
  .card {
    width: 200px;
    height: 130px;
    border-radius: 5px;
    box-shadow: 0 0 10px lightgray;
    padding: 6px;
    margin: 12px;
  }
  .delete-user {
    color: #f1404b;
    font-size: 14px;
    font-weight: bold;
    float: right;
    margin-bottom: 4px;
    cursor: pointer;
  }
  .user-info {
    padding-top: 4px; 
    min-height: 90px;
    clear:both;
    overflow: scroll;
  }
  .user-info p:nth-child(2n+1) {
    font-size: 12px;
    font-weight: bold;
    color: #888;
  }
  .user-info p:nth-child(2n) {
    font-size: 16px;
    font-weight: bold;
    margin-left: 6px;
  }
</style>