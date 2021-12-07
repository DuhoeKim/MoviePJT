<template>
  <div id="app">
    <Navbar/>
    <router-view/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Navbar from '@/components/Navbar'
export default {
  name: 'App',
  components:{
    Navbar,
  },
  data(){
    return {
      nowScrollPosition: 0,
    }
  },
  methods: {
    logout() {
      this.$store.commit('DELETE_TOKEN')
      localStorage.removeItem('accessToken')
      this.$router.push({ name: 'Home'})
    },
    navbarUpDown(){
      const navbar = document.querySelector('.scroll-up-down')
      if(window.scrollY > this.nowScrollPosition){
        navbar.style.transform = 'translateY(-100px)'
        this.nowScrollPosition = window.scrollY
      } else {
        navbar.style.transform = 'translateY(0px)'
        this.nowScrollPosition = window.scrollY
      }
    },
  },
  computed: {
    ...mapGetters([
      'isLogin',
    ]),
    scrollPosition(){
      return window.scrollY
    }
  },
  created() {
    window.addEventListener('scroll', this.navbarUpDown)
    const accessToken = localStorage.getItem('accessToken') || ''
    this.$store.commit('SET_TOKEN', accessToken)
    this.$store.dispatch('getMovies')
  },
  beforeCreate () {
    document.querySelector('body').setAttribute('style', 'background: #181924')
  },

}
</script>


<style>
#app {
  font-family: 'IBM Plex Sans KR', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: white;
}
.scale {
  transform: scale(1);
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transition: all 0.3s ease-in-out;  
}
.scale:hover {
  cursor: pointer;
  z-index: 1;
  transform: scale(1.2);
  -webkit-transform: scale(1.1);
  -moz-transform: scale(1.1);
  -ms-transform: scale(1.1);
  -o-transform: scale(1.1);
}
button {
  transform: scale(1);
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transition: all 0.3s ease-in-out;  
}
button:hover {
  cursor: pointer;
  z-index: 1;
  transform: scale(1.2);
  -webkit-transform: scale(1.1);
  -moz-transform: scale(1.1);
  -ms-transform: scale(1.1);
  -o-transform: scale(1.1);
}
.scroll-up-down{
  transition: 0.15s ease-in-out;
}
.navbar {
  height: 70px;
}
.main{
  background: rgb(39,42,66);
  padding: 0rem 200px;
  padding-top: 5rem;
  height: 25rem;
}
.main h1{
  font-size: 4rem;
}
</style>
