<template>
  <div class="d-flex flex-column align-items-center mt-5 pt-5">
    <h1 class="text-center headline">영화 월드컵 32강</h1>
    <div v-if="!start" class="d-flex flex-column justify-content-center align-items-center" style="height: 70vh">
      <span> 영화 포스터만 보고 영화 골라! </span>
      <button v-if="!start" @click="startGame" class="btn btn-custom border-white text-white"> <span>시작하기</span> </button>  
    </div>

    <div v-else-if="randomMovies.length > 1" class="d-flex justify-content-between align-items-center">
      <div class="d-flex scale flex-column align-items-center m-5">
        <img @click="pick1" :src="imgURL1" alt="" width="600" height="900">
        <h1>{{randomMovies[nowIndex].title}}</h1>
      </div>

      <p>vs</p>
      
      <div class="d-flex flex-column align-items-center scale m-5">
        <img @click="pick2" :src="imgURL2" alt="" width="600" height="900">
        <h1>{{randomMovies[nowIndex+1].title}}</h1>
      </div>
    </div>

    <div v-else class="d-flex flex-column align-items-center">
      <h1> 최종 우승 </h1> 
      <img @click="goMovieDetail" class="scale" :src="imgURL1" alt="" width="600" height="900">
      <button @click="regame" class="mt-5 btn btn-custom border-white text-white"><span>다시하기</span> </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Test',
  data(){
    return{
      start: false,
      nowIndex: 0,
      imgURL1: '', 
      imgURL2: '',
      finalWinnerURL: '',
    }
  },
  methods: {
    startGame(){
      this.start = !this.start
      this.imgURL1 = `https://image.tmdb.org/t/p/original${this.randomMovies[this.nowIndex].poster_path}`
      this.imgURL2 = `https://image.tmdb.org/t/p/original${this.randomMovies[this.nowIndex+1].poster_path}`
    },
    pick1(){
      this.$store.dispatch('removeLoserMovie', this.nowIndex+1)
      this.nowIndex += 1
      if (this.nowIndex === this.randomMovies.length){
        this.nowIndex = 0
      }
      this.imgURL1 = `https://image.tmdb.org/t/p/original${this.randomMovies[this.nowIndex].poster_path}`
      this.imgURL2 = `https://image.tmdb.org/t/p/original${this.randomMovies[this.nowIndex+1].poster_path}`
    },
    pick2(){
      this.$store.dispatch('removeLoserMovie', this.nowIndex)
      this.nowIndex += 1
      if (this.nowIndex === this.randomMovies.length){
        this.nowIndex = 0
      }

      this.imgURL1 = `https://image.tmdb.org/t/p/original${this.randomMovies[this.nowIndex].poster_path}`
      this.imgURL2 = `https://image.tmdb.org/t/p/original${this.randomMovies[this.nowIndex+1].poster_path}`
    },
    regame() {
      this.$store.dispatch('startGame')
      this.start = !this.start
    },
    goMovieDetail() {
      this.$router.push({ name: "MovieDetail", query: {data : JSON.stringify({movieId: this.randomMovies[0].id})}})
      this.$store.dispatch('startGame')
      this.start = !this.start
    }
  },
  computed: {
    randomMovies(){
      return this.$store.state.randomMovies
    },
  },
}
</script>

<style scoped>
  .headline {
    font-size: 4rem;
  }
  p {
    font-size: 4rem;
  }
  span{
    font-size: 3rem;
  }
  img {
    border-radius: 5%;
  }
  .btn-custom {
    width: 15rem;
    height: 5rem;
    border-radius: 3%;
  }
</style>