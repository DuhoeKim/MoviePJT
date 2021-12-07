
<template>
  <div class="container d-flex flex-column justify-content-center p-5" style="height: 100vh;">
    <div class="ms-auto me-auto col-6 content p-5" >
    <h1 class="text-center">로그인</h1>
      <form @submit.prevent="login">
        <div class="mb-3">
          <label for="user-id" class="form-label">아이디</label>
          <input v-model="username" type="text" class="form-control p-2" id="user-id" autofocus autocomplete="off">
        </div>
        <div class="mb-3">
          <label for="user-password" class="form-label">비밀번호</label>
          <input v-model="password" type="password" class="form-control p-2" id="user-password">
        </div>
        <div class="d-flex justify-content-between">
          <button @click="goSignup" type="button" class="btn bg-custom text-white"> 회원가입 </button>
          <button type="submit" class="btn bg-custom text-white ">로그인</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios'
export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods:{
    goSignup() {
      this.$router.push({ name : "Signup"})
    },
    login(){
      const payload = {
        username: this.username,
        password: this.password
      }
      axios.post('http://localhost:8000/api/token/', payload)
        .then(response => {
          localStorage.setItem('accessToken', response.data.access)
          this.$store.commit('SET_TOKEN', response.data.access)
        })
        .catch(() => {
          alert('아이디/비밀번호를 다시 확인해주세요.')
          this.username = ''
          this.password = ''
        })
    }
  },
  computed:{
    ...mapGetters([
      'isLogin'
    ])
  },
  watch: {
    isLogin(){
      if(this.isLogin){
        if (this.$route.query.next){
          this.$router.push(JSON.parse(this.$route.query.next))
        } 
        else {
          this.$router.push({ name: 'Home'})
        }
      }
    }
  },
}
</script>

<style scoped>
  .content {
    background-color: rgb(39,42,66);
    border-radius: 20px;
    box-shadow: 20px 20px rgb(103,42,66);
  }
  .bg-custom{
    background: rgb(103,42,66);
  }
</style>
