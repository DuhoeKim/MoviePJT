<template>
  <div class="container d-flex flex-column justify-content-center p-5" style="height: 100vh;">
    <div class="ms-auto me-auto col-6 content p-5">
    <h1 class="text-center">회원가입</h1>
      <form @submit.prevent="signup">
        <div class="mb-3">
          <label for="user-id" class="form-label">아이디</label>
          <input v-model="username" type="text" class="form-control p-2" id="user-id" autofocus autocomplete="off">
        </div>
        <div class="mb-3">
          <label for="user-password" class="form-label">비밀번호</label>
          <input v-model="password" type="password" class="form-control p-2" id="user-password">
        </div>
        <div class="mb-3">
          <label for="user-password-confirm" class="form-label">비밀번호 확인</label>
          <input v-model="passwordConfirmation" type="password" class="form-control p-2" id="user-password-confirm">
        </div>
        <div class="d-flex justify-content-end">
          <button type="submit" class="btn bg-custom text-white">회원가입</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Signup',
  data() {
    return {
      username: '',
      password: '',
      passwordConfirmation:'',
    }
  },
  methods: {
    signup() {
      axios.post('http://localhost:8000/accounts/signup/',{
        username: this.username,
        password: this.password,
        password_confirmation: this.passwordConfirmation
      })
        .then(() => {
          alert('회원가입이 완료되었습니다.')
          this.$router.push({ name: 'Login'})
        })
        .catch(() => {
          alert('잘못된 양식입니다.')
          this.username = ''
          this.password = ''
          this.passwordConfirmation = ''
        })
    }
  }
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
