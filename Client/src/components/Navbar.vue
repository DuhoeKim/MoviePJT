<template>
    <nav  class="navbar navbar-dark fixed-top scroll-up-down mb-2">
      <div class="container-fluid">
        <router-link class="navbar-brand scale text-white fs-1" :to="{ name: 'Home' }">Doce Cinema</router-link>
        <div class="d-flex me-auto ">
          <router-link class="nav-link active scale text-white fs-3" :to="{ name: 'Home' }" >Home</router-link>
          <router-link class="nav-link active scale text-white fs-3" :to="{ name: 'Community' }" >Community</router-link>
          <router-link class="nav-link active scale text-white fs-3" :to="{ name: 'ChoiceGame' }" >ChoiceGame</router-link>
        </div>
        <span v-if="!isLogin" class="d-flex text-decoration-none">
          <router-link class="nav-link active scale text-white fs-3" :to="{ name: 'Login' }">Login</router-link>
          <router-link class="nav-link active scale text-white fs-3" :to="{ name: 'Signup' }">Signup</router-link>
        </span>
        <span v-else class="d-flex">
          <router-link class="nav-link active scale text-white fs-3" :to="{ name: 'Profile' }">My</router-link>
          <span @click="logout" class="nav-link active logout scale text-white fs-3">Logout</span>
        </span>
      </div>
    </nav>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: "Navbar",
  methods:{
    logout() {
      this.$store.commit('DELETE_TOKEN')
      localStorage.removeItem('accessToken')
      this.$router.push({ name: 'Home'})
    },
  },
  computed:{
    ...mapGetters([
      'isLogin',
    ])
  }
}
</script>

<style>

</style>